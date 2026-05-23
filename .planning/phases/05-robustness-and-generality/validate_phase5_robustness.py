import argparse
import json
import subprocess
import sys
from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError


RESULTS_ROOT = Path("TRC-23-02333") / "trace_sl_results"
ROBUSTNESS_DIR = RESULTS_ROOT / "pems7_228_stage14_robustness"
CANDIDATE_DIR = RESULTS_ROOT / "pems7_228_stage14_candidate_sensitivity"
REQUIRED_CANDIDATE_COUNTS = {50, 100, 200, 500}
CORE_ROBUSTNESS_FILES = [
    "combined_metrics.csv",
    "gls_map_layout_summary.csv",
    "gls_map_paired_delta_tests.csv",
    "combined_rcss_candidates.csv",
    "candidate_sensitivity_summary.csv",
    "rcss_selected_sources.csv",
    "SUMMARY.md",
]
CORE_CANDIDATE_FILES = [
    "combined_metrics.csv",
    "candidate_sensitivity_summary.csv",
    "runtime_candidate_sensitivity.csv",
    "stage14_timing.csv",
    "SUMMARY.md",
]
ROBUSTNESS_CONDITION_COLUMNS = [
    "robustness_family",
    "robustness_condition",
    "failure_rate",
    "noise_scale",
    "missing_rate",
    "missing_block_steps",
    "cost_budget",
    "split_mode",
]
CANDIDATE_ROBUSTNESS_COLUMNS = [
    "robustness_family",
    "robustness_condition",
    "failure_rate",
    "noise_scale",
    "missing_rate",
    "missing_block_steps",
    "cost_proxy",
    "cost_budget",
    "split_mode",
]
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
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
CURATED_EVIDENCE_DOCS = [
    RESULTS_ROOT / "README.md",
    ROBUSTNESS_DIR / "SUMMARY.md",
    CANDIDATE_DIR / "SUMMARY.md",
    Path(".planning") / "phases" / "05-robustness-and-generality" / "05-ROBUSTNESS-EVIDENCE-AUDIT.md",
]


class ValidationContext:
    def __init__(self, project_root):
        self.project_root = project_root
        self.errors = []
        self.warns = []
        self.frames = {}

    def fail(self, requirement, message):
        self.errors.append((requirement, message))

    def warn(self, requirement, message):
        self.warns.append((requirement, message))


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Validate Phase 5 Stage 14 robustness evidence artifacts")
    parser.add_argument("--project-root", "--root", dest="project_root", default=None)
    return parser.parse_args(argv)


def read_csv(path, requirement, context):
    if not path.exists():
        context.fail(requirement, f"missing required CSV: {path}")
        return pd.DataFrame()
    if path.stat().st_size == 0:
        context.fail(requirement, f"empty required CSV: {path}")
        return pd.DataFrame()
    try:
        frame = pd.read_csv(path)
    except EmptyDataError:
        context.fail(requirement, f"empty required CSV: {path}")
        return pd.DataFrame()
    except Exception as exc:
        context.fail(requirement, f"could not read CSV {path}: {exc}")
        return pd.DataFrame()
    if frame.empty:
        context.fail(requirement, f"CSV has no rows: {path}")
    return frame


def check_required_paths(root, relative_dir, file_names, requirement, context):
    directory = root / relative_dir
    if not directory.exists() or not directory.is_dir():
        context.fail(requirement, f"missing required directory: {directory}")
        return directory
    for name in file_names:
        path = directory / name
        if not path.exists():
            context.fail(requirement, f"missing required artifact: {path}")
        elif path.is_file() and path.stat().st_size == 0:
            context.fail(requirement, f"empty required artifact: {path}")
    return directory


def missing_columns(frame, columns):
    return [name for name in columns if name not in frame.columns]


def numeric_series(frame, column):
    return pd.to_numeric(frame[column], errors="coerce")


def string_series(frame, column):
    return frame[column].astype(str)


def normalized_condition_values(frame):
    if "robustness_condition" not in frame.columns:
        return set()
    values = string_series(frame, "robustness_condition").replace({"nan": ""}).str.strip()
    return {value for value in values if value}


def condition_values_match_required(frame, required_conditions=None):
    required_conditions = required_conditions or REQUIRED_ROBUSTNESS_CONDITIONS
    return required_conditions.issubset(normalized_condition_values(frame))


