#!/usr/bin/env python3
"""Generate a reviewer-facing current-best full-baseline heatmap figure."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
SOURCE_CSV = CURRENT_BEST / "trace_biopt_full_baseline_matrix.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_full_baseline_heatmap.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_full_baseline_heatmap.pdf"

DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
BUDGET_SUFFIXES = [("10", "10%"), ("20", "20%"), ("30", "30%")]
LABELS = {
    "trace_biopt": "TRACE-BiOpt",
    "validation_swap_selected": "Prev. TRACE-SL",
    "rcss_selected": "RCSS",
    "multistart_swap_by_validation": "Multistart swap",
    "swap_from_greedy_a_trace": "Swap-A",
    "greedy_a_trace": "Greedy A-trace",
    "greedy_d_logdet": "Greedy D-logdet",
    "scenario_average_a_trace": "Avg-scenario A",
    "scenario_cvar_a_trace": "CVaR-scenario A",
    "graph_sampling_laplacian": "Graph-spectral",
    "qr_pod_modes": "QR/POD",
    "observability_proxy": "Observability",
    "top_variance": "Top variance",
    "coverage": "Coverage",
    "degree": "Degree",
    "random": "Random",
    "best_random_by_validation": "Best random (val)",
    "best_random_by_trace": "Best random (trace)",
    "swap_from_best_random_trace": "Swap-random",
    "swap_from_scenario_average": "Swap-avg-scen",
    "swap_from_scenario_cvar": "Swap-CVaR-scen",
    "robust_coverage_cvar": "Robust coverage",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def nice_label(layout_type: str) -> str:
    return LABELS.get(layout_type, layout_type.replace("_", " "))


def write_long_csv(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    long_rows: list[dict[str, str]] = []
    for row in rows:
        trace_means = {
            suffix: float(next(r[f"mean_{suffix}"] for r in rows if r["dataset"] == row["dataset"] and r["layout_type"] == "trace_biopt"))
            for suffix, _ in BUDGET_SUFFIXES
        }
        for suffix, budget_label in BUDGET_SUFFIXES:
            mean_value = float(row[f"mean_{suffix}"])
            rank_value = int(row[f"rank_{suffix}"])
            long_rows.append(
                {
                    "dataset": row["dataset"],
                    "layout_type": row["layout_type"],
                    "layout_label": nice_label(row["layout_type"]),
                    "budget_pct": budget_label.rstrip("%"),
                    "mean_mae": f"{mean_value:.10f}",
                    "rank": str(rank_value),
                    "trace_gap": f"{(mean_value - trace_means[suffix]):.10f}",
                    "avg_rank": row["avg_rank"],
                }
            )
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["dataset", "layout_type", "layout_label", "budget_pct", "mean_mae", "rank", "trace_gap", "avg_rank"],
        )
        writer.writeheader()
        writer.writerows(long_rows)
    return long_rows


def main() -> int:
    rows = load_csv(SOURCE_CSV)
    long_rows = write_long_csv(rows)

    dataset_rows = {dataset: [row for row in rows if row["dataset"] == dataset] for dataset in DATASETS}
    max_gap = max(float(row["trace_gap"]) for row in long_rows)
    min_gap = min(float(row["trace_gap"]) for row in long_rows)
    if min_gap < 0.0 < max_gap:
        norm = colors.TwoSlopeNorm(vmin=min_gap, vcenter=0.0, vmax=max_gap)
    else:
        norm = colors.Normalize(vmin=min_gap, vmax=max_gap if max_gap > min_gap else min_gap + 1e-9)

    fig, axes = plt.subplots(1, 3, figsize=(12.0, 8.8), constrained_layout=True)
    cmap = plt.get_cmap("RdYlGn")

    for ax, dataset in zip(axes, DATASETS):
        panel_rows = sorted(
            dataset_rows[dataset],
            key=lambda item: (float(item["avg_rank"]), item["layout_type"] != "trace_biopt", item["layout_type"]),
        )
        labels = [nice_label(row["layout_type"]) for row in panel_rows]
        gaps = np.array(
            [[float(row[f"mean_{suffix}"]) - float(next(r[f"mean_{suffix}"] for r in panel_rows if r["layout_type"] == "trace_biopt")) for suffix, _ in BUDGET_SUFFIXES] for row in panel_rows]
        )
        ranks = np.array([[int(row[f"rank_{suffix}"]) for suffix, _ in BUDGET_SUFFIXES] for row in panel_rows], dtype=int)
        image = ax.imshow(gaps, aspect="auto", cmap=cmap, norm=norm)
        ax.set_title(dataset, fontsize=11, pad=8)
        ax.set_xticks(range(len(BUDGET_SUFFIXES)))
        ax.set_xticklabels([label for _, label in BUDGET_SUFFIXES], fontsize=9)
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels, fontsize=7)
        ax.tick_params(axis="both", length=0)
        ax.set_xticks(np.arange(-0.5, len(BUDGET_SUFFIXES), 1), minor=True)
        ax.set_yticks(np.arange(-0.5, len(labels), 1), minor=True)
        ax.grid(which="minor", color="#ffffff", linestyle="-", linewidth=0.7)
        ax.tick_params(which="minor", bottom=False, left=False)

        for row_idx in range(gaps.shape[0]):
            for col_idx in range(gaps.shape[1]):
                gap = gaps[row_idx, col_idx]
                rank = ranks[row_idx, col_idx]
                text_color = "black" if abs(norm(gap) - 0.5) < 0.23 else "white"
                ax.text(
                    col_idx,
                    row_idx,
                    f"{rank}",
                    ha="center",
                    va="center",
                    fontsize=6.5,
                    color=text_color,
                    fontweight="bold" if labels[row_idx] == "TRACE-BiOpt" else "normal",
                )

        trace_idx = labels.index("TRACE-BiOpt")
        ax.add_patch(plt.Rectangle((-0.5, trace_idx - 0.5), len(BUDGET_SUFFIXES), 1, fill=False, edgecolor="black", linewidth=1.2))

    cbar = fig.colorbar(image, ax=axes.ravel().tolist(), shrink=0.85, pad=0.02)
    cbar.set_label("Baseline MAE - TRACE-BiOpt MAE", fontsize=9)
    cbar.ax.tick_params(labelsize=8)
    fig.suptitle("Current-best 22-method baseline heatmap (cell text = within-row rank)", fontsize=12)
    OUT_FIG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)

    print(f"Wrote {OUT_FIG} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
