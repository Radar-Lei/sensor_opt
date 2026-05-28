#!/usr/bin/env python3
"""Generate TRACE-BiOpt optimization diagnostics from Stage15 histories."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
STAGE15 = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2"
COMBINED = STAGE15 / "combined"
DETAIL_CSV = COMBINED / "trace_biopt_optimization_diagnostics_detail.csv"
SUMMARY_CSV = COMBINED / "trace_biopt_optimization_diagnostics.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_optimization.tex"


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def seed_from_path(path: Path) -> int:
    return int(path.parent.name.removeprefix("seed_"))


def pct_drop(start: float, end: float) -> float:
    return 100.0 * (start - end) / start if start else 0.0


def load_config(path: Path) -> dict[str, object]:
    return json.loads((path.parent / "config.json").read_text(encoding="utf-8"))


def stop_reason(history: list[dict[str, object]], exchange_iter_cap: int) -> str:
    for step in reversed(history):
        if step["stage"] == "exchange_stop":
            return str(step.get("stop_reason", "unknown"))
    exchange_steps = sum(step["stage"] == "exchange" for step in history)
    if exchange_iter_cap > 0 and exchange_steps >= exchange_iter_cap:
        return "exchange_budget_exhausted"
    return "unknown"


def history_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in sorted(STAGE15.glob("*/seed_*/trace_biopt_history.json")):
        dataset_dir = path.parents[1].name
        if dataset_dir == "combined":
            continue
        seed = seed_from_path(path)
        config = load_config(path)
        n_nodes = int(config["train_shape"][1])
        exchange_add_pool = min(int(config["trace_biopt_exchange_add_pool"]), n_nodes)
        entries = json.loads(path.read_text(encoding="utf-8"))
        for entry in entries:
            hist = entry["history"]
            objectives = [float(step["objective"]) for step in hist]
            forward = [step for step in hist if step["stage"] == "forward"]
            construction = [step for step in hist if step["stage"] != "exchange"]
            exchange = [step for step in hist if step["stage"] == "exchange"]
            sensor_count = int(entry["sensor_count"])
            outside_count = n_nodes - sensor_count
            exchange_remove_pool = min(int(config["trace_biopt_exchange_remove_pool"]), sensor_count)
            searched_neighbors = exchange_remove_pool * min(exchange_add_pool, outside_count)
            full_neighbors = sensor_count * outside_count
            reason = stop_reason(hist, int(config["trace_biopt_exchange_iter"]))
            first_objective = objectives[0]
            exchange_start_objective = float(construction[-1]["objective"]) if construction else first_objective
            final_objective = float(entry["final_terms"]["objective"])
            rows.append(
                {
                    "dataset": entry["dataset"],
                    "dataset_dir": dataset_dir,
                    "seed": seed,
                    "budget": float(entry["budget"]),
                    "sensor_count": sensor_count,
                    "n_nodes": n_nodes,
                    "forward_steps": len(forward),
                    "construction_steps": len(construction),
                    "exchange_steps": len(exchange),
                    "exchange_iter_cap": int(config["trace_biopt_exchange_iter"]),
                    "exchange_add_pool": exchange_add_pool,
                    "exchange_remove_pool": exchange_remove_pool,
                    "searched_one_exchange_neighbors": searched_neighbors,
                    "full_one_exchange_neighbors": full_neighbors,
                    "searched_one_exchange_coverage_pct": 100.0 * searched_neighbors / full_neighbors if full_neighbors else 0.0,
                    "stop_reason": reason,
                    "no_improving_stop": reason == "no_improving_one_exchange",
                    "exchange_budget_exhausted": reason == "exchange_budget_exhausted",
                    "first_objective": first_objective,
                    "exchange_start_objective": exchange_start_objective,
                    "final_objective": final_objective,
                    "full_objective_drop_pct": pct_drop(first_objective, final_objective),
                    "exchange_objective_drop_pct": pct_drop(exchange_start_objective, final_objective),
                    "validation_mae": float(entry["validation_mae"]),
                    "final_reconstruction_huber": float(entry["final_terms"]["reconstruction_huber"]),
                    "final_posterior_trace_per_node": float(entry["final_terms"]["posterior_trace_per_node"]),
                    "final_scenario_cvar_trace_per_node": float(entry["final_terms"]["scenario_cvar_trace_per_node"]),
                    "final_spatial_penalty": float(entry["final_terms"]["spatial_penalty"]),
                    "objective_monotone": all(a >= b for a, b in zip(objectives, objectives[1:])),
                    "beta": float(entry["weights"]["beta"]),
                    "gamma": float(entry["weights"]["gamma"]),
                    "eta": float(entry["weights"]["eta"]),
                    "huber_delta": float(entry["weights"]["huber_delta"]),
                }
            )
    if not rows:
        raise ValueError(f"no TRACE-BiOpt histories under {STAGE15}")
    return rows


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, float], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["dataset"]), float(row["budget"]))].append(row)
    out: list[dict[str, object]] = []
    for (dataset, budget), sub in sorted(grouped.items()):
        out.append(
            {
                "dataset": dataset,
                "budget": budget,
                "runs": len(sub),
                "sensor_count_mean": mean(float(row["sensor_count"]) for row in sub),
                "forward_steps_mean": mean(float(row["forward_steps"]) for row in sub),
                "construction_steps_mean": mean(float(row["construction_steps"]) for row in sub),
                "exchange_steps_mean": mean(float(row["exchange_steps"]) for row in sub),
                "exchange_steps_min": min(int(row["exchange_steps"]) for row in sub),
                "exchange_steps_max": max(int(row["exchange_steps"]) for row in sub),
                "searched_one_exchange_neighbors_mean": mean(float(row["searched_one_exchange_neighbors"]) for row in sub),
                "full_one_exchange_neighbors_mean": mean(float(row["full_one_exchange_neighbors"]) for row in sub),
                "searched_one_exchange_coverage_pct_mean": mean(float(row["searched_one_exchange_coverage_pct"]) for row in sub),
                "no_improving_stop_runs": sum(bool(row["no_improving_stop"]) for row in sub),
                "exchange_budget_exhausted_runs": sum(bool(row["exchange_budget_exhausted"]) for row in sub),
                "full_objective_drop_pct_mean": mean(float(row["full_objective_drop_pct"]) for row in sub),
                "exchange_objective_drop_pct_mean": mean(float(row["exchange_objective_drop_pct"]) for row in sub),
                "validation_mae_mean": mean(float(row["validation_mae"]) for row in sub),
                "final_objective_mean": mean(float(row["final_objective"]) for row in sub),
                "objective_monotone_runs": sum(bool(row["objective_monotone"]) for row in sub),
            }
        )
    return out


def write_tex(rows: list[dict[str, object]]) -> None:
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{TRACE-BiOpt optimization diagnostics from Stage15 histories, including searched one-exchange coverage and stop certificates.}",
        "\\label{tab:trace-biopt-optimization}",
        "\\tiny",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{lccccccc}",
        "\\toprule",
        "Dataset & Budget & Exchanges & Search cov. & Stop cert. & Full drop & Exchange drop & Mono. \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(str(row['dataset']))} & "
            f"{int(float(row['budget']) * 100)}\\% & "
            f"{float(row['exchange_steps_mean']):.1f} [{int(row['exchange_steps_min'])},{int(row['exchange_steps_max'])}] & "
            f"{float(row['searched_one_exchange_coverage_pct_mean']):.1f}\\% & "
            f"{int(row['no_improving_stop_runs'])}/{int(row['exchange_budget_exhausted_runs'])} & "
            f"{float(row['full_objective_drop_pct_mean']):.1f}\\% & "
            f"{float(row['exchange_objective_drop_pct_mean']):.2f}\\% & "
            f"{int(row['objective_monotone_runs'])}/{int(row['runs'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "}",
            "\\begin{flushleft}\\footnotesize Each row aggregates ten Stage15 split-seed runs. Search cov. is the mean searched one-exchange neighborhood size as a percentage of the full $k(n-k)$ swap set under the declared deterministic add/remove pools. Stop cert. reports runs ending by no improving searched one-exchange move versus runs exhausting the declared exchange-iteration budget. Full drop is the mean percent reduction from the first recorded construction or warm-start objective to the final TRACE-BiOpt objective. Exchange drop is the mean percent reduction from the completed construction/warm-start layout to the final exchanged layout. Monotone counts runs whose accepted construction/exchange history is non-increasing in the single TRACE-BiOpt objective.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    detail = history_rows()
    detail_fields = list(detail[0].keys())
    summary = summarize(detail)
    summary_fields = list(summary[0].keys())
    write_csv(DETAIL_CSV, detail, detail_fields)
    write_csv(SUMMARY_CSV, summary, summary_fields)
    write_tex(summary)
    print(f"Wrote {OUT_TEX}, {SUMMARY_CSV}, and {DETAIL_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
