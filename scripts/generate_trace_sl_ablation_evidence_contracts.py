#!/usr/bin/env python3
"""Generate TRACE-SL ablation and dataset-classification evidence contracts."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd


TRACE_RESULTS_ROOT = Path("TRC-23-02333/trace_sl_results")
PAPER_SOURCES_DIR = TRACE_RESULTS_ROOT / "paper_sources"
CORE_STAGE12_DIR = TRACE_RESULTS_ROOT / "pems7_228_stage12_baseline_portfolio"
EXTERNAL_GATE_PATH = PAPER_SOURCES_DIR / "external_evidence_gate.json"
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
REQUIRED_SPLIT_COUNT = 10
MAIN_METHOD_LABEL = "validation_swap_selected"
LOW_BUDGET_MULTISTART_CAVEAT_TAG = "pems7_228_low_budget_multistart_not_dominant"
PAIRED_STAT_COLUMNS = ("delta_mean", "ci95_low", "ci95_high", "paired_t_p", "wilcoxon_p", "win_count")
PAIRED_STATS_AVAILABLE = "paired_stats_available"
DESCRIPTIVE_ONLY = "descriptive_only"

REQUIRED_ABLATION_LAYOUTS = (
    "random",
    "best_random_by_validation",
    "greedy_a_trace",
    "rcss_selected",
    "validation_swap_selected",
    "multistart_swap_by_validation",
)
OPTIONAL_ABLATION_LAYOUTS = (
    "greedy_d_logdet",
    "top_variance",
    "graph_sampling_laplacian",
    "observability_proxy",
    "qr_pod_modes",
    "scenario_cvar_a_trace",
)

ABLATION_CONTRACT_COLUMNS = (
    "dataset",
    "source_stage",
    "source_dir",
    "source_csv",
    "budget",
    "method_label",
    "layout_type",
    "component_layer",
    "supported_question",
    "comparison_target",
    "table_role",
    "evidence_basis",
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
    "paired_evidence_status_detail",
    "claim_route",
    "caveat_tag",
    "provenance",
)

DATASET_CLASSIFICATION_COLUMNS = (
    "dataset",
    "evid_requirement",
    "evidence_class",
    "evidence_lane",
    "evidence_status",
    "allowed_use",
    "blocked_use",
    "required_upgrade",
    "actual_split_count",
    "required_split_count",
    "held_out_test_status",
    "paired_evidence_status",
    "gate_stage12_complete",
    "core_claim_eligible",
    "requirement_complete",
    "claim_route",
    "blocker_reason",
    "provenance",
)


class AblationEvidenceValidationError(ValueError):
    """Raised when Phase 9 ablation evidence policy is violated."""


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


def resolve_output_dir(project_root: Path, output_dir: Path | None) -> Path:
    if output_dir is None:
        output_dir = PAPER_SOURCES_DIR
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


def is_git_path_tracked(project_root: Path, relative: str) -> bool:
    result = subprocess.run(
        ["git", "-C", str(project_root), "ls-files", "--error-unmatch", relative],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def assert_git_path_is_tracked(project_root: Path, relative: str, label: str) -> None:
    if not is_git_path_tracked(project_root, relative):
        raise ValueError(f"{label} is not committed/tracked by git: {relative}")


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected aggregate CSV not found: {path}")
    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError(f"Expected nonempty aggregate CSV: {path}")
    return frame


def load_json(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"Expected JSON artifact not found: {path}")
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected object JSON payload: {path}")
    return payload


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


def _budget_requires_caveat(budget: object) -> bool:
    try:
        return abs(float(budget) - 0.1) < 1e-9
    except (TypeError, ValueError):
        return False


def _paired_lookup(paired_frame: pd.DataFrame) -> dict[tuple[float, str], pd.Series]:
    selected = paired_frame[paired_frame["layout"].astype(str).eq(MAIN_METHOD_LABEL)].copy()
    lookup: dict[tuple[float, str], pd.Series] = {}
    for _, row in selected.iterrows():
        lookup[(float(row["budget"]), str(row["baseline"]))] = row
    return lookup


def _actual_split_count(layout_row: pd.Series, required_split_count: int) -> int:
    if "count" not in layout_row or pd.isna(layout_row["count"]):
        return 0
    count = int(layout_row["count"])
    if count > required_split_count and str(layout_row.get("layout_type", "")) == "random":
        return required_split_count
    return count


def component_metadata(layout_type: str) -> dict[str, str]:
    if layout_type == "random":
        return {
            "component_layer": "random_baseline_pool",
            "supported_question": "How does an unselected random sensor pool perform on held-out test reconstruction?",
            "comparison_target": "validation_swap_selected",
            "claim_route": "core_in_domain_ablation_baseline",
        }
    if layout_type == "best_random_by_validation":
        return {
            "component_layer": "validation_based_candidate_selection",
            "supported_question": "Does validation selection improve over random mean candidates without claiming validation MAE as test evidence?",
            "comparison_target": "random",
            "claim_route": "core_in_domain_ablation_selection",
        }
    if layout_type in {"greedy_a_trace", "greedy_d_logdet", "scenario_cvar_a_trace"}:
        return {
            "component_layer": "certificate_candidate_generation",
            "supported_question": "What does certificate-only candidate generation contribute before validation selection and swap refinement?",
            "comparison_target": "validation_swap_selected",
            "claim_route": "core_in_domain_ablation_certificate_guided",
        }
    if layout_type == "rcss_selected":
        return {
            "component_layer": "validation_based_candidate_selection",
            "supported_question": "What does RCSS validation/certificate candidate selection contribute before local refinement?",
            "comparison_target": "validation_swap_selected",
            "claim_route": "core_in_domain_ablation_rcss_selection",
        }
    if layout_type == "validation_swap_selected":
        return {
            "component_layer": "validation_aware_local_refinement",
            "supported_question": "What is the final validation-aware local refinement performance on held-out test evidence?",
            "comparison_target": "reviewer_baselines",
            "claim_route": "core_in_domain_main_method",
        }
    if layout_type == "multistart_swap_by_validation":
        return {
            "component_layer": "validation_aware_local_refinement",
            "supported_question": "Does a multistart validation-swap comparator qualify the low-budget TRACE-SL caveat?",
            "comparison_target": "validation_swap_selected",
            "claim_route": "core_in_domain_multistart_caveat",
        }
    return {
        "component_layer": "reviewer_baseline",
        "supported_question": "How does a reviewer-facing baseline compare on held-out test reconstruction?",
        "comparison_target": "validation_swap_selected",
        "claim_route": "core_in_domain_ablation_baseline",
    }


def validate_ablation_rows(rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("ablation contract rows are empty")
    required_columns = set(ABLATION_CONTRACT_COLUMNS)
    labels = {str(row["layout_type"]) for row in rows}
    missing = sorted(set(REQUIRED_ABLATION_LAYOUTS).difference(labels))
    if missing:
        raise ValueError(f"missing required layout_type rows: {missing}")
    for row in rows:
        if set(row) != required_columns:
            raise ValueError(f"ablation row has unexpected columns: {sorted(set(row))}")
        rendered = json.dumps(row, sort_keys=True, default=str)
        assert_no_raw_dataset_path(rendered, "ablation row")
        if row["evidence_basis"] == "validation_mae":
            raise ValueError("validation MAE cannot be marked as held-out test evidence")
        paired_status = str(row["paired_evidence_status"])
        missing_paired_stats = [column for column in PAIRED_STAT_COLUMNS if row[column] == "" or pd.isna(row[column])]
        if paired_status == PAIRED_STATS_AVAILABLE:
            if missing_paired_stats:
                raise ValueError(f"paired_stats_available row missing paired statistics: {missing_paired_stats}")
            if "gls_map_paired_delta_tests.csv" not in str(row["source_csv"]):
                raise ValueError("paired_stats_available rows must include paired-stat provenance")
        elif paired_status == DESCRIPTIVE_ONLY:
            if any(not (row[column] == "" or pd.isna(row[column])) for column in PAIRED_STAT_COLUMNS):
                raise ValueError("descriptive_only row carries paired statistics")
        else:
            raise ValueError(f"unknown paired_evidence_status: {paired_status}")
        if _budget_requires_caveat(row["budget"]) and row["caveat_tag"] != LOW_BUDGET_MULTISTART_CAVEAT_TAG:
            raise ValueError(f"10% rows must carry {LOW_BUDGET_MULTISTART_CAVEAT_TAG}")
        if row["layout_type"] == "multistart_swap_by_validation" and row["caveat_tag"] != LOW_BUDGET_MULTISTART_CAVEAT_TAG:
            raise ValueError(f"multistart rows must carry {LOW_BUDGET_MULTISTART_CAVEAT_TAG}")


def build_ablation_contract(project_root: Path) -> list[dict[str, object]]:
    source_dir = project_root / CORE_STAGE12_DIR
    layout_csv = source_dir / "gls_map_layout_summary.csv"
    paired_csv = source_dir / "gls_map_paired_delta_tests.csv"
    for path in (layout_csv, paired_csv):
        relative = require_trace_results_path(path, project_root, "core ablation source")
        assert_git_path_is_tracked(project_root, relative, "Core ablation source")
    layout_frame = load_csv(layout_csv)
    paired_frame = load_csv(paired_csv)
    require_columns(layout_frame, {"budget", "layout_type", "mean", "std", "count"}, "core ablation layout summary")
    require_columns(
        paired_frame,
        {"budget", "layout", "baseline", "delta_mean", "ci95_low", "ci95_high", "paired_t_p", "wilcoxon_p", "win_count", "count"},
        "core ablation paired statistics",
    )
    available_labels = {str(value) for value in layout_frame["layout_type"].dropna().unique()}
    missing = sorted(set(REQUIRED_ABLATION_LAYOUTS).difference(available_labels))
    if missing:
        raise ValueError(f"missing required layout_type rows: {missing}")
    labels = [label for label in (*REQUIRED_ABLATION_LAYOUTS, *OPTIONAL_ABLATION_LAYOUTS) if label in available_labels]
    paired = _paired_lookup(paired_frame)
    source_dir_relative = project_relative(source_dir, project_root)
    rows: list[dict[str, object]] = []
    for budget in sorted(float(value) for value in layout_frame["budget"].dropna().unique()):
        budget_frame = layout_frame[layout_frame["budget"].astype(float).eq(budget)]
        for label in labels:
            selected = budget_frame[budget_frame["layout_type"].astype(str).eq(label)]
            if selected.empty:
                continue
            layout_row = selected.iloc[0]
            paired_row = paired.get((budget, label))
            paired_status = PAIRED_STATS_AVAILABLE if paired_row is not None else DESCRIPTIVE_ONLY
            source_csv = layout_csv.name
            if paired_status == PAIRED_STATS_AVAILABLE:
                missing_stats = [column for column in PAIRED_STAT_COLUMNS if paired_row[column] == "" or pd.isna(paired_row[column])]
                if missing_stats:
                    raise ValueError(f"paired_stats_available row missing paired statistics for {label} at budget {budget}: {missing_stats}")
                source_csv = f"{layout_csv.name};{paired_csv.name}"
            caveat = ""
            if _budget_requires_caveat(budget) or label == "multistart_swap_by_validation":
                caveat = LOW_BUDGET_MULTISTART_CAVEAT_TAG
            component = component_metadata(label)
            provenance = f"{source_dir_relative}/{source_csv}"
            row: dict[str, object] = {
                "dataset": "PeMS7_228",
                "source_stage": "stage12_baseline_portfolio",
                "source_dir": source_dir_relative,
                "source_csv": source_csv,
                "budget": budget,
                "method_label": MAIN_METHOD_LABEL,
                "layout_type": label,
                "component_layer": component["component_layer"],
                "supported_question": component["supported_question"],
                "comparison_target": component["comparison_target"],
                "table_role": "main_method" if label == MAIN_METHOD_LABEL else "ablation_component",
                "evidence_basis": "held_out_test_aggregate",
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
                "actual_split_count": _actual_split_count(layout_row, REQUIRED_SPLIT_COUNT),
                "required_split_count": REQUIRED_SPLIT_COUNT,
                "evidence_status": "completed",
                "paired_evidence_status_detail": "held-out paired statistics available" if paired_status == PAIRED_STATS_AVAILABLE else "layout-summary evidence only",
                "claim_route": component["claim_route"],
                "caveat_tag": caveat,
                "provenance": provenance,
            }
            rows.append(row)
    validate_ablation_rows(rows)
    return rows


def load_external_gate(project_root: Path) -> dict[str, object]:
    gate_path = project_root / EXTERNAL_GATE_PATH
    relative = require_trace_results_path(gate_path, project_root, "external evidence gate")
    assert_git_path_is_tracked(project_root, relative, "External evidence gate")
    gate = load_json(gate_path)
    snapshot = {
        "pems7_1026_stage12_complete": bool(gate.get("pems7_1026_stage12_complete", False)),
        "seattle_stage12_complete": bool(gate.get("seattle_stage12_complete", False)),
        "seattle_core_claim_blocked": bool(gate.get("seattle_core_claim_blocked", True)),
        "v1_1_completion_allowed": bool(gate.get("v1_1_completion_allowed", False)),
    }
    for key, value in snapshot.items():
        gate[key] = value
    return gate


def _gate_dataset(gate: dict[str, object], dataset: str) -> dict[str, object]:
    datasets = gate.get("datasets", {})
    if isinstance(datasets, dict):
        value = datasets.get(dataset, {})
        if isinstance(value, dict):
            return value
    return {}


def _classification_row(
    dataset: str,
    evid_requirement: str,
    evidence_class: str,
    evidence_lane: str,
    evidence_status: str,
    allowed_use: str,
    blocked_use: str,
    required_upgrade: str,
    actual_split_count: int,
    required_split_count: int,
    held_out_test_status: str,
    paired_evidence_status: str,
    gate_stage12_complete: bool,
    core_claim_eligible: bool,
    requirement_complete: bool,
    claim_route: str,
    blocker_reason: str,
    provenance: str,
) -> dict[str, object]:
    row = {
        "dataset": dataset,
        "evid_requirement": evid_requirement,
        "evidence_class": evidence_class,
        "evidence_lane": evidence_lane,
        "evidence_status": evidence_status,
        "allowed_use": allowed_use,
        "blocked_use": blocked_use,
        "required_upgrade": required_upgrade,
        "actual_split_count": actual_split_count,
        "required_split_count": required_split_count,
        "held_out_test_status": held_out_test_status,
        "paired_evidence_status": paired_evidence_status,
        "gate_stage12_complete": gate_stage12_complete,
        "core_claim_eligible": core_claim_eligible,
        "requirement_complete": requirement_complete,
        "claim_route": claim_route,
        "blocker_reason": blocker_reason,
        "provenance": provenance,
    }
    for value in row.values():
        assert_no_raw_dataset_path(str(value), "dataset classification row")
    return row


def build_dataset_classification(project_root: Path) -> list[dict[str, object]]:
    gate = load_external_gate(project_root)
    pems_summary = _gate_dataset(gate, "PeMS7_1026")
    seattle_summary = _gate_dataset(gate, "Seattle")
    pems_complete = bool(gate.get("pems7_1026_stage12_complete", False))
    seattle_complete = bool(gate.get("seattle_stage12_complete", False))
    seattle_blocked = bool(gate.get("seattle_core_claim_blocked", True))
    pems_actual = int(pems_summary.get("actual_split_count", 0) or 0)
    seattle_actual = int(seattle_summary.get("actual_split_count", 0) or 0)
    pems_blocker = str(pems_summary.get("blocker_reason", "") or "Stage11, DRY_RUN, or one-seed Stage12 feasibility artifacts are non-evidence for EVID-03 completion")
    if not pems_complete and "non-evidence" not in pems_blocker:
        pems_blocker = f"{pems_blocker}; Stage11, DRY_RUN, and one-seed feasibility outputs are non-evidence for EVID-03 completion".strip("; ")
    seattle_blocker = str(seattle_summary.get("blocker_reason", "") or "Seattle Stage12 ten-split gate is incomplete")
    if not seattle_complete and "non-evidence" not in seattle_blocker:
        seattle_blocker = f"{seattle_blocker}; one-seed feasibility outputs are non-evidence for EVID-04 completion".strip("; ")
    rows = [
        _classification_row(
            "PeMS7_228",
            "EVID-01/ABLT-01",
            "core",
            "core",
            "completed",
            "core in-domain ablation and main-table evidence where held-out Stage12 aggregates support the row",
            "external generalization or global robustness claims",
            "none for Phase 9 ablation contract",
            REQUIRED_SPLIT_COUNT,
            REQUIRED_SPLIT_COUNT,
            "held_out_test_aggregate",
            PAIRED_STATS_AVAILABLE,
            True,
            True,
            True,
            "core_in_domain",
            "",
            (CORE_STAGE12_DIR / "gls_map_layout_summary.csv").as_posix(),
        ),
        _classification_row(
            "PeMS7_1026",
            "EVID-03",
            "external" if pems_complete else "conditional",
            "external" if pems_complete else "conditional",
            "completed" if pems_complete else str(pems_summary.get("evidence_status", "blocked") or "blocked"),
            "external/supporting PeMS discussion only until tracked ten-split Stage12 evidence exists",
            "core claim support or EVID-03 completion from Stage11, DRY_RUN, or one-seed feasibility artifacts",
            "tracked Stage12 baseline portfolio with exactly ten splits and reviewer-facing aggregate artifacts",
            pems_actual,
            int(pems_summary.get("required_split_count", REQUIRED_SPLIT_COUNT) or REQUIRED_SPLIT_COUNT),
            "held_out_test_aggregate" if pems_complete else "non_completing_stage11_or_feasibility",
            PAIRED_STATS_AVAILABLE if pems_complete else DESCRIPTIVE_ONLY,
            pems_complete,
            pems_complete,
            pems_complete,
            "external_supporting_until_gate_complete",
            pems_blocker if not pems_complete else "",
            str(pems_summary.get("source_dir", TRACE_RESULTS_ROOT / "pems7_1026_stage12_baseline_portfolio")),
        ),
        _classification_row(
            "Seattle",
            "EVID-04",
            "conditional" if seattle_blocked else "external",
            "conditional" if seattle_blocked else "external",
            "completed" if seattle_complete else str(seattle_summary.get("evidence_status", "blocked") or "blocked"),
            "external/transfer-style support only after complete tracked ten-split Stage12 evidence",
            "core claims while external_evidence_gate or stage12_status.json reports incomplete evidence",
            "completed tracked Seattle Stage12 ten-split aggregate artifacts and completed stage12_status.json",
            seattle_actual,
            int(seattle_summary.get("required_split_count", REQUIRED_SPLIT_COUNT) or REQUIRED_SPLIT_COUNT),
            "held_out_test_aggregate" if seattle_complete else "non_completing_feasibility_or_blocked_status",
            PAIRED_STATS_AVAILABLE if seattle_complete else DESCRIPTIVE_ONLY,
            seattle_complete,
            seattle_complete and not seattle_blocked,
            seattle_complete and not seattle_blocked,
            "blocked_from_core_until_gate_complete",
            seattle_blocker if not seattle_complete or seattle_blocked else "",
            str(seattle_summary.get("source_dir", TRACE_RESULTS_ROOT / "seattle_stage12_baseline_portfolio")),
        ),
        _classification_row(
            "Robustness stress tests",
            "ABLT-04",
            "appendix-only",
            "appendix-only",
            "supporting_stress_test",
            "appendix or bounded stress-test evidence for tested perturbations",
            "global robustness claims or core dataset elevation without multi-seed perturbation evidence",
            "multi-seed perturbation evidence before any stronger robustness claim route",
            0,
            REQUIRED_SPLIT_COUNT,
            "stress_test_only",
            DESCRIPTIVE_ONLY,
            False,
            False,
            True,
            "appendix_or_supporting_stress_test",
            "robustness evidence remains stress-test or appendix-only unless multi-seed perturbation evidence is added",
            (TRACE_RESULTS_ROOT / "pems7_228_stage14_robustness").as_posix(),
        ),
    ]
    validate_dataset_classification(rows)
    return rows


def validate_dataset_classification(rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("dataset classification rows are empty")
    required_columns = set(DATASET_CLASSIFICATION_COLUMNS)
    by_dataset = {str(row["dataset"]): row for row in rows}
    for dataset in ("PeMS7_228", "PeMS7_1026", "Seattle", "Robustness stress tests"):
        if dataset not in by_dataset:
            raise ValueError(f"missing dataset classification row: {dataset}")
    for row in rows:
        if set(row) != required_columns:
            raise ValueError(f"dataset classification row has unexpected columns: {sorted(set(row))}")
        rendered = json.dumps(row, sort_keys=True, default=str)
        assert_no_raw_dataset_path(rendered, "dataset classification row")
        if row["dataset"] in {"PeMS7_1026", "Seattle"} and not bool(row["gate_stage12_complete"]):
            if bool(row["requirement_complete"]) or bool(row["core_claim_eligible"]):
                raise ValueError(f"{row['dataset']} cannot complete requirement or become core eligible while gate is incomplete")
        if row["dataset"] == "Seattle" and row["evidence_lane"] == "core":
            raise ValueError("Seattle is blocked from core evidence classification in Phase 9")
        if row["dataset"] == "Robustness stress tests" and row["evidence_lane"] not in {"supporting", "appendix-only"}:
            raise ValueError("robustness evidence must remain supporting or appendix-only")


def build_metadata(
    ablation_rows: Sequence[dict[str, object]],
    classification_rows: Sequence[dict[str, object]],
    gate: dict[str, object],
) -> dict[str, object]:
    snapshot_keys = (
        "pems7_1026_stage12_complete",
        "seattle_stage12_complete",
        "seattle_core_claim_blocked",
        "v1_1_completion_allowed",
    )
    source_artifacts = sorted(
        {
            str(row["provenance"])
            for row in (*ablation_rows, *classification_rows)
            if not str(row["provenance"]).startswith(RAW_DATASET_PREFIX)
        }
    )
    return {
        "schema": "trace_sl_ablation_evidence_contracts_v1",
        "generated_at_utc": "1970-01-01T00:00:00Z",
        "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
        "generated_by": "scripts/generate_trace_sl_ablation_evidence_contracts.py",
        "row_counts": {
            "ablation_contract": len(ablation_rows),
            "dataset_evidence_classification": len(classification_rows),
        },
        "required_ablation_layouts": list(REQUIRED_ABLATION_LAYOUTS),
        "status_vocabulary": ["completed", "blocked", "conditional", "supporting_stress_test", "pending_tracking"],
        "external_gate_snapshot": {key: bool(gate.get(key, False)) for key in snapshot_keys},
        "source_artifacts": source_artifacts,
        "policy": {
            "raw_dataset_prefix": RAW_DATASET_PREFIX,
            "raw_dataset_disposition": "protected local input only; never listed as evidence artifact",
            "validation_mae_disposition": "selection evidence only; never marked as held-out test evidence",
            "stage11_and_feasibility_disposition": "non-evidence for EVID-03/EVID-04 ten-split completion",
            "seattle_core_policy": "blocked from core until external gate and status artifacts report complete tracked ten-split Stage12 evidence",
        },
    }


def build_all_contracts(project_root: Path, output_dir: Path | None = None) -> dict[str, object]:
    del output_dir
    gate = load_external_gate(project_root)
    ablation_rows = build_ablation_contract(project_root)
    classification_rows = build_dataset_classification(project_root)
    metadata = build_metadata(ablation_rows, classification_rows, gate)
    return {
        "ablation_contract": ablation_rows,
        "dataset_evidence_classification": classification_rows,
        "metadata": metadata,
    }


def render_contract_index(metadata: dict[str, object]) -> str:
    return (
        "# TRACE-SL Phase 9 Ablation Evidence Contracts\n\n"
        f"Generated by `{metadata['generated_by']}` at `{metadata['generated_at_utc']}`.\n\n"
        "This generated view mirrors the CSV/JSON contracts; it is not manuscript prose.\n\n"
        "## Row Counts\n\n"
        f"- Ablation contract rows: `{metadata['row_counts']['ablation_contract']}`\n"
        f"- Dataset classification rows: `{metadata['row_counts']['dataset_evidence_classification']}`\n\n"
        "## Policy\n\n"
        f"- Raw dataset prefix: `{metadata['policy']['raw_dataset_prefix']}`\n"
        f"- Validation MAE: {metadata['policy']['validation_mae_disposition']}\n"
        f"- Stage11/feasibility: {metadata['policy']['stage11_and_feasibility_disposition']}\n"
    )


def write_readme(output_dir: Path) -> None:
    readme = output_dir / "README.md"
    existing = readme.read_text(encoding="utf-8") if readme.exists() else "# TRACE-SL paper source tables\n\n"
    block = (
        "\n## Phase 9 Ablation and Dataset Classification Sources\n\n"
        "Regenerate Phase 9 ablation contracts from the repository root with:\n\n"
        "```bash\n"
        "python scripts/generate_trace_sl_ablation_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources\n"
        "```\n\n"
        "Generated files:\n\n"
        "- `ablation_contract.csv` / `ablation_contract.json` / `ablation_contract.md`: Phase 9 ablation rows with layer, question, held-out evidence basis, paired-stat honesty, and caveat routing.\n"
        "- `dataset_evidence_classification.csv` / `dataset_evidence_classification.json` / `dataset_evidence_classification.md`: dataset evidence lanes and fail-closed EVID-03/EVID-04 status classification.\n\n"
        "Raw traffic datasets under `TRC-23-02333/dataset/` are protected local inputs and are not evidence artifacts.\n"
    )
    marker = "## Phase 9 Ablation and Dataset Classification Sources"
    if marker in existing:
        existing = existing.split(marker, 1)[0].rstrip() + "\n"
    readme.write_text(existing.rstrip() + "\n" + block, encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PAPER_SOURCES_DIR,
        help="Output directory, relative to project root unless absolute.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    project_root = args.project_root.resolve()
    output_dir = resolve_output_dir(project_root, args.output_dir)
    contracts = build_all_contracts(project_root, output_dir)
    write_table_outputs(
        contracts["ablation_contract"],
        output_dir / "ablation_contract.csv",
        output_dir / "ablation_contract.md",
        ABLATION_CONTRACT_COLUMNS,
    )
    write_json(
        output_dir / "ablation_contract.json",
        {
            "schema": "trace_sl_ablation_contract_v1",
            "metadata": contracts["metadata"],
            "ablation_contract": contracts["ablation_contract"],
        },
    )
    write_table_outputs(
        contracts["dataset_evidence_classification"],
        output_dir / "dataset_evidence_classification.csv",
        output_dir / "dataset_evidence_classification.md",
        DATASET_CLASSIFICATION_COLUMNS,
    )
    write_json(
        output_dir / "dataset_evidence_classification.json",
        {
            "schema": "trace_sl_dataset_evidence_classification_v1",
            "metadata": contracts["metadata"],
            "dataset_evidence_classification": contracts["dataset_evidence_classification"],
        },
    )
    write_readme(output_dir)
    print(f"wrote ablation_contract: {len(contracts['ablation_contract'])} rows")
    print(f"wrote dataset_evidence_classification: {len(contracts['dataset_evidence_classification'])} rows")
    print(f"paper sources: {project_relative(output_dir, project_root)}")


if __name__ == "__main__":
    main()
