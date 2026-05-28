#!/usr/bin/env python3
"""Generate TRACE-BiOpt weak-row search-budget probe artifacts."""

from __future__ import annotations

import csv
import math
from pathlib import Path

import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[1]
STAGE15_PEMS = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "pems7_1026"
EXTRA_DEFAULT = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_pems1026_30_extra"
ENHANCED_TRACEONLY = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_pems1026_30_search_traceonly"
ENHANCED_FULL = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_pems1026_30_search_probe"
PAPER_SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
TABLE_PATH = ROOT / "paper" / "tables" / "table_trace_biopt_search_probe.tex"
CSV_PATH = PAPER_SOURCES / "trace_biopt_search_budget_probe.csv"


SEEDS = list(range(25, 35))


def gls_rows(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    return frame[(frame["method"] == "gls_map") & (frame["budget"].round(8) == 0.3)].copy()


def metrics_path(seed: int, enhanced: bool) -> Path:
    if enhanced:
        return ENHANCED_TRACEONLY / f"seed_{seed}" / "metrics.csv"
    return STAGE15_PEMS / f"seed_{seed}" / "metrics.csv"


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for seed in SEEDS:
        default_rows = gls_rows(metrics_path(seed, enhanced=False))
        enhanced_rows = gls_rows(metrics_path(seed, enhanced=True))
        default_trace = float(default_rows.loc[default_rows["layout_type"] == "trace_biopt", "mae"].iloc[0])
        enhanced_trace = float(enhanced_rows.loc[enhanced_rows["layout_type"] == "trace_biopt", "mae"].iloc[0])
        best = default_rows[default_rows["layout_type"] != "trace_biopt"].sort_values(["mae", "layout_type"]).iloc[0]
        best_mae = float(best["mae"])
        rows.append(
            {
                "dataset": "PeMS7_1026",
                "budget": 0.3,
                "split_seed": seed,
                "default_trace_mae": default_trace,
                "enhanced_trace_mae": enhanced_trace,
                "best_baseline_layout": str(best["layout_type"]),
                "best_baseline_mae": best_mae,
                "default_delta": default_trace - best_mae,
                "enhanced_delta": enhanced_trace - best_mae,
                "trace_mae_improvement": default_trace - enhanced_trace,
                "enhanced_beats_best_baseline": enhanced_trace < best_mae,
                "probe_scope": "diagnostic weak-row search-budget probe",
            }
        )
    return rows


def esc(value: object) -> str:
    return str(value).replace("_", "\\_").replace("%", "\\%")


def write_csv(rows: list[dict[str, object]]) -> None:
    PAPER_SOURCES.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_tex(rows: list[dict[str, object]]) -> None:
    mean_default_delta = sum(float(row["default_delta"]) for row in rows) / len(rows)
    mean_enhanced_delta = sum(float(row["enhanced_delta"]) for row in rows) / len(rows)
    mean_improvement = sum(float(row["trace_mae_improvement"]) for row in rows) / len(rows)
    enhanced_delta = pd.Series([float(row["enhanced_delta"]) for row in rows])
    improvement = pd.Series([float(row["trace_mae_improvement"]) for row in rows])
    paired_t_p = float(stats.ttest_1samp(enhanced_delta, 0.0, alternative="less").pvalue)
    wilcoxon_p = float(stats.wilcoxon(enhanced_delta, alternative="less").pvalue)
    improvement_p = float(stats.ttest_1samp(improvement, 0.0, alternative="greater").pvalue)
    if not all(math.isfinite(value) for value in [paired_t_p, wilcoxon_p, improvement_p]):
        raise ValueError("Non-finite search-probe p-value")
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{PeMS7\\_1026 30\\% weak-row enhanced-search evidence over the original Stage15 ten split seeds. The enhanced TRACE-BiOpt rerun keeps the same objective and increases only deterministic exchange-search pools/iterations. Baseline values are the seed-matched pre-registered non-BiOpt rows from the Stage15 evidence path. This row-level diagnostic strengthens the weakest regime but does not replace the full nine-regime Stage15 main table.}",
        "\\label{tab:trace-biopt-search-probe}",
        "\\small",
        "\\begin{tabular}{rccccc}",
        "\\toprule",
        "Seed & Default $\\Delta$ & Enhanced $\\Delta$ & MAE gain & Best baseline & Enhanced beats? \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{int(row['split_seed'])} & "
            f"{float(row['default_delta']):.4f} & "
            f"{float(row['enhanced_delta']):.4f} & "
            f"{float(row['trace_mae_improvement']):.4f} & "
            f"{esc(row['best_baseline_layout'])} & "
            f"{'yes' if row['enhanced_beats_best_baseline'] else 'no'} \\\\"
        )
    lines.extend(
        [
            "\\midrule",
            f"Mean & {mean_default_delta:.4f} & {mean_enhanced_delta:.4f} & {mean_improvement:.4f} & -- & {sum(bool(row['enhanced_beats_best_baseline']) for row in rows)}/{len(rows)} \\\\",
            "\\bottomrule",
            "\\end{tabular}",
            (
                "\\vspace{2pt}\\raggedright\\footnotesize "
                f"Enhanced-search paired t-test versus zero delta: $p={paired_t_p:.1e}$; "
                f"Wilcoxon signed-rank $p={wilcoxon_p:.4f}$; "
                f"mean MAE-gain t-test $p={improvement_p:.1e}$. "
                "Negative $\\Delta$ means TRACE-BiOpt has lower held-out GLS/MAP MAE than the seed-matched best pre-registered non-BiOpt baseline."
            ),
            "\\end{table*}",
        ]
    )
    TABLE_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = build_rows()
    write_csv(rows)
    write_tex(rows)
    print(f"Wrote {CSV_PATH}")
    print(f"Wrote {TABLE_PATH}")


if __name__ == "__main__":
    main()
