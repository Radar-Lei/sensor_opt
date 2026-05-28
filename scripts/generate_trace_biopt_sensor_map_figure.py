#!/usr/bin/env python3
"""Generate current-best low-budget sensor layout maps."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.sparse import csgraph
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
STAGE16_SWEEP = TRACE_RESULTS / "stage16_calibrated_trace_sweep"
STAGE16_PROBE = TRACE_RESULTS / "stage16_calibrated_trace_probe"
PEMS228_PROBE = TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe"
OUT_SUMMARY = CURRENT_BEST / "trace_biopt_sensor_map_summary.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_sensor_maps.pdf"

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
SOURCE_ROOTS = [
    STAGE16_SWEEP,
    STAGE16_PROBE,
    PEMS228_PROBE,
]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def stage15_layout_path(dataset: str, split_seed: int) -> Path:
    return STAGE15 / RESULT_DIR[dataset] / f"seed_{split_seed}" / "layouts.json"


def resolve_trace_layout_path(dataset: str, budget: float, evidence_source: str, split_seed: int) -> tuple[Path, str]:
    if evidence_source == "stage15_main":
        return stage15_layout_path(dataset, split_seed), "stage15_main"
    if evidence_source.startswith("stage16_replaceable:"):
        root_name = evidence_source.split(":", 1)[1]
        for base in SOURCE_ROOTS:
            candidate = base / root_name / f"seed_{split_seed}" / "layouts.json"
            if candidate.exists():
                return candidate, root_name
        raise FileNotFoundError(f"could not resolve Stage16 layouts for {dataset} {budget}: {evidence_source}")
    raise ValueError(f"unsupported evidence source: {evidence_source}")


def load_layout(path: Path, dataset: str, budget: float, layout_type: str) -> dict[str, object]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    return next(
        row for row in rows
        if row["dataset"] == dataset
        and abs(float(row["budget"]) - budget) < 1e-9
        and row["layout_type"] == layout_type
    )


def collect_frequency(dataset: str, budget: float, layout_type: str, trace_evidence_source: str | None = None) -> tuple[Counter[int], str]:
    counter: Counter[int] = Counter()
    source_name = ""
    for seed in range(25, 35):
        if layout_type == "trace_biopt":
            path, source_name = resolve_trace_layout_path(dataset, budget, trace_evidence_source or "stage15_main", seed)
        else:
            path = stage15_layout_path(dataset, seed)
            source_name = "stage15_baseline"
        match = load_layout(path, dataset, budget, layout_type)
        counter.update(match["sensors"])
    return counter, source_name


def peMS_228_coords() -> np.ndarray:
    station = pd.read_csv(ROOT / "TRC-23-02333" / "dataset" / "PeMS7_228" / "PeMSD7_M_Station_Info.csv")
    return station[["Longitude", "Latitude"]].to_numpy(dtype=float)


def seattle_coords() -> np.ndarray:
    nodes = pd.read_csv(ROOT / "TRC-23-02333" / "dataset" / "Seattle" / "nodes_loop_mp_list.csv")
    loc = pd.read_csv(ROOT / "TRC-23-02333" / "dataset" / "Seattle" / "Cabinet Location Information.csv")
    loc_map = {
        str(name): (float(lon), float(lat))
        for name, lat, lon in zip(loc["CabName"], loc["Lat"], loc["Lon"])
    }
    keys = nodes["milepost"].astype(str).str[1:]
    coords = np.array([loc_map[key] for key in keys], dtype=float)
    return coords


def spectral_coords_from_distance(distance: np.ndarray) -> np.ndarray:
    positive = distance[np.isfinite(distance) & (distance > 0)]
    scale = float(np.median(positive))
    similarity = np.exp(-distance / scale)
    similarity[~np.isfinite(distance) | (distance <= 0)] = 0.0
    np.fill_diagonal(similarity, 0.0)
    lap = csgraph.laplacian(similarity, normed=True)
    _, vecs = eigsh(lap, k=3, which="SM")
    coords = vecs[:, 1:3]
    coords = (coords - coords.mean(axis=0)) / coords.std(axis=0)
    return coords


def dataset_coords(dataset: str) -> tuple[np.ndarray, str]:
    if dataset == "PeMS7_228":
        return peMS_228_coords(), "geographic_station_coordinates"
    if dataset == "Seattle":
        return seattle_coords(), "geographic_cabinet_coordinates"
    if dataset == "PeMS7_1026":
        dist = np.loadtxt(ROOT / "TRC-23-02333" / "dataset" / "PeMS7_1026" / "PeMSD7_W_1026.csv", delimiter=",")
        return spectral_coords_from_distance(dist), "distance_spectral_embedding"
    raise ValueError(dataset)


def add_summary_row(
    rows: list[dict[str, str]],
    *,
    dataset: str,
    budget_pct: int,
    layout_role: str,
    layout_label: str,
    layout_type: str,
    best_baseline_layout: str,
    coordinate_mode: str,
    node_count: int,
    counter: Counter[int],
    evidence_source: str,
) -> None:
    values = np.array(list(counter.values()), dtype=float) if counter else np.array([], dtype=float)
    rows.append(
        {
            "dataset": dataset,
            "budget_pct": str(budget_pct),
            "layout_role": layout_role,
            "layout_label": layout_label,
            "layout_type": layout_type,
            "best_baseline_layout": best_baseline_layout,
            "coordinate_mode": coordinate_mode,
            "node_count": str(node_count),
            "selected_unique_nodes": str(len(counter)),
            "always_selected_nodes": str(int((values == 10).sum()) if values.size else 0),
            "mean_selection_frequency": f"{values.mean() / 10.0:.6f}" if values.size else "0.000000",
            "max_selection_frequency": f"{values.max() / 10.0:.6f}" if values.size else "0.000000",
            "evidence_source": evidence_source,
        }
    )


def main() -> int:
    delta_rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    low_budget_rows = [row for row in delta_rows if abs(float(row["budget"]) - 0.1) < 1e-9]
    row_lookup = {row["dataset"]: row for row in low_budget_rows}

    summary_rows: list[dict[str, str]] = []
    fig, axes = plt.subplots(len(DATASETS), 2, figsize=(10.2, 11.2), constrained_layout=True)

    for ridx, dataset in enumerate(DATASETS):
        row = row_lookup[dataset]
        budget = float(row["budget"])
        evidence_source = row["evidence_source"]
        baseline = row["best_baseline_layout"]
        baseline_label = BASELINE_LABEL.get(baseline, baseline.replace("_", " "))
        coords, coordinate_mode = dataset_coords(dataset)
        trace_freq, trace_source_name = collect_frequency(dataset, budget, "trace_biopt", evidence_source)
        base_freq, _ = collect_frequency(dataset, budget, baseline)
        trace_nodes = set(trace_freq)
        base_nodes = set(base_freq)
        overlap = trace_nodes & base_nodes
        union = trace_nodes | base_nodes

        add_summary_row(
            summary_rows,
            dataset=dataset,
            budget_pct=10,
            layout_role="trace_biopt_current_best",
            layout_label="TRACE-BiOpt",
            layout_type="trace_biopt",
            best_baseline_layout=baseline,
            coordinate_mode=coordinate_mode,
            node_count=coords.shape[0],
            counter=trace_freq,
            evidence_source=evidence_source,
        )
        add_summary_row(
            summary_rows,
            dataset=dataset,
            budget_pct=10,
            layout_role="strongest_baseline",
            layout_label=baseline_label,
            layout_type=baseline,
            best_baseline_layout=baseline,
            coordinate_mode=coordinate_mode,
            node_count=coords.shape[0],
            counter=base_freq,
            evidence_source="stage15_baseline",
        )

        for cidx, (freq, title, cmap_name, subtitle) in enumerate(
            [
                (trace_freq, "TRACE-BiOpt", "Blues", trace_source_name.replace("_", " ")),
                (base_freq, baseline_label, "Reds", "stage15 strongest baseline"),
            ]
        ):
            ax = axes[ridx, cidx]
            ax.scatter(coords[:, 0], coords[:, 1], s=5, color="#d0d0d0", alpha=0.45, linewidths=0)
            if freq:
                idx = np.array(sorted(freq))
                vals = np.array([freq[i] / 10.0 for i in idx])
                ax.scatter(
                    coords[idx, 0],
                    coords[idx, 1],
                    s=12 + 88 * vals,
                    c=vals,
                    cmap=cmap_name,
                    vmin=0.1,
                    vmax=1.0,
                    linewidths=0,
                )
            if coordinate_mode.startswith("geographic"):
                ax.set_aspect("equal", adjustable="box")
            ax.set_xticks([])
            ax.set_yticks([])
            for spine in ax.spines.values():
                spine.set_visible(False)
            if ridx == 0:
                ax.set_title(title, fontsize=10)
            if cidx == 0:
                ax.set_ylabel(TITLE_MAP[dataset], fontsize=10)
            ax.text(
                0.02,
                0.98,
                subtitle,
                transform=ax.transAxes,
                fontsize=7.5,
                color="#555555",
                ha="left",
                va="top",
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
            if cidx == 0:
                ax.text(
                    0.02,
                    0.04,
                    coordinate_mode.replace("_", " "),
                    transform=ax.transAxes,
                    fontsize=7.5,
                    color="#555555",
                    ha="left",
                    va="bottom",
                )

    fig.suptitle("Current-best low-budget sensor maps", fontsize=12, y=1.02)
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)

    with OUT_SUMMARY.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "dataset",
                "budget_pct",
                "layout_role",
                "layout_label",
                "layout_type",
                "best_baseline_layout",
                "coordinate_mode",
                "node_count",
                "selected_unique_nodes",
                "always_selected_nodes",
                "mean_selection_frequency",
                "max_selection_frequency",
                "evidence_source",
            ],
        )
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Wrote {OUT_FIG} and {OUT_SUMMARY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
