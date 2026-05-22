---
phase: 03-baseline-portfolio
reviewed: 2026-05-22T00:00:00Z
depth: standard
files_reviewed: 3
files_reviewed_list:
  - TRC-23-02333/summarize_trace_sl_rcss.py
  - TRC-23-02333/transparent_estimator_eval.py
  - scripts/run_stage12_pems7_228.sh
findings:
  critical: 2
  warning: 3
  info: 0
  total: 5
status: issues_found
---

# Phase 03: Code Review Report

## Summary

Reviewed the Phase 3 baseline portfolio evaluator, multi-split summarizer, and Stage 12 launcher. The submitted implementation has correctness and reproducibility defects around Stage 12 defaults, baseline-portfolio flag semantics, ignored output locations, and numerical edge cases in layout helpers.

## Critical Issues

### CR-01: Stage 12 launcher defaults to a single seed, disabling multi-split evidence and paired tests

**File:** `scripts/run_stage12_pems7_228.sh:5`

**Issue:** `SEEDS` defaults to only `25`. The summarizer is multi-split oriented and only emits paired statistical tests when at least two valid deltas exist. With this default, Stage 12 produces no meaningful paired p-values and does not satisfy the project evidence standard for paired comparisons / robustness across splits.

**Fix:** Use the established multi-split default unless this launcher is explicitly documented as a smoke run: `SEEDS="${SEEDS:-25 26 27 28 29}"`.

### CR-02: Stage 12 default output path is ignored by `.gitignore`, so curated evidence will not be committed

**File:** `scripts/run_stage12_pems7_228.sh:4`

**Issue:** The launcher writes to `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio`, but `.gitignore` currently ignores `TRC-23-02333/trace_sl_results/*` and only unignores earlier Stage 6–11 result directories. This makes Phase 3/Stage 12 outputs invisible to Git by default, breaking reproducibility artifact capture.

**Fix:** Add unignore rules for the Stage 12 result directory and logs.

## Warnings

### WR-01: `--include-baseline-portfolio` does not actually enable the full baseline portfolio

**File:** `TRC-23-02333/transparent_estimator_eval.py:801-807`

**Issue:** The flag enables greedy/swap/observability/graph/QR rows, but not `include_simple_baselines`, `include_scenario_greedy`, or `include_rcss`. A user invoking the advertised portfolio flag directly will miss `top_variance`, `scenario_cvar_a_trace`, and `robust_coverage_cvar` rows that the summarizer and Phase 3 comparison framing expect.

**Fix:** Bundle the full intended portfolio under this flag.

### WR-02: `make_similarity` can emit NaNs for empty/non-finite positive distances

**File:** `TRC-23-02333/transparent_estimator_eval.py:109-115`

**Issue:** `sigma = np.median(positive)` is unchecked. If the distance matrix has no positive finite entries, or contains only non-finite positives, `sigma` becomes `NaN`/`inf`, contaminating observability, Laplacian, and graph-sampling layouts.

**Fix:** Filter finite positives and fall back safely.

### WR-03: `quality_coverage_sample` can divide by zero if requested sensor count exceeds node count

**File:** `TRC-23-02333/transparent_estimator_eval.py:383-389`

**Issue:** The loop assumes at least one remaining node. If called with `sensor_count > n_nodes`, `remaining` becomes all false, fallback weights also sum to zero, and `probs = weights / weights.sum()` produces invalid probabilities.

**Fix:** Validate `sensor_count` upfront.
