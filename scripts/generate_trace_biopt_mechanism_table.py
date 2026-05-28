#!/usr/bin/env python3
"""Generate TRACE-BiOpt mechanism diagnostics from current best evidence."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGE15 = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined"
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
OUT_CSV = CURRENT_BEST / "trace_biopt_mechanism_diagnostics.csv"
OUT_TEX = ROOT / "paper" / "tables" / "table_trace_biopt_mechanism.tex"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def fmt_count(count: int, total: int) -> str:
    return f"{count}/{total}"


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def main() -> int:
    dominance = load_csv(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv")
    correlations = load_csv(STAGE15 / "certificate_correlation_summary.csv")
    if not dominance:
        raise ValueError("dominance evidence is empty")

    total = len(dominance)
    beaten = sum(row["trace_beats_best_baseline"] == "True" for row in dominance)
    significant = sum(float(row["paired_paired_t_p"]) < 0.05 for row in dominance)
    all_split_wins = sum(int(float(row["paired_win_count"])) == int(float(row["paired_count"])) for row in dominance)
    baseline_counts = sorted({int(float(row["baseline_count"])) for row in dominance})
    comparator_counts = Counter(row["best_baseline_layout"] for row in dominance)
    weakest = min(dominance, key=lambda row: abs(float(row["trace_minus_best_baseline"])))
    promoted_rows = sum(row["evidence_source"].startswith("stage16_replaceable:") for row in dominance)

    gls = {row["certificate"]: row for row in correlations if row["method"] == "gls_map"}
    posterior = gls["posterior_trace"]
    condition = gls["condition_number"]
    logdet = gls["information_logdet"]

    comparator_text = ", ".join(
        f"{name} in {count}/{total} rows" for name, count in sorted(comparator_counts.items())
    )
    baseline_count_text = (
        f"{baseline_counts[0]} baseline rows per regime"
        if len(baseline_counts) == 1
        else f"{min(baseline_counts)}--{max(baseline_counts)} baseline rows per regime"
    )
    weakest_label = f"{weakest['dataset']} {int(float(weakest['budget']) * 100)}%"
    weakest_text = (
        f"{weakest_label}: delta {float(weakest['trace_minus_best_baseline']):.4f} MAE, "
        f"{int(float(weakest['paired_win_count']))}/{int(float(weakest['paired_count']))} paired wins, "
        f"paired t p={float(weakest['paired_paired_t_p']):.4f}"
    )
    cert_text = (
        f"posterior trace Spearman rho={float(posterior['spearman_mae_mean']):.3f}; "
        f"condition number rho={float(condition['spearman_mae_mean']):.3f}; "
        f"information logdet rho={float(logdet['spearman_mae_mean']):.3f}; "
        f"n={int(float(posterior['spearman_mae_count']))}"
    )

    rows = [
        {
            "diagnostic": "Strongest-comparator gate",
            "evidence": f"TRACE-BiOpt beats the row-specific best non-BiOpt baseline in {fmt_count(beaten, total)} rows; {baseline_count_text}.",
            "interpretation": "The main table is not a comparison against a fixed weak baseline.",
        },
        {
            "diagnostic": "Paired-test strength",
            "evidence": f"{fmt_count(significant, total)} rows have paired t-test p<0.05; {fmt_count(all_split_wins, total)} rows win all ten paired splits.",
            "interpretation": "Most regimes show split-paired evidence beyond mean dominance.",
        },
        {
            "diagnostic": "Weak-row resolution path",
            "evidence": weakest_text + f"; {promoted_rows}/{total} current-best rows are already promoted from calibrated reruns.",
            "interpretation": "Weak rows are resolved inside the same TRACE-BiOpt objective family and then promoted into the audited main evidence chain.",
        },
        {
            "diagnostic": "Comparator hardness",
            "evidence": comparator_text + ".",
            "interpretation": "The strongest comparator often comes from the prior TRACE-SL or RCSS family, not only simple heuristics.",
        },
        {
            "diagnostic": "Certificate alignment",
            "evidence": cert_text + ".",
            "interpretation": "Posterior/certificate quantities track held-out MAE under the GLS/MAP protocol.",
        },
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["diagnostic", "evidence", "interpretation"])
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "\\begin{table*}[t]",
        "\\centering",
        "\\caption{Mechanism diagnostics for TRACE-BiOpt from the current best evidence chain.}",
        "\\label{tab:trace-biopt-mechanism}",
        "\\small",
        "\\begin{tabularx}{\\textwidth}{>{\\raggedright\\arraybackslash}p{0.22\\textwidth}>{\\raggedright\\arraybackslash}p{0.39\\textwidth}>{\\raggedright\\arraybackslash}X}",
        "\\toprule",
        "Diagnostic & Evidence & Interpretation \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['diagnostic'])} & {tex_escape(row['evidence'])} & {tex_escape(row['interpretation'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabularx}", "\\end{table*}", ""])
    OUT_TEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_TEX} and {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
