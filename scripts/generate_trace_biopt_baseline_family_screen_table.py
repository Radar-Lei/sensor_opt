#!/usr/bin/env python3
"""Generate a reviewer-facing family-level comparison-class screen."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd


CURRENT_BEST = Path("TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence")
BEST_DELTA = CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"
SIGNIFICANCE_SUMMARY = CURRENT_BEST / "trace_biopt_significance_posture_summary.csv"
SIGNIFICANCE_DETAIL = CURRENT_BEST / "trace_biopt_significance_posture_detail.csv"
OUTPUT_CSV = CURRENT_BEST / "trace_biopt_baseline_family_screen.csv"
OUTPUT_TEX = Path("paper/tables/table_trace_biopt_baseline_family_screen.tex")


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


def tex_escape(value: str) -> str:
    return value.replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")


def format_delta(value: float) -> str:
    return f"{float(value):.4f}"


def format_p(value: float) -> str:
    value = float(value)
    if value < 1e-3:
        return f"{value:.1e}"
    return f"{value:.4f}"


def build_frame() -> pd.DataFrame:
    best_rows = pd.read_csv(BEST_DELTA)
    summary_rows = pd.read_csv(SIGNIFICANCE_SUMMARY)
    summary_rows = summary_rows[summary_rows["dataset"] != "All rows"].copy()
    summary_rows["budget"] = summary_rows["budget"].astype(float)
    detail_rows = pd.read_csv(SIGNIFICANCE_DETAIL)
    detail_rows["budget"] = detail_rows["budget"].astype(float)

    strongest_counts = Counter(CATEGORIES[row["best_baseline_layout"]] for _, row in best_rows.iterrows())
    family_layouts: dict[str, set[str]] = defaultdict(set)
    family_stats: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "family": "",
            "baseline_count": 0,
            "comparison_count": 0,
            "strongest_mean_rows": 0,
            "hardest_corrected_rows": 0,
            "closest_mean_delta": None,
            "largest_holm_p": None,
            "surviving_challengers": 0,
        }
    )

    for _, row in detail_rows.iterrows():
        family = CATEGORIES[row["baseline_layout"]]
        stats = family_stats[family]
        stats["family"] = family
        stats["comparison_count"] = int(stats["comparison_count"]) + 1
        family_layouts[family].add(row["baseline_layout"])

        delta = float(row["mean_delta"])
        if stats["closest_mean_delta"] is None or delta > float(stats["closest_mean_delta"]):
            stats["closest_mean_delta"] = delta

        holm_p = float(row["paired_t_p_holm"])
        if stats["largest_holm_p"] is None or holm_p > float(stats["largest_holm_p"]):
            stats["largest_holm_p"] = holm_p

        trace_better = str(row["trace_significantly_better_holm"]).lower() == "true"
        if not trace_better:
            stats["surviving_challengers"] = int(stats["surviving_challengers"]) + 1

    hardest_counts: Counter[str] = Counter()
    for _, row in summary_rows.iterrows():
        subset = detail_rows[
            (detail_rows["dataset"] == row["dataset"])
            & (detail_rows["budget"] == float(row["budget"]))
            & (detail_rows["baseline_label"] == row["closest_challenger_label"])
        ]
        hardest_layout = subset.iloc[0]["baseline_layout"]
        hardest_counts[CATEGORIES[hardest_layout]] += 1

    for family, layouts in family_layouts.items():
        stats = family_stats[family]
        stats["baseline_count"] = len(layouts)
        stats["strongest_mean_rows"] = strongest_counts.get(family, 0)
        stats["hardest_corrected_rows"] = hardest_counts.get(family, 0)

    return pd.DataFrame(sorted(family_stats.values(), key=lambda row: row["family"]))


def write_tex(frame: pd.DataFrame) -> None:
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Family-level screen of the pre-registered non-BiOpt comparison class. The table compresses the 21 audited baselines into method families and reports how often each family supplies the strongest mean challenger or the hardest challenger after Holm correction. Every family still leaves zero surviving tied-or-better challenger after corrected paired tests.}",
        "\\label{tab:trace-biopt-baseline-family-screen}",
        "\\small",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.29\\textwidth}cccccc}",
        "\\toprule",
        "Family & Baselines & Tests & \\makecell[c]{Strongest\\\\mean rows} & \\makecell[c]{Hardest\\\\corrected rows} & \\makecell[c]{Closest $\\Delta$\\\\MAE} & \\makecell[c]{Largest\\\\Holm $p$} \\\\",
        "\\midrule",
    ]
    for _, row in frame.iterrows():
        lines.append(
            f"{tex_escape(row['family'])} & "
            f"{int(row['baseline_count'])} & "
            f"{int(row['comparison_count'])} & "
            f"{int(row['strongest_mean_rows'])} & "
            f"{int(row['hardest_corrected_rows'])} & "
            f"{format_delta(row['closest_mean_delta'])} & "
            f"{format_p(row['largest_holm_p'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "\\vspace{0.35em}",
            (
                "\\parbox{0.96\\textwidth}{\\small The strongest family-level near misses come from the prior TRACE-SL / RCSS family, which provides 8/9 strongest-mean challengers and 7/9 hardest corrected challengers, yet its closest current-best gap remains $-0.0375$ MAE and it leaves zero corrected survivors. The exchange-refined family contributes the remaining strongest-mean row, while the scenario-risk and simple-heuristic families each appear once as the hardest corrected family.}"
            ),
            "\\end{table*}",
            "",
        ]
    )
    OUTPUT_TEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    frame = build_frame()
    frame.to_csv(OUTPUT_CSV, index=False)
    write_tex(frame)
    print(f"Wrote {OUTPUT_TEX} and {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
