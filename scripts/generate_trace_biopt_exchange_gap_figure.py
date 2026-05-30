#!/usr/bin/env python3
"""Generate current-best TRACE-BiOpt exchange-gap posture diagnostics."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
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

OUT_SUMMARY = CURRENT_BEST / "trace_biopt_exchange_gap_summary.csv"
OUT_CURVES = CURRENT_BEST / "trace_biopt_exchange_gap_curves.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_exchange_gap_curves.pdf"

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
        raise FileNotFoundError(
            f"unable to resolve source root for {dataset} seed {split_seed}: {evidence_source}"
        )
    raise ValueError(f"unsupported evidence source: {evidence_source}")


def history_entry(seed_dir: Path, dataset: str, budget: float) -> dict[str, object]:
    rows = load_json(seed_dir / "trace_biopt_history.json")
    return next(
        row for row in rows
        if row["dataset"] == dataset and abs(float(row["budget"]) - budget) < 1e-9
    )


def exchange_objectives(entry: dict[str, object]) -> list[float]:
    return [
        float(step["objective"])
        for step in entry["history"]
        if step["stage"] == "exchange"
    ]


def residual_exchange_curve(objectives: list[float]) -> tuple[list[float], list[float]]:
    if len(objectives) == 1:
        return list(GRID), [float(np.interp(value, [0.0, 1.0], [1.0, 0.0])) for value in GRID]
    xs = np.linspace(0.0, 1.0, len(objectives))
    start = objectives[0]
    final = objectives[-1]
    denom = start - final
    if abs(denom) < 1e-12:
        ys = np.zeros(len(objectives))
    else:
        ys = np.array([(objective - final) / denom for objective in objectives], dtype=float)
    interp = np.interp(GRID, xs, ys)
    return list(GRID), [float(value) for value in interp]


def seed_records() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    current_best_rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    summary_records: list[dict[str, object]] = []
    curve_records: list[dict[str, object]] = []
    for row in current_best_rows:
        dataset = row["dataset"]
        budget = float(row["budget"])
        evidence_source = row["evidence_source"]
        source_label = SOURCE_LABEL.get(
            evidence_source if evidence_source == "stage15_main" else evidence_source.split(":", 1)[1],
            "Stage16 calibrated rerun",
        )
        exchange_steps = []
        zero_exchange_runs = 0
        residual_25 = []
        residual_50 = []
        residual_75 = []
        for split_seed in range(25, 35):
            seed_dir, _ = resolve_seed_dir(dataset, split_seed, evidence_source)
            entry = history_entry(seed_dir, dataset, budget)
            objectives = exchange_objectives(entry)
            if not objectives:
                zero_exchange_runs += 1
                continue
            exchange_steps.append(len(objectives))
            fractions, gaps = residual_exchange_curve(objectives)
            residual_25.append(float(np.interp(0.25, fractions, gaps)))
            residual_50.append(float(np.interp(0.50, fractions, gaps)))
            residual_75.append(float(np.interp(0.75, fractions, gaps)))
            for fraction, gap in zip(fractions, gaps):
                curve_records.append(
                    {
                        "dataset": dataset,
                        "budget": budget,
                        "budget_pct": int(round(budget * 100)),
                        "split_seed": split_seed,
                        "evidence_source": evidence_source,
                        "source_label": source_label,
                        "progress_fraction": f"{fraction:.2f}",
                        "residual_exchange_gap": f"{gap:.6f}",
                    }
                )
        summary_records.append(
            {
                "dataset": dataset,
                "budget": budget,
                "budget_pct": int(round(budget * 100)),
                "evidence_source": evidence_source,
                "source_label": source_label,
                "runs": 10,
                "runs_with_exchange": len(exchange_steps),
                "zero_exchange_runs": zero_exchange_runs,
                "mean_exchange_steps": f"{mean(exchange_steps) if exchange_steps else 0.0:.6f}",
                "mean_residual_gap_25pct": f"{mean(residual_25) if residual_25 else 0.0:.6f}",
                "mean_residual_gap_50pct": f"{mean(residual_50) if residual_50 else 0.0:.6f}",
                "mean_residual_gap_75pct": f"{mean(residual_75) if residual_75 else 0.0:.6f}",
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
        gridspec_kw={"height_ratios": [2.2, 1.25]},
        constrained_layout=True,
    )

    for col, dataset in enumerate(DATASETS):
        top_ax = axes[0, col]
        bottom_ax = axes[1, col]
        for budget in BUDGETS:
            rows = grouped_curve.get((dataset, budget), [])
            if not rows:
                continue
            mean_curve = []
            for fraction in GRID:
                values = [
                    float(row["residual_exchange_gap"])
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
            top_ax.set_ylabel("Residual exchange gap")
        top_ax.set_xlabel("Accepted exchange progress")

        xs = np.arange(len(BUDGETS))
        exchange_steps = [
            float(summary_lookup[(dataset, budget)]["mean_exchange_steps"])
            for budget in BUDGETS
        ]
        zero_runs = [
            int(summary_lookup[(dataset, budget)]["zero_exchange_runs"])
            for budget in BUDGETS
        ]
        bars = bottom_ax.bar(xs, exchange_steps, width=0.62, color="#9ecae1")
        bottom_ax.set_xticks(xs, [f"{int(round(budget * 100))}%" for budget in BUDGETS])
        bottom_ax.set_xlabel("Budget")
        bottom_ax.grid(True, axis="y", alpha=0.22)
        if col == 0:
            bottom_ax.set_ylabel("Mean accepted exchanges")
    line_handles, line_labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(
        line_handles,
        line_labels,
        loc="lower center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, -0.02),
    )

    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT_FIG}, {OUT_SUMMARY}, and {OUT_CURVES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
