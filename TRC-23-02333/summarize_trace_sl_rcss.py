import argparse
from pathlib import Path

import pandas as pd
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


def build_paired_comparisons(pivot, comparison_layouts, baseline_layouts):
    delta_rows = []
    paired_rows = []
    for budget, sub in pivot.groupby(level="budget"):
        sub = sub.droplevel("budget")
        row = {"budget": budget}
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
                        "budget": budget,
                        "layout": layout,
                        "baseline": baseline,
                        **stats_row,
                    }
                )
        delta_rows.append(row)
    return pd.DataFrame(delta_rows), pd.DataFrame(paired_rows)


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


def collect_input_frames(input_roots):
    metrics = []
    correlations = []
    rcss_candidates = []
    for input_root in input_roots:
        metric_paths = sorted(input_root.glob("seed_*/metrics.csv"))
        if metric_paths:
            for path in metric_paths:
                seed = int(path.parent.name.split("_", 1)[1])
                frame = pd.read_csv(path)
                frame["split_seed"] = seed
                metrics.append(frame)
                corr_path = path.parent / "certificate_correlations.csv"
                if corr_path.exists():
                    corr = pd.read_csv(corr_path)
                    corr["split_seed"] = seed
                    correlations.append(corr)
                rcss_path = path.parent / "rcss_candidates.csv"
                if rcss_path.exists():
                    rcss = pd.read_csv(rcss_path)
                    rcss["split_seed"] = seed
                    rcss_candidates.append(rcss)
            continue

        combined_path = input_root / "combined_metrics.csv"
        if combined_path.exists():
            metrics.append(pd.read_csv(combined_path))
        corr_path = input_root / "combined_certificate_correlations.csv"
        if corr_path.exists():
            correlations.append(pd.read_csv(corr_path))
        rcss_path = input_root / "combined_rcss_candidates.csv"
        if rcss_path.exists():
            rcss_candidates.append(pd.read_csv(rcss_path))
    return metrics, correlations, rcss_candidates


def main():
    parser = argparse.ArgumentParser(description="Summarize TRACE-SL multi-split RCSS results")
    parser.add_argument("--input-root", required=True, nargs="+")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    input_roots = [Path(raw) for raw in args.input_root]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    metrics, correlations, rcss_candidates = collect_input_frames(input_roots)

    if not metrics:
        roots = ", ".join(str(path) for path in input_roots)
        raise SystemExit(f"No seed metrics found under {roots}")

    combined = pd.concat(metrics, ignore_index=True)
    combined.to_csv(output_dir / "combined_metrics.csv", index=False)

    gls = combined[combined["method"] == "gls_map"].copy()
    layout_summary = (
        gls.groupby(["budget", "layout_type"])["mae"]
        .agg(["mean", "std", "count"])
        .reset_index()
        .sort_values(["budget", "mean"])
    )
    layout_summary.to_csv(output_dir / "gls_map_layout_summary.csv", index=False)

    pivot = gls.pivot_table(index=["split_seed", "budget"], columns="layout_type", values="mae", aggfunc="mean")
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
    for (split_seed, budget), sub in gls.groupby(["split_seed", "budget"]):
        idx = sub["mae"].idxmin()
        winners.append({"split_seed": split_seed, "budget": budget, "best_layout": gls.loc[idx, "layout_type"], "mae": gls.loc[idx, "mae"]})
    winner_frame = pd.DataFrame(winners)
    winner_frame.to_csv(output_dir / "gls_map_per_split_winners.csv", index=False)
    winner_frame.groupby(["budget", "best_layout"]).size().reset_index(name="wins").to_csv(output_dir / "gls_map_win_counts.csv", index=False)

    if correlations:
        corr = pd.concat(correlations, ignore_index=True)
        corr.to_csv(output_dir / "combined_certificate_correlations.csv", index=False)
        corr_summary = build_certificate_summary(corr)
        flatten_certificate_summary(corr_summary).to_csv(output_dir / "certificate_correlation_summary.csv", index=False)

    if rcss_candidates:
        rcss = pd.concat(rcss_candidates, ignore_index=True)
        rcss.to_csv(output_dir / "combined_rcss_candidates.csv", index=False)
        selected = rcss[rcss["selected"] == True]
        selected.groupby(["budget", "source"]).size().reset_index(name="selected_count").to_csv(output_dir / "rcss_selected_sources.csv", index=False)

    lines = [
        "---",
        "status: complete",
        "---",
        "",
        "# TRACE-SL RCSS Multi-Split Summary",
        "",
        "## Mean GLS/MAP test MAE across splits",
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
        winner_frame.groupby(["budget", "best_layout"]).size().reset_index(name="wins").to_string(index=False),
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
                selected.groupby(["budget", "source"]).size().reset_index(name="selected_count").to_string(index=False),
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## Output files",
            "",
            "- combined_metrics.csv",
            "- gls_map_layout_summary.csv",
            "- gls_map_delta_summary.csv",
            "- gls_map_paired_delta_tests.csv",
            "- gls_map_ablation_summary.csv",
            "- gls_map_per_split_winners.csv",
            "- gls_map_win_counts.csv",
            "- combined_rcss_candidates.csv",
            "- rcss_selected_sources.csv",
        ]
    )
    (output_dir / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
    print(layout_summary.to_string(index=False))
    print(f"Wrote summary to {output_dir}")


if __name__ == "__main__":
    main()
