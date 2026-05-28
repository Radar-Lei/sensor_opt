import argparse
from pathlib import Path

import pandas as pd


CONDITION_COLUMNS = [
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


def group_columns(frame):
    return [name for name in CONDITION_COLUMNS if name in frame.columns]


def build_dominance_rows(layout_summary):
    required = {"layout_type", "mean"}
    missing = required.difference(layout_summary.columns)
    if missing:
        raise ValueError(f"layout summary missing columns: {sorted(missing)}")
    groups = group_columns(layout_summary)
    if "budget" not in groups:
        raise ValueError("layout summary must include budget")
    rows = []
    for group_key, sub in layout_summary.groupby(groups, dropna=False):
        group_key = group_key if isinstance(group_key, tuple) else (group_key,)
        base = dict(zip(groups, group_key))
        trace = sub[sub["layout_type"] == "trace_biopt"]
        if trace.empty:
            raise ValueError(f"missing trace_biopt row for group {base}")
        baselines = sub[sub["layout_type"] != "trace_biopt"].copy()
        if baselines.empty:
            raise ValueError(f"missing baseline rows for group {base}")
        trace_mean = float(pd.to_numeric(trace["mean"], errors="raise").iloc[0])
        baselines["mean"] = pd.to_numeric(baselines["mean"], errors="raise")
        best = baselines.sort_values(["mean", "layout_type"]).iloc[0]
        best_mean = float(best["mean"])
        rows.append(
            {
                **base,
                "trace_biopt_mean": trace_mean,
                "best_baseline_mean": best_mean,
                "best_baseline_layout": best["layout_type"],
                "trace_minus_best_baseline": trace_mean - best_mean,
                "trace_beats_best_baseline": bool(trace_mean < best_mean),
                "baseline_count": int(baselines.shape[0]),
            }
        )
    out = pd.DataFrame(rows)
    return out.sort_values(groups).reset_index(drop=True)


def attach_best_baseline_paired_stats(dominance_rows, paired_tests):
    if paired_tests is None:
        return dominance_rows
    required = {"layout", "baseline", "delta_mean", "win_count", "count"}
    missing = required.difference(paired_tests.columns)
    if missing:
        raise ValueError(f"paired tests missing columns: {sorted(missing)}")
    paired = paired_tests[paired_tests["layout"] == "trace_biopt"].copy()
    if paired.empty:
        raise ValueError("paired tests missing trace_biopt rows")
    join_cols = [name for name in group_columns(dominance_rows) if name in paired.columns]
    paired = paired.rename(columns={"baseline": "best_baseline_layout"})
    paired_cols = [
        "delta_mean",
        "delta_std",
        "delta_sem",
        "ci95_low",
        "ci95_high",
        "cohens_dz",
        "paired_t_p",
        "wilcoxon_p",
        "win_count",
        "count",
    ]
    paired_cols = [name for name in paired_cols if name in paired.columns]
    paired = paired[[*join_cols, "best_baseline_layout", *paired_cols]].rename(
        columns={name: f"paired_{name}" for name in paired_cols}
    )
    merged = dominance_rows.merge(paired, on=[*join_cols, "best_baseline_layout"], how="left")
    if merged["paired_count"].isna().any():
        missing_rows = merged[merged["paired_count"].isna()][[*join_cols, "best_baseline_layout"]]
        raise ValueError(f"missing paired stats for best baseline rows: {missing_rows.to_dict(orient='records')}")
    return merged


def markdown_table(frame):
    columns = [
        name
        for name in [
            "dataset",
            "budget",
            "trace_biopt_mean",
            "best_baseline_mean",
            "best_baseline_layout",
            "trace_minus_best_baseline",
            "trace_beats_best_baseline",
            "paired_count",
            "paired_win_count",
            "paired_paired_t_p",
            "paired_wilcoxon_p",
        ]
        if name in frame.columns
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


def main():
    parser = argparse.ArgumentParser(description="Generate TRACE-BiOpt best-baseline dominance evidence")
    parser.add_argument("--layout-summary", required=True)
    parser.add_argument("--paired-tests", default="")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    layout_summary = pd.read_csv(args.layout_summary)
    rows = build_dominance_rows(layout_summary)
    paired_tests = pd.read_csv(args.paired_tests) if args.paired_tests else None
    rows = attach_best_baseline_paired_stats(rows, paired_tests)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    rows.to_csv(output_dir / "trace_biopt_best_baseline_delta.csv", index=False)
    lines = [
        "# TRACE-BiOpt Best-Baseline Dominance",
        "",
        "Negative `trace_minus_best_baseline` means TRACE-BiOpt has lower held-out GLS/MAP MAE than the best non-BiOpt baseline in that group.",
        "",
        markdown_table(rows),
        "",
    ]
    (output_dir / "TRACE_BIOPT_DOMINANCE.md").write_text("\n".join(lines), encoding="utf-8")
    print(markdown_table(rows))


if __name__ == "__main__":
    main()
