---
phase: 04-core-experiment-evidence
plan: 04
subsystem: research-evidence-curation
tags: [trace-sl, external-validation, pems7-1026, seattle, claim-status]

requires:
  - phase: 04-core-experiment-evidence
    provides: Phase 04 Plan 01 evidence audit identifying PeMS7_1026 lower-power status and Seattle curation requirement.
  - phase: 04-core-experiment-evidence
    provides: Phase 04 Plan 03 Stage 12 PeMS7_228 launcher pattern and baseline-portfolio flag contract.
provides:
  - Optional Stage 12 launchers for PeMS7_1026 and Seattle evidence extension.
  - Dataset claim-status decision record for PeMS7_1026 lower-power external evidence and Seattle supporting/conditional evidence.
  - Curated result README guidance synchronized with external/supporting evidence status.
affects: [phase-4-external-evidence, phase-4-manuscript-claims, phase-6-reproducibility]

tech-stack:
  added: []
  patterns: [dry-run-capable shell launchers, no-raw-data claim-status documentation, synchronized result inventory]

key-files:
  created:
    - scripts/run_stage12_pems7_1026.sh
    - scripts/run_stage12_seattle.sh
    - .planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md
  modified:
    - TRC-23-02333/trace_sl_results/README.md

key-decisions:
  - "PeMS7_1026 remains lower-power external evidence because current curated artifacts have five held-out GLS/MAP splits, not a synchronized ten-split extension."
  - "Seattle is synchronized as supporting/conditional evidence, not core evidence, because it has scripts/results/summaries/README guidance but only a light five-split bundle."
  - "Stage 12 external launchers include dry-run mode and baseline-portfolio flags while preserving existing layout labels."

patterns-established:
  - "External dataset status docs cite curated trace_sl_results artifacts and launcher scripts only, not raw dataset contents."
  - "Optional expensive evidence regeneration scripts should expose DRY_RUN, PYTHON_BIN, seed, budget, candidate-count, and threading overrides."

requirements-completed: [EXP-02, EXP-03]

duration: 3min
completed: 2026-05-22
---

# Phase 04 Plan 04: External Dataset Claim Status Summary

**PeMS7_1026 lower-power external framing and Seattle supporting/conditional evidence synchronized with reproducible Stage 12 launchers**

## Performance

- **Duration:** 3 min
- **Started:** 2026-05-22T17:00:16Z
- **Completed:** 2026-05-22T17:03:13Z
- **Tasks:** 2
- **Files modified:** 4

## Accomplishments

- Added optional Stage 12 launchers for PeMS7_1026 and Seattle with safe `DRY_RUN` support, override-friendly run parameters, BLAS thread caps, evaluator invocation, summarizer invocation, and compatible Phase 3 baseline-portfolio flags.
- Created `04-DATASET-CLAIM-STATUS.md`, explicitly recording PeMS7_1026 as lower-power external evidence and Seattle as supporting/conditional evidence without citing raw dataset contents.
- Updated `TRC-23-02333/trace_sl_results/README.md` so result inventory and reading guidance no longer overclaim PeMS7_1026 or Seattle as core evidence.

## Task Commits

Each task was committed atomically:

1. **Task 1: Add optional Stage 12 external/Seattle launchers** - `24aa066` (feat)
2. **Task 2: Document dataset claim status and synchronize result README** - `d7555dd` (docs)

**Plan metadata:** pending final metadata commit

## Files Created/Modified

- `scripts/run_stage12_pems7_1026.sh` - Optional PeMS7_1026 Stage 12 extension launcher defaulting to a five-seed lower-power external output and supporting ten-split override.
- `scripts/run_stage12_seattle.sh` - Optional Seattle Stage 12 supporting-light launcher with dry-run verification and synchronized evaluator/summarizer flow.
- `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md` - D-06/D-07 decision record for split counts, available artifacts, claim status, and extension commands.
- `TRC-23-02333/trace_sl_results/README.md` - Curated result inventory updated with core, lower-power external, and supporting/conditional claim-status guidance.

## Decisions Made

- PeMS7_1026 remains lower-power external evidence until a ten-split extension is generated, aggregated, reviewed, and committed.
- Seattle is synchronized as supporting/conditional evidence rather than core evidence because its current committed bundle is light and five-split.
- Both new launchers include Phase 3 baseline-portfolio flags because the evaluator exposes compatible CLI flags and stable labels are preserved.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Known Stubs

None detected in files created or modified by this plan. The documented lower-power/supporting statuses are intentional evidence caveats, not placeholders.

## Threat Flags

None. The new shell launchers are local batch scripts and the status artifacts cite curated result paths/scripts only; no new network endpoint, authentication path, file-upload path, or schema trust boundary was introduced beyond the plan's threat model.

## Verification

- `bash -n scripts/run_stage12_pems7_1026.sh && bash -n scripts/run_stage12_seattle.sh`
- Launcher token assertion confirmed `summarize_trace_sl_rcss.py`, `DATA_ROOT`, `OUTPUT_DIR`, and `SEEDS` in both new launchers.
- Dataset claim-status assertion confirmed `PeMS7_1026`, `Seattle`, `lower-power`, `core`, and `supporting` in the status artifact; confirmed README references to `seattle_stage11_auto_weight_light` and `pems7_1026_stage11_auto_weight`; confirmed status artifact does not contain the raw dataset path string.

## Next Phase Readiness

- Plan 04-05 can proceed with runtime/candidate-count sensitivity knowing external dataset claims are caveated.
- Manuscript-facing evidence can cite PeMS7_1026 as lower-power external and Seattle as supporting/conditional unless later ten-split/stronger bundles are generated.

## Self-Check: PASSED

- Found created/modified files: `scripts/run_stage12_pems7_1026.sh`, `scripts/run_stage12_seattle.sh`, `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md`, `TRC-23-02333/trace_sl_results/README.md`, and `.planning/phases/04-core-experiment-evidence/04-04-SUMMARY.md`.
- Found task commits: `24aa066` and `d7555dd`.
- Verification passed: launcher shell syntax, required launcher-token assertion, and dataset claim-status/README consistency assertion.

---
*Phase: 04-core-experiment-evidence*
*Completed: 2026-05-22*
