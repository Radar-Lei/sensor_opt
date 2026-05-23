---
phase: 05-robustness-and-generality
plan: 01
subsystem: evaluator-robustness-hooks
tags: [robustness, evaluator, held-out-evidence, trace-sl]
dependency_graph:
  requires: [04-core-experiment-evidence]
  provides: [ROBUST-01, ROBUST-02, ROBUST-03, ROBUST-04, ROBUST-05]
  affects: [TRC-23-02333/transparent_estimator_eval.py, TRC-23-02333/test_transparent_estimator_eval.py]
tech_stack:
  added: [direct-python-test-script]
  patterns: [synthetic-array-tests, deterministic-perturbation-helpers, artifact-schema-metadata]
key_files:
  created: [TRC-23-02333/test_transparent_estimator_eval.py]
  modified: [TRC-23-02333/transparent_estimator_eval.py, .gitignore]
decisions:
  - "Robustness perturbations are applied at the held-out evaluate_layout boundary, while validation_mae explicitly uses apply_robustness=False."
  - "Heterogeneous sensor costs are represented by a deterministic graph/traffic proxy and optional cost_aware_coverage_proxy layout metadata."
metrics:
  duration: "~20min"
  completed: "2026-05-23T02:30:19Z"
  tasks: 3
  files: 3
---

# Phase 05 Plan 01: Evaluator Robustness Hooks Summary

## One-liner

Evaluator-level deterministic robustness hooks now support held-out sensor failures, observation noise, missing observations/time blocks, heterogeneous cost-proxy metadata, and chronological splits without leaking stress settings into validation selection.

## Completed Tasks

| Task | Name | Commit | Files |
|---|---|---|---|
| 1 RED | Add failing helper tests | b49428a | `.gitignore`, `TRC-23-02333/test_transparent_estimator_eval.py` |
| 1 GREEN | Add deterministic perturbation and split helpers | cb2a91a | `TRC-23-02333/transparent_estimator_eval.py` |
| 2 RED | Add failing robustness wiring tests | ffa9727 | `TRC-23-02333/test_transparent_estimator_eval.py` |
| 2 GREEN | Wire perturbations through held-out evaluation | 6165549 | `TRC-23-02333/transparent_estimator_eval.py` |
| 3 RED | Add failing artifact metadata tests | c56da5d | `TRC-23-02333/test_transparent_estimator_eval.py` |
| 3 GREEN | Emit robustness, cost, and split metadata | 85f093e | `TRC-23-02333/transparent_estimator_eval.py` |

## What Changed

- Added `split_mode` support for random and chronological daily splits, threaded through PeMS and Seattle loaders and exposed via `--split-mode`.
- Added deterministic helper functions for sensor failure, observation noise, random missingness, contiguous missing blocks, cost proxy derivation, and cost-aware coverage proxy layout selection.
- Extended `solve_quadratic` to support scalar observation weights and per-row/per-node observation weight matrices so missing observed readings can be represented as zero observation weight.
- Extended `evaluate_layout(..., apply_robustness=True)` to apply held-out perturbations at the shared evaluator boundary for `neighbor_average`, `gsp`, and `gls_map`; `validation_mae` uses `apply_robustness=False` by default.
- Added CLI flags and artifact fields for robustness condition provenance: `robustness_family`, `robustness_condition`, `failure_rate`, `noise_scale`, `missing_rate`, `missing_block_steps`, `cost_proxy`, `cost_budget`, `layout_sensor_cost`, `cost_feasible`, `split_mode`, `selected_sensor_count`, `active_sensor_count`, and `dropped_sensor_count`.

## Verification

Passed:

```bash
python -m py_compile /home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py /home/samuel/projects/sensor_opt/TRC-23-02333/test_transparent_estimator_eval.py
python /home/samuel/projects/sensor_opt/TRC-23-02333/test_transparent_estimator_eval.py
python /home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py --data-root /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228 --output-dir /tmp/trace_sl_phase5_eval_smoke --budgets "0.10" --num-layouts 1 --max-test-steps 1 --include-simple-baselines --robustness-family sensor_failure --robustness-condition failure_0.10 --failure-rate 0.10 --robustness-seed 505 --split-mode chronological
```

Artifact schema check confirmed required robustness columns and held-out `gls_map` rows under `robustness_family=sensor_failure` in `/tmp/trace_sl_phase5_eval_smoke/metrics.csv`.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing critical functionality] Allowed planned evaluator test script through existing TRC ignore rule**
- **Found during:** Task 1 RED commit
- **Issue:** `.gitignore` ignored all `TRC-23-02333/*` except a small allowlist, which blocked committing the required direct test script.
- **Fix:** Added `!TRC-23-02333/test_transparent_estimator_eval.py` to the allowlist.
- **Files modified:** `.gitignore`
- **Commit:** b49428a

## Known Stubs

None.

## Threat Flags

None beyond the plan threat model; CLI input validation was added for fractions, nonnegative scales, nonnegative missing block steps, and nonnegative cost budgets.

## TDD Gate Compliance

- RED commits present: b49428a, ffa9727, c56da5d
- GREEN commits present after RED gates: cb2a91a, 6165549, 85f093e

## Self-Check: PASSED

- Found created file: `/home/samuel/projects/sensor_opt/TRC-23-02333/test_transparent_estimator_eval.py`
- Found modified file: `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py`
- Found commits: b49428a, cb2a91a, ffa9727, 6165549, c56da5d, 85f093e
