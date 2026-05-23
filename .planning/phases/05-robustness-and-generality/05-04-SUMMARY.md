---
phase: 05-robustness-and-generality
plan: 04
subsystem: research-evidence-validation
tags: [python, pandas, robustness, validation, trace-sl, claim-contract]

requires:
  - phase: 05-robustness-and-generality
    provides: Stage 14 robustness and candidate-sensitivity artifacts from Plan 05-03
  - phase: 04-core-experiment-evidence
    provides: Phase 4 held-out evidence discipline, validation/test separation, and claim contract references
provides:
  - Final fail-closed ROBUST-01..ROBUST-06 validator
  - Synthetic validator regression tests
  - Phase 5 robustness evidence audit
  - Claim-evidence contract synchronization for Stage 14 robustness artifacts
affects: [phase-05-verification, phase-06-reproducibility, phase-07-manuscript]

tech-stack:
  added: []
  patterns:
    - stdlib-plus-pandas artifact validator
    - synthetic temporary artifact tests
    - fail-closed evidence/caveat status reporting

key-files:
  created:
    - .planning/phases/05-robustness-and-generality/validate_phase5_robustness.py
    - .planning/phases/05-robustness-and-generality/test_validate_phase5_robustness.py
    - .planning/phases/05-robustness-and-generality/05-ROBUSTNESS-EVIDENCE-AUDIT.md
  modified:
    - .planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md

key-decisions:
  - "ROBUST-06 is fail-closed unless all candidate counts 50/100/200/500 appear in performance and runtime artifacts or a validator-recognized limited-tractability caveat is present."
  - "Phase 5 robustness claims are bounded to Stage 14 tested perturbations and candidate-pool settings, not deployment-wide robustness."

patterns-established:
  - "Validator prints one PASS/WARN/FAIL row per ROBUST requirement and exits nonzero on uncaveated failures."
  - "Evidence audits map robustness requirements to curated trace_sl_results artifacts rather than raw data."

requirements-completed: [ROBUST-01, ROBUST-02, ROBUST-03, ROBUST-04, ROBUST-05, ROBUST-06]

duration: 20min
completed: 2026-05-23
---

# Phase 05 Plan 04: Final Robustness Validator and Claim Sync Summary

**Fail-closed ROBUST-01..06 Stage 14 validator with synthetic tests, evidence audit, and bounded claim-contract routing.**

## Performance

- **Duration:** 20 min
- **Started:** 2026-05-23T02:47:00Z
- **Completed:** 2026-05-23T03:07:28Z
- **Tasks:** 3
- **Files modified:** 4

## Accomplishments

- Built `.planning/phases/05-robustness-and-generality/validate_phase5_robustness.py`, a stdlib-plus-pandas fail-closed validator for ROBUST-01..ROBUST-06.
- Added synthetic regression tests covering PASS, missing core artifacts, missing condition columns, uncaveated candidate runtime gaps, and valid ROBUST-06 caveat WARN behavior.
- Documented the Phase 5 evidence audit and synchronized the Phase 1 claim-evidence contract with Stage 14 robustness/candidate artifacts and bounded claim language.

## Task Commits

Each task was committed atomically:

1. **Task 1 RED: failing tests for robustness validator** - `31ee7c9` (test)
2. **Task 1 GREEN: fail-closed validator implementation** - `9df7c83` (feat)
3. **Task 2: Phase 5 robustness evidence audit** - `49caa05` (docs)
4. **Task 3: claim-evidence contract synchronization** - `936b8a1` (docs)

**Plan metadata:** pending final metadata commit

## Files Created/Modified

- `.planning/phases/05-robustness-and-generality/validate_phase5_robustness.py` - Validates Stage 14 robustness and candidate artifacts, prints ROBUST-01..06 statuses, supports `--project-root`/`--root`, and does not read raw datasets.
- `.planning/phases/05-robustness-and-generality/test_validate_phase5_robustness.py` - Uses temporary synthetic artifacts to test pass/fail/WARN validator behavior without raw dataset reads.
- `.planning/phases/05-robustness-and-generality/05-ROBUSTNESS-EVIDENCE-AUDIT.md` - Maps ROBUST-01..06 to artifact paths, required columns, caveats, validator status, and claim implications.
- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` - Adds Stage 14 robustness/candidate evidence references while preserving Phase 4 evidence, validation/test separation, certificate-guided wording, and low-budget caveats.

## Verification

All required commands passed without masking failures:

```bash
python -m py_compile .planning/phases/05-robustness-and-generality/validate_phase5_robustness.py .planning/phases/05-robustness-and-generality/test_validate_phase5_robustness.py
python .planning/phases/05-robustness-and-generality/test_validate_phase5_robustness.py
python .planning/phases/05-robustness-and-generality/validate_phase5_robustness.py
```

Real validator output:

```text
ROBUST-01 PASS: artifact-backed evidence and required schema checks passed
ROBUST-02 PASS: artifact-backed evidence and required schema checks passed
ROBUST-03 PASS: artifact-backed evidence and required schema checks passed
ROBUST-04 PASS: artifact-backed evidence and required schema checks passed
ROBUST-05 PASS: artifact-backed evidence and required schema checks passed
ROBUST-06 PASS: artifact-backed evidence and required schema checks passed
```

Additional assertions passed:

- `phase5-audit-ok`
- `claim-contract-phase5-sync-ok`
- `validator-source-raw-dataset-path-ok`

## Decisions Made

- ROBUST-06 caveat handling is restricted to a machine-readable `candidate_sensitivity_caveat.json` with `requirement=ROBUST-06`, `allowed_exception=true`, nonempty missing/completed counts, a nonempty reason, `evidence_attempted=true`, and limited-tractability disposition.
- Cost evidence is documented as a deterministic proxy with limitations, not a full heterogeneous procurement model.
- Claim contract language now routes Phase 5 evidence to tested perturbations and candidate-pool settings only.

## Deviations from Plan

None - plan executed as written.

## Issues Encountered

- During RED, the synthetic test helper initially needed `extrasaction="ignore"` so a missing-column fixture could write intentionally incomplete CSV headers. This was fixed before the RED test commit and did not change the plan scope.

## Known Stubs

None found in files created/modified by this plan.

## Threat Flags

None. The validator introduces artifact-schema checking only and does not add network endpoints, auth paths, raw file access, or schema changes at trust boundaries.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 5 now has a final automated validator, evidence audit, and claim-contract synchronization. Phase 6 can use these files as reproducibility gates and Phase 7 can draw bounded robustness wording from the audit.

## Self-Check: PASSED

- Found created files: validator, tests, robustness audit.
- Found modified claim-evidence contract.
- Found task commits: `31ee7c9`, `9df7c83`, `49caa05`, `936b8a1`.

---
*Phase: 05-robustness-and-generality*
*Completed: 2026-05-23*
