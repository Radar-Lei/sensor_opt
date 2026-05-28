#!/usr/bin/env python3
"""Generate a reviewer-facing current-best MAP stability posture table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
DELTA_CSV = CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"
OUT_CSV = CURRENT_BEST / "trace_biopt_map_stability_posture.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_map_stability_posture.tex"

TRACE_ROOT_MAP = {
    "pems7_1026_10_20_posterior_iter20": TRACE_RESULTS / "stage16_calibrated_trace_sweep" / "pems7_1026_10_20_posterior_iter20",
    "pems7_228_20_30_fullsearch": TRACE_RESULTS / "stage16_calibrated_trace_sweep" / "pems7_228_20_30_fullsearch",
    "seattle_10_20_30_trainval": TRACE_RESULTS / "stage16_calibrated_trace_sweep" / "seattle_10_20_30_trainval",
    "pems1026_30_trainval_lowcert": TRACE_RESULTS / "stage16_calibrated_trace_probe" / "pems1026_30_trainval_lowcert",
    "train_val_lowcert_delta1_fullsearch": TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe" / "train_val_lowcert_delta1_fullsearch",
}
STAGE15_ROOT_MAP = {
    "PeMS7_1026": TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2" / "pems7_1026",
    "PeMS7_228": TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2" / "pems7_228",
    "Seattle": TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2" / "seattle",
}


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


def evidence_source_label(evidence_source: str) -> str:
    if evidence_source.startswith("stage16_replaceable:"):
        return "Stage16 calibrated rerun"
    if evidence_source == "stage15_main":
        return "Stage15 main evidence"
    return evidence_source


def baseline_label(layout: str) -> str:
    labels = {
        "swap_from_greedy_a_trace": "Swap from A-trace",
        "validation_swap_selected": "Prev. TRACE-SL",
        "rcss_selected": "RCSS",
    }
    return labels.get(layout, layout)


def reading(condition_ratio: float, lower_cond_wins: int, evidence_source: str) -> str:
    if evidence_source.startswith("stage16_replaceable:") and lower_cond_wins == 10:
        return "Promoted rerun improves MAE while lowering the lower-level condition number on every split."
    if condition_ratio <= 1.05:
        return "MAE gains come with near-parity conditioning; no numerical-fragility story is needed."
    return "MAE gains coexist with a modestly higher condition number, so the stability theorem should be read as finite/invertible rather than as a monotone conditioning guarantee."


def find_metric_row(path: Path, dataset: str, budget: float, layout_type: str) -> dict[str, str]:
    for row in load_csv_rows(path):
        if (
            row["dataset"] == dataset
            and abs(float(row["budget"]) - budget) < 1e-12
            and row["layout_type"] == layout_type
            and row["method"] == "gls_map"
        ):
            return row
    raise ValueError(f"Missing row for {path} {dataset} {budget} {layout_type}")


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def main() -> int:
    out_rows: list[dict[str, str]] = []
    for row in load_csv_rows(DELTA_CSV):
        dataset = row["dataset"]
        budget = float(row["budget"])
        budget_pct = int(round(budget * 100))
        evidence_source = row["evidence_source"]
        trace_root = (
            TRACE_ROOT_MAP[evidence_source.split(":", 1)[1]]
            if evidence_source.startswith("stage16_replaceable:")
            else STAGE15_ROOT_MAP[dataset]
        )
        baseline_root = STAGE15_ROOT_MAP[dataset]
        baseline_layout = row["best_baseline_layout"]

        trace_cond = []
        baseline_cond = []
        trace_mae = []
        baseline_mae = []
        for seed in range(25, 35):
            trace_row = find_metric_row(trace_root / f"seed_{seed}" / "metrics.csv", dataset, budget, "trace_biopt")
            baseline_row = find_metric_row(baseline_root / f"seed_{seed}" / "metrics.csv", dataset, budget, baseline_layout)
            trace_cond.append(float(trace_row["condition_number"]))
            baseline_cond.append(float(baseline_row["condition_number"]))
            trace_mae.append(float(trace_row["mae"]))
            baseline_mae.append(float(baseline_row["mae"]))

        trace_cond_mean = mean(trace_cond)
        baseline_cond_mean = mean(baseline_cond)
        condition_ratio = trace_cond_mean / baseline_cond_mean
        lower_cond_wins = sum(t < b for t, b in zip(trace_cond, baseline_cond))
        out_rows.append(
            {
                "dataset": dataset,
                "budget": f"{budget:.1f}",
                "budget_pct": str(budget_pct),
                "trace_source_label": evidence_source_label(evidence_source),
                "best_baseline_label": baseline_label(baseline_layout),
                "trace_mae_mean": f"{mean(trace_mae):.6f}",
                "best_baseline_mae_mean": f"{mean(baseline_mae):.6f}",
                "mae_gap": f"{mean(trace_mae) - mean(baseline_mae):.6f}",
                "trace_condition_mean": f"{trace_cond_mean:.6f}",
                "trace_condition_max": f"{max(trace_cond):.6f}",
                "best_baseline_condition_mean": f"{baseline_cond_mean:.6f}",
                "best_baseline_condition_max": f"{max(baseline_cond):.6f}",
                "condition_ratio": f"{condition_ratio:.6f}",
                "lower_condition_win_count": str(lower_cond_wins),
                "reading": reading(condition_ratio, lower_cond_wins, evidence_source),
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Current-best MAP stability posture against the row-wise strongest baseline.}",
        "\\label{tab:trace-biopt-map-stability}",
        "\\footnotesize",
        "\\begin{tabularx}{\\textwidth}{lccccc>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Dataset & Budget & MAE gap & Cond. ratio & Lower-cond wins & Trace cond. max & Reading \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        lines.append(
            f"{tex_escape(row['dataset'])} & "
            f"{row['budget_pct']}\\% & "
            f"{float(row['mae_gap']):.3f} & "
            f"{float(row['condition_ratio']):.2f}$\\times$ & "
            f"{row['lower_condition_win_count']}/10 & "
            f"{float(row['trace_condition_max']):.0f} & "
            f"{tex_escape(row['reading'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabularx}",
            "\\begin{flushleft}\\footnotesize MAE gap is TRACE-BiOpt minus the row-wise strongest baseline, so negative values favor TRACE-BiOpt. Cond. ratio is the mean TRACE-BiOpt lower-level GLS/MAP condition number divided by the strongest baseline's mean condition number over the ten split-specific runs. This table is a bounded theorem-to-evidence bridge for Theorem~\\ref{thm:map-stability}: it shows whether current-best gains coincide with milder or harsher linear-system conditioning, not a new dominance claim.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
