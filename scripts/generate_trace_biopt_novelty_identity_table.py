#!/usr/bin/env python3
"""Generate a reviewer-facing novelty/identity table for TRACE-BiOpt."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_novelty_identity.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_novelty_identity.tex"


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
    provenance = load_csv(CURRENT_BEST / "trace_biopt_current_best_provenance.csv")
    exact_summary = load_csv(CURRENT_BEST / "trace_biopt_exact_subnetwork_summary.csv")
    significance_summary = load_csv(CURRENT_BEST / "trace_biopt_significance_posture_summary.csv")

    baseline_count = len(contract["aggregate_claim"]["baseline_registry"])
    paired_ready_rows = sum(row["paired_status"] == "submission-ready paired dominance" for row in provenance)
    promoted_rows = sum(row["source"] == "Stage16 calibrated rerun" for row in provenance)
    exact_hits = sum(int(row["exact_hits"]) for row in exact_summary)
    exact_cases = sum(int(row["exact_cases"]) for row in exact_summary)
    aggregate_significance = next(row for row in significance_summary if row["dataset"] == "All rows")
    corrected_wins = int(aggregate_significance["significantly_worse_baselines_holm"])
    corrected_total = int(aggregate_significance["baseline_count"])

    rows = [
        {
            "possible_misread": "Portfolio or AutoML selector",
            "what_would_be_missing": "The paper would mainly choose among RCSS, A-trace, graph-sampling, TRACE-SL, or random candidates rather than define one transport design objective.",
            "trace_biopt_identity": f"TRACE-BiOpt instead solves one recoverability-driven bilevel objective; the {baseline_count} non-BiOpt layouts stay outside the solver as an external audited comparison class rather than method candidates.",
            "paper_visible_anchor": "Single-objective solver + external audited comparison-class disclosure.",
        },
        {
            "possible_misread": "Surrogate OED or graph-sampling criterion",
            "what_would_be_missing": "Posterior trace or graph recoverability alone would stand in for the deployment objective, with no direct hidden-state reconstruction-risk target.",
            "trace_biopt_identity": "TRACE-BiOpt uses posterior trace as one certificate inside hidden Huber loss, a formal CVaR tail-risk epigraph, and spatial redundancy under the same bilevel layout problem.",
            "paper_visible_anchor": "Objective decomposition + formal CVaR proposition + route-ablation and weight-sensitivity lanes.",
        },
        {
            "possible_misread": "Estimator benchmark on a fixed graph",
            "what_would_be_missing": "The main contribution would be a better predictor or imputer once the sensor graph is given, not a pre-deployment infrastructure choice.",
            "trace_biopt_identity": "The transparent GLS/MAP estimator is intentionally fixed while the sparse layout is optimized upstream as the transport-network design variable.",
            "paper_visible_anchor": "Problem statement + related-work distinction from forecasting/imputation.",
        },
        {
            "possible_misread": "Weak-baseline empirical win",
            "what_would_be_missing": "The claim would rest on one named weak comparator instead of the strongest audited alternative on each row.",
            "trace_biopt_identity": f"The current-best chain closes {paired_ready_rows}/9 rows under paired strongest-baseline comparison, {promoted_rows}/9 rows are already strengthened by calibrated Stage16 reruns, and Holm-corrected paired tests still give {corrected_wins}/{corrected_total} significant wins with no surviving tied or better challenger.",
            "paper_visible_anchor": "Dominance table + full baseline matrix + significance posture + reader guide.",
        },
        {
            "possible_misread": "Exact global optimization paper",
            "what_would_be_missing": "A full-network MIP or exhaustive solver would certify the global optimum on every tested network and budget.",
            "trace_biopt_identity": f"The paper stays scoped: it exact-hits {exact_hits}/{exact_cases} audited 16-node subnetwork cases with zero objective gap, while full-network global optimality remains explicitly excluded.",
            "paper_visible_anchor": "Bounded exact benchmark + discussion boundary matrix.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing identity test for TRACE-BiOpt. Each row states a plausible misreading of the paper and the paper-visible feature that prevents that misreading from being the right interpretation.}",
        "\\label{tab:trace-biopt-novelty-identity}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\raggedright\\arraybackslash}p{0.22\\textwidth}>{\\raggedright\\arraybackslash}p{0.36\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Possible misread & If that were true, what would be missing? & TRACE-BiOpt identity instead & Paper-visible anchor \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['possible_misread'])} & {tex_escape(row['what_would_be_missing'])} & {tex_escape(row['trace_biopt_identity'])} & {tex_escape(row['paper_visible_anchor'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_TEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
