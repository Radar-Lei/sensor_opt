#!/usr/bin/env python3
"""Generate a reviewer-facing current-best budget phasing table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"

IN_CSV = CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_budget_phasing.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_budget_phasing.tex"

DATASET_ORDER = ["PeMS7_1026", "PeMS7_228", "Seattle"]


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


def fmt_triplet(a: float, b: float, c: float) -> str:
    return f"{a:.3f} -> {b:.3f} -> {c:.3f}"


def fmt_step(step1: float, step2: float, share: float) -> str:
    return (
        f"10->20: {step1:.3f}; "
        f"20->30: {step2:.3f}; "
        f"first-step share: {share:.0%}"
    )


def fmt_margin(a: float, b: float, c: float) -> str:
    return f"{a:.3f} -> {b:.3f} -> {c:.3f}"


def build_readout(dataset: str, margin10: float, margin20: float, margin30: float, share: float) -> str:
    if dataset == "PeMS7_1026":
        return (
            f"The first 10-point increment captures {share:.0%} of the total "
            "10-30% TRACE-BiOpt gain, but the strongest-baseline margin still "
            f"contracts at 30% ({fmt_margin(margin10, margin20, margin30)}), so "
            "extra budget still needs calibrated search scaling."
        )
    if dataset == "PeMS7_228":
        return (
            f"The first increment captures {share:.0%} of the total gain, and the "
            "strongest-baseline margin keeps widening "
            f"({fmt_margin(margin10, margin20, margin30)}), so added sensors keep "
            "paying in both absolute and relative recoverability."
        )
    return (
        f"The first increment captures {share:.0%} of the total gain and the "
        "strongest-baseline margin widens monotonically "
        f"({fmt_margin(margin10, margin20, margin30)}), making staged rollout the "
        "cleanest on Seattle."
    )


def main() -> int:
    rows = load_csv(IN_CSV)
    grouped: dict[str, dict[int, dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["dataset"], {})[int(round(float(row["budget"]) * 100))] = row

    out_rows: list[dict[str, str]] = []
    for dataset in DATASET_ORDER:
        budgets = grouped[dataset]
        row10 = budgets[10]
        row20 = budgets[20]
        row30 = budgets[30]

        trace10 = float(row10["trace_biopt_mean"])
        trace20 = float(row20["trace_biopt_mean"])
        trace30 = float(row30["trace_biopt_mean"])
        base10 = float(row10["best_baseline_mean"])
        base20 = float(row20["best_baseline_mean"])
        base30 = float(row30["best_baseline_mean"])

        trace_gain_10_20 = trace10 - trace20
        trace_gain_20_30 = trace20 - trace30
        trace_gain_total = trace10 - trace30
        trace_first_step_share = trace_gain_10_20 / trace_gain_total

        base_gain_10_20 = base10 - base20
        base_gain_20_30 = base20 - base30
        base_gain_total = base10 - base30
        base_first_step_share = base_gain_10_20 / base_gain_total

        margin10 = base10 - trace10
        margin20 = base20 - trace20
        margin30 = base30 - trace30

        out_rows.append(
            {
                "dataset": dataset,
                "trace_mae_path": fmt_triplet(trace10, trace20, trace30),
                "trace_marginal_gain": fmt_step(trace_gain_10_20, trace_gain_20_30, trace_first_step_share),
                "margin_path_vs_best_baseline": fmt_margin(margin10, margin20, margin30),
                "best_baseline_step_share": f"{base_first_step_share:.0%}",
                "deployment_readout": build_readout(
                    dataset,
                    margin10,
                    margin20,
                    margin30,
                    trace_first_step_share,
                ),
                "trace_gain_10_20": f"{trace_gain_10_20:.12f}",
                "trace_gain_20_30": f"{trace_gain_20_30:.12f}",
                "trace_first_step_share": f"{trace_first_step_share:.12f}",
                "trace_total_gain": f"{trace_gain_total:.12f}",
                "margin_10": f"{margin10:.12f}",
                "margin_20": f"{margin20:.12f}",
                "margin_30": f"{margin30:.12f}",
                "baseline_gain_10_20": f"{base_gain_10_20:.12f}",
                "baseline_gain_20_30": f"{base_gain_20_30:.12f}",
                "baseline_total_gain": f"{base_gain_total:.12f}",
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Current-best TRACE-BiOpt budget-phasing posture. Each row turns the 10\\%, 20\\%, and 30\\% current-best curves into a staged deployment readout rather than another dominance table.}",
        "\\label{tab:trace-biopt-budget-phasing}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.13\\textwidth}>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}p{0.22\\textwidth}>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Dataset & TRACE-BiOpt MAE path & TRACE-BiOpt marginal gain & Margin path vs strongest baseline & Deployment readout \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{tex_escape(row['dataset'])} & "
            f"{tex_escape(row['trace_mae_path'])} & "
            f"{tex_escape(row['trace_marginal_gain'])} & "
            f"{tex_escape(row['margin_path_vs_best_baseline'])} & "
            f"{tex_escape(row['deployment_readout'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
