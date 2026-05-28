#!/usr/bin/env python3
"""Generate a reviewer-facing current-best tail-risk posture table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"

OBJECTIVE_MIX_CSV = CURRENT_BEST / "trace_biopt_objective_mix_summary.csv"
WEIGHT_SENSITIVITY_CSV = CURRENT_BEST / "trace_biopt_weight_sensitivity.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_tail_risk_posture.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_tail_risk_posture.tex"

CASES = [
    ("Seattle 20\\%", "Seattle", 20),
    ("Seattle 30\\%", "Seattle", 30),
    ("PeMS7\\_228 10\\%", "PeMS7_228", 10),
]


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
    objective_mix = {
        (row["dataset"], int(row["budget_pct"])): row
        for row in load_csv(OBJECTIVE_MIX_CSV)
    }
    weight_rows = {
        (row["case_label"], row["route_label"]): row
        for row in load_csv(WEIGHT_SENSITIVITY_CSV)
    }

    out_rows: list[dict[str, str]] = []
    for case_label, dataset, budget_pct in CASES:
        mix = objective_mix[(dataset, budget_pct)]
        if dataset == "Seattle":
            current = weight_rows[(case_label, "Seattle diagnostic certified")]
            zero = weight_rows[(case_label, "Zero-weight probe")]
            comparator_summary = (
                f"Zero-weight strong-search is worse by {float(zero['test_delta_vs_case_best']):.3f} MAE"
            )
            reading = (
                "Tail-risk mass stays small but nonzero inside a posterior-driven stable route; "
                "removing it entirely under matched strong search still hurts held-out MAE."
            )
        else:
            current = weight_rows[(case_label, "Calibrated low-cert")]
            zero = weight_rows[(case_label, "Zero-weight probe")]
            heavy = weight_rows[(case_label, "Stage15 certified")]
            comparator_summary = (
                f"Zero-weight is worse by {float(zero['test_delta_vs_case_best']):.3f} MAE; "
                f"heavy-cert Stage15 is worse by {float(heavy['test_delta_vs_case_best']):.3f} MAE"
            )
            reading = (
                "The promoted low-budget route keeps a light but nonzero tail-risk term; "
                "both removing it and over-weighting the certificate family perform worse."
            )

        out_rows.append(
            {
                "case_label": case_label,
                "dataset": dataset,
                "budget_pct": str(budget_pct),
                "current_route_label": current["route_label"],
                "current_weights_label": current["weights_label"],
                "current_risk_source_label": current["risk_source_label"],
                "current_cvar_share_pct": f"{float(mix['cvar_share_pct']):.6f}",
                "current_posterior_share_pct": f"{float(mix['posterior_share_pct']):.6f}",
                "current_reconstruction_share_pct": f"{float(mix['reconstruction_share_pct']):.6f}",
                "comparator_summary": comparator_summary,
                "tail_risk_reading": reading,
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing TRACE-BiOpt tail-risk posture slices. This table does not ask the CVaR term to dominate the objective; it shows instead whether a small but explicit tail-risk component survives in the winning route and how matched internal probes behave when that component is removed or over-weighted.}",
        "\\label{tab:trace-biopt-tail-risk-posture}",
        "\\tiny",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.12\\textwidth}>{\\raggedright\\arraybackslash}p{0.17\\textwidth}>{\\centering\\arraybackslash}p{0.10\\textwidth}>{\\centering\\arraybackslash}p{0.10\\textwidth}>{\\raggedright\\arraybackslash}p{0.22\\textwidth}>{\\raggedright\\arraybackslash}p{0.22\\textwidth}}",
        "\\toprule",
        "Case & Current route & CVaR share & Posterior share & Internal comparison & Reading \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{row['case_label']} & "
            f"{tex_escape(row['current_route_label'])} {tex_escape(row['current_weights_label'])} & "
            f"{float(row['current_cvar_share_pct']):.2f}\\% & "
            f"{float(row['current_posterior_share_pct']):.2f}\\% & "
            f"{tex_escape(row['comparator_summary'])} & "
            f"{tex_escape(row['tail_risk_reading'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "}",
            "\\begin{flushleft}\\footnotesize CVaR share and posterior share are the mean weighted shares of the accepted final TRACE-BiOpt objective on the reference route in each row. The Seattle slices are bounded same-split diagnostic routes paired with the zero-weight strong-search probes from Table~\\ref{tab:trace-biopt-weight-sensitivity}; they do not replace the ten-seed current-best evidence chain. The PeMS7\\_228 10\\% slice compares the promoted calibrated low-cert route against both the zero-weight probe and the heavier Stage15 certificate-weighted route on the same split.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
