import argparse
import re
from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError
from scipy.stats import sem, t, ttest_rel, wilcoxon


def paired_delta_stats(delta):
    matched = pd.to_numeric(delta, errors="coerce").dropna()
    count = int(matched.shape[0])
    stats_row = {
        "delta_mean": matched.mean() if count else pd.NA,
        "delta_std": matched.std() if count else pd.NA,
        "delta_sem": pd.NA,
        "ci95_low": pd.NA,
        "ci95_high": pd.NA,
        "cohens_dz": pd.NA,
        "paired_t_p": pd.NA,
        "wilcoxon_p": pd.NA,
        "win_count": int((matched < 0).sum()),
        "count": count,
    }
    if count < 2:
        return stats_row

    delta_std = matched.std()
    delta_sem = sem(matched)
    interval_radius = t.ppf(0.975, count - 1) * delta_sem
    stats_row["delta_sem"] = delta_sem
    stats_row["ci95_low"] = matched.mean() - interval_radius
    stats_row["ci95_high"] = matched.mean() + interval_radius
    stats_row["cohens_dz"] = matched.mean() / delta_std if delta_std != 0 else pd.NA
    stats_row["paired_t_p"] = ttest_rel(matched, pd.Series(0.0, index=matched.index), nan_policy="omit").pvalue
    try:
        stats_row["wilcoxon_p"] = wilcoxon(matched).pvalue
    except ValueError:
        stats_row["wilcoxon_p"] = pd.NA
    return stats_row


