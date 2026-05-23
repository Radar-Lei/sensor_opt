#!/usr/bin/env python3
import argparse
import csv
import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd


REPRO_REQUIREMENTS = ["REPRO-01", "REPRO-02", "REPRO-03", "REPRO-04", "REPRO-05"]
RESULTS_ROOT = Path("TRC-23-02333") / "trace_sl_results"
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
MANIFEST_PATH = RESULTS_ROOT / "reproducibility_manifest.json"
MANIFEST_MD_PATH = RESULTS_ROOT / "REPRODUCIBILITY_MANIFEST.md"
PAPER_SOURCES_DIR = RESULTS_ROOT / "paper_sources"
PHASE4_VALIDATOR = Path(".planning") / "phases" / "04-core-experiment-evidence" / "validate_phase4_evidence.py"
PHASE5_VALIDATOR = Path(".planning") / "phases" / "05-robustness-and-generality" / "validate_phase5_robustness.py"
PHASE6_AUDIT = Path(".planning") / "phases" / "06-reproducibility-and-artifact-curation" / "06-REPRODUCIBILITY-AUDIT.md"

STAGE12_DIR = RESULTS_ROOT / "pems7_228_stage12_baseline_portfolio"
STAGE13_DIR = RESULTS_ROOT / "pems7_228_stage13_candidate_sensitivity"
STAGE14_ROBUSTNESS_DIR = RESULTS_ROOT / "pems7_228_stage14_robustness"
STAGE14_CANDIDATE_DIR = RESULTS_ROOT / "pems7_228_stage14_candidate_sensitivity"

REQUIRED_CURATED_STAGE_DIRS = {
    "Stage 12 PeMS7_228": STAGE12_DIR,
    "Stage 13 candidate sensitivity": STAGE13_DIR,
    "Stage 14 robustness": STAGE14_ROBUSTNESS_DIR,
    "Stage 14 candidate sensitivity": STAGE14_CANDIDATE_DIR,
}
REQUIRED_STAGE_DEFAULTS = {
    str(STAGE12_DIR): ["SEEDS", "BUDGETS", "RCSS_RANDOM_CANDIDATES", "RCSS_QUALITY_CANDIDATES", "PYTHON_BIN"],
    str(STAGE13_DIR): ["SEEDS", "BUDGETS", "CANDIDATE_COUNTS", "PYTHON_BIN"],
    str(STAGE14_ROBUSTNESS_DIR): ["SEEDS", "BUDGETS", "RCSS_RANDOM_CANDIDATES", "RCSS_QUALITY_CANDIDATES", "PYTHON_BIN"],
    str(STAGE14_CANDIDATE_DIR): ["SEEDS", "BUDGETS", "CANDIDATE_COUNTS", "PYTHON_BIN"],
}
REQUIRED_PACKAGE_NAMES = {"pandas", "numpy", "scipy", "scikit-learn"}
REQUIRED_PAPER_SOURCE_CSVS = [
    "core_performance_table.csv",
    "paired_delta_table.csv",
    "robustness_condition_table.csv",
    "candidate_runtime_table.csv",
    "certificate_correlation_table.csv",
]
REQUIRED_PAPER_SOURCE_MARKDOWN = ["core_performance_table.md", "README.md"]
REQUIRED_PROVENANCE_COLUMNS = {"source_stage", "source_dir", "source_csv"}
REQUIRED_BASELINE_LAYOUTS = {
    "validation_swap_selected",
    "rcss_selected",
    "multistart_swap_by_validation",
    "greedy_a_trace",
    "greedy_d_logdet",
    "observability_proxy",
    "graph_sampling_laplacian",
    "qr_pod_modes",
}
REQUIRED_ROBUSTNESS_CONDITIONS = {
    "baseline",
    "failure_0.05",
    "failure_0.10",
    "failure_0.20",
    "noise_0.05",
    "random_missing_0.10",
    "block_missing_12",
    "cost_proxy_budget",
    "chronological_split",
}
REQUIRED_CANDIDATE_COUNTS = {50, 100, 200, 500}
LAUNCHER_SCRIPTS = [
    "scripts/run_stage12_pems7_228.sh",
    "scripts/run_stage13_candidate_sensitivity_pems7_228.sh",
    "scripts/run_stage14_pems7_228_robustness.sh",
    "scripts/run_stage14_candidate_sensitivity_pems7_228.sh",
]
SMOKE_LABELS = {
    "scripts/run_stage12_pems7_228.sh": "Stage 12 PeMS7_228",
    "scripts/run_stage13_candidate_sensitivity_pems7_228.sh": "Stage 13 candidate sensitivity",
    "scripts/run_stage14_pems7_228_robustness.sh": "Stage 14 robustness",
    "scripts/run_stage14_candidate_sensitivity_pems7_228.sh": "Stage 14 candidate sensitivity",
}
DOCS_TO_SCAN = [
    RESULTS_ROOT / "README.md",
    MANIFEST_MD_PATH,
    PAPER_SOURCES_DIR / "README.md",
    PHASE6_AUDIT,
]
ALLOWED_RAW_DATASET_DOC_CONTEXT = (
    "data_root",
    "command template",
    "raw dataset prefix",
    "raw dataset",
    "ignored",
    "local input",
    "not evidence",
    "no raw dataset evidence",
    "do not",
    "must not",
    "excluded",
)


