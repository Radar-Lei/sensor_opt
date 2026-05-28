#!/usr/bin/env python3
"""Generate a reviewer-facing Stage14 stress frontier table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
SOURCE = PAPER_SOURCES / "robustness_condition_table.csv"
OUT_CSV = PAPER_SOURCES / "robustness_frontier_summary.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_robustness_frontier.tex"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def condition_label(row: dict[str, str]) -> str:
    family = row["robustness_family"]
    if family == "baseline":
        return "baseline"
    if family == "sensor_failure":
        return f"sensor failure {float(row['failure_rate']):.0%}"
    if family == "observation_noise":
        return f"observation noise {float(row['noise_scale']):.0%}"
    if family == "random_missing":
        return f"random missing {float(row['missing_rate']):.0%}"
    if family == "block_missing":
        return f"block missing {int(float(row['missing_block_steps']))} steps"
    if family == "cost_proxy":
        return f"cost proxy budget {float(row['cost_budget']):.0f}"
    if family == "temporal_shift":
        return "chronological split"
    return row["robustness_condition"]


def layout_family(layout_type: str) -> str:
    if layout_type == "graph_sampling_laplacian":
        return "graph-spectral"
    if layout_type == "qr_pod_modes":
        return "POD/QR"
    if layout_type == "greedy_d_logdet":
        return "logdet"
    if layout_type in {"multistart_swap_by_validation", "swap_from_best_random_trace", "validation_swap_selected"}:
        return "swap"
    if layout_type in {"observability_proxy"}:
        return "observability"
    if layout_type in {"robust_coverage_cvar", "coverage"}:
        return "coverage"
    if layout_type in {"top_variance"}:
        return "variance"
    return "trace/certificate heuristic"


def display_layout(layout_type: str) -> str:
    mapping = {
        "graph_sampling_laplacian": "graph_sampling",
        "qr_pod_modes": "qr_pod",
        "greedy_d_logdet": "greedy_d_logdet",
        "multistart_swap_by_validation": "multistart_swap",
        "observability_proxy": "observability_proxy",
        "validation_swap_selected": "validation_swap",
    }
    return mapping.get(layout_type, layout_type)


def build_rows() -> list[dict[str, str]]:
    rows = load_csv(SOURCE)
    groups: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in rows:
        key = (row["robustness_family"], row["robustness_condition"])
        groups.setdefault(key, []).append(row)

    summary: list[dict[str, str]] = []
    for (_family, _condition), group in sorted(groups.items()):
        ordered = sorted(group, key=lambda row: (float(row["mean"]), row["layout_type"]))
        best = ordered[0]
        runner = ordered[1]
        summary.append(
            {
                "condition": condition_label(best),
                "winner_layout": display_layout(best["layout_type"]),
                "winner_family": layout_family(best["layout_type"]),
                "winner_mae": f"{float(best['mean']):.4f}",
                "runner_up_layout": display_layout(runner["layout_type"]),
                "runner_up_mae": f"{float(runner['mean']):.4f}",
                "gap_to_runner_up": f"{float(runner['mean']) - float(best['mean']):.4f}",
                "claim_route": "stress-test only",
            }
        )
    return summary


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_tex(rows: list[dict[str, str]]) -> None:
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Stage14 PeMS7\\_228 stress frontier over perturbation, cost, and temporal-shift slices. Lower MAE is better.}",
        "\\label{tab:trace-biopt-robustness-frontier}",
        "\\tiny",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}p{0.12\\textwidth}>{\\centering\\arraybackslash}p{0.09\\textwidth}>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\centering\\arraybackslash}p{0.08\\textwidth}}",
        "\\toprule",
        "Condition & Winner & Family & Best & Runner-up & Gap \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['condition'])} & "
            f"{tex_escape(row['winner_layout'])} & "
            f"{tex_escape(row['winner_family'])} & "
            f"{row['winner_mae']} & "
            f"{tex_escape(row['runner_up_layout'])} & "
            f"{row['gap_to_runner_up']} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "\\begin{flushleft}\\footnotesize These rows remain bounded Stage14 stress-test evidence only. They do not assert TRACE-BiOpt robustness under the same perturbations because the Stage14 artifact evaluates pre-TRACE-BiOpt reviewer-facing baselines on two split seeds; the table is used to summarize how the stress frontier moves across perturbation types.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = build_rows()
    write_csv(OUT_CSV, rows)
    write_tex(rows)
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
