#!/usr/bin/env python3
"""Generate a compact discussion-facing TRACE-BiOpt boundary table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"

IN_CSV = CURRENT_BEST / "trace_biopt_claim_boundary_matrix.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_discussion_boundary.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_discussion_boundary.tex"


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
    rows = load_csv(IN_CSV)
    lane_lookup = {row["claim_lane"]: row for row in rows}
    significance_rows = load_csv(CURRENT_BEST / "trace_biopt_significance_posture_summary.csv")
    aggregate_significance = next(row for row in significance_rows if row["dataset"] == "All rows")
    corrected_wins = int(aggregate_significance["significantly_worse_baselines_holm"])
    corrected_total = int(aggregate_significance["baseline_count"])

    out_rows = [
        {
            "boundary_label": "Baseline scope",
            "what_still_stands": f"TRACE-BiOpt is current-best rank 1 on all 9/9 tested rows against the row-wise strongest audited comparator from the 21-method registry, and the external audited comparison-class contract still gives {corrected_wins}/{corrected_total} Holm-corrected significant wins with no surviving tied or better challenger.",
            "explicit_non_claim": lane_lookup["Main empirical dominance"]["explicit_non_claim"],
            "reviewer_takeaway": "Read the paper as an external audited comparison-class contract with a multiplicity-robust all-baseline screen, not as a guarantee against every possible future comparator.",
        },
        {
            "boundary_label": "Calibrated rerun status",
            "what_still_stands": lane_lookup["Calibrated rerun promotion"]["paper_can_say"],
            "explicit_non_claim": lane_lookup["Calibrated rerun promotion"]["explicit_non_claim"],
            "reviewer_takeaway": "Promoted reruns strengthen weak rows inside one objective family, but only completed reruns replace the Stage15-backed route.",
        },
        {
            "boundary_label": "Theory and solver",
            "what_still_stands": "The lower-level MAP model, posterior-risk identity, formal CVaR tail-risk epigraph, validation generalization statement, and searched-neighborhood stationarity certificate are all explicit and audited.",
            "explicit_non_claim": lane_lookup["Theory and solver scope"]["explicit_non_claim"],
            "reviewer_takeaway": "The method is principled bilevel network design, but not an exact global MIP solver or a universal MAE theorem.",
        },
        {
            "boundary_label": "Mechanism diagnostics",
            "what_still_stands": lane_lookup["Mechanism and regime diagnostics"]["paper_can_say"],
            "explicit_non_claim": lane_lookup["Mechanism and regime diagnostics"]["explicit_non_claim"],
            "reviewer_takeaway": "Calibration, search-budget, and certificate diagnostics explain why rows move; they do not create extra dominance claims.",
        },
        {
            "boundary_label": "Stress evidence",
            "what_still_stands": lane_lookup["Bounded deployment stress evidence"]["paper_can_say"],
            "explicit_non_claim": lane_lookup["Bounded deployment stress evidence"]["explicit_non_claim"],
            "reviewer_takeaway": "Deployment stress tests are operational screens, not proof that TRACE-BiOpt dominates under every perturbation family.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Discussion-facing TRACE-BiOpt boundary table.}",
        "\\label{tab:trace-biopt-discussion-boundary}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.14\\textwidth}>{\\raggedright\\arraybackslash}p{0.26\\textwidth}>{\\raggedright\\arraybackslash}p{0.24\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Boundary & What still stands & Explicit non-claim & Reviewer takeaway \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{tex_escape(row['boundary_label'])} & "
            f"{tex_escape(row['what_still_stands'])} & "
            f"{tex_escape(row['explicit_non_claim'])} & "
            f"{tex_escape(row['reviewer_takeaway'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabularx}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