@dataclass
class CommandSpec:
    label: str
    args: list[str]
    env: dict[str, str] = field(default_factory=dict)


@dataclass
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


class ValidationContext:
    def __init__(self, project_root):
        self.project_root = Path(project_root).resolve()
        self.errors = []
        self.passes = []
        self.details = []

    def fail(self, requirement, message):
        self.errors.append((requirement, message))

    def pass_check(self, requirement, message):
        self.passes.append((requirement, message))

    def detail(self, requirement, message):
        self.details.append((requirement, message))

    def has_failures(self, requirement=None):
        if requirement is None:
            return bool(self.errors)
        return any(req == requirement for req, _ in self.errors)

    def messages_for(self, requirement):
        messages = [message for req, message in self.errors if req == requirement]
        if messages:
            return messages
        passes = [message for req, message in self.passes if req == requirement]
        details = [message for req, message in self.details if req == requirement]
        return passes + details

    def status_for(self, requirement):
        return "FAIL" if self.has_failures(requirement) else "PASS"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Validate TRACE-SL Phase 6 reproducibility artifacts")
    parser.add_argument("--project-root", default=None, help="Repository root; defaults to this script's project root")
    return parser.parse_args(argv)


def relative_to_root(path, root):
    path = Path(path)
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def read_json(path, requirement, context):
    full_path = context.project_root / path
    if not full_path.exists():
        context.fail(requirement, f"missing required JSON: {path}")
        return {}
    if full_path.stat().st_size == 0:
        context.fail(requirement, f"empty required JSON: {path}")
        return {}
    try:
        return json.loads(full_path.read_text(encoding="utf-8"))
    except Exception as exc:
        context.fail(requirement, f"unreadable JSON {path}: {exc}")
        return {}


def read_text(path, requirement, context):
    full_path = context.project_root / path
    if not full_path.exists():
        context.fail(requirement, f"missing required text artifact: {path}")
        return ""
    if full_path.stat().st_size == 0:
        context.fail(requirement, f"empty required text artifact: {path}")
        return ""
    try:
        return full_path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        context.fail(requirement, f"unreadable text artifact {path}: {exc}")
        return ""


def read_csv_frame(path, requirement, context):
    full_path = context.project_root / path
    if not full_path.exists():
        context.fail(requirement, f"missing required CSV: {path}")
        return pd.DataFrame()
    if full_path.stat().st_size == 0:
        context.fail(requirement, f"empty required CSV: {path}")
        return pd.DataFrame()
    try:
        frame = pd.read_csv(full_path)
    except Exception as exc:
        context.fail(requirement, f"unreadable CSV {path}: {exc}")
        return pd.DataFrame()
    if frame.empty:
        context.fail(requirement, f"CSV has no rows: {path}")
    return frame


