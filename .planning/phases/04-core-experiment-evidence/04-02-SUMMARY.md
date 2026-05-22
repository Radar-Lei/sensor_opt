---
phase: 04-core-experiment-evidence
plan: 02
subsystem: experiment-evidence
tags: [trace-sl, statistics, scipy, pandas, certificates]

requires:
  - phase: 03-baseline-portfolio
    provides: Stable final baseline and portfolio layout labels for paper-visible comparisons
  - phase: 04-core-experiment-evidence/04-01
    provides: Audited held-out GLS/MAP evidence scope and caveats
provides:
  - EXP-04 paired GLS/MAP comparison statistics with intervals, effect sizes, paired tests, win counts, and matched-pair counts
  - EXP-05 empirical certificate-error correlation summaries with count fields and non-formal wording
affects: [paper-results, trace-sl-results, reproducibility, phase-04]

tech-stack:
  added: []
  patterns:
    - Main summarizer helper functions for reusable paired-statistics and certificate aggregation
    - Aggregate-directory fallback so existing combined Stage 11 result bundles can be re-summarized without seed directories

key-files:
  created:
    - TRC-23-02333/test_summarize_trace_sl_rcss.py
  modified:
    - TRC-23-02333/summarize_trace_sl_rcss.py

key-decisions:
  - "Kept TRC-23-02333/summarize_trace_sl_rcss.py as the main aggregation point for EXP-04 and EXP-05 rather than adding notebooks or a parallel summary script."
  - "Certificate language now explicitly says empirical certificate-error correlation support, not formal optimality certification."

patterns-established:
  - "paired_delta_stats(delta): compute matched-split mean/std/SEM/95% t interval/Cohen dz/tests with pd.NA for insufficient pairs."
  - "collect_input_frames(input_roots): summarize either seed_* artifacts or existing combined aggregate directories."

requirements-completed: [EXP-04, EXP-05]

duration: 12min
completed: 2026-05-22
---

# Phase 04 Plan 02: Statistical Evidence Summarizer Summary

**TRACE-SL summarizer now regenerates paper-visible paired comparison intervals/effect sizes and empirical certificate-error summaries from existing Stage artifacts.**

## Performance

- **Duration:** 12 min
- **Started:** 2026-05-22T16:10:01Z
- **Completed:** 2026-05-22T16:16:08Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments

- Added matched-split paired delta helpers that compute `delta_mean`, `delta_std`, `delta_sem`, `ci95_low`, `ci95_high`, `cohens_dz`, `paired_t_p`, `wilcoxon_p`, `win_count`, and `count` for held-out GLS/MAP layout comparisons.
- Preserved existing paper-visible layout labels, including `validation_swap_selected`, `rcss_selected`, `multistart_swap_by_validation`, `observability_proxy`, `graph_sampling_laplacian`, and `qr_pod_modes` where present in aggregate inputs.
- Added empirical certificate-error summary helpers with Pearson/Spearman mean/std/min/max/count fields and generated Markdown wording that avoids formal certification overclaims.
- Added lightweight unittest coverage for the new summarizer helpers without adding dependencies to `requirements.txt`.

## Task Commits

Each task was committed atomically with TDD RED/GREEN commits:

1. **Task 1 RED: Add interval/effect-size tests** - `bc75d7e` (`test`)
2. **Task 1 GREEN: Implement paired comparison interval statistics** - `f905a94` (`feat`)
3. **Task 2 RED: Add certificate summary tests** - `4bdcd2c` (`test`)
4. **Task 2 GREEN: Implement empirical certificate summary counts** - `1763c28` (`feat`)

**Plan metadata:** committed separately after this summary.

## Files Created/Modified

- `TRC-23-02333/summarize_trace_sl_rcss.py` - Adds reusable paired-delta statistics, aggregate-directory input fallback, certificate count aggregation, and empirical summary wording.
- `TRC-23-02333/test_summarize_trace_sl_rcss.py` - Adds unittest coverage for paired statistics, insufficient matched pairs, missing layouts, certificate counts, and empirical wording.

## Decisions Made

