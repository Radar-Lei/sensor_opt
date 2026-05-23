---
phase: 08-external-stage12-evidence
plan: 01
subsystem: research-artifacts
tags: [trace-sl, stage12, external-evidence, provenance, gate, tdd]

requires:
  - phase: 07-claim-and-main-table-contract
    provides: Phase 7 generator style, claim/table contract schemas, and paired-stat honesty rules
provides:
  - PeMS7_1026 and Seattle Stage12 ten-split launcher defaults
  - Tested external Stage12 evidence contract generator
  - Machine-checkable Seattle and v1.1 fail-closed evidence gate logic
affects: [phase-08, phase-09, phase-10, paper-sources, external-evidence]

tech-stack:
  added: []
  patterns: [CSV/JSON-first generated paper-source contracts, fail-closed evidence gates, git-tracked aggregate provenance checks]

key-files:
  created:
    - scripts/generate_trace_sl_external_evidence_contracts.py
    - scripts/test_generate_trace_sl_external_evidence_contracts.py
    - .planning/phases/08-external-stage12-evidence/08-01-SUMMARY.md
  modified:
    - scripts/run_stage12_pems7_1026.sh
    - scripts/run_stage12_seattle.sh

key-decisions:
  - "External Stage12 completion requires existing, git-tracked aggregate artifacts and exactly ten split seeds; untracked aggregates remain pending_tracking rather than complete."
  - "Seattle remains blocked from core claims unless tracked ten-split Stage12 evidence is complete and any stage12_status.json reports completion."
  - "Rows without paired-stat provenance are descriptive_only; paired_stats_available rows must carry paired values and gls_map_paired_delta_tests.csv provenance."

patterns-established:
  - "External evidence contracts mirror Phase 7 CSV/JSON-first generator interfaces and deterministic metadata."
  - "Gate summaries carry dataset-level blocker reasons for missing, Stage11, lower-split, untracked, or Seattle-status-blocked evidence."

requirements-completed: []
duration: 5min
completed: 2026-05-23
---

# Phase 08 Plan 01: External Stage12 Evidence Contract Summary

**Fail-closed Stage12 external-evidence launchers and contract gates for PeMS7_1026 and Seattle**

## Performance

- **Duration:** 5 min
- **Started:** 2026-05-23T13:24:41Z
- **Completed:** 2026-05-23T13:29:45Z
- **Tasks:** 2
- **Files modified:** 5

## Accomplishments

- Confirmed prior launcher commit `52a7e1e` satisfies Task 1: both external launchers default to Stage12 baseline-portfolio output directories, ten split seeds, and reviewer-facing baseline flags.
- Added TDD regression coverage for ten-split completion, pending tracking, Stage11 rejection, paired-stat honesty, raw-data rejection, Seattle status consumption, and Seattle fail-closed eligibility.
- Implemented `scripts/generate_trace_sl_external_evidence_contracts.py` with Phase 7-style `build_all_contracts`, table/JSON writers, README support, tracked-source checks, and machine-checkable external gate payloads.

## Task Commits

1. **Task 1: Correct PeMS7_1026 and Seattle Stage12 launchers** - `52a7e1e` (feat)
2. **Task 2 RED: Add failing external evidence contract tests** - `4f0fdee` (test)
3. **Task 2 GREEN: Implement external evidence contract gate** - `d1783d6` (feat)

**Plan metadata:** pending final docs commit

## Files Created/Modified

- `scripts/run_stage12_pems7_1026.sh` - Stage12 PeMS7_1026 launcher with ten default seeds and baseline-portfolio output.
- `scripts/run_stage12_seattle.sh` - Stage12 Seattle launcher with ten default seeds and baseline-portfolio output.
- `scripts/test_generate_trace_sl_external_evidence_contracts.py` - Regression tests for external evidence completion and fail-closed gate behavior.
- `scripts/generate_trace_sl_external_evidence_contracts.py` - Generator for external evidence contract rows and gate payloads.
- `.planning/phases/08-external-stage12-evidence/08-01-SUMMARY.md` - Plan execution summary.

## Decisions Made

- Treat untracked but otherwise present aggregate evidence as `pending_tracking`, keeping dataset completion false until `git ls-files --error-unmatch` succeeds.
- Keep Seattle blocked by default; complete tracked Stage12 evidence and a non-blocking/completed `stage12_status.json` are required before Seattle can become core-claim eligible.
- Preserve paired-stat honesty by marking rows without paired comparisons as `descriptive_only` and requiring paired-stat columns plus paired-test CSV provenance for `paired_stats_available` rows.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- Existing repository state included an uncommitted `.planning/STATE.md` modification and untracked `.claude/` directory from outside this plan. They were left untouched for raw hygiene and scope isolation.

## Verification

- `bash -n scripts/run_stage12_pems7_1026.sh`
- `bash -n scripts/run_stage12_seattle.sh`
- `DRY_RUN=1 PYTHON_BIN=python bash scripts/run_stage12_pems7_1026.sh` produced ten evaluator commands and one summarizer command with `--include-baseline-portfolio`.
- `DRY_RUN=1 PYTHON_BIN=python bash scripts/run_stage12_seattle.sh` produced ten evaluator commands and one summarizer command with `--include-baseline-portfolio`.
- `python scripts/test_generate_trace_sl_external_evidence_contracts.py` passed: 7 tests.

## Known Stubs

None found in files created or modified by this plan.

## Threat Flags

| Flag | File | Description |
|------|------|-------------|
| threat_flag: generated evidence gate | `scripts/generate_trace_sl_external_evidence_contracts.py` | Adds a new paper-source contract/gate trust boundary; mitigated with raw-dataset rejection, git tracking checks, split-count gates, and paired-stat provenance tests from the plan threat model. |

## Self-Check: PASSED

- Found `scripts/run_stage12_pems7_1026.sh`
- Found `scripts/run_stage12_seattle.sh`
- Found `scripts/generate_trace_sl_external_evidence_contracts.py`
- Found `scripts/test_generate_trace_sl_external_evidence_contracts.py`
- Found `.planning/phases/08-external-stage12-evidence/08-01-SUMMARY.md`
- Found commits `52a7e1e`, `4f0fdee`, and `d1783d6`

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Plan 02 can use the Stage12 launchers to run or track real PeMS7_1026 and Seattle aggregate evidence.
- Plan 04 can generate external paper-source contracts once the required aggregate CSV/JSON/Markdown artifacts exist and are tracked.
- EVID-03 and EVID-04 are not marked complete by this plan because actual external ten-split aggregate evidence has not yet been produced and tracked.

---
*Phase: 08-external-stage12-evidence*
*Completed: 2026-05-23*
