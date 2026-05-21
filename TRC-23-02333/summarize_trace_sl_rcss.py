import argparse
from pathlib import Path

import pandas as pd
from scipy.stats import ttest_rel, wilcoxon


def main():
    parser = argparse.ArgumentParser(description="Summarize TRACE-SL multi-split RCSS results")
    parser.add_argument("--input-root", required=True, nargs="+")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    input_roots = [Path(raw) for raw in args.input_root]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    metrics = []
    correlations = []
    rcss_candidates = []
    for input_root in input_roots:
        for path in sorted(input_root.glob("seed_*/metrics.csv")):
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
        "greedy_a_trace",
        "scenario_cvar_a_trace",
        "multistart_swap_by_validation",
        "swap_from_scenario_cvar",
    ]
    delta_rows = []
    paired_rows = []
    for budget, sub in pivot.groupby(level="budget"):
        sub = sub.droplevel("budget")
        row = {"budget": budget}
        for layout in comparison_layouts:
            if layout in sub.columns:
                for baseline in baseline_layouts:
                    if baseline in sub.columns:
                        delta = sub[layout] - sub[baseline]
                        row[f"{layout}_minus_{baseline}_mean"] = delta.mean()
                        row[f"{layout}_minus_{baseline}_std"] = delta.std()
                        paired_row = {
                            "budget": budget,
                            "layout": layout,
                            "baseline": baseline,
                            "delta_mean": delta.mean(),
                            "delta_std": delta.std(),
                            "win_count": int((delta < 0).sum()),
                            "count": int(delta.notna().sum()),
                        }
                        if delta.notna().sum() >= 2:
                            paired_row["paired_t_p"] = ttest_rel(sub[layout], sub[baseline], nan_policy="omit").pvalue
                            try:
                                paired_row["wilcoxon_p"] = wilcoxon(delta.dropna()).pvalue
                            except ValueError:
                                paired_row["wilcoxon_p"] = pd.NA
                        paired_rows.append(paired_row)
        delta_rows.append(row)
    delta_summary = pd.DataFrame(delta_rows)
    delta_summary.to_csv(output_dir / "gls_map_delta_summary.csv", index=False)
    paired_tests = pd.DataFrame(paired_rows)
    paired_tests.to_csv(output_dir / "gls_map_paired_delta_tests.csv", index=False)

    ablation_layouts = [
        "best_random_by_validation",
        "top_variance",
        "greedy_a_trace",
        "scenario_cvar_a_trace",
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
        corr_summary = corr.groupby(["method", "certificate"])[["pearson_mae", "spearman_mae"]].agg(["mean", "std", "min", "max"])
        corr_summary.to_csv(output_dir / "certificate_correlation_summary.csv")

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
        lines.extend(
            [
                "## Certificate stability",
                "",
                "```",
                corr_summary.to_string(),
                "```",
                "",
            ]
        )
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