CONDITION_COLUMNS = [
    "candidate_count",
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


def normalize_group_key(group_key):
    return group_key if isinstance(group_key, tuple) else (group_key,)


def condition_group_columns(frame):
    return ["budget", *[name for name in CONDITION_COLUMNS if name in frame.columns]]


def sort_frame(frame, sort_cols):
    present = [name for name in sort_cols if name in frame.columns]
    if frame.empty or not present:
        return frame.reset_index(drop=True)
    return frame.sort_values(present).reset_index(drop=True)


def build_layout_summary(gls):
    evidence_group_cols = condition_group_columns(gls)
    layout_group_cols = [*evidence_group_cols, "layout_type"]
    summary = (
        gls.groupby(layout_group_cols, dropna=False)["mae"]
        .agg(["mean", "std", "count"])
        .reset_index()
    )
    return sort_frame(summary, [*evidence_group_cols, "mean"])


def build_paired_comparisons(pivot, comparison_layouts, baseline_layouts):
    delta_rows = []
    paired_rows = []
    group_levels = [name for name in pivot.index.names if name != "split_seed"]
    for group_key, sub in pivot.groupby(level=group_levels):
        group_key = normalize_group_key(group_key)
        row = dict(zip(group_levels, group_key))
        drop_levels = [name for name in group_levels if name in sub.index.names and len(sub.index.get_level_values(name).unique()) == 1]
        sub = sub.droplevel(drop_levels)
        for layout in comparison_layouts:
            if layout not in sub.columns:
                continue
            for baseline in baseline_layouts:
                if baseline not in sub.columns:
                    continue
                delta = sub[layout] - sub[baseline]
                stats_row = paired_delta_stats(delta)
                row[f"{layout}_minus_{baseline}_mean"] = stats_row["delta_mean"]
                row[f"{layout}_minus_{baseline}_std"] = stats_row["delta_std"]
                paired_rows.append(
                    {
                        **dict(zip(group_levels, group_key)),
                        "layout": layout,
                        "baseline": baseline,
                        **stats_row,
                    }
                )
        delta_rows.append(row)
    sort_cols = [name for name in condition_group_columns(pivot.reset_index()) if name in group_levels]
    return sort_frame(pd.DataFrame(delta_rows), sort_cols), sort_frame(pd.DataFrame(paired_rows), sort_cols)


def build_certificate_summary(corr):
    return corr.groupby(["method", "certificate"])[["pearson_mae", "spearman_mae"]].agg(["mean", "std", "min", "max", "count"])


def flatten_certificate_summary(corr_summary):
    flat = corr_summary.reset_index()
    flat.columns = [
        "_".join(str(part) for part in column if str(part)) if isinstance(column, tuple) else str(column)
        for column in flat.columns
    ]
    return flat


def certificate_summary_lines(corr_summary):
    return [
        "## Empirical certificate-error correlation summary",
        "",
        "These correlations are empirical support for certificate-guided selection, not formal optimality guarantees.",
        "",
        "```",
        corr_summary.to_string(),
        "```",
        "",
    ]


def selected_candidate_mask(frame):
    if "selected" not in frame.columns:
        return pd.Series(False, index=frame.index)
    selected = frame["selected"]
    if selected.dtype == bool:
        return selected.fillna(False)
    return selected.astype(str).str.lower().isin(["true", "1", "yes"])


def build_candidate_sensitivity_summary(rcss_candidates):
    diagnostics = [
        "validation_mae",
        "posterior_trace",
        "scenario_cvar_trace",
        "condition_number",
        "coverage_penalty",
        "rcss_score",
    ]
    available_diagnostics = [name for name in diagnostics if name in rcss_candidates.columns]
    group_cols = [*condition_group_columns(rcss_candidates), "source"]
    rows = []
    selected_mask = selected_candidate_mask(rcss_candidates)
    for group_key, sub in rcss_candidates.groupby(group_cols, dropna=False):
        if len(group_cols) == 1:
            group_key = (group_key,)
        selected = sub[selected_mask.loc[sub.index]]
        row = {
            **dict(zip(group_cols, group_key)),
            "candidate_row_count": int(sub.shape[0]),
            "selected_count": int(selected.shape[0]),
        }
        for name in available_diagnostics:
            values = pd.to_numeric(sub[name], errors="coerce")
            row[f"{name}_mean"] = values.mean()
            row[f"{name}_std"] = values.std()
            selected_values = pd.to_numeric(selected[name], errors="coerce") if not selected.empty else pd.Series(dtype=float)
            row[f"selected_{name}_mean"] = selected_values.mean()
            row[f"selected_{name}_std"] = selected_values.std()
        rows.append(row)
    return pd.DataFrame(rows).sort_values(group_cols).reset_index(drop=True)


def build_runtime_candidate_sensitivity_summary(frame):
    if frame.empty or "runtime_seconds" not in frame.columns:
        return pd.DataFrame()
    if "candidate_count" not in frame.columns:
        return pd.DataFrame()
    runtime = frame.copy()
    runtime["runtime_seconds"] = pd.to_numeric(runtime["runtime_seconds"], errors="coerce")
    runtime["candidate_count"] = pd.to_numeric(runtime["candidate_count"], errors="coerce")
    runtime = runtime.dropna(subset=["candidate_count", "runtime_seconds"])
    if runtime.empty:
        return pd.DataFrame()
    group_cols = [name for name in condition_group_columns(runtime) if name in runtime.columns]
    optional_cols = ["source", "status"]
    group_cols.extend([name for name in optional_cols if name in runtime.columns])
    out = runtime.groupby(group_cols, dropna=False)["runtime_seconds"].agg(["mean", "std", "min", "max", "count"]).reset_index()
    out = out.rename(columns={"mean": "runtime_seconds"})
    out["candidate_count"] = out["candidate_count"].astype(int)
    return out.sort_values(group_cols).reset_index(drop=True)


def collect_runtime_candidate_frames(input_roots, rcss_candidates):
    frames = []
    for input_root in input_roots:
        timing_paths = [input_root / "stage14_timing.csv", input_root / "stage13_timing.csv"]
        summary_path = input_root / "runtime_candidate_sensitivity.csv"
        timing_frame = next((read_nonempty_csv(path) for path in timing_paths if read_nonempty_csv(path) is not None), None)
        if timing_frame is not None:
            frames.append(timing_frame)
        else:
            summary_frame = read_nonempty_csv(summary_path)
            if summary_frame is not None:
                frames.append(summary_frame)
    for frame in rcss_candidates:
        if {"candidate_count", "runtime_seconds"}.issubset(frame.columns):
            frames.append(frame)
    return frames


def candidate_sensitivity_lines(candidate_summary, runtime_summary):
    lines = [
        "## Candidate-count sensitivity and practical tractability",
        "",
        "Candidate-count sensitivity is summarized as practical tractability and selection stability evidence, not as a broad scalability claim.",
        "",
        "### Candidate source and diagnostic stability",
        "",
        "```",
        candidate_summary.to_string(index=False),
        "```",
        "",
    ]
    if not runtime_summary.empty:
        lines.extend(
            [
                "### Measured runtime / tractability evidence",
                "",
                "```",
                runtime_summary.to_string(index=False),
                "```",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "### Runtime / tractability evidence",
                "",
                "No measured timing artifact was present in these inputs, so EXP-06 runtime closure must come from Stage 13 measured outputs.",
                "",
            ]
        )
    return lines


def candidate_count_from_root(input_root):
    match = re.search(r"(?:^|/)candidates_(\d+)$", str(input_root))
    return int(match.group(1)) if match else None


def add_candidate_count(frame, candidate_count):
    if candidate_count is not None and "candidate_count" not in frame.columns:
        frame = frame.copy()
        frame["candidate_count"] = candidate_count
    return frame


def read_nonempty_csv(path):
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        return pd.read_csv(path)
    except EmptyDataError:
        return None


def collect_seed_dir_frames(seed_dirs):
    metrics = []
    correlations = []
    rcss_candidates = []
    for seed_dir in seed_dirs:
        metrics_path = seed_dir / "metrics.csv"
        metric_frame = read_nonempty_csv(metrics_path)
        if metric_frame is None:
            continue
        candidate_count = candidate_count_from_root(seed_dir.parent)
        try:
            seed = int(seed_dir.name.split("_", 1)[1])
        except (IndexError, ValueError):
            seed = None
        frame = add_candidate_count(metric_frame, candidate_count)
        if seed is not None:
            frame["split_seed"] = seed
        metrics.append(frame)
        corr_path = seed_dir / "certificate_correlations.csv"
        corr_frame = read_nonempty_csv(corr_path)
        if corr_frame is not None:
            corr = add_candidate_count(corr_frame, candidate_count)
            if seed is not None:
                corr["split_seed"] = seed
            correlations.append(corr)
        rcss_path = seed_dir / "rcss_candidates.csv"
        rcss_frame = read_nonempty_csv(rcss_path)
        if rcss_frame is not None:
            rcss = add_candidate_count(rcss_frame, candidate_count)
            if seed is not None:
                rcss["split_seed"] = seed
            rcss_candidates.append(rcss)
    return metrics, correlations, rcss_candidates


def collect_input_frames(input_roots, seed_dirs=None):
    metrics, correlations, rcss_candidates = collect_seed_dir_frames(seed_dirs or [])
    for input_root in input_roots:
        candidate_count = candidate_count_from_root(input_root)
        direct_metrics = read_nonempty_csv(input_root / "metrics.csv")
        if direct_metrics is not None:
            seed_metrics, seed_correlations, seed_rcss = collect_seed_dir_frames([input_root])
            metrics.extend(seed_metrics)
            correlations.extend(seed_correlations)
            rcss_candidates.extend(seed_rcss)
            continue

        metric_paths = sorted(input_root.glob("seed_*/metrics.csv"))
        if metric_paths:
            for path in metric_paths:
                seed = int(path.parent.name.split("_", 1)[1])
                frame = add_candidate_count(pd.read_csv(path), candidate_count)
                frame["split_seed"] = seed
                metrics.append(frame)
                corr_path = path.parent / "certificate_correlations.csv"
                corr_frame = read_nonempty_csv(corr_path)
                if corr_frame is not None:
                    corr = add_candidate_count(corr_frame, candidate_count)
                    corr["split_seed"] = seed
                    correlations.append(corr)
                rcss_path = path.parent / "rcss_candidates.csv"
                rcss_frame = read_nonempty_csv(rcss_path)
                if rcss_frame is not None:
                    rcss = add_candidate_count(rcss_frame, candidate_count)
                    rcss["split_seed"] = seed
                    rcss_candidates.append(rcss)
            continue

        combined_path = input_root / "combined_metrics.csv"
        combined_frame = read_nonempty_csv(combined_path)
        if combined_frame is not None:
            metrics.append(add_candidate_count(combined_frame, candidate_count))
        corr_path = input_root / "combined_certificate_correlations.csv"
        corr_frame = read_nonempty_csv(corr_path)
        if corr_frame is not None:
            correlations.append(add_candidate_count(corr_frame, candidate_count))
        rcss_path = input_root / "combined_rcss_candidates.csv"
        rcss_frame = read_nonempty_csv(rcss_path)
        if rcss_frame is not None:
            rcss_candidates.append(add_candidate_count(rcss_frame, candidate_count))
    return metrics, correlations, rcss_candidates


def main():
    parser = argparse.ArgumentParser(description="Summarize TRACE-SL multi-split RCSS results")
    parser.add_argument("--input-root", required=True, nargs="+")
    parser.add_argument("--seed-dir", nargs="*", default=[])
    parser.add_argument("--runtime-root", nargs="*", default=[])
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    input_roots = [Path(raw) for raw in args.input_root]
    seed_dirs = [Path(raw) for raw in args.seed_dir]
    runtime_roots = [Path(raw) for raw in args.runtime_root]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    metrics, correlations, rcss_candidates = collect_input_frames(input_roots, seed_dirs)
    runtime_candidate_frames = collect_runtime_candidate_frames([*input_roots, *runtime_roots], rcss_candidates)

    if not metrics:
        roots = ", ".join(str(path) for path in input_roots)
        raise SystemExit(f"No seed metrics found under {roots}")

    combined = pd.concat(metrics, ignore_index=True)
    combined.to_csv(output_dir / "combined_metrics.csv", index=False)

    gls = combined[combined["method"] == "gls_map"].copy()
    evidence_group_cols = condition_group_columns(gls)
    layout_summary = build_layout_summary(gls)
    layout_summary.to_csv(output_dir / "gls_map_layout_summary.csv", index=False)

    pivot = gls.pivot_table(index=["split_seed", *evidence_group_cols], columns="layout_type", values="mae", aggfunc="mean")
    comparison_layouts = ["validation_swap_selected", "rcss_selected", "robust_coverage_cvar"]
    baseline_layouts = [
        "random",
        "best_random_by_validation",
        "top_variance",
        "observability_proxy",
        "greedy_a_trace",
        "greedy_d_logdet",
        "graph_sampling_laplacian",
        "qr_pod_modes",
        "scenario_cvar_a_trace",
        "multistart_swap_by_validation",
        "swap_from_scenario_cvar",
    ]
    delta_summary, paired_tests = build_paired_comparisons(pivot, comparison_layouts, baseline_layouts)
    delta_summary.to_csv(output_dir / "gls_map_delta_summary.csv", index=False)
    paired_tests.to_csv(output_dir / "gls_map_paired_delta_tests.csv", index=False)

    ablation_layouts = [
        "best_random_by_validation",
        "top_variance",
        "observability_proxy",
        "greedy_a_trace",
        "greedy_d_logdet",
        "graph_sampling_laplacian",
        "qr_pod_modes",
        "scenario_cvar_a_trace",
        "multistart_swap_by_validation",
        "rcss_selected",
        "validation_swap_selected",
    ]
    ablation_summary = layout_summary[layout_summary["layout_type"].isin(ablation_layouts)].copy()
    ablation_summary.to_csv(output_dir / "gls_map_ablation_summary.csv", index=False)

    winners = []
    for group_key, sub in gls.groupby(["split_seed", *evidence_group_cols]):
        group_key = normalize_group_key(group_key)
        idx = sub["mae"].idxmin()
        winners.append({**dict(zip(["split_seed", *evidence_group_cols], group_key)), "best_layout": gls.loc[idx, "layout_type"], "mae": gls.loc[idx, "mae"]})
    winner_frame = pd.DataFrame(winners)
    winner_frame.to_csv(output_dir / "gls_map_per_split_winners.csv", index=False)
    winner_frame.groupby([*evidence_group_cols, "best_layout"]).size().reset_index(name="wins").to_csv(output_dir / "gls_map_win_counts.csv", index=False)

    if correlations:
        corr = pd.concat(correlations, ignore_index=True)
        corr.to_csv(output_dir / "combined_certificate_correlations.csv", index=False)
        corr_summary = build_certificate_summary(corr)
        flatten_certificate_summary(corr_summary).to_csv(output_dir / "certificate_correlation_summary.csv", index=False)

    if rcss_candidates:
        rcss = pd.concat(rcss_candidates, ignore_index=True)
        rcss.to_csv(output_dir / "combined_rcss_candidates.csv", index=False)
        selected = rcss[selected_candidate_mask(rcss)]
        selected_source_cols = [*condition_group_columns(selected), "source"]
        selected.groupby(selected_source_cols).size().reset_index(name="selected_count").to_csv(output_dir / "rcss_selected_sources.csv", index=False)
        candidate_summary = build_candidate_sensitivity_summary(rcss)
        candidate_summary.to_csv(output_dir / "candidate_sensitivity_summary.csv", index=False)

    runtime_summary = pd.DataFrame()
    if runtime_candidate_frames:
        runtime_inputs = pd.concat(runtime_candidate_frames, ignore_index=True)
        runtime_summary = build_runtime_candidate_sensitivity_summary(runtime_inputs)
        if not runtime_summary.empty:
            runtime_summary.to_csv(output_dir / "runtime_candidate_sensitivity.csv", index=False)

    lines = [
        "---",
        "status: complete",
        "---",
        "",
        "# TRACE-SL RCSS Multi-Split Summary",
        "",
        "## Mean GLS/MAP test MAE across splits",
        "",
        "Robustness and candidate-sensitivity tables are grouped by condition columns when present. These aggregates are stress-test evidence for the evaluated perturbations and split settings, not a universal deployment guarantee.",
        "",
        "```",
        layout_summary.to_string(index=False),
        "```",
        "",
        "## RCSS deltas, negative is better",
        "",
        "```",
        delta_summary.to_string(index=False),
        "```",
        "",
        "## Winner counts",
        "",
        "```",
        winner_frame.groupby([*evidence_group_cols, "best_layout"]).size().reset_index(name="wins").to_string(index=False),
        "```",
        "",
        "## Main ablation layouts",
        "",
        "```",
        ablation_summary.to_string(index=False),
        "```",
        "",
        "## Paired delta tests",
        "",
        "```",
        paired_tests.to_string(index=False),
        "```",
        "",
    ]
    if correlations:
        lines.extend(certificate_summary_lines(corr_summary))
    if rcss_candidates:
        lines.extend(
            [
                "## RCSS selected sources",
                "",
                "```",
                selected.groupby(selected_source_cols).size().reset_index(name="selected_count").to_string(index=False),
                "```",
                "",
            ]
        )
        lines.extend(candidate_sensitivity_lines(candidate_summary, runtime_summary))
    output_files = [
        "combined_metrics.csv",
        "gls_map_layout_summary.csv",
        "gls_map_delta_summary.csv",
        "gls_map_paired_delta_tests.csv",
        "gls_map_ablation_summary.csv",
        "gls_map_per_split_winners.csv",
        "gls_map_win_counts.csv",
    ]
    if correlations:
        output_files.extend(["combined_certificate_correlations.csv", "certificate_correlation_summary.csv"])
    if rcss_candidates:
        output_files.extend(["combined_rcss_candidates.csv", "rcss_selected_sources.csv", "candidate_sensitivity_summary.csv"])
    if not runtime_summary.empty:
        output_files.append("runtime_candidate_sensitivity.csv")
    lines.extend(
        [
            "## Output files",
            "",
            *[f"- {name}" for name in output_files],
        ]
    )
    (output_dir / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
    print(layout_summary.to_string(index=False))
    print(f"Wrote summary to {output_dir}")


if __name__ == "__main__":
    main()
