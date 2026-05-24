#!/usr/bin/env python3
"""Generate TRACE-SL reproducibility provenance manifests."""

from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
import copy
from importlib import metadata
from pathlib import Path
from typing import Iterable

RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
RAW_DATASET_LABEL = "protected local raw dataset input prefix"
RESULT_ROOT = Path("TRC-23-02333/trace_sl_results")

CURATED_STAGE_ENTRIES = [
    {
        "stage": "12",
        "directory": "pems7_228_stage12_baseline_portfolio",
        "claim_status": "core in-domain baseline-portfolio evidence",
        "launcher": "scripts/run_stage12_pems7_228.sh",
        "required_artifacts": [
            "SUMMARY.md",
            "combined_metrics.csv",
            "gls_map_layout_summary.csv",
            "gls_map_delta_summary.csv",
            "gls_map_paired_delta_tests.csv",
            "gls_map_win_counts.csv",
            "rcss_selected_sources.csv",
        ],
    },
    {
        "stage": "13",
        "directory": "pems7_228_stage13_candidate_sensitivity",
        "claim_status": "core tractability/sensitivity evidence",
        "launcher": "scripts/run_stage13_candidate_sensitivity_pems7_228.sh",
        "required_artifacts": [
            "SUMMARY.md",
            "combined_metrics.csv",
            "candidate_sensitivity_summary.csv",
            "runtime_candidate_sensitivity.csv",
            "stage13_timing.csv",
            "rcss_selected_sources.csv",
        ],
    },
    {
        "stage": "14",
        "directory": "pems7_228_stage14_robustness",
        "claim_status": "core stress-test robustness evidence",
        "launcher": "scripts/run_stage14_pems7_228_robustness.sh",
        "required_artifacts": [
            "SUMMARY.md",
            "combined_metrics.csv",
            "gls_map_layout_summary.csv",
            "gls_map_paired_delta_tests.csv",
            "gls_map_win_counts.csv",
            "candidate_sensitivity_summary.csv",
        ],
    },
    {
        "stage": "14",
        "directory": "pems7_228_stage14_candidate_sensitivity",
        "claim_status": "core candidate-count/runtime sensitivity evidence",
        "launcher": "scripts/run_stage14_candidate_sensitivity_pems7_228.sh",
        "required_artifacts": [
            "SUMMARY.md",
            "combined_metrics.csv",
            "candidate_sensitivity_summary.csv",
            "runtime_candidate_sensitivity.csv",
            "stage14_timing.csv",
        ],
        "allowed_exception_artifact": "candidate_sensitivity_caveat.json",
    },
    {
        "stage": "external",
        "directory": "pems7_1026_stage11_auto_weight",
        "claim_status": "lower-power external supporting/optional evidence",
        "launcher": "scripts/run_stage11_pems7_1026.sh",
        "required_artifacts": [
            "SUMMARY.md",
            "combined_metrics.csv",
            "gls_map_layout_summary.csv",
            "gls_map_delta_summary.csv",
            "gls_map_paired_delta_tests.csv",
            "gls_map_win_counts.csv",
            "rcss_selected_sources.csv",
        ],
    },
    {
        "stage": "supporting",
        "directory": "seattle_stage11_auto_weight_light",
        "claim_status": "supporting/conditional evidence",
        "launcher": "scripts/run_stage11_seattle.sh",
        "required_artifacts": [
            "SUMMARY.md",
            "combined_metrics.csv",
            "gls_map_layout_summary.csv",
            "gls_map_delta_summary.csv",
            "gls_map_paired_delta_tests.csv",
            "gls_map_win_counts.csv",
            "rcss_selected_sources.csv",
        ],
    },
]

LIST_DEFAULT_KEYS = {
    "SEEDS",
    "BUDGETS",
    "CANDIDATE_COUNTS",
    "CONDITIONS",
}

SINGLE_DEFAULT_KEYS = {
    "DATA_ROOT",
    "OUTPUT_DIR",
    "NUM_LAYOUTS",
    "RCSS_RANDOM_CANDIDATES",
    "RCSS_QUALITY_CANDIDATES",
    "SCENARIO_COUNT",
    "VALIDATION_SWAP_STARTS",
    "VALIDATION_SWAP_ITER",
    "VALIDATION_SWAP_ADD_POOL",
    "VALIDATION_SWAP_REMOVE_POOL",
    "THREADS_PER_JOB",
    "MAX_TEST_STEPS",
    "PYTHON_BIN",
    "COST_BUDGET",
}

