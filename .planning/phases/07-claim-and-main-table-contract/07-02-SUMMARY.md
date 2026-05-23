---
phase: 07-claim-and-main-table-contract
plan: "02"
subsystem: research-artifacts
tags: [trace-sl, claim-contract, paper-sources, pandas, csv-json]

requires:
  - phase: 07-claim-and-main-table-contract
    provides: tested deterministic generator and initial Phase 7 contract artifacts from Plan 07-01
provides:
  - frozen CSV/JSON-first Phase 7 claim contract artifacts with plan-required schema marker
  - frozen PeMS7_228 Stage12 main-table contract artifacts with paired-stat provenance and caveat tags
  - paper-source README index covering Phase 7 generated contract files and regeneration commands
affects: [phase-07, phase-08, phase-09, phase-10, paper-sources, manuscript-handoff]

tech-stack:
  added: []
  patterns:
    - deterministic CSV/JSON-first research artifact generation
    - generated Markdown views backed by machine-readable rows
    - inline pandas/json integrity gates for contract policy enforcement

key-files:
  created: []
  modified:
    - scripts/generate_trace_sl_claim_contracts.py
    - scripts/test_generate_trace_sl_claim_contracts.py
    - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json
    - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv
    - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md
    - TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv
    - TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md
    - TRC-23-02333/trace_sl_results/paper_sources/README.md

key-decisions:
  - "Keep Phase 7 contract outputs CSV/JSON-first, with Markdown as generated views rather than manuscript prose."
  - "Use the plan-required `trace_sl_claim_contract_v1` schema marker as the machine-readable policy identifier."
  - "Treat PeMS7_1026, Seattle, and robustness evidence as non-core Phase 7 lanes until later evidence phases complete."

patterns-established:
  - "Contract regeneration must be followed by regression tests and inline CSV/JSON integrity assertions."
  - "README remains an artifact index and regeneration guide, not a manuscript section draft."

requirements-completed: [CLAIM-01, CLAIM-02, CLAIM-03, CLAIM-04, EVID-01, EVID-02, HAND-01]

duration: 3min
completed: 2026-05-23
---

# Phase 7 Plan 02: Frozen Claim and Main-Table Contract Artifacts Summary

**CSV/JSON-first TRACE-SL claim and main-table contracts regenerated with synchronized caveat, provenance, evidence-lane, and README integrity gates**

## Performance

- **Duration:** 3 min
- **Started:** 2026-05-23T12:07:31Z
- **Completed:** 2026-05-23T12:10:29Z
- **Tasks:** 2
- **Files modified:** 8

## Accomplishments

- Regenerated the Phase 7 claim/table contracts under `TRC-23-02333/trace_sl_results/paper_sources/` using the deterministic generator from Plan 07-01.
- Verified the frozen artifacts are nonempty, provenance-first, free of raw dataset evidence paths, and preserve the PeMS7_228 low-budget multistart caveat.
- Confirmed the paper-source README lists the new Phase 7 contract files, includes the regeneration command, and remains an artifact index rather than manuscript prose.

## Task Commits

1. **Task 1: Generate CSV/JSON-first claim and table artifacts** - `09c928f` (fix)
2. **Task 2: Update paper-source index and run contract integrity gates** - no new commit; README was already synchronized by the generator, and verification produced no additional diff.

**Plan metadata:** pending final docs commit

## Files Created/Modified

- `scripts/generate_trace_sl_claim_contracts.py` - Emits the plan-required `trace_sl_claim_contract_v1` JSON schema marker.
- `scripts/test_generate_trace_sl_claim_contracts.py` - Adds regression coverage for the JSON policy schema marker.
- `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json` - Machine-readable Phase 7 policy with the corrected schema marker.
- `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv` - Frozen claim lane, wording, caveat, and evidence-routing contract; regenerated and verified unchanged.
- `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md` - Generated Markdown view of the claim contract; regenerated and verified unchanged.
- `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv` - Frozen Stage12 PeMS7_228 main-table contract; regenerated and verified unchanged.
- `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md` - Generated Markdown view of the main-table contract; regenerated and verified unchanged.
- `TRC-23-02333/trace_sl_results/paper_sources/README.md` - Paper-source artifact index and regeneration guide; verified unchanged and complete.

## Decisions Made

- Used the generated CSV/JSON artifacts as the source of truth and treated Markdown files as synchronized generated views.
- Kept the README scoped to artifact inventory, provenance, raw-data hygiene, and regeneration commands; no introduction, related work, method, results, limitations, abstract, or conclusion prose was added.
- Preserved Phase 7 evidence boundaries: PeMS7_228 is the core in-domain contract source; PeMS7_1026 and Seattle remain external/supporting; robustness remains stress-test/appendix routed.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Corrected JSON policy schema marker**
- **Found during:** Task 2 (Update paper-source index and run contract integrity gates)
- **Issue:** The inline integrity gate required the machine-readable policy to contain `trace_sl_claim_contract_v1`, while the generated JSON used `trace-sl-phase7-claim-contract-v1`.
- **Fix:** Updated the generator to emit the plan-required schema marker, regenerated `claim_contract.json`, and added a regression test for the exact marker.
- **Files modified:** `scripts/generate_trace_sl_claim_contracts.py`, `scripts/test_generate_trace_sl_claim_contracts.py`, `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json`
- **Verification:** `python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources && python scripts/test_generate_trace_sl_claim_contracts.py`; inline CSV/JSON/README integrity gate passed.
- **Committed in:** `09c928f`

---

**Total deviations:** 1 auto-fixed (Rule 1 bug)
**Impact on plan:** The fix aligned the generated machine-readable policy with the plan acceptance criteria without changing claim scope, evidence routing, or manuscript boundaries.

## Issues Encountered

- The first Task 2 inline integrity gate failed because the generated JSON schema marker did not match the plan-required marker. The generator, regression test, and generated JSON were corrected and reverified.
- No authentication gates, package installs, raw dataset access, or architectural blockers occurred.

## User Setup Required

None - no external service configuration required.

## Known Stubs

None. Stub scan found only an intentional negative-test mutation in `scripts/test_generate_trace_sl_claim_contracts.py` that sets `caveat_tag=""` to verify fail-closed validation.

## Threat Flags

None. The plan introduced no new network endpoints, auth paths, file access patterns outside the planned curated aggregate boundary, or schema changes at trust boundaries. Raw dataset evidence paths are rejected by tests and integrity gates.

## Verification

- `python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources` — passed.
- `python scripts/test_generate_trace_sl_claim_contracts.py` — passed, 8 tests.
- Inline pandas/json integrity gate — passed: nonempty CSV/JSON artifacts, `trace_sl_claim_contract_v1` policy marker, low-budget caveat tag, no raw dataset paths, README links and regeneration command present, and no manuscript-section headings.

## Self-Check: PASSED

- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md`
- FOUND: `TRC-23-02333/trace_sl_results/paper_sources/README.md`
- FOUND commit: `09c928f`

## Next Phase Readiness

- Phase 7 has a frozen claim and main-table contract handoff for later writing work without generating manuscript prose.
- Phase 8 remains responsible for PeMS7_1026 and Seattle Stage12 10-split evidence before those datasets can support stronger external or core claims.

---
*Phase: 07-claim-and-main-table-contract*
*Completed: 2026-05-23*
