#!/usr/bin/env python3
"""Generate reviewer-facing deployment stress posture table from Stage14 frontier."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
SOURCE = PAPER_SOURCES / "robustness_frontier_summary.csv"
OUT_CSV = PAPER_SOURCES / "robustness_stress_posture_summary.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_deployment_stress_posture.tex"


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
    frontier = {row["condition"]: row for row in load_csv(SOURCE)}

    rows = [
        {
            "stress_regime": "Nominal and cost-limited screen",
            "supporting_conditions": "baseline; cost proxy budget 45",
            "frontier_reading": (
                f"graph-spectral wins both slices with the same {float(frontier['baseline']['gap_to_runner_up']):.4f} MAE gap "
                "over the runner-up POD/QR family."
            ),
            "deployment_posture": "Cost proxy alone does not move the bounded stress frontier in this check; no special contingency is suggested beyond the default audited comparison set.",
        },
        {
            "stress_regime": "Diffuse corruption",
            "supporting_conditions": "observation noise 5%; random missing 10%",
            "frontier_reading": (
                f"graph-spectral remains best with relatively wide gaps of {float(frontier['observation noise 5%']['gap_to_runner_up']):.4f} "
                f"and {float(frontier['random missing 10%']['gap_to_runner_up']):.4f} MAE."
            ),
            "deployment_posture": "Dispersed measurement degradation keeps the frontier relatively separated, so graph-spectral layouts are the strongest bounded stress default in these slices.",
        },
        {
            "stress_regime": "Escalating sensor attrition",
            "supporting_conditions": "sensor failure 5%; sensor failure 10%; sensor failure 20%",
            "frontier_reading": (
                "graph-spectral wins all three failure slices, but the 20% failure gap shrinks to "
                f"{float(frontier['sensor failure 20%']['gap_to_runner_up']):.4f} MAE."
            ),
            "deployment_posture": "Heavy attrition is a narrow-frontier regime; deployment review should include redundancy or fallback planning because the stress winner is only marginally separated.",
        },
        {
            "stress_regime": "Chronological drift",
            "supporting_conditions": "chronological split",
            "frontier_reading": (
                f"graph-spectral still wins, but only by {float(frontier['chronological split']['gap_to_runner_up']):.4f} MAE "
                "over multistart swap."
            ),
            "deployment_posture": "Temporal nonstationarity should trigger re-validation rather than a blanket robustness claim because the frontier is already narrow under chronological drift.",
        },
        {
            "stress_regime": "Contiguous outage",
            "supporting_conditions": "block missing 12 steps",
            "frontier_reading": (
                "the only family shift occurs here: logdet becomes the winner with a "
                f"{float(frontier['block missing 12 steps']['gap_to_runner_up']):.4f} MAE gap."
            ),
            "deployment_posture": "Long contiguous outages are the clearest tested case where observability-style algebraic structure matters; outage-contingency planning should not assume the nominal winner family persists.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["stress_regime", "supporting_conditions", "frontier_reading", "deployment_posture"],
        )
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Reviewer-facing deployment stress posture from the bounded Stage14 PeMS7\\_228 frontier. The table translates the stress-frontier winners and gap sizes into operational reading rather than into TRACE-BiOpt dominance claims.}",
        "\\label{tab:trace-biopt-deployment-stress-posture}",
        "\\scriptsize",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\raggedright\\arraybackslash}p{0.19\\textwidth}>{\\raggedright\\arraybackslash}p{0.23\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Stress regime & Supporting conditions & Frontier reading & Deployment posture \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['stress_regime'])} & {tex_escape(row['supporting_conditions'])} & "
            f"{tex_escape(row['frontier_reading'])} & {tex_escape(row['deployment_posture'])} \\\\"
        )
    lines.extend(
        [
            "\\bottomrule",
            "\\end{tabularx}",
            "\\begin{flushleft}\\footnotesize This table remains bounded Stage14 stress evidence only. It does not assert TRACE-BiOpt dominance under the same perturbations, because the underlying artifact evaluates pre-TRACE-BiOpt reviewer-facing baselines on two split seeds.\\end{flushleft}",
            "\\end{table*}",
            "",
        ]
    )
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
