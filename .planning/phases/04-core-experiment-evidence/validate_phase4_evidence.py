#!/usr/bin/env python3
import argparse
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[3]
RESULTS_ROOT = PROJECT_ROOT / "TRC-23-02333" / "trace_sl_results"
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"

PHASE_DIR = PROJECT_ROOT / ".planning" / "phases" / "04-core-experiment-evidence"
AUDIT_PATH = PHASE_DIR / "04-EVIDENCE-AUDIT.md"
DATASET_STATUS_PATH = PHASE_DIR / "04-DATASET-CLAIM-STATUS.md"
CONTRACT_PATH = PROJECT_ROOT / ".planning" / "phases" / "01-claim-evidence-contract" / "01-CLAIM-EVIDENCE-CONTRACT.md"
RESULTS_README_PATH = RESULTS_ROOT / "README.md"

P228_STAGE12_DIR = RESULTS_ROOT / "pems7_228_stage12_baseline_portfolio"
P1026_DIR = RESULTS_ROOT / "pems7_1026_stage11_auto_weight"
SEATTLE_DIR = RESULTS_ROOT / "seattle_stage11_auto_weight_light"
STAGE13_DIR = RESULTS_ROOT / "pems7_228_stage13_candidate_sensitivity"

REQUIREMENTS = ["EXP-01", "EXP-02", "EXP-03", "EXP-04", "EXP-05", "EXP-06"]
REQUIRED_STAGE12_FILES = [
    "combined_metrics.csv",
    "gls_map_layout_summary.csv",
    "gls_map_paired_delta_tests.csv",
    "certificate_correlation_summary.csv",
    "combined_certificate_correlations.csv",
    "combined_rcss_candidates.csv",
    "SUMMARY.md",
]
REQUIRED_STAGE12_LAYOUTS = {
    "validation_swap_selected",
    "rcss_selected",
    "multistart_swap_by_validation",
    "greedy_a_trace",
    "greedy_d_logdet",
    "observability_proxy",
    "graph_sampling_laplacian",
    "qr_pod_modes",
}
REQUIRED_METRIC_COLUMNS = {
    "dataset",
    "budget",
    "layout_type",
    "method",
    "split_seed",
    "mae",
    "rmse",
    "mape",
}
REQUIRED_STAT_COLUMNS = {
    "ci95_low",
    "ci95_high",
    "cohens_dz",
    "paired_t_p",
    "wilcoxon_p",
    "count",
}
PENDING_MARKERS = ("pending", "regeneration-required", "runtime unavailable", "not yet present")


@dataclass
class CheckResult:
    requirement: str
    status: str
    evidence: str
    detail: str


def status_rank(status):
    return {"PASS": 0, "WARN": 1, "FAIL": 2}.get(status, 2)


def worst_status(statuses):
    return max(statuses, key=status_rank)


def relative(path):
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def read_csv(path, errors):
    try:
        return pd.read_csv(path)
    except Exception as exc:  # noqa: BLE001 - validator should report corrupt curated artifacts.
        errors.append(CheckResult("INPUT", "FAIL", relative(path), f"could not read CSV: {exc}"))
        return None


def read_text(path, errors):
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 - validator should report corrupt curated docs.
        errors.append(CheckResult("INPUT", "FAIL", relative(path), f"could not read text: {exc}"))
        return ""


def require_files(root, names):
    return [name for name in names if not (root / name).exists()]


def has_pending_only_wording(text):
    lowered = text.lower()
    return any(marker in lowered for marker in PENDING_MARKERS)


def split_count_range(frame):
    grouped = frame.groupby(["budget", "layout_type"])["split_seed"].nunique()
    if grouped.empty:
        return 0, 0
    return int(grouped.min()), int(grouped.max())


