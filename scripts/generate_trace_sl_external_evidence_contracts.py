#!/usr/bin/env python3
"""Generate TRACE-SL external Stage12 evidence contracts and gates."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd


TRACE_RESULTS_ROOT = Path("TRC-23-02333/trace_sl_results")
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
REQUIRED_SPLIT_COUNT = 10
REQUIRED_BUDGETS = ("0.10", "0.20", "0.30")
REQUIRED_ARTIFACTS = (
    "SUMMARY.md",
    "combined_metrics.csv",
    "gls_map_layout_summary.csv",
    "gls_map_delta_summary.csv",
    "gls_map_paired_delta_tests.csv",
    "gls_map_win_counts.csv",
    "rcss_selected_sources.csv",
)
PAIRED_STAT_COLUMNS = ("delta_mean", "ci95_low", "ci95_high", "paired_t_p", "wilcoxon_p", "win_count")
PAIRED_STATS_AVAILABLE = "paired_stats_available"
DESCRIPTIVE_ONLY = "descriptive_only"
MAIN_METHOD_LABEL = "validation_swap_selected"

DATASET_SPECS = (
    {
        "dataset": "PeMS7_1026",
        "source_stage": "external_stage12_baseline_portfolio",
        "result_dir": TRACE_RESULTS_ROOT / "pems7_1026_stage12_baseline_portfolio",
        "launcher": "scripts/run_stage12_pems7_1026.sh",
        "required_split_count": REQUIRED_SPLIT_COUNT,
        "budgets": REQUIRED_BUDGETS,
        "required_artifacts": REQUIRED_ARTIFACTS,
        "reviewer_baseline_labels": (
            "multistart_swap_by_validation",
            "best_random_by_validation",
            "random",
            "top_variance",
            "greedy_a_trace",
            "graph_sampling_laplacian",
            "observability_proxy",
            "qr_pod_modes",
        ),
        "status_json": None,
    },
    {
        "dataset": "Seattle",
        "source_stage": "external_stage12_baseline_portfolio",
        "result_dir": TRACE_RESULTS_ROOT / "seattle_stage12_baseline_portfolio",
        "launcher": "scripts/run_stage12_seattle.sh",
        "required_split_count": REQUIRED_SPLIT_COUNT,
        "budgets": REQUIRED_BUDGETS,
        "required_artifacts": REQUIRED_ARTIFACTS,
        "reviewer_baseline_labels": (
            "multistart_swap_by_validation",
            "best_random_by_validation",
            "random",
            "top_variance",
            "greedy_a_trace",
            "graph_sampling_laplacian",
            "observability_proxy",
            "qr_pod_modes",
        ),
        "status_json": "stage12_status.json",
    },
)

EXTERNAL_EVIDENCE_COLUMNS = (
    "dataset",
    "source_stage",
    "source_dir",
    "source_csv",
    "budget",
    "method_label",
    "layout_type",
    "table_role",
    "test_mae_mean",
    "test_mae_std",
    "test_rmse_mean",
    "test_mape_mean",
    "paired_baseline",
    "paired_evidence_status",
    "delta_mean",
    "ci95_low",
    "ci95_high",
    "paired_t_p",
    "wilcoxon_p",
    "win_count",
    "actual_split_count",
    "required_split_count",
    "evidence_status",
    "claim_lane",
    "core_claim_eligible",
    "blocker_reason",
)


class ExternalEvidenceValidationError(ValueError):
    """Raised when external evidence contract inputs violate Phase 8 policy."""


def project_relative(path: Path, project_root: Path | None = None) -> str:
    resolved = path.resolve()
    if project_root is None:
        project_root = Path.cwd()
    try:
        return resolved.relative_to(project_root.resolve()).as_posix()
    except ValueError:
        parts = resolved.parts
        if "TRC-23-02333" in parts:
            start = parts.index("TRC-23-02333")
            return Path(*parts[start:]).as_posix()
        return path.as_posix()


def resolve_output_dir(project_root: Path, output_dir: Path) -> Path:
    if output_dir.is_absolute():
        return output_dir
    return project_root / output_dir


def assert_no_raw_dataset_path(value: str | Path, label: str) -> None:
    rendered = Path(value).as_posix() if isinstance(value, Path) else str(value)
    if RAW_DATASET_PREFIX in rendered:
        raise ValueError(f"{label} references raw dataset path: {rendered}")


def require_trace_results_path(path: Path, project_root: Path, label: str) -> str:
    relative = project_relative(path, project_root)
    assert_no_raw_dataset_path(relative, label)
    if not relative.startswith(TRACE_RESULTS_ROOT.as_posix() + "/"):
        raise ValueError(f"{label} is outside curated trace_sl_results: {relative}")
    return relative


def assert_git_path_is_tracked(project_root: Path, relative: str, label: str) -> None:
    result = subprocess.run(
        ["git", "-C", str(project_root), "ls-files", "--error-unmatch", relative],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"{label} is not committed/tracked by git: {relative}")


def is_git_path_tracked(project_root: Path, relative: str) -> bool:
    result = subprocess.run(
        ["git", "-C", str(project_root), "ls-files", "--error-unmatch", relative],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected aggregate CSV not found: {path}")
    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError(f"Expected nonempty aggregate CSV: {path}")
    return frame


def require_columns(frame: pd.DataFrame, required: Iterable[str], label: str) -> None:
    missing = sorted(set(required).difference(frame.columns))
    if missing:
        raise ValueError(f"{label} missing columns: {missing}")


def format_markdown_value(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value)


def markdown_table(rows: Sequence[dict[str, object]], columns: Sequence[str]) -> str:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        values = [format_markdown_value(row.get(column, "")) for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines) + "\n"


def write_table_outputs(
    rows: Sequence[dict[str, object]],
    output_csv: Path,
    markdown_csv: Path | None = None,
    columns: Sequence[str] | None = None,
) -> None:
    if not rows:
        raise ValueError(f"Refusing to write empty contract table: {output_csv}")
    if columns is None:
        columns = list(rows[0].keys())
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows).loc[:, list(columns)]
    frame.to_csv(output_csv, index=False)
    if markdown_csv is not None:
        markdown_csv.write_text(markdown_table(frame.to_dict(orient="records"), columns), encoding="utf-8")


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _empty_metric(row: pd.Series, *names: str) -> object:
    for name in names:
        if name in row and not pd.isna(row[name]):
            return row[name]
    return ""


def actual_split_count(combined_frame: pd.DataFrame, layout_frame: pd.DataFrame) -> int:
    if "split_seed" in combined_frame.columns:
        seeds = combined_frame["split_seed"].dropna().unique()
        if len(seeds):
            return len(seeds)
    if "count" in layout_frame.columns:
        counts = [int(value) for value in layout_frame["count"].dropna().tolist() if int(value) < 100]
        if counts:
            return max(counts)
    return 0


def load_status_payload(status_path: Path, project_root: Path) -> dict[str, object] | None:
    if not status_path.exists():
        return None
    relative = require_trace_results_path(status_path, project_root, "status JSON")
    assert_git_path_is_tracked(project_root, relative, "Status JSON")
    with status_path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    status = str(payload.get("status", "")).lower()
    if status not in {"completed", "complete"}:
        blocker = str(payload.get("blocker_reason") or payload.get("reason") or f"stage12_status.json reports {status or 'non-complete'}")
        return {"blocked": True, "blocker_reason": blocker, "payload": payload}
    return {"blocked": False, "blocker_reason": "", "payload": payload}


def paired_lookup(paired_frame: pd.DataFrame) -> dict[tuple[float, str], pd.Series]:
    selected = paired_frame[paired_frame["layout"].eq(MAIN_METHOD_LABEL)].copy()
    lookup: dict[tuple[float, str], pd.Series] = {}
    for _, row in selected.iterrows():
        lookup[(float(row["budget"]), str(row["baseline"]))] = row
    return lookup


def build_blocked_row(
    dataset: str,
    source_stage: str,
    source_dir: str,
    required_split_count: int,
    actual_count: int,
    evidence_status: str,
    blocker_reason: str,
) -> dict[str, object]:
    return {
        "dataset": dataset,
        "source_stage": source_stage,
        "source_dir": source_dir,
        "source_csv": "",
        "budget": "",
        "method_label": MAIN_METHOD_LABEL,
        "layout_type": "",
        "table_role": "dataset_gate",
        "test_mae_mean": "",
        "test_mae_std": "",
        "test_rmse_mean": "",
        "test_mape_mean": "",
        "paired_baseline": "",
        "paired_evidence_status": DESCRIPTIVE_ONLY,
        "delta_mean": "",
        "ci95_low": "",
        "ci95_high": "",
        "paired_t_p": "",
        "wilcoxon_p": "",
        "win_count": "",
        "actual_split_count": actual_count,
        "required_split_count": required_split_count,
        "evidence_status": evidence_status,
        "claim_lane": "external_evidence",
        "core_claim_eligible": False,
        "blocker_reason": blocker_reason,
    }


def build_dataset_rows(
    dataset: str,
    source_stage: str,
    source_dir: Path,
    layout_frame: pd.DataFrame,
    paired_frame: pd.DataFrame,
    required_split_count: int,
    evidence_status: str,
    core_claim_eligible: bool,
    blocker_reason: str,
) -> list[dict[str, object]]:
    require_columns(layout_frame, {"budget", "layout_type", "mean", "std", "count"}, "layout summary")
    require_columns(
        paired_frame,
        {"budget", "layout", "baseline", "delta_mean", "ci95_low", "ci95_high", "paired_t_p", "wilcoxon_p", "win_count", "count"},
        "paired statistics",
    )
    source_dir_relative = project_relative(source_dir)
    paired = paired_lookup(paired_frame)
    labels = [str(label) for label in layout_frame["layout_type"].dropna().unique()]
    budgets = sorted(float(value) for value in layout_frame["budget"].dropna().unique())
    rows: list[dict[str, object]] = []
    for budget in budgets:
        budget_frame = layout_frame[layout_frame["budget"].astype(float).eq(budget)]
        for label in labels:
            selected = budget_frame[budget_frame["layout_type"].astype(str).eq(label)]
            if selected.empty:
                continue
            layout_row = selected.iloc[0]
            paired_row = paired.get((budget, label))
            paired_status = PAIRED_STATS_AVAILABLE if paired_row is not None else DESCRIPTIVE_ONLY
            source_csv = "gls_map_layout_summary.csv"
            if paired_status == PAIRED_STATS_AVAILABLE:
                missing = [column for column in PAIRED_STAT_COLUMNS if paired_row[column] == "" or pd.isna(paired_row[column])]
                if missing:
                    raise ValueError(
                        f"paired_stats_available row missing paired statistics for {dataset} {label} at budget {budget}: {missing}"
                    )
                source_csv = "gls_map_layout_summary.csv;gls_map_paired_delta_tests.csv"
            row = {
                "dataset": dataset,
                "source_stage": source_stage,
                "source_dir": source_dir_relative,
                "source_csv": source_csv,
                "budget": budget,
                "method_label": MAIN_METHOD_LABEL,
                "layout_type": label,
                "table_role": "main_method" if label == MAIN_METHOD_LABEL else "reviewer_baseline",
                "test_mae_mean": layout_row["mean"],
                "test_mae_std": layout_row["std"],
                "test_rmse_mean": _empty_metric(layout_row, "rmse_mean", "test_rmse_mean", "rmse"),
                "test_mape_mean": _empty_metric(layout_row, "mape_mean", "test_mape_mean", "mape"),
                "paired_baseline": "" if label == MAIN_METHOD_LABEL else label,
                "paired_evidence_status": paired_status,
                "delta_mean": "" if paired_row is None else paired_row["delta_mean"],
                "ci95_low": "" if paired_row is None else paired_row["ci95_low"],
                "ci95_high": "" if paired_row is None else paired_row["ci95_high"],
                "paired_t_p": "" if paired_row is None else paired_row["paired_t_p"],
                "wilcoxon_p": "" if paired_row is None else paired_row["wilcoxon_p"],
                "win_count": "" if paired_row is None else paired_row["win_count"],
                "actual_split_count": int(layout_row["count"]) if int(layout_row["count"]) < 100 else required_split_count,
                "required_split_count": required_split_count,
                "evidence_status": evidence_status,
                "claim_lane": "external_evidence",
                "core_claim_eligible": core_claim_eligible,
                "blocker_reason": blocker_reason,
            }
            rows.append(row)
    return rows


def validate_contract_rows(rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("external evidence contract rows are empty")
    required_columns = set(EXTERNAL_EVIDENCE_COLUMNS)
    for row in rows:
        if set(row) != required_columns:
            raise ValueError(f"external evidence row has unexpected columns: {sorted(set(row))}")
        for column in ("source_dir", "source_csv"):
            assert_no_raw_dataset_path(str(row[column]), column)
        paired_status = str(row["paired_evidence_status"])
        missing_paired_stats = [column for column in PAIRED_STAT_COLUMNS if row[column] == "" or pd.isna(row[column])]
        if paired_status == PAIRED_STATS_AVAILABLE:
            if missing_paired_stats:
                raise ValueError(f"paired_stats_available row missing paired statistics: {missing_paired_stats}")
            if "gls_map_paired_delta_tests.csv" not in str(row["source_csv"]):
                raise ValueError("paired_stats_available rows must include gls_map_paired_delta_tests.csv provenance")
        elif paired_status == DESCRIPTIVE_ONLY:
            if any(not (row[column] == "" or pd.isna(row[column])) for column in PAIRED_STAT_COLUMNS):
                raise ValueError("descriptive_only row carries paired statistics")
            if "gls_map_paired_delta_tests.csv" in str(row["source_csv"]):
                raise ValueError("descriptive_only rows must not include paired-stat provenance")
        else:
            raise ValueError(f"unknown paired_evidence_status: {paired_status}")
        if row["dataset"] == "Seattle" and row["core_claim_eligible"] and (
            row["evidence_status"] != "completed" or int(row["actual_split_count"]) != REQUIRED_SPLIT_COUNT
        ):
            raise ValueError("Seattle core_claim_eligible requires complete tracked ten-split Stage12 evidence")


def build_dataset_contract(project_root: Path, spec: dict[str, object]) -> dict[str, object]:
    dataset = str(spec["dataset"])
    source_stage = str(spec["source_stage"])
    required_split_count = int(spec["required_split_count"])
    result_dir = Path(spec["result_dir"])
    if not result_dir.is_absolute():
        absolute_dir = project_root / result_dir
    else:
        absolute_dir = result_dir
    source_dir_relative = project_relative(absolute_dir, project_root)
    assert_no_raw_dataset_path(source_dir_relative, "result directory")
    if "stage11" in source_dir_relative.lower():
        blocker = "Stage11 directory cannot satisfy Stage12 10 split completion"
        row = build_blocked_row(dataset, source_stage, source_dir_relative, required_split_count, 0, "blocked", blocker)
        return {"rows": [row], "summary": dataset_summary(dataset, source_dir_relative, 0, required_split_count, "blocked", False, blocker, [])}
    if not source_dir_relative.startswith(TRACE_RESULTS_ROOT.as_posix() + "/"):
        raise ValueError(f"result directory is outside curated trace_sl_results: {source_dir_relative}")

    status_name = spec.get("status_json")
    if status_name:
        status_path = absolute_dir / str(status_name)
        status = load_status_payload(status_path, project_root)
        if status and status["blocked"]:
            blocker = str(status["blocker_reason"])
            row = build_blocked_row(dataset, source_stage, source_dir_relative, required_split_count, 0, "blocked", blocker)
            return {"rows": [row], "summary": dataset_summary(dataset, source_dir_relative, 0, required_split_count, "blocked", False, blocker, [])}

    artifact_statuses = []
    for artifact in spec["required_artifacts"]:
        path = absolute_dir / str(artifact)
        relative = project_relative(path, project_root)
        require_trace_results_path(path, project_root, "required artifact")
        artifact_statuses.append(
            {
                "path": relative,
                "exists": path.exists(),
                "tracked": is_git_path_tracked(project_root, relative) if path.exists() else False,
            }
        )
    missing = [row["path"] for row in artifact_statuses if not row["exists"]]
    if missing:
        blocker = f"missing required aggregate artifacts: {', '.join(missing)}"
        row = build_blocked_row(dataset, source_stage, source_dir_relative, required_split_count, 0, "blocked", blocker)
        return {"rows": [row], "summary": dataset_summary(dataset, source_dir_relative, 0, required_split_count, "blocked", False, blocker, artifact_statuses)}

    layout_frame = load_csv(absolute_dir / "gls_map_layout_summary.csv")
    paired_frame = load_csv(absolute_dir / "gls_map_paired_delta_tests.csv")
    combined_frame = load_csv(absolute_dir / "combined_metrics.csv")
    actual_count = actual_split_count(combined_frame, layout_frame)
    untracked = [row["path"] for row in artifact_statuses if not row["tracked"]]
    if actual_count != required_split_count:
        evidence_status = "blocked"
        complete = False
        blocker = f"expected {required_split_count} split Stage12 evidence, found {actual_count} split evidence"
    elif untracked:
        evidence_status = "pending_tracking"
        complete = False
        blocker = "required aggregate CSVs/artifacts exist but are not git-tracked: " + ", ".join(untracked)
    else:
        evidence_status = "completed"
        complete = True
        blocker = ""

    rows = build_dataset_rows(
        dataset,
        source_stage,
        absolute_dir,
        layout_frame,
        paired_frame,
        required_split_count,
        evidence_status,
        complete,
        blocker,
    )
    for row in rows:
        row["actual_split_count"] = actual_count
    validate_contract_rows(rows)
    return {"rows": rows, "summary": dataset_summary(dataset, source_dir_relative, actual_count, required_split_count, evidence_status, complete, blocker, artifact_statuses)}


def dataset_summary(
    dataset: str,
    source_dir: str,
    actual_count: int,
    required_count: int,
    evidence_status: str,
    complete: bool,
    blocker_reason: str,
    artifacts: Sequence[dict[str, object]],
) -> dict[str, object]:
    return {
        "dataset": dataset,
        "source_dir": source_dir,
        "actual_split_count": actual_count,
        "required_split_count": required_count,
        "evidence_status": evidence_status,
        "stage12_complete": complete,
        "core_claim_eligible": complete,
        "blocker_reason": blocker_reason,
        "required_artifacts": list(artifacts),
    }


def build_external_evidence_gate(dataset_summaries: Sequence[dict[str, object]]) -> dict[str, object]:
    by_dataset = {str(summary["dataset"]): summary for summary in dataset_summaries}
    pems_complete = bool(by_dataset.get("PeMS7_1026", {}).get("stage12_complete", False))
    seattle_complete = bool(by_dataset.get("Seattle", {}).get("stage12_complete", False))
    seattle_blocked = not seattle_complete
    return {
        "gate_schema": "trace_sl_external_evidence_gate_v1",
        "generated_at_utc": "1970-01-01T00:00:00Z",
        "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
        "generated_by": "scripts/generate_trace_sl_external_evidence_contracts.py",
        "required_split_count": REQUIRED_SPLIT_COUNT,
        "pems7_1026_stage12_complete": pems_complete,
        "seattle_stage12_complete": seattle_complete,
        "seattle_core_claim_blocked": seattle_blocked,
        "v1_1_completion_allowed": pems_complete and seattle_complete,
        "datasets": by_dataset,
        "policy": {
            "raw_dataset_prefix": RAW_DATASET_PREFIX,
            "raw_dataset_disposition": "protected local input only; never listed as evidence artifact",
            "stage11_disposition": "blocked for Stage12 completion",
            "pending_tracking_disposition": "aggregate evidence exists but remains incomplete until required sources are git-tracked",
            "seattle_core_policy": "Seattle core eligibility requires complete tracked ten-split Stage12 evidence and completed stage12_status.json when present",
        },
    }


def build_all_contracts(project_root: Path, output_dir: Path | None = None) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    for spec in DATASET_SPECS:
        dataset_contract = build_dataset_contract(project_root, dict(spec))
        rows.extend(dataset_contract["rows"])
        summaries.append(dataset_contract["summary"])
    validate_contract_rows(rows)
    return {
        "external_evidence_contract": rows,
        "external_evidence_gate": build_external_evidence_gate(summaries),
    }


def render_gate_markdown(gate: dict[str, object]) -> str:
    lines = [
        "# TRACE-SL External Evidence Gate",
        "",
        f"Generated by `{gate['generated_by']}` at `{gate['generated_at_utc']}`.",
        "",
        "This generated view mirrors `external_evidence_gate.json`; it is not manuscript prose.",
        "",
        "## Gate Status",
        "",
        f"- PeMS7_1026 Stage12 complete: `{gate['pems7_1026_stage12_complete']}`",
        f"- Seattle Stage12 complete: `{gate['seattle_stage12_complete']}`",
        f"- Seattle core claim blocked: `{gate['seattle_core_claim_blocked']}`",
        f"- v1.1 completion allowed: `{gate['v1_1_completion_allowed']}`",
        "",
        "## Dataset Status",
        "",
        "| Dataset | Evidence status | Actual splits | Required splits | Core eligible | Blocker |",
        "|---|---|---:|---:|---:|---|",
    ]
    for summary in gate["datasets"].values():
        lines.append(
            "| {dataset} | {status} | {actual} | {required} | {eligible} | {blocker} |".format(
                dataset=summary["dataset"],
                status=summary["evidence_status"],
                actual=summary["actual_split_count"],
                required=summary["required_split_count"],
                eligible=summary["core_claim_eligible"],
                blocker=summary["blocker_reason"],
            )
        )
    lines.extend(
        [
            "",
            "## Raw Dataset Hygiene",
            "",
            f"- Raw dataset prefix: `{gate['policy']['raw_dataset_prefix']}`",
            f"- Disposition: {gate['policy']['raw_dataset_disposition']}",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_readme(output_dir: Path) -> None:
    readme = output_dir / "README.md"
    existing = readme.read_text(encoding="utf-8") if readme.exists() else "# TRACE-SL paper source tables\n\n"
    external_block = (
        "\n## External Stage12 Evidence Sources\n\n"
        "Regenerate external evidence contracts from the repository root with:\n\n"
        "```bash\n"
        "python scripts/generate_trace_sl_external_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources\n"
        "```\n\n"
        "Generated files:\n\n"
        "- `external_evidence_contract.csv` / `external_evidence_contract.json` / `external_evidence_contract.md`: Phase 8 external Stage12 evidence rows with split counts, tracking provenance, paired-stat honesty, and blocker status.\n"
        "- `external_evidence_gate.json` / `external_evidence_gate.md`: machine-checkable PeMS7_1026 and Seattle Stage12 completion gate; completed gates support bounded external empirical discussion and still block universal cross-network generalization claims.\n\n"
        "Raw traffic datasets under `TRC-23-02333/dataset/` are protected local inputs and are not evidence artifacts.\n"
    )
    marker = "## External Stage12 Evidence Sources"
    if marker in existing:
        existing = existing.split(marker, 1)[0].rstrip() + "\n"
    readme.write_text(existing.rstrip() + "\n" + external_block, encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=TRACE_RESULTS_ROOT / "paper_sources",
        help="Output directory, relative to project root unless absolute.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    project_root = args.project_root.resolve()
    output_dir = resolve_output_dir(project_root, args.output_dir)
    contracts = build_all_contracts(project_root, output_dir)
    write_table_outputs(
        contracts["external_evidence_contract"],
        output_dir / "external_evidence_contract.csv",
        output_dir / "external_evidence_contract.md",
        EXTERNAL_EVIDENCE_COLUMNS,
    )
    write_json(output_dir / "external_evidence_contract.json", {"external_evidence_contract": contracts["external_evidence_contract"]})
    write_json(output_dir / "external_evidence_gate.json", contracts["external_evidence_gate"])
    (output_dir / "external_evidence_gate.md").write_text(render_gate_markdown(contracts["external_evidence_gate"]), encoding="utf-8")
    write_readme(output_dir)
    print(f"wrote external_evidence_contract: {len(contracts['external_evidence_contract'])} rows")
    print(f"paper sources: {project_relative(output_dir, project_root)}")


if __name__ == "__main__":
    main()
