#!/usr/bin/env python3
"""Generate TRACE-BiOpt low-budget calibration-risk probe artifacts."""

from __future__ import annotations

import csv
import math
from pathlib import Path

import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[1]
STAGE15_PEMS = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "pems7_228"
PROBE = (
    ROOT
    / "TRC-23-02333"
    / "trace_sl_results"
    / "stage15_biopt_pems228_10_risksource_probe"
    / "train_val_lowcert_delta1_fullsearch"
)
PAPER_SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
TABLE_PATH = ROOT / "paper" / "tables" / "table_trace_biopt_calibration_probe.tex"
CSV_PATH = PAPER_SOURCES / "trace_biopt_calibration_risk_probe.csv"
SEEDS = list(range(25, 35))


def gls_rows(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    return frame[(frame["method"] == "gls_map") & (frame["budget"].round(8) == 0.1)].copy()


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for seed in SEEDS:
        default_rows = gls_rows(STAGE15_PEMS / f"seed_{seed}" / "metrics.csv")
        probe_rows = gls_rows(PROBE / f"seed_{seed}" / "metrics.csv")
        default_trace = float(default_rows.loc[default_rows["layout_type"] == "trace_biopt", "mae"].iloc[0])
        calibrated_trace = float(probe_rows.loc[probe_rows["layout_type"] == "trace_biopt", "mae"].iloc[0])
        best = default_rows[default_rows["layout_type"] != "trace_biopt"].sort_values(["mae", "layout_type"]).iloc[0]
        best_mae = float(best["mae"])
        rows.append(
            {
                "dataset": "PeMS7_228",
                "budget": 0.1,
                "split_seed": seed,
                "default_trace_mae": default_trace,
                "calibrated_trace_mae": calibrated_trace,
                "best_baseline_layout": str(best["layout_type"]),
                "best_baseline_mae": best_mae,
                "default_delta": default_trace - best_mae,
                "calibrated_delta": calibrated_trace - best_mae,
                "trace_mae_improvement": default_trace - calibrated_trace,
                "calibrated_beats_best_baseline": calibrated_trace < best_mae,
                "probe_scope": "diagnostic low-budget calibration-risk probe",
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
    mean_calibrated_delta = sum(float(row["calibrated_delta"]) for row in rows) / len(rows)
    mean_improvement = sum(float(row["trace_mae_improvement"]) for row in rows) / len(rows)
    calibrated_delta = pd.Series([float(row["calibrated_delta"]) for row in rows])
    improvement = pd.Series([float(row["trace_mae_improvement"]) for row in rows])
    paired_t_p = float(stats.ttest_1samp(calibrated_delta, 0.0, alternative="less").pvalue)
    wilcoxon_p = float(stats.wilcoxon(calibrated_delta, alternative="less").pvalue)
    improvement_p = float(stats.ttest_1samp(improvement, 0.0, alternative="greater").pvalue)
    if not all(math.isfinite(value) for value in [paired_t_p, wilcoxon_p, improvement_p]):
        raise ValueError("Non-finite calibration-probe p-value")

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{PeMS7\\_228 10\\% low-budget calibration-risk diagnostic over the original Stage15 ten split seeds. The calibrated TRACE-BiOpt rerun keeps a single reconstruction-aware objective, estimates upper-level reconstruction risk on train+validation days, lowers certificate weights, and uses complete one-exchange search. Baseline values are the seed-matched pre-registered non-BiOpt rows from the Stage15 evidence path. This rerun now supplies the current-best evidence for the PeMS7\\_228 10\\% row while leaving the other dataset-budget rows on their own evidence paths.}",
        "\\label{tab:trace-biopt-calibration-probe}",
        "\\small",
        "\\begin{tabular}{rccccc}",
        "\\toprule",
        "Seed & Default $\\Delta$ & Calibrated $\\Delta$ & MAE gain & Best baseline & Calibrated beats? \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{int(row['split_seed'])} & "
            f"{float(row['default_delta']):.4f} & "
            f"{float(row['calibrated_delta']):.4f} & "
            f"{float(row['trace_mae_improvement']):.4f} & "
            f"{esc(row['best_baseline_layout'])} & "
            f"{'yes' if row['calibrated_beats_best_baseline'] else 'no'} \\\\"
        )
    lines.extend(
        [
            "\\midrule",
            f"Mean & {mean_default_delta:.4f} & {mean_calibrated_delta:.4f} & {mean_improvement:.4f} & -- & {sum(bool(row['calibrated_beats_best_baseline']) for row in rows)}/{len(rows)} \\\\",
            "\\bottomrule",
            "\\end{tabular}",
            (
                "\\vspace{2pt}\\raggedright\\footnotesize "
                f"Calibrated-risk paired t-test versus zero delta: $p={paired_t_p:.1e}$; "
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