def check_completed_stage12_metrics(errors):
    missing_files = require_files(P228_STAGE12_DIR, REQUIRED_STAGE12_FILES)
    if missing_files:
        return "FAIL", f"missing required Stage 12 files: {', '.join(missing_files)}", None

    seed_metrics = sorted(P228_STAGE12_DIR.glob("seed_*/metrics.csv"))
    if len(seed_metrics) != 10:
        return "FAIL", f"expected 10 Stage 12 seed metrics files, found {len(seed_metrics)}", None

    metrics = read_csv(P228_STAGE12_DIR / "combined_metrics.csv", errors)
    if metrics is None:
        return "FAIL", "combined_metrics.csv is unreadable", None
    missing_columns = sorted(REQUIRED_METRIC_COLUMNS - set(metrics.columns))
    if missing_columns:
        return "FAIL", f"combined_metrics.csv missing columns: {', '.join(missing_columns)}", None

    gls = metrics[metrics["method"] == "gls_map"].copy()
    if gls.empty:
        return "FAIL", "combined_metrics.csv lacks held-out method == gls_map rows", None
    min_splits, max_splits = split_count_range(gls)
    if min_splits < 10:
        return "FAIL", f"held-out GLS/MAP rows are incomplete: split_count_range={min_splits}..{max_splits}", None

    present_layouts = set(gls["layout_type"].dropna().astype(str).unique())
    missing_layouts = sorted(REQUIRED_STAGE12_LAYOUTS - present_layouts)
    if missing_layouts:
        return "FAIL", f"missing required Stage 12 layout labels: {', '.join(missing_layouts)}", None

    summary_text = read_text(P228_STAGE12_DIR / "SUMMARY.md", errors)
    if has_pending_only_wording(summary_text):
        return "FAIL", "Stage 12 SUMMARY.md contains pending-only wording", None

    detail = (
        f"PeMS7_228 Stage 12 has {len(seed_metrics)} seed metrics files; "
        f"held-out GLS/MAP split_count_range={min_splits}..{max_splits}; "
        f"required labels present: {', '.join(sorted(REQUIRED_STAGE12_LAYOUTS))}."
    )
    return "PASS", detail, gls


def check_exp01(errors):
    status, detail, _ = check_completed_stage12_metrics(errors)
    return CheckResult("EXP-01", status, relative(P228_STAGE12_DIR), detail)


def dataset_split_count(root, requirement, label, allowed_warning):
    errors = []
    metrics = read_csv(root / "combined_metrics.csv", errors)
    if metrics is None:
        return CheckResult(requirement, "FAIL", relative(root), "; ".join(result.detail for result in errors))
    gls = metrics[metrics["method"] == "gls_map"].copy()
    min_splits, max_splits = split_count_range(gls)
    if min_splits >= 10:
        status = "PASS"
        caveat = "meets ten-split target"
    else:
        status = "WARN" if allowed_warning else "FAIL"
        caveat = "lower-power/supporting caveat allowed by D-06/D-07" if allowed_warning else "missing required ten-split evidence"
    detail = f"{label} held-out GLS/MAP split_count_range={min_splits}..{max_splits}; {caveat}."
    return CheckResult(requirement, status, relative(root), detail)


def check_exp02():
    return dataset_split_count(P1026_DIR, "EXP-02", "PeMS7_1026 external evidence", allowed_warning=True)


def check_exp03(errors):
    required = ["SUMMARY.md", "combined_metrics.csv", "gls_map_layout_summary.csv", "gls_map_paired_delta_tests.csv", "certificate_correlation_summary.csv"]
    missing = require_files(SEATTLE_DIR, required)
    if missing:
        return CheckResult("EXP-03", "WARN", relative(SEATTLE_DIR), f"Seattle supporting evidence incomplete: missing {', '.join(missing)}; D-07 caveat applies.")
    readme = read_text(RESULTS_README_PATH, errors)
    status_doc = read_text(DATASET_STATUS_PATH, errors)
    needed = ["supporting/conditional", "Seattle"]
    if not all(token in readme and token in status_doc for token in needed):
        return CheckResult("EXP-03", "WARN", relative(SEATTLE_DIR), "Seattle exists but supporting/conditional status is not synchronized in README and status doc; D-07 caveat applies.")
    split_result = dataset_split_count(SEATTLE_DIR, "EXP-03", "Seattle supporting evidence", allowed_warning=True)
    split_result.detail += " README and dataset-status doc keep Seattle supporting/conditional."
    return split_result


