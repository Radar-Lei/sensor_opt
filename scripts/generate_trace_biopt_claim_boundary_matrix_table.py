#!/usr/bin/env python3
"""Generate reviewer-facing claim-boundary matrix for TRACE-BiOpt."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
PAPER_SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
OUT_CSV = CURRENT_BEST / "trace_biopt_claim_boundary_matrix.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_claim_boundary_matrix.tex"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def main() -> int:
    contract = load_json(CURRENT_BEST / "trace_biopt_claim_contract.json")
    provenance = load_csv(CURRENT_BEST / "trace_biopt_current_best_provenance.csv")
    robustness_frontier = load_csv(PAPER_SOURCES / "robustness_frontier_summary.csv")

    row_count = int(contract["aggregate_claim"]["row_count"])
    baseline_count = len(contract["aggregate_claim"]["baseline_registry"])
    promoted_rows = sum(row["source"] == "Stage16 calibrated rerun" for row in provenance)
    paired_ready_rows = sum(row["claim_status"] == "supported_submission_ready" for row in contract["rows"])
    graph_wins = sum(row["winner_family"] == "graph-spectral" for row in robustness_frontier)

    rows = [
        {
            "claim_lane": "Main empirical dominance",
            "paper_can_say": f"TRACE-BiOpt is rank 1 against the row-wise strongest audited non-BiOpt baseline drawn from {baseline_count} pre-registered comparators on all {row_count}/{row_count} tested dataset-budget rows, with {paired_ready_rows}/{row_count} submission-ready paired wins.",
            "supporting_artifacts": "Current-best dominance table; full baseline matrix; claim contract; paired-delta tests.",
            "explicit_non_claim": "Does not imply dominance over untested baselines, other budgets, or other traffic networks.",
        },
        {
            "claim_lane": "Calibrated rerun promotion",
            "paper_can_say": f"{promoted_rows}/{row_count} current-best rows are already promoted from complete replaceable Stage16 calibrated reruns under the same TRACE-BiOpt objective family.",
            "supporting_artifacts": "Replacement gate; current-best provenance table; Stage16 progress summary.",
            "explicit_non_claim": "Rows without completed calibrated reruns remain backed by the Stage15 main evidence chain.",
        },
        {
            "claim_lane": "Theory and solver scope",
            "paper_can_say": "The lower-level MAP solve is explicit and stable; posterior trace has Bayes-risk meaning; validation generalization is stated over all size-k layouts; and the solver returns a searched-neighborhood stationarity certificate.",
            "supporting_artifacts": "Method section theorem blocks; theory table; proof audit artifacts.",
            "explicit_non_claim": "Does not prove exact global optimality, universal MAE improvement, or robustness outside the stated assumptions.",
        },
        {
            "claim_lane": "Mechanism and regime diagnostics",
            "paper_can_say": "Calibration-sensitive, search-budget-sensitive, and certificate-sensitive regimes are identified inside the same TRACE-BiOpt objective family rather than by switching methods.",
            "supporting_artifacts": "Mechanism table; calibration-alignment figure; objective-mix figure; weight-sensitivity table; design protocol table.",
            "explicit_non_claim": "These diagnostics explain why current-best rows behave as they do; they are not extra dominance rows or universal monotonicity theorems.",
        },
        {
            "claim_lane": "Bounded deployment stress evidence",
            "paper_can_say": f"The bounded Stage14 PeMS7_228 frontier is graph-spectral on {graph_wins}/9 tested stress slices, with deployment posture changing most under block-missing and narrow failure/drift gaps.",
            "supporting_artifacts": "Robustness routing table; stress frontier table; deployment stress posture table.",
            "explicit_non_claim": "These stress slices remain stress-test-only evidence and do not become TRACE-BiOpt robustness dominance claims.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["claim_lane", "paper_can_say", "supporting_artifacts", "explicit_non_claim"],
        )
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing TRACE-BiOpt claim-boundary matrix. The table states what each evidence lane supports and what the manuscript explicitly refuses to claim.}",
        "\\label{tab:trace-biopt-claim-boundary-matrix}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.17\\textwidth}>{\\raggedright\\arraybackslash}p{0.29\\textwidth}>{\\raggedright\\arraybackslash}p{0.23\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Claim lane & What the paper can say & Supporting artifact lane & Explicit non-claim \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['claim_lane'])} & {tex_escape(row['paper_can_say'])} & "
            f"{tex_escape(row['supporting_artifacts'])} & {tex_escape(row['explicit_non_claim'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
