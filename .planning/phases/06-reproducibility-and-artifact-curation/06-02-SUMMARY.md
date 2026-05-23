---
phase: 06-reproducibility-and-artifact-curation
plan: 02
subsystem: reproducibility
tags: [trace-sl, paper-sources, csv, markdown, pandas, reproducibility]

requires:
  - phase: 04-core-experiment-evidence
    provides: Phase 4 Stage 12/13 committed aggregate CSV artifacts and verification reports
  - phase: 05-robustness-and-generality
    provides: Phase 5 Stage 14 committed robustness and candidate/runtime aggregate artifacts
provides:
  - Deterministic paper-source generator for TRACE-SL manuscript tables
  - Provenance-backed CSV/Markdown paper-source artifacts under trace_sl_results/paper_sources
  - TDD regression tests for core performance, robustness rows, and Markdown rendering
affects: [phase-06-final-validation, paper-writing, reproducibility-artifacts]

tech-stack:
  added: []
  patterns: [standard-library unittest, pandas CSV transforms, deterministic Markdown rendering, git-tracked aggregate-source validation]

key-files:
  created:
    - scripts/test_generate_trace_sl_paper_sources.py
    - scripts/generate_trace_sl_paper_sources.py
    - TRC-23-02333/trace_sl_results/paper_sources/core_performance_table.csv
    - TRC-23-02333/trace_sl_results/paper_sources/core_performance_table.md
    - TRC-23-02333/trace_sl_results/paper_sources/paired_delta_table.csv
    - TRC-23-02333/trace_sl_results/paper_sources/robustness_condition_table.csv
    - TRC-23-02333/trace_sl_results/paper_sources/candidate_runtime_table.csv
    - TRC-23-02333/trace_sl_results/paper_sources/certificate_correlation_table.csv
    - TRC-23-02333/trace_sl_results/paper_sources/README.md
  modified:
    - .gitignore

key-decisions:
  - "Generate manuscript-facing paper sources only from committed aggregate CSVs and fail closed when a source CSV is missing, empty, outside trace_sl_results, or untracked by git."
  - "Keep source provenance on every generated row through source_stage, source_dir, and source_csv columns."
  - "Expose only the curated paper_sources and Stage 14 result directories through .gitignore exceptions while continuing to ignore raw datasets."

patterns-established:
  - "Paper-source rows are generated from aggregate CSVs by pure helper functions with TDD coverage."
  - "CSV outputs are primary machine-readable sources; Markdown is rendered deterministically from the same rows."

requirements-completed: [REPRO-04, REPRO-01]

duration: 5min
completed: 2026-05-23
---

# Phase 06 Plan 02: Paper-Source Table Generation Summary

**Deterministic TRACE-SL paper-source CSV/Markdown tables generated from committed Phase 4/5 aggregate artifacts with per-row provenance.**

## Performance

- **Duration:** 5 min
- **Started:** 2026-05-23T04:14:03Z
- **Completed:** 2026-05-23T04:18:50Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Added TDD coverage for core performance label filtering/provenance, robustness condition preservation, and deterministic Markdown rendering.
- Implemented `scripts/generate_trace_sl_paper_sources.py` to read only committed aggregate CSVs under `TRC-23-02333/trace_sl_results/` and fail closed on untracked/missing/empty source CSVs.
- Generated nonempty paper-source CSV/Markdown artifacts for core performance, paired deltas, robustness conditions, candidate/runtime sensitivity, and certificate correlations.
- Preserved required method labels where present: `validation_swap_selected`, `rcss_selected`, `multistart_swap_by_validation`, `greedy_a_trace`, `greedy_d_logdet`, `observability_proxy`, `graph_sampling_laplacian`, and `qr_pod_modes`.

## Task Commits

Each task was committed atomically:

1. **Task 1: Specify paper-source generation behavior** - `9819490` (test)
2. **Task 2: Implement and generate paper-source tables** - `37e2fc5` (feat)

## Files Created/Modified

