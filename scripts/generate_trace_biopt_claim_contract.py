#!/usr/bin/env python3
"""Generate TRACE-BiOpt claim contracts from dominance evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

import pandas as pd


SCHEMA = "trace_biopt_claim_contract_v1"
REQUIRED_DOMINANCE_COLUMNS = (
    "dataset",
    "budget",
    "trace_biopt_mean",
    "best_baseline_mean",
    "best_baseline_layout",
    "trace_minus_best_baseline",
    "trace_beats_best_baseline",
    "baseline_count",
    "paired_count",
    "paired_win_count",
    "paired_paired_t_p",
    "paired_wilcoxon_p",
)
CONTRACT_COLUMNS = (
    "claim_id",
    "dataset",
    "budget",
    "claim_status",
    "evidence_strength",
    "allowed_wording",
    "required_caveat",
    "forbidden_wording",
    "trace_biopt_mean",
    "best_baseline_mean",
    "best_baseline_layout",
    "trace_minus_best_baseline",
    "baseline_count",
    "paired_count",
    "paired_win_count",
    "paired_paired_t_p",
    "paired_wilcoxon_p",
    "dominance_source",
    "paired_source",
    "layout_summary_source",
)


class ClaimContractError(ValueError):
    """Raised when Stage15 evidence is insufficient for a claim contract."""


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected CSV not found: {path}")
    frame = pd.read_csv(path)
    if frame.empty:
        raise ClaimContractError(f"Expected nonempty CSV: {path}")
    return frame


def require_columns(frame: pd.DataFrame, columns: Sequence[str], label: str) -> None:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ClaimContractError(f"{label} is missing required columns: {missing}")


def bool_series(values: pd.Series) -> pd.Series:
    if values.dtype == bool:
        return values
    return values.astype(str).str.lower().isin({"true", "1", "yes"})


def format_budget(value: float) -> str:
    return f"{100.0 * float(value):.0f}%"


def format_float(value: object) -> str:
    if pd.isna(value):
        return ""
    return f"{float(value):.6g}"


def project_relative(path: Path, project_root: Path | None = None) -> str:
    resolved = path.resolve()
    root = (project_root or Path.cwd()).resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def evidence_strength(row: pd.Series) -> str:
    paired_count = int(row["paired_count"])
    paired_win_count = int(row["paired_win_count"])
    paired_t_p = row.get("paired_paired_t_p")
    if paired_count >= 10 and paired_win_count == paired_count and pd.notna(paired_t_p) and float(paired_t_p) < 0.05:
        return "submission_ready_paired_dominance"
    if paired_count >= 10:
        return "multi_seed_mean_dominance_paired_mixed"
    if paired_win_count == paired_count:
        return "directional_mean_dominance_all_observed_splits"
    return "directional_mean_dominance_mixed_split_wins"


def caveat_for_strength(strength: str, paired_count: int) -> str:
    if strength == "submission_ready_paired_dominance":
        return "Report paired statistics and restrict the claim to tested pre-registered baselines."
    return (
        f"Report this as directional evidence over {paired_count} seeds; "
        "do not use final significance wording until additional seeds support stable paired tests."
    )


def evidence_route_phrase(row: pd.Series) -> str:
    source = str(row.get("evidence_source", "") or "")
    if source.startswith("stage16_replaceable:"):
        root = source.split(":", 1)[1]
        return f"in the current-best evidence chain via the replaceable Stage16 calibrated rerun `{root}`."
    if source == "stage15_main":
        return "in the current-best evidence chain, where this row currently remains on the Stage15 main evidence path."
    return "in the current evidence run."


def allowed_wording(row: pd.Series) -> str:
    return (
        "TRACE-BiOpt achieved the lowest mean held-out GLS/MAP MAE among all "
        f"pre-registered non-BiOpt baselines on {row['dataset']} at "
        f"{format_budget(row['budget'])} sensor budget {evidence_route_phrase(row)}"
    )


def forbidden_wording(row: pd.Series) -> str:
    return (
        "Do not claim global optimality, universal dominance over untested baselines, "
        "cross-network generalization, or statistically significant superiority unless "
        f"the paired-test gate is satisfied for {row['dataset']} {format_budget(row['budget'])}."
    )


def build_baseline_registry(layout_summary: pd.DataFrame | None) -> list[str]:
    if layout_summary is None:
        return []
    require_columns(layout_summary, ("layout_type",), "layout summary")
    baselines = sorted(str(x) for x in layout_summary["layout_type"].dropna().unique() if str(x) != "trace_biopt")
    if not baselines:
        raise ClaimContractError("layout summary did not contain any non-BiOpt baselines")
    return baselines


def build_contract_rows(
    dominance: pd.DataFrame,
    dominance_source: Path,
    paired_source: Path | None = None,
    layout_summary_source: Path | None = None,
) -> list[dict[str, object]]:
    require_columns(dominance, REQUIRED_DOMINANCE_COLUMNS, "dominance table")
    beats = bool_series(dominance["trace_beats_best_baseline"])
    if not bool(beats.all()):
        failed = dominance.loc[~beats, ["dataset", "budget", "best_baseline_layout", "trace_minus_best_baseline"]]
        raise ClaimContractError(f"TRACE-BiOpt does not beat the best baseline for all rows:\n{failed.to_string(index=False)}")

    rows: list[dict[str, object]] = []
    dominance_rel = project_relative(dominance_source)
    paired_rel = project_relative(paired_source) if paired_source else ""
    layout_rel = project_relative(layout_summary_source) if layout_summary_source else ""
    sorted_frame = dominance.sort_values(["dataset", "budget"]).reset_index(drop=True)
    for _, row in sorted_frame.iterrows():
        strength = evidence_strength(row)
        paired_count = int(row["paired_count"])
        rows.append(
            {
                "claim_id": f"BIOPT-{row['dataset']}-{format_budget(row['budget']).replace('%', 'pct')}",
                "dataset": row["dataset"],
                "budget": float(row["budget"]),
                "claim_status": "supported_directional" if not strength.startswith("submission_ready") else "supported_submission_ready",
                "evidence_strength": strength,
                "allowed_wording": allowed_wording(row),
                "required_caveat": caveat_for_strength(strength, paired_count),
                "forbidden_wording": forbidden_wording(row),
                "trace_biopt_mean": float(row["trace_biopt_mean"]),
                "best_baseline_mean": float(row["best_baseline_mean"]),
                "best_baseline_layout": row["best_baseline_layout"],
                "trace_minus_best_baseline": float(row["trace_minus_best_baseline"]),
                "baseline_count": int(row["baseline_count"]),
                "paired_count": paired_count,
                "paired_win_count": int(row["paired_win_count"]),
                "paired_paired_t_p": None if pd.isna(row["paired_paired_t_p"]) else float(row["paired_paired_t_p"]),
                "paired_wilcoxon_p": None if pd.isna(row["paired_wilcoxon_p"]) else float(row["paired_wilcoxon_p"]),
                "dominance_source": dominance_rel,
                "paired_source": paired_rel,
                "layout_summary_source": layout_rel,
            }
        )
    return rows


def aggregate_claim(rows: Sequence[dict[str, object]], baseline_registry: Sequence[str]) -> dict[str, object]:
    budgets = sorted({float(row["budget"]) for row in rows})
    datasets = sorted({str(row["dataset"]) for row in rows})
    weakest = sorted(rows, key=lambda row: float(row["trace_minus_best_baseline"]), reverse=True)[0]
    all_submission_ready = all(str(row["claim_status"]) == "supported_submission_ready" for row in rows)
    return {
        "status": "supported_submission_ready" if all_submission_ready else "supported_directional",
        "allowed_wording": (
            "Across the tested datasets and 10/20/30 percent budgets, TRACE-BiOpt "
            "has the lowest mean held-out GLS/MAP MAE against the pre-registered "
            "non-BiOpt baseline set."
        ),
        "required_caveat": (
            "All nine tested dataset-budget rows satisfy the paired-dominance gate; "
            "claims still remain restricted to the tested datasets and the pre-registered non-BiOpt baseline set."
            if all_submission_ready
            else "This is directional current evidence, not final TR-B significance wording; "
            "additional seeds are required for stable paired tests."
        ),
        "datasets": datasets,
        "budgets": budgets,
        "row_count": len(rows),
        "baseline_registry": list(baseline_registry),
        "weakest_margin_row": {
            "dataset": weakest["dataset"],
            "budget": weakest["budget"],
            "trace_minus_best_baseline": weakest["trace_minus_best_baseline"],
            "best_baseline_layout": weakest["best_baseline_layout"],
        },
    }


def markdown_table(rows: Sequence[dict[str, object]], columns: Sequence[str]) -> str:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        values = []
        for column in columns:
            value = row.get(column, "")
            if isinstance(value, float):
                values.append(format_float(value))
            else:
                values.append("" if value is None else str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines) + "\n"


def write_outputs(rows: Sequence[dict[str, object]], aggregate: dict[str, object], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows).loc[:, list(CONTRACT_COLUMNS)]
    frame.to_csv(output_dir / "trace_biopt_claim_contract.csv", index=False)
    payload = {
        "schema": SCHEMA,
        "aggregate_claim": aggregate,
        "row_count": len(rows),
        "rows": list(rows),
    }
    (output_dir / "trace_biopt_claim_contract.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_columns = (
        "claim_id",
        "claim_status",
        "evidence_strength",
        "trace_biopt_mean",
        "best_baseline_mean",
        "best_baseline_layout",
        "trace_minus_best_baseline",
        "paired_count",
        "paired_win_count",
        "paired_paired_t_p",
    )
    markdown = (
        "# TRACE-BiOpt Claim Contract\n\n"
        f"Schema: `{SCHEMA}`\n\n"
        "Aggregate allowed wording:\n\n"
        f"> {aggregate['allowed_wording']}\n\n"
        "Required aggregate caveat:\n\n"
        f"> {aggregate['required_caveat']}\n\n"
        + markdown_table(rows, md_columns)
    )
    (output_dir / "trace_biopt_claim_contract.md").write_text(markdown, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dominance", type=Path, required=True, help="trace_biopt_best_baseline_delta.csv")
    parser.add_argument("--paired-tests", type=Path, default=None, help="gls_map_paired_delta_tests.csv provenance source")
    parser.add_argument("--layout-summary", type=Path, default=None, help="gls_map_layout_summary.csv baseline registry source")
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dominance = load_csv(args.dominance)
    layout_summary = load_csv(args.layout_summary) if args.layout_summary else None
    baseline_registry = build_baseline_registry(layout_summary)
    rows = build_contract_rows(
        dominance,
        args.dominance,
        paired_source=args.paired_tests,
        layout_summary_source=args.layout_summary,
    )
    aggregate = aggregate_claim(rows, baseline_registry)
    write_outputs(rows, aggregate, args.output_dir)
    print(f"Wrote TRACE-BiOpt claim contract to {args.output_dir}")


if __name__ == "__main__":
    main()
