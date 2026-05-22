#!/usr/bin/env python3
import argparse
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[3]
RESULTS_ROOT_LABEL = "TRC-23-02333/trace_sl_results"
RESULTS_ROOT = PROJECT_ROOT / "TRC-23-02333" / "trace_sl_results"
RAW_DATASET_GUARD = "Raw datasets are out of scope: do not read TRC-23-02333/dataset artifacts."

P228_DIR = RESULTS_ROOT / "pems7_228_stage11_auto_weight_10split"
P1026_DIR = RESULTS_ROOT / "pems7_1026_stage11_auto_weight"
SEATTLE_DIR = RESULTS_ROOT / "seattle_stage11_auto_weight_light"
STAGE12_LAUNCHER = PROJECT_ROOT / "scripts" / "run_stage12_pems7_228.sh"
EVALUATOR = PROJECT_ROOT / "TRC-23-02333" / "transparent_estimator_eval.py"

REQUIRED_P228_FILES = [
    "combined_metrics.csv",
    "gls_map_layout_summary.csv",
    "gls_map_paired_delta_tests.csv",
    "certificate_correlation_summary.csv",
    "combined_rcss_candidates.csv",
    "SUMMARY.md",
]
FINAL_LAYOUTS = {"validation_swap_selected", "rcss_selected", "multistart_swap_by_validation"}
PORTFOLIO_LABELS = {
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
REQUIRED_PAIRED_COLUMNS = {"budget", "layout", "baseline", "delta_mean", "delta_std", "win_count", "count", "paired_t_p", "wilcoxon_p"}
REQUIREMENTS = ["EXP-01", "EXP-02", "EXP-03", "EXP-04", "EXP-05", "EXP-06"]


@dataclass
class CheckResult:
    requirement: str
    status: str
    evidence: str
    detail: str


def status_rank(status):
    return {"PASS": 0, "WARN": 1, "FAIL": 2}.get(status, 1)


def combine_status(*statuses):
    return max(statuses, key=status_rank)


def relative(path):
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def require_files(root, names):
    missing = [name for name in names if not (root / name).exists()]
    return missing


def read_csv(path, errors):
    try:
        return pd.read_csv(path)
    except Exception as exc:  # noqa: BLE001 - CLI should report corrupt curated input compactly.
        errors.append(f"FAIL|INPUT|{relative(path)}|could not read CSV: {exc}")
        return None


def read_text(path, errors):
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 - CLI should report corrupt curated input compactly.
        errors.append(f"FAIL|INPUT|{relative(path)}|could not read text: {exc}")
        return ""


def split_count_detail(frame):
    grouped = frame.groupby(["dataset", "budget", "layout_type", "method"])["split_seed"].nunique()
    if grouped.empty:
        return "no dataset/budget/layout/method groups found"
    min_count = int(grouped.min())
    max_count = int(grouped.max())
    dataset_names = ",".join(str(x) for x in sorted(frame["dataset"].dropna().unique()))
    budgets = ",".join(str(x) for x in sorted(frame["budget"].dropna().unique()))
    return f"datasets={dataset_names}; budgets={budgets}; split_count_range={min_count}..{max_count}"


def check_stage12_enablement(errors):
    launcher_text = read_text(STAGE12_LAUNCHER, errors)
    evaluator_text = read_text(EVALUATOR, errors)
    launcher_has_greedy = "--include-greedy" in launcher_text
    portfolio_flag_present = "--include-baseline-portfolio" in launcher_text
    evaluator_portfolio_enables_greedy = "args.include_greedy = True" in evaluator_text and "greedy_d_logdet" in evaluator_text
    if launcher_has_greedy:
        return "PASS", "Stage 12 launcher contains exact --include-greedy flag for greedy_a_trace and greedy_d_logdet rows."
    if portfolio_flag_present and evaluator_portfolio_enables_greedy:
        return "PASS", "Stage 12 launcher uses --include-baseline-portfolio; evaluator source confirms it enables greedy_a_trace and greedy_d_logdet."
    return "WARN", "Stage 12 source confirmation missing for greedy_a_trace/greedy_d_logdet row enablement."


def check_exp01(errors):
    missing = require_files(P228_DIR, REQUIRED_P228_FILES)
    if missing:
        return CheckResult("EXP-01", "FAIL", relative(P228_DIR), f"missing required PeMS7_228 primary evidence files: {', '.join(missing)}")

    metrics = read_csv(P228_DIR / "combined_metrics.csv", errors)
    if metrics is None:
        return CheckResult("EXP-01", "FAIL", relative(P228_DIR / "combined_metrics.csv"), "combined metrics are corrupt or unreadable")
    missing_cols = sorted(REQUIRED_METRIC_COLUMNS - set(metrics.columns))
    if missing_cols:
        return CheckResult("EXP-01", "FAIL", relative(P228_DIR / "combined_metrics.csv"), f"missing metric columns: {', '.join(missing_cols)}")

    gls = metrics[metrics["method"] == "gls_map"].copy()
    present_layouts = set(gls["layout_type"].dropna().astype(str).unique())
    missing_final = sorted(FINAL_LAYOUTS - present_layouts)
    missing_portfolio = sorted(PORTFOLIO_LABELS - present_layouts)
    stage12_status, stage12_detail = check_stage12_enablement(errors)
    details = [
        "PeMS7_228 Stage 11 10-split is primary core evidence per D-05.",
        "Held-out method == gls_map rows are used for final performance evidence per D-01.",
        split_count_detail(gls),
        stage12_detail,
    ]
    if missing_final:
        return CheckResult("EXP-01", "FAIL", relative(P228_DIR), "; ".join(details + [f"missing final layout rows: {', '.join(missing_final)}"]))
    if missing_portfolio:
        return CheckResult(
            "EXP-01",
            "WARN",
            relative(P228_DIR),
            "; ".join(details + [f"Phase 3 portfolio rows absent from Stage 11 and Stage 12 regeneration required: {', '.join(missing_portfolio)}"]),
        )
    return CheckResult("EXP-01", stage12_status, relative(P228_DIR), "; ".join(details + ["final and Phase 3 portfolio rows present."]))


def dataset_split_status(root, requirement, label, expected_splits):
    path = root / "combined_metrics.csv"
    if not path.exists():
        return CheckResult(requirement, "FAIL", relative(root), f"{label} combined_metrics.csv missing")
    errors = []
    metrics = read_csv(path, errors)
    if metrics is None:
        return CheckResult(requirement, "FAIL", relative(path), "; ".join(errors))
    gls = metrics[metrics["method"] == "gls_map"].copy()
    split_counts = gls.groupby(["budget", "layout_type"])["split_seed"].nunique()
    min_count = int(split_counts.min()) if not split_counts.empty else 0
    max_count = int(split_counts.max()) if not split_counts.empty else 0
    status = "PASS" if min_count >= expected_splits else "WARN"
    detail = f"{label} held-out GLS/MAP artifact has split_count_range={min_count}..{max_count}; "
    if min_count >= expected_splits:
        detail += f"meets {expected_splits}-split target."
    else:
        detail += f"lower-power evidence; later plan must extend or caveat per D-06."
    return CheckResult(requirement, status, relative(root), detail)


def check_exp02():
    return dataset_split_status(P1026_DIR, "EXP-02", "PeMS7_1026 external evidence", 10)


def check_exp03():
    if not SEATTLE_DIR.exists():
        return CheckResult("EXP-03", "WARN", relative(SEATTLE_DIR), "Seattle evidence directory absent; remove Seattle from core claim set per D-07.")
    required = ["SUMMARY.md", "combined_metrics.csv", "gls_map_layout_summary.csv", "gls_map_paired_delta_tests.csv", "certificate_correlation_summary.csv"]
    missing = require_files(SEATTLE_DIR, required)
    if missing:
        return CheckResult("EXP-03", "WARN", relative(SEATTLE_DIR), f"Seattle curation incomplete; missing {', '.join(missing)}; keep supporting/conditional per D-07.")
    return CheckResult("EXP-03", "WARN", relative(SEATTLE_DIR), "Seattle artifacts exist, but README synchronization/core-claim status still requires Phase 4 curation per D-07.")


def check_exp04(errors):
    path = P228_DIR / "gls_map_paired_delta_tests.csv"
    if not path.exists():
        return CheckResult("EXP-04", "FAIL", relative(path), "paired delta test table missing")
    paired = read_csv(path, errors)
    if paired is None:
        return CheckResult("EXP-04", "FAIL", relative(path), "paired delta test table unreadable")
    missing_cols = sorted(REQUIRED_PAIRED_COLUMNS - set(paired.columns))
    if missing_cols:
        return CheckResult("EXP-04", "FAIL", relative(path), f"paired table missing columns: {', '.join(missing_cols)}")
    interval_cols = [col for col in paired.columns if "ci" in col.lower() or "interval" in col.lower() or "effect" in col.lower()]
    status = "PASS" if interval_cols else "WARN"
    detail = "paired deltas/tests present for held-out GLS/MAP comparisons"
    if interval_cols:
        detail += f" with interval/effect columns: {', '.join(interval_cols)}"
    else:
        detail += "; confidence intervals/effect sizes not yet present and must be added by Plan 04-02."
    return CheckResult("EXP-04", status, relative(path), detail)


def check_exp05(errors):
    required = [P228_DIR / "certificate_correlation_summary.csv", P228_DIR / "combined_certificate_correlations.csv"]
    missing = [relative(path) for path in required if not path.exists()]
    if missing:
        return CheckResult("EXP-05", "FAIL", relative(P228_DIR), f"missing certificate correlation artifacts: {', '.join(missing)}")
    corr = read_csv(P228_DIR / "combined_certificate_correlations.csv", errors)
    if corr is None:
        return CheckResult("EXP-05", "FAIL", relative(P228_DIR / "combined_certificate_correlations.csv"), "correlation table unreadable")
    needed = {"method", "certificate", "pearson_mae", "spearman_mae"}
    missing_cols = sorted(needed - set(corr.columns))
    if missing_cols:
        return CheckResult("EXP-05", "FAIL", relative(P228_DIR / "combined_certificate_correlations.csv"), f"missing correlation columns: {', '.join(missing_cols)}")
    return CheckResult("EXP-05", "PASS", relative(P228_DIR), "Pearson/Spearman certificate-error correlations are present; interpret as empirical support per D-11.")


def check_exp06(errors):
    candidates = P228_DIR / "combined_rcss_candidates.csv"
    if not candidates.exists():
        return CheckResult("EXP-06", "FAIL", relative(candidates), "candidate diagnostics missing")
    frame = read_csv(candidates, errors)
    if frame is None:
        return CheckResult("EXP-06", "FAIL", relative(candidates), "candidate diagnostics unreadable")
    source_count = int(frame["source"].nunique()) if "source" in frame.columns else 0
    budget_count = int(frame["budget"].nunique()) if "budget" in frame.columns else 0
    runtime_markers = []
    for path in sorted(RESULTS_ROOT.glob("*runtime*")) + sorted(RESULTS_ROOT.glob("*sensitivity*")):
        runtime_markers.append(relative(path))
    status = "PASS" if runtime_markers else "WARN"
    detail = f"candidate diagnostics present across {source_count} sources and {budget_count} budgets"
    if runtime_markers:
        detail += f"; runtime/candidate sensitivity artifacts found: {', '.join(runtime_markers)}"
    else:
        detail += "; runtime/candidate-count sensitivity artifact not yet present and must be closed by Plan 04-05."
    return CheckResult("EXP-06", status, relative(candidates), detail)


def run_checks():
    errors = []
    results = [
        check_exp01(errors),
        check_exp02(),
        check_exp03(),
        check_exp04(errors),
        check_exp05(errors),
        check_exp06(errors),
    ]
    for raw in errors:
        parts = raw.split("|", 3)
        if len(parts) == 4:
            results.append(CheckResult(parts[1], parts[0], parts[2], parts[3]))
    return results


def print_table(results):
    rows = [(r.requirement, r.status, r.evidence, r.detail) for r in results]
    widths = [
        max(len("Requirement"), *(len(row[0]) for row in rows)),
        max(len("Status"), *(len(row[1]) for row in rows)),
        max(len("Evidence"), *(len(row[2]) for row in rows)),
    ]
    print(f"{'Requirement':<{widths[0]}}  {'Status':<{widths[1]}}  {'Evidence':<{widths[2]}}  Detail")
    print(f"{'-' * widths[0]}  {'-' * widths[1]}  {'-' * widths[2]}  {'-' * 6}")
    for requirement in REQUIREMENTS:
        for row in [r for r in results if r.requirement == requirement]:
            print(f"{row.requirement:<{widths[0]}}  {row.status:<{widths[1]}}  {row.evidence:<{widths[2]}}  {row.detail}")


def main():
    parser = argparse.ArgumentParser(description="Audit Phase 4 TRACE-SL evidence coverage without raw dataset reads")
    parser.add_argument("--fail-on-warn", action="store_true", help="Treat WARN rows as nonzero for strict CI use")
    args = parser.parse_args()
    results = run_checks()
    print_table(results)
    if any(result.status == "FAIL" for result in results):
        raise SystemExit(1)
    if args.fail_on_warn and any(result.status == "WARN" for result in results):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
