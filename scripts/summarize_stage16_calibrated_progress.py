import argparse
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

try:
    from scipy import stats
except ImportError:  # pragma: no cover
    stats = None


CONDITION_COLUMNS = [
    "dataset",
    "budget",
    "robustness_family",
    "robustness_condition",
    "failure_rate",
    "noise_scale",
    "missing_rate",
    "missing_block_steps",
    "split_mode",
    "cost_proxy",
    "cost_budget",
]

SEED_PATTERN = re.compile(r"seed_(\d+)")


def group_columns(frame):
    return [name for name in CONDITION_COLUMNS if name in frame.columns] + ["split_seed"]


def read_stage16_metrics(stage16_roots):
    frames = []
    for root in stage16_roots:
        root_path = Path(root)
        for metrics_path in sorted(root_path.glob("seed_*/metrics.csv")):
            frame = pd.read_csv(metrics_path)
            frame["stage16_root"] = root_path.name
            frame["stage16_metrics_path"] = str(metrics_path)
            frames.append(frame)
    if not frames:
        raise ValueError("no Stage16 metrics.csv files found under the provided roots")
    combined = pd.concat(frames, ignore_index=True)
    required = {"method", "layout_type", "mae"}
    missing = required.difference(combined.columns)
    if missing:
        raise ValueError(f"Stage16 metrics missing columns: {sorted(missing)}")
    return combined


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def parse_seed_from_name(path):
    match = SEED_PATTERN.search(Path(path).name)
    if not match:
        raise ValueError(f"could not parse seed from path: {path}")
    return int(match.group(1))


def last_progress_event(progress_path):
    progress_file = Path(progress_path)
    if not progress_file.exists():
        return {}
    lines = progress_file.read_text(encoding="utf-8").splitlines()
    if not lines:
        return {}
    return json.loads(lines[-1])


def to_float_or_nan(value):
    if value is None:
        return float("nan")
    try:
        return float(value)
    except (TypeError, ValueError):
        return float("nan")


def to_int_or_nan(value):
    if value is None:
        return float("nan")
    try:
        return int(value)
    except (TypeError, ValueError):
        return float("nan")


def collect_live_progress(stage16_roots, stale_minutes=30.0, now_ts=None):
    now_ts = datetime.now(timezone.utc).timestamp() if now_ts is None else float(now_ts)
    stale_seconds = float(stale_minutes) * 60.0
    rows = []
    for root in stage16_roots:
        root_path = Path(root)
        progress_dir = root_path / "progress"
        if not progress_dir.exists():
            continue
        for checkpoint_path in sorted(progress_dir.glob("seed_*_checkpoint.json")):
            split_seed = parse_seed_from_name(checkpoint_path)
            metrics_path = root_path / f"seed_{split_seed}" / "metrics.csv"
            if metrics_path.exists():
                continue
            checkpoint = read_json(checkpoint_path)
            progress_path = checkpoint_path.with_name(checkpoint_path.name.replace("_checkpoint.json", "_progress.jsonl"))
            last_event = last_progress_event(progress_path)
            merged = {**last_event, **checkpoint}
            last_mtime = checkpoint_path.stat().st_mtime
            if progress_path.exists():
                last_mtime = max(last_mtime, progress_path.stat().st_mtime)
            age_seconds = max(0.0, now_ts - last_mtime)
            rows.append(
                {
                    "dataset": merged.get("dataset", ""),
                    "budget": to_float_or_nan(merged.get("budget")),
                    "stage16_root": root_path.name,
                    "split_seed": split_seed,
                    "layout_seed": to_int_or_nan(merged.get("layout_seed")),
                    "latest_stage": merged.get("latest_stage") or merged.get("stage") or "",
                    "iteration": to_int_or_nan(merged.get("iteration")),
                    "objective": to_float_or_nan(merged.get("objective")),
                    "reconstruction_huber": to_float_or_nan(merged.get("reconstruction_huber")),
                    "selected_sensor_count": to_int_or_nan(merged.get("selected_sensor_count")),
                    "sensor_count": to_int_or_nan(merged.get("sensor_count")),
                    "max_rss_mb": to_float_or_nan(merged.get("max_rss_mb")),
                    "last_update_utc": datetime.fromtimestamp(last_mtime, tz=timezone.utc).isoformat(),
                    "last_update_age_minutes": age_seconds / 60.0,
                    "stale": bool(age_seconds > stale_seconds),
                    "checkpoint_path": str(checkpoint_path),
                    "progress_path": str(progress_path) if progress_path.exists() else "",
                    "metrics_path": str(metrics_path),
                }
            )
    if not rows:
        return pd.DataFrame(
            columns=[
                "dataset",
                "budget",
                "stage16_root",
                "split_seed",
                "layout_seed",
                "latest_stage",
                "iteration",
                "objective",
                "reconstruction_huber",
                "selected_sensor_count",
                "sensor_count",
                "max_rss_mb",
                "last_update_utc",
                "last_update_age_minutes",
                "stale",
                "checkpoint_path",
                "progress_path",
                "metrics_path",
            ]
        )
    return pd.DataFrame(rows).sort_values(["dataset", "stage16_root", "split_seed"]).reset_index(drop=True)