- Kept the existing summarizer as the sole aggregation entry point for D-10/EXP-04/EXP-05 to avoid notebook or ad hoc calculation drift.
- Used a 95% Student t interval for matched deltas when at least two matched pairs exist; interval/effect/test fields remain `pd.NA` for insufficient pairs.
- Treated existing `combined_metrics.csv`, `combined_certificate_correlations.csv`, and `combined_rcss_candidates.csv` as valid summarizer inputs when seed directories are absent, enabling re-aggregation of curated Stage 11 bundles.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Added aggregate-directory input fallback**
- **Found during:** Task 1 (Add interval and effect-size fields to paired comparisons)
- **Issue:** The planned verification command targeted the curated `pems7_228_stage11_auto_weight_10split` directory, which contains aggregate CSVs but no `seed_*/metrics.csv` directories; the original summarizer therefore exited with `No seed metrics found`.
- **Fix:** Added `collect_input_frames(input_roots)` so the main summarizer can read either per-seed artifacts or existing combined aggregate CSVs.
- **Files modified:** `TRC-23-02333/summarize_trace_sl_rcss.py`
- **Verification:** Both `/tmp/trace_sl_phase4_stats_check` and `/tmp/trace_sl_phase4_cert_check` commands completed and emitted required schemas.
- **Committed in:** `f905a94`

---

**Total deviations:** 1 auto-fixed (1 blocking)
**Impact on plan:** The fix is required by D-10 and the plan’s own verification target; it broadens input compatibility without changing evaluator outputs or raw data.

## Issues Encountered

- `TRC-23-02333/test_summarize_trace_sl_rcss.py` is ignored by the repository’s TRC cleanup rule, so the RED test file was staged with explicit `git add -f` for the planned TDD artifact. No raw datasets were touched.
- GSD SDK state helper commands reported missing legacy fields in `STATE.md`; roadmap and requirement handlers were invoked, and `STATE.md` was updated manually for this plan’s next action/decision/session metadata.

## Verification

- `python /home/samuel/projects/sensor_opt/TRC-23-02333/test_summarize_trace_sl_rcss.py`
- `python -m py_compile /home/samuel/projects/sensor_opt/TRC-23-02333/summarize_trace_sl_rcss.py`
- `python /home/samuel/projects/sensor_opt/TRC-23-02333/summarize_trace_sl_rcss.py --input-root /home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split --output-dir /tmp/trace_sl_phase4_stats_check`
- Schema check confirmed `gls_map_paired_delta_tests.csv` contains `delta_mean`, `delta_std`, `delta_sem`, `ci95_low`, `ci95_high`, `cohens_dz`, `paired_t_p`, `wilcoxon_p`, `win_count`, and `count`.
- `python /home/samuel/projects/sensor_opt/TRC-23-02333/summarize_trace_sl_rcss.py --input-root /home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split --output-dir /tmp/trace_sl_phase4_cert_check`
- Schema/text check confirmed `certificate_correlation_summary.csv` has count columns, `SUMMARY.md` contains empirical certificate wording, and selected-source output includes `budget`, `source`, and `selected_count`.

## Known Stubs

None.

## Threat Flags

None.

## TDD Gate Compliance

- RED commits present: `bc75d7e`, `4bdcd2c`
- GREEN commits present after RED: `f905a94`, `1763c28`
- Refactor commits: none needed

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 04 Plan 03 can consume the richer summarizer outputs for downstream evidence curation. Existing Stage 11 aggregate directories can now be re-aggregated directly through the main summarizer without raw dataset reads or new package installs.

## Self-Check: PASSED

- Found summary file: `/home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/04-02-SUMMARY.md`
- Found modified summarizer: `/home/samuel/projects/sensor_opt/TRC-23-02333/summarize_trace_sl_rcss.py`
- Found test file: `/home/samuel/projects/sensor_opt/TRC-23-02333/test_summarize_trace_sl_rcss.py`
- Found task commits: `bc75d7e`, `f905a94`, `4bdcd2c`, `1763c28`
- Automated verification passed for paired-statistics and certificate-summary checks.

---
*Phase: 04-core-experiment-evidence*
*Completed: 2026-05-22*