def rows_for_condition(frame, condition):
    if "robustness_condition" not in frame.columns:
        return pd.DataFrame()
    return frame[string_series(frame, "robustness_condition") == condition]


def gls_rows(frame, requirement, context):
    if "method" not in frame.columns:
        context.fail(requirement, "combined_metrics.csv missing method column")
        return pd.DataFrame()
    gls = frame[string_series(frame, "method") == "gls_map"].copy()
    if gls.empty:
        context.fail(requirement, "combined_metrics.csv has no held-out method == gls_map rows")
    return gls


def has_positive_value(frame, column):
    if column not in frame.columns:
        return False
    values = numeric_series(frame, column).dropna()
    return bool((values > 0).any())


def has_value(frame, column, expected):
    if column not in frame.columns:
        return False
    values = string_series(frame, column).str.lower()
    return bool((values == str(expected).lower()).any())


def valid_boolish_true(series):
    values = series.dropna()
    if values.empty:
        return False
    if values.dtype == bool:
        return bool(values.any())
    return bool(values.astype(str).str.lower().isin(["true", "1", "yes"]).any())


def check_common_robustness_schema(frames, context):
    for name, frame in frames.items():
        missing = missing_columns(frame, ["robustness_condition"])
        if missing:
            context.fail("ROBUST-01", f"{name} missing condition-preserving columns: {', '.join(missing)}")
    for name in ["combined_metrics", "gls_map_layout_summary", "gls_map_paired_delta_tests"]:
        frame = frames.get(name, pd.DataFrame())
        missing = missing_columns(frame, ROBUSTNESS_CONDITION_COLUMNS)
        if missing:
            context.fail("ROBUST-01", f"{name} missing required robustness columns: {', '.join(missing)}")
    for name in ["combined_rcss_candidates", "candidate_sensitivity_summary", "rcss_selected_sources"]:
        frame = frames.get(name, pd.DataFrame())
        missing = missing_columns(frame, CANDIDATE_ROBUSTNESS_COLUMNS)
        if missing:
            context.fail("ROBUST-01", f"{name} missing required candidate robustness columns: {', '.join(missing)}")


def check_candidate_condition_coverage(frames, context):
    metrics = frames.get("combined_metrics", pd.DataFrame())
    if not condition_values_match_required(metrics):
        return
    for name in ["combined_rcss_candidates", "candidate_sensitivity_summary", "rcss_selected_sources"]:
        frame = frames.get(name, pd.DataFrame())
        if frame.empty:
            continue
        missing_conditions = sorted(REQUIRED_ROBUSTNESS_CONDITIONS - normalized_condition_values(frame))
        if missing_conditions:
            context.fail("ROBUST-01", f"{name} missing required robustness_condition values: {missing_conditions}")


def check_condition_in_aggregates(frames, condition, requirement, context):
    for name in ["gls_map_layout_summary", "gls_map_paired_delta_tests", "candidate_sensitivity_summary", "rcss_selected_sources"]:
        frame = frames.get(name, pd.DataFrame())
        if frame.empty:
            continue
        if rows_for_condition(frame, condition).empty:
            context.fail(requirement, f"{name} missing robustness_condition={condition}")


def validate_robust_01(gls, frames, context):
    required = ["failure_rate", "active_sensor_count", "dropped_sensor_count"]
    missing = missing_columns(gls, required)
    if missing:
        context.fail("ROBUST-01", f"combined_metrics.csv missing sensor-failure columns: {', '.join(missing)}")
        return
    for condition, rate in [("failure_0.05", 0.05), ("failure_0.10", 0.10), ("failure_0.20", 0.20)]:
        sub = rows_for_condition(gls, condition)
        if sub.empty:
            context.fail("ROBUST-01", f"missing held-out gls_map rows for {condition}")
            continue
        if not (numeric_series(sub, "failure_rate").round(6) == round(rate, 6)).any():
            context.fail("ROBUST-01", f"{condition} rows do not record failure_rate={rate}")
        if not has_positive_value(sub, "dropped_sensor_count"):
            context.fail("ROBUST-01", f"{condition} rows do not record dropped sensors")
        if not has_positive_value(sub, "active_sensor_count"):
            context.fail("ROBUST-01", f"{condition} rows do not record active sensors")
        check_condition_in_aggregates(frames, condition, "ROBUST-01", context)