def best_baseline_rows(stage15_metrics):
    base = stage15_metrics[stage15_metrics["method"] == "gls_map"].copy()
    groups = group_columns(base)
    baselines = base[base["layout_type"] != "trace_biopt"].copy()
    baselines["mae"] = pd.to_numeric(baselines["mae"], errors="raise")
    best = (
        baselines.sort_values(groups + ["mae", "layout_type"])
        .groupby(groups, dropna=False, as_index=False)
        .first()
        .rename(
            columns={
                "layout_type": "best_baseline_layout",
                "mae": "best_baseline_mae",
                "layout_seed": "best_baseline_layout_seed",
            }
        )
    )
    return best


def old_trace_rows(stage15_metrics):
    base = stage15_metrics[stage15_metrics["method"] == "gls_map"].copy()
    groups = group_columns(base)
    trace = (
        base[base["layout_type"] == "trace_biopt"]
        .copy()
        .rename(columns={"mae": "stage15_trace_mae"})
    )
    extra = [name for name in ["layout_seed", "validation_selected_mae"] if name in trace.columns]
    keep = [*groups, "stage15_trace_mae", *extra]
    return trace[keep].drop_duplicates()


def stage16_trace_rows(stage16_metrics):
    base = stage16_metrics[
        (stage16_metrics["method"] == "gls_map")
        & (stage16_metrics["layout_type"] == "trace_biopt")
    ].copy()
    if base.empty:
        raise ValueError("Stage16 metrics contain no gls_map/trace_biopt rows")
    base = base.rename(columns={"mae": "stage16_trace_mae"})
    groups = group_columns(base)
    keep = [*groups, "stage16_root", "stage16_trace_mae"]
    if "layout_seed" in base.columns:
        keep.append("layout_seed")
    if "validation_selected_mae" in base.columns:
        keep.append("validation_selected_mae")
    if "posterior_trace" in base.columns:
        keep.append("posterior_trace")
    return base[keep].drop_duplicates()


def attach_stats(values):
    values = pd.Series(values).dropna().astype(float)
    if values.empty:
        return {
            "mean": float("nan"),
            "worst": float("nan"),
            "wins": 0,
            "count": 0,
            "paired_t_p": float("nan"),
            "wilcoxon_p": float("nan"),
        }
    paired_t_p = float("nan")
    wilcoxon_p = float("nan")
    if stats is not None and values.shape[0] >= 2:
        try:
            paired_t_p = float(stats.ttest_1samp(values, 0.0, alternative="less").pvalue)
        except Exception:
            paired_t_p = float("nan")
        try:
            wilcoxon_p = float(stats.wilcoxon(values, alternative="less").pvalue)
        except Exception:
            wilcoxon_p = float("nan")
    return {
        "mean": float(values.mean()),
        "worst": float(values.max()),
        "wins": int((values < 0).sum()),
        "count": int(values.shape[0]),
        "paired_t_p": paired_t_p,
        "wilcoxon_p": wilcoxon_p,
    }


def build_seed_level(stage15_metrics, stage16_metrics):
    groups = group_columns(stage15_metrics)
    best = best_baseline_rows(stage15_metrics)
    old_trace = old_trace_rows(stage15_metrics)
    stage16 = stage16_trace_rows(stage16_metrics)
    merged = stage16.merge(best, on=groups, how="inner").merge(old_trace, on=groups, how="left")
    if merged.empty:
        raise ValueError("no overlapping Stage15/Stage16 rows after join")
    merged["delta_vs_best_baseline"] = merged["stage16_trace_mae"] - merged["best_baseline_mae"]
    merged["gain_vs_stage15_trace"] = merged["stage16_trace_mae"] - merged["stage15_trace_mae"]
    merged["stage16_beats_best_baseline"] = merged["delta_vs_best_baseline"] < 0
    merged = merged.sort_values(["dataset", "budget", "split_seed", "stage16_root"]).reset_index(drop=True)
    return merged


