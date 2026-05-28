#!/usr/bin/env python3
"""Generate current-best TRACE-BiOpt objective-mix figure."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
STAGE16_SWEEP = TRACE_RESULTS / "stage16_calibrated_trace_sweep"
STAGE16_PROBE = TRACE_RESULTS / "stage16_calibrated_trace_probe"
PEMS228_PROBE = TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe"

OUT_CSV = CURRENT_BEST / "trace_biopt_objective_mix_summary.csv"
OUT_FIG = ROOT / "paper" / "figures" / "fig_trace_biopt_objective_mix.pdf"

DATASET_DIR = {
    "PeMS7_1026": "pems7_1026",
    "PeMS7_228": "pems7_228",
    "Seattle": "seattle",
}
SOURCE_ROOTS = [STAGE16_SWEEP, STAGE16_PROBE, PEMS228_PROBE]
COMPONENTS = [
    ("reconstruction_share_pct", "Huber recon.", "#1f77b4"),
    ("posterior_share_pct", "Posterior", "#ff7f0e"),
    ("cvar_share_pct", "CVaR", "#2ca02c"),
    ("spatial_share_pct", "Spatial", "#9467bd"),
]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_root(dataset: str, evidence_source: str) -> Path:
    if evidence_source == "stage15_main":
        return STAGE15 / DATASET_DIR[dataset]
    root_name = evidence_source.split(":", 1)[1]
    for base in SOURCE_ROOTS:
        candidate = base / root_name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(evidence_source)


def build_rows() -> list[dict[str, object]]:
    rows = []
    current_rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    for row in current_rows:
        dataset = row["dataset"]
        budget = float(row["budget"])
        root = resolve_root(dataset, row["evidence_source"])
        recon_vals = []
        post_vals = []
        cvar_vals = []
        spatial_vals = []
        for split_seed in range(25, 35):
            history = load_json(root / f"seed_{split_seed}" / "trace_biopt_history.json")
            entry = next(item for item in history if abs(float(item["budget"]) - budget) < 1e-9)
            terms = entry["final_terms"]
            weights = entry["weights"]
            recon = float(terms["reconstruction_huber"])
            post = float(weights["beta"]) * float(terms["posterior_trace_per_node"])
            cvar = float(weights["gamma"]) * float(terms["scenario_cvar_trace_per_node"])
            spatial = float(weights["eta"]) * float(terms["spatial_penalty"])
            total = recon + post + cvar + spatial
            recon_vals.append(100.0 * recon / total if total else 0.0)
            post_vals.append(100.0 * post / total if total else 0.0)
            cvar_vals.append(100.0 * cvar / total if total else 0.0)
            spatial_vals.append(100.0 * spatial / total if total else 0.0)
        rows.append(
            {
                "dataset": dataset,
                "budget": budget,
                "budget_pct": int(round(budget * 100)),
                "evidence_source": row["evidence_source"],
                "reconstruction_share_pct": f"{mean(recon_vals):.6f}",
                "posterior_share_pct": f"{mean(post_vals):.6f}",
                "cvar_share_pct": f"{mean(cvar_vals):.6f}",
                "spatial_share_pct": f"{mean(spatial_vals):.6f}",
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    rows = sorted(
        build_rows(),
        key=lambda row: (["PeMS7_1026", "PeMS7_228", "Seattle"].index(row["dataset"]), float(row["budget"])),
    )
    write_csv(OUT_CSV, rows)

    labels = [f"{row['dataset'].replace('PeMS7_', 'PeMS')}\n{int(row['budget_pct'])}%" for row in rows]
    x = np.arange(len(rows))
    fig, ax = plt.subplots(figsize=(10.6, 4.4), constrained_layout=True)
    bottom = np.zeros(len(rows))
    for field, label, color in COMPONENTS:
        values = np.array([float(row[field]) for row in rows], dtype=float)
        ax.bar(x, values, bottom=bottom, width=0.72, color=color, label=label)
        bottom += values

    ax.set_ylim(0, 100)
    ax.set_ylabel("Share of final objective (%)")
    ax.set_xticks(x, labels)
    ax.grid(True, axis="y", alpha=0.22)
    ax.legend(loc="upper center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.12))
    fig.savefig(OUT_FIG, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT_FIG} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
