---
status: complete
completed: "2026-05-26"
quick_id: "260526-v7m"
slug: "implement-trace-biopt-as-a-single-bileve"
---

# Summary

Implemented a first TRACE-BiOpt code path as a single reconstruction-aware
layout method, not a candidate-pool selector.

Changed artifacts:

- Added `TRACE_BIOPT_SPEC.md` with the one-objective method boundary, solver
  semantics, and evidence gate.
- Added `--include-biopt` to `TRC-23-02333/transparent_estimator_eval.py`.
- Added `trace_biopt` layout output and `trace_biopt_history.json`.
- Added `TRC-23-02333/trace_biopt.py` convenience entry point.
- Added `scripts/run_stage15_biopt_weak_points.sh` for PeMS7_1026, Seattle,
  and PeMS7_228 at the weak 10 percent budget.
- Updated the summarizer so `trace_biopt` enters paired comparisons and
  combined multi-dataset summaries remain dataset-separated.
- Added focused tests for Huber loss, TRACE-BiOpt objective terms,
  deterministic solver behavior, and dataset grouping.

Verification:

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py TRC-23-02333/trace_biopt.py TRC-23-02333/summarize_trace_sl_rcss.py`
- `pytest -q TRC-23-02333/test_transparent_estimator_eval.py TRC-23-02333/test_summarize_trace_sl_rcss.py tests/test_stage12_runtime_fast_paths.py tests/test_stage12_runtime_trace_cache.py`
- `DRY_RUN=1 SEEDS=25 BUDGETS=0.10 NUM_LAYOUTS=2 RCSS_RANDOM_CANDIDATES=2 RCSS_QUALITY_CANDIDATES=1 scripts/run_stage15_biopt_weak_points.sh`
- Smoke run on PeMS7_228 with tiny budget/pools wrote `trace_biopt_history.json`
  and summarized successfully under `/tmp/sensor_opt_trace_biopt_smoke*`.

Remaining work:

- Run real Stage15 weak-point experiments.
- If TRACE-BiOpt does not beat the best baseline at weak points, tune the
  single objective/solver rather than adding baselines to the method.
- Add continuous relaxation, top-k rounding, and limited two-swap/beam only
  if they keep the same `J(S)` objective.
