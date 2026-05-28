#!/usr/bin/env python3
"""Generate a network-level planning takeaway table for TRACE-BiOpt."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_planning_takeaways.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_planning_takeaways.tex"


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
    budget_rows = {row["dataset"]: row for row in load_csv(CURRENT_BEST / "trace_biopt_budget_phasing.csv")}
    exact_rows = {row["dataset"]: row for row in load_csv(CURRENT_BEST / "trace_biopt_exact_subnetwork_summary.csv")}
    significance_rows = [row for row in load_csv(CURRENT_BEST / "trace_biopt_significance_posture_summary.csv") if row["dataset"] != "All rows"]
    provenance = {
        f"{row['dataset']} {int(float(row['budget']) * 100)}%": row
        for row in load_csv(CURRENT_BEST / "trace_biopt_current_best_provenance.csv")
    }
    significance_by_dataset: dict[str, str] = {}
    for dataset in {row["dataset"] for row in significance_rows}:
        dataset_rows = [row for row in significance_rows if row["dataset"] == dataset]
        wins = sum(int(row["significantly_worse_baselines_holm"]) for row in dataset_rows)
        total = sum(int(row["baseline_count"]) for row in dataset_rows)
        significance_by_dataset[dataset] = f"{wins}/{total}"

    rows = [
        {
            "dataset": "PeMS7_1026",
            "planning_archetype": "Large search-sensitive network",
            "current_best_readout": (
                f"All three budgets are Stage16-promoted; strongest-baseline margins contract "
                f"{budget_rows['PeMS7_1026']['margin_path_vs_best_baseline']} even as TRACE-BiOpt MAE keeps falling, "
                f"the Holm-corrected within-dataset all-baseline screen stays clean at {significance_by_dataset['PeMS7_1026']}, "
                f"and the bounded exact benchmark still hits {exact_rows['PeMS7_1026']['exact_hits']}/{exact_rows['PeMS7_1026']['exact_cases']} audited subnetworks."
            ),
            "planning_takeaway": "Treat added sensors and added search budget as complementary capital: larger networks need calibrated risk estimation and deeper deterministic exchange search before a weak margin should be interpreted as method failure.",
        },
        {
            "dataset": "PeMS7_228",
            "planning_archetype": "Expansion-friendly medium network",
            "current_best_readout": (
                f"All three budgets are Stage16-promoted; strongest-baseline margins widen "
                f"{budget_rows['PeMS7_228']['margin_path_vs_best_baseline']}, the Holm-corrected within-dataset all-baseline screen stays clean at {significance_by_dataset['PeMS7_228']}, and the bounded exact benchmark stays at "
                f"{exact_rows['PeMS7_228']['exact_hits']}/{exact_rows['PeMS7_228']['exact_cases']} audited hits."
            ),
            "planning_takeaway": "Once low-budget calibration is repaired, staged expansion is justified: extra hardware keeps paying off in both absolute reconstruction error and relative margin over the strongest audited comparator.",
        },
        {
            "dataset": "Seattle",
            "planning_archetype": "Low-variance staged-rollout network",
            "current_best_readout": (
                f"The 20% and 30% rows are Stage16-promoted while {provenance['Seattle 10%']['source']} remains for Seattle 10%; "
                f"the strongest-baseline margins still widen {budget_rows['Seattle']['margin_path_vs_best_baseline']}, the Holm-corrected within-dataset all-baseline screen stays clean at {significance_by_dataset['Seattle']}, and bounded exact subnetworks stay at "
                f"{exact_rows['Seattle']['exact_hits']}/{exact_rows['Seattle']['exact_cases']} hits without upgrading the fail-closed 10% promotion lane."
            ),
            "planning_takeaway": "Seattle is the cleanest staged-rollout case, but the conservative reading should remain visible: keep the 10% row on its retained evidence lane and use the promoted 20/30% routes as the deployable default.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Network-level planning takeaways from the TRACE-BiOpt current-best evidence chain. Rather than restating dominance, the table translates each tested network into a transport-planning posture for staged deployment decisions.}",
        "\\label{tab:trace-biopt-planning-takeaways}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.13\\textwidth}>{\\raggedright\\arraybackslash}p{0.20\\textwidth}>{\\raggedright\\arraybackslash}p{0.31\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Dataset & Planning archetype & Current-best readout & Transport-planning takeaway \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['dataset'])} & {tex_escape(row['planning_archetype'])} & {tex_escape(row['current_best_readout'])} & {tex_escape(row['planning_takeaway'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_TEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
