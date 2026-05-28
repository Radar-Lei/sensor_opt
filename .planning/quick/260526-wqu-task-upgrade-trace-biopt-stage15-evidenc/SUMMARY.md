# Quick Summary: TRACE-BiOpt Stage15 Evidence Configuration

## Completed

- Diagnosed the original `stage15_biopt_allbudget_seed25` run:
  PeMS7_1026 and PeMS7_228 passed all budgets, while Seattle failed at 20
  percent and 30 percent against `validation_swap_selected`.
- Tested Seattle follow-ups and found the same certificate-regularized
  objective with a larger deterministic search budget recovered both failed
  rows.
- Updated `scripts/run_stage15_biopt_weak_points.sh` to support
  dataset-prefixed `TRACE_BIOPT_*` overrides. Default PeMS settings remain the
  smaller search budget; default Seattle settings use the stronger search
  budget.
- Re-ran seed-25 all-budget evidence as
  `stage15_biopt_allbudget_seed25_v2`; TRACE-BiOpt beats the best non-BiOpt
  baseline on all nine dataset-budget rows.

## Verification

- `DRY_RUN=1 SEEDS=25 BUDGETS="0.10 0.20 0.30" scripts/run_stage15_biopt_weak_points.sh`
- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py TRC-23-02333/trace_biopt.py TRC-23-02333/summarize_trace_sl_rcss.py scripts/generate_trace_biopt_dominance.py`
- `pytest -q TRC-23-02333/test_transparent_estimator_eval.py TRC-23-02333/test_summarize_trace_sl_rcss.py scripts/test_generate_trace_biopt_dominance.py tests/test_stage12_runtime_fast_paths.py tests/test_stage12_runtime_trace_cache.py`
- `OUTPUT_ROOT=TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_seed25_v2 SEEDS=25 BUDGETS="0.10 0.20 0.30" scripts/run_stage15_biopt_weak_points.sh`

## Remaining

- Multi-seed all-budget evidence and paired tests are still required before
  final TR-B dominance wording.

