---
phase: 05-robustness-and-generality
plan: 03
subsystem: research-evidence
tags: [trace-sl, pems7-228, robustness, candidate-sensitivity, bash, csv]

requires:
  - phase: 05-robustness-and-generality
    provides: robustness CLI flags and condition-aware summarization
provides:
  - Stage 14 PeMS7_228 robustness launcher and artifact-backed reduced evidence
  - Stage 14 PeMS7_228 candidate-count launcher with 50/100/200/500 runtime evidence
  - Curated Stage 14 result inventory wording
affects: [phase-05-validation, phase-06-artifact-curation, paper-robustness-claims]

tech-stack:
  added: []
  patterns:
    - repo-relative Bash experiment launchers with DRY_RUN, thread caps, and environment overrides
    - condition-aware CSV/Markdown evidence under trace_sl_results

key-files:
  created:
    - scripts/run_stage14_pems7_228_robustness.sh
    - scripts/run_stage14_candidate_sensitivity_pems7_228.sh
    - TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/combined_metrics.csv
    - TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/stage14_timing.csv
  modified:
    - TRC-23-02333/transparent_estimator_eval.py
    - TRC-23-02333/summarize_trace_sl_rcss.py
    - TRC-23-02333/trace_sl_results/README.md

key-decisions:
  - "Stage 14 robustness uses a reduced PeMS7_228 bundle with nine stress-test conditions as artifact-backed evidence, not as a universal robustness proof."
  - "Stage 14 candidate sensitivity completed all 50/100/200/500 reduced runs locally, so no ROBUST-06 caveat artifact was needed."

patterns-established:
  - "Stage 14 launchers mirror Stage 12/13 DRY_RUN and thread-control patterns while exposing reduced-run scale knobs."
  - "Summarizer now tolerates empty optional certificate correlation CSVs and Stage 14 timing files."

requirements-completed: [ROBUST-01, ROBUST-02, ROBUST-03, ROBUST-04, ROBUST-05, ROBUST-06]

duration: 22min
completed: 2026-05-23
---

# Phase 05 Plan 03: Stage 14 Robustness and Candidate Sensitivity Summary

**PeMS7_228 Stage 14 stress-test robustness and 50/100/200/500 candidate-count evidence generated as reproducible shell launchers plus CSV/Markdown artifacts.**

## Performance

- **Duration:** 22min
- **Started:** 2026-05-23T02:44:27Z
- **Completed:** 2026-05-23T03:06:40Z
- **Tasks:** 3
- **Files modified:** 303 committed files/artifacts across launchers, evaluator/summarizer support, result bundles, and inventory docs

## Accomplishments

- Added `run_stage14_pems7_228_robustness.sh` covering baseline, sensor failure 5/10/20%, observation noise, random missingness, block missingness, cost proxy, and chronological split conditions.
- Generated reduced PeMS7_228 Stage 14 robustness evidence with real `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_paired_delta_tests.csv`, and `SUMMARY.md` artifacts.
- Added `run_stage14_candidate_sensitivity_pems7_228.sh` and generated 50/100/200/500 candidate-count performance plus runtime evidence with `stage14_timing.csv`, `candidate_sensitivity_summary.csv`, and `runtime_candidate_sensitivity.csv`.
- Updated the curated result inventory to frame Stage 14 as stress-test evidence and external robustness as supporting/optional.

## Task Commits

1. **Task 1: Add launcher and generate Stage 14 PeMS7_228 robustness evidence** - `d133d1b` (feat)
2. **Task 2: Add launcher and generate Stage 14 candidate-count/runtime evidence** - `a0f9af4` (feat)
3. **Task 3: Register generated Stage 14 evidence in the result inventory** - `d406b87` (docs)

## Files Created/Modified

- `scripts/run_stage14_pems7_228_robustness.sh` - Stage 14 robustness launcher with DRY_RUN, BLAS caps, repo-relative defaults, condition iteration, and final aggregation.
- `scripts/run_stage14_candidate_sensitivity_pems7_228.sh` - Stage 14 candidate-count launcher with timing rows and optional caveat support.
- `TRC-23-02333/transparent_estimator_eval.py` - Handles one-row reduced validation tuning without an empty tuner split.
- `TRC-23-02333/summarize_trace_sl_rcss.py` - Skips empty optional CSVs and reads `stage14_timing.csv` for runtime aggregation.
- `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/` - Generated reduced robustness evidence bundle.
- `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/` - Generated reduced candidate-count/runtime evidence bundle.
- `TRC-23-02333/trace_sl_results/README.md` - Curated inventory now includes Stage 14 robustness and candidate sensitivity.

## Verification

