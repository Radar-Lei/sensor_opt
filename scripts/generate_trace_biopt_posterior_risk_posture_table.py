#!/usr/bin/env python3
"""Generate a reviewer-facing posterior-risk posture table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
WEIGHT_SENSITIVITY_CSV = CURRENT_BEST / "trace_biopt_weight_sensitivity.csv"
OBJECTIVE_MIX_CSV = CURRENT_BEST / "trace_biopt_objective_mix_summary.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_posterior_risk_posture.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_posterior_risk_posture.tex"


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def tex_passthrough_label(value: str) -> str:
    return value.replace("\\\\", "\\")


def display_route_label(value: str) -> str:
    if value == "Seattle diagnostic certified":
        return "Seattle diag. certified"
    return value


def display_reading(value: str) -> str:
    if value == "Within a matched route probe, the lower posterior-trace route also achieves lower held-out MAE.":
        return "Lower trace aligns with lower held-out MAE in this matched probe."
    return value


def case_best(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["case_label"], []).append(row)
    return {
        case_label: min(items, key=lambda row: float(row["test_mae"]))
        for case_label, items in grouped.items()
    }


def main() -> int:
    weight_rows = load_csv_rows(WEIGHT_SENSITIVITY_CSV)
    objective_mix_rows = {
        (row["dataset"], row["budget_pct"]): row
        for row in load_csv_rows(OBJECTIVE_MIX_CSV)
    }
    best_lookup = case_best(weight_rows)

    out_rows: list[dict[str, str]] = []
    for row in weight_rows:
        best = best_lookup[row["case_label"]]
        if row["route_label"] == best["route_label"]:
            continue
        mix_row = objective_mix_rows[(best["dataset"], best["budget_pct"])]
        posterior_delta = float(row["posterior_trace"]) - float(best["posterior_trace"])
        mae_delta = float(row["test_mae"]) - float(best["test_mae"])
        out_rows.append(
            {
                "case_label": row["case_label"],
                "dataset": row["dataset"],
                "budget_pct": row["budget_pct"],
                "best_route_label": best["route_label"],
                "comparison_route_label": row["route_label"],
                "best_route_posterior_trace": f"{float(best['posterior_trace']):.6f}",
                "comparison_posterior_trace": f"{float(row['posterior_trace']):.6f}",
                "posterior_trace_delta_vs_best": f"{posterior_delta:.6f}",
                "best_route_test_mae": f"{float(best['test_mae']):.6f}",
                "comparison_test_mae": f"{float(row['test_mae']):.6f}",
                "test_mae_delta_vs_best": f"{mae_delta:.6f}",
                "best_route_posterior_share_pct": mix_row["posterior_share_pct"],
                "reading": (
                    "Within a matched route probe, the lower posterior-trace route also achieves lower held-out MAE."
                    if posterior_delta > 0 and mae_delta > 0
                    else "Posterior-trace and held-out MAE do not move together in this controlled probe."
                ),
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Posterior-risk posture in matched TRACE-BiOpt route probes.}",
        "\\label{tab:trace-biopt-posterior-risk}",
        "\\footnotesize",
        "\\begin{tabularx}{\\textwidth}{llcccc>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Case & Comparator & $\\Delta$ trace & $\\Delta$ MAE & Best-route posterior share & Best route & Reading \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{tex_passthrough_label(row['case_label'])} & "
            f"{tex_escape(row['comparison_route_label'])} & "
            f"{float(row['posterior_trace_delta_vs_best']):.1f} & "
            f"{float(row['test_mae_delta_vs_best']):.3f} & "
            f"{float(row['best_route_posterior_share_pct']):.1f}\\% & "
            f"{tex_escape(display_route_label(row['best_route_label']))} & "
            f"{tex_escape(display_reading(row['reading']))} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabularx}",
            "\\begin{flushleft}\\footnotesize $\\Delta$ trace and $\\Delta$ MAE are comparator minus the reference TRACE-BiOpt route in the same case, so positive values mean the reference route has both lower posterior trace and lower held-out MAE. The Seattle rows are bounded same-split diagnostic slices, while the PeMS7\\_228 row uses the promoted calibrated current-best route. This is a bounded theorem-to-evidence bridge for Theorem~\\ref{thm:trace-risk}: it uses only matched route probes inside the same dataset-budget slice and does not claim that posterior trace must rank every audited baseline by MAE under non-Gaussian traffic data.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
