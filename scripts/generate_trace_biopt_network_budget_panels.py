#!/usr/bin/env python3
"""Generate network/budget illustration panels for TRACE-BiOpt experiments.

Copy to the repository and run from the repo root:

    python scripts/generate_trace_biopt_network_budget_panels.py --root . --mask-source trace

Useful alternatives:

    # Pure experimental-setup illustration, independent of TRACE-BiOpt outputs
    python scripts/generate_trace_biopt_network_budget_panels.py --root . --mask-source random

    # Show which nodes are not instrumented instead of installed sensors
    python scripts/generate_trace_biopt_network_budget_panels.py --root . --mask-source random --highlight hidden

Outputs:
    paper/figures/fig_network_case_overview.pdf/.png
    paper/figures/fig_sensor_budget_panels.pdf/.png

What the two figures mean:
  * fig_network_case_overview: one row, three experiment networks.
  * fig_sensor_budget_panels: 3 datasets x 3 budgets. Grey nodes are the
    background network; highlighted nodes are sensors by default. A 10% budget
    means roughly 10% nodes have sensors and 90% remain hidden/uninstrumented.

The script tries to use geographic coordinates when available. PeMS7_1026 is
visualized by a spectral embedding of its distance matrix, matching the current
style used by the existing sensor-map script.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import pandas as pd

try:
    from scipy.sparse import csgraph
    from scipy.sparse.linalg import eigsh
except Exception:  # pragma: no cover - fallback only used if scipy unavailable
    csgraph = None
    eigsh = None


DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
BUDGETS = [0.10, 0.20, 0.30]
RESULT_DIR = {
    "PeMS7_1026": "pems7_1026",
    "PeMS7_228": "pems7_228",
    "Seattle": "seattle",
}
DATASET_TITLES = {
    "PeMS7_1026": "PeMS7_1026",
    "PeMS7_228": "PeMS7_228",
    "Seattle": "Seattle",
}

BASE_NODE_COLOR = "#B8C2CC"
BASE_EDGE_COLOR = "#D6DEE6"
SENSOR_COLOR = "#1F7A4D"
HIDDEN_COLOR = "#D04A32"
TEXT_COLOR = "#1A202C"
SUBTLE_TEXT = "#4A5568"
PANEL_BG = "#FFFFFF"


@dataclass(frozen=True)
class NetworkView:
    dataset: str
    coords: np.ndarray
    edges: np.ndarray
    coordinate_mode: str


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "axes.titlesize": 9.5,
            "axes.labelsize": 8.5,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.dpi": 350,
            "savefig.bbox": "tight",
        }
    )


def normalize_coords(coords: np.ndarray) -> np.ndarray:
    coords = np.asarray(coords, dtype=float)
    if coords.ndim != 2 or coords.shape[1] != 2:
        raise ValueError(f"coordinates must have shape (n, 2), got {coords.shape}")
    ok = np.isfinite(coords).all(axis=1)
    if not ok.all():
        raise ValueError(f"coordinates contain {int((~ok).sum())} non-finite rows")
    centered = coords - coords.mean(axis=0, keepdims=True)
    scale = np.max(np.ptp(centered, axis=0))
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0
    return centered / scale


def knn_edges(coords: np.ndarray, k: int = 3, max_edges: int = 3500) -> np.ndarray:
    """Build a lightweight visual edge set from coordinates.

    This is for visualization only; it prevents the network panels from becoming
    isolated point clouds when no explicit road-link file is available.
    """
    n = coords.shape[0]
    diff = coords[:, None, :] - coords[None, :, :]
    dist = np.sqrt(np.sum(diff * diff, axis=2))
    np.fill_diagonal(dist, np.inf)
    pairs: set[tuple[int, int]] = set()
    for i in range(n):
        nn = np.argpartition(dist[i], kth=min(k, n - 1))[:k]
        for j in nn:
            a, b = sorted((int(i), int(j)))
            pairs.add((a, b))
    edges = np.array(sorted(pairs), dtype=int)
    if len(edges) > max_edges:
        # Keep the shortest visual edges when the graph is very dense.
        lengths = np.linalg.norm(coords[edges[:, 0]] - coords[edges[:, 1]], axis=1)
        keep = np.argsort(lengths)[:max_edges]
        edges = edges[keep]
    return edges


def knn_edges_from_distance(distance: np.ndarray, k: int = 3, max_edges: int = 3500) -> np.ndarray:
    distance = np.asarray(distance, dtype=float)
    n = distance.shape[0]
    d = distance.copy()
    d[~np.isfinite(d)] = np.inf
    d[d <= 0] = np.inf
    pairs: set[tuple[int, int]] = set()
    for i in range(n):
        nn = np.argpartition(d[i], kth=min(k, n - 1))[:k]
        for j in nn:
            if not np.isfinite(d[i, j]):
                continue
            a, b = sorted((int(i), int(j)))
            pairs.add((a, b))
    edges = np.array(sorted(pairs), dtype=int)
    if len(edges) > max_edges:
        lengths = distance[edges[:, 0], edges[:, 1]]
        keep = np.argsort(lengths)[:max_edges]
        edges = edges[keep]
    return edges


def spectral_coords_from_distance(distance: np.ndarray) -> np.ndarray:
    if csgraph is None or eigsh is None:
        # Classical MDS fallback if scipy is unavailable.
        d = np.asarray(distance, dtype=float)
        d[~np.isfinite(d)] = np.nanmax(d[np.isfinite(d)])
        d2 = d * d
        n = d.shape[0]
        j = np.eye(n) - np.ones((n, n)) / n
        b = -0.5 * j @ d2 @ j
        vals, vecs = np.linalg.eigh(b)
        order = np.argsort(vals)[::-1][:2]
        vals = np.maximum(vals[order], 0)
        coords = vecs[:, order] * np.sqrt(vals)
        return normalize_coords(coords)

    positive = distance[np.isfinite(distance) & (distance > 0)]
    scale = float(np.median(positive)) if positive.size else 1.0
    similarity = np.exp(-distance / scale)
    similarity[~np.isfinite(distance) | (distance <= 0)] = 0.0
    np.fill_diagonal(similarity, 0.0)
    lap = csgraph.laplacian(similarity, normed=True)
    _, vecs = eigsh(lap, k=3, which="SM")
    return normalize_coords(vecs[:, 1:3])


def pems228_coords(root: Path) -> np.ndarray:
    path = root / "TRC-23-02333" / "dataset" / "PeMS7_228" / "PeMSD7_M_Station_Info.csv"
    station = pd.read_csv(path)
    return normalize_coords(station[["Longitude", "Latitude"]].to_numpy(dtype=float))


def seattle_coords(root: Path) -> np.ndarray:
    nodes = pd.read_csv(root / "TRC-23-02333" / "dataset" / "Seattle" / "nodes_loop_mp_list.csv")
    loc = pd.read_csv(root / "TRC-23-02333" / "dataset" / "Seattle" / "Cabinet Location Information.csv")
    loc_map = {
        str(name): (float(lon), float(lat))
        for name, lat, lon in zip(loc["CabName"], loc["Lat"], loc["Lon"])
    }
    keys = nodes["milepost"].astype(str).str[1:]
    coords = np.array([loc_map[key] for key in keys], dtype=float)
    return normalize_coords(coords)


def pems1026_distance(root: Path) -> np.ndarray:
    return np.loadtxt(
        root / "TRC-23-02333" / "dataset" / "PeMS7_1026" / "PeMSD7_W_1026.csv",
        delimiter=",",
    )


def load_network(root: Path, dataset: str, k_edges: int) -> NetworkView:
    if dataset == "PeMS7_228":
        coords = pems228_coords(root)
        edges = knn_edges(coords, k=k_edges)
        mode = "geographic station coordinates; visual kNN edges"
    elif dataset == "Seattle":
        coords = seattle_coords(root)
        edges = knn_edges(coords, k=k_edges)
        mode = "geographic cabinet coordinates; visual kNN edges"
    elif dataset == "PeMS7_1026":
        distance = pems1026_distance(root)
        coords = spectral_coords_from_distance(distance)
        edges = knn_edges_from_distance(distance, k=k_edges)
        mode = "distance-matrix spectral embedding"
    else:
        raise ValueError(dataset)
    return NetworkView(dataset=dataset, coords=coords, edges=edges, coordinate_mode=mode)


def draw_network_base(ax: plt.Axes, view: NetworkView, node_size: float | None = None) -> None:
    coords = view.coords
    edges = view.edges
    if len(edges):
        segments = np.stack([coords[edges[:, 0]], coords[edges[:, 1]]], axis=1)
        lc = LineCollection(segments, colors=BASE_EDGE_COLOR, linewidths=0.35, alpha=0.72, zorder=1)
        ax.add_collection(lc)
    n = coords.shape[0]
    if node_size is None:
        node_size = 10 if n <= 300 else 4.2
    ax.scatter(coords[:, 0], coords[:, 1], s=node_size, c=BASE_NODE_COLOR, alpha=0.52, linewidths=0, zorder=2)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor(PANEL_BG)
    for spine in ax.spines.values():
        spine.set_visible(False)


def budget_count(n: int, budget: float) -> int:
    return max(1, min(n, int(round(budget * n))))


def random_sensors(n: int, budget: float, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    k = budget_count(n, budget)
    return np.sort(rng.choice(n, size=k, replace=False))


def read_current_best_delta(root: Path) -> list[dict[str, str]]:
    path = root / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence" / "trace_biopt_best_baseline_delta.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def stage15_layout_path(root: Path, dataset: str, split_seed: int) -> Path:
    return (
        root
        / "TRC-23-02333"
        / "trace_sl_results"
        / "stage15_biopt_allbudget_10seed_v2"
        / RESULT_DIR[dataset]
        / f"seed_{split_seed}"
        / "layouts.json"
    )


def resolve_trace_layout_path(root: Path, dataset: str, budget: float, evidence_source: str, split_seed: int) -> Path:
    trace_results = root / "TRC-23-02333" / "trace_sl_results"
    if evidence_source == "stage15_main":
        return stage15_layout_path(root, dataset, split_seed)
    if evidence_source.startswith("stage16_replaceable:"):
        root_name = evidence_source.split(":", 1)[1]
        source_roots = [
            trace_results / "stage16_calibrated_trace_sweep",
            trace_results / "stage16_calibrated_trace_probe",
            trace_results / "stage15_biopt_pems228_10_risksource_probe",
        ]
        for base in source_roots:
            candidate = base / root_name / f"seed_{split_seed}" / "layouts.json"
            if candidate.exists():
                return candidate
    raise FileNotFoundError(f"Cannot resolve trace layout for {dataset}, budget={budget}, source={evidence_source}")


def load_layout_sensors(path: Path, dataset: str, budget: float, layout_type: str = "trace_biopt") -> np.ndarray:
    rows = json.loads(path.read_text(encoding="utf-8"))
    for row in rows:
        if (
            row.get("dataset") == dataset
            and abs(float(row.get("budget")) - budget) < 1e-9
            and row.get("layout_type") == layout_type
        ):
            return np.array(sorted(int(x) for x in row["sensors"]), dtype=int)
    raise LookupError(f"No {layout_type} layout for {dataset}, budget={budget} in {path}")


def trace_sensors(root: Path, dataset: str, budget: float, split_seed: int) -> np.ndarray:
    rows = read_current_best_delta(root)
    match = None
    for row in rows:
        if row["dataset"] == dataset and abs(float(row["budget"]) - budget) < 1e-9:
            match = row
            break
    if match is None:
        raise LookupError(f"No current-best row for {dataset}, budget={budget}")
    path = resolve_trace_layout_path(root, dataset, budget, match["evidence_source"], split_seed)
    return load_layout_sensors(path, dataset, budget, layout_type="trace_biopt")


def selected_indices(
    *,
    root: Path,
    view: NetworkView,
    budget: float,
    mask_source: str,
    split_seed: int,
    random_seed: int,
    strict: bool,
) -> tuple[np.ndarray, str]:
    n = view.coords.shape[0]
    if mask_source == "random":
        # Deterministic, dataset/budget-specific seed so the figure is stable.
        seed = random_seed + 1009 * DATASETS.index(view.dataset) + int(round(100 * budget))
        return random_sensors(n, budget, seed), "representative random mask"
    if mask_source == "trace":
        try:
            sensors = trace_sensors(root, view.dataset, budget, split_seed)
            sensors = sensors[(sensors >= 0) & (sensors < n)]
            return np.sort(sensors), f"TRACE-BiOpt, split seed {split_seed}"
        except Exception as exc:
            if strict:
                raise
            print(f"[warning] {exc}; falling back to deterministic random mask", file=sys.stderr)
            seed = random_seed + 1009 * DATASETS.index(view.dataset) + int(round(100 * budget))
            return random_sensors(n, budget, seed), "random fallback"
    raise ValueError(f"unknown mask_source: {mask_source}")


def draw_highlighted_nodes(
    ax: plt.Axes,
    view: NetworkView,
    selected: np.ndarray,
    *,
    budget: float,
    highlight: str,
    label: str,
) -> None:
    n = view.coords.shape[0]
    selected_set = set(int(x) for x in selected)
    if highlight == "sensors":
        highlight_idx = selected
        count_label = f"{len(selected)}/{n} sensors; {n - len(selected)} hidden"
        color = SENSOR_COLOR
        title_suffix = "sensors installed"
    elif highlight == "hidden":
        hidden = np.array([i for i in range(n) if i not in selected_set], dtype=int)
        highlight_idx = hidden
        count_label = f"{len(hidden)}/{n} uninstrumented; {len(selected)} sensors"
        color = HIDDEN_COLOR
        title_suffix = "nodes without sensors"
    else:
        raise ValueError(highlight)

    coords = view.coords
    marker_size = 28 if n <= 300 else 13
    edge_width = 0.40 if n <= 300 else 0.25
    if len(highlight_idx):
        ax.scatter(
            coords[highlight_idx, 0],
            coords[highlight_idx, 1],
            s=marker_size,
            c=color,
            alpha=0.95,
            edgecolors="white",
            linewidths=edge_width,
            zorder=4,
        )
    ax.set_title(
        f"{DATASET_TITLES[view.dataset]} — {int(round(100 * budget))}%\n{count_label}",
        color=TEXT_COLOR,
        pad=3.5,
    )
    ax.text(
        0.02,
        0.02,
        label,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=6.7,
        color=SUBTLE_TEXT,
        bbox={"boxstyle": "round,pad=0.18", "fc": "white", "ec": "#E2E8F0", "lw": 0.5, "alpha": 0.88},
    )
    ax.text(
        0.98,
        0.02,
        title_suffix,
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=6.7,
        color=color,
    )


def save(fig: plt.Figure, out_base: Path) -> None:
    out_base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_base.with_suffix(".pdf"))
    fig.savefig(out_base.with_suffix(".png"))
    plt.close(fig)
    print(f"wrote {out_base.with_suffix('.pdf')} and {out_base.with_suffix('.png')}")


def plot_network_overview(views: list[NetworkView], out_dir: Path) -> None:
    fig, axes = plt.subplots(1, len(views), figsize=(10.8, 3.25), constrained_layout=True)
    for ax, view in zip(axes, views):
        draw_network_base(ax, view)
        n = view.coords.shape[0]
        ax.set_title(f"{DATASET_TITLES[view.dataset]}\n{n} candidate sensor locations", color=TEXT_COLOR)
        ax.text(
            0.02,
            0.02,
            view.coordinate_mode,
            transform=ax.transAxes,
            ha="left",
            va="bottom",
            fontsize=6.8,
            color=SUBTLE_TEXT,
            bbox={"boxstyle": "round,pad=0.18", "fc": "white", "ec": "#E2E8F0", "lw": 0.5, "alpha": 0.86},
        )
    fig.suptitle("Experiment network cases", fontsize=12, weight="bold", y=1.04)
    save(fig, out_dir / "fig_network_case_overview")


def plot_budget_panels(
    *,
    root: Path,
    views: list[NetworkView],
    out_dir: Path,
    mask_source: str,
    split_seed: int,
    random_seed: int,
    highlight: str,
    strict: bool,
) -> None:
    fig, axes = plt.subplots(
        len(views),
        len(BUDGETS),
        figsize=(10.8, 9.0),
        constrained_layout=True,
    )
    for ridx, view in enumerate(views):
        for cidx, budget in enumerate(BUDGETS):
            ax = axes[ridx, cidx]
            draw_network_base(ax, view)
            selected, label = selected_indices(
                root=root,
                view=view,
                budget=budget,
                mask_source=mask_source,
                split_seed=split_seed,
                random_seed=random_seed,
                strict=strict,
            )
            draw_highlighted_nodes(ax, view, selected, budget=budget, highlight=highlight, label=label)
    if highlight == "sensors":
        subtitle = "Highlighted nodes are installed sensors; grey nodes are hidden/uninstrumented locations."
    else:
        subtitle = "Highlighted nodes are locations without sensors; grey background includes all candidate locations."
    fig.suptitle(
        f"Sensor-budget illustration across experiment networks\n{subtitle}",
        fontsize=12,
        weight="bold",
        y=1.03,
    )
    save(fig, out_dir / "fig_sensor_budget_panels")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Repository root")
    parser.add_argument("--mask-source", choices=["trace", "random"], default="trace", help="Use representative TRACE-BiOpt layouts or deterministic random masks")
    parser.add_argument("--layout-seed", type=int, default=25, help="Split seed used when --mask-source trace")
    parser.add_argument("--random-seed", type=int, default=20260529, help="Base seed for deterministic random masks")
    parser.add_argument("--highlight", choices=["sensors", "hidden"], default="sensors", help="Highlight installed sensors or nodes without sensors")
    parser.add_argument("--knn", type=int, default=3, help="k for lightweight visual kNN edges")
    parser.add_argument("--strict", action="store_true", help="Fail instead of falling back to random masks if TRACE layout files are missing")
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = root / "paper" / "figures"
    configure_matplotlib()
    views = [load_network(root, dataset, args.knn) for dataset in DATASETS]
    plot_network_overview(views, out_dir)
    plot_budget_panels(
        root=root,
        views=views,
        out_dir=out_dir,
        mask_source=args.mask_source,
        split_seed=args.layout_seed,
        random_seed=args.random_seed,
        highlight=args.highlight,
        strict=args.strict,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
