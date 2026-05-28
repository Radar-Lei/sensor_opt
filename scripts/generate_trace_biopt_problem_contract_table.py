#!/usr/bin/env python3
"""Generate a Section 3 problem-contract table for TRACE-BiOpt."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_problem_contract.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_problem_contract.tex"


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
    baseline_family_screen = load_csv(CURRENT_BEST / "trace_biopt_baseline_family_screen.csv")

    baseline_count = len(contract["aggregate_claim"]["baseline_registry"])
    family_count = len(baseline_family_screen)
    row_count = int(contract["aggregate_claim"]["row_count"])
    aggregate_significance = next(row for row in significance_summary if row["dataset"] == "All rows")
    corrected_wins = int(aggregate_significance["significantly_worse_baselines_holm"])
    corrected_total = int(aggregate_significance["baseline_count"])

    rows = [
        {
            "contract_axis": "Decision timing",
            "paper_visible_statement": "Freeze one sparse siting plan before most future traffic states are observed, then judge it on downstream hidden-state recoverability.",
            "reviewer_reading": "The decision is a long-lived fixed-infrastructure transportation network-design choice, not a layout tuned after the graph is already observed.",
        },
        {
            "contract_axis": "Target quantity",
            "paper_visible_statement": "Optimize hidden-state recoverability rather than coverage, visibility, OD identifiability, or a pure graph score.",
            "reviewer_reading": "The problem is about the recoverability of the hidden network state, not only the visibility of the observed subset.",
        },
        {
            "contract_axis": "Bilevel structure",
            "paper_visible_statement": "The lower level is one transparent GLS/MAP inverse problem and the upper level is one recoverability-driven bilevel stochastic design objective.",
            "reviewer_reading": "TRACE-BiOpt solves one transparent inverse problem inside one bilevel stochastic transportation network-design formulation rather than composing unrelated heuristics.",
        },
        {
            "contract_axis": "Deployment-time split discipline",
            "paper_visible_statement": "Training estimates reconstruction ingredients, validation drives the design objective and deterministic exchange search, and test data stay held out until the siting rule is frozen.",
            "reviewer_reading": "The problem definition is deployment-facing: validation calibrates the design, while test data remain final evidence rather than another tuning loop.",
        },
        {
            "contract_axis": "External comparison class",
            "paper_visible_statement": f"The {baseline_count} pre-registered baselines across {family_count} audited families stay outside the problem as an external audited comparison class, and the current-best chain leaves no surviving challenger after {corrected_wins}/{corrected_total} Holm-corrected paired wins.",
            "reviewer_reading": "Baselines test the solved design after the rule is frozen; they are not internal candidates in the optimization problem.",
        },
        {
            "contract_axis": "Explicit problem scope",
            "paper_visible_statement": f"The empirical claim is row-wise hidden-state reconstruction dominance on {row_count}/{row_count} submission-ready rows, not universal observability, universal exactness, or dominance over untested baselines.",
            "reviewer_reading": "The problem contract is strong but bounded: it is a recoverability-driven siting problem under explicit evidence and theory limits.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{TRACE-BiOpt problem contract. The table compresses the Section~3 problem definition into the deployment-time decision, hidden-state target, bilevel structure, split discipline, external comparison class, and explicit scope that a reviewer should carry into the method and experiments.}",
        "\\label{tab:trace-biopt-problem-contract}",
        "\\small",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.19\\textwidth}>{\\raggedright\\arraybackslash}p{0.41\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Contract axis & Paper-visible statement & Reviewer-facing reading \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['contract_axis'])} & {tex_escape(row['paper_visible_statement'])} & {tex_escape(row['reviewer_reading'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_TEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
