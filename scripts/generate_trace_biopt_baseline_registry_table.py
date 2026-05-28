#!/usr/bin/env python3
"""Generate the TRACE-BiOpt Stage15 non-BiOpt baseline registry table."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGE15 = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined"
OUT_CSV = STAGE15 / "trace_biopt_baseline_registry.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_baseline_registry.tex"


CATEGORIES = {
    "random": "Random / validation-selected",
    "best_random_by_trace": "Random / validation-selected",
    "best_random_by_validation": "Random / validation-selected",
    "top_variance": "Simple traffic heuristic",
    "degree": "Graph heuristic",
    "coverage": "Coverage / observability",
    "observability_proxy": "Coverage / observability",
    "graph_sampling_laplacian": "Graph signal processing",
    "qr_pod_modes": "Sparse modal placement",
    "greedy_a_trace": "Optimal-design surrogate",
    "greedy_d_logdet": "Optimal-design surrogate",
    "scenario_average_a_trace": "Scenario-risk surrogate",
    "scenario_cvar_a_trace": "Scenario-risk surrogate",
    "robust_coverage_cvar": "Robust coverage",
    "rcss_selected": "Prior TRACE-SL / RCSS",
    "validation_swap_selected": "Prior TRACE-SL / RCSS",
    "multistart_swap_by_validation": "Prior TRACE-SL / RCSS",
    "swap_from_best_random_trace": "Exchange-refined baseline",
    "swap_from_greedy_a_trace": "Exchange-refined baseline",
    "swap_from_scenario_average": "Exchange-refined baseline",
    "swap_from_scenario_cvar": "Exchange-refined baseline",
}


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
    layout_rows = load_csv(STAGE15 / "gls_map_layout_summary.csv")
    dominance_rows = load_csv(STAGE15 / "trace_biopt_best_baseline_delta.csv")
    baselines = sorted({row["layout_type"] for row in layout_rows if row["layout_type"] != "trace_biopt"})
    missing = [name for name in baselines if name not in CATEGORIES]
    if missing:
        raise ValueError(f"unclassified baselines: {missing}")
    best_counts = Counter(row["best_baseline_layout"] for row in dominance_rows)
    category_counts = Counter(CATEGORIES[name] for name in baselines)

    rows = [
        {
            "baseline": name,
            "category": CATEGORIES[name],
            "stage15_registry": "yes",
            "row_specific_best_count": str(best_counts.get(name, 0)),
        }
        for name in baselines
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["baseline", "category", "stage15_registry", "row_specific_best_count"])
        writer.writeheader()
        writer.writerows(rows)

    summary = "; ".join(f"{category}: {count}" for category, count in sorted(category_counts.items()))
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Pre-registered non-BiOpt baseline registry used by the Stage15 dominance gate.}",
        "\\label{tab:trace-biopt-baseline-registry}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.32\\textwidth}>{\\raggedright\\arraybackslash}p{0.33\\textwidth}>{\\centering\\arraybackslash}p{0.12\\textwidth}>{\\centering\\arraybackslash}X}",
        "\\toprule",
        "Baseline row & Category & Registry & Best rows \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['baseline'])} & {tex_escape(row['category'])} & {row['stage15_registry']} & {row['row_specific_best_count']} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabularx}",
        f"\\begin{{flushleft}}\\footnotesize Registry contains {len(rows)} non-BiOpt baselines across categories: {tex_escape(summary)}. Best rows count how many of the nine dataset-budget regimes use that baseline as the row-specific strongest comparator in Table~\\ref{{tab:trace-biopt-dominance}}.\\end{{flushleft}}",
        "\\end{table*}",
        "",
    ])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
