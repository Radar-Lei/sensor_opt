#!/usr/bin/env python3
"""Generate reviewer-facing regime lessons from current-best TRACE-BiOpt evidence."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
STAGE15 = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined"
OUT_CSV = CURRENT_BEST / "trace_biopt_regime_lessons.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_regime_lessons.tex"


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


def regime_label(dataset: str, budget: float) -> str:
    return f"{dataset} {int(round(budget * 100))}%"


def comparator_family(layout: str) -> str:
    if layout == "rcss_selected":
        return "RCSS selector"
    if layout == "swap_from_greedy_a_trace":
        return "A-trace swap family"
    if layout == "validation_swap_selected":
        return "prior TRACE-SL swap family"
    return layout


def evidence_lane(source: str) -> str:
    if source.startswith("stage16_replaceable:"):
        return "Stage16 calibrated rerun"
    return "Stage15 main evidence"


def search_signal(no_improving: int, exhausted: int) -> str:
    if exhausted > no_improving:
        return "search-budget sensitive"
    if no_improving > exhausted:
        return "searched-neighborhood stable"
    return "mixed stop signal"


def lesson(row: dict[str, str], opt: dict[str, str]) -> str:
    dataset = row["dataset"]
    budget = float(row["budget"])
    source = row["evidence_source"]
    baseline = row["best_baseline_layout"]
    no_improving = int(opt["no_improving_stop_runs"])
    exhausted = int(opt["exchange_budget_exhausted_runs"])

    if source.startswith("stage16_replaceable:") and dataset == "PeMS7_228" and budget == 0.1:
        return "Thin validation windows can mis-rank low-budget layouts; calibrating reconstruction risk on train+validation resolves the row."
    if source.startswith("stage16_replaceable:") and dataset == "PeMS7_1026" and budget == 0.3:
        return "Large networks need both calibrated risk estimation and more search budget to convert a weak margin into a stable paired win."
    if baseline == "rcss_selected":
        return "TRACE-BiOpt beats a certificate-ranked selector directly, so the gain is not only from candidate-pool curation."
    if baseline == "swap_from_greedy_a_trace":
        return "Direct A-trace local search is insufficient once hidden-state risk, tail risk, and redundancy are optimized jointly."
    if exhausted > no_improving:
        return "The regime benefits from more aggressive searched one-exchange refinement because the declared budget often binds before local stability."
    return "The dominant gain is robust direct optimization of reconstruction risk over the prior TRACE-SL swap family under the same evaluation protocol."


def main() -> int:
    delta_rows = sorted(
        load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"),
        key=lambda row: (row["dataset"], float(row["budget"])),
    )
    opt_rows = {
        (row["dataset"], float(row["budget"])): row
        for row in load_csv(STAGE15 / "trace_biopt_optimization_diagnostics.csv")
    }

    output_rows = []
    for row in delta_rows:
        key = (row["dataset"], float(row["budget"]))
        opt = opt_rows[key]
        output_rows.append(
            {
                "regime": regime_label(row["dataset"], float(row["budget"])),
                "best_baseline_family": comparator_family(row["best_baseline_layout"]),
                "evidence_lane": evidence_lane(row["evidence_source"]),
                "search_signal": search_signal(int(opt["no_improving_stop_runs"]), int(opt["exchange_budget_exhausted_runs"])),
                "lesson": lesson(row, opt),
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["regime", "best_baseline_family", "evidence_lane", "search_signal", "lesson"],
        )
        writer.writeheader()
        writer.writerows(output_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing regime lessons from the current-best TRACE-BiOpt evidence chain. The table translates row-level strongest-baseline, replacement-route, and optimization-certificate evidence into transport-design interpretation.}",
        "\\label{tab:trace-biopt-regime-lessons}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}p{0.17\\textwidth}>{\\raggedright\\arraybackslash}p{0.17\\textwidth}>{\\raggedright\\arraybackslash}p{0.17\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Regime & Strongest non-BiOpt family & Evidence lane & Search signal & Main lesson \\\\",
        "\\midrule",
    ]
    for row in output_rows:
        lines.append(
            f"{tex_escape(row['regime'])} & {tex_escape(row['best_baseline_family'])} & "
            f"{tex_escape(row['evidence_lane'])} & {tex_escape(row['search_signal'])} & "
            f"{tex_escape(row['lesson'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
