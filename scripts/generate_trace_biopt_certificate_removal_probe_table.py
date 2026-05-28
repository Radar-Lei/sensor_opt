#!/usr/bin/env python3
"""Generate a single-seed certificate-removal probe table for TRACE-BiOpt."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"
STAGE17 = TRACE_RESULTS / "stage17_certificate_weight_probe"

OUT_CSV = CURRENT_BEST / "trace_biopt_certificate_removal_probe.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_certificate_removal_probe.tex"

CASES = [
    {
        "dataset": "Seattle",
        "budget": 0.2,
        "seed_dir": STAGE15 / "seattle" / "seed_25",
        "probe_dir": TRACE_RESULTS / "diagnose_biopt_seattle_strongsearch_96",
    },
    {
        "dataset": "Seattle",
        "budget": 0.3,
        "seed_dir": STAGE15 / "seattle" / "seed_25",
        "probe_dir": TRACE_RESULTS / "diagnose_biopt_seattle_strongsearch_96",
    },
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


def trace_mae(metrics_rows: list[dict[str, str]], budget: float) -> float:
    row = next(
        row for row in metrics_rows
        if row["layout_type"] == "trace_biopt"
        and row["method"] == "gls_map"
        and abs(float(row["budget"]) - budget) < 1e-9
    )
    return float(row["mae"])


def validation_mae(history_rows: list[dict[str, object]], budget: float) -> float:
    row = next(row for row in history_rows if abs(float(row["budget"]) - budget) < 1e-9)
    return float(row["validation_mae"])


def build_rows() -> list[dict[str, object]]:
    rows = []
    for case in CASES:
        dataset = case["dataset"]
        budget = float(case["budget"])
        seed_dir = Path(case["seed_dir"])
        probe_dir = Path(case["probe_dir"])
        default_metrics = load_csv(seed_dir / "metrics.csv")
        probe_metrics = load_csv(probe_dir / "metrics.csv")
        default_history = load_json(seed_dir / "trace_biopt_history.json")
        probe_history = load_json(probe_dir / "trace_biopt_history.json")
        default_test_mae = trace_mae(default_metrics, budget)
        probe_test_mae = trace_mae(probe_metrics, budget)
        default_val_mae = validation_mae(default_history, budget)
        probe_val_mae = validation_mae(probe_history, budget)
        rows.append(
            {
                "dataset": dataset,
                "budget": budget,
                "budget_pct": int(round(budget * 100)),
                "default_route_label": "Seattle diagnostic certified route",
                "probe_route_label": "Zero-weight strong-search probe",
                "default_val_mae": f"{default_val_mae:.6f}",
                "probe_val_mae": f"{probe_val_mae:.6f}",
                "default_test_mae": f"{default_test_mae:.6f}",
                "probe_test_mae": f"{probe_test_mae:.6f}",
                "test_probe_minus_default": f"{probe_test_mae - default_test_mae:.6f}",
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_tex(rows: list[dict[str, object]]) -> None:
    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Single-seed certificate-removal probe on stable Seattle diagnostic slices. The completed diagnostic route keeps the split seed and strong-search budget used during method diagnosis, but sets $(\\beta,\\gamma,\\eta)=(0,0,0)$ and routes the objective through reconstruction-only optimization. Lower MAE is better.}",
        "\\label{tab:trace-biopt-certificate-removal-probe}",
        "\\small",
        "\\begin{tabular}{lcccccc}",
        "\\toprule",
        "Dataset & Budget & Curr. val & Zero-wt val & Curr. test & Zero-wt test & Probe $-$ curr. \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(str(row['dataset']))} & "
            f"{int(row['budget_pct'])}\\% & "
            f"{float(row['default_val_mae']):.3f} & "
            f"{float(row['probe_val_mae']):.3f} & "
            f"{float(row['default_test_mae']):.3f} & "
            f"{float(row['probe_test_mae']):.3f} & "
            f"{float(row['test_probe_minus_default']):+.3f} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "\\begin{flushleft}\\footnotesize The probe is routed as mechanism evidence only. It asks whether the stable certificate-weighted Seattle diagnostic route still looks best when the posterior-trace, scenario-CVaR, and spatial terms are removed and the route falls back to a reconstruction-only strong-search diagnostic. These are bounded same-split Seattle slices, not replacement-evidence rows.\\end{flushleft}",
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
