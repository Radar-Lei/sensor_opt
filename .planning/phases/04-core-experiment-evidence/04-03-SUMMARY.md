---
phase: 04-core-experiment-evidence
plan: 03
subsystem: experiment-evidence
tags: [trace-sl, pems7-228, stage12, baseline-portfolio, paired-statistics]

requires:
  - phase: 03-baseline-portfolio
    provides: Phase 3 reviewer-facing baseline flags and stable layout labels.
  - phase: 04-core-experiment-evidence/04-01
    provides: EXP-01 audit showing Stage 12 regeneration was required for portfolio rows.
  - phase: 04-core-experiment-evidence/04-02
    provides: Summarizer support for confidence intervals, effect sizes, paired tests, and certificate counts.
provides:
  - Complete PeMS7_228 Stage 12 ten-split baseline-portfolio evidence bundle for seeds 25..34.
  - Reproducible Stage 12 launcher with dry-run verification path and portfolio flags.
  - EXP-01/EXP-04 aggregate artifacts containing final TRACE-SL variants, Phase 3 baselines, paired intervals, effect sizes, and tests.
affects: [paper-results, trace-sl-results, reproducibility, phase-04, baseline-portfolio]

tech-stack:
  added: []
  patterns:
    - Bash launchers expose DRY_RUN and PYTHON_BIN overrides while preserving repo-relative reproducibility commands.
    - Stage result directories commit per-seed artifacts plus aggregate CSV/Markdown summaries under trace_sl_results.

key-files:
  created:
    - TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/SUMMARY.md
    - TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/combined_metrics.csv
    - TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_layout_summary.csv
    - TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_paired_delta_tests.csv
  modified:
    - scripts/run_stage12_pems7_228.sh

key-decisions:
  - "Stage 12 PeMS7_228 now uses seeds 25..34 as the primary ten-split evidence bundle instead of the earlier five-seed launcher default."
  - "Full Stage 12 regeneration was run because no complete seed_*/metrics.csv artifacts existed and local PeMS7_228 data was available."
  - "The 10% multistart caveat remains visible through explicit Stage 12 layout-summary and paired-comparison rows."

patterns-established:
  - "DRY_RUN=1 bash scripts/run_stage12_pems7_228.sh prints evaluator and summarizer commands without opening raw datasets."
  - "Stage 12 evidence verification requires all ten seed metrics plus aggregate files and required Phase 3 layout labels."

requirements-completed: [EXP-01, EXP-04]

duration: 25min
completed: 2026-05-22
---

# Phase 04 Plan 03: Stage 12 PeMS7_228 Evidence Summary

**PeMS7_228 Stage 12 now has a reproducible ten-split baseline-portfolio evidence bundle with Phase 3 layout rows and paired EXP-04 statistics.**

## Performance

- **Duration:** 25 min
- **Started:** 2026-05-22T16:19:28Z
- **Completed:** 2026-05-22T16:44:31Z
- **Tasks:** 2
- **Files modified:** 113

## Accomplishments

- Hardened `scripts/run_stage12_pems7_228.sh` so its defaults target seeds `25 26 27 28 29 30 31 32 33 34`, budgets `0.10 0.20 0.30`, the stable Stage 12 output directory, Phase 3 portfolio flags, and BLAS thread caps.
- Added a launcher `DRY_RUN=1` path that prints the per-seed evaluator and aggregate summarizer commands without reading local raw datasets.
- Ran full PeMS7_228 Stage 12 generation with local data and committed per-seed artifacts for all ten seeds plus aggregate CSV/Markdown outputs.
- Verified that Stage 12 aggregate evidence includes `validation_swap_selected`, `rcss_selected`, `multistart_swap_by_validation`, `greedy_a_trace`, `greedy_d_logdet`, `observability_proxy`, `graph_sampling_laplacian`, and `qr_pod_modes` with held-out GLS/MAP rows.
- Preserved the low-budget comparator caveat: at 10% budget Stage 12 shows `validation_swap_selected` mean 3.590056, `multistart_swap_by_validation` mean 3.594525, and `rcss_selected` mean 3.604982; paired `validation_swap_selected - multistart_swap_by_validation` has CI [-0.045768, 0.036830] and p=0.812100.

## Task Commits

Each task was committed atomically:

1. **Task 1: Harden Stage 12 launcher for ten-split primary evidence** - `1d4988d` (feat)
2. **Task 2: Generate or audit Stage 12 PeMS7_228 aggregate evidence** - `5b3a112` (feat)

**Plan metadata:** pending final metadata commit.

## Files Created/Modified

