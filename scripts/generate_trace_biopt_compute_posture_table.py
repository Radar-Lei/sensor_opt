#!/usr/bin/env python3
"""Generate current-best TRACE-BiOpt compute-posture evidence."""

from __future__ import annotations

import csv
import json
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
STAGE16_SWEEP = TRACE_RESULTS / "stage16_calibrated_trace_sweep"
STAGE16_PROBE = TRACE_RESULTS / "stage16_calibrated_trace_probe"
PEMS228_PROBE = TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe"

DETAIL_CSV = CURRENT_BEST / "trace_biopt_compute_posture_detail.csv"
SUMMARY_CSV = CURRENT_BEST / "trace_biopt_compute_posture.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_compute_posture.tex"

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


def parse_stat_timestamp(raw: str) -> float | None:
    raw = raw.strip()
    if raw == "-":
        return None
    main, offset = raw.rsplit(" ", 1)
    if "." in main:
        prefix, frac = main.split(".", 1)
        frac = frac[:6].ljust(6, "0")
    else:
        prefix = main
        frac = "000000"
    normalized = f"{prefix}.{frac} {offset}"
    return datetime.strptime(normalized, "%Y-%m-%d %H:%M:%S.%f %z").timestamp()


def stat_epochs(path: Path) -> tuple[float, float]:
    birth_raw, mtime_raw = subprocess.check_output(
        ["stat", "-c", "%w|%y", str(path)],
        text=True,
    ).strip().split("|", 1)
    birth = parse_stat_timestamp(birth_raw)
    mtime = parse_stat_timestamp(mtime_raw)
    if mtime is None:
        raise ValueError(f"mtime unavailable for {path}")
    if birth is None:
        birth = mtime
    return birth, mtime


def resolve_seed_paths(dataset: str, evidence_source: str, split_seed: int) -> tuple[Path, Path, Path, str]:
    if evidence_source == "stage15_main":
        base = STAGE15 / RESULT_DIR[dataset]
        return (
            base / f"seed_{split_seed}",
            base / "progress" / f"seed_{split_seed}_progress.jsonl",
            base / "progress" / f"seed_{split_seed}_checkpoint.json",
            "stage15_main",
        )
    if evidence_source.startswith("stage16_replaceable:"):
        root_name = evidence_source.split(":", 1)[1]
        for base in SOURCE_ROOTS:
            seed_dir = base / root_name / f"seed_{split_seed}"
            progress_path = base / root_name / "progress" / f"seed_{split_seed}_progress.jsonl"
            checkpoint_path = base / root_name / "progress" / f"seed_{split_seed}_checkpoint.json"
            if seed_dir.exists() and progress_path.exists() and checkpoint_path.exists():
                return seed_dir, progress_path, checkpoint_path, root_name
        raise FileNotFoundError(f"unable to resolve current-best source for {dataset} seed {split_seed}: {evidence_source}")
    raise ValueError(f"unsupported evidence source: {evidence_source}")


def count_exchange_steps(seed_dir: Path) -> int:
    history_rows = load_json(seed_dir / "trace_biopt_history.json")
    return sum(
        sum(1 for step in entry["history"] if step["stage"] == "exchange")
        for entry in history_rows
    )


def route_label(dataset: str, evidence_source: str, covered_rows: list[int]) -> str:
    budget_text = "/".join(str(budget) for budget in covered_rows)
    if evidence_source == "stage15_main":
        return f"{dataset} Stage15 main route ({budget_text}%)"
    return f"{dataset} calibrated rerun ({budget_text}%)"


def source_scope(evidence_source: str, run_budget_count: int) -> str:
    if evidence_source == "stage15_main":
        return "all-budget main-evidence run"
    if run_budget_count == 1:
        return "single-budget calibrated rerun"
    if run_budget_count == 2:
        return "paired-budget calibrated rerun"
    return "multi-budget calibrated rerun"


