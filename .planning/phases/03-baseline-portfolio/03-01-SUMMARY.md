---
phase: 03-baseline-portfolio
plan: 01
subsystem: research-baselines
tags: [trace-sl, baselines, gls-map, graph-sampling, qr-pod, stage12]

requires:
  - phase: 01-claim-evidence-contract
    provides: claim/evidence boundaries, multistart caveat policy, transparent-method positioning
  - phase: 02-formulation-and-theory-bridge
    provides: TRACE-SL formulation, validation/test separation, posterior diagnostics wording
provides:
  - Phase 3 evaluator flags and layout rows for observability proxy, graph sampling, QR/POD, A/D-optimal, and multistart baselines
  - Stage 12 PeMS7_228 baseline portfolio launcher
  - Machine-auditable BASE-01..BASE-06 inventory and no-raw-data wiring checker
affects: [phase-04-core-experiment-evidence, phase-07-transportation-science-manuscript]

tech-stack:
  added: []
  patterns: [monolithic-evaluator-layout-rows, no-raw-data-static-check, stage-launcher-thread-caps]

key-files:
  created:
    - scripts/run_stage12_pems7_228.sh
    - .planning/phases/03-baseline-portfolio/03-BASELINE-INVENTORY.md
    - .planning/phases/03-baseline-portfolio/check_phase3_baseline_wiring.py
  modified:
    - TRC-23-02333/transparent_estimator_eval.py
    - TRC-23-02333/summarize_trace_sl_rcss.py

key-decisions:
  - "Implemented graph_sampling_laplacian as a real Laplacian-mode layout row rather than documenting BASE-03 as represented only by existing GSP reconstruction evidence."
  - "Deferred BASE-05 learning-style reconstruction with a concrete protocol/evidence action because adding a black-box learner in Phase 3 would violate transparent-method positioning."
  - "Kept Stage 12 as wiring/static validation only; no PeMS/Seattle raw dataset smoke run was performed in Phase 3."

patterns-established:
  - "Phase 3 baselines enter the existing layouts tuple stream and are evaluated by evaluate_layout(test, ...) rather than fake summary rows."
  - "Baseline portfolio evidence is separated from Phase 4 full split regeneration and statistical audit."

requirements-completed: [BASE-01, BASE-02, BASE-03, BASE-04, BASE-05, BASE-06]

duration: 20min
completed: 2026-05-22
---

# Phase 3 Plan 01: Baseline Portfolio Summary

**Reviewer-facing TRACE-SL baseline portfolio wired through the existing evaluator with Stage 12 launcher, aggregate-summary awareness, and BASE-01..BASE-06 inventory.**

## Performance

- **Duration:** 20 min
- **Started:** 2026-05-22T14:46:56Z
- **Completed:** 2026-05-22T15:06:56Z
- **Tasks:** 3
- **Files modified:** 6

## Accomplishments

- Added Phase 3 evaluator flags and real layout rows for `observability_proxy`, `graph_sampling_laplacian`, and `qr_pod_modes`, while exposing existing `greedy_a_trace`, `greedy_d_logdet`, and `multistart_swap_by_validation` as portfolio members.
- Added `scripts/run_stage12_pems7_228.sh` with override-friendly defaults, BLAS thread caps, Phase 3 flags, and aggregation via the existing summarizer.
- Updated the summarizer so Phase 3 layout names are visible in GLS/MAP baseline deltas and ablation summaries when Stage 12 artifacts are generated.
- Created a BASE-01..BASE-06 inventory and static checker proving flags, layout names, launcher wiring, summarizer hooks, and no-raw-data verification behavior.

## Task Commits

Each task was committed atomically:

1. **Task 1: Add baseline portfolio layout rows to the existing evaluator** - `740cf72` (feat)
2. **Task 2: Wire the baseline portfolio into reproducible Stage 12 artifacts and summaries** - `ddf7260` (feat)
3. **Task 3: Create baseline inventory and run schema-focused smoke verification** - `55b579e` (docs)

## Files Created/Modified