DEFAULT_PATTERN = re.compile(
    r"^(?P<key>[A-Z][A-Z0-9_]*)=(?P<quote>[\"'])?\$\{(?P=key):-?(?P<value>[^}]*)\}(?P=quote)?(?:\s|$)"
)
ARRAY_PATTERN = re.compile(r"^(?P<key>[A-Z][A-Z0-9_]*)=\($")


def relpath(project_root: Path, path: Path) -> str:
    """Return a POSIX relative path for a path under the project root."""
    return path.resolve().relative_to(project_root.resolve()).as_posix()


def split_words(value: str) -> list[str]:
    """Split simple shell default lists without evaluating shell syntax."""
    return [part for part in value.strip().split() if part]


def parse_shell_defaults(launcher_path: Path | str) -> dict[str, object]:
    """Parse simple ${VAR:-default} assignments and literal arrays from a launcher."""
    launcher = Path(launcher_path)
    defaults: dict[str, object] = {}
    lines = launcher.read_text(encoding="utf-8").splitlines()
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        match = DEFAULT_PATTERN.match(stripped)
        if match:
            key = match.group("key")
            value = match.group("value")
            if key in LIST_DEFAULT_KEYS:
                defaults[key] = split_words(value)
            elif key in SINGLE_DEFAULT_KEYS:
                defaults[key] = value
            index += 1
            continue
        array_match = ARRAY_PATTERN.match(stripped)
        if array_match:
            key = array_match.group("key")
            values: list[str] = []
            index += 1
            while index < len(lines):
                item = lines[index].strip()
                if item == ")":
                    break
                if item and not item.startswith("#"):
                    values.append(item.strip('"\''))
                index += 1
            if key in LIST_DEFAULT_KEYS:
                defaults[key] = values
        index += 1
    return defaults


def is_evidence_path(path: Path) -> bool:
    """Return whether a path is allowed to appear as an evidence artifact."""
    return not path.as_posix().startswith(RAW_DATASET_PREFIX)