def detail_rows() -> list[dict[str, object]]:
    current_best_rows = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    route_to_budgets: dict[tuple[str, str], list[int]] = defaultdict(list)
    for row in current_best_rows:
        route_to_budgets[(row["dataset"], row["evidence_source"])].append(int(round(float(row["budget"]) * 100)))

    out: list[dict[str, object]] = []
    for (dataset, evidence_source), covered_budgets in sorted(route_to_budgets.items()):
        covered_budgets = sorted(set(covered_budgets))
        for split_seed in range(25, 35):
            seed_dir, progress_path, checkpoint_path, source_root = resolve_seed_paths(dataset, evidence_source, split_seed)
            checkpoint = load_json(checkpoint_path)
            progress_birth, _ = stat_epochs(progress_path)
            checkpoint_birth, checkpoint_mtime = stat_epochs(checkpoint_path)
            end_time = checkpoint_birth if checkpoint_birth >= progress_birth else checkpoint_mtime
            metrics_rows = load_json(seed_dir / "metrics.json")
            run_budget_count = len({float(row["budget"]) for row in metrics_rows})
            out.append(
                {
                    "dataset": dataset,
                    "evidence_source": evidence_source,
                    "source_root": source_root,
                    "route_label": route_label(dataset, evidence_source, covered_budgets),
                    "covered_current_best_rows": "/".join(str(budget) for budget in covered_budgets) + "%",
                    "run_budget_count": run_budget_count,
                    "source_scope": source_scope(evidence_source, run_budget_count),
                    "split_seed": split_seed,
                    "wall_clock_minutes": (end_time - progress_birth) / 60.0,
                    "peak_rss_mb": float(checkpoint["max_rss_mb"]),
                    "exchange_steps": count_exchange_steps(seed_dir),
                }
            )
    return out


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["route_label"])].append(row)

    preferred_labels = [
        "PeMS7_1026 calibrated rerun (10/20%)",
        "PeMS7_1026 calibrated rerun (30%)",
        "PeMS7_228 calibrated rerun (10%)",
        "PeMS7_228 calibrated rerun (20/30%)",
        "Seattle Stage15 main route (10/20/30%)",
    ]
    ordered_labels = [label for label in preferred_labels if label in grouped]
    ordered_labels.extend(sorted(label for label in grouped if label not in ordered_labels))
    out: list[dict[str, object]] = []
    for label in ordered_labels:
        sub = grouped[label]
        out.append(
            {
                "route_label": label,
                "dataset": sub[0]["dataset"],
                "covered_current_best_rows": sub[0]["covered_current_best_rows"],
                "source_scope": sub[0]["source_scope"],
                "run_budget_count": sub[0]["run_budget_count"],
                "runs": len(sub),
                "wall_clock_minutes_mean": mean(float(row["wall_clock_minutes"]) for row in sub),
                "wall_clock_minutes_min": min(float(row["wall_clock_minutes"]) for row in sub),
                "wall_clock_minutes_max": max(float(row["wall_clock_minutes"]) for row in sub),
                "peak_rss_gb_mean": mean(float(row["peak_rss_mb"]) for row in sub) / 1024.0,
                "peak_rss_gb_min": min(float(row["peak_rss_mb"]) for row in sub) / 1024.0,
                "peak_rss_gb_max": max(float(row["peak_rss_mb"]) for row in sub) / 1024.0,
                "exchange_steps_mean": mean(float(row["exchange_steps"]) for row in sub),
                "exchange_steps_min": min(int(row["exchange_steps"]) for row in sub),
                "exchange_steps_max": max(int(row["exchange_steps"]) for row in sub),
            }
        )
    return out


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_tex(rows: list[dict[str, object]]) -> None:
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Current-best TRACE-BiOpt compute posture by source route.}",
        "\\label{tab:trace-biopt-compute-posture}",
        "\\tiny",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.25\\textwidth}>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\centering\\arraybackslash}p{0.07\\textwidth}>{\\centering\\arraybackslash}p{0.14\\textwidth}>{\\centering\\arraybackslash}p{0.14\\textwidth}>{\\centering\\arraybackslash}p{0.12\\textwidth}}",
        "\\toprule",
        "Route & Scope & Budgets/run & Wall-clock & Peak RSS & Exchanges \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(str(row['route_label']))} & "
            f"{tex_escape(str(row['source_scope']))} & "
            f"{int(row['run_budget_count'])} & "
            f"{float(row['wall_clock_minutes_mean']):.1f} (max {float(row['wall_clock_minutes_max']):.1f}) min & "
            f"{float(row['peak_rss_gb_mean']):.2f} (max {float(row['peak_rss_gb_max']):.2f}) GB & "
            f"{float(row['exchange_steps_mean']):.1f} [{int(row['exchange_steps_min'])},{int(row['exchange_steps_max'])}] \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "}",
            "\\begin{flushleft}\\footnotesize Covered rows are the current-best rows that inherit the route. Budgets/run counts all budgets executed inside that deterministic source route, which can exceed the current-best rows adopted from it. Wall-clock is computed from the progress-file creation time to the checkpoint-file creation time for each split-specific run; the table reports the mean with the maximum split-specific run in parentheses, while the CSV companion retains the full range. Peak RSS uses the route-level checkpoint record rather than the budget-sliced trace peak already reported in Table~\\ref{tab:trace-biopt-solver-scale}. Exchanges sum accepted one-exchange moves over all budgets executed inside the route.\\end{flushleft}",
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
