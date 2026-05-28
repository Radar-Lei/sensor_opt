#!/usr/bin/env python3
"""Generate current-best seed-level paired-margin diagnostics."""

from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15_METRICS = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2" / "combined" / "combined_metrics.csv"
STAGE16_REPLACEMENT = TRACE_RESULTS / "stage16_calibrated_trace_sweep" / "replacement_status" / "stage16_replacement_seed_level.csv"
OUT_POINTS = CURRENT_BEST / "trace_biopt_paired_margin_points.csv"
OUT_SUMMARY = CURRENT_BEST / "trace_biopt_paired_margin_summary.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_paired_margins.pdf"

DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
SOURCE_LABEL = {
    "stage15_main": "Stage15 main evidence",
    "stage16_replaceable": "Stage16 calibrated rerun",
}
BASELINE_LABEL = {
    "validation_swap_selected": "Prev. TRACE-SL",
    "swap_from_greedy_a_trace": "Swap from A-trace",
    "rcss_selected": "RCSS",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def stage15_lookup() -> dict[tuple[str, float, str, int], dict[str, str]]:
    rows = load_csv(STAGE15_METRICS)
    lookup: dict[tuple[str, float, str, int], dict[str, str]] = {}
    for row in rows:
        if row["method"] != "gls_map":
            continue
        key = (
            row["dataset"],
            float(row["budget"]),
            row["layout_type"],
            int(row["split_seed"]),
        )
        lookup[key] = row
    return lookup


def build_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    current_rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    stage15 = stage15_lookup()
    replacement_rows = load_csv(STAGE16_REPLACEMENT)
    replacement_lookup: dict[tuple[str, float, str, int], dict[str, str]] = {}
    for row in replacement_rows:
        replacement_lookup[(
            row["dataset"],
            float(row["budget"]),
            row["stage16_root"],
            int(row["split_seed"]),
        )] = row

    point_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for current in sorted(current_rows, key=lambda row: (DATASETS.index(row["dataset"]), float(row["budget"]))):
        dataset = current["dataset"]
        budget = float(current["budget"])
        budget_pct = int(round(budget * 100))
        evidence_source = current["evidence_source"]
        source_mode = "stage16_replaceable" if evidence_source.startswith("stage16_replaceable:") else evidence_source
        source_label = SOURCE_LABEL[source_mode]
        best_layout = current["best_baseline_layout"]
        best_label = BASELINE_LABEL.get(best_layout, best_layout.replace("_", " "))
        deltas: list[float] = []

        for split_seed in range(25, 35):
            if evidence_source == "stage15_main":
                trace_row = stage15[(dataset, budget, "trace_biopt", split_seed)]
                trace_mae = float(trace_row["mae"])
            else:
                stage16_root = evidence_source.split(":", 1)[1]
                trace_row = replacement_lookup[(dataset, budget, stage16_root, split_seed)]
                trace_mae = float(trace_row["stage16_trace_mae"])
            baseline_row = stage15[(dataset, budget, best_layout, split_seed)]
            baseline_mae = float(baseline_row["mae"])
            paired_margin = trace_mae - baseline_mae
            deltas.append(paired_margin)
            point_rows.append(
                {
                    "dataset": dataset,
                    "budget": budget,
                    "budget_pct": budget_pct,
                    "split_seed": split_seed,
                    "evidence_source": evidence_source,
                    "source_label": source_label,
                    "best_baseline_layout": best_layout,
                    "best_baseline_label": best_label,
                    "trace_biopt_mae": trace_mae,
                    "best_baseline_mae": baseline_mae,
                    "paired_margin": paired_margin,
                }
            )

        summary_rows.append(
            {
                "dataset": dataset,
                "budget": budget,
                "budget_pct": budget_pct,
                "evidence_source": evidence_source,
                "source_label": source_label,
                "best_baseline_layout": best_layout,
                "best_baseline_label": best_label,
                "mean_paired_margin": mean(deltas),
                "min_paired_margin": min(deltas),
                "max_paired_margin": max(deltas),
                "win_count": sum(delta < 0.0 for delta in deltas),
                "count": len(deltas),
            }
        )

    return point_rows, summary_rows


def render_figure(point_rows: list[dict[str, object]], summary_rows: list[dict[str, object]]) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.6), sharey=True, constrained_layout=True)
    source_color = {
        "Stage15 main evidence": "#6b7280",
        "Stage16 calibrated rerun": "#1f77b4",
    }
    offsets = [-0.18, -0.14, -0.10, -0.06, -0.02, 0.02, 0.06, 0.10, 0.14, 0.18]

    grouped_points: dict[str, list[dict[str, object]]] = {dataset: [] for dataset in DATASETS}
    grouped_summary: dict[str, list[dict[str, object]]] = {dataset: [] for dataset in DATASETS}
    for row in point_rows:
        grouped_points[row["dataset"]].append(row)
    for row in summary_rows:
        grouped_summary[row["dataset"]].append(row)

    for ax, dataset in zip(axes, DATASETS):
        ax.axhline(0.0, color="#b91c1c", linewidth=1.0, linestyle="--", alpha=0.7)
        dataset_points = sorted(grouped_points[dataset], key=lambda row: (float(row["budget"]), int(row["split_seed"])))
        dataset_summary = sorted(grouped_summary[dataset], key=lambda row: float(row["budget"]))
        for budget_index, budget_pct in enumerate([10, 20, 30], start=1):
            subset = [row for row in dataset_points if int(row["budget_pct"]) == budget_pct]
            xs = [budget_index + offsets[index] for index in range(len(subset))]
            ys = [float(row["paired_margin"]) for row in subset]
            color = source_color[subset[0]["source_label"]]
            ax.scatter(xs, ys, s=26, color=color, alpha=0.85, edgecolor="white", linewidth=0.4, zorder=3)

        for budget_index, row in enumerate(dataset_summary, start=1):
            ax.scatter(
                [budget_index],
                [float(row["mean_paired_margin"])],
                s=70,
                marker="D",
                color="black",
                edgecolor="white",
                linewidth=0.6,
                zorder=4,
            )

        ax.set_title(dataset, fontsize=10)
        ax.set_xticks([1, 2, 3], ["10", "20", "30"])
        ax.set_xlabel("Budget (%)")
        ax.grid(True, axis="y", alpha=0.25)
        ax.set_ylim(-0.34, 0.03)

    axes[0].set_ylabel("TRACE-BiOpt - strongest baseline MAE")
    handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=source_color["Stage15 main evidence"], markersize=6, label="Stage15 main evidence"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=source_color["Stage16 calibrated rerun"], markersize=6, label="Stage16 calibrated rerun"),
        plt.Line2D([0], [0], marker="D", color="w", markerfacecolor="black", markersize=7, label="Row mean"),
    ]
    fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.06))
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    point_rows, summary_rows = build_rows()
    write_csv(
        OUT_POINTS,
        point_rows,
        [
            "dataset",
            "budget",
            "budget_pct",
            "split_seed",
            "evidence_source",
            "source_label",
            "best_baseline_layout",
            "best_baseline_label",
            "trace_biopt_mae",
            "best_baseline_mae",
            "paired_margin",
        ],
    )
    write_csv(
        OUT_SUMMARY,
        summary_rows,
        [
            "dataset",
            "budget",
            "budget_pct",
            "evidence_source",
            "source_label",
            "best_baseline_layout",
            "best_baseline_label",
            "mean_paired_margin",
            "min_paired_margin",
            "max_paired_margin",
            "win_count",
            "count",
        ],
    )
    render_figure(point_rows, summary_rows)
    print(f"Wrote {OUT_FIG}, {OUT_POINTS}, and {OUT_SUMMARY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
