#!/usr/bin/env python3
"""Generate Stage16 replacement-candidate claim artifacts from calibrated sweeps."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

import pandas as pd

from summarize_stage16_calibrated_progress import build_seed_level, build_summary, read_stage16_metrics

try:
    from scipy import stats
except ImportError:  # pragma: no cover
    stats = None


SCHEMA = "stage16_replacement_claim_contract_v1"
BASELINE_REGISTRY = "TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_10seed_v2/combined/trace_biopt_baseline_registry.csv"


def format_budget(value: float) -> str:
    return f"{100.0 * float(value):.0f}%"


def format_float(value: object) -> str:
    if pd.isna(value):
        return ""
    return f"{float(value):.6g}"


def project_relative(path: Path, root: Path | None = None) -> str:
    resolved = path.resolve()
    base = (root or Path.cwd()).resolve()
    try:
        return resolved.relative_to(base).as_posix()
    except ValueError:
        return path.as_posix()


def evidence_strength(row: pd.Series) -> str:
    completed = int(row["completed_seeds"])
    wins = int(row["wins"])
    paired_t = row.get("delta_paired_t_p")
    if bool(row["all_completed"]) and completed >= 10 and wins == completed and pd.notna(paired_t) and float(paired_t) < 0.05:
        return "submission_ready_paired_dominance"
    if bool(row["all_completed"]):
        return "multi_seed_mean_dominance_paired_mixed"
    if wins == completed and completed > 0:
        return "in_progress_all_completed_seeds_win"
    return "in_progress_mixed_or_incomplete"


def replacement_status(row: pd.Series) -> str:
    if not bool(row["all_completed"]):
        return "in_progress"
    if int(row["wins"]) != int(row["completed_seeds"]):
        return "fail_closed"
    return "replaceable"


def allowed_wording(row: pd.Series) -> str:
    return (
        "The Stage16 calibrated TRACE-BiOpt rerun achieved the lowest mean held-out "
        f"GLS/MAP MAE among the pre-registered non-BiOpt baselines on {row['dataset']} "
        f"at {format_budget(row['budget'])} sensor budget."
    )


def required_caveat(row: pd.Series) -> str:
    if replacement_status(row) == "replaceable":
        return (
            "This wording is restricted to the tested dataset-budget row and the "
            "pre-registered non-BiOpt baseline set."
        )
    return (
        f"Only {int(row['completed_seeds'])}/{int(row['expected_seeds'])} seeds are complete; "
        "do not replace the Stage15 main-table row or use final claim wording yet."
    )


def forbidden_wording(row: pd.Series) -> str:
    return (
        "Do not claim full-table Stage16 replacement, global optimality, untested-baseline "
        "dominance, or cross-network significance from this row alone."
    )


def compute_pair_stats(seed_values: pd.Series) -> dict[str, float | int | None]:
    values = seed_values.dropna().astype(float)
    paired_t_p = None
    wilcoxon_p = None
    if stats is not None and values.shape[0] >= 2:
        try:
            paired_t_p = float(stats.ttest_1samp(values, 0.0, alternative="less").pvalue)
        except Exception:
            paired_t_p = None
        try:
            wilcoxon_p = float(stats.wilcoxon(values, alternative="less").pvalue)
        except Exception:
            wilcoxon_p = None
    return {
        "paired_count": int(values.shape[0]),
        "paired_win_count": int((values < 0).sum()),
        "paired_paired_t_p": paired_t_p,
        "paired_wilcoxon_p": wilcoxon_p,
    }


def build_row_contracts(summary: pd.DataFrame, seed_level: pd.DataFrame, output_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for _, row in summary.sort_values(["dataset", "budget", "stage16_root"]).iterrows():
        sub = seed_level[
            (seed_level["dataset"] == row["dataset"])
            & (seed_level["budget"] == row["budget"])
            & (seed_level["stage16_root"] == row["stage16_root"])
        ]
        pair_stats = compute_pair_stats(sub["delta_vs_best_baseline"])
        stage15_pair_stats = compute_pair_stats(sub["gain_vs_stage15_trace"])
        rows.append(
            {
                "claim_id": f"STAGE16-{row['dataset']}-{format_budget(row['budget']).replace('%', 'pct')}",
                "dataset": row["dataset"],
                "budget": float(row["budget"]),
                "stage16_root": row["stage16_root"],
                "replacement_status": replacement_status(row),
                "evidence_strength": evidence_strength(row),
                "allowed_wording": allowed_wording(row),
                "required_caveat": required_caveat(row),
                "forbidden_wording": forbidden_wording(row),
                "completed_seeds": int(row["completed_seeds"]),
                "expected_seeds": int(row["expected_seeds"]),
                "trace_minus_best_baseline_mean": float(row["mean_delta_vs_best_baseline"]),
                "trace_minus_best_baseline_worst": float(row["worst_delta_vs_best_baseline"]),
                "trace_minus_stage15_trace_mean": float(row["mean_gain_vs_stage15_trace"]),
                "trace_minus_stage15_trace_worst": float(row["worst_gain_vs_stage15_trace"]),
                "paired_count": pair_stats["paired_count"],
                "paired_win_count": pair_stats["paired_win_count"],
                "paired_paired_t_p": pair_stats["paired_paired_t_p"],
                "paired_wilcoxon_p": pair_stats["paired_wilcoxon_p"],
                "stage15_gain_paired_count": stage15_pair_stats["paired_count"],
                "stage15_gain_paired_win_count": stage15_pair_stats["paired_win_count"],
                "stage15_gain_paired_t_p": stage15_pair_stats["paired_paired_t_p"],
                "stage15_gain_wilcoxon_p": stage15_pair_stats["paired_wilcoxon_p"],
                "baseline_registry_source": project_relative(Path(BASELINE_REGISTRY)),
                "seed_level_source": project_relative(output_dir / "stage16_replacement_seed_level.csv"),
                "summary_source": project_relative(output_dir / "stage16_replacement_summary.csv"),
            }
        )
    return rows


def aggregate_status(rows: Sequence[dict[str, object]]) -> dict[str, object]:
    replaceable = [row for row in rows if row["replacement_status"] == "replaceable"]
    in_progress = [row for row in rows if row["replacement_status"] == "in_progress"]
    fail_closed = [row for row in rows if row["replacement_status"] == "fail_closed"]
    return {
        "row_count": len(rows),
        "replaceable_rows": len(replaceable),
        "in_progress_rows": len(in_progress),
        "fail_closed_rows": len(fail_closed),
        "replaceable_claim_ids": [row["claim_id"] for row in replaceable],
        "in_progress_claim_ids": [row["claim_id"] for row in in_progress],
        "fail_closed_claim_ids": [row["claim_id"] for row in fail_closed],
    }


def markdown_table(rows: Sequence[dict[str, object]], columns: Sequence[str]) -> str:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        values = []
        for column in columns:
            value = row.get(column, "")
            if isinstance(value, float):
                values.append(format_float(value))
            else:
                values.append("" if value is None else str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines) + "\n"


def write_outputs(rows: Sequence[dict[str, object]], aggregate: dict[str, object], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    frame.to_csv(output_dir / "stage16_replacement_claim_contract.csv", index=False)
    payload = {"schema": SCHEMA, "aggregate_status": aggregate, "rows": list(rows)}
    (output_dir / "stage16_replacement_claim_contract.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md = [
        "# Stage16 Replacement Claim Contract",
        "",
        f"Replaceable rows: {aggregate['replaceable_rows']}; in-progress rows: {aggregate['in_progress_rows']}; fail-closed rows: {aggregate['fail_closed_rows']}.",
        "",
        markdown_table(
            rows,
            (
                "claim_id",
                "replacement_status",
                "evidence_strength",
                "completed_seeds",
                "expected_seeds",
                "trace_minus_best_baseline_mean",
                "trace_minus_best_baseline_worst",
                "paired_count",
                "paired_win_count",
                "paired_paired_t_p",
            ),
        ),
    ]
    (output_dir / "STAGE16_REPLACEMENT_STATUS.md").write_text("\n".join(md), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Stage16 replacement-candidate claim artifacts")
    parser.add_argument(
        "--stage15-metrics",
        default="TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_10seed_v2/combined/combined_metrics.csv",
    )
    parser.add_argument("--stage16-root", action="append", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    stage15_metrics = pd.read_csv(args.stage15_metrics)
    stage16_metrics = read_stage16_metrics(args.stage16_root)
    seed_level = build_seed_level(stage15_metrics, stage16_metrics)
    summary = build_summary(seed_level, stage15_metrics)
    rows = build_row_contracts(summary, seed_level, output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    seed_level.to_csv(output_dir / "stage16_replacement_seed_level.csv", index=False)
    summary.to_csv(output_dir / "stage16_replacement_summary.csv", index=False)
    write_outputs(rows, aggregate_status(rows), output_dir)
    print(markdown_table(rows, ("claim_id", "replacement_status", "completed_seeds", "expected_seeds", "trace_minus_best_baseline_mean")))


if __name__ == "__main__":
    main()
