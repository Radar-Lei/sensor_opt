---
phase: 04-core-experiment-evidence
plan: 05
subsystem: runtime-candidate-sensitivity
tags: [trace-sl, pems7-228, candidate-sensitivity, runtime, exp-06]

requires:
  - phase: 04-core-experiment-evidence
    provides: Phase 04 Plan 01 evidence audit and Phase 04 Plan 02 sensitivity aggregation support.
provides:
  - Candidate-count sensitivity aggregation from RCSS candidate artifacts.
  - Reproducible Stage 13 PeMS7_228 candidate-count sensitivity launcher.
  - Evidence-backed runtime/candidate tractability summary for EXP-06.
affects: [phase-4-core-evidence, phase-6-reproducibility, manuscript-results]

tech-stack:
  added: []
  patterns: [evidence-backed runtime summary, dry-run shell launcher, curated trace_sl_results stage]

key-files:
  created:
    - scripts/run_stage13_candidate_sensitivity_pems7_228.sh
    - TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/SUMMARY.md
    - TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/runtime_candidate_sensitivity.csv
  modified:
    - TRC-23-02333/summarize_trace_sl_rcss.py
    - .gitignore

key-decisions:
  - "EXP-06 is satisfied with evidence-backed candidate-count and runtime/tractability outputs, not pending commands or runtime-unavailable prose."
  - "Stage 13 is framed as practical tractability and selection-stability evidence, not as a broad scalability guarantee."
  - "The committed minimal Stage 13 sweep covers candidate counts 50 and 100 on PeMS7_228 budget 0.20 with measured runtime seconds."

patterns-established:
  - "Stage sensitivity launchers should provide DRY_RUN=1 command verification and preserve raw dataset files as ignored local inputs."
  - "Runtime summaries should be emitted as `runtime_candidate_sensitivity.csv` with candidate_count and runtime_seconds columns."

requirements-completed: [EXP-06]

duration: 28min
completed: 2026-05-23
---

# Phase 04 Plan 05: Runtime/Candidate Sensitivity Summary

**Stage 13 PeMS7_228 candidate-count and runtime sensitivity evidence is now generated and committed.**

## Performance

- **Tasks:** 2
- **Files modified/created:** summarizer, Stage 13 launcher, Stage 13 result bundle, `.gitignore`

## Accomplishments

- Added candidate sensitivity aggregation to `TRC-23-02333/summarize_trace_sl_rcss.py`, including `candidate_sensitivity_summary.csv` and measured runtime summary support.
- Added `scripts/run_stage13_candidate_sensitivity_pems7_228.sh` with `DRY_RUN=1`, BLAS thread caps, configurable seeds/budgets/candidate counts, per-candidate output directories, timing capture, and top-level aggregation.
- Ran a minimal evidence-backed Stage 13 sweep for candidate counts 50 and 100 using seed 25 and budget 0.20.
- Committed `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/`, including per-candidate summaries, combined metrics, candidate diagnostics, and `runtime_candidate_sensitivity.csv`.

## Task Commits

1. **Task 1: Add candidate/runtime sensitivity aggregation** — `b52bd38`, `673d8d1`
2. **Task 2: Execute/audit Stage 13 sensitivity evidence** — `11dd2fc`

## Files Created/Modified

- `TRC-23-02333/summarize_trace_sl_rcss.py`
- `scripts/run_stage13_candidate_sensitivity_pems7_228.sh`
- `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/SUMMARY.md`
- `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/runtime_candidate_sensitivity.csv`
- `.gitignore`

## Deviations from Plan

- The first interrupted execution produced `stage13_timing.csv` but not the required `runtime_candidate_sensitivity.csv`. I fixed the launcher to preserve timing under the required filename before final aggregation, then reran the minimal Stage 13 sweep.

## Issues Encountered

- Executor stream interrupted before SUMMARY creation. Recovery used committed task evidence, disk artifacts, and the plan acceptance command to safely complete the remaining summary/commit steps.

## User Setup Required

None.

## Known Stubs

None. The Stage 13 result bundle contains completed candidate-count directories and measured runtime values.

## Threat Flags

None. The launcher reads local ignored PeMS data only when executed normally; `DRY_RUN=1` verifies commands without reading raw datasets.

## Verification

- `python -m py_compile TRC-23-02333/summarize_trace_sl_rcss.py`
- `DRY_RUN=1 bash scripts/run_stage13_candidate_sensitivity_pems7_228.sh`
- Stage 13 acceptance check confirmed:
  - `SUMMARY.md` exists and contains candidate/runtime/tractability language.
  - No pending/runtime-unavailable wording is used as completion evidence.
  - At least two candidate-count directories exist.
  - `runtime_candidate_sensitivity.csv` exists with `candidate_count` and `runtime_seconds` columns.
  - Candidate counts have measured nonnegative runtime values.

## Next Phase Readiness

Plan 04-06 can now validate EXP-06 using committed Stage 13 artifacts.

## Self-Check: PASSED

- Required files exist on disk.
- Required commits exist.
- Plan acceptance command passed.
- EXP-06 has evidence-backed candidate-count and runtime/tractability sensitivity outputs.

---
*Phase: 04-core-experiment-evidence*
*Completed: 2026-05-23*