def validate_robust_02(gls, frames, context):
    missing = missing_columns(gls, ["noise_scale"])
    if missing:
        context.fail("ROBUST-02", f"combined_metrics.csv missing observation-noise columns: {', '.join(missing)}")
        return
    sub = gls[has_condition_or_family(gls, condition_prefix="noise_", family="observation_noise")]
    if sub.empty:
        context.fail("ROBUST-02", "missing held-out gls_map observation-noise rows")
        return
    if not has_positive_value(sub, "noise_scale"):
        context.fail("ROBUST-02", "observation-noise rows do not record nonzero noise_scale")
    for condition in sorted(string_series(sub, "robustness_condition").unique()):
        check_condition_in_aggregates(frames, condition, "ROBUST-02", context)


def has_condition_or_family(frame, condition_prefix=None, family=None):
    mask = pd.Series(False, index=frame.index)
    if condition_prefix and "robustness_condition" in frame.columns:
        mask = mask | string_series(frame, "robustness_condition").str.startswith(condition_prefix)
    if family and "robustness_family" in frame.columns:
        mask = mask | (string_series(frame, "robustness_family") == family)
    return mask


def validate_robust_03(gls, frames, context):
    missing = missing_columns(gls, ["missing_rate", "missing_block_steps"])
    if missing:
        context.fail("ROBUST-03", f"combined_metrics.csv missing missingness columns: {', '.join(missing)}")
        return
    random_rows = gls[has_condition_or_family(gls, condition_prefix="random_missing", family="random_missing")]
    block_rows = gls[has_condition_or_family(gls, condition_prefix="block_missing", family="block_missing")]
    if random_rows.empty:
        context.fail("ROBUST-03", "missing held-out gls_map random missingness rows")
    elif not has_positive_value(random_rows, "missing_rate"):
        context.fail("ROBUST-03", "random missingness rows do not record nonzero missing_rate")
    if block_rows.empty:
        context.fail("ROBUST-03", "missing held-out gls_map block missingness rows")
    elif not has_positive_value(block_rows, "missing_block_steps"):
        context.fail("ROBUST-03", "block missingness rows do not record nonzero missing_block_steps")
    for frame in [random_rows, block_rows]:
        if not frame.empty:
            for condition in sorted(string_series(frame, "robustness_condition").unique()):
                check_condition_in_aggregates(frames, condition, "ROBUST-03", context)


def validate_robust_04(gls, frames, context):
    required = ["cost_budget", "layout_sensor_cost", "cost_feasible"]
    missing = missing_columns(gls, required)
    if missing:
        context.fail("ROBUST-04", f"combined_metrics.csv missing cost-proxy columns: {', '.join(missing)}")
        return
    cost_rows = gls[has_condition_or_family(gls, condition_prefix="cost_proxy", family="cost_proxy")]
    if cost_rows.empty:
        context.fail("ROBUST-04", "missing held-out gls_map cost proxy rows")
        return
    if not has_positive_value(cost_rows, "cost_budget"):
        context.fail("ROBUST-04", "cost proxy rows do not record positive cost_budget")
    if not has_positive_value(cost_rows, "layout_sensor_cost"):
        context.fail("ROBUST-04", "cost proxy rows do not record layout_sensor_cost")
    if not valid_boolish_true(cost_rows["cost_feasible"]):
        context.fail("ROBUST-04", "cost proxy rows do not record any feasible layout")
    for condition in sorted(string_series(cost_rows, "robustness_condition").unique()):
        check_condition_in_aggregates(frames, condition, "ROBUST-04", context)


def validate_robust_05(gls, frames, context):
    missing = missing_columns(gls, ["split_mode"])
    if missing:
        context.fail("ROBUST-05", f"combined_metrics.csv missing temporal-shift columns: {', '.join(missing)}")
        return
    temporal_rows = gls[(string_series(gls, "split_mode").str.lower() == "chronological") | has_condition_or_family(gls, condition_prefix="chronological", family="temporal_shift")]
    if temporal_rows.empty:
        context.fail("ROBUST-05", "missing held-out gls_map split_mode=chronological rows")
        return
    for condition in sorted(string_series(temporal_rows, "robustness_condition").unique()):
        check_condition_in_aggregates(frames, condition, "ROBUST-05", context)


