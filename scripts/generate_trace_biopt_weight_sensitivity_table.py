#!/usr/bin/env python3
"""Generate a regime-specific TRACE-BiOpt weight-sensitivity table."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE_RESULTS = ROOT / "TRC-23-02333" / "trace_sl_results"
CURRENT_BEST = TRACE_RESULTS / "current_best_trace_biopt_evidence"
STAGE15 = TRACE_RESULTS / "stage15_biopt_allbudget_10seed_v2"

OUT_CSV = CURRENT_BEST / "trace_biopt_weight_sensitivity.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_weight_sensitivity.tex"

CASES = [
    {
        "case_label": "Seattle 20\\%",
        "dataset": "Seattle",
        "budget": 0.2,
        "routes": [
            {
                "route_label": "Seattle diagnostic certified",
                "seed_dir": STAGE15 / "seattle" / "seed_25",
                "search_route": "Stage15 active-set",
            },
            {
                "route_label": "Zero-weight probe",
                "seed_dir": TRACE_RESULTS / "diagnose_biopt_seattle_strongsearch_96",
                "search_route": "Strong-search 96",
            },
        ],
    },
    {
        "case_label": "Seattle 30\\%",
        "dataset": "Seattle",
        "budget": 0.3,
        "routes": [
            {
                "route_label": "Seattle diagnostic certified",
                "seed_dir": STAGE15 / "seattle" / "seed_25",
                "search_route": "Stage15 active-set",
            },
            {
                "route_label": "Zero-weight probe",
                "seed_dir": TRACE_RESULTS / "diagnose_biopt_seattle_strongsearch_96",
                "search_route": "Strong-search 96",
            },
        ],
    },
    {
        "case_label": "PeMS7\\_228 10\\%",
        "dataset": "PeMS7_228",
        "budget": 0.1,
        "routes": [
            {
                "route_label": "Stage15 certified",
                "seed_dir": STAGE15 / "pems7_228" / "seed_25",
                "search_route": "Stage15 active-set",
            },
            {
                "route_label": "Zero-weight probe",
                "seed_dir": TRACE_RESULTS / "diagnose_biopt_pems228_strong96",
                "search_route": "Strong-search 96",
            },
            {
                "route_label": "Calibrated low-cert",
                "seed_dir": TRACE_RESULTS / "stage15_biopt_pems228_10_risksource_probe" / "train_val_lowcert_delta1_fullsearch" / "seed_25",
                "search_route": "Train+val full-search 192",
            },
        ],
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


def trace_row(metrics_rows: list[dict[str, str]], budget: float) -> dict[str, str]:
    return next(
        row for row in metrics_rows
        if row["layout_type"] == "trace_biopt"
        and row["method"] == "gls_map"
        and abs(float(row["budget"]) - budget) < 1e-9
    )


def format_weights(config: dict[str, object]) -> str:
    return (
        f"({float(config['trace_biopt_beta']):.2f},"
        f"{float(config['trace_biopt_gamma']):.2f},"
        f"{float(config['trace_biopt_eta']):.2f})"
    )


def display_risk_source(value: str) -> str:
    if value == "train_val":
        return "train+val"
    return value


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in CASES:
        case_rows = []
        for route in case["routes"]:
            seed_dir = Path(route["seed_dir"])
            metrics = load_csv(seed_dir / "metrics.csv")
            config = load_json(seed_dir / "config.json")
            row = trace_row(metrics, float(case["budget"]))
            risk_source = config.get("trace_biopt_risk_source", "val")
            case_rows.append(
                {
                    "case_label": case["case_label"],
                    "dataset": case["dataset"],
                    "budget": float(case["budget"]),
                    "budget_pct": int(round(float(case["budget"]) * 100)),
                    "route_label": route["route_label"],
                    "weights_label": format_weights(config),
                    "risk_source": str(risk_source),
                    "risk_source_label": display_risk_source(str(risk_source)),
                    "search_route": route["search_route"],
                    "validation_mae": f"{float(row['validation_selected_mae']):.6f}",
                    "test_mae": f"{float(row['mae']):.6f}",
                    "posterior_trace": f"{float(row['posterior_trace']):.6f}",
                }
            )
        best_test = min(float(row["test_mae"]) for row in case_rows)
        for row in case_rows:
            row["test_delta_vs_case_best"] = f"{float(row['test_mae']) - best_test:.6f}"
            rows.append(row)
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
        "\\caption{Regime-specific TRACE-BiOpt objective-weight sensitivity slices. Lower MAE is better. These rows are mechanism evidence only: the Seattle rows are bounded same-split diagnostic slices around the stable certificate-weighted Seattle route, while the PeMS7\\_228 10\\% weak row uses the promoted calibrated current-best route.}",
        "\\label{tab:trace-biopt-weight-sensitivity}",
        "\\tiny",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.12\\textwidth}>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\centering\\arraybackslash}p{0.11\\textwidth}>{\\centering\\arraybackslash}p{0.07\\textwidth}>{\\raggedright\\arraybackslash}p{0.14\\textwidth}>{\\centering\\arraybackslash}p{0.07\\textwidth}>{\\centering\\arraybackslash}p{0.07\\textwidth}>{\\centering\\arraybackslash}p{0.09\\textwidth}}",
        "\\toprule",
        "Case & Route & $(\\beta,\\gamma,\\eta)$ & Risk & Search & Val. & Test & $\\Delta$ vs best \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{row['case_label']} & "
            f"{tex_escape(str(row['route_label']))} & "
            f"{tex_escape(str(row['weights_label']))} & "
            f"{tex_escape(str(row['risk_source_label']))} & "
            f"{tex_escape(str(row['search_route']))} & "
            f"{float(row['validation_mae']):.3f} & "
            f"{float(row['test_mae']):.3f} & "
            f"{float(row['test_delta_vs_case_best']):+.3f} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabular}",
            "\\begin{flushleft}\\footnotesize The Seattle rows are bounded same-split diagnostic slices: they compare the stable Stage15 certificate-weighted Seattle route with a matched zero-weight strong-search diagnostic on the same split seed and do not replace the ten-seed current-best evidence chain. The PeMS7\\_228 10\\% rows compare the original heavy-cert Stage15 route, a zero-weight strong-search diagnostic, and the promoted current-best calibrated low-cert full-search route on the same split seed.\\end{flushleft}",
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
