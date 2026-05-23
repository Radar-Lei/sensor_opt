---
phase: 05-robustness-and-generality
plan: 02
subsystem: research-artifacts
tags: [trace-sl, robustness, summarizer, pandas, candidate-sensitivity]

requires:
  - phase: 05-robustness-and-generality
    provides: Phase 5 evaluator condition columns and robustness artifact metadata from Plan 05-01
provides:
  - Condition-aware TRACE-SL aggregation across robustness, candidate-count, and split columns
  - Regression tests for robustness-condition separation and old Stage 12/13 schema compatibility
  - Markdown wording that frames robustness tables as stress-test evidence rather than universal proof
affects: [phase-05, robustness-evidence, candidate-sensitivity, paper-claims]

tech-stack:
  added: []
  patterns:
    - Centralized optional evidence grouping through condition_group_columns(frame)
    - Direct unittest-style temporary artifact tests for summarizer CSV/Markdown outputs

key-files:
  created:
    - .planning/phases/05-robustness-and-generality/05-02-SUMMARY.md
  modified:
    - TRC-23-02333/summarize_trace_sl_rcss.py
    - TRC-23-02333/test_summarize_trace_sl_rcss.py

key-decisions:
  - "Use one stable condition_group_columns(frame) helper for budget plus present Phase 5 condition columns before aggregation."
  - "Keep Phase 4 filenames and method/layout labels unchanged while adding condition grouping columns."

patterns-established:
  - "Condition-aware aggregation: all summarizer tables derive evidence grouping keys from present optional condition columns."
  - "Robustness wording: generated SUMMARY.md treats condition tables as stress-test evidence, not universal robustness proof."

requirements-completed: [ROBUST-01, ROBUST-02, ROBUST-03, ROBUST-04, ROBUST-05, ROBUST-06]

duration: 5min
completed: 2026-05-23
---

# Phase 05 Plan 02: Condition-Aware TRACE-SL Summarizer Summary

**TRACE-SL summaries now preserve robustness, candidate-count, and split condition columns before computing aggregate evidence.**

## Performance

- **Duration:** 5 min
- **Started:** 2026-05-23T02:35:11Z
- **Completed:** 2026-05-23T02:40:01Z
- **Tasks:** 2
- **Files modified:** 3

## Accomplishments

- Added `condition_group_columns(frame)` with stable optional order: `candidate_count`, `robustness_family`, `robustness_condition`, `failure_rate`, `noise_scale`, `missing_rate`, `missing_block_steps`, `cost_proxy`, `cost_budget`, and `split_mode` after `budget`.
- Applied condition-aware grouping to GLS/MAP layout summaries, delta summaries, paired tests, ablation summaries, per-split winners, win counts, selected-source summaries, candidate diagnostics, runtime summaries, and generated Markdown.
- Added direct Python regression tests proving same-budget robustness conditions remain separate, candidate/split columns survive where present, and old Stage 12/13 schemas without optional condition columns remain runnable.

## Task Commits

1. **Task 1: Add condition-aware grouping helpers and tests** - `6575bbb` (test)
2. **Task 2: Apply condition grouping to summaries, deltas, winners, candidates, and Markdown** - `ed14f97` (feat)

**Plan metadata:** pending final docs commit

## Files Created/Modified

- `TRC-23-02333/summarize_trace_sl_rcss.py` - Centralized condition grouping and applied it across aggregate CSV/Markdown outputs.
- `TRC-23-02333/test_summarize_trace_sl_rcss.py` - Added regression tests for condition grouping, temporary summarizer outputs, candidate summaries, runtime summaries, and old schema compatibility.
- `.planning/phases/05-robustness-and-generality/05-02-SUMMARY.md` - Execution record for Plan 05-02.

## Verification

- `python -m py_compile TRC-23-02333/summarize_trace_sl_rcss.py TRC-23-02333/test_summarize_trace_sl_rcss.py` — passed.
- `python TRC-23-02333/test_summarize_trace_sl_rcss.py` — passed, 13 tests.
- `python TRC-23-02333/summarize_trace_sl_rcss.py --input-root TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/candidates_50 TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/candidates_100 --runtime-root TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity --output-dir /tmp/trace_sl_phase5_summary_check` — passed.
- Python assertions confirmed `/tmp/trace_sl_phase5_summary_check/gls_map_layout_summary.csv` and `/tmp/trace_sl_phase5_summary_check/runtime_candidate_sensitivity.csv` include `candidate_count` and preserve values `{50, 100}`.

## Decisions Made

- Used a single helper rather than separate ad hoc grouping lists so Phase 5 condition columns cannot diverge across outputs.
- Preserved all Phase 4 output filenames and stable method/layout labels; only grouping keys and Markdown interpretation text changed.

## Deviations from Plan

None - plan executed as written.

## Known Stubs

None. The only stub-pattern match is the existing CLI `default=[]` for `--runtime-root`; it is a normal argparse default and does not feed UI rendering or evidence values.

## Threat Flags

None. Changes only aggregate generated result artifacts and do not introduce new endpoints, auth paths, file-access trust boundaries, schema migrations, or raw dataset access.

## Issues Encountered

- Initial RED tests failed because the helper did not exist, as expected for TDD.
- During GREEN work, runtime grouping initially assumed `budget` existed in runtime-only timing artifacts; fixed by grouping only by present condition columns for runtime summaries while still requiring `candidate_count`.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Plan 05-03 can generate or curate Phase 5 robustness artifacts knowing the summarizer will not collapse different stress conditions into one mean. The generated Markdown explicitly frames robustness tables as stress-test evidence, not universal robustness proof.

## Self-Check: PASSED

Verified created/modified files exist and task commits `6575bbb` and `ed14f97` are present in git history.

---
*Phase: 05-robustness-and-generality*
*Completed: 2026-05-23*