def git_ls_files(project_root, pathspec=RAW_DATASET_PREFIX):
    result = subprocess.run(
        ["git", "-C", str(project_root), "ls-files", "--", pathspec],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git ls-files failed")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def run_command(command, project_root):
    env = os.environ.copy()
    env.update(command.env)
    try:
        result = subprocess.run(
            command.args,
            cwd=project_root,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as exc:
        return CommandResult(127, "", str(exc))
    return CommandResult(result.returncode, result.stdout, result.stderr)


def parse_int_set(value):
    if value is None:
        return set()
    if isinstance(value, (list, tuple, set)):
        raw_values = value
    else:
        raw_values = str(value).replace(",", " ").split()
    values = set()
    for item in raw_values:
        try:
            values.add(int(float(str(item))))
        except ValueError:
            continue
    return values


def manifest_stage_map(manifest):
    stages = manifest.get("curated_result_stages")
    if not isinstance(stages, list):
        return {}
    result = {}
    for stage in stages:
        if isinstance(stage, dict) and stage.get("directory"):
            result[str(stage["directory"])] = stage
    return result


def validate_repro_01(context):
    manifest = read_json(MANIFEST_PATH, "REPRO-01", context)
    if not manifest:
        return
    if not str(manifest.get("manifest_schema", "")).strip():
        context.fail("REPRO-01", "manifest_schema is required")

    environment = manifest.get("environment")
    if not isinstance(environment, dict):
        context.fail("REPRO-01", "environment metadata is required")
        environment = {}
    packages = environment.get("packages")
    if not isinstance(packages, dict) or not packages:
        context.fail("REPRO-01", "environment package metadata is required")
    else:
        missing_packages = sorted(REQUIRED_PACKAGE_NAMES - set(packages))
        if missing_packages:
            context.fail("REPRO-01", f"missing package metadata: {', '.join(missing_packages)}")
        for name in REQUIRED_PACKAGE_NAMES & set(packages):
            metadata = packages.get(name)
            if not isinstance(metadata, dict) or "available" not in metadata:
                context.fail("REPRO-01", f"package metadata for {name} must record availability")

    git = manifest.get("git")
    if not isinstance(git, dict):
        context.fail("REPRO-01", "git provenance is required")
    else:
        for key in ["commit", "branch", "tracked_raw_dataset_path_count", "tracked_raw_dataset_paths"]:
            if key not in git:
                context.fail("REPRO-01", f"git provenance missing {key}")

    stages = manifest_stage_map(manifest)
    for label, directory in REQUIRED_CURATED_STAGE_DIRS.items():
        directory_text = str(directory)
        stage = stages.get(directory_text)
        if not stage:
            context.fail("REPRO-01", f"manifest missing curated result directory for {label}: {directory_text}")
            continue
        if not (context.project_root / directory).is_dir():
            context.fail("REPRO-01", f"curated result directory does not exist: {directory_text}")
        inventory = stage.get("inventory")
        if not isinstance(inventory, dict) or not inventory.get("exists") or int(inventory.get("artifact_count", 0) or 0) <= 0:
            context.fail("REPRO-01", f"{label} inventory must record existing nonempty artifacts")
        defaults = stage.get("launcher_defaults")
        if not isinstance(defaults, dict):
            context.fail("REPRO-01", f"{label} launcher defaults are required")
            defaults = {}
        for key in REQUIRED_STAGE_DEFAULTS[directory_text]:
            if key not in defaults or str(defaults.get(key, "")).strip() == "":
                context.fail("REPRO-01", f"{label} launcher defaults missing {key}")
        if not parse_int_set(defaults.get("SEEDS")):
            context.fail("REPRO-01", f"{label} launcher defaults must include seeds")
        if not str(defaults.get("BUDGETS", "")).strip():
            context.fail("REPRO-01", f"{label} launcher defaults must include budgets")
        if "candidate" in label.lower():
            counts = parse_int_set(defaults.get("CANDIDATE_COUNTS"))
            if not counts:
                context.fail("REPRO-01", f"{label} launcher defaults must include candidate counts")
        else:
            candidate_keys = ["RCSS_RANDOM_CANDIDATES", "RCSS_QUALITY_CANDIDATES"]
            if not any(parse_int_set(defaults.get(key)) for key in candidate_keys):
                context.fail("REPRO-01", f"{label} launcher defaults must include candidate counts")
    if not context.has_failures("REPRO-01"):
        context.pass_check("REPRO-01", "manifest contains curated Stage 12/13/14 inventories, launcher defaults, environment package metadata, git provenance, seeds, budgets, and candidate counts")


def raw_dataset_reference_is_allowed(line):
    lowered = line.lower()
    if RAW_DATASET_PREFIX not in line:
        return True
    return any(token in lowered for token in ALLOWED_RAW_DATASET_DOC_CONTEXT)


def validate_repro_02(context):
    try:
        tracked = git_ls_files(context.project_root, RAW_DATASET_PREFIX)
    except Exception as exc:
        context.fail("REPRO-02", f"could not verify tracked raw dataset hygiene: {exc}")
        tracked = []
    if tracked:
        context.fail("REPRO-02", f"tracked raw dataset paths are forbidden: {tracked}")

    offenders = []
    for doc in DOCS_TO_SCAN:
        full_path = context.project_root / doc
        if not full_path.exists():
            continue
        text = full_path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if RAW_DATASET_PREFIX in line and not raw_dataset_reference_is_allowed(line):
                offenders.append(f"{doc}:{line_number}")
    if offenders:
        context.fail("REPRO-02", "paper-visible docs cite raw dataset paths as evidence: " + ", ".join(offenders))
    if not context.has_failures("REPRO-02"):
        context.pass_check("REPRO-02", "git tracks no raw dataset paths and paper-visible docs do not use raw datasets as evidence")


def validate_repro_03(context):
    manifest = read_json(MANIFEST_PATH, "REPRO-03", context)
    stages = manifest_stage_map(manifest)
    missing = []
    for label, directory in REQUIRED_CURATED_STAGE_DIRS.items():
        if str(directory) not in stages:
            missing.append(f"{label}: absent from manifest")
        if not (context.project_root / directory).is_dir():
            missing.append(f"{label}: missing directory {directory}")
    for item in missing:
        context.fail("REPRO-03", item)

    readme = read_text(RESULTS_ROOT / "README.md", "REPRO-03", context)
    for directory in REQUIRED_CURATED_STAGE_DIRS.values():
        if str(directory) not in readme:
            context.fail("REPRO-03", f"results README does not reference curated directory {directory}")
    for required in ["reproducibility_manifest.json", "REPRODUCIBILITY_MANIFEST.md", "paper_sources/"]:
        if required not in readme:
            context.fail("REPRO-03", f"results README missing artifact reference: {required}")
    if not context.has_failures("REPRO-03"):
        context.pass_check("REPRO-03", "curated result directories named in manifest/docs exist and README references manifest and paper_sources")


def csv_has_rows(path):
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        rows = list(reader)
    return len(rows) > 1


def validate_repro_04(context):
    paper_dir = context.project_root / PAPER_SOURCES_DIR
    if not paper_dir.is_dir():
        context.fail("REPRO-04", f"missing paper_sources directory: {PAPER_SOURCES_DIR}")
        return
    for name in REQUIRED_PAPER_SOURCE_CSVS:
        relative = PAPER_SOURCES_DIR / name
        path = context.project_root / relative
        if not path.exists():
            context.fail("REPRO-04", f"missing required generated CSV: {name}")
            continue
        if path.stat().st_size == 0 or not csv_has_rows(path):
            context.fail("REPRO-04", f"generated CSV is empty or header-only: {name}")
            continue
        frame = read_csv_frame(relative, "REPRO-04", context)
        missing = sorted(REQUIRED_PROVENANCE_COLUMNS - set(frame.columns))
        if missing:
            context.fail("REPRO-04", f"{name} missing provenance columns: {', '.join(missing)}")
        for column in REQUIRED_PROVENANCE_COLUMNS & set(frame.columns):
            if frame[column].isna().any() or (frame[column].astype(str).str.strip() == "").any():
                context.fail("REPRO-04", f"{name} has blank provenance values in {column}")
    for name in REQUIRED_PAPER_SOURCE_MARKDOWN:
        relative = PAPER_SOURCES_DIR / name
        path = context.project_root / relative
        if not path.exists() or path.stat().st_size == 0:
            context.fail("REPRO-04", f"missing or empty generated Markdown: {name}")
    if not context.has_failures("REPRO-04"):
        context.pass_check("REPRO-04", "paper_sources CSV/Markdown artifacts are nonempty and CSV rows carry source_stage/source_dir/source_csv provenance")


def required_smoke_commands(project_root):
    smoke_root = Path(os.environ.get("TMPDIR", "/tmp")) / "trace_sl_phase6_smoke"
    common = {
        "DRY_RUN": "1",
        "PYTHON_BIN": "python",
        "DATA_ROOT": "TRC-23-02333/dataset/PeMS7_228",
        "SEEDS": "25",
        "BUDGETS": "0.20",
        "NUM_LAYOUTS": "1",
        "RCSS_RANDOM_CANDIDATES": "1",
        "RCSS_QUALITY_CANDIDATES": "1",
        "SCENARIO_COUNT": "1",
        "VALIDATION_SWAP_STARTS": "1",
        "VALIDATION_SWAP_ITER": "1",
        "VALIDATION_SWAP_ADD_POOL": "1",
        "VALIDATION_SWAP_REMOVE_POOL": "1",
        "THREADS_PER_JOB": "1",
        "MAX_TEST_STEPS": "1",
    }
    specs = []
    for script in LAUNCHER_SCRIPTS:
        env = dict(common)
        env["OUTPUT_DIR"] = str(smoke_root / Path(script).stem)
        if "candidate_sensitivity" in script:
            env["CANDIDATE_COUNTS"] = "50 100 200 500"
        specs.append(CommandSpec(SMOKE_LABELS[script], ["bash", script], env))
    return specs


def syntax_commands():
    return [CommandSpec(f"bash -n {script}", ["bash", "-n", script]) for script in LAUNCHER_SCRIPTS]


def phase_validator_commands(project_root):
    return [
        CommandSpec("Phase 4 validator", ["python", str(PHASE4_VALIDATOR)]),
        CommandSpec("Phase 5 validator", ["python", str(PHASE5_VALIDATOR), "--project-root", str(project_root)]),
    ]


def command_script(command):
    if len(command.args) >= 2 and command.args[0] == "bash" and command.args[1] != "-n":
        return command.args[1]
    return ""


def validate_required_smoke_set(commands, context):
    present = {command_script(command) for command in commands if command.env.get("DRY_RUN") == "1"}
    for script, label in SMOKE_LABELS.items():
        if script not in present:
            context.fail("REPRO-05", f"required DRY_RUN smoke command missing: {label} ({script})")


def run_command_group(commands, context, requirement="REPRO-05"):
    for command in commands:
        result = run_command(command, context.project_root)
        if result.returncode != 0:
            stderr = result.stderr.strip()
            stdout = result.stdout.strip()
            detail = stderr or stdout or f"exit {result.returncode}"
            context.fail(requirement, f"{command.label} failed: {detail}")
        else:
            context.detail(requirement, f"{command.label} passed")


def string_values(frame, column):
    if column not in frame.columns:
        return set()
    return {value for value in frame[column].dropna().astype(str).str.strip() if value and value != "nan"}


def numeric_values(frame, column):
    if column not in frame.columns:
        return set()
    return set(pd.to_numeric(frame[column], errors="coerce").dropna().astype(int).tolist())


def validate_stage12_rows(context):
    frame = read_csv_frame(STAGE12_DIR / "combined_metrics.csv", "REPRO-05", context)
    if frame.empty:
        return
    for column in ["method", "layout_type"]:
        if column not in frame.columns:
            context.fail("REPRO-05", f"Stage 12 combined_metrics.csv missing {column}")
            return
    gls = frame[frame["method"].astype(str) == "gls_map"]
    if gls.empty:
        context.fail("REPRO-05", "Stage 12 combined_metrics.csv has no method == gls_map rows")
        return
    layouts = string_values(gls, "layout_type")
    missing_layouts = sorted(REQUIRED_BASELINE_LAYOUTS - layouts)
    if missing_layouts:
        context.fail("REPRO-05", "Stage 12 missing required baseline/main layout rows: " + ", ".join(missing_layouts))


def validate_stage14_robustness_rows(context):
    frame = read_csv_frame(STAGE14_ROBUSTNESS_DIR / "combined_metrics.csv", "REPRO-05", context)
    if frame.empty:
        return
    for column in ["method", "layout_type", "robustness_condition"]:
        if column not in frame.columns:
            context.fail("REPRO-05", f"Stage 14 robustness combined_metrics.csv missing {column}")
            return
    gls = frame[frame["method"].astype(str) == "gls_map"]
    if gls.empty:
        context.fail("REPRO-05", "Stage 14 robustness has no method == gls_map rows")
    if "validation_swap_selected" not in string_values(gls, "layout_type"):
        context.fail("REPRO-05", "Stage 14 robustness lacks layout_type == validation_swap_selected rows")
    missing_conditions = sorted(REQUIRED_ROBUSTNESS_CONDITIONS - string_values(gls, "robustness_condition"))
    if missing_conditions:
        context.fail("REPRO-05", "Stage 14 robustness missing conditions: " + ", ".join(missing_conditions))


def validate_candidate_count_rows(context):
    for label, relative in [
        ("Stage 14 candidate sensitivity", STAGE14_CANDIDATE_DIR / "combined_metrics.csv"),
        ("Stage 14 candidate runtime", STAGE14_CANDIDATE_DIR / "runtime_candidate_sensitivity.csv"),
        ("Stage 14 candidate timing", STAGE14_CANDIDATE_DIR / "stage14_timing.csv"),
    ]:
        frame = read_csv_frame(relative, "REPRO-05", context)
        if frame.empty:
            continue
        if "candidate_count" not in frame.columns:
            context.fail("REPRO-05", f"{label} missing candidate_count column")
            continue
        if "method" in frame.columns:
            method_values = string_values(frame, "method")
            if "gls_map" in method_values:
                frame = frame[frame["method"].astype(str) == "gls_map"]
        counts = numeric_values(frame, "candidate_count")
        missing = sorted(REQUIRED_CANDIDATE_COUNTS - counts)
        if missing:
            context.fail("REPRO-05", f"{label} missing candidate counts: {missing}")


def validate_repro_05(context):
    smoke_commands = required_smoke_commands(context.project_root)
    validate_required_smoke_set(smoke_commands, context)
    run_command_group(phase_validator_commands(context.project_root), context)
    run_command_group(syntax_commands(), context)
    run_command_group(smoke_commands, context)
    validate_stage12_rows(context)
    validate_stage14_robustness_rows(context)
    validate_candidate_count_rows(context)
    if not context.has_failures("REPRO-05"):
        context.pass_check("REPRO-05", "Phase 4/5 validators, bash -n launcher checks, DRY_RUN smoke launchers, and aggregate method/layout/condition/candidate rows all passed")


def run_all_checks(project_root):
    context = ValidationContext(project_root)
    validate_repro_01(context)
    validate_repro_02(context)
    validate_repro_03(context)
    validate_repro_04(context)
    validate_repro_05(context)
    return context


def print_status_rows(context):
    for requirement in REPRO_REQUIREMENTS:
        status = context.status_for(requirement)
        messages = context.messages_for(requirement)
        detail = "; ".join(messages) if messages else "no detail recorded"
        print(f"{requirement} {status}: {detail}")


def main(argv=None):
    args = parse_args(argv)
    project_root = Path(args.project_root).resolve() if args.project_root else Path(__file__).resolve().parents[3]
    context = run_all_checks(project_root)
    print_status_rows(context)
    return 1 if context.has_failures() else 0


if __name__ == "__main__":
    sys.exit(main())
