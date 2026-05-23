---
phase: 06-reproducibility-and-artifact-curation
plan: 01
subsystem: reproducibility
tags: [trace-sl, provenance, manifest, reproducibility, standard-library]
requires:
  - phase: 04-core-experiment-evidence
    provides: Curated Stage 12 baseline-portfolio evidence artifacts
  - phase: 05-robustness-and-generality
    provides: Curated Stage 13/14 sensitivity and robustness evidence artifacts
provides:
  - Deterministic TRACE-SL reproducibility manifest generator
  - Machine-readable JSON provenance inventory for curated Stage 12/13/14 and supporting evidence
  - Human-readable Markdown provenance inventory with launcher defaults and raw-data hygiene
affects: [06-03-final-validation, paper-writing, artifact-curation]
tech-stack:
  added: []
  patterns:
    - Standard-library manifest generation without sourcing shell launchers
    - Path-only raw dataset hygiene scan via git ls-files
key-files:
  created:
    - scripts/generate_trace_sl_repro_manifest.py
    - scripts/test_generate_trace_sl_repro_manifest.py
    - TRC-23-02333/trace_sl_results/reproducibility_manifest.json
    - TRC-23-02333/trace_sl_results/REPRODUCIBILITY_MANIFEST.md
  modified: []
key-decisions:
  - "Raw datasets are represented only through path-count hygiene metadata and are excluded from evidence artifact inventories."
  - "Generated manifest provenance records the latest input-affecting commit while excluding generated manifest outputs to keep reruns idempotent."
patterns-established:
  - "parse_shell_defaults reads simple launcher defaults from text without sourcing or executing shell."
  - "inventory_result_dir records relative CSV/JSON/Markdown artifact paths, sizes, and evidence eligibility."
requirements-completed: [REPRO-01, REPRO-02, REPRO-03]
duration: 8min
completed: 2026-05-23
---

# Phase 06 Plan 01: Reproducibility Manifest Summary

**Deterministic TRACE-SL provenance manifest with launcher defaults, environment metadata, curated artifact inventory, and raw-data hygiene boundaries**

## Performance

- **Duration:** 8 min
- **Started:** 2026-05-23T04:14:18Z
- **Completed:** 2026-05-23T04:22:39Z
- **Tasks:** 2
- **Files modified:** 4

## Accomplishments

- Added TDD contract tests for launcher default parsing, curated artifact inventory, and optional package metadata reporting.
- Implemented a standard-library manifest generator that inventories curated TRACE-SL Stage 12/13/14 plus supporting evidence without reading raw datasets or running experiments.
- Generated JSON and Markdown reproducibility manifests under `TRC-23-02333/trace_sl_results/`, including launcher seeds/budgets/candidate defaults, package metadata, git provenance, and zero tracked raw dataset paths.

## Task Commits

Each task was committed atomically:

1. **Task 1: Specify manifest extraction behavior** - `55a7471` (test)
2. **Task 2: Implement and generate reproducibility manifest** - `1df1c37` (feat)
3. **Task 2 auto-fix: deterministic timestamp** - `31657da` (fix)
4. **Task 2 auto-fix: refreshed manifest provenance** - `f452f4f` (fix)
5. **Task 2 auto-fix: stable input-scoped git provenance** - `55f234c` (fix)
6. **Task 2 auto-fix: refreshed input commit** - `f4173df` (fix)

_Note: TDD produced a RED test commit before implementation._

## Files Created/Modified

- `scripts/test_generate_trace_sl_repro_manifest.py` - Standard-library `unittest` coverage for parser, inventory, and environment metadata contracts.
- `scripts/generate_trace_sl_repro_manifest.py` - Deterministic provenance manifest generator using only Python standard library.
- `TRC-23-02333/trace_sl_results/reproducibility_manifest.json` - Machine-readable manifest for curated TRACE-SL evidence.
- `TRC-23-02333/trace_sl_results/REPRODUCIBILITY_MANIFEST.md` - Human-readable manifest table and provenance summary.

## Decisions Made

- Kept raw dataset handling to `git ls-files -- TRC-23-02333/dataset/` path-count hygiene only; no raw dataset contents are opened or inventoried as evidence.
- Used `importlib.metadata` instead of importing numerical packages so environment collection is non-invasive and works when optional packages are absent.
- Recorded latest input-affecting git commit while excluding generated manifest outputs, because recording the manifest output commit itself makes repeated generation non-idempotent.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Made generated manifest deterministic**
- **Found during:** Task 2 (Implement and generate reproducibility manifest)
- **Issue:** `generated_at_utc` used wall-clock time, so the required generator command changed outputs on every run.
- **Fix:** Replaced it with a fixed deterministic timestamp plus explanatory provenance note.
- **Files modified:** `scripts/generate_trace_sl_repro_manifest.py`, generated JSON/Markdown manifests
- **Verification:** `python scripts/test_generate_trace_sl_repro_manifest.py` and required generator command passed.
- **Committed in:** `31657da`

**2. [Rule 1 - Bug] Stabilized git provenance after output commits**
- **Found during:** Task 2 (Implement and generate reproducibility manifest)
- **Issue:** Recording current `HEAD` made the manifest self-referential; after committing generated outputs, rerunning the generator changed the recorded commit.
- **Fix:** Added input-scoped commit provenance using `git rev-list -1 HEAD -- <inputs>` while excluding generated manifest outputs.
- **Files modified:** `scripts/generate_trace_sl_repro_manifest.py`, generated JSON/Markdown manifests
- **Verification:** Required generator command reran without changing tracked plan files after final refresh.
- **Committed in:** `55f234c`, `f4173df`

---

**Total deviations:** 2 auto-fixed bugs
**Impact on plan:** Both fixes were necessary to satisfy the plan's deterministic-manifest requirement; no scope expansion.

## Issues Encountered

- The generated manifest files are under an ignored result directory, so they required explicit `git add -f` while still staging only plan-related files.
- The main workspace had pre-existing unrelated changes and untracked files; these were intentionally left unstaged and untouched.

## Known Stubs

None detected in created/modified plan files.

## Threat Flags

None. The new script reads launcher text, curated result artifact metadata, and git metadata only; it introduces no network endpoints, auth paths, raw file disclosure, or schema trust-boundary changes beyond the threat model.

## User Setup Required

None - no external service configuration required.

## Verification

- `python scripts/test_generate_trace_sl_repro_manifest.py` passed.
- `python scripts/generate_trace_sl_repro_manifest.py --project-root /home/samuel/projects/sensor_opt --output-json TRC-23-02333/trace_sl_results/reproducibility_manifest.json --output-md TRC-23-02333/trace_sl_results/REPRODUCIBILITY_MANIFEST.md` passed.
- Manifest reports 6 curated result stages and 0 tracked raw dataset paths.

## Next Phase Readiness

- Plan 06-03 can validate REPRO-01..03 against `reproducibility_manifest.json` and `REPRODUCIBILITY_MANIFEST.md`.
- Plan 06-02 paper-source generation can proceed independently; no shared files were modified.

## Self-Check: PASSED

- Confirmed all created files exist.
- Confirmed task and auto-fix commits exist in git history: `55a7471`, `1df1c37`, `31657da`, `f452f4f`, `55f234c`, `f4173df`.

---
*Phase: 06-reproducibility-and-artifact-curation*
*Completed: 2026-05-23*