def completed_evidence_dirs():
    return [P228_STAGE12_DIR, STAGE13_DIR]


def check_exp04(errors):
    failures = []
    details = []
    for root in completed_evidence_dirs():
        path = root / "gls_map_paired_delta_tests.csv"
        if not path.exists():
            failures.append(f"{relative(path)} missing")
            continue
        paired = read_csv(path, errors)
        if paired is None:
            failures.append(f"{relative(path)} unreadable")
            continue
        missing_columns = sorted(REQUIRED_STAT_COLUMNS - set(paired.columns))
        if missing_columns:
            failures.append(f"{relative(path)} missing statistical columns: {', '.join(missing_columns)}")
            continue
        if {"layout", "baseline"}.issubset(paired.columns):
            greedy_rows = paired[paired["baseline"].isin(["greedy_a_trace", "greedy_d_logdet"])]
            if root == P228_STAGE12_DIR and greedy_rows.empty:
                failures.append(f"{relative(path)} lacks greedy_a_trace/greedy_d_logdet Phase 3 baseline comparison rows")
            details.append(f"{relative(path)} has {len(paired)} rows and required interval/effect/test/count columns")
    if failures:
        return CheckResult("EXP-04", "FAIL", relative(P228_STAGE12_DIR), "; ".join(failures))
    return CheckResult("EXP-04", "PASS", relative(P228_STAGE12_DIR / "gls_map_paired_delta_tests.csv"), "; ".join(details))


def check_exp05(errors):
    failures = []
    details = []
    for root in [P228_STAGE12_DIR, STAGE13_DIR]:
        corr_summary = root / "certificate_correlation_summary.csv"
        combined_corr = root / "combined_certificate_correlations.csv"
        summary = root / "SUMMARY.md"
        for path in [corr_summary, combined_corr, summary]:
            if not path.exists():
                failures.append(f"{relative(path)} missing")
        if failures:
            continue
        corr = read_csv(combined_corr, errors)
        if corr is None:
            failures.append(f"{relative(combined_corr)} unreadable")
            continue
        missing = sorted({"method", "certificate", "pearson_mae", "spearman_mae"} - set(corr.columns))
        if missing:
            failures.append(f"{relative(combined_corr)} missing columns: {', '.join(missing)}")
            continue
        text = read_text(summary, errors).lower()
        if "empirical" not in text or "formal" not in text:
            failures.append(f"{relative(summary)} lacks empirical/non-formal certificate wording")
            continue
        details.append(f"{relative(root)} certificate summaries and empirical wording present")
    if failures:
        return CheckResult("EXP-05", "FAIL", relative(P228_STAGE12_DIR), "; ".join(failures))
    return CheckResult("EXP-05", "PASS", relative(P228_STAGE12_DIR), "; ".join(details))