- `TRC-23-02333/transparent_estimator_eval.py` - Adds Phase 3 portfolio CLI flags and layout helpers/rows routed through held-out reconstruction evaluation.
- `TRC-23-02333/summarize_trace_sl_rcss.py` - Adds Phase 3 baseline names to GLS/MAP delta and ablation comparison lists.
- `scripts/run_stage12_pems7_228.sh` - Defines the reusable PeMS7_228 baseline portfolio launcher.
- `.planning/phases/03-baseline-portfolio/03-BASELINE-INVENTORY.md` - Maps BASE-01..BASE-06 to reviewer objections, hooks, layout artifacts, evidence status, and Phase 4 actions.
- `.planning/phases/03-baseline-portfolio/check_phase3_baseline_wiring.py` - Static no-raw-data verification for evaluator, summarizer, launcher, and inventory wiring.
- `.planning/phases/03-baseline-portfolio/03-01-SUMMARY.md` - This execution summary.

## Decisions Made

- Implemented `graph_sampling_laplacian` as a real Laplacian-mode layout row, so BASE-03 is not only a prose tie to existing GSP reconstruction.
- Deferred BASE-05 learned reconstruction because Phase 3 lacks a predeclared leakage-safe training protocol and the project positioning prioritizes transparent reconstruction-aware placement.
- Preserved Stage 11 defaults by making all Phase 3 rows opt-in through explicit flags or `--include-baseline-portfolio`.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Fixed static checker ordering assertion for existing validation helper**
- **Found during:** Task 3 (schema-focused smoke verification)
- **Issue:** The checker searched for the first `evaluate_layout(test` occurrence, which appears in the pre-existing `validation_mae` helper before layout-row generation, causing a false negative.
- **Fix:** Changed the checker to compare Phase 3 row definitions against the final evaluation-loop occurrence using `rfind`.
- **Files modified:** `.planning/phases/03-baseline-portfolio/check_phase3_baseline_wiring.py`
- **Verification:** `python .planning/phases/03-baseline-portfolio/check_phase3_baseline_wiring.py`
- **Committed in:** `55b579e`

---

**Total deviations:** 1 auto-fixed (1 bug)
**Impact on plan:** Verification became stricter and accurate without changing implementation scope.

## Issues Encountered

- No raw-data smoke runs were performed by design; Phase 3 verification used compile, help, shell syntax, inventory grep, and static no-raw-data checks.

## Verification

Passed:

1. `python -m py_compile TRC-23-02333/transparent_estimator_eval.py TRC-23-02333/summarize_trace_sl_rcss.py`
2. `bash -n scripts/run_stage12_pems7_228.sh`
3. `python TRC-23-02333/transparent_estimator_eval.py --help | grep -E -- '--include-baseline-portfolio|--include-observability-proxy|--include-graph-sampling-baseline|--include-qr-pod-baseline'`
4. `grep -E 'BASE-01|BASE-02|BASE-03|BASE-04|BASE-05|BASE-06' .planning/phases/03-baseline-portfolio/03-BASELINE-INVENTORY.md`
5. `python .planning/phases/03-baseline-portfolio/check_phase3_baseline_wiring.py`

## Known Stubs

None found in created/modified Phase 3 files. BASE-05 is an explicit documented deferral with Phase 4/Phase 7 action, not a stub metric row.

## Threat Flags

None. Phase 3 added CLI flags and a launcher path, both already covered by the plan threat model; no new network endpoint, auth path, file trust boundary, or schema boundary was introduced.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Phase 4 can run Stage 12 or a successor full-evidence launcher to generate held-out split artifacts for the new baseline rows, then audit paired deltas/statistical evidence before manuscript claims. Raw datasets remain local and ignored; Stage 12 reads them only when Phase 4 explicitly performs data runs.

## Self-Check: PASSED

- Found all created files: Stage 12 launcher, baseline inventory, static checker, and this summary.
- Found all task commits: `740cf72`, `ddf7260`, `55b579e`.
- Verification commands passed without opening raw dataset paths.

---
*Phase: 03-baseline-portfolio*
*Completed: 2026-05-22*
