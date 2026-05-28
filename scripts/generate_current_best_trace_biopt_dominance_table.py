#!/usr/bin/env python3
"""Generate the paper current-best TRACE-BiOpt dominance table from CSV evidence."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


DEFAULT_INPUT = Path("TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_best_baseline_delta.csv")
DEFAULT_OUTPUT = Path("paper/tables/table_trace_biopt_dominance.tex")
SIGNIFICANCE_DETAIL = Path("TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_significance_posture_detail.csv")


def format_budget(value: float) -> str:
    return f"{int(round(100.0 * float(value)))}\\%"


def format_p(value: float) -> str:
    value = float(value)
    if value < 1e-3:
        return f"{value:.1e}"
    return f"{value:.4f}"


def dataset_tex(value: str) -> str:
    return value.replace("_", "\\_")


def tex_escape(value: str) -> str:
    return value.replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")


def promoted_note_rows(frame: pd.DataFrame) -> str:
    promoted = frame[frame["evidence_source"].astype(str).str.startswith("stage16_replaceable:")]
    if promoted.empty:
        return ""
    labels = [
        f"{row['dataset'].replace('_', '\\_')} {int(round(float(row['budget']) * 100))}\\%"
        for _, row in promoted.sort_values(["dataset", "budget"]).iterrows()
    ]
    if len(labels) == 1:
        return f" The {labels[0]} row is promoted from a complete replaceable Stage16 calibrated rerun."
    joined = ", ".join(labels[:-1]) + f", and {labels[-1]}" if len(labels) > 2 else " and ".join(labels)
    return f" The {joined} rows are promoted from complete replaceable Stage16 calibrated reruns."


def directional_note_rows(frame: pd.DataFrame) -> str:
    directional = frame[
        (frame["paired_win_count"].astype(int) < frame["paired_count"].astype(int))
        | (frame["paired_paired_t_p"].astype(float) >= 0.05)
    ]
    if directional.empty:
        return ""
    labels = [
        f"{row['dataset'].replace('_', '\\_')} {int(round(float(row['budget']) * 100))}\\%"
        for _, row in directional.sort_values(["dataset", "budget"]).iterrows()
    ]
    if len(labels) == 1:
        return f" The {labels[0]} row is treated as directional mean dominance, not final significance evidence."
    joined = ", ".join(labels[:-1]) + f", and {labels[-1]}" if len(labels) > 2 else " and ".join(labels)
    return f" The {joined} rows are treated as directional mean dominance, not final significance evidence."


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dominance-csv", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-tex", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    frame = pd.read_csv(args.dominance_csv).sort_values(["dataset", "budget"]).reset_index(drop=True)
    detail = pd.read_csv(SIGNIFICANCE_DETAIL)
    label_lookup = {}
    for _, row in detail.iterrows():
        key = (row["dataset"], float(row["budget"]), row["baseline_layout"])
        label_lookup.setdefault(key, row["baseline_label"])
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Current best ten-seed strongest-challenger dominance table. Lower MAE is better. Replaceable Stage16 calibrated rows are promoted into the main evidence path; rows without complete Stage16 reruns retain the Stage15 ten-seed evidence. The strongest challenger is the best mean-MAE baseline selected from the pre-registered non-BiOpt baseline set within each dataset-budget row. Paired tests compare TRACE-BiOpt with that row's strongest challenger on the same ten split seeds.}",
        "\\label{tab:trace-biopt-dominance}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\begin{tabular}{llp{0.19\\textwidth}rrrrr}",
        "\\toprule",
        "Dataset & Budget & Strongest challenger & TRACE-BiOpt & Challenger MAE & Delta & Wins & Paired $p$ \\\\",
        "\\midrule",
    ]
    for _, row in frame.iterrows():
        challenger_label = label_lookup[(row["dataset"], float(row["budget"]), row["best_baseline_layout"])]
        lines.append(
            f"{dataset_tex(row['dataset'])} & {format_budget(row['budget'])} & "
            f"{tex_escape(challenger_label)} & "
            f"{float(row['trace_biopt_mean']):.4f} & {float(row['best_baseline_mean']):.4f} & "
            f"{float(row['trace_minus_best_baseline']):.4f} & "
            f"{int(row['paired_win_count'])}/{int(row['paired_count'])} & {format_p(float(row['paired_paired_t_p']))} \\\\"
        )
    note = (
        "\\parbox{0.96\\textwidth}{\\small The strongest challengers are "
        "Swap from A-trace on PeMS7\\_1026 10\\%, RCSS on Seattle 10\\%, and "
        "the previous TRACE-SL validation-swap route on the remaining rows."
        f"{promoted_note_rows(frame)}{directional_note_rows(frame)}"
        "}"
    )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\vspace{0.35em}", note, "\\end{table*}", ""])
    args.output_tex.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output_tex}")


if __name__ == "__main__":
    main()
