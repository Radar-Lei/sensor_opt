#!/usr/bin/env python3
"""Generate current-best all-baseline significance posture artifacts."""

from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean

from scipy import stats


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15_METRICS = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2" / "combined" / "combined_metrics.csv"
STAGE16_REPLACEMENT = TRACE_RESULTS / "stage16_calibrated_trace_sweep" / "replacement_status" / "stage16_replacement_seed_level.csv"
OUT_SUMMARY = CURRENT_BEST / "trace_biopt_significance_posture_summary.csv"
OUT_DETAIL = CURRENT_BEST / "trace_biopt_significance_posture_detail.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_significance_posture.tex"

DATASETS = ["PeMS7_1026", "PeMS7_228", "Seattle"]
BASELINE_LABEL = {
    "validation_swap_selected": "Prev. TRACE-SL",
    "swap_from_greedy_a_trace": "Swap from A-trace",
    "rcss_selected": "RCSS",
    "multistart_swap_by_validation": "Multistart validation-swap",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def holm_adjust(p_values: list[float]) -> list[float]:
    indexed = sorted(enumerate(p_values), key=lambda item: item[1])
    m = len(indexed)
    adjusted = [0.0] * m
    running = 0.0
    for rank, (original_index, p_value) in enumerate(indexed):
        factor = m - rank
        running = max(running, min(1.0, factor * p_value))
        adjusted[original_index] = running
    return adjusted


def stage15_lookup() -> dict[tuple[str, float, str, int], float]:
    rows = load_csv(STAGE15_METRICS)
    return {
        (row["dataset"], float(row["budget"]), row["layout_type"], int(row["split_seed"])): float(row["mae"])
        for row in rows
        if row["method"] == "gls_map"
    }


def stage16_lookup() -> dict[tuple[str, float, str, int], float]:
    rows = load_csv(STAGE16_REPLACEMENT)
    return {
        (row["dataset"], float(row["budget"]), row["stage16_root"], int(row["split_seed"])): float(row["stage16_trace_mae"])
        for row in rows
    }


def trace_seed_values(
    current_row: dict[str, str],
    stage15: dict[tuple[str, float, str, int], float],
    stage16: dict[tuple[str, float, str, int], float],
) -> dict[int, float]:
    dataset = current_row["dataset"]
    budget = float(current_row["budget"])
    evidence_source = current_row["evidence_source"]
    if evidence_source == "stage15_main":
        return {split_seed: stage15[(dataset, budget, "trace_biopt", split_seed)] for split_seed in range(25, 35)}
    stage16_root = evidence_source.split(":", 1)[1]
    return {split_seed: stage16[(dataset, budget, stage16_root, split_seed)] for split_seed in range(25, 35)}


def tex_escape(value: str) -> str:
    return value.replace("_", "\\_").replace("%", "\\%").replace("&", "\\&")


def main() -> int:
    current_rows = sorted(
        load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"),
        key=lambda row: (DATASETS.index(row["dataset"]), float(row["budget"])),
    )
    stage15 = stage15_lookup()
    stage16 = stage16_lookup()
    baseline_layouts = sorted({key[2] for key in stage15 if key[2] != "trace_biopt"})

    detail_rows: list[dict[str, object]] = []
    for current_row in current_rows:
        dataset = current_row["dataset"]
        budget = float(current_row["budget"])
        budget_pct = int(round(budget * 100))
        trace_values = trace_seed_values(current_row, stage15, stage16)
        for baseline_layout in baseline_layouts:
            baseline_values = {split_seed: stage15[(dataset, budget, baseline_layout, split_seed)] for split_seed in range(25, 35)}
            deltas = [trace_values[split_seed] - baseline_values[split_seed] for split_seed in range(25, 35)]
            paired_t_p = float(stats.ttest_1samp(deltas, 0.0, alternative="less").pvalue)
            paired_t_p_greater = float(stats.ttest_1samp(deltas, 0.0, alternative="greater").pvalue)
            wilcoxon_p = float(stats.wilcoxon(deltas, alternative="less").pvalue)
            detail_rows.append(
                {
                    "dataset": dataset,
                    "budget": budget,
                    "budget_pct": budget_pct,
                    "evidence_source": current_row["evidence_source"],
                    "baseline_layout": baseline_layout,
                    "baseline_label": BASELINE_LABEL.get(baseline_layout, baseline_layout.replace("_", " ")),
                    "mean_delta": mean(deltas),
                    "win_count": sum(delta < 0.0 for delta in deltas),
                    "count": len(deltas),
                    "paired_t_p_less": paired_t_p,
                    "paired_t_p_greater": paired_t_p_greater,
                    "wilcoxon_p_less": wilcoxon_p,
                }
            )

    holm_p_values = holm_adjust([float(row["paired_t_p_less"]) for row in detail_rows])
    for row, holm_p in zip(detail_rows, holm_p_values):
        row["paired_t_p_holm"] = holm_p
        row["trace_significantly_better_holm"] = bool(float(row["mean_delta"]) < 0.0 and holm_p < 0.05)
        row["baseline_significantly_better_holm"] = bool(float(row["mean_delta"]) > 0.0 and float(row["paired_t_p_greater"]) < 0.05)
        row["wilcoxon_supports_trace"] = bool(float(row["wilcoxon_p_less"]) < 0.05)

    summary_rows: list[dict[str, object]] = []
    for current_row in current_rows:
        dataset = current_row["dataset"]
        budget = float(current_row["budget"])
        budget_pct = int(round(budget * 100))
        subset = [row for row in detail_rows if row["dataset"] == dataset and float(row["budget"]) == budget]
        hardest = max(subset, key=lambda row: float(row["paired_t_p_holm"]))
        summary_rows.append(
            {
                "dataset": dataset,
                "budget": budget,
                "budget_pct": budget_pct,
                "evidence_source": current_row["evidence_source"],
                "significantly_worse_baselines_holm": sum(bool(row["trace_significantly_better_holm"]) for row in subset),
                "non_worse_baselines_holm": sum(not bool(row["trace_significantly_better_holm"]) for row in subset),
                "baseline_significantly_better_holm": sum(bool(row["baseline_significantly_better_holm"]) for row in subset),
                "closest_challenger_layout": hardest["baseline_layout"],
                "closest_challenger_label": hardest["baseline_label"],
                "closest_challenger_mean_delta": hardest["mean_delta"],
                "max_paired_t_p_holm": hardest["paired_t_p_holm"],
                "max_wilcoxon_p_less": max(float(row["wilcoxon_p_less"]) for row in subset),
                "baseline_count": len(subset),
            }
        )

    global_hardest = max(detail_rows, key=lambda row: float(row["paired_t_p_holm"]))
    summary_rows.append(
        {
            "dataset": "All rows",
            "budget": "",
            "budget_pct": "",
            "evidence_source": "current_best",
            "significantly_worse_baselines_holm": sum(bool(row["trace_significantly_better_holm"]) for row in detail_rows),
            "non_worse_baselines_holm": sum(not bool(row["trace_significantly_better_holm"]) for row in detail_rows),
            "baseline_significantly_better_holm": sum(bool(row["baseline_significantly_better_holm"]) for row in detail_rows),
            "closest_challenger_layout": global_hardest["baseline_layout"],
            "closest_challenger_label": global_hardest["baseline_label"],
            "closest_challenger_mean_delta": global_hardest["mean_delta"],
            "max_paired_t_p_holm": global_hardest["paired_t_p_holm"],
            "max_wilcoxon_p_less": max(float(row["wilcoxon_p_less"]) for row in detail_rows),
            "baseline_count": len(detail_rows),
        }
    )

    write_csv(
        OUT_DETAIL,
        detail_rows,
        [
            "dataset",
            "budget",
            "budget_pct",
            "evidence_source",
            "baseline_layout",
            "baseline_label",
            "mean_delta",
            "win_count",
            "count",
            "paired_t_p_less",
            "paired_t_p_greater",
            "paired_t_p_holm",
            "wilcoxon_p_less",
            "trace_significantly_better_holm",
            "baseline_significantly_better_holm",
            "wilcoxon_supports_trace",
        ],
    )
    write_csv(
        OUT_SUMMARY,
        summary_rows,
        [
            "dataset",
            "budget",
            "budget_pct",
            "evidence_source",
            "significantly_worse_baselines_holm",
            "non_worse_baselines_holm",
            "baseline_significantly_better_holm",
            "closest_challenger_layout",
            "closest_challenger_label",
            "closest_challenger_mean_delta",
            "max_paired_t_p_holm",
            "max_wilcoxon_p_less",
            "baseline_count",
        ],
    )

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Current-best all-baseline significance posture. Each row compares TRACE-BiOpt with all 21 pre-registered non-BiOpt baselines on the same ten split seeds. Counts use one-sided paired $t$-tests with Holm familywise correction over all 189 current-best row-baseline comparisons. The last column reports the hardest challenger after correction; the detail CSV also records unadjusted one-sided Wilcoxon checks.}",
        "\\label{tab:trace-biopt-significance-posture}",
        "\\tiny",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\renewcommand{\\arraystretch}{0.95}",
        "\\begin{tabularx}{\\textwidth}{llrrr>{\\raggedright\\arraybackslash}Xrrr}",
        "\\toprule",
        "Dataset & Budget & Worse / total & Non-worse & Better & Hardest challenger & Mean $\\Delta$ & Max Holm $p$ & Max Wilcoxon $p$ \\\\",
        "\\midrule",
    ]
    for row in summary_rows:
        dataset = tex_escape(str(row["dataset"]))
        budget = "--" if row["dataset"] == "All rows" else f"{int(row['budget_pct'])}\\%"
        lines.append(
            f"{dataset} & {budget} & "
            f"{int(row['significantly_worse_baselines_holm'])}/{int(row['baseline_count'])} & "
            f"{int(row['non_worse_baselines_holm'])} & "
            f"{int(row['baseline_significantly_better_holm'])} & "
            f"{tex_escape(str(row['closest_challenger_label']))} & "
            f"{float(row['closest_challenger_mean_delta']):.4f} & "
            f"{float(row['max_paired_t_p_holm']):.4f} & "
            f"{float(row['max_wilcoxon_p_less']):.4f} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabularx}",
        "\\begin{flushleft}\\footnotesize `Worse / total` counts baselines for which TRACE-BiOpt remains significantly better after global Holm correction; `Non-worse` counts baselines not separated by that corrected test; `Better` counts baselines significantly better than TRACE-BiOpt. Negative mean $\\Delta$ favors TRACE-BiOpt.\\end{flushleft}",
        "\\renewcommand{\\arraystretch}{1.0}",
        "\\end{table*}",
        "",
    ])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX}, {OUT_SUMMARY}, and {OUT_DETAIL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