- `scripts/test_generate_trace_sl_paper_sources.py` - Standard-library unittest suite for paper-source generation helpers.
- `scripts/generate_trace_sl_paper_sources.py` - Deterministic generator over committed aggregate CSVs with provenance columns and Markdown rendering.
- `TRC-23-02333/trace_sl_results/paper_sources/core_performance_table.csv` - Stage 12 core GLS/MAP performance source table.
- `TRC-23-02333/trace_sl_results/paper_sources/core_performance_table.md` - Deterministic Markdown rendering of the core performance table.
- `TRC-23-02333/trace_sl_results/paper_sources/paired_delta_table.csv` - Stage 12 paired delta/test source table for the main method against available baselines.
- `TRC-23-02333/trace_sl_results/paper_sources/robustness_condition_table.csv` - Stage 14 robustness-condition performance source table.
- `TRC-23-02333/trace_sl_results/paper_sources/candidate_runtime_table.csv` - Stage 14 candidate-count runtime and candidate diagnostic source table.
- `TRC-23-02333/trace_sl_results/paper_sources/certificate_correlation_table.csv` - Stage 12/13 empirical certificate-correlation source table.
- `TRC-23-02333/trace_sl_results/paper_sources/README.md` - Regeneration command and paper-source artifact description.
- `.gitignore` - Added precise exceptions for committed Stage 14 and paper-source result directories; raw datasets remain ignored.

## Generated Table Metrics

| Table | Rows | Provenance columns |
|---|---:|---|
| `core_performance_table.csv` | 24 | `source_stage`, `source_dir`, `source_csv` |
| `paired_delta_table.csv` | 33 | `source_stage`, `source_dir`, `source_csv` |
| `robustness_condition_table.csv` | 72 | `source_stage`, `source_dir`, `source_csv` |
| `candidate_runtime_table.csv` | 68 | `source_stage`, `source_dir`, `source_csv` |
| `certificate_correlation_table.csv` | 12 | `source_stage`, `source_dir`, `source_csv` |

## Decisions Made

- Used pandas only, matching the existing project dependency set; no package installs or new dependencies were added.
- Treated git-tracked source verification as part of correctness so generated paper sources cannot silently read uncommitted ad hoc outputs.
- Kept generated CSVs as the authoritative paper-source artifacts and generated Markdown only for the core performance table requested by the plan.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Preserved requested method-label order and normalized synthetic TRACE-SL paths**
- **Found during:** Task 2 (Implement and generate paper-source tables)
- **Issue:** Initial implementation sorted core rows alphabetically and returned absolute temporary paths in synthetic tests.
- **Fix:** Added stable ordering by requested label list and normalized paths rooted at `TRC-23-02333` when outside the active project root.
- **Files modified:** `scripts/generate_trace_sl_paper_sources.py`
- **Verification:** `python scripts/test_generate_trace_sl_paper_sources.py`
- **Committed in:** `37e2fc5`

**2. [Rule 3 - Blocking] Added precise `.gitignore` exceptions for generated paper sources**
- **Found during:** Task 2 (Implement and generate paper-source tables)
- **Issue:** Existing `TRC-23-02333/trace_sl_results/*` ignore rule hid the required generated `paper_sources/` outputs from git.
- **Fix:** Added narrow exceptions for `paper_sources/` and the committed Stage 14 source directories; raw dataset ignores were left unchanged.
- **Files modified:** `.gitignore`
- **Verification:** `git status --short --untracked-files=all -- TRC-23-02333/trace_sl_results/paper_sources`
- **Committed in:** `37e2fc5`

---

**Total deviations:** 2 auto-fixed (1 bug, 1 blocking issue)
**Impact on plan:** Both fixes were required to satisfy deterministic generation and committed-artifact handoff without expanding scope or touching raw datasets.

## Issues Encountered

- The RED TDD run failed as expected because `scripts/generate_trace_sl_paper_sources.py` did not exist yet.
- Existing unrelated workspace changes were left unstaged and uncommitted, including `.planning/quick` deletions, `idea-stage` edits, `.claude/`, Phase 1 UAT/verification files, and `scripts/generate_trace_sl_repro_manifest.py`.

## User Setup Required

None - no external service configuration required.

## Known Stubs

None found in plan-created/modified files. Stub-marker scan found no `TODO`, `FIXME`, `placeholder`, or `coming soon` markers in the generator, tests, or generated paper-source directory.

## Auth Gates

None.

## Next Phase Readiness

- Phase 06 Plan 03 can validate the generated `paper_sources/` layout and cross-check REPRO-04/05 against the committed CSV/Markdown artifacts.
- Manuscript rendering can consume these generated CSV/Markdown sources rather than manually copied numbers.

## Self-Check: PASSED

- Found all created generator, test, and paper-source files.
- Verified task commits exist: `9819490`, `37e2fc5`.
- Verification commands passed:
  - `python scripts/test_generate_trace_sl_paper_sources.py`
  - `python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources`

---
*Phase: 06-reproducibility-and-artifact-curation*
*Completed: 2026-05-23*
