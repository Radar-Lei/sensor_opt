#!/usr/bin/env python3
"""Generate deterministic TRACE-SL claim and main-table contracts."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd


TRACE_RESULTS_ROOT = Path("TRC-23-02333/trace_sl_results")
STAGE12_DIR = TRACE_RESULTS_ROOT / "pems7_228_stage12_baseline_portfolio"
SOURCE_COLUMNS = ("source_stage", "source_dir", "source_csv")

FORBIDDEN_WORDING = (
    "optimal",
    "certified",
    "globally robust",
    "guaranteed MAE improvement",
    "generalizes across networks",
)
BOUNDED_ALLOWED_WORDING = (
    "certificate-guided",
    "posterior-certificate-aware",
    "stress-tested",
    "improves in the tested setting",
    "external evidence",
)
LOW_BUDGET_MULTISTART_CAVEAT_TAG = "pems7_228_low_budget_multistart_not_dominant"
MAIN_METHOD_LABEL = "validation_swap_selected"
MAIN_TABLE_LAYOUT_LABELS = (
    "validation_swap_selected",
    "multistart_swap_by_validation",
    "rcss_selected",
    "best_random_by_validation",
    "random",
    "top_variance",
    "greedy_a_trace",
    "graph_sampling_laplacian",
    "observability_proxy",
    "qr_pod_modes",
)
SECONDARY_CERTIFICATE_BASELINE = "greedy_d_logdet"

CLAIM_CONTRACT_COLUMNS = (
    "source_stage",
    "source_dir",
    "source_csv",
    "claim_id",
    "claim_lane",
    "claim_status",
    "allowed_wording",
    "forbidden_wording",
    "evidence_source",
    "evidence_artifact",
    "required_metric_basis",
    "required_caveat_tag",
    "phase_scope",
    "notes",
)
MAIN_TABLE_CONTRACT_COLUMNS = (
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
    "delta_mean",
    "ci95_low",
    "ci95_high",
    "paired_t_p",
    "wilcoxon_p",
    "win_count",
    "split_count",
    "caveat_tag",
    "claim_lane",
)


class ContractValidationError(ValueError):
    """Raised when generated claim/table contracts violate Phase 7 policy."""


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


def source_metadata(source_stage: str, source_dir: Path, source_csv: Path) -> dict[str, str]:
    return {
        "source_stage": source_stage,
        "source_dir": project_relative(source_dir),
        "source_csv": source_csv.name,
    }


def evidence_metadata(source_stage: str, evidence_artifact: str) -> dict[str, str]:
    artifact_path = Path(evidence_artifact)
    return {
        "source_stage": source_stage,
        "source_dir": artifact_path.parent.as_posix(),
        "source_csv": artifact_path.name,
    }


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected aggregate CSV not found: {path}")
    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError(f"Expected nonempty aggregate CSV: {path}")
    return frame


def rows_from_frame(
    frame: pd.DataFrame,
    source_stage: str,
    source_dir: Path,
    source_csv: Path,
    columns: Sequence[str] | None = None,
) -> list[dict[str, object]]:
    if columns is None:
        columns = [column for column in frame.columns if column not in SOURCE_COLUMNS]
    metadata = source_metadata(source_stage, source_dir, source_csv)
    rows: list[dict[str, object]] = []
    for raw_row in frame.loc[:, list(columns)].to_dict(orient="records"):
        row = dict(metadata)
        row.update(raw_row)
        rows.append(row)
    return rows


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


def assert_git_path_is_tracked(project_root: Path, relative: str, label: str) -> None:
    result = subprocess.run(
        ["git", "-C", str(project_root), "ls-files", "--error-unmatch", relative],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"{label} is not committed/tracked by git: {relative}")


def assert_source_is_tracked(project_root: Path, source: Path) -> None:
    relative = project_relative(source, project_root)
    if relative.startswith("TRC-23-02333/dataset/") or not relative.startswith(TRACE_RESULTS_ROOT.as_posix() + "/"):
        raise ValueError(f"Source is outside curated trace_sl_results: {relative}")
    assert_git_path_is_tracked(project_root, relative, "Source CSV")


def assert_evidence_artifact_is_tracked(project_root: Path, artifact: str) -> None:
    if not artifact:
        return
    if artifact.startswith("TRC-23-02333/dataset/"):
        raise ValueError(f"Evidence artifact references raw dataset path: {artifact}")
    if artifact.startswith(TRACE_RESULTS_ROOT.as_posix() + "/") or artifact.startswith(".planning/"):
        assert_git_path_is_tracked(project_root, artifact, "Evidence artifact")
        return
    raise ValueError(f"Evidence artifact is outside curated contract roots: {artifact}")


def resolve_output_dir(project_root: Path, output_dir: Path) -> Path:
    if output_dir.is_absolute():
        return output_dir
    return project_root / output_dir


def require_columns(frame: pd.DataFrame, required: Iterable[str], label: str) -> None:
    missing = sorted(set(required).difference(frame.columns))
    if missing:
        raise ValueError(f"{label} missing columns: {missing}")


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


def _claim_row(
    metadata: dict[str, str],
    claim_id: str,
    claim_lane: str,
    claim_status: str,
    allowed_wording: str,
    forbidden_wording: str,
    evidence_source: str,
    evidence_artifact: str,
    required_metric_basis: str,
    required_caveat_tag: str,
    phase_scope: str,
    notes: str,
) -> dict[str, object]:
    row: dict[str, object] = dict(metadata)
    row.update(
        {
            "claim_id": claim_id,
            "claim_lane": claim_lane,
            "claim_status": claim_status,
            "allowed_wording": allowed_wording,
            "forbidden_wording": forbidden_wording,
            "evidence_source": evidence_source,
            "evidence_artifact": evidence_artifact,
            "required_metric_basis": required_metric_basis,
            "required_caveat_tag": required_caveat_tag,
            "phase_scope": phase_scope,
            "notes": notes,
        }
    )
    return row


def build_claim_contract_rows(stage12_dir: Path, layout_csv: Path, paired_csv: Path) -> list[dict[str, object]]:
    layout_artifact = project_relative(layout_csv)
    paired_artifact = project_relative(paired_csv)
    pems7_1026_artifact = "TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/gls_map_layout_summary.csv"
    robustness_layout_artifact = "TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_layout_summary.csv"
    robustness_summary_artifact = "TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/SUMMARY.md"
    rows = [
        _claim_row(
            evidence_metadata("stage12_baseline_portfolio", layout_artifact),
            "CLAIM-01",
            "core_in_domain",
            "transportation_science_ready",
            "certificate-guided",
            "",
            "PeMS7_228 Stage12 baseline portfolio",
            layout_artifact,
            "held_out_test_with_paired_comparisons",
            LOW_BUDGET_MULTISTART_CAVEAT_TAG,
            "phase7_core",
            "transparent reconstruction-aware sparse sensor layout design with validation-swap-selected main method",
        ),
        _claim_row(
            evidence_metadata("phase7_claim_policy", ".planning/REQUIREMENTS.md"),
            "CLAIM-02",
            "tr_part_b_extension",
            "requires_stronger_theory",
            "posterior-certificate-aware",
            "",
            "Theory extension",
            ".planning/REQUIREMENTS.md",
            "theory_or_bound_required_before_elevation",
            "",
            "phase7_boundary",
            "formal certification, global optimality, and broad generality remain outside Transportation Science-ready claims",
        ),
        _claim_row(
            evidence_metadata("stage12_baseline_portfolio", paired_artifact),
            "EVID-01",
            "core_in_domain",
            "transportation_science_ready",
            "improves in the tested setting",
            "",
            "PeMS7_228 Stage12 baseline portfolio",
            paired_artifact,
            "held_out_test_with_paired_comparisons",
            LOW_BUDGET_MULTISTART_CAVEAT_TAG,
            "phase7_core",
            "main in-domain table is derived from committed Stage12 aggregate evidence only",
        ),
        _claim_row(
            evidence_metadata("stage11_external_evidence", pems7_1026_artifact),
            "EVID-EXT-PeMS7_1026",
            "external_evidence",
            "supporting_until_phase8",
            "external evidence",
            "generalizes across networks",
            "PeMS7_1026",
            pems7_1026_artifact,
            "phase8_stage12_10_split_required_before_core_claim",
            "",
            "phase7_external_boundary",
            "PeMS7_1026 cannot be core_in_domain or transportation_science_ready in Phase 7",
        ),
        _claim_row(
            evidence_metadata("stage14_robustness", robustness_layout_artifact),
            "HAND-01-STRESS",
            "stress_test",
            "bounded_stress_test_evidence",
            "stress-tested",
            "globally robust",
            "Stage14 robustness",
            robustness_layout_artifact,
            "stress_test_only_unless_multi_seed_perturbation_evidence",
            "",
            "phase7_robustness_boundary",
            "single-stage robustness rows are routed as stress-test evidence, not global robustness",
        ),
        _claim_row(
            evidence_metadata("stage14_robustness", robustness_summary_artifact),
            "HAND-01-APPENDIX",
            "appendix",
            "bounded_appendix_evidence",
            "stress-tested",
            "",
            "Stage14 robustness",
            robustness_summary_artifact,
            "appendix_or_stress_test_only",
            "",
            "phase7_robustness_boundary",
            "robustness details remain appendix/stress-test routed unless stronger perturbation evidence is added",
        ),
    ]
    for index, forbidden in enumerate(FORBIDDEN_WORDING, start=1):
        rows.append(
            _claim_row(
                evidence_metadata("phase7_claim_policy", ".planning/REQUIREMENTS.md"),
                f"CLAIM-03-{index:02d}",
                "wording_guardrail",
                "forbidden",
                BOUNDED_ALLOWED_WORDING[min(index - 1, len(BOUNDED_ALLOWED_WORDING) - 1)],
                forbidden,
                "Phase 7 wording policy",
                ".planning/REQUIREMENTS.md",
                "wording_policy",
                LOW_BUDGET_MULTISTART_CAVEAT_TAG if forbidden == "guaranteed MAE improvement" else "",
                "phase7_wording_boundary",
                "forbidden wording must fail closed before claim/table artifact generation",
            )
        )
    return rows


def validate_claim_contract_rows(rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("claim contract rows are empty")
    required_columns = set(CLAIM_CONTRACT_COLUMNS)
    for row in rows:
        if set(row) != required_columns:
            raise ValueError(f"claim contract row has unexpected columns: {sorted(set(row))}")
        artifact = str(row["evidence_artifact"])
        source_dir = str(row["source_dir"])
        source_csv = str(row["source_csv"])
        if "TRC-23-02333/dataset/" in artifact or source_dir.startswith("TRC-23-02333/dataset/"):
            raise ValueError("claim contract references raw dataset path")
        if artifact:
            expected_metadata = evidence_metadata(str(row["source_stage"]), artifact)
            if source_dir != expected_metadata["source_dir"] or source_csv != expected_metadata["source_csv"]:
                raise ValueError(f"claim contract provenance does not match evidence artifact: {artifact}")

    present_forbidden = [str(row["forbidden_wording"]) for row in rows if row["claim_lane"] == "wording_guardrail"]
    missing_forbidden = [term for term in FORBIDDEN_WORDING if term not in present_forbidden]
    if missing_forbidden:
        raise ValueError(f"missing forbidden wording rows: {missing_forbidden}")

    present_allowed = {str(row["allowed_wording"]) for row in rows}
    missing_allowed = [phrase for phrase in BOUNDED_ALLOWED_WORDING if phrase not in present_allowed]
    if missing_allowed:
        raise ValueError(f"missing bounded allowed wording rows: {missing_allowed}")

    lanes = {str(row["claim_lane"]) for row in rows}
    required_lanes = {"core_in_domain", "tr_part_b_extension", "wording_guardrail", "external_evidence", "stress_test", "appendix"}
    if not required_lanes.issubset(lanes):
        raise ValueError(f"missing claim lanes: {sorted(required_lanes.difference(lanes))}")

    for row in rows:
        evidence_source = str(row["evidence_source"])
        lane = str(row["claim_lane"])
        status = str(row["claim_status"])
        if evidence_source in {"PeMS7_1026", "Seattle"} and (
            lane == "core_in_domain" or status == "transportation_science_ready"
        ):
            raise ValueError("external evidence cannot be elevated to core Phase 7 claims")
        if evidence_source == "Stage14 robustness" and lane not in {"stress_test", "appendix"}:
            notes = str(row["notes"]).lower()
            if "multi-seed perturbation evidence" not in notes:
                raise ValueError("robustness evidence must stay in stress_test or appendix lanes")


def _paired_lookup(paired_frame: pd.DataFrame) -> dict[tuple[float, str], pd.Series]:
    selected = paired_frame[paired_frame["layout"].eq(MAIN_METHOD_LABEL)].copy()
    lookup: dict[tuple[float, str], pd.Series] = {}
    for _, row in selected.iterrows():
        lookup[(float(row["budget"]), str(row["baseline"]))] = row
    return lookup


def build_main_table_contract_rows(
    layout_frame: pd.DataFrame,
    paired_frame: pd.DataFrame,
    source_dir: Path,
    layout_csv: Path,
    paired_csv: Path,
) -> list[dict[str, object]]:
    require_columns(layout_frame, {"budget", "layout_type", "mean", "std", "count"}, "layout summary")
    require_columns(
        paired_frame,
        {"budget", "layout", "baseline", "delta_mean", "ci95_low", "ci95_high", "paired_t_p", "wilcoxon_p", "win_count", "count"},
        "paired statistics",
    )
    labels = list(MAIN_TABLE_LAYOUT_LABELS)
    optional_labels = [SECONDARY_CERTIFICATE_BASELINE]
    available_labels = set(layout_frame["layout_type"].dropna().astype(str))
    missing = sorted(set(labels).difference(available_labels))
    if missing:
        raise ValueError(f"main table source missing required layout_type rows: {missing}")
    for label in optional_labels:
        if label in available_labels:
            labels.append(label)

    paired = _paired_lookup(paired_frame)
    budgets = sorted(float(value) for value in layout_frame["budget"].dropna().unique())
    rows: list[dict[str, object]] = []
    source_csv = f"{layout_csv.name};{paired_csv.name}"
    metadata = source_metadata("stage12_baseline_portfolio", source_dir, layout_csv)
    metadata["source_csv"] = source_csv

    for budget in budgets:
        budget_frame = layout_frame[layout_frame["budget"].astype(float).eq(budget)]
        for label in labels:
            selected = budget_frame[budget_frame["layout_type"].astype(str).eq(label)]
            if selected.empty:
                continue
            layout_row = selected.iloc[0]
            paired_row = paired.get((budget, label))
            caveat = ""
            if _budget_requires_caveat(budget) or label == "multistart_swap_by_validation":
                caveat = LOW_BUDGET_MULTISTART_CAVEAT_TAG
            row: dict[str, object] = dict(metadata)
            row.update(
                {
                    "budget": budget,
                    "method_label": MAIN_METHOD_LABEL,
                    "layout_type": label,
                    "table_role": "main_method" if label == MAIN_METHOD_LABEL else "reviewer_baseline",
                    "test_mae_mean": layout_row["mean"],
                    "test_mae_std": layout_row["std"],
                    "test_rmse_mean": _empty_metric(layout_row, "rmse_mean", "test_rmse_mean", "rmse"),
                    "test_mape_mean": _empty_metric(layout_row, "mape_mean", "test_mape_mean", "mape"),
                    "paired_baseline": "" if label == MAIN_METHOD_LABEL else label,
                    "delta_mean": "" if paired_row is None else paired_row["delta_mean"],
                    "ci95_low": "" if paired_row is None else paired_row["ci95_low"],
                    "ci95_high": "" if paired_row is None else paired_row["ci95_high"],
                    "paired_t_p": "" if paired_row is None else paired_row["paired_t_p"],
                    "wilcoxon_p": "" if paired_row is None else paired_row["wilcoxon_p"],
                    "win_count": "" if paired_row is None else paired_row["win_count"],
                    "split_count": layout_row["count"],
                    "caveat_tag": caveat,
                    "claim_lane": "core_in_domain",
                }
            )
            rows.append(row)
    return rows


def validate_main_table_contract_rows(rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("main table contract rows are empty")
    required_columns = set(MAIN_TABLE_CONTRACT_COLUMNS)
    for row in rows:
        if set(row) != required_columns:
            raise ValueError(f"main table row has unexpected columns: {sorted(set(row))}")
        if "TRC-23-02333/dataset/" in str(row["source_dir"]):
            raise ValueError("main table contract references raw dataset path")
        if row["method_label"] != MAIN_METHOD_LABEL:
            raise ValueError(f"main table method_label must be {MAIN_METHOD_LABEL}")
        if row["claim_lane"] != "core_in_domain":
            raise ValueError("main table rows must remain core_in_domain PeMS7_228 evidence")
        if _budget_requires_caveat(row["budget"]) and row["caveat_tag"] != LOW_BUDGET_MULTISTART_CAVEAT_TAG:
            raise ValueError(f"10% rows must carry {LOW_BUDGET_MULTISTART_CAVEAT_TAG}")
        if row["paired_baseline"] == "multistart_swap_by_validation" and row["caveat_tag"] != LOW_BUDGET_MULTISTART_CAVEAT_TAG:
            raise ValueError(f"multistart dominance rows must carry {LOW_BUDGET_MULTISTART_CAVEAT_TAG}")

    labels = {str(row["layout_type"]) for row in rows}
    missing_labels = sorted(set(MAIN_TABLE_LAYOUT_LABELS).difference(labels))
    if missing_labels:
        raise ValueError(f"main table contract missing required layout labels: {missing_labels}")


def main_table_labels_in_rows(main_rows: Sequence[dict[str, object]]) -> list[str]:
    ordered = list(MAIN_TABLE_LAYOUT_LABELS) + [SECONDARY_CERTIFICATE_BASELINE]
    present = {str(row["layout_type"]) for row in main_rows}
    return [label for label in ordered if label in present]


def build_claim_contract_policy(claim_rows: Sequence[dict[str, object]], main_rows: Sequence[dict[str, object]]) -> dict[str, object]:
    validate_claim_contract_rows(claim_rows)
    validate_main_table_contract_rows(main_rows)
    return {
        "claim_contract_schema": "trace_sl_claim_contract_v1",
        "generated_at_utc": "1970-01-01T00:00:00Z",
        "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
        "generated_by": "scripts/generate_trace_sl_claim_contracts.py",
        "forbidden_wording": list(FORBIDDEN_WORDING),
        "bounded_allowed_wording": list(BOUNDED_ALLOWED_WORDING),
        "claim_lanes": sorted({str(row["claim_lane"]) for row in claim_rows}),
        "claim_statuses": sorted({str(row["claim_status"]) for row in claim_rows}),
        "evidence_routing": {
            "core_in_domain": "PeMS7_228 Stage12 baseline portfolio only in Phase 7",
            "external_evidence": "PeMS7_1026 stays supporting until Phase 8 Stage12 10-split evidence; Seattle remains out of the Phase 7 contract until routed through tracked summary artifacts",
            "robustness": "stress_test or appendix unless source row declares multi-seed perturbation evidence",
            "claim_metric_basis": "held-out test evidence with paired comparisons where available; validation MAE is selection evidence only",
        },
        "caveat_tags": [LOW_BUDGET_MULTISTART_CAVEAT_TAG],
        "main_method_label": MAIN_METHOD_LABEL,
        "main_table_layout_labels": main_table_labels_in_rows(main_rows),
        "secondary_certificate_baseline_if_present": SECONDARY_CERTIFICATE_BASELINE,
        "source_artifacts": sorted(
            {
                str(row["evidence_artifact"])
                for row in claim_rows
                if not str(row["evidence_artifact"]).startswith("TRC-23-02333/dataset/")
            }
        ),
        "row_counts": {
            "claim_contract": len(claim_rows),
            "main_table_contract": len(main_rows),
        },
    }


def build_all_contracts(project_root: Path, output_dir: Path | None = None) -> dict[str, object]:
    stage12_layout = project_root / STAGE12_DIR / "gls_map_layout_summary.csv"
    stage12_paired = project_root / STAGE12_DIR / "gls_map_paired_delta_tests.csv"
    for source in (stage12_layout, stage12_paired):
        assert_source_is_tracked(project_root, source)
    layout_frame = load_csv(stage12_layout)
    paired_frame = load_csv(stage12_paired)
    claim_rows = build_claim_contract_rows(stage12_layout.parent, stage12_layout, stage12_paired)
    for row in claim_rows:
        assert_evidence_artifact_is_tracked(project_root, str(row["evidence_artifact"]))
    main_rows = build_main_table_contract_rows(layout_frame, paired_frame, stage12_layout.parent, stage12_layout, stage12_paired)
    validate_claim_contract_rows(claim_rows)
    validate_main_table_contract_rows(main_rows)
    policy = build_claim_contract_policy(claim_rows, main_rows)
    return {
        "claim_contract": claim_rows,
        "main_table_contract": main_rows,
        "claim_contract_policy": policy,
    }


def write_readme(output_dir: Path) -> None:
    readme = output_dir / "README.md"
    readme.write_text(
        "# TRACE-SL paper source tables\n\n"
        "This directory contains deterministic manuscript-facing CSV, JSON, and Markdown sources generated from committed aggregate result artifacts under `TRC-23-02333/trace_sl_results/`. "
        "They are inputs for later manuscript table/figure rendering, not manually copied paper values.\n\n"
        "Regenerate paper-source tables from the repository root with:\n\n"
        "```bash\n"
        "python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources\n"
        "python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources\n"
        "```\n\n"
        "## Generated files\n\n"
        "- `core_performance_table.csv` / `core_performance_table.md`: Stage 12 GLS/MAP core method and comparator performance by budget.\n"
        "- `paired_delta_table.csv`: Stage 12 paired deltas/tests for `validation_swap_selected` against available baselines.\n"
        "- `robustness_condition_table.csv`: Stage 14 condition-preserving robustness performance rows.\n"
        "- `candidate_runtime_table.csv`: Stage 14 candidate-count runtime and candidate diagnostic sensitivity rows.\n"
        "- `certificate_correlation_table.csv`: Stage 12/13 empirical certificate-error correlation summaries.\n"
        "- `claim_contract.csv` / `claim_contract.json` / `claim_contract.md`: Phase 7 claim wording, evidence routing, and caveat policy.\n"
        "- `main_table_contract.csv` / `main_table_contract.md`: Phase 7 Stage12 PeMS7_228 main-table contract with paired-stat provenance and caveat tags.\n\n"
        "Every generated row includes `source_stage`, `source_dir`, and `source_csv` provenance columns. The generators verify that source CSVs and nonempty evidence artifacts are tracked by git and read only committed aggregate CSVs, not raw traffic datasets.\n",
        encoding="utf-8",
    )


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
        contracts["claim_contract"],
        output_dir / "claim_contract.csv",
        output_dir / "claim_contract.md",
        CLAIM_CONTRACT_COLUMNS,
    )
    write_json(output_dir / "claim_contract.json", contracts["claim_contract_policy"])
    write_table_outputs(
        contracts["main_table_contract"],
        output_dir / "main_table_contract.csv",
        output_dir / "main_table_contract.md",
        MAIN_TABLE_CONTRACT_COLUMNS,
    )
    write_readme(output_dir)
    print(f"wrote claim_contract: {len(contracts['claim_contract'])} rows")
    print(f"wrote main_table_contract: {len(contracts['main_table_contract'])} rows")
    print(f"paper sources: {project_relative(output_dir, project_root)}")


if __name__ == "__main__":
    main()
