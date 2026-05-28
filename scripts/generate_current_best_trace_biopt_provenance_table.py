#!/usr/bin/env python3
"""Generate an appendix table describing current-best dominance provenance."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_current_best_provenance.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_current_best_provenance.tex"


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


def format_budget(value: str) -> str:
    return f"{int(round(float(value) * 100))}\\%"


def evidence_label(value: str) -> str:
    if value.startswith("stage16_replaceable:"):
        return "Stage16 calibrated rerun"
    return "Stage15 main evidence"


def strength_label(row: dict[str, str]) -> str:
    wins = int(float(row["paired_win_count"]))
    count = int(float(row["paired_count"]))
    p = float(row["paired_paired_t_p"])
    if wins == count and p < 0.05:
        return "submission-ready paired dominance"
    return "directional or mixed paired evidence"


def main() -> int:
    rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    rows = sorted(rows, key=lambda row: (row["dataset"], float(row["budget"])))

    output_rows = []
    for row in rows:
        output_rows.append(
            {
                "dataset": row["dataset"],
                "budget": row["budget"],
                "source": evidence_label(row["evidence_source"]),
                "paired_status": strength_label(row),
                "wins": f"{int(float(row['paired_win_count']))}/{int(float(row['paired_count']))}",
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["dataset", "budget", "source", "paired_status", "wins"])
        writer.writeheader()
        writer.writerows(output_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Row-level provenance of the current-best TRACE-BiOpt dominance chain.}",
        "\\label{tab:trace-biopt-current-best-provenance}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.2\\textwidth}>{\\centering\\arraybackslash}p{0.1\\textwidth}>{\\raggedright\\arraybackslash}p{0.24\\textwidth}>{\\raggedright\\arraybackslash}X>{\\centering\\arraybackslash}p{0.1\\textwidth}}",
        "\\toprule",
        "Dataset & Budget & Main-row source & Paired-evidence status & Wins \\\\",
        "\\midrule",
    ]
    for row in output_rows:
        lines.append(
            f"{tex_escape(row['dataset'])} & {format_budget(row['budget'])} & "
            f"{tex_escape(row['source'])} & {tex_escape(row['paired_status'])} & {tex_escape(row['wins'])} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabularx}",
        "\\begin{flushleft}\\footnotesize A row is marked Stage16 calibrated rerun only when the replacement gate reports a complete replaceable rerun on the original ten split seeds. Other rows remain on the audited Stage15 evidence path until the calibrated rerun is complete.\\end{flushleft}",
        "\\end{table*}",
        "",
    ])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
