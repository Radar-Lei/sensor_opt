---
phase: 07-claim-and-main-table-contract
plan: "01"
subsystem: research-artifacts
tags: [trace-sl, claim-contract, paper-sources, pandas, unittest]

requires:
  - phase: 06-reproducibility-and-artifact-curation
    provides: committed TRACE-SL aggregate result artifacts and paper-source generation patterns
provides:
  - deterministic Phase 7 claim contract generator with fail-fast validators
  - Stage12 PeMS7_228 main-table contract derived from tracked aggregate CSV evidence
  - regression tests for wording, evidence routing, provenance, and caveat guardrails
affects: [phase-07, phase-08, phase-09, phase-10, paper-sources]

tech-stack:
  added: []
  patterns:
    - dynamic-import unittest regression script
    - CSV/JSON-first generated research contracts
    - git-tracked curated source enforcement

key-files:
  created:
    - scripts/generate_trace_sl_claim_contracts.py
    - scripts/test_generate_trace_sl_claim_contracts.py
    - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv
    - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json
    - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md
    - TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv
    - TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md
  modified:
    - TRC-23-02333/trace_sl_results/paper_sources/README.md

key-decisions:
  - "Phase 7 claim-facing evidence uses held-out Stage12 PeMS7_228 test aggregates and paired comparisons, not validation MAE."
  - "PeMS7_1026 and Seattle remain external/supporting in Phase 7 until Phase 8 Stage12 10-split evidence is complete."
  - "Robustness evidence remains stress-test or appendix routed unless a row explicitly declares multi-seed perturbation evidence."

patterns-established:
  - "Contract generator validates source provenance, schema, claim lanes, forbidden wording, and caveat tags before writing outputs."
  - "Main-table rows attach the low-budget multistart caveat to all 10% budget rows and multistart-sensitive comparisons."

requirements-completed: [CLAIM-01, CLAIM-02, CLAIM-03, CLAIM-04, EVID-01, EVID-02, HAND-01]

duration: 7min
completed: 2026-05-23
---

# Phase 7 Plan 01: Claim and Main Table Contract Generator Summary

**Deterministic TRACE-SL claim/table contract generator with fail-fast wording, routing, provenance, and low-budget multistart caveat enforcement**

## Performance

- **Duration:** 7 min
- **Started:** 2026-05-23T11:57:57Z
- **Completed:** 2026-05-23T12:04:30Z
- **Tasks:** 2
- **Files modified:** 8

## Accomplishments

- Added fail-fast regression tests covering Phase 7 claim lanes, exact forbidden/allowed wording, Stage12 schema validation, external-evidence boundaries, robustness routing, and multistart caveat tags.
- Implemented `scripts/generate_trace_sl_claim_contracts.py` with top-level builder/validator functions and a CLI that reads only tracked curated aggregate sources under `TRC-23-02333/trace_sl_results/`.
- Generated CSV/JSON/Markdown paper-source contracts for the claim policy and PeMS7_228 Stage12 main table, including paired-stat provenance and caveat tags.

## Task Commits

1. **Task 1: Write fail-fast contract regression tests** - `60dda3e` (test)
2. **Task 2: Implement deterministic claim/table contract generator** - `3c32154` (feat)

**Plan metadata:** pending final docs commit

_Note: This plan used TDD-style task commits: RED test commit followed by GREEN implementation/artifact commit._

## Files Created/Modified

- `scripts/test_generate_trace_sl_claim_contracts.py` - Unittest regression suite using dynamic import and temporary Stage12-style CSV fixtures.
- `scripts/generate_trace_sl_claim_contracts.py` - Deterministic generator, validators, JSON policy builder, and CLI for Phase 7 contracts.
- `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv` - Machine-readable claim lane, wording, caveat, and evidence-routing contract.
- `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json` - Deterministic policy metadata with forbidden wording, allowed wording, routing rules, caveat tags, and source pointers.
- `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md` - Markdown view generated from the claim contract rows.
- `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv` - Stage12 PeMS7_228 main-table contract rows joined to paired comparison statistics.
- `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md` - Markdown view generated from main-table contract rows.
- `TRC-23-02333/trace_sl_results/paper_sources/README.md` - Paper-source index updated with the new contract generator and outputs.

## Decisions Made

- Used the existing paper-source generator style: standalone Python CLI, pandas CSV loading, deterministic JSON/Markdown writers, and `git ls-files --error-unmatch` tracked-source validation.
- Kept `greedy_d_logdet` optional as a secondary certificate baseline when present; required reviewer-facing rows are the Phase 7 `MAIN_TABLE_LAYOUT_LABELS` set.
- Represented unavailable RMSE/MAPE source metrics as blank contract fields because Stage12 `gls_map_layout_summary.csv` provides MAE `mean/std/count`; tests verify this is schema-stable rather than manuscript prose.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] Generated contract artifacts during Task 2**
- **Found during:** Task 2 (Implement deterministic claim/table contract generator)
- **Issue:** The task primarily specified the generator, but Phase 7 success criteria and later plan readiness need concrete paper-source contract outputs to validate raw-data hygiene and provenance.
- **Fix:** Ran the generator after implementation and committed the generated CSV/JSON/Markdown contracts plus the updated paper-source README with the task commit.
- **Files modified:** `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.*`, `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.*`, `TRC-23-02333/trace_sl_results/paper_sources/README.md`
- **Verification:** `python scripts/test_generate_trace_sl_claim_contracts.py`; generator CLI run; grep confirmed generated contract artifacts do not reference `TRC-23-02333/dataset/`.
- **Committed in:** `3c32154`

---

**Total deviations:** 1 auto-fixed (Rule 2 missing critical)
**Impact on plan:** The added generated artifacts are required for correctness and downstream readiness; no manuscript prose or raw dataset access was introduced.

## Issues Encountered

- The RED test run failed as expected because `scripts/generate_trace_sl_claim_contracts.py` did not exist before implementation.
- No authentication gates, package installs, or architectural blockers occurred.

## User Setup Required

None - no external service configuration required.

## Known Stubs

None. Stub scan found only a negative-test mutation that intentionally sets `caveat_tag=""` to verify fail-closed behavior.

## Threat Flags

None. The new generator introduces file reads and generated artifact writes only within the planned curated aggregate boundary; raw dataset paths are rejected or omitted.

## Verification

- `python scripts/test_generate_trace_sl_claim_contracts.py` — passed.
- `python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources` — passed.
- `grep -R "TRC-23-02333/dataset/"` across generated claim/table artifacts — no matches.

## Self-Check: PASSED

- FOUND: `scripts/generate_trace_sl_claim_contracts.py`
- FOUND: `scripts/test_generate_trace_sl_claim_contracts.py`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md`
- FOUND commit: `60dda3e`
- FOUND commit: `3c32154`

## Next Phase Readiness

- Plan 07-02 can consume the generated claim/table contracts directly or re-run the deterministic generator for idempotent output validation.
- Phase 8 must still complete PeMS7_1026 and Seattle Stage12 10-split evidence before either dataset is elevated beyond external/supporting status.

---
*Phase: 07-claim-and-main-table-contract*
*Completed: 2026-05-23*