- `bash -n scripts/run_stage14_pems7_228_robustness.sh` — passed.
- `DRY_RUN=1 SEEDS="25" BUDGETS="0.10" NUM_LAYOUTS=1 RCSS_RANDOM_CANDIDATES=1 RCSS_QUALITY_CANDIDATES=1 scripts/run_stage14_pems7_228_robustness.sh` — passed.
- `SEEDS="25 26" BUDGETS="0.10" NUM_LAYOUTS=1 RCSS_RANDOM_CANDIDATES=2 RCSS_QUALITY_CANDIDATES=2 SCENARIO_COUNT=2 VALIDATION_SWAP_STARTS=1 VALIDATION_SWAP_ITER=1 VALIDATION_SWAP_ADD_POOL=5 VALIDATION_SWAP_REMOVE_POOL=5 MAX_TEST_STEPS=1 THREADS_PER_JOB=1 scripts/run_stage14_pems7_228_robustness.sh` — passed after auto-fixes and generated artifacts.
- Plan Task 1 Python artifact assertion — passed with `stage14-robustness-evidence-ok`.
- `bash -n scripts/run_stage14_candidate_sensitivity_pems7_228.sh` — passed.
- `DRY_RUN=1 CANDIDATE_COUNTS="50 100 200 500" SEEDS="25" BUDGETS="0.20" NUM_LAYOUTS=1 scripts/run_stage14_candidate_sensitivity_pems7_228.sh` — passed.
- `CANDIDATE_COUNTS="50 100 200 500" SEEDS="25" BUDGETS="0.20" NUM_LAYOUTS=1 SCENARIO_COUNT=1 VALIDATION_SWAP_STARTS=1 VALIDATION_SWAP_ITER=1 VALIDATION_SWAP_ADD_POOL=5 VALIDATION_SWAP_REMOVE_POOL=5 MAX_TEST_STEPS=1 THREADS_PER_JOB=1 scripts/run_stage14_candidate_sensitivity_pems7_228.sh` — passed and completed all candidate counts, including 500.
- Plan Task 2 Python artifact assertion — passed with `stage14-candidate-evidence-ok`.
- README token assertion — passed with `stage14-readme-ok`.

## Decisions Made

- No `candidate_sensitivity_caveat.json` was generated because the reduced 50/100/200/500 candidate-count run completed locally.
- Stage 14 README language explicitly avoids universal deployment claims and treats external robustness as supporting/optional.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Fixed empty validation tuner split for one-step reduced runs**
- **Found during:** Task 1 actual reduced robustness run
- **Issue:** `MAX_TEST_STEPS=1` also reduced validation to one row; `split_validation_for_tuning` returned an empty tuner split, causing `np.vstack` to fail.
- **Fix:** Reused the single validation row for both selector and tuner when validation has fewer than two rows.
- **Files modified:** `TRC-23-02333/transparent_estimator_eval.py`
- **Verification:** Robustness actual reduced run completed after the fix.
- **Committed in:** `d133d1b`

**2. [Rule 1 - Bug] Ignored empty optional certificate correlation CSVs during aggregation**
- **Found during:** Task 1 aggregation
- **Issue:** Some reduced one-row seed runs emitted empty optional `certificate_correlations.csv` files, and `pd.read_csv` raised `EmptyDataError`.
- **Fix:** Added a safe CSV reader that skips missing or empty optional CSV artifacts.
- **Files modified:** `TRC-23-02333/summarize_trace_sl_rcss.py`
- **Verification:** Robustness aggregation and artifact assertion passed.
- **Committed in:** `d133d1b`

**3. [Rule 2 - Missing Critical] Added Stage 14 timing ingestion to runtime summarization**
- **Found during:** Task 2 artifact assertion
- **Issue:** The summarizer only recognized `stage13_timing.csv`, so Stage 14 candidate runs did not produce `runtime_candidate_sensitivity.csv` from `stage14_timing.csv`.
- **Fix:** Extended runtime collection to read `stage14_timing.csv` before falling back to Stage 13 timing or existing runtime summaries.
- **Files modified:** `TRC-23-02333/summarize_trace_sl_rcss.py`
- **Verification:** Candidate summary regeneration and artifact assertion passed.
- **Committed in:** `a0f9af4`

---

**Total deviations:** 3 auto-fixed (2 bugs, 1 missing critical aggregation support)
**Impact on plan:** All fixes were necessary for reduced artifact generation and validation; no scope expansion beyond Stage 14 evidence support.

## Known Stubs

None detected in created/modified Stage 14 launchers, summaries, or inventory wording. `candidate_sensitivity_caveat.json` is intentionally absent because no candidate count failed.

## Threat Flags

None. New files are local batch launchers and generated result artifacts under `trace_sl_results`; no new service endpoints, auth paths, raw-data publication, or external network surfaces were introduced.

## Issues Encountered

- The initial artifact directory is ignored by `.gitignore`, so generated Stage 14 evidence was intentionally force-added with explicit pathspecs. No raw datasets were staged or committed.
- Pre-existing unrelated working-tree changes remained untouched: `.planning/quick` deletions, `idea-stage` changes, `.claude/`, and Phase 01 verification/UAT files.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 05 Plan 04 can validate ROBUST-01..06 against committed Stage 14 artifacts. Candidate-count evidence has complete 50/100/200/500 coverage, so the validator should not require a caveat branch for this run.

## Self-Check: PASSED

- Created/modified key files exist.
- Task commits found: `d133d1b`, `a0f9af4`, `d406b87`.
- Required artifact assertions passed for robustness, candidate sensitivity, and README inventory.

---
*Phase: 05-robustness-and-generality*
*Completed: 2026-05-23*
