#!/usr/bin/env python3
"""Generate representative low-budget hidden-node error heatmaps."""

from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
from sklearn.covariance import LedoitWolf


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
OUT_GRID = CURRENT_BEST / "trace_biopt_hidden_error_heatmap_grid.csv"
OUT_SUMMARY = CURRENT_BEST / "trace_biopt_hidden_error_heatmap_summary.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_hidden_error_heatmaps.pdf"

REPRESENTATIVE_BUDGET = 0.1
REPRESENTATIVE_SEED = 25
RESULT_DIR = {
    "PeMS7_1026": "pems7_1026",
    "PeMS7_228": "pems7_228",
    "Seattle": "seattle",
}
SOURCE_ROOTS = [
    TRACE_RESULTS / "stage16_calibrated_trace_sweep",
    TRACE_RESULTS / "stage16_calibrated_trace_probe",
    TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe",
]
TRACE_SOURCE_LABEL = {
    "stage15_main": "Stage15 main evidence",
    "stage16_replaceable": "Stage16 calibrated rerun",
}
BASELINE_LABEL = {
    "validation_swap_selected": "Prev. TRACE-SL",
    "swap_from_greedy_a_trace": "Swap from A-trace",
    "rcss_selected": "RCSS",
}
DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_eval_module():
    spec = importlib.util.spec_from_file_location(
        "transparent_estimator_eval",
        ROOT / "TRC-23-02333" / "transparent_estimator_eval.py",
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def resolve_seed_dir(dataset: str, split_seed: int, evidence_source: str) -> Path:
    if evidence_source == "stage15_main":
        return STAGE15 / RESULT_DIR[dataset] / f"seed_{split_seed}"
    if evidence_source.startswith("stage16_replaceable:"):
        root_name = evidence_source.split(":", 1)[1]
        for base in SOURCE_ROOTS:
            candidate = base / root_name / f"seed_{split_seed}"
            if candidate.exists():
                return candidate
    raise FileNotFoundError(f"Unable to resolve {dataset} seed {split_seed} for {evidence_source}")


def load_layout_sensors(seed_dir: Path, layout_type: str, budget: float) -> np.ndarray:
    layouts = json.loads((seed_dir / "layouts.json").read_text(encoding="utf-8"))
    for row in layouts:
        if row["layout_type"] == layout_type and abs(float(row["budget"]) - budget) < 1e-9:
            return np.array(sorted(int(x) for x in row["sensors"]), dtype=int)
    raise ValueError(f"Missing layout {layout_type} budget={budget} in {seed_dir}")


def dataset_loader(tev, data_root: str, split_seed: int, split_mode: str):
    if Path(data_root).name.lower() == "seattle":
        return tev.load_seattle_dataset(data_root, split_seed, split_mode=split_mode)
    return tev.load_pems_dataset(data_root, split_seed, split_mode=split_mode)


def per_node_hidden_mae(tev, seed_dir: Path, sensors: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    config = json.loads((seed_dir / "config.json").read_text(encoding="utf-8"))
    train, _, test, _, distance, _, _ = dataset_loader(
        tev,
        config["data_root"],
        int(config["split_seed"]),
        config.get("split_mode", "random"),
    )
    n_nodes = train.shape[1]
    mean = train.mean(axis=0)
    std = train.std(axis=0) + 1e-6
    train_z = (train - mean) / std
    tod = tev.time_of_day_mean(train, mean)
    covariance = LedoitWolf().fit(train_z).covariance_
    precision = linalg.inv(covariance + 1e-6 * np.eye(n_nodes))
    gls_matrix = float(config["gls_prior_weight"]) * precision
    sensors = np.array(sorted(int(x) for x in sensors), dtype=int)
    hidden = np.array([node for node in range(n_nodes) if node not in set(sensors)], dtype=int)
    observed_z = (test - mean) / std
    prior_z = (tev.historical_mean_predict(tod, test.shape[0]) - mean) / std
    observation_weights = np.full(observed_z.shape, float(config["obs_weight"]), dtype=float)
    gls_z, _ = tev.solve_quadratic(observed_z, prior_z, sensors, gls_matrix, observation_weights)
    pred = mean + std * gls_z
    per_node = np.mean(np.abs(pred[:, hidden] - test[:, hidden]), axis=0)
    return hidden, per_node


def build_rows():
    tev = load_eval_module()
    current_best_rows = [
        row for row in load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
        if abs(float(row["budget"]) - REPRESENTATIVE_BUDGET) < 1e-9
    ]
    grid_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for row in sorted(current_best_rows, key=lambda item: DATASETS.index(item["dataset"])):
        dataset = row["dataset"]
        evidence_source = row["evidence_source"]
        trace_dir = resolve_seed_dir(dataset, REPRESENTATIVE_SEED, evidence_source)
        baseline_dir = STAGE15 / RESULT_DIR[dataset] / f"seed_{REPRESENTATIVE_SEED}"
        trace_sensors = load_layout_sensors(trace_dir, "trace_biopt", REPRESENTATIVE_BUDGET)
        baseline_sensors = load_layout_sensors(baseline_dir, row["best_baseline_layout"], REPRESENTATIVE_BUDGET)
        trace_hidden, trace_node_mae = per_node_hidden_mae(tev, trace_dir, trace_sensors)
        baseline_hidden, baseline_node_mae = per_node_hidden_mae(tev, baseline_dir, baseline_sensors)
        common_hidden = np.intersect1d(trace_hidden, baseline_hidden)
        trace_map = {int(node): float(value) for node, value in zip(trace_hidden, trace_node_mae)}
        baseline_map = {int(node): float(value) for node, value in zip(baseline_hidden, baseline_node_mae)}
        trace_common = np.array([trace_map[int(node)] for node in common_hidden], dtype=float)
        baseline_common = np.array([baseline_map[int(node)] for node in common_hidden], dtype=float)
        gain = baseline_common - trace_common
        order = np.argsort(-baseline_common)
        common_hidden = common_hidden[order]
        trace_common = trace_common[order]
        baseline_common = baseline_common[order]
        gain = gain[order]
        source_mode = "stage16_replaceable" if evidence_source.startswith("stage16_replaceable:") else evidence_source

        summary_rows.append(
            {
                "dataset": dataset,
                "budget_pct": int(round(REPRESENTATIVE_BUDGET * 100)),
                "split_seed": REPRESENTATIVE_SEED,
                "trace_source_label": TRACE_SOURCE_LABEL[source_mode],
                "trace_evidence_source": evidence_source,
                "best_baseline_layout": row["best_baseline_layout"],
                "best_baseline_label": BASELINE_LABEL.get(row["best_baseline_layout"], row["best_baseline_layout"]),
                "common_hidden_count": int(common_hidden.size),
                "trace_mean_common_hidden_mae": float(trace_common.mean()),
                "baseline_mean_common_hidden_mae": float(baseline_common.mean()),
                "mean_hidden_gain": float(gain.mean()),
                "median_hidden_gain": float(np.median(gain)),
                "improved_hidden_share": float((gain > 0.0).mean()),
                "max_hidden_gain": float(gain.max()),
                "worst_hidden_gain": float(gain.min()),
            }
        )

        for rank, node, baseline_value, trace_value, gain_value in zip(
            range(1, common_hidden.size + 1),
            common_hidden,
            baseline_common,
            trace_common,
            gain,
        ):
            grid_rows.append(
                {
                    "dataset": dataset,
                    "budget_pct": int(round(REPRESENTATIVE_BUDGET * 100)),
                    "split_seed": REPRESENTATIVE_SEED,
                    "trace_source_label": TRACE_SOURCE_LABEL[source_mode],
                    "trace_evidence_source": evidence_source,
                    "best_baseline_layout": row["best_baseline_layout"],
                    "best_baseline_label": BASELINE_LABEL.get(row["best_baseline_layout"], row["best_baseline_layout"]),
                    "hidden_node": int(node),
                    "node_rank_by_baseline_error": int(rank),
                    "baseline_hidden_mae": float(baseline_value),
                    "trace_hidden_mae": float(trace_value),
                    "gain_vs_baseline": float(gain_value),
                }
            )

    return grid_rows, summary_rows


def render_figure(grid_rows: list[dict[str, object]], summary_rows: list[dict[str, object]]) -> None:
    grid_by_dataset = {dataset: [] for dataset in DATASETS}
    summary_by_dataset = {}
    for row in grid_rows:
        grid_by_dataset[row["dataset"]].append(row)
    for row in summary_rows:
        summary_by_dataset[row["dataset"]] = row

    error_max = max(
        max(float(row["baseline_hidden_mae"]), float(row["trace_hidden_mae"]))
        for row in grid_rows
    )
    gain_abs = max(abs(float(row["gain_vs_baseline"])) for row in grid_rows)

    fig = plt.figure(figsize=(11.4, 4.8), constrained_layout=True)
    outer = gridspec.GridSpec(2, 3, height_ratios=[4.0, 1.2], figure=fig)
    baseline_cmap = plt.get_cmap("magma")
    gain_cmap = plt.get_cmap("coolwarm")

    for col, dataset in enumerate(DATASETS):
        sub = sorted(grid_by_dataset[dataset], key=lambda row: int(row["node_rank_by_baseline_error"]))
        baseline = np.array([float(row["baseline_hidden_mae"]) for row in sub], dtype=float)[None, :]
        trace = np.array([float(row["trace_hidden_mae"]) for row in sub], dtype=float)[None, :]
        gain = np.array([float(row["gain_vs_baseline"]) for row in sub], dtype=float)[None, :]
        summary = summary_by_dataset[dataset]

        ax_top = fig.add_subplot(outer[0, col])
        ax_bottom = fig.add_subplot(outer[1, col])
        im_top = ax_top.imshow(
            np.vstack([baseline, trace]),
            aspect="auto",
            cmap=baseline_cmap,
            vmin=0.0,
            vmax=error_max,
            interpolation="nearest",
        )
        im_bottom = ax_bottom.imshow(
            gain,
            aspect="auto",
            cmap=gain_cmap,
            vmin=-gain_abs,
            vmax=gain_abs,
            interpolation="nearest",
        )
        ax_top.set_title(dataset, fontsize=10)
        ax_top.set_yticks([0, 1], [summary["best_baseline_label"], "TRACE-BiOpt"])
        ax_top.set_xticks([])
        ax_bottom.set_yticks([0], ["Gain"])
        ax_bottom.set_xticks([0, len(sub) - 1], ["Harder nodes", "Easier nodes"])
        ax_bottom.tick_params(axis="x", labelsize=8)

        ax_top.text(
            0.01,
            -0.18,
            f"Improved hidden share={float(summary['improved_hidden_share']):.3f}\nMean gain={float(summary['mean_hidden_gain']):.3f}",
            transform=ax_top.transAxes,
            fontsize=8,
            va="top",
        )

    cbar_top = fig.colorbar(im_top, ax=fig.axes[0:3], location="right", shrink=0.82, pad=0.02)
    cbar_top.set_label("Per-node hidden MAE")
    cbar_bottom = fig.colorbar(im_bottom, ax=fig.axes[3:6], location="right", shrink=0.82, pad=0.02)
    cbar_bottom.set_label("Baseline - TRACE-BiOpt")
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    grid_rows, summary_rows = build_rows()
    write_csv(
        OUT_GRID,
        grid_rows,
        [
            "dataset",
            "budget_pct",
            "split_seed",
            "trace_source_label",
            "trace_evidence_source",
            "best_baseline_layout",
            "best_baseline_label",
            "hidden_node",
            "node_rank_by_baseline_error",
            "baseline_hidden_mae",
            "trace_hidden_mae",
            "gain_vs_baseline",
        ],
    )
    write_csv(
        OUT_SUMMARY,
        summary_rows,
        [
            "dataset",
            "budget_pct",
            "split_seed",
            "trace_source_label",
            "trace_evidence_source",
            "best_baseline_layout",
            "best_baseline_label",
            "common_hidden_count",
            "trace_mean_common_hidden_mae",
            "baseline_mean_common_hidden_mae",
            "mean_hidden_gain",
            "median_hidden_gain",
            "improved_hidden_share",
            "max_hidden_gain",
            "worst_hidden_gain",
        ],
    )
    render_figure(grid_rows, summary_rows)
    print(f"Wrote {OUT_FIG}, {OUT_GRID}, and {OUT_SUMMARY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
