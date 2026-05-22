---
phase: 04-core-experiment-evidence
plan: 06
subsystem: evidence-validation-and-claim-sync
tags: [trace-sl, phase-4, evidence-validator, claim-contract, exp-01, exp-06]

requires:
  - phase: 04-core-experiment-evidence
    provides: Plans 04-02 through 04-05 statistical, Stage 12, external-status, and Stage 13 evidence artifacts.
provides:
  - Final Phase 4 validator covering EXP-01 through EXP-06.
  - Final Phase 4 evidence audit synchronized with accepted caveats.
  - Claim-evidence contract rows C-01 through C-05 updated with Phase 4 evidence status.
affects: [phase-5-robustness, phase-6-reproducibility, manuscript-results]

tech-stack:
  added: []
  patterns: [curated-artifact validation, no-raw-data evidence guard, claim-contract synchronization]

key-files:
  created:
    - .planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py
    - .planning/phases/04-core-experiment-evidence/test_validate_phase4_evidence.py
  modified:
    - .planning/phases/04-core-experiment-evidence/04-EVIDENCE-AUDIT.md
    - .planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md

key-decisions:
  - "Final Phase 4 validation fails missing primary PeMS7_228 Stage 12, statistical, certificate, EXP-06 runtime/candidate, or raw-dataset citation evidence."
  - "Only PeMS7_1026 lower-power external status and Seattle supporting/conditional status are allowed WARN outcomes."
  - "The claim contract now routes Phase 4 claims through Stage 12, Stage 13, audit/status docs, and curated result README artifacts."

patterns-established:
  - "End-of-phase evidence validators should read curated trace_sl_results artifacts and planning docs, not raw datasets."
  - "Claim synchronization should update evidence status/source/caveat fields without drafting final manuscript prose."

requirements-completed: [EXP-01, EXP-02, EXP-03, EXP-04, EXP-05, EXP-06]

duration: 6min
completed: 2026-05-22
---

# Phase 04 Plan 06: Final Evidence Validation and Claim Sync Summary

**Phase 4 now has a validator-enforced evidence gate plus synchronized audit and claim-contract status for EXP-01 through EXP-06.**

## Performance

- **Duration:** 6 min
- **Started:** 2026-05-22T17:27:12Z
- **Completed:** 2026-05-22T17:33:18Z
- **Tasks:** 2
- **Files modified:** 4

## Accomplishments

- Added `validate_phase4_evidence.py`, a pandas/pathlib CLI validator that checks EXP-01 through EXP-06 and exits nonzero on missing required primary evidence.
- Added source-contract tests for the final validator, including required PeMS7_228 Stage 12 labels and the raw-dataset evidence guard.
- Updated `04-EVIDENCE-AUDIT.md` to mark EXP-01, EXP-04, EXP-05, and EXP-06 supported, while preserving only the allowed PeMS7_1026 lower-power and Seattle supporting/conditional WARN caveats.
- Updated Phase 4-relevant claim rows C-01 through C-05 in `01-CLAIM-EVIDENCE-CONTRACT.md` to point at curated Stage 12/Stage 13 outputs, phase audit/status docs, and explicit caveats.

## Task Commits

Each task was committed atomically:

1. **Task 1 RED: Add failing validator contract tests** - `19373ce` (test)
2. **Task 1 GREEN: Add final Phase 4 evidence validator** - `44d3c04` (feat)
3. **Task 2: Synchronize evidence audit and claim-evidence contract** - `4ecd44f` (docs)

**Plan metadata:** pending final metadata commit.

## Files Created/Modified

- `.planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py` - Final Phase 4 smoke/schema/status validator for EXP-01 through EXP-06 and raw-dataset evidence citations.
- `.planning/phases/04-core-experiment-evidence/test_validate_phase4_evidence.py` - Lightweight unittest coverage for current validator outcomes, required Stage 12 labels, and raw-dataset guard.
- `.planning/phases/04-core-experiment-evidence/04-EVIDENCE-AUDIT.md` - Final audit status table synchronized to Stage 12, Stage 13, PeMS7_1026, and Seattle evidence status.
- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` - Phase 4 claim rows C-01 through C-05 updated with evidence sources, statuses, and caveats.

## Decisions Made

- Treat PeMS7_228 Stage 12 as the primary core ten-split evidence bundle for final/Phase 3 baseline labels, including `validation_swap_selected`, `rcss_selected`, `multistart_swap_by_validation`, `greedy_a_trace`, `greedy_d_logdet`, `observability_proxy`, `graph_sampling_laplacian`, and `qr_pod_modes`.
- Fail validation if EXP-04 completed evidence lacks `ci95_low`, `ci95_high`, `cohens_dz`, `paired_t_p`, `wilcoxon_p`, or `count`.
- Fail validation if EXP-06 Stage 13 evidence is missing measured runtime/candidate-count outputs or uses pending/runtime-unavailable wording.
- Preserve WARN, not FAIL, only for PeMS7_1026 lower-power external evidence and Seattle supporting/conditional evidence.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- GSD SDK state helper commands reported legacy-format parse errors for `STATE.md`; manual state/roadmap updates are captured in the final metadata commit.
- Pre-existing unrelated working-tree changes remained untouched, including deleted quick-planning files and idea-stage edits.

## User Setup Required

None - no external service configuration required.

## Known Stubs

None. The validator checks committed curated artifacts and the audit/contract updates cite present evidence bundles or explicit D-06/D-07 caveats.

## Threat Flags

None. The plan’s trust-boundary mitigations were implemented: curated evidence validation, claim-contract synchronization, and raw-dataset evidence citation checks.

## Verification

- `python -m py_compile /home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py`
- `python /home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/test_validate_phase4_evidence.py`
- `python /home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py`
- Phase 4 doc-sync assertion confirmed audit tokens `EXP-01` through `EXP-06`, `greedy_a_trace`, `greedy_d_logdet`; contract tokens `held-out`, `validation MAE`, `certificate`, `Seattle`, `PeMS7_1026`; and no raw dataset evidence citation in the audit.

## TDD Gate Compliance

- RED commit present: `19373ce`
- GREEN commit present after RED: `44d3c04`
- Refactor commits: none needed

## Next Phase Readiness

Phase 5 can proceed using Phase 4’s finalized evidence gate and synchronized claim caveats. Phase 6/manuscript work can cite curated Stage 12 and Stage 13 artifacts without re-auditing Phase 4 primary evidence status.

## Self-Check: PASSED

- Found summary file: `/home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/04-06-SUMMARY.md`
- Found validator: `/home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py`
- Found validator test: `/home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/test_validate_phase4_evidence.py`
- Found updated audit: `/home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/04-EVIDENCE-AUDIT.md`
- Found updated claim contract: `/home/samuel/projects/sensor_opt/.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md`
- Found task commits: `19373ce`, `44d3c04`, and `4ecd44f`
- Automated validator, unit test, and doc-sync verification passed.

---
*Phase: 04-core-experiment-evidence*
*Completed: 2026-05-22*
