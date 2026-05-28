#!/usr/bin/env python3
"""Generate a reviewer-facing current-best initializer posture table."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"

SOLVER_SCALE_CSV = CURRENT_BEST / "trace_biopt_solver_scale_summary.csv"
COMPUTE_POSTURE_CSV = CURRENT_BEST / "trace_biopt_compute_posture.csv"
OBJECTIVE_DESCENT_CSV = CURRENT_BEST / "trace_biopt_objective_descent_summary.csv"

OUT_CSV = CURRENT_BEST / "trace_biopt_initializer_posture.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_initializer_posture.tex"

DATASET_ORDER = ["PeMS7_1026", "PeMS7_228", "Seattle"]
INIT_DISPLAY = {
    "posterior_greedy_warm_start": "posterior warm-start",
    "objective_forward": "objective-forward",
}
MODE_DISPLAY = {
    "exchange_only_warm_start": "exchange-only warm start",
    "forward_then_exchange": "forward then exchange",
}


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


def main() -> int:
    solver_rows = load_csv(SOLVER_SCALE_CSV)
    compute_rows = load_csv(COMPUTE_POSTURE_CSV)
    descent_rows = load_csv(OBJECTIVE_DESCENT_CSV)

    grouped_solver: dict[str, list[dict[str, str]]] = {dataset: [] for dataset in DATASET_ORDER}
    grouped_descent: dict[str, list[dict[str, str]]] = {dataset: [] for dataset in DATASET_ORDER}
    grouped_compute: dict[str, list[dict[str, str]]] = {dataset: [] for dataset in DATASET_ORDER}
    for row in solver_rows:
        grouped_solver[row["dataset"]].append(row)
    for row in descent_rows:
        grouped_descent[row["dataset"]].append(row)
    for row in compute_rows:
        grouped_compute[row["dataset"]].append(row)

    out_rows: list[dict[str, str]] = []
    for dataset in DATASET_ORDER:
        solver_sub = grouped_solver[dataset]
        descent_sub = grouped_descent[dataset]
        compute_sub = grouped_compute[dataset]

        budgets = "/".join(str(int(float(row["budget"]) * 100)) for row in solver_sub)
        source_labels = sorted({row["source_label"] for row in solver_sub})
        init_labels = sorted({row["dominant_initializer"] for row in solver_sub})
        stage_modes = sorted({row["dominant_stage_mode"] for row in descent_sub})

        min_cov = min(float(row["searched_one_exchange_coverage_pct_mean"]) for row in solver_sub)
        max_cov = max(float(row["searched_one_exchange_coverage_pct_mean"]) for row in solver_sub)
        min_exchange = min(float(row["exchange_steps_mean"]) for row in solver_sub)
        max_exchange = max(float(row["exchange_steps_mean"]) for row in solver_sub)
        min_rss = min(float(row["peak_trace_rss_mb_mean"]) / 1024.0 for row in solver_sub)
        max_rss = max(float(row["peak_trace_rss_mb_mean"]) / 1024.0 for row in solver_sub)
        min_forward = min(float(row["mean_forward_like_steps"]) for row in descent_sub)
        max_forward = max(float(row["mean_forward_like_steps"]) for row in descent_sub)
        max_exchange_share = max(float(row["mean_exchange_share_pct"]) for row in descent_sub)
        min_route_minutes = min(float(row["wall_clock_minutes_mean"]) for row in compute_sub)
        max_route_minutes = max(float(row["wall_clock_minutes_mean"]) for row in compute_sub)
        route_scopes = sorted({row["source_scope"] for row in compute_sub})

        if dataset == "PeMS7_1026":
            reading = (
                "Large-network calibrated rows rely on a posterior warm start, then spend the "
                "solver budget almost entirely in exchange-only cleanup under very small searched neighborhoods."
            )
        elif dataset == "PeMS7_228":
            reading = (
                "Mid-scale calibrated rows stay in direct objective-forward construction, then "
                "enumerate the complete one-exchange neighborhood, so calibration changes the route without changing the solver family."
            )
        else:
            reading = (
                "Seattle now splits between one retained low-budget Stage15 row and promoted "
                "20/30% calibrated reruns, but it still sits in the light direct-construction regime: "
                "objective-forward dominates and exchange tails stay short even after calibration."
            )

        out_rows.append(
            {
                "dataset": dataset,
                "covered_rows_pct": budgets + "%",
                "source_mix": ", ".join(source_labels),
                "initializer_family": ", ".join(init_labels),
                "stage_mode": ", ".join(stage_modes),
                "searched_coverage_pct_range": f"{min_cov:.1f}-{max_cov:.1f}",
                "exchange_steps_range": f"{min_exchange:.1f}-{max_exchange:.1f}",
                "forward_like_steps_range": f"{min_forward:.1f}-{max_forward:.1f}",
                "exchange_share_pct_max": f"{max_exchange_share:.3f}",
                "peak_rss_gb_range": f"{min_rss:.2f}-{max_rss:.2f}",
                "route_wall_clock_minutes_range": f"{min_route_minutes:.3f}-{max_route_minutes:.3f}",
                "route_scope": ", ".join(route_scopes),
                "solver_reading": reading,
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing current-best TRACE-BiOpt initializer posture. The table compresses the nine row-level solver traces into three regime-level readings so the deterministic algorithm is visible as a size-adaptive solver family rather than as one opaque search trace.}",
        "\\label{tab:trace-biopt-initializer-posture}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.11\\textwidth}>{\\raggedright\\arraybackslash}p{0.10\\textwidth}>{\\raggedright\\arraybackslash}p{0.15\\textwidth}>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}p{0.12\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Dataset regime & Covered rows & Source mix & Initializer / stage mode & Search / compute posture & Solver reading \\\\",
        "\\midrule",
    ]
    for row in out_rows:
        posture = (
            f"cov. {row['searched_coverage_pct_range']}%; "
            f"ex. {row['exchange_steps_range']}; "
            f"fwd. {row['forward_like_steps_range']}; "
            f"RSS {row['peak_rss_gb_range']} GB; "
            f"route {row['route_wall_clock_minutes_range']} min"
        )
        lines.append(
            f"{tex_escape(row['dataset'])} & "
            f"{tex_escape(row['covered_rows_pct'])} & "
            f"{tex_escape(row['source_mix'])} & "
            f"{tex_escape(INIT_DISPLAY.get(row['initializer_family'], row['initializer_family']))} / "
            f"{tex_escape(MODE_DISPLAY.get(row['stage_mode'], row['stage_mode']))} & "
            f"{tex_escape(posture)} & "
            f"{tex_escape(row['solver_reading'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabularx}",
            "\\begin{flushleft}\\footnotesize Search / compute posture summarizes the row-level solver-scale, compute-posture, and objective-descent artifacts already used elsewhere in the current-best chain. Coverage is the searched one-exchange neighborhood as a percentage of the full $k(n-k)$ swap set. Exchange and forward counts are accepted-step means aggregated over the covered current-best rows for that network. The table is intended to expose solver regime, not to add a new dominance claim.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
