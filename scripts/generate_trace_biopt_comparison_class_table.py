#!/usr/bin/env python3
"""Generate a Related Work comparison-class contract table for TRACE-BiOpt."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_comparison_class_contract.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_comparison_class_contract.tex"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def main() -> int:
    contract = load_json(CURRENT_BEST / "trace_biopt_claim_contract.json")
    significance_summary = load_csv(CURRENT_BEST / "trace_biopt_significance_posture_summary.csv")
    exact_summary = load_csv(CURRENT_BEST / "trace_biopt_exact_subnetwork_summary.csv")
    baseline_family_screen = load_csv(CURRENT_BEST / "trace_biopt_baseline_family_screen.csv")

    baseline_count = len(contract["aggregate_claim"]["baseline_registry"])
    family_count = len(baseline_family_screen)
    row_count = int(contract["aggregate_claim"]["row_count"])
    aggregate_significance = next(row for row in significance_summary if row["dataset"] == "All rows")
    corrected_wins = int(aggregate_significance["significantly_worse_baselines_holm"])
    corrected_total = int(aggregate_significance["baseline_count"])
    exact_hits = sum(int(row["exact_hits"]) for row in exact_summary)
    exact_cases = sum(int(row["exact_cases"]) for row in exact_summary)

    rows = [
        {
            "axis": "Decision timing",
            "trace_biopt_contract": "Freeze one sparse siting plan before most future traffic states are observed.",
            "paper_should_not_be_read_as": "A benchmark that starts after the sensor graph is already fixed.",
        },
        {
            "axis": "Optimized quantity",
            "trace_biopt_contract": "Optimize hidden-state recoverability under one transparent GLS/MAP inverse problem.",
            "paper_should_not_be_read_as": "Coverage maximization, OD identifiability, observability only, or a pure graph-sampling score.",
        },
        {
            "axis": "Method identity",
            "trace_biopt_contract": "Solve one fixed-infrastructure transportation network-design method centered on one recoverability-driven bilevel stochastic objective and one deterministic solver route.",
            "paper_should_not_be_read_as": "A pool of candidate generators, a portfolio selector, or a post-hoc AutoML layout chooser.",
        },
        {
            "axis": "Role of baselines",
            "trace_biopt_contract": f"Keep {baseline_count} pre-registered baselines spanning {family_count} audited method families outside the solver as an external audited comparison class.",
            "paper_should_not_be_read_as": "A method that quietly reuses baselines as internal candidates and then reports the winner as new.",
        },
        {
            "axis": "Empirical claim",
            "trace_biopt_contract": f"On the current-best chain, all {row_count}/{row_count} rows are submission-ready paired wins and Holm-corrected paired tests still show {corrected_wins}/{corrected_total} significant wins with no surviving challenger.",
            "paper_should_not_be_read_as": "A weak-baseline benchmark win that survives only because the comparison class is narrow or uncorrected.",
        },
        {
            "axis": "Explicit scope",
            "trace_biopt_contract": f"Keep global optimality and untested-baseline dominance out of scope while exact-hitting {exact_hits}/{exact_cases} audited 16-node subnetworks with zero objective gap.",
            "paper_should_not_be_read_as": "A paper that silently upgrades bounded evidence into universal exactness or universal superiority.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{TRACE-BiOpt comparison-class contract. The table states how a TR-B reader should classify the paper before entering the detailed literature split.}",
        "\\label{tab:trace-biopt-comparison-class-contract}",
        "\\small",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\raggedright\\arraybackslash}p{0.34\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Reading axis & TRACE-BiOpt contract & The paper should not be read as \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['axis'])} & {tex_escape(row['trace_biopt_contract'])} & {tex_escape(row['paper_should_not_be_read_as'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_TEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
