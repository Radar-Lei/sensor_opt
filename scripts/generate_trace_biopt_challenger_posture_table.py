#!/usr/bin/env python3
"""Generate a reviewer-facing strongest-vs-hardest challenger posture table."""

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd


CURRENT_BEST = Path("TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence")
BEST_DELTA = CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"
SIGNIFICANCE_SUMMARY = CURRENT_BEST / "trace_biopt_significance_posture_summary.csv"
SIGNIFICANCE_DETAIL = CURRENT_BEST / "trace_biopt_significance_posture_detail.csv"
OUTPUT_CSV = CURRENT_BEST / "trace_biopt_challenger_posture.csv"
OUTPUT_TEX = Path("paper/tables/table_trace_biopt_challenger_posture.tex")


def budget_tex(value: float) -> str:
    return f"{int(round(100.0 * float(value)))}\\%"


def dataset_tex(value: str) -> str:
    return value.replace("_", "\\_")


def tex_escape(value: str) -> str:
    return value.replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")


def format_p(value: float) -> str:
    value = float(value)
    if value < 1e-3:
        return f"{value:.1e}"
    return f"{value:.4f}"


def load_label_lookup() -> dict[tuple[str, float, str], str]:
    lookup: dict[tuple[str, float, str], str] = {}
    with SIGNIFICANCE_DETAIL.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            lookup[(row["dataset"], float(row["budget"]), row["baseline_layout"])] = row["baseline_label"]
    return lookup


def build_frame() -> pd.DataFrame:
    best = pd.read_csv(BEST_DELTA).sort_values(["dataset", "budget"]).reset_index(drop=True)
    summary = pd.read_csv(SIGNIFICANCE_SUMMARY)
    summary = summary[summary["dataset"] != "All rows"].copy()
    summary["budget"] = summary["budget"].astype(float)
    label_lookup = load_label_lookup()

    rows = []
    for _, row in best.iterrows():
        dataset = row["dataset"]
        budget = float(row["budget"])
        strongest_label = label_lookup[(dataset, budget, row["best_baseline_layout"])]
        sig_row = summary[(summary["dataset"] == dataset) & (summary["budget"] == budget)].iloc[0]
        hardest_label = sig_row["closest_challenger_label"]
        same_family = strongest_label == hardest_label
        rows.append(
            {
                "dataset": dataset,
                "budget": budget,
                "budget_pct": int(round(100.0 * budget)),
                "evidence_source": row["evidence_source"],
                "strongest_mean_challenger": strongest_label,
                "strongest_mean_delta": float(row["trace_minus_best_baseline"]),
                "hardest_corrected_challenger": hardest_label,
                "hardest_corrected_delta": float(sig_row["closest_challenger_mean_delta"]),
                "max_holm_p": float(sig_row["max_paired_t_p_holm"]),
                "same_family": "Yes" if same_family else "No",
                "challenger_posture": (
                    "same challenger family drives mean and corrected evidence"
                    if same_family
                    else "mean-strongest and hardest-corrected challengers differ"
                ),
            }
        )
    return pd.DataFrame(rows)


def write_tex(frame: pd.DataFrame) -> None:
    mismatch_count = int((frame["same_family"] == "No").sum())
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Strongest-mean versus hardest-corrected challenger posture. The main dominance table names the best mean-MAE challenger in each row, while the corrected all-baseline screen identifies the challenger with the largest surviving Holm-adjusted paired $p$ value. When the two differ, TRACE-BiOpt is not only ahead of one convenient baseline family; distinct challenger families are closest under mean ranking and corrected paired inference.}",
        "\\label{tab:trace-biopt-challenger-posture}",
        "\\small",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\begin{tabular}{ll>{\\raggedright\\arraybackslash}p{0.21\\textwidth}>{\\raggedright\\arraybackslash}p{0.24\\textwidth}cr}",
        "\\toprule",
        "Dataset & Budget & \\makecell[l]{Strongest mean\\\\challenger} & \\makecell[l]{Hardest corrected\\\\challenger} & Same family? & Max Holm $p$ \\\\",
        "\\midrule",
    ]
    for _, row in frame.iterrows():
        lines.append(
            f"{dataset_tex(row['dataset'])} & {budget_tex(row['budget'])} & "
            f"{tex_escape(row['strongest_mean_challenger'])} & "
            f"{tex_escape(row['hardest_corrected_challenger'])} & "
            f"{row['same_family']} & {format_p(row['max_holm_p'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "\\vspace{0.35em}",
            (
                "\\parbox{0.96\\textwidth}{\\small Across "
                f"{mismatch_count}/9 current-best rows, the strongest mean challenger and the hardest corrected challenger come from different baseline families. "
                "The clearest front-screen mismatches are PeMS7\\_1026 10\\% (Swap from A-trace versus Prev. TRACE-SL) and Seattle 10\\% (RCSS versus Multistart validation-swap).}"
            ),
            "\\end{table*}",
            "",
        ]
    )
    OUTPUT_TEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    frame = build_frame()
    frame.to_csv(OUTPUT_CSV, index=False)
    write_tex(frame)
    print(f"Wrote {OUTPUT_TEX} and {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
