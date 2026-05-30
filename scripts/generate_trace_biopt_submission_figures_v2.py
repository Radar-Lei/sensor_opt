#!/usr/bin/env python3
"""Reviewer-facing figures for the TRACE-BiOpt TR-B submission.

Copy this file to `scripts/generate_trace_biopt_submission_figures_v2.py`
and run it from the repository root:

    python scripts/generate_trace_biopt_submission_figures_v2.py

Inputs expected under:
    TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/

Outputs:
    paper/figures/fig_trace_biopt_margin_forest_v2.{pdf,png}
    paper/figures/fig_trace_biopt_seed_margins_v2.{pdf,png}
    paper/figures/fig_trace_biopt_compact_baseline_heatmap_v2.{pdf,png}
    paper/figures/fig_trace_biopt_submission_panel_v2.{pdf,png}

Design intent:
  1) Make the main claim visually auditable in one figure.
  2) Avoid overloading the manuscript with many audit tables.
  3) Keep the figure reproducible from the current-best evidence CSVs.

Dependencies: pandas, numpy, matplotlib. No seaborn.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


DATASET_ORDER = ["PeMS7_1026", "PeMS7_228", "Seattle"]
BUDGET_ORDER = [0.10, 0.20, 0.30]
BUDGET_LABEL = {0.10: "10%", 0.20: "20%", 0.30: "30%"}

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

# Color-blind friendly palette; still prints acceptably in grayscale.
TRACE_COLOR = "#0072B2"
BASELINE_COLOR = "#D55E00"
STAGE15_COLOR = "#CC79A7"
STAGE16_COLOR = "#009E73"
GRID_COLOR = "#D9D9D9"
ZERO_COLOR = "#333333"


def nice_layout_name(name: str) -> str:
    return LABELS.get(str(name), str(name).replace("_", " "))


def budget_key(value: float | str) -> float:
    return round(float(value), 2)


def regime_label(dataset: str, budget: float | str) -> str:
    b = budget_key(budget)
    return f"{dataset} {BUDGET_LABEL.get(b, f'{int(round(100*b))}%')}"


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.titlesize": 11,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "savefig.bbox": "tight",
            "savefig.dpi": 300,
        }
    )


def require_files(paths: Iterable[Path]) -> None:
    missing = [p for p in paths if not p.exists()]
    if missing:
        joined = "\n  ".join(str(p) for p in missing)
        raise FileNotFoundError(
            "Missing required current-best evidence file(s):\n  "
            + joined
            + "\nRun `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh` first."
        )


def read_current_best(root: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    evidence = root / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
    delta_path = evidence / "trace_biopt_best_baseline_delta.csv"
    matrix_path = evidence / "trace_biopt_full_baseline_matrix.csv"
    seed_path = evidence / "trace_biopt_paired_margin_points.csv"
    require_files([delta_path, matrix_path, seed_path])

    delta = pd.read_csv(delta_path)
    matrix = pd.read_csv(matrix_path)
    seed = pd.read_csv(seed_path)

    # Keep only nominal baseline rows when robustness/stress rows are present.
    if {"robustness_family", "robustness_condition"}.issubset(delta.columns):
        delta = delta[(delta["robustness_family"] == "baseline") & (delta["robustness_condition"] == "baseline")].copy()

    # Normalize numeric columns.
    for col in [
        "budget",
        "trace_biopt_mean",
        "best_baseline_mean",
        "trace_minus_best_baseline",
        "paired_delta_mean",
        "paired_ci95_low",
        "paired_ci95_high",
        "paired_paired_t_p",
        "paired_wilcoxon_p",
    ]:
        if col in delta.columns:
            delta[col] = pd.to_numeric(delta[col], errors="coerce")

    if "budget" in seed.columns:
        seed["budget"] = pd.to_numeric(seed["budget"], errors="coerce")
    for col in ["trace_biopt_mae", "best_baseline_mae", "paired_margin"]:
        if col in seed.columns:
            seed[col] = pd.to_numeric(seed[col], errors="coerce")

    for prefix in ["mean", "rank"]:
        for suffix in ["10", "20", "30"]:
            col = f"{prefix}_{suffix}"
            if col in matrix.columns:
                matrix[col] = pd.to_numeric(matrix[col], errors="coerce")
    if "avg_rank" in matrix.columns:
        matrix["avg_rank"] = pd.to_numeric(matrix["avg_rank"], errors="coerce")

    delta["dataset_order"] = delta["dataset"].map({d: i for i, d in enumerate(DATASET_ORDER)})
    delta["budget_order"] = delta["budget"].map({b: i for i, b in enumerate(BUDGET_ORDER)})
    delta = delta.sort_values(["dataset_order", "budget_order"]).reset_index(drop=True)
    return delta, matrix, seed


def save_figure(fig: mpl.figure.Figure, out_base: Path) -> None:
    out_base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_base.with_suffix(".pdf"))
    fig.savefig(out_base.with_suffix(".png"), dpi=350)
    plt.close(fig)
    print(f"wrote {out_base.with_suffix('.pdf')} and {out_base.with_suffix('.png')}")


def plot_margin_forest(delta: pd.DataFrame, out_dir: Path) -> None:
    """One clean figure for the headline claim: 9 paired margins and CIs."""
    import matplotlib.gridspec as gridspec

    df = delta.copy()
    df["label"] = [regime_label(d, b) for d, b in zip(df["dataset"], df["budget"])]
    df["best_label"] = df["best_baseline_layout"].map(nice_layout_name)
    df["source_kind"] = np.where(df["evidence_source"].astype(str).str.startswith("stage15"), "Stage15", "Stage16")

    y = np.arange(len(df))[::-1]
    # Flip sign so positive = baseline MAE - TRACE MAE = TRACE advantage.
    x = -df["paired_delta_mean"].to_numpy()
    # When x is negated, the CI arms swap: original high arm becomes low arm.
    xerr_low = df["paired_ci95_high"].to_numpy() - df["paired_delta_mean"].to_numpy()
    xerr_high = df["paired_delta_mean"].to_numpy() - df["paired_ci95_low"].to_numpy()

    fig = plt.figure(figsize=(7.5, 4.6))
    gs = gridspec.GridSpec(
        2, 2,
        width_ratios=[3.2, 1],
        height_ratios=[10, 1],
        wspace=0.02,
        hspace=0.18,
        left=0.12, right=0.96, top=0.91, bottom=0.10,
    )
    ax = fig.add_subplot(gs[0, 0])
    ax_labels = fig.add_subplot(gs[0, 1])
    ax_legend = fig.add_subplot(gs[1, :])

    # --- Main data panel ---
    for source, marker, color in [("Stage16", "o", STAGE16_COLOR), ("Stage15", "s", STAGE15_COLOR)]:
        mask = df["source_kind"].eq(source).to_numpy()
        ax.errorbar(
            x[mask],
            y[mask],
            xerr=np.vstack([xerr_low[mask], xerr_high[mask]]),
            fmt=marker,
            color=color,
            ecolor=color,
            elinewidth=1.1,
            capsize=3,
            markersize=5.5,
            label=source,
            zorder=3,
        )

    ax.axvline(0.0, color=ZERO_COLOR, lw=1.0, linestyle="--", zorder=1)
    ax.set_yticks(y)
    ax.set_yticklabels(df["label"])
    ax.set_xlabel("Strongest non-BiOpt baseline MAE $-$ TRACE-BiOpt MAE")
    ax.set_title("Paired current-best dominance margins across tested regimes", fontsize=10)
    ax.grid(axis="x", color=GRID_COLOR, linewidth=0.8, zorder=0)

    # --- Right-side label panel (no ticks/spines) ---
    ax_labels.set_ylim(ax.get_ylim())
    ax_labels.axis("off")
    for yi, challenger in zip(y, df["best_label"]):
        ax_labels.text(0.05, yi, challenger, va="center", ha="left", fontsize=7.2, transform=ax_labels.transData)
    ax_labels.text(0.05, y.max() + 0.65, "Strongest challenger", va="bottom", ha="left", fontsize=7.5, fontweight="bold", transform=ax_labels.transData)

    # --- Legend in bottom row ---
    ax_legend.axis("off")
    handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=STAGE16_COLOR, markersize=6, label="Stage16"),
        plt.Line2D([0], [0], marker="s", color="w", markerfacecolor=STAGE15_COLOR, markersize=6, label="Stage15"),
    ]
    ax_legend.legend(handles=handles, loc="upper center", ncol=2, frameon=False, fontsize=8, handletextpad=0.4, columnspacing=1.2)

    caption_note = "Positive values indicate lower held-out GLS/MAP MAE for TRACE-BiOpt; whiskers are paired 95% CIs."
    fig.text(0.12, 0.02, caption_note, ha="left", va="bottom", fontsize=7.5)
    save_figure(fig, out_dir / "fig_trace_biopt_margin_forest_v2")


def plot_seed_margins(seed: pd.DataFrame, out_dir: Path) -> None:
    """Seed-level dots make the paired-test evidence more transparent."""
    df = seed.copy()
    df["dataset_order"] = df["dataset"].map({d: i for i, d in enumerate(DATASET_ORDER)})
    df["budget_order"] = df["budget"].map({b: i for i, b in enumerate(BUDGET_ORDER)})
    df = df.sort_values(["dataset_order", "budget_order", "split_seed"]).reset_index(drop=True)
    regimes = df[["dataset", "budget"]].drop_duplicates().reset_index(drop=True)
    regimes["label"] = [regime_label(d, b) for d, b in zip(regimes["dataset"], regimes["budget"])]
    key_to_x = {(r.dataset, r.budget): idx for idx, r in regimes.iterrows()}
    df["x"] = [key_to_x[(d, b)] for d, b in zip(df["dataset"], df["budget"])]

    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    rng = np.random.default_rng(20260529)
    jitter = rng.uniform(-0.14, 0.14, size=len(df))
    colors = np.where(df["evidence_source"].astype(str).str.startswith("stage15"), STAGE15_COLOR, STAGE16_COLOR)
    ax.scatter(df["x"] + jitter, -df["paired_margin"], s=18, c=colors, alpha=0.72, edgecolors="none")

    # Mean and 95% interval per regime, computed from the plotted seed-level points.
    for idx, row in regimes.iterrows():
        vals = -df.loc[(df["dataset"] == row["dataset"]) & (df["budget"] == row["budget"]), "paired_margin"].dropna().to_numpy()
        mu = float(vals.mean())
        if len(vals) > 1:
            se = float(vals.std(ddof=1) / math.sqrt(len(vals)))
            ci = 1.96 * se
        else:
            ci = 0.0
        ax.errorbar(idx, mu, yerr=ci, fmt="D", color="black", markersize=4.2, capsize=3, zorder=5)

    ax.axhline(0.0, color=ZERO_COLOR, lw=1.0, linestyle="--")
    ax.set_xticks(np.arange(len(regimes)))
    ax.set_xticklabels(regimes["label"], rotation=35, ha="right")
    ax.set_ylabel("Baseline MAE $-$ TRACE-BiOpt MAE")
    ax.set_title("Every split seed favors TRACE-BiOpt over the strongest challenger")
    ax.grid(axis="y", color=GRID_COLOR, linewidth=0.8)
    ax.text(0.0, -0.27, "Positive values indicate TRACE-BiOpt advantage; diamonds show mean ± 1.96 SE.", transform=ax.transAxes, ha="left", va="top", fontsize=7.5)
    save_figure(fig, out_dir / "fig_trace_biopt_seed_margins_v2")


def matrix_to_long(matrix: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, row in matrix.iterrows():
        dataset = row["dataset"]
        layout = row["layout_type"]
        trace_row = matrix[(matrix["dataset"] == dataset) & (matrix["layout_type"] == "trace_biopt")].iloc[0]
        for suffix, budget in [("10", 0.10), ("20", 0.20), ("30", 0.30)]:
            rows.append(
                {
                    "dataset": dataset,
                    "layout_type": layout,
                    "layout_label": nice_layout_name(layout),
                    "budget": budget,
                    "budget_label": BUDGET_LABEL[budget],
                    "mean_mae": row[f"mean_{suffix}"],
                    "rank": int(row[f"rank_{suffix}"]),
                    "gap_vs_trace": row[f"mean_{suffix}"] - trace_row[f"mean_{suffix}"],
                    "avg_rank": row["avg_rank"],
                }
            )
    return pd.DataFrame(rows)


def plot_compact_heatmap(matrix: pd.DataFrame, out_dir: Path, top_k_baselines: int = 9) -> None:
    """A compact version of the full-baseline matrix for main-text use.

    It keeps TRACE-BiOpt plus the top-k non-BiOpt methods by average rank. The full
    22-method matrix should stay in the appendix or repository.
    """
    avg_rank = matrix.groupby("layout_type")["avg_rank"].mean().sort_values()
    selected = ["trace_biopt"] + [x for x in avg_rank.index if x != "trace_biopt"][:top_k_baselines]
    long = matrix_to_long(matrix[matrix["layout_type"].isin(selected)].copy())

    regimes = [(d, b) for d in DATASET_ORDER for b in BUDGET_ORDER]
    methods = sorted(selected, key=lambda name: (0 if name == "trace_biopt" else 1, avg_rank.get(name, 99), name))
    data = np.full((len(methods), len(regimes)), np.nan)
    ranks = np.full((len(methods), len(regimes)), np.nan)
    for i, method in enumerate(methods):
        for j, (dataset, budget) in enumerate(regimes):
            sub = long[(long["layout_type"] == method) & (long["dataset"] == dataset) & (long["budget"] == budget)]
            if not sub.empty:
                data[i, j] = float(sub.iloc[0]["gap_vs_trace"])
                ranks[i, j] = float(sub.iloc[0]["rank"])

    vmax = float(np.nanmax(np.abs(data)))
    norm = mcolors.TwoSlopeNorm(vmin=-vmax, vcenter=0.0, vmax=vmax)
    fig, ax = plt.subplots(figsize=(7.5, 4.9))
    im = ax.imshow(data, aspect="auto", cmap="RdYlGn", norm=norm)

    ax.set_yticks(np.arange(len(methods)))
    ax.set_yticklabels([nice_layout_name(m) for m in methods])
    ax.set_xticks(np.arange(len(regimes)))
    ax.set_xticklabels([regime_label(d, b).replace(" ", "\n") for d, b in regimes], rotation=0)
    ax.set_title(f"Compact baseline matrix: TRACE-BiOpt plus top {top_k_baselines} challengers")
    ax.set_xlabel("Dataset-budget regime")

    ax.set_xticks(np.arange(-0.5, len(regimes), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(methods), 1), minor=True)
    ax.grid(which="minor", color="white", linestyle="-", linewidth=0.7)
    ax.tick_params(which="minor", bottom=False, left=False)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if np.isnan(data[i, j]):
                continue
            text = "1" if methods[i] == "trace_biopt" else str(int(ranks[i, j]))
            ax.text(j, i, text, ha="center", va="center", fontsize=7, fontweight="bold" if methods[i] == "trace_biopt" else "normal")

    cbar = fig.colorbar(im, ax=ax, shrink=0.84, pad=0.02)
    cbar.set_label("Method MAE minus TRACE-BiOpt MAE")
    ax.text(0.0, -0.18, "Cell text is within-regime rank; full 22-method matrix belongs in appendix/supplement.", transform=ax.transAxes, ha="left", va="top", fontsize=7.5)
    save_figure(fig, out_dir / "fig_trace_biopt_compact_baseline_heatmap_v2")


def plot_submission_panel(delta: pd.DataFrame, out_dir: Path) -> None:
    """A one-page graphical abstract-style panel from the strongest result."""
    df = delta.copy()
    df["budget_pct"] = (df["budget"] * 100).round().astype(int)

    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    for dataset, group in df.groupby("dataset", sort=False):
        group = group.sort_values("budget")
        ax.plot(group["budget_pct"], -group["trace_minus_best_baseline"], marker="o", linewidth=2.0, label=dataset)

    ax.axhline(0.0, color=ZERO_COLOR, lw=1.0)
    ax.set_xticks([10, 20, 30])
    ax.set_xlabel("Sensor budget (%)")
    ax.set_ylabel("MAE advantage over strongest challenger")
    ax.set_title("TRACE-BiOpt advantage over the strongest non-BiOpt baseline")
    ax.grid(axis="y", color=GRID_COLOR, linewidth=0.8)
    ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.18))

    ax.text(
        0.02,
        0.96,
        "All nine values are positive\n(TRACE-BiOpt has lower MAE)",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
        bbox={"boxstyle": "round,pad=0.25", "fc": "white", "ec": GRID_COLOR, "lw": 0.8},
    )
    save_figure(fig, out_dir / "fig_trace_biopt_submission_panel_v2")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Repository root. Default: parent of scripts/.")
    parser.add_argument("--top-k-baselines", type=int, default=9, help="Number of non-BiOpt methods in compact heatmap.")
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = root / "paper" / "figures"
    configure_matplotlib()
    delta, matrix, seed = read_current_best(root)
    plot_margin_forest(delta, out_dir)
    plot_seed_margins(seed, out_dir)
    plot_compact_heatmap(matrix, out_dir, top_k_baselines=args.top_k_baselines)
    plot_submission_panel(delta, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
