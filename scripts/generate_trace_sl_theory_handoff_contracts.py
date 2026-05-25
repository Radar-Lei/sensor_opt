#!/usr/bin/env python3
"""Generate TRACE-SL theory and handoff paper-foundation contracts."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd


TRACE_RESULTS_ROOT = Path("TRC-23-02333/trace_sl_results")
PAPER_SOURCES_DIR = TRACE_RESULTS_ROOT / "paper_sources"
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
GENERATED_AT_UTC = "1970-01-01T00:00:00Z"
FORBIDDEN_MANUSCRIPT_HEADINGS = (
    "introduction",
    "related work",
    "method section",
    "results section",
    "limitations",
    "abstract",
    "conclusion",
)

THEORY_STATEMENT_COLUMNS = (
    "requirement_id",
    "statement_id",
    "statement_type",
    "statement_name",
    "scoped_statement",
    "assumptions",
    "non_claim_boundaries",
    "source_artifact",
    "source_role",
    "claim_route",
)

HANDOFF_MANIFEST_COLUMNS = (
    "handoff_id",
    "requirement_id",
    "artifact_path",
    "artifact_type",
    "source_phase",
    "supports",
    "safe_for_writing",
    "raw_dataset_free",
    "manuscript_prose_status",
    "regenerate_command",
)

THEORY_ROWS = (
    {
        "requirement_id": "THEORY-01",
        "statement_id": "TH-01",
        "statement_type": "formulation",
        "statement_name": "budgeted_hidden_network_reconstruction",
        "scoped_statement": "Choose a fixed sensor set S with |S| <= k from observed candidates; learn reconstruction ingredients on training splits, tune layout selection on validation splits, and report final reconstruction only on held-out test splits after the selection rule is fixed.",
        "assumptions": "fixed graph and candidate set; train/validation/test split separation; transparent GLS/MAP or GSP reconstruction; budget k derived from budget fraction",
        "non_claim_boundaries": "does not assert global optimality or guaranteed MAE improvement",
        "source_artifact": "TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json",
        "source_role": "claim boundary and split-policy source",
        "claim_route": "paper_foundation_formulation",
    },
    {
        "requirement_id": "THEORY-02",
        "statement_id": "TH-02",
        "statement_type": "identity",
        "statement_name": "posterior_trace_squared_error_identity",
        "scoped_statement": "Under the stated linear-Gaussian squared-error model, the posterior covariance trace over hidden components equals the conditional expected squared reconstruction error up to the fixed observation/noise model used by the estimator.",
        "assumptions": "linear-Gaussian prior and observation model; squared-error loss; hidden-component posterior covariance computed after conditioning on selected sensors",
        "non_claim_boundaries": "does not convert posterior trace into an MAE guarantee for non-Gaussian traffic data",
        "source_artifact": "TRC-23-02333/transparent_estimator_eval.py",
        "source_role": "posterior trace computation implementation",
        "claim_route": "theory_ready_identity",
    },
    {
        "requirement_id": "THEORY-03",
        "statement_id": "TH-03",
        "statement_type": "proposition",
        "statement_name": "posterior_covariance_monotonicity",
        "scoped_statement": "For the same linear-Gaussian model, conditioning on an additional sensor cannot increase the posterior covariance in positive-semidefinite order, so posterior trace is nonincreasing as sensors are added.",
        "assumptions": "same prior/noise model before and after adding the sensor; valid conditioning update; no model refit between nested sensor sets",
        "non_claim_boundaries": "does not imply submodularity, approximation ratio, or monotone empirical MAE on every split",
        "source_artifact": "TRC-23-02333/transparent_estimator_eval.py",
        "source_role": "posterior covariance and trace helper implementation",
        "claim_route": "theory_ready_monotonicity",
    },
    {
        "requirement_id": "THEORY-04",
        "statement_id": "TH-04",
        "statement_type": "local_optimality",
        "statement_name": "validation_aware_one_swap_local_optimality",
        "scoped_statement": "A validation-aware swap output is locally optimal with respect to the evaluated one-swap neighborhood when no tested remove/add exchange from the configured candidate pool strictly improves validation reconstruction loss.",
        "assumptions": "finite evaluated neighborhood; deterministic validation score for a fixed split and method; configured add/remove pools and iteration budget define the neighborhood",
        "non_claim_boundaries": "does not assert global optimality outside the evaluated one-swap neighborhood",
        "source_artifact": "TRC-23-02333/transparent_estimator_eval.py",
        "source_role": "validation swap search implementation",
        "claim_route": "algorithmic_statement_local_search",
    },
    {
        "requirement_id": "THEORY-05",
        "statement_id": "TH-05",
        "statement_type": "complexity",
        "statement_name": "rcss_candidate_search_evaluation_complexity",
        "scoped_statement": "RCSS runtime can be stated as candidate generation plus candidate scoring plus validation-aware swap evaluation, scaling with the configured candidate counts, budgets, validation windows, swap starts, swap iterations, and add/remove pool sizes recorded by launchers and manifests.",
        "assumptions": "finite candidate counts and budget list; transparent evaluator cost is measured per candidate/swap; launcher defaults define the reported workload",
        "non_claim_boundaries": "does not claim polynomial-time optimal placement certification or hardware-independent runtime guarantees",
        "source_artifact": "TRC-23-02333/trace_sl_results/reproducibility_manifest.json",
        "source_role": "launcher defaults and reproducibility manifest",
        "claim_route": "complexity_statement_workload_bound",
    },
)

HANDOFF_ROWS = (
    {
        "handoff_id": "HO-CLAIM",
        "requirement_id": "HAND-02/HAND-03",
        "artifact_path": "TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json",
        "artifact_type": "claim_contract",
        "source_phase": "Phase 7",
        "supports": "claim wording, evidence routing, and caveat policy",
        "safe_for_writing": True,
        "raw_dataset_free": True,
        "manuscript_prose_status": "not_manuscript_prose",
        "regenerate_command": "python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources",
    },
    {
        "handoff_id": "HO-MAIN-TABLE",
        "requirement_id": "HAND-02/HAND-03",
        "artifact_path": "TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv",
        "artifact_type": "table_contract",
        "source_phase": "Phase 7",
        "supports": "core PeMS7_228 main-table evidence and paired-stat honesty",
        "safe_for_writing": True,
        "raw_dataset_free": True,
        "manuscript_prose_status": "not_manuscript_prose",
        "regenerate_command": "python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources",
    },
    {
        "handoff_id": "HO-EXTERNAL-GATE",
        "requirement_id": "HAND-02/HAND-03",
        "artifact_path": "TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json",
        "artifact_type": "gate_contract",
        "source_phase": "Phase 8",
        "supports": "fail-closed PeMS7_1026 and Seattle Stage12 completion boundaries",
        "safe_for_writing": True,
        "raw_dataset_free": True,
        "manuscript_prose_status": "not_manuscript_prose",
        "regenerate_command": "python scripts/generate_trace_sl_external_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources",
    },
    {
        "handoff_id": "HO-ABLATION",
        "requirement_id": "HAND-02/HAND-03",
        "artifact_path": "TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.json",
        "artifact_type": "ablation_contract",
        "source_phase": "Phase 9",
        "supports": "ablation layer, evidence basis, paired-stat status, and caveat routing",
        "safe_for_writing": True,
        "raw_dataset_free": True,
        "manuscript_prose_status": "not_manuscript_prose",
        "regenerate_command": "python scripts/generate_trace_sl_ablation_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources",
    },
    {
        "handoff_id": "HO-DATASET-LANES",
        "requirement_id": "HAND-02/HAND-03",
        "artifact_path": "TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.json",
        "artifact_type": "evidence_classification",
        "source_phase": "Phase 9",
        "supports": "dataset evidence lanes and non-core external status",
        "safe_for_writing": True,
        "raw_dataset_free": True,
        "manuscript_prose_status": "not_manuscript_prose",
        "regenerate_command": "python scripts/generate_trace_sl_ablation_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources",
    },
    {
        "handoff_id": "HO-REPRO",
        "requirement_id": "HAND-02/HAND-03",
        "artifact_path": "TRC-23-02333/trace_sl_results/reproducibility_manifest.json",
        "artifact_type": "reproducibility_manifest",
        "source_phase": "Phase 6/8.5",
        "supports": "committed summaries, launcher defaults, curated artifacts, and raw-data exclusion policy",
        "safe_for_writing": True,
        "raw_dataset_free": True,
        "manuscript_prose_status": "not_manuscript_prose",
        "regenerate_command": "python scripts/generate_trace_sl_repro_manifest.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results",
    },
    {
        "handoff_id": "HO-THEORY",
        "requirement_id": "THEORY-01/THEORY-02/THEORY-03/THEORY-04/THEORY-05/HAND-02",
        "artifact_path": "TRC-23-02333/trace_sl_results/paper_sources/theory_statement_contract.json",
        "artifact_type": "theory_contract",
        "source_phase": "Phase 10",
        "supports": "theory-ready scoped statements and non-claim boundaries",
        "safe_for_writing": True,
        "raw_dataset_free": True,
        "manuscript_prose_status": "not_manuscript_prose",
        "regenerate_command": "python scripts/generate_trace_sl_theory_handoff_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources",
    },
)


def project_relative(path: Path, project_root: Path) -> str:
    return path.resolve().relative_to(project_root.resolve()).as_posix()


def resolve_output_dir(project_root: Path, output_dir: Path) -> Path:
    if output_dir.is_absolute():
        return output_dir
    return project_root / output_dir


def assert_no_raw_dataset_path(value: object, label: str) -> None:
    rendered = json.dumps(value, sort_keys=True, default=str) if not isinstance(value, str) else value
    if RAW_DATASET_PREFIX in rendered:
        raise ValueError(f"{label} references raw dataset path")


def assert_git_path_is_committed(project_root: Path, relative: str, label: str) -> None:
    result = subprocess.run(
        ["git", "-C", str(project_root), "cat-file", "-e", f"HEAD:{relative}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"{label} is not committed in HEAD: {relative}")
    diff = subprocess.run(
        ["git", "-C", str(project_root), "diff", "--quiet", "HEAD", "--", relative],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if diff.returncode != 0:
        raise ValueError(f"{label} has uncommitted changes relative to HEAD: {relative}")


def assert_artifact_is_safe(project_root: Path, artifact: str, label: str) -> None:
    assert_no_raw_dataset_path(artifact, label)
    if artifact.startswith(TRACE_RESULTS_ROOT.as_posix() + "/") or artifact.startswith("scripts/") or artifact == "TRC-23-02333/transparent_estimator_eval.py":
        path = project_root / artifact
        if not path.exists():
            raise FileNotFoundError(f"{label} not found: {artifact}")
        assert_git_path_is_committed(project_root, artifact, label)
        return
    raise ValueError(f"{label} is outside curated roots: {artifact}")


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
        lines.append("| " + " | ".join(format_markdown_value(row.get(column, "")) for column in columns) + " |")
    return "\n".join(lines) + "\n"


def write_table_outputs(rows: Sequence[dict[str, object]], output_csv: Path, output_md: Path, columns: Sequence[str]) -> None:
    if not rows:
        raise ValueError(f"refusing to write empty table: {output_csv}")
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows).loc[:, list(columns)]
    frame.to_csv(output_csv, index=False)
    output_md.write_text(markdown_table(frame.to_dict(orient="records"), columns), encoding="utf-8")


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_rows(rows: Sequence[dict[str, object]], columns: Sequence[str], label: str) -> None:
    if not rows:
        raise ValueError(f"{label} rows are empty")
    expected = set(columns)
    for row in rows:
        if set(row) != expected:
            raise ValueError(f"{label} row has unexpected columns: {sorted(set(row))}")
        assert_no_raw_dataset_path(row, label)
        rendered = json.dumps(row, sort_keys=True, default=str).lower()
        for heading in FORBIDDEN_MANUSCRIPT_HEADINGS:
            if heading in rendered:
                raise ValueError(f"{label} contains manuscript prose heading marker: {heading}")


def build_theory_rows(project_root: Path) -> list[dict[str, object]]:
    rows = [dict(row) for row in THEORY_ROWS]
    for row in rows:
        assert_artifact_is_safe(project_root, str(row["source_artifact"]), "Theory source artifact")
    validate_rows(rows, THEORY_STATEMENT_COLUMNS, "theory statement")
    return rows


def build_handoff_rows(project_root: Path) -> list[dict[str, object]]:
    rows = [dict(row) for row in HANDOFF_ROWS]
    for row in rows:
        artifact = str(row["artifact_path"])
        if artifact.endswith("theory_statement_contract.json"):
            continue
        assert_artifact_is_safe(project_root, artifact, "Handoff artifact")
    validate_rows(rows, HANDOFF_MANIFEST_COLUMNS, "handoff manifest")
    if not all(bool(row["safe_for_writing"]) and bool(row["raw_dataset_free"]) for row in rows):
        raise ValueError("handoff rows must be safe for writing and raw-dataset-free")
    return rows


def build_metadata(theory_rows: Sequence[dict[str, object]], handoff_rows: Sequence[dict[str, object]]) -> dict[str, object]:
    return {
        "schema": "trace_sl_theory_handoff_contracts_v1",
        "generated_at_utc": GENERATED_AT_UTC,
        "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
        "generated_by": "scripts/generate_trace_sl_theory_handoff_contracts.py",
        "row_counts": {
            "theory_statement_contract": len(theory_rows),
            "paper_foundation_handoff_manifest": len(handoff_rows),
        },
        "requirements": sorted({str(row["requirement_id"]) for row in (*theory_rows, *handoff_rows)}),
        "manuscript_heading_scan": "enforced_by_generator",
        "raw_dataset_policy_marker": "protected local raw dataset input prefix",
        "raw_dataset_policy": "protected local input only; excluded from handoff evidence artifacts",
        "manuscript_prose_policy": "row-level paper-foundation contracts only; no manuscript prose drafting",
        "source_artifacts": sorted({str(row["source_artifact"]) for row in theory_rows} | {str(row["artifact_path"]) for row in handoff_rows}),
    }


def build_all_contracts(project_root: Path, output_dir: Path | None = None) -> dict[str, object]:
    del output_dir
    theory_rows = build_theory_rows(project_root)
    handoff_rows = build_handoff_rows(project_root)
    metadata = build_metadata(theory_rows, handoff_rows)
    validate_rows(theory_rows, THEORY_STATEMENT_COLUMNS, "theory statement")
    validate_rows(handoff_rows, HANDOFF_MANIFEST_COLUMNS, "handoff manifest")
    return {
        "theory_statement_contract": theory_rows,
        "paper_foundation_handoff_manifest": handoff_rows,
        "metadata": metadata,
    }


def update_readme(output_dir: Path) -> None:
    readme = output_dir / "README.md"
    block = (
        "\n## Phase 10 Theory and Handoff Sources\n\n"
        "Regenerate Phase 10 theory and handoff contracts from the repository root with:\n\n"
        "```bash\n"
        "python scripts/generate_trace_sl_theory_handoff_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources\n"
        "```\n\n"
        "Generated files:\n\n"
        "- `theory_statement_contract.csv` / `theory_statement_contract.json` / `theory_statement_contract.md`: Phase 10 theory-ready scoped statements, assumptions, and non-claim boundaries.\n"
        "- `paper_foundation_handoff_manifest.csv` / `paper_foundation_handoff_manifest.json` / `paper_foundation_handoff_manifest.md`: reproducibility-safe paper-foundation artifact pointers for later writing.\n\n"
        "These are row-level paper-foundation contracts, not manuscript prose. Raw traffic datasets under `TRC-23-02333/dataset/` are protected local inputs and are not evidence artifacts.\n"
    )
    text = readme.read_text(encoding="utf-8") if readme.exists() else "# TRACE-SL paper source tables\n"
    heading = "## Phase 10 Theory and Handoff Sources"
    if heading in text:
        text = text[: text.index(heading) - 1].rstrip() + block
    else:
        text = text.rstrip() + block
    readme.write_text(text, encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, default=PAPER_SOURCES_DIR)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    project_root = args.project_root.resolve()
    output_dir = resolve_output_dir(project_root, args.output_dir)
    contracts = build_all_contracts(project_root, output_dir)
    theory_rows = contracts["theory_statement_contract"]
    handoff_rows = contracts["paper_foundation_handoff_manifest"]
    metadata = contracts["metadata"]
    write_table_outputs(theory_rows, output_dir / "theory_statement_contract.csv", output_dir / "theory_statement_contract.md", THEORY_STATEMENT_COLUMNS)
    write_json(output_dir / "theory_statement_contract.json", {"theory_statement_contract": theory_rows, "metadata": metadata})
    write_table_outputs(handoff_rows, output_dir / "paper_foundation_handoff_manifest.csv", output_dir / "paper_foundation_handoff_manifest.md", HANDOFF_MANIFEST_COLUMNS)
    write_json(output_dir / "paper_foundation_handoff_manifest.json", {"paper_foundation_handoff_manifest": handoff_rows, "metadata": metadata})
    update_readme(output_dir)
    print(f"wrote theory_statement_contract: {len(theory_rows)} rows")
    print(f"wrote paper_foundation_handoff_manifest: {len(handoff_rows)} rows")
    print(f"paper sources: {project_relative(output_dir, project_root)}")


if __name__ == "__main__":
    main()