def candidate_counts(frame, requirement, artifact_name, context, require_runtime=False):
    if frame.empty:
        return set()
    if "candidate_count" not in frame.columns:
        context.fail(requirement, f"{artifact_name} missing candidate_count column")
        return set()
    work = frame.copy()
    work["candidate_count"] = pd.to_numeric(work["candidate_count"], errors="coerce")
    if require_runtime:
        if "runtime_seconds" not in work.columns:
            context.fail(requirement, f"{artifact_name} missing runtime_seconds column")
            return set()
        work["runtime_seconds"] = pd.to_numeric(work["runtime_seconds"], errors="coerce")
        work = work[work["runtime_seconds"].notna() & (work["runtime_seconds"] >= 0)]
        if "status" in work.columns:
            status = string_series(work, "status").str.lower()
            work = work[status.isin(["success", "completed", "complete", "ok", "pass", "passed"])]
    if "method" in work.columns:
        work = work[string_series(work, "method") == "gls_map"]
        if work.empty:
            context.fail(requirement, f"{artifact_name} has no method == gls_map candidate rows")
    counts = set(work["candidate_count"].dropna().astype(int).tolist())
    missing = REQUIRED_CANDIDATE_COUNTS - counts
    if missing:
        context.fail(requirement, f"{artifact_name} missing candidate counts: {sorted(missing)}")
    return counts


def load_valid_caveat(candidate_dir):
    path = candidate_dir / "candidate_sensitivity_caveat.json"
    if not path.exists():
        return None, ["candidate_sensitivity_caveat.json is absent"]
    try:
        caveat = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, [f"candidate_sensitivity_caveat.json is unreadable: {exc}"]
    errors = []
    if caveat.get("requirement") != "ROBUST-06":
        errors.append("requirement must be ROBUST-06")
    if caveat.get("allowed_exception") is not True:
        errors.append("allowed_exception must be true")
    missing = caveat.get("missing_candidate_counts")
    completed = caveat.get("completed_candidate_counts")
    if not isinstance(missing, list) or not missing:
        errors.append("missing_candidate_counts must be nonempty")
    if not isinstance(completed, list) or not completed:
        errors.append("completed_candidate_counts must be nonempty")
    if not str(caveat.get("reason", "")).strip():
        errors.append("reason must be nonempty")
    if caveat.get("evidence_attempted") is not True:
        errors.append("evidence_attempted must be true")
    disposition = str(caveat.get("validator_disposition", "")).lower()
    if "limited" not in disposition or "tractability" not in disposition:
        errors.append("validator_disposition must indicate limited tractability")
    return caveat if not errors else None, errors


