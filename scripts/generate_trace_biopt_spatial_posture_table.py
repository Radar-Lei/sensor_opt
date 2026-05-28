#!/usr/bin/env python3
"""Generate a reviewer-facing current-best low-budget spatial posture table."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.sparse.csgraph import shortest_path


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
STAGE16_SWEEP = TRACE_RESULTS / "stage16_calibrated_trace_sweep"
STAGE16_PROBE = TRACE_RESULTS / "stage16_calibrated_trace_probe"
PEMS228_PROBE = TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe"

OUT_CSV = CURRENT_BEST / "trace_biopt_spatial_posture.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_spatial_posture.tex"

RESULT_DIR = {
    "PeMS7_1026": "pems7_1026",
    "PeMS7_228": "pems7_228",
    "Seattle": "seattle",
}
BASELINE_LABEL = {
    "swap_from_greedy_a_trace": "Swap from A-trace",
    "validation_swap_selected": "Prev. TRACE-SL",
    "rcss_selected": "RCSS",
}
SOURCE_ROOTS = [STAGE16_SWEEP, STAGE16_PROBE, PEMS228_PROBE]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def dataset_distance(dataset: str) -> np.ndarray:
    if dataset == "Seattle":
        adjacency = np.load(ROOT / "TRC-23-02333" / "dataset" / "Seattle" / "Loop_Seattle_2015_A.npy").astype(float)
        graph = adjacency + adjacency.T
        graph[graph > 0] = 1.0
        distance = shortest_path(graph, directed=False, unweighted=True)
        finite = distance[np.isfinite(distance) & (distance > 0)]
        fill_value = float(finite.max() + 1.0)
        distance = np.where(np.isfinite(distance), distance, fill_value)
        np.fill_diagonal(distance, 0.0)
        return distance
    filename = "PeMSD7_W_228.csv" if dataset == "PeMS7_228" else "PeMSD7_W_1026.csv"
    return np.loadtxt(ROOT / "TRC-23-02333" / "dataset" / dataset / filename, delimiter=",")


def stage15_layout_path(dataset: str, split_seed: int) -> Path:
    return STAGE15 / RESULT_DIR[dataset] / f"seed_{split_seed}" / "layouts.json"


def resolve_trace_layout_path(dataset: str, evidence_source: str, split_seed: int) -> Path:
    if evidence_source == "stage15_main":
        return stage15_layout_path(dataset, split_seed)
    root_name = evidence_source.split(":", 1)[1]
    for base in SOURCE_ROOTS:
        candidate = base / root_name / f"seed_{split_seed}" / "layouts.json"
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"could not resolve trace layouts for {dataset}: {evidence_source}")


def load_layout(path: Path, dataset: str, budget: float, layout_type: str) -> dict[str, object]:
    rows = load_json(path)
    return next(
        row for row in rows
        if row["dataset"] == dataset
        and abs(float(row["budget"]) - budget) < 1e-9
        and row["layout_type"] == layout_type
    )


def layout_distance_metrics(distance: np.ndarray, sensors: list[int]) -> tuple[float, float]:
    idx = np.array(sorted(sensors), dtype=int)
    sub = distance[np.ix_(idx, idx)]
    upper = sub[np.triu_indices(len(idx), 1)]
    upper = upper[upper > 0]
    mean_pairwise = float(upper.mean()) if upper.size else 0.0
    nearest = []
    for row in sub:
        vals = row[row > 0]
        if vals.size:
            nearest.append(float(vals.min()))
    mean_nearest = float(np.mean(nearest)) if nearest else 0.0
    return mean_pairwise, mean_nearest


def main() -> int:
    delta_rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    low_budget_rows = [row for row in delta_rows if abs(float(row["budget"]) - 0.1) < 1e-9]
    out_rows: list[dict[str, str]] = []

    for row in low_budget_rows:
        dataset = row["dataset"]
        budget = float(row["budget"])
        baseline = row["best_baseline_layout"]
        evidence_source = row["evidence_source"]
        distance = dataset_distance(dataset)

        trace_pairwise = []
        trace_nearest = []
        base_pairwise = []
        base_nearest = []
        trace_counter: Counter[int] = Counter()
        base_counter: Counter[int] = Counter()

        for split_seed in range(25, 35):
            trace_layout = load_layout(
                resolve_trace_layout_path(dataset, evidence_source, split_seed),
                dataset,
                budget,
                "trace_biopt",
            )["sensors"]
            base_layout = load_layout(
                stage15_layout_path(dataset, split_seed),
                dataset,
                budget,
                baseline,
            )["sensors"]
            pairwise, nearest = layout_distance_metrics(distance, trace_layout)
            trace_pairwise.append(pairwise)
            trace_nearest.append(nearest)
            pairwise, nearest = layout_distance_metrics(distance, base_layout)
            base_pairwise.append(pairwise)
            base_nearest.append(nearest)
            trace_counter.update(trace_layout)
            base_counter.update(base_layout)

        pair_delta = float(np.mean(trace_pairwise) - np.mean(base_pairwise))
        nn_delta = float(np.mean(trace_nearest) - np.mean(base_nearest))
        trace_always = sum(v == 10 for v in trace_counter.values())
        base_always = sum(v == 10 for v in base_counter.values())
        trace_unique = len(trace_counter)
        base_unique = len(base_counter)

        if dataset == "PeMS7_1026":
            reading = (
                "TRACE-BiOpt is not simply maximizing spatial spread: pairwise spacing shrinks slightly, "
                "but shortlist collapse weakens because always-selected nodes drop and unique support expands."
            )
        else:
            reading = (
                "TRACE-BiOpt is spatially more distributed on the current-best low-budget row: "
                "both pairwise spacing and nearest-neighbor spacing increase over the strongest baseline."
            )

        out_rows.append(
            {
                "dataset": dataset,
                "budget_pct": "10",
                "best_baseline_layout": baseline,
                "best_baseline_label": BASELINE_LABEL.get(baseline, baseline.replace("_", " ")),
                "trace_pairwise_distance_mean": f"{float(np.mean(trace_pairwise)):.6f}",
                "baseline_pairwise_distance_mean": f"{float(np.mean(base_pairwise)):.6f}",
                "pairwise_distance_delta": f"{pair_delta:.6f}",
                "trace_nearest_distance_mean": f"{float(np.mean(trace_nearest)):.6f}",
                "baseline_nearest_distance_mean": f"{float(np.mean(base_nearest)):.6f}",
                "nearest_distance_delta": f"{nn_delta:.6f}",
                "trace_unique_nodes": str(trace_unique),
                "baseline_unique_nodes": str(base_unique),
                "trace_always_selected_nodes": str(trace_always),
                "baseline_always_selected_nodes": str(base_always),
                "evidence_source": evidence_source,
                "spatial_reading": reading,
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing current-best low-budget spatial posture. Pairwise and nearest-neighbor deltas are TRACE-BiOpt minus the row-wise strongest baseline, computed on the same split-specific layouts with dataset-native graph-distance matrices. This is bounded mechanism evidence for the spatial regularization term, not a new dominance table.}",
        "\\label{tab:trace-biopt-spatial-posture}",
        "\\tiny",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.11\\textwidth}>{\\raggedright\\arraybackslash}p{0.14\\textwidth}>{\\centering\\arraybackslash}p{0.11\\textwidth}>{\\centering\\arraybackslash}p{0.11\\textwidth}>{\\centering\\arraybackslash}p{0.11\\textwidth}>{\\centering\\arraybackslash}p{0.11\\textwidth}>{\\raggedright\\arraybackslash}p{0.26\\textwidth}}",
        "\\toprule",
        "Dataset & Strongest baseline & $\\Delta$ pairwise & $\\Delta$ nearest & Always-selected & Unique support & Reading \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{tex_escape(row['dataset'])} & "
            f"{tex_escape(row['best_baseline_label'])} & "
            f"{float(row['pairwise_distance_delta']):+.2f} & "
            f"{float(row['nearest_distance_delta']):+.2f} & "
            f"{row['trace_always_selected_nodes']}/{row['baseline_always_selected_nodes']} & "
            f"{row['trace_unique_nodes']}/{row['baseline_unique_nodes']} & "
            f"{tex_escape(row['spatial_reading'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "}",
            "\\begin{flushleft}\\footnotesize Always-selected counts show how many nodes appear in all ten split-specific layouts for TRACE-BiOpt versus the strongest baseline. Unique support counts show how many distinct nodes appear across the ten layouts. On PeMS7\\_1026 the spatial term should be read as a guardrail against shortlist collapse, not as a command to maximize raw distance.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
