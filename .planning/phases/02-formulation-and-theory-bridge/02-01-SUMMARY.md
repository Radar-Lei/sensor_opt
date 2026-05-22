---
phase: 02-formulation-and-theory-bridge
plan: 01
subsystem: research-methodology
tags: [trace-sl, sensor-placement, gls-map, rcss, posterior-trace, validation-swap]

requires:
  - phase: 01-claim-evidence-contract
    provides: Certificate terminology, validation/test evidence guardrails, and claim-evidence boundaries
provides:
  - Manuscript-ready budgeted reconstruction-aware sensor-set formulation
  - RCSS surrogate objective with validation loss, posterior trace, scenario CVaR trace, condition number, and coverage terms
  - Linear-Gaussian GLS/MAP posterior-error bridge scoped to expected hidden-state squared error
  - Validation-aware swap complexity and fixed-candidate local-optimality language
affects: [phase-03-baseline-portfolio, phase-04-core-experiment-evidence, phase-05-robustness-and-generality, phase-07-manuscript-package]

tech-stack:
  added: []
  patterns: [phase-local method artifact, claim-guardrailed theory bridge, validation/test separation]

key-files:
  created:
    - .planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md
    - .planning/phases/02-formulation-and-theory-bridge/02-01-SUMMARY.md
  modified: []

key-decisions:
  - "TRACE-SL is framed as offline budgeted sparse sensor-set design for hidden-node reconstruction, not candidate-pool tuning."
  - "RCSS is documented as a predeclared surrogate/portfolio with validation-only selection evidence and held-out test evidence kept separate."
  - "Posterior trace language is scoped to linear-Gaussian squared-error analysis and empirical MAE-oriented guidance, preserving certificate-guided terminology."
  - "Validation-aware swap is claimed only as fixed-candidate one-swap local optimality under the implemented validation-loss acceptance rule."

patterns-established:
  - "Phase-local theory artifacts should name implementation anchors while avoiding raw dataset paths."
  - "Certificate wording must distinguish empirical diagnostics from theorem-level guarantees."
  - "Validation selection and held-out test evaluation must remain separate in method text."

requirements-completed: [THEORY-01, THEORY-02, THEORY-03, THEORY-04, THEORY-05]

duration: 5min
completed: 2026-05-22
---

# Phase 2 Plan 1: Formulation and Theory Bridge Summary

**Budgeted TRACE-SL sensor-set formulation with RCSS surrogate, GLS/MAP posterior-error bridge, and validation-swap local analysis**

## Performance

- **Duration:** 5 min
- **Started:** 2026-05-22T02:01:34Z
- **Completed:** 2026-05-22T02:06:05Z
- **Tasks:** 3
- **Files modified:** 2

## Accomplishments

- Created the Phase 2 bridge artifact with Phase Boundary, Source Register, Notation, budgeted reconstruction-aware optimization, and protocol separation.
- Added the RCSS surrogate objective, auto-weight selector/tuner validation split explanation, and linear-Gaussian posterior covariance trace derivation.
- Added MAE caveats, certificate-guided terminology guardrails, validation-aware swap complexity, dense-solver scaling limitation, and fixed-candidate one-swap local optimality.

## Task Commits

Each task was committed atomically:

1. **Task 1: Draft the formal sensor-set formulation slice** - `fd67501` (docs)
2. **Task 2: Add RCSS surrogate and posterior-error derivation slice** - `2e4901d` (docs)
3. **Task 3: Add validation-swap analysis, guardrails, and source coverage audit** - `867fc5b` (docs)

**Plan metadata:** pending final metadata commit

## Files Created/Modified

- `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md` - Phase-local method/theory bridge artifact covering THEORY-01..THEORY-05 and D-01..D-12.
- `.planning/phases/02-formulation-and-theory-bridge/02-01-SUMMARY.md` - Execution summary and context handoff.

## Decisions Made

- TRACE-SL wording is anchored as offline sparse sensor-set design under `|S| <= k` for hidden complement reconstruction.
- Validation MAE is retained as selection/tuning/refinement evidence only; held-out test remains the final performance evidence channel.
- Posterior trace is presented as an A-optimal expected squared-error proxy under linear-Gaussian assumptions, not a broad MAE guarantee.
- Validation-aware swap is described with fixed-candidate local optimality and dense-solver scaling limitations.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] Removed raw dataset path citation from artifact**
- **Found during:** Task 1 verification
- **Issue:** The initial artifact contained the forbidden raw dataset path string while stating it was not used.
- **Fix:** Reworded the sentence to avoid citing the raw dataset path directly.
- **Files modified:** `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md`
- **Verification:** Task checks assert the forbidden raw dataset path is absent.
- **Committed in:** `fd67501`

**2. [Rule 1 - Bug] Adjusted guardrail wording to satisfy exact verification vocabulary**
- **Found during:** Task 3 verification
- **Issue:** Guardrail text included forbidden verification phrases while describing excluded work.
- **Fix:** Rephrased excluded work without using forbidden phrases, preserving the intended boundary.
- **Files modified:** `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md`
- **Verification:** Task 3 and overall Python checks passed.
- **Committed in:** `867fc5b`

---

**Total deviations:** 2 auto-fixed (1 missing critical, 1 bug)
**Impact on plan:** Both fixes preserved plan scope and strengthened compliance with raw-data and verification guardrails.

## Issues Encountered

- No blocking issues. Existing unrelated working-tree changes and untracked files were left untouched.

## User Setup Required

None - no external service configuration required.

## Known Stubs

None found in files created or modified by this plan.

## Next Phase Readiness

- Phase 2 Plan 02 can build on this artifact for the optional TR Part B theory-gap note and narrative integration.
- Phases 3, 4, 5, and 7 can cite the formulation, surrogate, posterior-error bridge, and validation-swap guardrails without reading raw datasets.

## Self-Check: PASSED

- Found `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md`.
- Found `.planning/phases/02-formulation-and-theory-bridge/02-01-SUMMARY.md`.
- Found task commit `fd67501`.
- Found task commit `2e4901d`.
- Found task commit `867fc5b`.

---
*Phase: 02-formulation-and-theory-bridge*
*Completed: 2026-05-22*
