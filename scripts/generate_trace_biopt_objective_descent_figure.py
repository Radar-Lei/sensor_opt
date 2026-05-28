#!/usr/bin/env python3
"""Generate current-best TRACE-BiOpt objective-descent diagnostics."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
STAGE16_SWEEP = TRACE_RESULTS / "stage16_calibrated_trace_sweep"
STAGE16_PROBE = TRACE_RESULTS / "stage16_calibrated_trace_probe"
PEMS228_PROBE = TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe"

OUT_SUMMARY = CURRENT_BEST / "trace_biopt_objective_descent_summary.csv"
OUT_CURVES = CURRENT_BEST / "trace_biopt_objective_descent_curves.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_objective_descent.pdf"

DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
BUDGETS = [0.1, 0.2, 0.3]
DATASET_DIR = {
    "PeMS7_1026": "pems7_1026",
    "PeMS7_228": "pems7_228",
    "Seattle": "seattle",
}
SOURCE_ROOTS = [STAGE16_SWEEP, STAGE16_PROBE, PEMS228_PROBE]
SOURCE_LABEL = {"stage15_main": "Stage15 main evidence"}
SOURCE_MARKER = {
    "Stage15 main evidence": "o",
    "Stage16 calibrated rerun": "s",
}
BUDGET_COLOR = {
    0.1: "#1f77b4",
    0.2: "#ff7f0e",
    0.3: "#2ca02c",
}
GRID = np.linspace(0.0, 1.0, 21)


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_seed_dir(dataset: str, split_seed: int, evidence_source: str) -> tuple[Path, str]:
    if evidence_source == "stage15_main":
        return STAGE15 / DATASET_DIR[dataset] / f"seed_{split_seed}", "stage15_main"
    if evidence_source.startswith("stage16_replaceable:"):
        root_name = evidence_source.split(":", 1)[1]
        for base in SOURCE_ROOTS:
            candidate = base / root_name / f"seed_{split_seed}"
            if candidate.exists():
                return candidate, root_name
        raise FileNotFoundError(f"unable to resolve source root for {dataset} seed {split_seed}: {evidence_source}")
    raise ValueError(f"unsupported evidence source: {evidence_source}")


def history_entry(seed_dir: Path, dataset: str, budget: float) -> dict[str, object]:
    rows = load_json(seed_dir / "trace_biopt_history.json")
    return next(
        row for row in rows
        if row["dataset"] == dataset and abs(float(row["budget"]) - budget) < 1e-9
    )


def accepted_steps(entry: dict[str, object]) -> list[dict[str, object]]:
    return [
        step for step in entry["history"]
        if step["stage"] in {"warm_start", "forward", "exchange"}
    ]


def normalized_gap_curve(steps: list[dict[str, object]]) -> tuple[list[float], list[float]]:
    objectives = [float(step["objective"]) for step in steps]
    if len(objectives) == 1:
        return list(GRID), [0.0 for _ in GRID]
    xs = np.linspace(0.0, 1.0, len(objectives))
    start = objectives[0]
    final = objectives[-1]
    denom = start - final
    if abs(denom) < 1e-12:
        ys = np.zeros(len(objectives))
    else:
        ys = np.array([(obj - final) / denom for obj in objectives], dtype=float)
    interp = np.interp(GRID, xs, ys)
    return list(GRID), [float(value) for value in interp]


def stage_mode(steps: list[dict[str, object]]) -> str:
    stages = [str(step["stage"]) for step in steps]
    if stages and all(stage == "exchange" for stage in stages):
        return "exchange_only_warm_start"
    if "exchange" in stages:
        return "forward_then_exchange"
    return "forward_only"


def seed_records() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    current_best_rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    summary_records: list[dict[str, object]] = []
    curve_records: list[dict[str, object]] = []
    for row in current_best_rows:
        dataset = row["dataset"]
        budget = float(row["budget"])
        evidence_source = row["evidence_source"]
        total_drop_pct = []
        exchange_share_pct = []
        forward_steps = []
        exchange_steps = []
        modes = []
        for split_seed in range(25, 35):
            seed_dir, source_root = resolve_seed_dir(dataset, split_seed, evidence_source)
            entry = history_entry(seed_dir, dataset, budget)
            steps = accepted_steps(entry)
            objectives = [float(step["objective"]) for step in steps]
            start = objectives[0]
            final = objectives[-1]
            total_drop = 0.0 if abs(start) < 1e-12 else 100.0 * (start - final) / start
            non_exchange = [float(step["objective"]) for step in steps if step["stage"] in {"warm_start", "forward"}]
            if non_exchange:
                pre_exchange = non_exchange[-1]
                exchange_share = 0.0 if abs(start - final) < 1e-12 else 100.0 * (pre_exchange - final) / (start - final)
            else:
                exchange_share = 100.0 if abs(start - final) >= 1e-12 else 0.0
            total_drop_pct.append(total_drop)
            exchange_share_pct.append(exchange_share)
            forward_steps.append(sum(step["stage"] in {"warm_start", "forward"} for step in steps))
            exchange_steps.append(sum(step["stage"] == "exchange" for step in steps))
            modes.append(stage_mode(steps))
            fractions, gaps = normalized_gap_curve(steps)
            for fraction, gap in zip(fractions, gaps):
                curve_records.append(
                    {
                        "dataset": dataset,
                        "budget": budget,
                        "budget_pct": int(round(budget * 100)),
                        "split_seed": split_seed,
                        "evidence_source": evidence_source,
                        "source_label": SOURCE_LABEL.get(source_root, "Stage16 calibrated rerun"),
                        "progress_fraction": f"{fraction:.2f}",
                        "normalized_gap": f"{gap:.6f}",
                    }
                )
        dominant_mode = Counter(modes).most_common(1)[0][0]
        summary_records.append(
            {
                "dataset": dataset,
                "budget": budget,
                "budget_pct": int(round(budget * 100)),
                "evidence_source": evidence_source,
                "source_label": SOURCE_LABEL.get(
                    evidence_source if evidence_source == "stage15_main" else evidence_source.split(":", 1)[1],
                    "Stage16 calibrated rerun",
                ),
                "dominant_stage_mode": dominant_mode,
                "runs": 10,
                "mean_total_drop_pct": f"{mean(total_drop_pct):.6f}",
                "mean_exchange_share_pct": f"{mean(exchange_share_pct):.6f}",
                "mean_forward_like_steps": f"{mean(forward_steps):.6f}",
                "mean_exchange_steps": f"{mean(exchange_steps):.6f}",
            }
        )
    return summary_records, curve_records


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    summary_records, curve_records = seed_records()
    write_csv(OUT_SUMMARY, summary_records, list(summary_records[0].keys()))
    write_csv(OUT_CURVES, curve_records, list(curve_records[0].keys()))

    grouped_curve: dict[tuple[str, float], list[dict[str, object]]] = defaultdict(list)
    for row in curve_records:
        grouped_curve[(str(row["dataset"]), float(row["budget"]))].append(row)
    summary_lookup = {
        (str(row["dataset"]), float(row["budget"])): row
        for row in summary_records
    }

    fig, axes = plt.subplots(
        2,
        3,
        figsize=(11.2, 5.8),
        gridspec_kw={"height_ratios": [2.2, 1.2]},
        constrained_layout=True,
    )

    for col, dataset in enumerate(DATASETS):
        top_ax = axes[0, col]
        bottom_ax = axes[1, col]
        for budget in BUDGETS:
            rows = grouped_curve[(dataset, budget)]
            mean_curve = []
            for fraction in GRID:
                values = [
                    float(row["normalized_gap"])
                    for row in rows
                    if abs(float(row["progress_fraction"]) - fraction) < 1e-9
                ]
                mean_curve.append(mean(values))
            source_label = summary_lookup[(dataset, budget)]["source_label"]
            top_ax.plot(
                GRID,
                mean_curve,
                color=BUDGET_COLOR[budget],
                linewidth=2.0,
                marker=SOURCE_MARKER[source_label],
                markersize=3.5,
                markevery=5,
                label=f"{int(round(budget * 100))}%",
            )

        top_ax.set_title(dataset, fontsize=10)
        top_ax.set_xlim(0.0, 1.0)
        top_ax.set_ylim(-0.02, 1.02)
        top_ax.grid(True, alpha=0.22)
        top_ax.set_xticks([0.0, 0.5, 1.0])
        if col == 0:
            top_ax.set_ylabel("Relative objective gap")
        top_ax.set_xlabel("Accepted-update progress")

        xs = np.arange(len(BUDGETS))
        forwards = [float(summary_lookup[(dataset, budget)]["mean_forward_like_steps"]) for budget in BUDGETS]
        exchanges = [float(summary_lookup[(dataset, budget)]["mean_exchange_steps"]) for budget in BUDGETS]
        bars_forward = bottom_ax.bar(xs, forwards, width=0.62, color="#9ecae1", label="Forward/warm start")
        bars_exchange = bottom_ax.bar(xs, exchanges, width=0.62, bottom=forwards, color="#fdae6b", label="Exchange")
        bottom_ax.set_xticks(xs, [f"{int(round(budget * 100))}%" for budget in BUDGETS])
        bottom_ax.set_xlabel("Budget")
        bottom_ax.grid(True, axis="y", alpha=0.22)
        if col == 0:
            bottom_ax.set_ylabel("Accepted steps")
        for idx, budget in enumerate(BUDGETS):
            mode = summary_lookup[(dataset, budget)]["dominant_stage_mode"]
            bottom_ax.text(
                idx,
                forwards[idx] + exchanges[idx] + 1.0,
                "exchange-only" if mode == "exchange_only_warm_start" else "forward+exchange",
                ha="center",
                va="bottom",
                fontsize=6.5,
                rotation=0,
            )

    line_handles, line_labels = axes[0, 0].get_legend_handles_labels()
    bar_handles = [bars_forward[0], bars_exchange[0]]
    bar_labels = ["Forward/warm start", "Exchange"]
    fig.legend(
        line_handles + bar_handles,
        line_labels + bar_labels,
        loc="upper center",
        ncol=5,
        frameon=False,
        bbox_to_anchor=(0.5, 1.03),
    )

    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT_FIG}, {OUT_SUMMARY}, and {OUT_CURVES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
