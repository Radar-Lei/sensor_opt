#!/usr/bin/env python3
"""Generate a bounded robustness-routing table from Stage14 stress tests."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources" / "robustness_condition_table.csv"
OUT_CSV = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources" / "robustness_routing_summary.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_robustness_routing.tex"


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


def condition_label(row: dict[str, str]) -> str:
    family = row["robustness_family"]
    if family == "baseline":
        return "baseline"
    if family == "sensor_failure":
        return f"sensor failure {float(row['failure_rate']):.0%}"
    if family == "observation_noise":
        return f"observation noise {float(row['noise_scale']):.0%}"
    if family == "random_missing":
        return f"random missing {float(row['missing_rate']):.0%}"
    if family == "block_missing":
        return f"block missing {int(float(row['missing_block_steps']))} steps"
    if family == "cost_proxy":
        return f"cost proxy budget {float(row['cost_budget']):.0f}"
    if family == "temporal_shift":
        return "chronological split"
    return row["robustness_condition"]


def main() -> int:
    rows = load_csv(SOURCE)
    if not rows:
        raise ValueError(f"empty robustness source: {SOURCE}")
    groups: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in rows:
        key = (row["robustness_family"], row["robustness_condition"])
        groups.setdefault(key, []).append(row)

    summary: list[dict[str, str]] = []
    for key, group in sorted(groups.items()):
        best = min(group, key=lambda row: (float(row["mean"]), row["layout_type"]))
        counts = sorted({int(float(row["count"])) for row in group})
        summary.append(
            {
                "source_stage": best["source_stage"],
                "condition": condition_label(best),
                "robustness_family": best["robustness_family"],
                "best_layout": best["layout_type"],
                "best_mae": f"{float(best['mean']):.4f}",
                "layout_rows": str(len(group)),
                "split_count_range": f"{counts[0]}-{counts[-1]}" if len(counts) > 1 else str(counts[0]),
                "claim_route": "stress-test only",
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "source_stage",
                "condition",
                "robustness_family",
                "best_layout",
                "best_mae",
                "layout_rows",
                "split_count_range",
                "claim_route",
            ],
        )
        writer.writeheader()
        writer.writerows(summary)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Robustness evidence routing from Stage14 PeMS7\\_228 stress tests.}",
        "\\label{tab:robustness-routing}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.22\\textwidth}>{\\raggedright\\arraybackslash}p{0.22\\textwidth}>{\\centering\\arraybackslash}p{0.12\\textwidth}>{\\centering\\arraybackslash}p{0.12\\textwidth}>{\\centering\\arraybackslash}p{0.10\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Condition & Best layout & Best MAE & Layout rows & Splits & Claim route \\\\",
        "\\midrule",
    ]
    for row in summary:
        lines.append(
            f"{tex_escape(row['condition'])} & {tex_escape(row['best_layout'])} & {row['best_mae']} & {row['layout_rows']} & {row['split_count_range']} & {tex_escape(row['claim_route'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabularx}",
            "\\begin{flushleft}\\footnotesize These rows are diagnostic Stage14 stress tests on PeMS7\\_228. They route perturbation, cost, and temporal-shift evidence to bounded robustness discussion only; they do not replace the Stage15 TRACE-BiOpt dominance evidence.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