def check_exp06(errors):
    required = ["SUMMARY.md", "combined_rcss_candidates.csv", "candidate_sensitivity_summary.csv", "runtime_candidate_sensitivity.csv"]
    missing = require_files(STAGE13_DIR, required)
    if missing:
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR), f"missing Stage 13 runtime/candidate sensitivity files: {', '.join(missing)}")

    summary_text = read_text(STAGE13_DIR / "SUMMARY.md", errors)
    if has_pending_only_wording(summary_text):
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR / "SUMMARY.md"), "Stage 13 summary contains pending/runtime-unavailable wording")
    lowered = summary_text.lower()
    if "candidate" not in lowered or "runtime" not in lowered or "tractability" not in lowered:
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR / "SUMMARY.md"), "Stage 13 summary lacks candidate/runtime/tractability wording")

    runtime = read_csv(STAGE13_DIR / "runtime_candidate_sensitivity.csv", errors)
    if runtime is None:
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR / "runtime_candidate_sensitivity.csv"), "runtime table unreadable")
    missing_cols = sorted({"candidate_count", "runtime_seconds"} - set(runtime.columns))
    if missing_cols:
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR / "runtime_candidate_sensitivity.csv"), f"runtime table missing columns: {', '.join(missing_cols)}")
    runtime_seconds = pd.to_numeric(runtime["runtime_seconds"], errors="coerce")
    candidate_counts = pd.to_numeric(runtime["candidate_count"], errors="coerce")
    if runtime_seconds.isna().any() or (runtime_seconds < 0).any():
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR / "runtime_candidate_sensitivity.csv"), "runtime_seconds must be measured nonnegative values")
    if candidate_counts.dropna().nunique() < 2:
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR / "runtime_candidate_sensitivity.csv"), "expected at least two candidate-count settings")

    candidates = read_csv(STAGE13_DIR / "combined_rcss_candidates.csv", errors)
    if candidates is None:
        return CheckResult("EXP-06", "FAIL", relative(STAGE13_DIR / "combined_rcss_candidates.csv"), "candidate diagnostics unreadable")
    source_count = int(candidates["source"].nunique()) if "source" in candidates.columns else 0
    return CheckResult(
        "EXP-06",
        "PASS",
        relative(STAGE13_DIR),
        f"Stage 13 has measured runtime for {candidate_counts.nunique()} candidate-count settings and candidate diagnostics across {source_count} sources.",
    )


def check_no_raw_dataset_evidence(errors):
    docs = [AUDIT_PATH, DATASET_STATUS_PATH, CONTRACT_PATH, RESULTS_README_PATH]
    offending = []
    for path in docs:
        text = read_text(path, errors)
        for line_number, line in enumerate(text.splitlines(), start=1):
            if RAW_DATASET_PREFIX in line and "do not" not in line.lower() and "out of scope" not in line.lower() and "must not" not in line.lower():
                offending.append(f"{relative(path)}:{line_number}")
    status = "FAIL" if offending else "PASS"
    detail = "raw dataset evidence citations found: " + ", ".join(offending) if offending else "No cited evidence path starts with TRC-23-02333/dataset/."
    return CheckResult("RAW-DATA", status, "phase docs", detail)


def run_checks():
    errors = []
    results = [
        check_exp01(errors),
        check_exp02(),
        check_exp03(errors),
        check_exp04(errors),
        check_exp05(errors),
        check_exp06(errors),
        check_no_raw_dataset_evidence(errors),
    ]
    return [result for result in results if result.requirement in REQUIREMENTS] + errors + [result for result in results if result.requirement == "RAW-DATA"]


def print_table(results):
    rows = [(result.requirement, result.status, result.evidence, result.detail) for result in results]
    widths = [
        max(len("Requirement"), *(len(row[0]) for row in rows)),
        max(len("Status"), *(len(row[1]) for row in rows)),
        max(len("Evidence"), *(len(row[2]) for row in rows)),
    ]
    print(f"{'Requirement':<{widths[0]}}  {'Status':<{widths[1]}}  {'Evidence':<{widths[2]}}  Detail")
    print(f"{'-' * widths[0]}  {'-' * widths[1]}  {'-' * widths[2]}  {'-' * 6}")
    for row in rows:
        print(f"{row[0]:<{widths[0]}}  {row[1]:<{widths[1]}}  {row[2]:<{widths[2]}}  {row[3]}")


def main():
    parser = argparse.ArgumentParser(description="Validate final Phase 4 TRACE-SL evidence artifacts without reading raw datasets")
    parser.add_argument("--fail-on-warn", action="store_true", help="Treat allowed WARN caveats as nonzero")
    args = parser.parse_args()
    results = run_checks()
    print_table(results)
    if any(result.status == "FAIL" for result in results):
        raise SystemExit(1)
    if args.fail_on_warn and any(result.status == "WARN" for result in results):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