def tracked_dataset_paths(project_root):
    try:
        result = subprocess.run(
            ["git", "-C", str(project_root), "ls-files", "--", RAW_DATASET_PREFIX],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as exc:
        return [], f"could not run git ls-files for raw dataset hygiene: {exc}"
    if result.returncode != 0:
        stderr = result.stderr.strip()
        lowered = stderr.lower()
        if "not a git repository" in lowered or "不是 git" in lowered:
            return [], None
        return [], f"git ls-files failed for raw dataset hygiene: {stderr}"
    paths = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return paths, None


def docs_referencing_raw_dataset(project_root, doc_paths=None):
    offenders = []
    for relative in doc_paths or CURATED_EVIDENCE_DOCS:
        path = project_root / relative
        if not path.exists() or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if RAW_DATASET_PREFIX in text:
            offenders.append(str(relative))
    return offenders


def validate_raw_data_hygiene(root, context):
    tracked, error = tracked_dataset_paths(root)
    if error:
        context.fail("ROBUST-06", error)
    if tracked:
        context.fail("ROBUST-06", f"tracked raw dataset paths are not allowed: {tracked}")
    offenders = docs_referencing_raw_dataset(root)
    if offenders:
        context.fail("ROBUST-06", f"curated evidence docs reference raw dataset paths: {offenders}")


def validate_robust_06(root, context):
    candidate_dir = check_required_paths(root, CANDIDATE_DIR, CORE_CANDIDATE_FILES, "ROBUST-06", context)
    frames = {
        "combined_metrics": read_csv(candidate_dir / "combined_metrics.csv", "ROBUST-06", context),
        "candidate_sensitivity_summary": read_csv(candidate_dir / "candidate_sensitivity_summary.csv", "ROBUST-06", context),
        "runtime_candidate_sensitivity": read_csv(candidate_dir / "runtime_candidate_sensitivity.csv", "ROBUST-06", context),
        "stage14_timing": read_csv(candidate_dir / "stage14_timing.csv", "ROBUST-06", context),
    }
    candidate_error_start = len(context.errors)
    candidate_counts(frames["combined_metrics"], "ROBUST-06", "combined_metrics.csv", context)
    candidate_counts(frames["candidate_sensitivity_summary"], "ROBUST-06", "candidate_sensitivity_summary.csv", context)
    candidate_counts(frames["runtime_candidate_sensitivity"], "ROBUST-06", "runtime_candidate_sensitivity.csv", context, require_runtime=True)
    candidate_counts(frames["stage14_timing"], "ROBUST-06", "stage14_timing.csv", context, require_runtime=True)
    candidate_errors = context.errors[candidate_error_start:]
    if candidate_errors:
        caveat, caveat_errors = load_valid_caveat(candidate_dir)
        if caveat is not None:
            context.errors = context.errors[:candidate_error_start]
            missing = sorted(int(value) for value in caveat["missing_candidate_counts"])
            completed = sorted(int(value) for value in caveat["completed_candidate_counts"])
            context.warn("ROBUST-06", f"limited tractability caveat accepted; missing={missing}; completed={completed}")
        else:
            context.fail("ROBUST-06", "invalid ROBUST-06 caveat: " + "; ".join(caveat_errors))


def validate_robustness_bundle(root, context):
    robustness_dir = check_required_paths(root, ROBUSTNESS_DIR, CORE_ROBUSTNESS_FILES, "ROBUST-01", context)
    frames = {
        "combined_metrics": read_csv(robustness_dir / "combined_metrics.csv", "ROBUST-01", context),
        "gls_map_layout_summary": read_csv(robustness_dir / "gls_map_layout_summary.csv", "ROBUST-01", context),
        "gls_map_paired_delta_tests": read_csv(robustness_dir / "gls_map_paired_delta_tests.csv", "ROBUST-01", context),
        "combined_rcss_candidates": read_csv(robustness_dir / "combined_rcss_candidates.csv", "ROBUST-01", context),
        "candidate_sensitivity_summary": read_csv(robustness_dir / "candidate_sensitivity_summary.csv", "ROBUST-01", context),
        "rcss_selected_sources": read_csv(robustness_dir / "rcss_selected_sources.csv", "ROBUST-01", context),
    }
    context.frames.update(frames)
    check_common_robustness_schema(frames, context)
    check_candidate_condition_coverage(frames, context)
    gls = gls_rows(frames["combined_metrics"], "ROBUST-01", context)
    validate_robust_01(gls, frames, context)
    validate_robust_02(gls, frames, context)
    validate_robust_03(gls, frames, context)
    validate_robust_04(gls, frames, context)
    validate_robust_05(gls, frames, context)


def messages_for(requirement, context):
    errors = [message for req, message in context.errors if req == requirement]
    warns = [message for req, message in context.warns if req == requirement]
    if errors:
        return "FAIL", errors
    if warns:
        return "WARN", warns
    return "PASS", ["artifact-backed evidence and required schema checks passed"]


def print_status_rows(context):
    for requirement in ["ROBUST-01", "ROBUST-02", "ROBUST-03", "ROBUST-04", "ROBUST-05", "ROBUST-06"]:
        status, messages = messages_for(requirement, context)
        print(f"{requirement} {status}: {'; '.join(messages)}")


def main(argv=None):
    args = parse_args(argv)
    project_root = Path(args.project_root).resolve() if args.project_root else Path(__file__).resolve().parents[3]
    context = ValidationContext(project_root)
    validate_robustness_bundle(project_root, context)
    validate_robust_06(project_root, context)
    validate_raw_data_hygiene(project_root, context)
    print_status_rows(context)
    if context.errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