def inventory_result_dir(project_root: Path | str, result_dir: Path | str) -> dict[str, object]:
    """Inventory non-sensitive CSV/JSON/Markdown artifacts for a curated result directory."""
    root = Path(project_root).resolve()
    directory = Path(result_dir)
    if not directory.is_absolute():
        directory = root / directory
    directory_exists = directory.exists()
    artifacts: list[dict[str, object]] = []
    if directory_exists:
        for path in sorted(directory.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in {".csv", ".json", ".md"}:
                continue
            relative = relpath(root, path)
            if not is_evidence_path(Path(relative)):
                continue
            artifacts.append(
                {
                    "path": relative,
                    "size_bytes": path.stat().st_size,
                    "exists": True,
                    "is_evidence_artifact": True,
                }
            )
    return {
        "directory": relpath(root, directory) if directory.is_absolute() else Path(directory).as_posix(),
        "exists": directory_exists,
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "raw_dataset_prefix": RAW_DATASET_LABEL,
        "raw_dataset_policy": "excluded_from_evidence",
    }


def collect_environment() -> dict[str, object]:
    """Collect Python and optional dependency metadata without importing packages."""
    package_names = ["numpy", "pandas", "scipy", "scikit-learn", "sklearn"]
    packages: dict[str, dict[str, object]] = {}
    for package_name in package_names:
        metadata_name = "scikit-learn" if package_name == "sklearn" else package_name
        try:
            version = metadata.version(metadata_name)
            packages[package_name] = {"available": True, "version": version}
        except metadata.PackageNotFoundError:
            packages[package_name] = {"available": False, "version": None}
    return {
        "python": {
            "version": platform.python_version(),
            "executable": sys.executable,
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "packages": packages,
    }


def run_git(project_root: Path, args: Iterable[str]) -> str:
    """Run a read-only git command and return stdout without raising on failure."""
    try:
        completed = subprocess.run(
            ["git", "-C", str(project_root), *args],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return f"git unavailable: {exc}"
    return completed.stdout.strip() if completed.returncode == 0 else completed.stderr.strip()


def collect_input_commit(project_root: Path) -> str:
    """Return the latest commit affecting generator inputs, excluding generated outputs."""
    input_paths = [
        "TRC-23-02333/trace_sl_results/README.md",
        "scripts/generate_trace_sl_repro_manifest.py",
        "scripts/run_stage11_pems7_1026.sh",
        "scripts/run_stage11_seattle.sh",
        "scripts/run_stage12_pems7_228.sh",
        "scripts/run_stage13_candidate_sensitivity_pems7_228.sh",
        "scripts/run_stage14_candidate_sensitivity_pems7_228.sh",
        "scripts/run_stage14_pems7_228_robustness.sh",
    ]
    input_paths.extend((RESULT_ROOT / entry["directory"]).as_posix() for entry in curated_stage_entries(project_root))
    input_paths.extend(
        [
            f":(exclude){RESULT_ROOT / 'reproducibility_manifest.json'}",
            f":(exclude){RESULT_ROOT / 'REPRODUCIBILITY_MANIFEST.md'}",
        ]
    )
    return run_git(project_root, ["rev-list", "-1", "HEAD", "--", *input_paths])


def collect_git_provenance(project_root: Path) -> dict[str, object]:
    """Collect local git provenance and raw-data path hygiene."""
    tracked_raw = [
        line
        for line in run_git(project_root, ["ls-files", "--", RAW_DATASET_PREFIX]).splitlines()
        if line.strip()
    ]
    status_lines = [
        line
        for line in run_git(project_root, ["status", "--short"]).splitlines()
        if line.strip()
    ]
    relevant_status_prefixes = (
        "scripts/generate_trace_sl_repro_manifest.py",
        "scripts/test_generate_trace_sl_repro_manifest.py",
        "TRC-23-02333/trace_sl_results/reproducibility_manifest.json",
        "TRC-23-02333/trace_sl_results/REPRODUCIBILITY_MANIFEST.md",
        ".planning/phases/06-reproducibility-and-artifact-curation/06-01-SUMMARY.md",
    )
    relevant_status = []
    for line in status_lines:
        path_part = line[3:]
        if path_part.startswith(relevant_status_prefixes):
            relevant_status.append(line)
    return {
        "commit": collect_input_commit(project_root),
        "commit_scope": "latest commit affecting manifest generator inputs; generated manifest outputs excluded for idempotence",
        "branch": run_git(project_root, ["rev-parse", "--abbrev-ref", "HEAD"]),
        "status_short_relevant": relevant_status,
        "status_short_total_count": len(status_lines),
        "tracked_raw_dataset_paths": tracked_raw,
        "tracked_raw_dataset_path_count": len(tracked_raw),
        "raw_dataset_policy": "protected local input only; excluded from paper-visible evidence artifacts",
    }


def safe_launcher_defaults(defaults: dict[str, object]) -> dict[str, object]:
    """Return launcher defaults that are safe to expose in evidence manifests."""
    safe: dict[str, object] = {}
    for key, value in defaults.items():
        rendered = " ".join(value) if isinstance(value, list) else str(value)
        if RAW_DATASET_PREFIX not in rendered:
            safe[key] = value
    return safe


def launcher_command(defaults: dict[str, object], launcher_path: str) -> str:
    """Build a human-readable launcher invocation with default environment overrides."""
    env_parts = []
    for key in sorted(defaults):
        value = defaults[key]
        if isinstance(value, list):
            rendered = " ".join(value)
        else:
            rendered = str(value)
        env_parts.append(f"{key}='{rendered}'")
    return " ".join(env_parts + ["bash", launcher_path])


def required_artifact_status(project_root: Path, directory: str, artifact_names: Iterable[str]) -> list[dict[str, object]]:
    """Return existence and size records for required top-level artifacts."""
    rows = []
    for artifact_name in artifact_names:
        path = RESULT_ROOT / directory / artifact_name
        absolute = project_root / path
        rows.append(
            {
                "path": path.as_posix(),
                "exists": absolute.exists(),
                "size_bytes": absolute.stat().st_size if absolute.exists() else 0,
                "is_evidence_artifact": is_evidence_path(path),
            }
        )
    return rows


def external_stage_entries_from_gate(project_root: Path) -> list[dict[str, object]]:
    """Return completed Stage12 external entries allowed by the external evidence gate."""
    gate_path = project_root / RESULT_ROOT / "paper_sources" / "external_evidence_gate.json"
    if not gate_path.exists():
        return []
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    specs = [
        {
            "gate_key": "pems7_1026_stage12_complete",
            "stage": "external-stage12",
            "directory": "pems7_1026_stage12_baseline_portfolio",
            "claim_status": "blocked external Stage12 evidence" if not gate.get("pems7_1026_stage12_complete") else "external Stage12 ten-split evidence",
            "launcher": "scripts/run_stage12_pems7_1026.sh",
        },
        {
            "gate_key": "seattle_stage12_complete",
            "stage": "external-stage12",
            "directory": "seattle_stage12_baseline_portfolio",
            "claim_status": "blocked external Stage12 evidence" if not gate.get("seattle_stage12_complete") else "external Stage12 ten-split evidence",
            "launcher": "scripts/run_stage12_seattle.sh",
        },
    ]
    entries: list[dict[str, object]] = []
    for spec in specs:
        if not gate.get(spec["gate_key"]):
            continue
        entry = {key: value for key, value in spec.items() if key != "gate_key"}
        entry["required_artifacts"] = [
            "SUMMARY.md",
            "combined_metrics.csv",
            "gls_map_layout_summary.csv",
            "gls_map_delta_summary.csv",
            "gls_map_paired_delta_tests.csv",
            "gls_map_win_counts.csv",
            "rcss_selected_sources.csv",
        ]
        entries.append(entry)
    return entries


def curated_stage_entries(project_root: Path) -> list[dict[str, object]]:
    entries = copy.deepcopy(CURATED_STAGE_ENTRIES)
    entries.extend(external_stage_entries_from_gate(project_root))
    return entries


def build_manifest(project_root: Path) -> dict[str, object]:
    """Build a deterministic TRACE-SL reproducibility manifest payload."""
    stages = []
    for entry in curated_stage_entries(project_root):
        directory = entry["directory"]
        launcher = entry["launcher"]
        launcher_path = project_root / launcher
        defaults = parse_shell_defaults(launcher_path) if launcher_path.exists() else {}
        exposed_defaults = safe_launcher_defaults(defaults)
        inventory = inventory_result_dir(project_root, RESULT_ROOT / directory)
        stage = {
            "stage": entry["stage"],
            "directory": directory,
            "claim_status": entry["claim_status"],
            "launcher": launcher,
            "launcher_exists": launcher_path.exists(),
            "launcher_defaults": exposed_defaults,
            "launcher_command_template": launcher_command(exposed_defaults, launcher),
            "required_artifacts": required_artifact_status(project_root, directory, entry["required_artifacts"]),
            "inventory": inventory,
        }
        if "allowed_exception_artifact" in entry:
            exception_path = RESULT_ROOT / directory / entry["allowed_exception_artifact"]
            stage["allowed_exception_artifact"] = {
                "path": exception_path.as_posix(),
                "exists": (project_root / exception_path).exists(),
            }
        stages.append(stage)
    return {
        "manifest_schema": "trace-sl-reproducibility-provenance-v1",
        "generated_at_utc": "1970-01-01T00:00:00Z",
        "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
        "generated_by": "scripts/generate_trace_sl_repro_manifest.py",
        "project_root_name": project_root.name,
        "policy": {
            "raw_dataset_prefix": RAW_DATASET_LABEL,
            "raw_dataset_disposition": "protected local input only; never listed as evidence artifact",
            "experiment_rerun_disposition": "not run by this generator",
            "dependency_disposition": "standard library only for generator; package metadata queried via importlib.metadata",
        },
        "environment": collect_environment(),
        "git": collect_git_provenance(project_root),
        "curated_result_stages": stages,
    }


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_markdown(payload: dict[str, object]) -> str:
    """Render a human-readable manifest from the JSON payload."""
    lines = [
        "# TRACE-SL Reproducibility Manifest",
        "",
        f"Generated by `{payload['generated_by']}` at `{payload['generated_at_utc']}`.",
        "",
        "## Raw Dataset Hygiene",
        "",
        f"- Raw dataset prefix: `{payload['policy']['raw_dataset_prefix']}`",
        f"- Disposition: {payload['policy']['raw_dataset_disposition']}",
        f"- Tracked raw dataset paths: {payload['git']['tracked_raw_dataset_path_count']}",
        "- Raw datasets are protected local inputs and are not evidence artifacts in this manifest.",
        "",
        "## Environment",
        "",
        f"- Python: {payload['environment']['python']['version']} ({payload['environment']['python']['implementation']})",
        f"- Executable: `{payload['environment']['python']['executable']}`",
        "",
        "| Package | Available | Version |",
        "|---|---:|---|",
    ]
    for name, info in sorted(payload["environment"]["packages"].items()):
        version = info["version"] if info["version"] is not None else "unavailable"
        lines.append(f"| {name} | {info['available']} | {version} |")
    lines.extend(
        [
            "",
            "## Git Provenance",
            "",
            f"- Commit: `{payload['git']['commit']}`",
            f"- Branch: `{payload['git']['branch']}`",
            f"- Relevant manifest status entries: {len(payload['git']['status_short_relevant'])}",
            f"- Total working-tree status entries: {payload['git']['status_short_total_count']}",
            "",
            "## Curated Result Stages",
            "",
            "| Directory | Claim status | Launcher | Artifacts | Required present |",
            "|---|---|---|---:|---:|",
        ]
    )
    for stage in payload["curated_result_stages"]:
        required = stage["required_artifacts"]
        present = sum(1 for row in required if row["exists"])
        lines.append(
            "| `{directory}` | {claim_status} | `{launcher}` | {artifact_count} | {present}/{total} |".format(
                directory=stage["directory"],
                claim_status=stage["claim_status"],
                launcher=stage["launcher"],
                artifact_count=stage["inventory"]["artifact_count"],
                present=present,
                total=len(required),
            )
        )
    lines.extend(["", "## Launcher Defaults", ""])
    for stage in payload["curated_result_stages"]:
        lines.extend(
            [
                f"### `{stage['launcher']}`",
                "",
                f"- Result directory: `{stage['directory']}`",
                f"- Claim status: {stage['claim_status']}",
                "",
                "| Key | Default |",
                "|---|---|",
            ]
        )
        for key, value in sorted(stage["launcher_defaults"].items()):
            rendered = " ".join(value) if isinstance(value, list) else str(value)
            lines.append(f"| `{key}` | `{rendered}` |")
        lines.extend(["", f"Command template: `{stage['launcher_command_template']}`", ""])
    lines.extend(["## Required Artifact Inventory", ""])
    for stage in payload["curated_result_stages"]:
        lines.extend([f"### `{stage['directory']}`", "", "| Path | Exists | Size bytes |", "|---|---:|---:|"])
        for row in stage["required_artifacts"]:
            lines.append(f"| `{row['path']}` | {row['exists']} | {row['size_bytes']} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_markdown(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(payload), encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=".", help="Repository root containing TRACE-SL artifacts.")
    parser.add_argument("--output-dir", help="Directory to write reproducibility_manifest.json and REPRODUCIBILITY_MANIFEST.md.")
    parser.add_argument("--output-json", help="Path to write machine-readable JSON manifest.")
    parser.add_argument("--output-md", help="Path to write human-readable Markdown manifest.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    project_root = Path(args.project_root).resolve()
    payload = build_manifest(project_root)
    if args.output_dir:
        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            output_dir = project_root / output_dir
        output_json = output_dir / "reproducibility_manifest.json"
        output_md = output_dir / "REPRODUCIBILITY_MANIFEST.md"
    elif args.output_json and args.output_md:
        output_json = Path(args.output_json)
        output_md = Path(args.output_md)
        if not output_json.is_absolute():
            output_json = project_root / output_json
        if not output_md.is_absolute():
            output_md = project_root / output_md
    else:
        raise SystemExit("provide --output-dir or both --output-json and --output-md")
    write_json(output_json, payload)
    write_markdown(output_md, payload)
    print(f"Wrote {output_json}")
    print(f"Wrote {output_md}")


if __name__ == "__main__":
    main()
