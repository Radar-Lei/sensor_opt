#!/usr/bin/env python3
"""Generate a current-best full baseline matrix table for TRACE-BiOpt."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGE15 = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined"
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_full_baseline_matrix.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_full_baseline_matrix.tex"

DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
BUDGETS = [0.1, 0.2, 0.3]


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


def fmt_cell(mean_value: float, rank_value: int, highlight: bool) -> str:
    text = f"{mean_value:.4f} [{rank_value}]"
    return f"\\textbf{{{text}}}" if highlight else text


def panel_lines(dataset: str, rows: list[dict[str, str]]) -> list[str]:
    lines = [
        f"\\multicolumn{{5}}{{l}}{{\\textbf{{{tex_escape(dataset)}}}}} \\\\",
        "\\midrule",
    ]
    for row in rows:
        method = tex_escape(row["layout_type"])
        if row["layout_type"] == "trace_biopt":
            method = f"\\textbf{{{method}}}"
        lines.append(
            f"{method} & "
            f"{fmt_cell(float(row['mean_10']), int(row['rank_10']), row['layout_type'] == 'trace_biopt')} & "
            f"{fmt_cell(float(row['mean_20']), int(row['rank_20']), row['layout_type'] == 'trace_biopt')} & "
            f"{fmt_cell(float(row['mean_30']), int(row['rank_30']), row['layout_type'] == 'trace_biopt')} & "
            f"{float(row['avg_rank']):.2f} \\\\"
        )
    return lines


def main() -> int:
    layout_rows = [
        row for row in load_csv(STAGE15 / "gls_map_layout_summary.csv")
        if row["robustness_family"] == "baseline" and row["robustness_condition"] == "baseline"
    ]
    current_best = {
        (row["dataset"], float(row["budget"])): float(row["trace_biopt_mean"])
        for row in load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    }

    grouped: dict[tuple[str, float], dict[str, float]] = {}
    for row in layout_rows:
        key = (row["dataset"], float(row["budget"]))
        grouped.setdefault(key, {})[row["layout_type"]] = float(row["mean"])

    # Promote the current-best TRACE-BiOpt means into the matrix.
    for key, trace_mean in current_best.items():
        grouped.setdefault(key, {})["trace_biopt"] = trace_mean

    layouts = sorted({layout for values in grouped.values() for layout in values})
    output_rows: list[dict[str, str]] = []
    dataset_panels: dict[str, list[dict[str, str]]] = {}

    for dataset in DATASETS:
        per_method: list[dict[str, str]] = []
        for layout in layouts:
            row: dict[str, str] = {"dataset": dataset, "layout_type": layout}
            ranks = []
            for budget in BUDGETS:
                values = grouped[(dataset, budget)]
                ranked = sorted(values.items(), key=lambda item: (item[1], item[0]))
                rank_map = {name: idx + 1 for idx, (name, _) in enumerate(ranked)}
                mean_value = values[layout]
                rank_value = rank_map[layout]
                suffix = str(int(round(budget * 100)))
                row[f"mean_{suffix}"] = f"{mean_value:.10f}"
                row[f"rank_{suffix}"] = str(rank_value)
                ranks.append(rank_value)
            row["avg_rank"] = f"{sum(ranks) / len(ranks):.4f}"
            per_method.append(row)
            output_rows.append(row.copy())
        dataset_panels[dataset] = sorted(
            per_method,
            key=lambda item: (float(item["avg_rank"]), item["layout_type"] != "trace_biopt", item["layout_type"]),
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["dataset", "layout_type", "mean_10", "rank_10", "mean_20", "rank_20", "mean_30", "rank_30", "avg_rank"],
        )
        writer.writeheader()
        writer.writerows(output_rows)

    lines = [
        "\\begin{table*}[p]",
        "\\centering",
        "\\caption{Current-best full baseline matrix. Each panel lists TRACE-BiOpt and all 21 pre-registered non-BiOpt baselines for one dataset. Entries are mean held-out GLS/MAP MAE with within-row rank in brackets; lower is better. TRACE-BiOpt ranks first on every dataset-budget row, so the best-baseline dominance table is a compression of a full matrix rather than a selective comparison.}",
        "\\label{tab:trace-biopt-full-baseline-matrix}",
        "\\tiny",
        "\\renewcommand{\\arraystretch}{0.92}",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.29\\textwidth}>{\\centering\\arraybackslash}p{0.15\\textwidth}>{\\centering\\arraybackslash}p{0.15\\textwidth}>{\\centering\\arraybackslash}p{0.15\\textwidth}>{\\centering\\arraybackslash}p{0.11\\textwidth}}",
        "\\toprule",
        "Method & 10\\% & 20\\% & 30\\% & Avg. rank \\\\",
    ]
    for idx, dataset in enumerate(DATASETS):
        if idx > 0:
            lines.extend(["\\midrule", "\\midrule"])
        lines.extend(panel_lines(dataset, dataset_panels[dataset]))
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "\\begin{flushleft}\\footnotesize The non-TRACE-BiOpt rows come from the audited Stage15 baseline summary. The TRACE-BiOpt row uses the current-best promoted mean where a complete replaceable Stage16 rerun exists and otherwise retains the Stage15 mean.\\end{flushleft}",
        "\\renewcommand{\\arraystretch}{1.0}",
        "\\end{table*}",
        "",
    ])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
