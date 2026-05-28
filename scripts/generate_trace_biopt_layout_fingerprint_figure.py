#!/usr/bin/env python3
"""Generate current-best low-budget layout fingerprints."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csgraph
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
OUT_SUMMARY = CURRENT_BEST / "trace_biopt_layout_fingerprint_summary.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_layout_fingerprints.pdf"

DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
RESULT_DIR = {
    "PeMS7_1026": "pems7_1026",
    "PeMS7_228": "pems7_228",
    "Seattle": "seattle",
}
TITLE_MAP = {
    "PeMS7_1026": "PeMS7_1026 10%",
    "PeMS7_228": "PeMS7_228 10%",
    "Seattle": "Seattle 10%",
}
BASELINE_LABEL = {
    "swap_from_greedy_a_trace": "Swap from A-trace",
    "validation_swap_selected": "Prev. TRACE-SL",
    "rcss_selected": "RCSS",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def dataset_similarity(dataset: str) -> np.ndarray:
    if dataset == "Seattle":
        a = np.load(ROOT / "TRC-23-02333" / "dataset" / "Seattle" / "Loop_Seattle_2015_A.npy").astype(float)
        sim = a + a.T
        sim[sim > 0] = 1.0
        np.fill_diagonal(sim, 0.0)
        return sim
    if dataset == "PeMS7_228":
        dist = np.loadtxt(ROOT / "TRC-23-02333" / "dataset" / "PeMS7_228" / "PeMSD7_W_228.csv", delimiter=",")
    elif dataset == "PeMS7_1026":
        dist = np.loadtxt(ROOT / "TRC-23-02333" / "dataset" / "PeMS7_1026" / "PeMSD7_W_1026.csv", delimiter=",")
    else:
        raise ValueError(dataset)
    positive = dist[dist > 0]
    scale = float(np.median(positive))
    sim = np.exp(-dist / scale)
    np.fill_diagonal(sim, 0.0)
    return sim


def spectral_coords(similarity: np.ndarray) -> np.ndarray:
    lap = csgraph.laplacian(similarity, normed=True)
    _, vecs = eigsh(lap, k=3, which="SM")
    coords = vecs[:, 1:3]
    coords = (coords - coords.mean(axis=0)) / coords.std(axis=0)
    return coords


def collect_frequency(dataset: str, budget: float, layout_type: str) -> Counter:
    counter: Counter[int] = Counter()
    for seed in range(25, 35):
        path = STAGE15 / RESULT_DIR[dataset] / f"seed_{seed}" / "layouts.json"
        rows = json.loads(path.read_text(encoding="utf-8"))
        match = next(
            row for row in rows
            if row["dataset"] == dataset and abs(float(row["budget"]) - budget) < 1e-9 and row["layout_type"] == layout_type
        )
        counter.update(match["sensors"])
    return counter


def main() -> int:
    delta = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    low_budget_rows = [row for row in delta if abs(float(row["budget"]) - 0.1) < 1e-9]
    row_lookup = {row["dataset"]: row for row in low_budget_rows}

    summary_rows: list[dict[str, str]] = []
    fig, axes = plt.subplots(len(DATASETS), 2, figsize=(9.4, 10.8), constrained_layout=True)

    for ridx, dataset in enumerate(DATASETS):
        row = row_lookup[dataset]
        baseline = row["best_baseline_layout"]
        baseline_label = BASELINE_LABEL.get(baseline, baseline.replace("_", " "))
        coords = spectral_coords(dataset_similarity(dataset))
        trace_freq = collect_frequency(dataset, 0.1, "trace_biopt")
        base_freq = collect_frequency(dataset, 0.1, baseline)
        trace_nodes = set(trace_freq)
        base_nodes = set(base_freq)
        overlap = trace_nodes & base_nodes
        union = trace_nodes | base_nodes
        trace_always = sum(v == 10 for v in trace_freq.values())
        base_always = sum(v == 10 for v in base_freq.values())
        summary_rows.append(
            {
                "dataset": dataset,
                "budget_pct": "10",
                "best_baseline_layout": baseline,
                "best_baseline_label": baseline_label,
                "trace_unique_nodes": str(len(trace_nodes)),
                "baseline_unique_nodes": str(len(base_nodes)),
                "overlap_unique_nodes": str(len(overlap)),
                "union_unique_nodes": str(len(union)),
                "unique_jaccard_overlap": f"{len(overlap) / len(union):.6f}",
                "trace_always_selected_nodes": str(trace_always),
                "baseline_always_selected_nodes": str(base_always),
            }
        )

        for cidx, (freq, title, color) in enumerate(
            [
                (trace_freq, "TRACE-BiOpt", "#1f77b4"),
                (base_freq, baseline_label, "#d62728"),
            ]
        ):
            ax = axes[ridx, cidx]
            ax.scatter(coords[:, 0], coords[:, 1], s=6, color="#d9d9d9", alpha=0.55, linewidths=0)
            if freq:
                idx = np.array(sorted(freq))
                vals = np.array([freq[i] / 10.0 for i in idx])
                ax.scatter(
                    coords[idx, 0],
                    coords[idx, 1],
                    s=14 + 90 * vals,
                    c=vals,
                    cmap="Blues" if cidx == 0 else "Reds",
                    vmin=0.1,
                    vmax=1.0,
                    linewidths=0,
                )
            ax.set_xticks([])
            ax.set_yticks([])
            if ridx == 0:
                ax.set_title(title, fontsize=10)
            if cidx == 0:
                ax.set_ylabel(TITLE_MAP[dataset], fontsize=10)
            ax.text(
                0.02,
                0.04,
                f"uniq={len(freq)}",
                transform=ax.transAxes,
                fontsize=8,
                color=color,
                ha="left",
                va="bottom",
            )
            if cidx == 1:
                ax.text(
                    0.98,
                    0.04,
                    f"J={len(overlap) / len(union):.2f}",
                    transform=ax.transAxes,
                    fontsize=8,
                    color="#444444",
                    ha="right",
                    va="bottom",
                )

    fig.suptitle("Current-best low-budget layout fingerprints in graph space", fontsize=12, y=1.02)
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)

    with OUT_SUMMARY.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "dataset",
                "budget_pct",
                "best_baseline_layout",
                "best_baseline_label",
                "trace_unique_nodes",
                "baseline_unique_nodes",
                "overlap_unique_nodes",
                "union_unique_nodes",
                "unique_jaccard_overlap",
                "trace_always_selected_nodes",
                "baseline_always_selected_nodes",
            ],
        )
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Wrote {OUT_FIG} and {OUT_SUMMARY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
