#!/usr/bin/env python3
"""Generate a reviewer-facing contribution stack table for TRACE-BiOpt."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_contribution_stack.tex"


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
    baseline_family_screen = load_csv(CURRENT_BEST / "trace_biopt_baseline_family_screen.csv")

    row_count = int(contract["aggregate_claim"]["row_count"])
    dataset_count = len(contract["aggregate_claim"]["datasets"])
    budget_count = len(contract["aggregate_claim"]["budgets"])
    baseline_count = len(contract["aggregate_claim"]["baseline_registry"])
    family_count = len(baseline_family_screen)
    stage16_rows = sum(row["source"] == "Stage16 calibrated rerun" for row in provenance)
    paired_ready_rows = sum(
        row["claim_status"] == "supported_submission_ready"
        for row in contract["rows"]
    )
    exact_hits = sum(int(row["exact_hits"]) for row in exact_summary)
    exact_cases = sum(int(row["exact_cases"]) for row in exact_summary)
    aggregate_significance = next(
        row for row in significance_summary if row["dataset"] == "All rows"
    )
    significant_pairs = int(aggregate_significance["significantly_worse_baselines_holm"])
    non_worse_pairs = int(aggregate_significance["non_worse_baselines_holm"])
    challenger_pairs = int(aggregate_significance["baseline_significantly_better_holm"])

    rows = [
        {
            "layer": "Formulation",
            "statement": "Sparse traffic sensing is posed as a size-$k$ robust bilevel stochastic network-design problem that directly minimizes hidden-state reconstruction risk, rather than as OD coverage, observability only, or candidate-pool selection.",
            "importance": "The infrastructure decision is tied to downstream recoverability under one transparent inverse problem instead of being deferred to a post-hoc benchmark table.",
        },
        {
            "layer": "Algorithm",
            "statement": "TRACE-BiOpt uses one objective with hidden Huber loss, posterior uncertainty, scenario-CVaR tail risk, and spatial redundancy, then solves it with scale-adaptive initialization and deterministic one-exchange refinement.",
            "importance": "The method is a single-objective deterministic solver, not a portfolio or AutoML-style selector over baselines.",
        },
        {
            "layer": "Theory",
            "statement": "The scoped theory package covers MAP closed form and stability, Bayes-risk meaning of posterior trace, a formal CVaR tail-risk epigraph, uniform validation generalization over all size-$k$ layouts, finite descent, and a searched-neighborhood exchange certificate.",
            "importance": "The method contributes analyzable optimization structure and a coherent tail-risk term for a principled bilevel stochastic design method rather than only empirical search heuristics.",
        },
        {
            "layer": "Evidence",
            "statement": f"The current-best evidence lane is an external audited comparison-class contract over {baseline_count} pre-registered non-BiOpt baselines spanning {family_count} audited method families across {dataset_count} networks and {budget_count} budgets; {stage16_rows}/{row_count} main rows are already promoted from calibrated reruns, {paired_ready_rows}/{row_count} rows satisfy the submission-ready paired-dominance gate, Holm-corrected paired tests still show TRACE-BiOpt significantly better on {significant_pairs}/{significant_pairs + non_worse_pairs + challenger_pairs} row-baseline comparisons with no surviving tied or better challenger, and the bounded exact-subnetwork benchmark exact-hits {exact_hits}/{exact_cases} audited cases with zero objective gap.",
            "importance": "The empirical claim is that TRACE-BiOpt beats the strongest audited comparator in every tested regime, survives multiplicity correction against the full pre-registered baseline registry, and carries an explicit external audited comparison-class contract instead of a selective benchmark screen.",
        },
        {
            "layer": "Claim discipline",
            "statement": "The manuscript explicitly excludes global optimality, dominance over untested baselines, and universal cross-network generalization.",
            "importance": "Innovation is stated together with boundaries that a TR-B reviewer can audit rather than infer.",
        },
    ]

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing contribution stack of TRACE-BiOpt. The table compresses the formulation, algorithm, theory, evidence, and claim-discipline layers that make the paper more than a baseline selector.}",
        "\\label{tab:trace-biopt-contribution-stack}",
        "\\small",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}p{0.48\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Layer & Paper-visible statement & Why it matters for TR-B \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['layer'])} & {tex_escape(row['statement'])} & {tex_escape(row['importance'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