def build_summary(seed_level, stage15_metrics):
    groups = [name for name in CONDITION_COLUMNS if name in seed_level.columns] + ["stage16_root"]
    expected = (
        stage15_metrics[stage15_metrics["method"] == "gls_map"]
        .groupby([name for name in CONDITION_COLUMNS if name in stage15_metrics.columns], dropna=False)["split_seed"]
        .nunique()
        .reset_index(name="expected_seeds")
    )
    rows = []
    for group_key, sub in seed_level.groupby(groups, dropna=False):
        group_key = group_key if isinstance(group_key, tuple) else (group_key,)
        base = dict(zip(groups, group_key))
        join_cols = [name for name in CONDITION_COLUMNS if name in base]
        expected_match = expected
        if join_cols:
            key_values = tuple(base[name] for name in join_cols)
            mask = (expected[join_cols] == pd.Series(key_values, index=join_cols)).all(axis=1)
            expected_match = expected[mask]
        expected_seeds = int(expected_match["expected_seeds"].iloc[0]) if not expected_match.empty else int(sub["split_seed"].nunique())
        delta_stats = attach_stats(sub["delta_vs_best_baseline"])
        gain_stats = attach_stats(sub["gain_vs_stage15_trace"])
        rows.append(
            {
                **base,
                "completed_seeds": int(sub["split_seed"].nunique()),
                "expected_seeds": expected_seeds,
                "all_completed": bool(sub["split_seed"].nunique() == expected_seeds),
                "wins": delta_stats["wins"],
                "losses_or_ties": int(delta_stats["count"] - delta_stats["wins"]),
                "mean_delta_vs_best_baseline": delta_stats["mean"],
                "worst_delta_vs_best_baseline": delta_stats["worst"],
                "delta_paired_t_p": delta_stats["paired_t_p"],
                "delta_wilcoxon_p": delta_stats["wilcoxon_p"],
                "mean_gain_vs_stage15_trace": gain_stats["mean"],
                "worst_gain_vs_stage15_trace": gain_stats["worst"],
                "gain_paired_t_p": gain_stats["paired_t_p"],
                "gain_wilcoxon_p": gain_stats["wilcoxon_p"],
            }
        )
    return pd.DataFrame(rows).sort_values(groups).reset_index(drop=True)


def markdown_table(frame):
    columns = [
        "dataset",
        "budget",
        "stage16_root",
        "completed_seeds",
        "expected_seeds",
        "wins",
        "losses_or_ties",
        "mean_delta_vs_best_baseline",
        "worst_delta_vs_best_baseline",
        "mean_gain_vs_stage15_trace",
        "delta_paired_t_p",
        "delta_wilcoxon_p",
    ]
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, separator]
    for _, row in frame[columns].iterrows():
        values = []
        for column in columns:
            value = row[column]
            if isinstance(value, float):
                values.append(f"{value:.6g}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def live_markdown_table(frame):
    columns = [
        "dataset",
        "budget",
        "stage16_root",
        "split_seed",
        "latest_stage",
        "iteration",
        "objective",
        "reconstruction_huber",
        "selected_sensor_count",
        "max_rss_mb",
        "last_update_age_minutes",
        "stale",
    ]
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, separator]
    for _, row in frame[columns].iterrows():
        values = []
        for column in columns:
            value = row[column]
            if isinstance(value, bool):
                values.append("yes" if value else "no")
            elif isinstance(value, float):
                if math.isnan(value):
                    values.append("")
                else:
                    values.append(f"{value:.6g}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Summarize completed Stage16 calibrated sweep progress against Stage15 evidence")
    parser.add_argument(
        "--stage15-metrics",
        default="TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_10seed_v2/combined/combined_metrics.csv",
    )
    parser.add_argument("--stage16-root", action="append", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--stale-minutes", type=float, default=30.0)
    args = parser.parse_args()

    stage15_metrics = pd.read_csv(args.stage15_metrics)
    stage16_metrics = read_stage16_metrics(args.stage16_root)
    seed_level = build_seed_level(stage15_metrics, stage16_metrics)
    summary = build_summary(seed_level, stage15_metrics)
    live_progress = collect_live_progress(args.stage16_root, stale_minutes=args.stale_minutes)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    seed_level.to_csv(output_dir / "stage16_progress_seed_level.csv", index=False)
    summary.to_csv(output_dir / "stage16_progress_summary.csv", index=False)
    live_progress.to_csv(output_dir / "stage16_live_progress.csv", index=False)
    lines = [
        "# Stage16 Calibrated Sweep Progress",
        "",
        "Negative `mean_delta_vs_best_baseline` means the completed Stage16 TRACE-BiOpt rows beat the Stage15 seed-matched best non-BiOpt baseline.",
        "Negative `mean_gain_vs_stage15_trace` means Stage16 improves over the original Stage15 TRACE-BiOpt row.",
        "",
        markdown_table(summary),
        "",
    ]
    if live_progress.empty:
        lines.extend(
            [
                "## Live In-Progress Seeds",
                "",
                "No in-progress seeds detected under the provided Stage16 roots.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Live In-Progress Seeds",
                "",
                f"`stale=yes` means the most recent checkpoint/progress update is older than {args.stale_minutes:.0f} minutes.",
                "",
                live_markdown_table(live_progress),
                "",
            ]
        )
    (output_dir / "STAGE16_PROGRESS.md").write_text("\n".join(lines), encoding="utf-8")
    print(markdown_table(summary))
    if not live_progress.empty:
        print()
        print(live_markdown_table(live_progress))


if __name__ == "__main__":
    main()
