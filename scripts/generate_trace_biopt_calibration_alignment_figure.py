#!/usr/bin/env python3
"""Generate validation-calibration and posterior-trace alignment figure."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from scipy import stats


ROOT = Path(__file__).resolve().parents[1]
STAGE15 = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined"
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_POINTS = CURRENT_BEST / "trace_biopt_calibration_alignment_points.csv"
OUT_SUMMARY = CURRENT_BEST / "trace_biopt_calibration_alignment_summary.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_calibration_alignment.pdf"

LAYOUT_LABELS = {
    "trace_biopt": "TRACE-BiOpt",
    "validation_swap_selected": "Prev. TRACE-SL",
    "multistart_swap_by_validation": "Multistart swap",
    "rcss_selected": "RCSS",
    "best_random_by_validation": "Best random",
}
COLORS = {
    "trace_biopt": "#1f77b4",
    "validation_swap_selected": "#d62728",
    "multistart_swap_by_validation": "#2ca02c",
    "rcss_selected": "#9467bd",
    "best_random_by_validation": "#ff7f0e",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def fmt(value: float) -> str:
    return f"{value:.6f}"


def main() -> int:
    rows = [
        row for row in load_csv(STAGE15 / "combined_metrics.csv")
        if row["method"] == "gls_map"
        and row["robustness_family"] == "baseline"
        and row["robustness_condition"] == "baseline"
        and row["validation_selected_mae"].strip()
        and row["posterior_trace"].strip()
        and row["layout_type"] in LAYOUT_LABELS
    ]
    summary_rows = load_csv(STAGE15 / "certificate_correlation_summary.csv")
    gls_summary = {
        row["certificate"]: row
        for row in summary_rows
        if row["method"] == "gls_map"
    }

    point_rows = []
    for row in rows:
        point_rows.append(
            {
                "dataset": row["dataset"],
                "budget": row["budget"],
                "split_seed": row["split_seed"],
                "layout_type": row["layout_type"],
                "layout_label": LAYOUT_LABELS[row["layout_type"]],
                "validation_selected_mae": row["validation_selected_mae"],
                "heldout_mae": row["mae"],
                "posterior_trace": row["posterior_trace"],
            }
        )

    with OUT_POINTS.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "dataset",
                "budget",
                "split_seed",
                "layout_type",
                "layout_label",
                "validation_selected_mae",
                "heldout_mae",
                "posterior_trace",
            ],
        )
        writer.writeheader()
        writer.writerows(point_rows)

    validation_x = [float(row["validation_selected_mae"]) for row in point_rows]
    heldout_y = [float(row["heldout_mae"]) for row in point_rows]
    posterior_x = [float(row["posterior_trace"]) for row in point_rows]
    validation_pearson = stats.pearsonr(validation_x, heldout_y)
    validation_spearman = stats.spearmanr(validation_x, heldout_y)
    posterior_pearson = stats.pearsonr(posterior_x, heldout_y)
    posterior_spearman = stats.spearmanr(posterior_x, heldout_y)

    summary_out = [
        {
            "scope": "selected_layout_rows",
            "metric_x": "validation_selected_mae",
            "metric_y": "heldout_mae",
            "statistic": "pearson",
            "value": fmt(validation_pearson.statistic),
            "n": str(len(point_rows)),
        },
        {
            "scope": "selected_layout_rows",
            "metric_x": "validation_selected_mae",
            "metric_y": "heldout_mae",
            "statistic": "spearman",
            "value": fmt(validation_spearman.statistic),
            "n": str(len(point_rows)),
        },
        {
            "scope": "selected_layout_rows",
            "metric_x": "posterior_trace",
            "metric_y": "heldout_mae",
            "statistic": "pearson",
            "value": fmt(posterior_pearson.statistic),
            "n": str(len(point_rows)),
        },
        {
            "scope": "selected_layout_rows",
            "metric_x": "posterior_trace",
            "metric_y": "heldout_mae",
            "statistic": "spearman",
            "value": fmt(posterior_spearman.statistic),
            "n": str(len(point_rows)),
        },
        {
            "scope": "full_layout_seedwise_summary",
            "metric_x": "posterior_trace",
            "metric_y": "heldout_mae",
            "statistic": "spearman_mean",
            "value": gls_summary["posterior_trace"]["spearman_mae_mean"],
            "n": gls_summary["posterior_trace"]["spearman_mae_count"],
        },
    ]

    for layout_type in sorted(LAYOUT_LABELS):
        layout_rows = [row for row in point_rows if row["layout_type"] == layout_type]
        val = [float(row["validation_selected_mae"]) for row in layout_rows]
        mae = [float(row["heldout_mae"]) for row in layout_rows]
        post = [float(row["posterior_trace"]) for row in layout_rows]
        summary_out.extend(
            [
                {
                    "scope": f"layout_type:{layout_type}",
                    "metric_x": "validation_selected_mae",
                    "metric_y": "heldout_mae",
                    "statistic": "spearman",
                    "value": fmt(stats.spearmanr(val, mae).statistic),
                    "n": str(len(layout_rows)),
                },
                {
                    "scope": f"layout_type:{layout_type}",
                    "metric_x": "posterior_trace",
                    "metric_y": "heldout_mae",
                    "statistic": "spearman",
                    "value": fmt(stats.spearmanr(post, mae).statistic),
                    "n": str(len(layout_rows)),
                },
                {
                    "scope": f"layout_type:{layout_type}",
                    "metric_x": "test_minus_validation",
                    "metric_y": "heldout_mae",
                    "statistic": "mean_gap",
                    "value": fmt(sum(m - v for m, v in zip(mae, val)) / len(layout_rows)),
                    "n": str(len(layout_rows)),
                },
            ]
        )

    with OUT_SUMMARY.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["scope", "metric_x", "metric_y", "statistic", "value", "n"],
        )
        writer.writeheader()
        writer.writerows(summary_out)

    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.6))
    fig.subplots_adjust(top=0.82, bottom=0.14, left=0.08, right=0.97, wspace=0.28)
    panels = [
        ("validation_selected_mae", "Validation-selected MAE", axes[0], validation_spearman.statistic),
        ("posterior_trace", "Posterior trace", axes[1], posterior_spearman.statistic),
    ]
    for metric_key, xlabel, ax, rho in panels:
        for layout_type in LAYOUT_LABELS:
            layout_rows = [row for row in point_rows if row["layout_type"] == layout_type]
            xvals = [float(row[metric_key]) for row in layout_rows]
            yvals = [float(row["heldout_mae"]) for row in layout_rows]
            ax.scatter(
                xvals,
                yvals,
                s=20,
                alpha=0.72,
                color=COLORS[layout_type],
                label=LAYOUT_LABELS[layout_type],
                edgecolors="none",
            )
        ax.set_xlabel(xlabel)
        ax.grid(True, alpha=0.22)
        ax.text(
            0.03,
            0.95,
            r"Spearman $\rho=$" + f"{rho:.3f}",
            transform=ax.transAxes,
            va="top",
            ha="left",
            fontsize=8,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.8),
        )
    axes[0].set_ylabel("Held-out GLS/MAP MAE")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.98))
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT_FIG}, {OUT_POINTS}, and {OUT_SUMMARY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
