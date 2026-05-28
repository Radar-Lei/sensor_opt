#!/usr/bin/env python3
"""Generate a reviewer-facing Theorem T3 generalization-burden table."""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
DATASET_ROOT = ROOT / "TRC-23-02333" / "dataset"
DELTA_CSV = CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_generalization_burden.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_generalization_burden.tex"

SLOTS_PER_DAY = 288
VALIDATION_DAYS = 2
DELTA = 0.05
CURRENT_BEST_SOURCE_LABELS = {
    "stage15_main": "Stage15 main evidence",
}


def load_delta_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def count_pems_nodes(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as handle:
        return len(next(csv.reader(handle)))


def count_seattle_nodes(path: Path) -> int:
    tensor = np.load(path)["arr_0"]
    return int(tensor.shape[0])


def dataset_node_counts() -> dict[str, int]:
    return {
        "PeMS7_1026": count_pems_nodes(DATASET_ROOT / "PeMS7_1026" / "PeMSD7_V_1026.csv"),
        "PeMS7_228": count_pems_nodes(DATASET_ROOT / "PeMS7_228" / "PeMSD7_V_228.csv"),
        "Seattle": count_seattle_nodes(DATASET_ROOT / "Seattle" / "tensor.npz"),
    }


def source_label(row: dict[str, str]) -> str:
    evidence_source = row["evidence_source"]
    if evidence_source.startswith("stage16_replaceable:"):
        return "Stage16 calibrated rerun"
    return CURRENT_BEST_SOURCE_LABELS.get(evidence_source, evidence_source)


def practical_reading(dataset: str, budget_pct: int) -> str:
    if dataset == "PeMS7_1026" and budget_pct == 30:
        return "largest all-layout validation burden under the same two-day window"
    if dataset == "PeMS7_1026":
        return "high combinatorial burden; stronger calibration/search support is most valuable here"
    if dataset == "PeMS7_228" and budget_pct == 10:
        return "smallest all-layout validation burden among the nine main rows"
    if dataset == "Seattle":
        return "mid-scale validation burden between the two PeMS extremes"
    return "moderate burden within the common two-day validation window"


def main() -> int:
    node_counts = dataset_node_counts()
    n_v = VALIDATION_DAYS * SLOTS_PER_DAY
    out_rows: list[dict[str, str]] = []
    for row in load_delta_rows(DELTA_CSV):
        dataset = row["dataset"]
        budget = float(row["budget"])
        budget_pct = int(round(budget * 100))
        node_count = node_counts[dataset]
        sensor_count = int(round(node_count * budget))
        log_layout_count = (
            math.lgamma(node_count + 1)
            - math.lgamma(sensor_count + 1)
            - math.lgamma(node_count - sensor_count + 1)
        ) / math.log(10.0)
        union_term = sensor_count * math.log(math.e * node_count / sensor_count)
        bound_factor = math.sqrt((union_term + math.log(2.0 / DELTA)) / (2.0 * n_v))
        out_rows.append(
            {
                "dataset": dataset,
                "budget": f"{budget:.1f}",
                "budget_pct": str(budget_pct),
                "node_count": str(node_count),
                "sensor_count": str(sensor_count),
                "validation_days": str(VALIDATION_DAYS),
                "slots_per_day": str(SLOTS_PER_DAY),
                "n_v": str(n_v),
                "delta": f"{DELTA:.2f}",
                "log10_layout_family_size": f"{log_layout_count:.6f}",
                "union_term": f"{union_term:.6f}",
                "uniform_gap_factor_over_B": f"{bound_factor:.6f}",
                "evidence_source_label": source_label(row),
                "practical_reading": practical_reading(dataset, budget_pct),
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Theorem~\\ref{thm:uniform-layout} burden factors under the common two-day validation window used by the current-best evidence chain.}",
        "\\label{tab:trace-biopt-generalization-burden}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{lccccc>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Dataset & Budget & $k$ & $\\log_{10}|\\mathfrak{S}_k|$ & $k\\log(e|\\calV|/k)$ & $B^{-1}\\Delta_{\\mathrm{unif}}$ & Reading \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{tex_escape(row['dataset'])} & "
            f"{row['budget_pct']}\\% & "
            f"{row['sensor_count']} & "
            f"{float(row['log10_layout_family_size']):.1f} & "
            f"{float(row['union_term']):.1f} & "
            f"{float(row['uniform_gap_factor_over_B']):.3f} & "
            f"{tex_escape(row['practical_reading'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabularx}",
            "\\begin{flushleft}\\footnotesize Here $n_v=2\\times 288=576$ validation slots and $\\delta=0.05$ for every row. $\\Delta_{\\mathrm{unif}}=B\\sqrt{(k\\log(e|\\calV|/k)+\\log(2/\\delta))/(2n_v)}$ is the theorem's uniform validation-to-deployment deviation term. The selected-layout excess-risk term is $2\\Delta_{\\mathrm{unif}}+\\epsilon_{\\mathrm{opt}}$, so the table is a validation-burden diagnostic rather than an empirical dominance claim by itself.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
