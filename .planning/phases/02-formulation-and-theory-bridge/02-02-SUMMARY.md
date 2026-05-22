---
phase: 02-formulation-and-theory-bridge
plan: 02
subsystem: research-methodology
tags: [trace-sl, theory-gap, tr-part-b, narrative-handoff, readme]

requires:
  - phase: 02-formulation-and-theory-bridge
    provides: Budgeted reconstruction-aware formulation, RCSS surrogate, posterior-error bridge, and validation-swap guardrails from Plan 02-01
  - phase: 01-claim-evidence-contract
    provides: Certificate terminology, validation/test separation, and claim-evidence boundaries
provides:
  - Optional TR Part B theory-gap note covering THEORY-06, D-13, and D-14
  - Narrative-level formulation and theory bridge wording for manuscript handoff
  - Public README pointer to reconstruction-aware sensor-set design and Phase 2 artifacts
affects: [phase-03-baseline-portfolio, phase-04-core-experiment-evidence, phase-05-robustness-and-generality, phase-07-manuscript-package]

tech-stack:
  added: []
  patterns: [phase-local theory note, certificate-guided wording, validation/test separation, public method pointer]

key-files:
  created:
    - .planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md
    - .planning/phases/02-formulation-and-theory-bridge/02-02-SUMMARY.md
  modified:
    - NARRATIVE_REPORT.md
    - README.md
    - .planning/ROADMAP.md
    - .planning/REQUIREMENTS.md

key-decisions:
  - "TR Part B monotonicity, approximate-submodularity, approximation, stability, and stochastic/bilevel analyses are extension opportunities, not current TRACE-SL guarantees."
  - "Narrative wording presents TRACE-SL as budgeted reconstruction-aware sensor-set design while preserving the strong core claim and validation/test separation."
  - "README wording stays compact and public-facing, linking Phase 2 artifacts without adding derivations or new reproduction commands."

patterns-established:
  - "TR Part B theory gaps should be labeled deferred v2 unless a future phase scopes a narrow theorem."
  - "Narrative and README text should use certificate-guided or posterior-certificate-aware terminology outside the scoped linear-Gaussian squared-error identity."
  - "Public documentation can point to Phase 2 method artifacts without citing raw datasets as evidence sources."

requirements-completed: [THEORY-01, THEORY-02, THEORY-03, THEORY-04, THEORY-05, THEORY-06]

duration: 2 min
completed: 2026-05-22
---

# Phase 2 Plan 2: Formulation and Theory Bridge Handoff Summary

**TR Part B theory-gap boundary plus narrative and README handoff text for reconstruction-aware sensor-set design**

## Performance

- **Duration:** 2 min
- **Started:** 2026-05-22T02:09:10Z
- **Completed:** 2026-05-22T02:11:05Z
- **Tasks:** 3
- **Files modified:** 6

## Accomplishments

- Created the optional TR Part B theory-gap note for THEORY-06, explicitly naming D-13 and D-14 extension needs without expanding Phase 2 scope.
- Added a `Formulation and theory bridge` subsection to `NARRATIVE_REPORT.md` that separates train-derived reconstruction ingredients, validation layout selection, and held-out test evaluation.
- Added a compact README method pointer describing TRACE-SL as reconstruction-aware sensor-set design and linking the Phase 2 formulation and TR Part B gap artifacts.

## Task Commits

Each task was committed atomically:

1. **Task 1: Create the TR Part B theory-gap note** - `797ebb2` (docs)
2. **Task 2: Update the narrative report with method/theory bridge wording** - `c2defd3` (docs)
3. **Task 3: Add a compact README method-formulation pointer** - `b0be17d` (docs)

**Plan metadata:** final metadata commit records this summary plus GSD roadmap and requirement updates.

## Files Created/Modified

- `.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md` - Optional TR Part B theory-gap note covering THEORY-06, D-13, D-14, and deferred v2 boundaries.
- `NARRATIVE_REPORT.md` - Added narrative-level formulation/theory bridge wording near the Method Summary.
- `README.md` - Added a compact public-facing formulation pointer and repository-layout links to Phase 2 artifacts.
- `.planning/REQUIREMENTS.md` - Marked THEORY-06 complete through the GSD requirements command; THEORY-01..05 were already complete.
- `.planning/ROADMAP.md` - Updated Phase 2 plan progress through the GSD roadmap command.
- `.planning/phases/02-formulation-and-theory-bridge/02-02-SUMMARY.md` - Execution summary and context handoff.

## Decisions Made

- TR Part B remains an optional extension path: monotonicity, approximate submodularity, approximation guarantees, stability under covariance perturbation, and stochastic/bilevel optimization analysis are named as future needs rather than current guarantees.
- The Transportation Science narrative remains strong: TRACE-SL is framed as budgeted reconstruction-aware sensor-set design, not narrowed to a heuristic-only contribution.
- Certificate language remains certificate-guided or posterior-certificate-aware except within the scoped linear-Gaussian squared-error posterior-trace identity.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- GSD `state.advance-plan`, `state.update-progress`, `state.record-metric`, and `state.record-session` commands returned no-op/error messages because the current `STATE.md` format lacks the fields those handlers parse. No manual STATE edit was made; roadmap and requirements updates were performed only through GSD commands as requested.
- Existing unrelated working-tree changes and untracked files were left untouched.

## User Setup Required

None - no external service configuration required.

## Known Stubs

None found in files created or modified by this plan.

## Next Phase Readiness

- Phase 2 is ready for verification: THEORY-01..THEORY-06 now have Phase 2 artifacts and public/narrative pointers.
- Phase 3 can use the formulation and TR Part B boundary when deciding reviewer-grade baselines and multistart portfolio/comparator wording.
- Phase 7 can reuse the narrative bridge and README pointer while preserving validation/test separation and certificate terminology guardrails.

## Self-Check: PASSED

- Found `.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md`.
- Found `NARRATIVE_REPORT.md`.
- Found `README.md`.
- Found `.planning/phases/02-formulation-and-theory-bridge/02-02-SUMMARY.md`.
- Found task commit `797ebb2`.
- Found task commit `c2defd3`.
- Found task commit `b0be17d`.
- Task-level and plan-level Python verification checks passed.

---
*Phase: 02-formulation-and-theory-bridge*
*Completed: 2026-05-22*
