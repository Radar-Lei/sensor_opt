---
status: partial
phase: 08-external-stage12-evidence
source:
  - 08-01-SUMMARY.md
  - 08-02-SUMMARY.md
  - 08-03-SUMMARY.md
  - 08-04-SUMMARY.md
  - 08-05-SUMMARY.md
started: 2026-05-25T07:18:49Z
updated: 2026-05-25T07:18:49Z
---

## Current Test

[testing paused — Stage12 runtime blocker requires performance unblock before evidence UAT can continue]

## Tests

### 1. External Stage12 Launcher Dry-Run Surface
expected: Running the PeMS7_1026 and Seattle Stage12 launchers in DRY_RUN mode shows ten evaluator commands plus one summarizer command for each dataset, using Stage12 baseline-portfolio defaults and reviewer-facing baseline flags.
result: skipped
reason: Superseded by user decision: DRY_RUN surface is not important until real Stage12 runtime is unblocked.

### 2. Fail-Closed External Evidence Generator
expected: Running the external evidence contract generator/tests produces paper-source contract rows for PeMS7_1026 and Seattle and marks incomplete, untracked, Stage11, or missing ten-split evidence as not complete rather than claimable.
result: skipped
reason: Superseded by user decision: gate behavior is already fail-closed; the blocking issue is runtime feasibility of full Stage12 evidence.

### 3. PeMS7_1026 Blocker Status
expected: The PeMS7_1026 Stage12 evidence state is visibly incomplete: no required top-level aggregate artifacts are claimed, EVID-03 remains unchecked/incomplete, and raw dataset files remain unstaged/uncommitted.
result: blocked
blocked_by: runtime-performance
reason: "User reported: actual Stage12 did not finish; 1026-node/Seattle runs take too long because validation repeatedly solves dense systems and computes certificates. Do not keep waiting or treat downscaled diagnostics as evidence."

### 4. Seattle Blocker Artifact
expected: The Seattle Stage12 status artifact reports dataset Seattle, requirement EVID-04, required_split_count 10, actual_split_count 0, status blocked, seattle_core_claim_blocked true, and v1_1_completion_allowed false without fabricated aggregate evidence.
result: blocked
blocked_by: runtime-performance
reason: "User reported: actual Seattle Stage12 did not finish; performance fixes are required before complete evidence UAT can resume."

### 5. External Evidence Gate Artifacts
expected: The generated paper-source external evidence contract/gate files exist and show two dataset rows with pems7_1026_stage12_complete=false, seattle_stage12_complete=false, seattle_core_claim_blocked=true, and v1_1_completion_allowed=false.
result: skipped
reason: User indicated other Phase 8 gate checks are less important than the runtime unblock; existing gate should remain fail-closed.

### 6. Planning Metadata Gate Sync
expected: ROADMAP, STATE, and REQUIREMENTS reflect the same gate truth: Phase 8 remains blocked by incomplete PeMS7_1026/Seattle Stage12 evidence, EVID-03 and EVID-04 remain unchecked/incomplete, EVID-05 remains pending, and v1.1 completion is not allowed.
result: skipped
reason: User decision: do not advance Phase 9 or alter paper claims; create a Phase 8.5 performance unblock before continuing evidence work.

## Summary

total: 6
passed: 0
issues: 0
pending: 0
skipped: 4
blocked: 2

## Gaps

- truth: "PeMS7_1026 and Seattle Stage12 can produce at least one Stage12-compatible full seed before ten-split evidence rerun."
  status: failed
  reason: "User reported: actual Stage12 did not finish; current implementation likely repeats dense 1026x1026 solves and certificate computations across validation timesteps/candidates."
  severity: blocker
  test: 3
  root_cause: "validation_mae routes through full evaluate_layout and passes a dense T×N observation_weights matrix, forcing solve_quadratic and certificate paths into repeated per-timestep dense solves/inversions during candidate validation and swap search."
  artifacts:
    - path: "TRC-23-02333/transparent_estimator_eval.py"
      issue: "validation path performs full multi-method evaluation and certificate work instead of computing only the selection method MAE."
    - path: "scripts/run_stage12_pems7_1026.sh"
      issue: "Stage12 defaults expose full ten-split, multi-budget RCSS workload whose current validation path is not runtime-feasible on PeMS7_1026 scale."
    - path: "scripts/run_stage12_seattle.sh"
      issue: "Seattle Stage12 evidence is blocked by the same runtime feasibility issue."
  missing:
    - "Add fast validation path that computes only args.selection_method without certificates."
    - "Add solve_quadratic constant-weight fast path with Cholesky solve for scalar/vector-equivalent observation weights."
    - "Cache posterior/scenario trace metrics with Woodbury-style updates where possible."
    - "Add progress logging/checkpoints for budgets, candidate batches, and swap iterations."
    - "Only consider swap top-K validation if safe fixes are insufficient, and validate on PeMS7_228 before formal Stage12 use."
  debug_session: "user-provided runtime diagnosis on 2026-05-25"
