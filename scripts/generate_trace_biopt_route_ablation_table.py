#!/usr/bin/env python3
"""Generate a reviewer-facing current-best route-ablation table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
PAPER_SOURCES = TRACE_RESULTS / "paper_sources"

OUT_CSV = CURRENT_BEST / "trace_biopt_route_ablation_summary.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_route_ablation.tex"


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
    weight_rows = load_csv(CURRENT_BEST / "trace_biopt_weight_sensitivity.csv")
    posterior_rows = load_csv(CURRENT_BEST / "trace_biopt_posterior_risk_posture.csv")
    stage16_rows = load_csv(PAPER_SOURCES / "trace_biopt_stage16_calibrated_probe.csv")

    lookup_weight = {(row["case_label"], row["route_label"]): row for row in weight_rows}
    lookup_posterior = {
        (row["case_label"], row["comparison_route_label"]): row
        for row in posterior_rows
    }

    default_1026 = sum(float(row["default_trace_mae"]) for row in stage16_rows) / len(stage16_rows)
    calibrated_1026 = sum(float(row["calibrated_trace_mae"]) for row in stage16_rows) / len(stage16_rows)
    delta_1026 = default_1026 - calibrated_1026

    out_rows = [
        {
            "case_label": "PeMS7\\_228 10\\%",
            "intervention_family": "Risk calibration + lighter certificate weights",
            "current_route_label": "Calibrated low-cert",
            "ablated_route_label": "Stage15 certified",
            "change_summary": "train+val risk, (0.50,0.01,0.00), full-search 192 vs val risk, (2.00,0.05,0.01), Stage15 active-set",
            "current_test_mae": lookup_weight[("PeMS7\\_228 10\\%", "Calibrated low-cert")]["test_mae"],
            "ablated_test_mae": lookup_weight[("PeMS7\\_228 10\\%", "Stage15 certified")]["test_mae"],
            "mae_penalty_vs_current": lookup_weight[("PeMS7\\_228 10\\%", "Stage15 certified")]["test_delta_vs_case_best"],
            "reading": "The mixed low-budget row is resolved inside the same TRACE-BiOpt family by calibrating upper-level risk, lowering cert weights, and completing full exchange.",
        },
        {
            "case_label": "PeMS7\\_228 10\\%",
            "intervention_family": "Certificate family removal",
            "current_route_label": "Calibrated low-cert",
            "ablated_route_label": "Zero-weight probe",
            "change_summary": "same split, but (0,0,0) under strong-search 96",
            "current_test_mae": lookup_weight[("PeMS7\\_228 10\\%", "Calibrated low-cert")]["test_mae"],
            "ablated_test_mae": lookup_weight[("PeMS7\\_228 10\\%", "Zero-weight probe")]["test_mae"],
            "mae_penalty_vs_current": lookup_weight[("PeMS7\\_228 10\\%", "Zero-weight probe")]["test_delta_vs_case_best"],
            "reading": "The promoted row is not explained by dropping certificates entirely; the zero-weight strong-search route is still worse.",
        },
        {
            "case_label": "Seattle 20\\%",
            "intervention_family": "Certificate family removal",
            "current_route_label": "Seattle diagnostic certified",
            "ablated_route_label": "Zero-weight probe",
            "change_summary": "remove posterior/CVaR/spatial terms under strong-search 96",
            "current_test_mae": lookup_weight[("Seattle 20\\%", "Seattle diagnostic certified")]["test_mae"],
            "ablated_test_mae": lookup_weight[("Seattle 20\\%", "Zero-weight probe")]["test_mae"],
            "mae_penalty_vs_current": lookup_weight[("Seattle 20\\%", "Zero-weight probe")]["test_delta_vs_case_best"],
            "reading": "Stable Seattle diagnostic slices still benefit from the certificate-weighted objective even when search is already strong.",
        },
        {
            "case_label": "Seattle 30\\%",
            "intervention_family": "Certificate family removal",
            "current_route_label": "Seattle diagnostic certified",
            "ablated_route_label": "Zero-weight probe",
            "change_summary": "remove posterior/CVaR/spatial terms under strong-search 96",
            "current_test_mae": lookup_weight[("Seattle 30\\%", "Seattle diagnostic certified")]["test_mae"],
            "ablated_test_mae": lookup_weight[("Seattle 30\\%", "Zero-weight probe")]["test_mae"],
            "mae_penalty_vs_current": lookup_weight[("Seattle 30\\%", "Zero-weight probe")]["test_delta_vs_case_best"],
            "reading": "The stable high-budget Seattle diagnostic slice keeps the same sign: strong search alone does not recover the certificate-weighted route.",
        },
        {
            "case_label": "PeMS7\\_1026 30\\%",
            "intervention_family": "Risk calibration + stronger search tail",
            "current_route_label": "Calibrated rerun",
            "ablated_route_label": "Stage15 default",
            "change_summary": "train+val risk, low-cert rerun, stronger active-set exchange vs original Stage15 route",
            "current_test_mae": f"{calibrated_1026:.6f}",
            "ablated_test_mae": f"{default_1026:.6f}",
            "mae_penalty_vs_current": f"{delta_1026:.6f}",
            "reading": "The large-network weak row tightens inside the same objective family rather than by switching to another baseline family.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing TRACE-BiOpt route-ablation slices. Unlike the legacy TRACE-SL component table, these rows stay inside the current TRACE-BiOpt objective family and ask which route ingredient is being removed or weakened on the rows that mattered most to the final claim chain.}",
        "\\label{tab:trace-biopt-route-ablation}",
        "\\tiny",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.11\\textwidth}>{\\raggedright\\arraybackslash}p{0.15\\textwidth}>{\\raggedright\\arraybackslash}p{0.11\\textwidth}>{\\raggedright\\arraybackslash}p{0.11\\textwidth}>{\\raggedright\\arraybackslash}p{0.20\\textwidth}>{\\centering\\arraybackslash}p{0.07\\textwidth}>{\\centering\\arraybackslash}p{0.07\\textwidth}>{\\centering\\arraybackslash}p{0.07\\textwidth}>{\\raggedright\\arraybackslash}p{0.22\\textwidth}}",
        "\\toprule",
        "Case & Intervention family & Current route & Ablated route & What changes & Current MAE & Ablated MAE & $\\Delta$ MAE & Reading \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{row['case_label']} & "
            f"{tex_escape(row['intervention_family'])} & "
            f"{tex_escape(row['current_route_label'])} & "
            f"{tex_escape(row['ablated_route_label'])} & "
            f"{tex_escape(row['change_summary'])} & "
            f"{float(row['current_test_mae']):.3f} & "
            f"{float(row['ablated_test_mae']):.3f} & "
            f"{float(row['mae_penalty_vs_current']):.3f} & "
            f"{tex_escape(row['reading'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "}",
            "\\begin{flushleft}\\footnotesize $\\Delta$ MAE is the held-out penalty of the ablated route relative to the reference TRACE-BiOpt route listed in the table, so positive values favor that reference route. The Seattle rows are bounded same-split diagnostic slices built from the matched strong-search probes already used in the certificate-removal and weight-sensitivity tables; they do not replace the ten-seed current-best evidence chain. The PeMS7\\_228 and PeMS7\\_1026 rows use the completed calibrated reruns that now feed the current-best evidence chain. This is bounded route-ablation evidence, not a new dominance table.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
