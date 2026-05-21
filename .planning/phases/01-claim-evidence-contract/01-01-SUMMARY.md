---
phase: 01-claim-evidence-contract
plan: 01
subsystem: research-planning
tags: [trace-sl, claim-evidence, transportation-science, documentation]
requires:
  - phase: project-initialization
    provides: PROJECT, ROADMAP, REQUIREMENTS, Phase 1 CONTEXT/PATTERNS, and curated TRACE-SL result summaries
provides:
  - Phase-local claim-evidence contract for TRACE-SL paper claims
  - Auditable C-01..C-05 matrix mapped to CLAIM-01..CLAIM-05
  - Guardrails for validation MAE, certificate wording, multistart caveat, Seattle status, and raw-data hygiene
affects: [phase-02-theory, phase-03-baselines, phase-04-experiments, phase-05-robustness, phase-06-reproducibility, phase-07-manuscript]
tech-stack:
  added: []
  patterns:
    - Markdown claim-evidence matrix with stable claim IDs and downstream owners
    - Curated-result references only; no raw dataset evidence dependency
key-files:
  created:
    - .planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md
    - .planning/phases/01-claim-evidence-contract/01-01-SUMMARY.md
  modified: []
key-decisions:
  - "TRACE-SL claims remain strong but are routed to explicit evidence, theory, audit, or limitation wording."
  - "Validation MAE is selection evidence only; held-out test metrics are required for performance claims."
  - "Certificate terminology remains certificate-guided/posterior-certificate-aware unless Phase 2 adds theorem-level support."
patterns-established:
  - "C-01..C-05 claim rows map directly to CLAIM-01..CLAIM-05 and D-01..D-15."
  - "Downstream phase owners are explicit for theory, baseline, evidence, robustness, curation, and manuscript work."
requirements-completed: [CLAIM-01, CLAIM-02, CLAIM-03, CLAIM-04, CLAIM-05]
duration: 3 min
completed: 2026-05-21
---

# Phase 1 Plan 01: Claim-Evidence Contract Summary

**TRACE-SL claim-evidence contract with auditable C-01..C-05 rows, curated evidence routing, and paper-facing overclaim guardrails.**

## Performance

- **Duration:** 3 min
- **Started:** 2026-05-21T14:29:23Z
- **Completed:** 2026-05-21T14:32:33Z
- **Tasks:** 3/3
- **Files modified:** 2

## Accomplishments

- Created `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` as the single Phase 1 contract artifact.
- Added a machine-auditable matrix with C-01 through C-05 mapped to CLAIM-01 through CLAIM-05 and D-01 through D-15.
- Locked guardrails against unsupported “best at all budgets,” formal “certified” branding, validation-MAE-as-test-evidence, non-curated Seattle core claims, and post-hoc best-method-per-budget selection.
- Routed unresolved theory, baseline, audit, robustness, reproducibility, and manuscript work to Phases 2 through 7 without expanding Phase 1 scope.

## Task Commits

Each task was committed atomically:

1. **Task 1: Create the contract scaffold and phase boundary** - `b6e1685` (docs)
2. **Task 2: Populate the claim-evidence matrix** - `3fd76e6` (docs)
3. **Task 3: Add guardrails, routing, and self-checks** - `0029a3d` (docs)

**Plan metadata:** committed separately after summary creation.

## Files Created/Modified

- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` - Phase-local claim-evidence contract, source register, matrix, guardrails, routing, and self-check.
- `.planning/phases/01-claim-evidence-contract/01-01-SUMMARY.md` - This execution summary.

## Decisions Made

- Preserved the strong TRACE-SL framing as transparent reconstruction-aware sparse traffic sensor placement, while requiring explicit evidence or limitation wording for every primary claim.
- Treated the 10% PeMS7_228 multistart-vs-RCSS issue as a predeclared comparator/portfolio or bounded-caveat item rather than an ignored anomaly.
- Kept Seattle evidence conditional/supporting-only until Phase 4 curation verifies repository-visible outputs and documentation consistency.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None. Existing unrelated working-tree changes were left untouched as required.

## Verification

Passed:

- Contract file exists at `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md`.
- CLAIM-01 through CLAIM-05 all appear in the contract.
- C-01 through C-05 all appear in the contract.
- Required tokens appear: `10% PeMS7_228`, `multistart`, `certificate-guided`, `TSLP`, `black-box`, `validation MAE`, `held-out test`, and `conditional/supporting-only`.
- No non-comment evidence source requires raw dataset reads matching `TRC-23-02333/dataset/.*(csv|npy|npz)`.

## Known Stubs

None. Placeholder text used during Task 1 was removed by Task 3.

## Threat Flags

None. This plan created documentation only and introduced no new network endpoints, auth paths, file-access code paths, or schema changes.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Ready for Phase 2 formulation/theory planning. The contract now defines which claims need theory, which evidence needs audit, and which wording must remain bounded until downstream work is complete.

## Self-Check: PASSED

- Created contract file exists.
- Summary file exists.
- Task commits exist: `b6e1685`, `3fd76e6`, `0029a3d`.
- Overall verification passed.

---
*Phase: 01-claim-evidence-contract*
*Completed: 2026-05-21*
