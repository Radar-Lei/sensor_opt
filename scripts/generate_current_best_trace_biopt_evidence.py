#!/usr/bin/env python3
"""Generate the current best TRACE-BiOpt dominance/claim artifacts."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import pandas as pd

try:
    from scipy import stats
except ImportError:  # pragma: no cover
    stats = None


ROOT = Path(__file__).resolve().parents[1]
STAGE15_DIR = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined"
REPLACEMENT_DIR = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage16_calibrated_trace_sweep" / "replacement_status"
STAGE15_METRICS = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined" / "combined_metrics.csv"

GROUP_COLUMNS = [
    "dataset",
    "budget",
    "robustness_family",
    "robustness_condition",
    "failure_rate",
    "noise_scale",
    "missing_rate",
    "missing_block_steps",
    "cost_proxy",
    "cost_budget",
    "split_mode",
]


def compute_paired(values: pd.Series) -> dict[str, float | int]:
    series = values.dropna().astype(float)
    paired_t_p = float("nan")
    wilcoxon_p = float("nan")
    if stats is not None and series.shape[0] >= 2:
        try:
            paired_t_p = float(stats.ttest_1samp(series, 0.0, alternative="less").pvalue)
        except Exception:
            paired_t_p = float("nan")
        try:
            wilcoxon_p = float(stats.wilcoxon(series, alternative="less").pvalue)
        except Exception:
            wilcoxon_p = float("nan")
    return {
        "paired_delta_mean": float(series.mean()),
        "paired_delta_std": float(series.std(ddof=1)) if series.shape[0] >= 2 else 0.0,
        "paired_delta_sem": float(series.std(ddof=1) / (series.shape[0] ** 0.5)) if series.shape[0] >= 2 else 0.0,
        "paired_ci95_low": float("nan"),
        "paired_ci95_high": float("nan"),
        "paired_cohens_dz": float("nan"),
        "paired_paired_t_p": paired_t_p,
        "paired_wilcoxon_p": wilcoxon_p,
        "paired_win_count": int((series < 0).sum()),
        "paired_count": int(series.shape[0]),
    }


def add_interval_fields(stats_dict: dict[str, float | int]) -> dict[str, float | int]:
    count = int(stats_dict["paired_count"])
    sem = float(stats_dict["paired_delta_sem"])
    mean = float(stats_dict["paired_delta_mean"])
    std = float(stats_dict["paired_delta_std"])
    if count >= 2:
        ci_half = 1.96 * sem
        stats_dict["paired_ci95_low"] = mean - ci_half
        stats_dict["paired_ci95_high"] = mean + ci_half
        stats_dict["paired_cohens_dz"] = mean / std if std > 0 else float("nan")
    return stats_dict


def format_value(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value)


def markdown_table(frame: pd.DataFrame) -> str:
    columns = list(frame.columns)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for _, row in frame.iterrows():
        lines.append("| " + " | ".join(format_value(row[column]) for column in columns) + " |")
    return "\n".join(lines)


def build_stage16_override_rows(
    stage15_rows: pd.DataFrame,
    replacement_contract: pd.DataFrame,
    replacement_seed_level: pd.DataFrame,
    stage15_metrics: pd.DataFrame,
) -> pd.DataFrame:
    replaceable = replacement_contract[replacement_contract["replacement_status"] == "replaceable"].copy()
    if replaceable.empty:
        return pd.DataFrame(columns=list(stage15_rows.columns) + ["evidence_source"])

    metrics = stage15_metrics[stage15_metrics["method"] == "gls_map"].copy()
    rows = []
    for _, repl in replaceable.iterrows():
        mask = (stage15_rows["dataset"] == repl["dataset"]) & (stage15_rows["budget"] == repl["budget"])
        original = stage15_rows.loc[mask]
        if original.empty:
            raise ValueError(f"missing Stage15 dominance row for {repl['dataset']} budget={repl['budget']}")
        original_row = original.iloc[0]
        seed_sub = replacement_seed_level[
            (replacement_seed_level["dataset"] == repl["dataset"])
            & (replacement_seed_level["budget"] == repl["budget"])
            & (replacement_seed_level["stage16_root"] == repl["stage16_root"])
        ].copy()
        baseline_layout = original_row["best_baseline_layout"]
        baseline_sub = metrics[
            (metrics["dataset"] == repl["dataset"])
            & (metrics["budget"] == repl["budget"])
            & (metrics["layout_type"] == baseline_layout)
        ][GROUP_COLUMNS + ["split_seed", "mae"]].rename(columns={"mae": "fixed_baseline_mae"})
        merged = seed_sub.merge(baseline_sub, on=GROUP_COLUMNS + ["split_seed"], how="inner")
        if merged.shape[0] != seed_sub.shape[0]:
            raise ValueError(f"missing fixed-baseline rows for {repl['dataset']} {repl['budget']} {baseline_layout}")
        merged["delta_vs_fixed_baseline"] = merged["stage16_trace_mae"] - merged["fixed_baseline_mae"]
        pair_stats = add_interval_fields(compute_paired(merged["delta_vs_fixed_baseline"]))
        stage16_mean = float(merged["stage16_trace_mae"].mean())
        fixed_baseline_mean = float(merged["fixed_baseline_mae"].mean())
        row = original_row.to_dict()
        row.update(
            {
                "trace_biopt_mean": stage16_mean,
                "best_baseline_mean": fixed_baseline_mean,
                "trace_minus_best_baseline": stage16_mean - fixed_baseline_mean,
                "trace_beats_best_baseline": bool(stage16_mean < fixed_baseline_mean),
                "paired_delta_mean": pair_stats["paired_delta_mean"],
                "paired_delta_std": pair_stats["paired_delta_std"],
                "paired_delta_sem": pair_stats["paired_delta_sem"],
                "paired_ci95_low": pair_stats["paired_ci95_low"],
                "paired_ci95_high": pair_stats["paired_ci95_high"],
                "paired_cohens_dz": pair_stats["paired_cohens_dz"],
                "paired_paired_t_p": pair_stats["paired_paired_t_p"],
                "paired_wilcoxon_p": pair_stats["paired_wilcoxon_p"],
                "paired_win_count": pair_stats["paired_win_count"],
                "paired_count": pair_stats["paired_count"],
                "evidence_source": f"stage16_replaceable:{repl['stage16_root']}",
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
    )
    args = parser.parse_args()

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    stage15_rows = pd.read_csv(STAGE15_DIR / "trace_biopt_best_baseline_delta.csv")
    stage15_rows["evidence_source"] = "stage15_main"
    replacement_contract = pd.read_csv(REPLACEMENT_DIR / "stage16_replacement_claim_contract.csv")
    replacement_seed_level = pd.read_csv(REPLACEMENT_DIR / "stage16_replacement_seed_level.csv")
    stage15_metrics = pd.read_csv(STAGE15_METRICS)

    override_rows = build_stage16_override_rows(stage15_rows, replacement_contract, replacement_seed_level, stage15_metrics)
    if not override_rows.empty:
        keep_mask = pd.Series(True, index=stage15_rows.index)
        for _, row in override_rows.iterrows():
            keep_mask &= ~(
                (stage15_rows["dataset"] == row["dataset"])
                & (stage15_rows["budget"] == row["budget"])
            )
        combined = pd.concat([stage15_rows.loc[keep_mask], override_rows], ignore_index=True, sort=False)
    else:
        combined = stage15_rows.copy()
    combined = combined.sort_values(["dataset", "budget"]).reset_index(drop=True)

    combined.to_csv(output_dir / "trace_biopt_best_baseline_delta.csv", index=False)
    md_lines = [
        "# TRACE-BiOpt Current Best Dominance",
        "",
        "Rows marked `stage16_replaceable:*` use replaceable Stage16 calibrated evidence; all other rows retain the Stage15 main evidence.",
        "",
        markdown_table(combined),
        "",
    ]
    (output_dir / "TRACE_BIOPT_DOMINANCE.md").write_text("\n".join(md_lines), encoding="utf-8")

    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "generate_trace_biopt_claim_contract.py"),
            "--dominance",
            str(output_dir / "trace_biopt_best_baseline_delta.csv"),
            "--paired-tests",
            str(STAGE15_DIR / "gls_map_paired_delta_tests.csv"),
            "--layout-summary",
            str(STAGE15_DIR / "gls_map_layout_summary.csv"),
            "--output-dir",
            str(output_dir),
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "generate_current_best_trace_biopt_dominance_table.py"),
            "--dominance-csv",
            str(output_dir / "trace_biopt_best_baseline_delta.csv"),
            "--output-tex",
            str(ROOT / "paper" / "tables" / "table_trace_biopt_dominance.tex"),
        ],
        cwd=ROOT,
        check=True,
    )

    summary = combined[["dataset", "budget", "trace_biopt_mean", "best_baseline_mean", "trace_minus_best_baseline", "evidence_source"]]
    print(markdown_table(summary))


if __name__ == "__main__":
    main()
