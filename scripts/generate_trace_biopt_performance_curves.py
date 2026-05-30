#!/usr/bin/env python3
"""Generate current-best TRACE-BiOpt performance curves for the paper."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_performance_curves.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_current_best_curves.pdf"

DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
TITLE_MAP = {
    "PeMS7_1026": "PeMS7_1026",
    "PeMS7_228": "PeMS7_228",
    "Seattle": "Seattle",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def short_baseline_label(layout: str) -> str:
    mapping = {
        "validation_swap_selected": "Prev. TRACE-SL",
        "swap_from_greedy_a_trace": "Swap from A-trace",
        "rcss_selected": "RCSS",
    }
    return mapping.get(layout, layout.replace("_", " "))


def main() -> int:
    rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    filtered = sorted(
        [
            row for row in rows
            if row["robustness_family"] == "baseline" and row["robustness_condition"] == "baseline"
        ],
        key=lambda row: (DATASETS.index(row["dataset"]), float(row["budget"])),
    )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "dataset",
                "budget",
                "budget_pct",
                "trace_biopt_mean",
                "best_baseline_mean",
                "best_baseline_layout",
                "best_baseline_label",
                "trace_minus_best_baseline",
                "evidence_source",
            ],
        )
        writer.writeheader()
        for row in filtered:
            writer.writerow(
                {
                    "dataset": row["dataset"],
                    "budget": row["budget"],
                    "budget_pct": str(int(round(float(row["budget"]) * 100))),
                    "trace_biopt_mean": row["trace_biopt_mean"],
                    "best_baseline_mean": row["best_baseline_mean"],
                    "best_baseline_layout": row["best_baseline_layout"],
                    "best_baseline_label": short_baseline_label(row["best_baseline_layout"]),
                    "trace_minus_best_baseline": row["trace_minus_best_baseline"],
                    "evidence_source": row["evidence_source"],
                }
            )

    grouped = {dataset: [] for dataset in DATASETS}
    for row in filtered:
        grouped[row["dataset"]].append(row)

    fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.5), sharey=False, constrained_layout=True)
    trace_color = "#1f77b4"
    baseline_color = "#d62728"

    for col, (ax, dataset) in enumerate(zip(axes, DATASETS)):
        dataset_rows = grouped[dataset]
        xs = [int(round(float(row["budget"]) * 100)) for row in dataset_rows]
        trace = [float(row["trace_biopt_mean"]) for row in dataset_rows]
        best = [float(row["best_baseline_mean"]) for row in dataset_rows]
        labels = [short_baseline_label(row["best_baseline_layout"]) for row in dataset_rows]

        ax.plot(xs, trace, marker="o", linewidth=2.2, color=trace_color, label="TRACE-BiOpt")
        ax.plot(xs, best, marker="s", linewidth=1.8, linestyle="--", color=baseline_color, label="Best non-BiOpt baseline")
        ax.fill_between(xs, trace, best, where=[t <= b for t, b in zip(trace, best)], color=trace_color, alpha=0.08)
        ax.set_title(TITLE_MAP[dataset], fontsize=10)
        ax.set_xlabel("Budget (%)")
        ax.set_xticks([10, 20, 30])
        ax.grid(True, axis="y", alpha=0.25)
        if col > 0:
            ax.tick_params(labelleft=False)
        ymin = min(trace + best)
        ymax = max(trace + best)
        pad = max(0.04, (ymax - ymin) * 0.18)
        ax.set_ylim(ymin - pad * 0.6, ymax + pad)
        for x, y, label in zip(xs, best, labels):
            ax.annotate(
                label,
                (x, y),
                xytext=(0, 8),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=7,
                color=baseline_color,
            )

    axes[0].set_ylabel("Held-out GLS/MAP MAE")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.06))
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT_FIG} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