- `scripts/run_stage12_pems7_228.sh` - Defaults Stage 12 to ten seeds, keeps Phase 3 portfolio flags including `--include-greedy`, adds `DRY_RUN=1`, and preserves override-friendly variables.
- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/` - New Stage 12 evidence directory with ten `seed_*` result folders and aggregate outputs.
- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/SUMMARY.md` - Generated aggregate Stage 12 summary containing layout means, paired tests, ablation rows, certificate summary, and selected-source counts.
- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/combined_metrics.csv` - Combined per-seed held-out metrics for the Stage 12 baseline portfolio.
- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_layout_summary.csv` - Held-out GLS/MAP layout summary with required Phase 3 baseline rows.
- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_paired_delta_tests.csv` - Paired deltas, intervals, effect sizes, paired tests, win counts, and matched-pair counts for paper-visible comparisons.
- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio_seed_25.log` through `..._seed_34.log` - Per-seed run logs from the full Stage 12 launcher execution.

## Decisions Made

- Regenerated Stage 12 instead of writing a pending-only summary because all ten `seed_*/metrics.csv` files were initially absent and local PeMS7_228 data files were available.
- Kept `--include-greedy` explicitly in the launcher even though `--include-baseline-portfolio` also enables greedy internally, so source/audit checks can directly prove `greedy_a_trace` and `greedy_d_logdet` are enabled.
- Committed the complete Stage 12 per-seed artifacts and logs because the plan required actual EXP-01 evidence rather than a pending-regeneration artifact.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Re-ran Stage 12 from the repository root after the first absolute-path launch produced no artifacts**
- **Found during:** Task 2 (Generate or audit Stage 12 PeMS7_228 aggregate evidence)
- **Issue:** The initial launcher command used an absolute script path from the executor shell context; because the script uses repo-relative paths, it did not populate the repository Stage 12 directory.
- **Fix:** Re-ran the launcher from `/home/samuel/projects/sensor_opt`, which matches the launcher’s documented repo-relative assumptions.
- **Files modified:** Generated Stage 12 artifacts under `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/`.
- **Verification:** The complete Stage 12 assertion passed with all ten seed metrics, required aggregate files, required layout labels, held-out GLS/MAP rows, and no pending-only summary wording.
- **Committed in:** `5b3a112`

---

**Total deviations:** 1 auto-fixed (1 blocking)
**Impact on plan:** The fix was required to generate the planned evidence in the intended repository artifact tree; no raw datasets were committed.

## Issues Encountered

- The full Stage 12 command was long-running but completed successfully. A duplicate absolute-path run was stopped after the repository-root run was confirmed active; no committed artifact came from the duplicate path.
- Existing unrelated working-tree changes remained untouched, including deleted quick-planning files and idea-stage edits that predated this execution.

## Verification

- `bash -n /home/samuel/projects/sensor_opt/scripts/run_stage12_pems7_228.sh`
- Launcher token/source assertion confirmed ten seeds, Stage 12 output directory, `--include-baseline-portfolio`, `--include-greedy`, `--include-observability-proxy`, `--include-graph-sampling-baseline`, `--include-qr-pod-baseline`, summarizer invocation, and evaluator labels `greedy_a_trace`/`greedy_d_logdet`.
- `DRY_RUN=1 bash /home/samuel/projects/sensor_opt/scripts/run_stage12_pems7_228.sh` printed all ten per-seed evaluator commands plus summarizer command without raw data reads.
- `bash scripts/run_stage12_pems7_228.sh` from `/home/samuel/projects/sensor_opt` completed Stage 12 generation for seeds 25..34.
- Stage 12 complete-evidence assertion passed for all ten seed metrics, `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_paired_delta_tests.csv`, `SUMMARY.md`, required layout labels, held-out `gls_map` rows, greedy paired-comparison rows, and no pending-only summary wording.

## Known Stubs

None.

## Threat Flags

None. The plan’s trust-boundary mitigations were applied: launcher defaults were token-checked, partial evidence fails verification, and raw datasets remained local/ignored.

## User Setup Required

None - local PeMS7_228 data was already available and no external service configuration was required.

## Next Phase Readiness

Phase 04 Plan 04 can treat EXP-01 PeMS7_228 Stage 12 primary evidence as available. Later curation should cite `/home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/` for the complete Phase 3 baseline portfolio rows and preserve the explicit 10% multistart/validation-swap/RCSS comparison caveat.

## Self-Check: PASSED

- Found summary file: `/home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/04-03-SUMMARY.md`
- Found launcher: `/home/samuel/projects/sensor_opt/scripts/run_stage12_pems7_228.sh`
- Found Stage 12 aggregate summary: `/home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/SUMMARY.md`
- Found Stage 12 aggregate metrics: `/home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/combined_metrics.csv`
- Found Stage 12 paired tests: `/home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_paired_delta_tests.csv`
- Found task commits: `1d4988d`, `5b3a112`
- Automated verification passed for launcher syntax/tokens, dry-run output, complete seed coverage, required aggregate files, required labels, held-out GLS/MAP rows, and low-budget caveat visibility.

---
*Phase: 04-core-experiment-evidence*
*Completed: 2026-05-22*
