#!/usr/bin/env python3
"""Generate current-best TRACE-BiOpt solver scale diagnostics."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
STAGE16_SWEEP = TRACE_RESULTS / "stage16_calibrated_trace_sweep"
STAGE16_PROBE = TRACE_RESULTS / "stage16_calibrated_trace_probe"
PEMS228_PROBE = TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe"
SUMMARY_CSV = CURRENT_BEST / "trace_biopt_solver_scale_summary.csv"
DETAIL_CSV = CURRENT_BEST / "trace_biopt_solver_scale_detail.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_solver_scale.tex"

RESULT_DIR = {
    "PeMS7_1026": "pems7_1026",
    "PeMS7_228": "pems7_228",
    "Seattle": "seattle",
}
SOURCE_ROOTS = [
    STAGE16_SWEEP,
    STAGE16_PROBE,
    PEMS228_PROBE,
]
SOURCE_LABEL = {
    "stage15_main": "Stage15 main evidence",
}
INIT_LABEL = {
    "forward": "objective_forward",
    "posterior_greedy_warm_start": "posterior_greedy_warm_start",
    "relaxed_warm_start": "relaxed_rounding_warm_start",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def resolve_seed_dir(dataset: str, split_seed: int, evidence_source: str) -> tuple[Path, str]:
    if evidence_source == "stage15_main":
        return STAGE15 / RESULT_DIR[dataset] / f"seed_{split_seed}", "stage15_main"
    if evidence_source.startswith("stage16_replaceable:"):
        root_name = evidence_source.split(":", 1)[1]
        for base in SOURCE_ROOTS:
            candidate = base / root_name / f"seed_{split_seed}"
            if candidate.exists():
                return candidate, root_name
        raise FileNotFoundError(f"unable to resolve source root for {dataset} seed {split_seed}: {evidence_source}")
    raise ValueError(f"unsupported evidence source: {evidence_source}")


def find_history_entry(history_rows: list[dict[str, object]], dataset: str, budget: float) -> dict[str, object]:
    return next(
        row for row in history_rows
        if row["dataset"] == dataset and abs(float(row["budget"]) - budget) < 1e-9
    )


def trace_peak_rss(progress_rows: list[dict[str, object]], budget: float, fallback: float) -> float:
    matches = [
        float(row["max_rss_mb"])
        for row in progress_rows
        if abs(float(row.get("budget", -1.0)) - budget) < 1e-9
        and str(row.get("stage", "")).startswith("trace_biopt_")
        and "max_rss_mb" in row
    ]
    return max(matches) if matches else float(fallback)


def effective_pool(pool_size: int, full_size: int) -> int:
    return full_size if pool_size <= 0 or pool_size >= full_size else pool_size


def first_initializer_stage(history: list[dict[str, object]]) -> str:
    stage = str(history[0]["stage"])
    if stage == "forward":
        return "forward"
    return stage


def detail_rows() -> list[dict[str, object]]:
    current_best_rows = [row for row in load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")]
    rows: list[dict[str, object]] = []
    for row in current_best_rows:
        dataset = row["dataset"]
        budget = float(row["budget"])
        evidence_source = row["evidence_source"]
        for split_seed in range(25, 35):
            seed_dir, source_root = resolve_seed_dir(dataset, split_seed, evidence_source)
            history_entry = find_history_entry(load_json(seed_dir / "trace_biopt_history.json"), dataset, budget)
            config = load_json(seed_dir / "config.json")
            progress_dir = seed_dir.parent / "progress"
            progress_rows = [
                json.loads(line)
                for line in (progress_dir / f"seed_{split_seed}_progress.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            checkpoint = load_json(progress_dir / f"seed_{split_seed}_checkpoint.json")
            n_nodes = int(config["train_shape"][1])
            sensor_count = int(history_entry["sensor_count"])
            outside_count = max(0, n_nodes - sensor_count)
            add_pool = effective_pool(int(config["trace_biopt_exchange_add_pool"]), outside_count)
            remove_pool = effective_pool(int(config["trace_biopt_exchange_remove_pool"]), sensor_count)
            searched_neighbors = add_pool * remove_pool
            full_neighbors = sensor_count * outside_count
            history = history_entry["history"]
            exchange_steps = sum(step["stage"] == "exchange" for step in history)
            stop_step = next((step for step in reversed(history) if step["stage"] == "exchange_stop"), None)
            stop_reason = str(stop_step["stop_reason"]) if stop_step is not None else "exchange_budget_exhausted"
            rows.append(
                {
                    "dataset": dataset,
                    "budget": budget,
                    "split_seed": split_seed,
                    "evidence_source": evidence_source,
                    "source_label": SOURCE_LABEL.get(source_root, "Stage16 calibrated rerun"),
                    "source_root": source_root,
                    "initializer": INIT_LABEL.get(first_initializer_stage(history), first_initializer_stage(history)),
                    "sensor_count": sensor_count,
                    "n_nodes": n_nodes,
                    "exchange_steps": exchange_steps,
                    "searched_one_exchange_coverage_pct": 100.0 * searched_neighbors / full_neighbors if full_neighbors else 0.0,
                    "stop_reason": stop_reason,
                    "peak_trace_rss_mb": trace_peak_rss(progress_rows, budget, float(checkpoint["max_rss_mb"])),
                    "validation_mae": float(history_entry["validation_mae"]),
                    "final_objective": float(history_entry["final_terms"]["objective"]),
                }
            )
    return rows


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, float], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["dataset"]), float(row["budget"]))].append(row)
    out: list[dict[str, object]] = []
    for (dataset, budget), sub in sorted(grouped.items()):
        init_counts = defaultdict(int)
        for row in sub:
            init_counts[str(row["initializer"])] += 1
        dominant_init = sorted(init_counts.items(), key=lambda item: (-item[1], item[0]))[0][0]
        out.append(
            {
                "dataset": dataset,
                "budget": budget,
                "runs": len(sub),
                "source_label": sub[0]["source_label"],
                "dominant_initializer": dominant_init,
                "sensor_count_mean": mean(float(row["sensor_count"]) for row in sub),
                "exchange_steps_mean": mean(float(row["exchange_steps"]) for row in sub),
                "exchange_steps_min": min(int(row["exchange_steps"]) for row in sub),
                "exchange_steps_max": max(int(row["exchange_steps"]) for row in sub),
                "searched_one_exchange_coverage_pct_mean": mean(float(row["searched_one_exchange_coverage_pct"]) for row in sub),
                "peak_trace_rss_mb_mean": mean(float(row["peak_trace_rss_mb"]) for row in sub),
                "peak_trace_rss_mb_min": min(float(row["peak_trace_rss_mb"]) for row in sub),
                "peak_trace_rss_mb_max": max(float(row["peak_trace_rss_mb"]) for row in sub),
                "no_improving_stop_runs": sum(str(row["stop_reason"]) == "no_improving_one_exchange" for row in sub),
                "exchange_budget_exhausted_runs": sum(str(row["stop_reason"]) == "exchange_budget_exhausted" for row in sub),
                "validation_mae_mean": mean(float(row["validation_mae"]) for row in sub),
                "final_objective_mean": mean(float(row["final_objective"]) for row in sub),
            }
        )
    return out


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_tex(rows: list[dict[str, object]]) -> None:
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Current-best TRACE-BiOpt solver scale by dataset-budget row.}",
        "\\label{tab:trace-biopt-solver-scale}",
        "\\tiny",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{lccccccc}",
        "\\toprule",
        "Dataset & Budget & Source & Init. & Exchanges & Search cov. & Peak RSS & Stop cert. \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(str(row['dataset']))} & "
            f"{int(float(row['budget']) * 100)}\\% & "
            f"{tex_escape(str(row['source_label']))} & "
            f"{tex_escape(str(row['dominant_initializer']))} & "
            f"{float(row['exchange_steps_mean']):.1f} [{int(row['exchange_steps_min'])},{int(row['exchange_steps_max'])}] & "
            f"{float(row['searched_one_exchange_coverage_pct_mean']):.1f}\\% & "
            f"{float(row['peak_trace_rss_mb_mean'])/1024.0:.2f} [{float(row['peak_trace_rss_mb_min'])/1024.0:.2f},{float(row['peak_trace_rss_mb_max'])/1024.0:.2f}] GB & "
            f"{int(row['no_improving_stop_runs'])}/{int(row['exchange_budget_exhausted_runs'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "}",
            "\\begin{flushleft}\\footnotesize Source identifies whether the current-best row is still backed by Stage15 main evidence or by a promoted Stage16 calibrated rerun. Init. is the dominant deterministic initializer recorded across the ten split-specific runs. Search cov. is the mean searched one-exchange neighborhood size as a percentage of the full $k(n-k)$ swap set under the declared add/remove pools, with zero-valued pools interpreted as complete enumeration. Peak RSS is the mean, minimum, and maximum peak resident memory observed during TRACE-BiOpt search events for that row. Stop cert. reports runs ending by no improving searched exchange versus runs exhausting the declared exchange-iteration budget.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    detail = detail_rows()
    summary = summarize(detail)
    write_csv(DETAIL_CSV, detail, list(detail[0].keys()))
    write_csv(SUMMARY_CSV, summary, list(summary[0].keys()))
    write_tex(summary)
    print(f"Wrote {OUT_TEX}, {SUMMARY_CSV}, and {DETAIL_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
