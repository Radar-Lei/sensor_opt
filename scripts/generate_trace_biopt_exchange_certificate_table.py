#!/usr/bin/env python3
"""Generate a reviewer-facing current-best exchange-certificate table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
SUMMARY_CSV = CURRENT_BEST / "trace_biopt_solver_scale_summary.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_exchange_certificate_summary.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_exchange_certificate.tex"


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


def classify_scope(row: dict[str, str]) -> tuple[str, str]:
    coverage = float(row["searched_one_exchange_coverage_pct_mean"])
    no_improve = int(row["no_improving_stop_runs"])
    budget_exhausted = int(row["exchange_budget_exhausted_runs"])
    runs = int(row["runs"])

    if coverage >= 99.999 and no_improve == runs and budget_exhausted == 0:
        return (
            "complete one-exchange certificate",
            "All runs searched the full one-exchange neighborhood and stopped only after no improving swap remained.",
        )
    if no_improve > 0 and budget_exhausted == 0:
        return (
            "searched active-set certificate",
            "Runs stop by no improving searched exchange, but the searched active set is smaller than the full k(n-k) swap set.",
        )
    if no_improve > 0 and budget_exhausted > 0:
        return (
            "mixed searched certificate",
            "Some runs end with no improving searched swap, but other runs still hit the declared exchange-iteration cap.",
        )
    return (
        "budget-limited certificate",
        "The solver typically exhausts the declared exchange budget before a no-improving searched-swap stop is observed.",
    )


def main() -> int:
    rows = load_csv(SUMMARY_CSV)
    out_rows: list[dict[str, str]] = []
    for row in rows:
        scope_label, reading = classify_scope(row)
        out_rows.append(
            {
                "dataset": row["dataset"],
                "budget_pct": str(int(round(float(row["budget"]) * 100))),
                "source_label": row["source_label"],
                "searched_one_exchange_coverage_pct_mean": f"{float(row['searched_one_exchange_coverage_pct_mean']):.6f}",
                "no_improving_stop_runs": row["no_improving_stop_runs"],
                "exchange_budget_exhausted_runs": row["exchange_budget_exhausted_runs"],
                "certificate_scope": scope_label,
                "certificate_reading": reading,
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Current-best TRACE-BiOpt exchange-gap certificate posture by dataset-budget row.}",
        "\\label{tab:trace-biopt-exchange-certificate}",
        "\\footnotesize",
        "\\begin{tabular}{lcccl}",
        "\\toprule",
        "Dataset & Budget & Search cov. & Stop cert. & Certificate scope \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{tex_escape(row['dataset'])} & "
            f"{row['budget_pct']}\\% & "
            f"{float(row['searched_one_exchange_coverage_pct_mean']):.1f}\\% & "
            f"{row['no_improving_stop_runs']}/{row['exchange_budget_exhausted_runs']} & "
            f"{tex_escape(row['certificate_scope'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "\\begin{flushleft}\\footnotesize Search cov. is the mean searched one-exchange neighborhood as a percentage of the full $k(n-k)$ swap set. Stop cert. reports runs ending by no improving searched exchange versus runs exhausting the declared exchange-iteration budget. A complete one-exchange certificate means $G_1(\\hat{\\calS})=0$ up to tolerance because the full neighborhood was searched; a searched active-set or mixed certificate means only $G^{\\mathrm{search}}_1(\\hat{\\calS})=0$ on the evaluated active set; a budget-limited row does not carry a zero-gap certificate.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
