---
status: complete
completed: "2026-05-26"
quick_id: "260526-vfc"
slug: "make-trace-biopt-stage15-weak-point-expe"
---

# Summary

Made TRACE-BiOpt Stage15 weak-point experiments fast, diagnosable, and stronger
without changing the method into a candidate-pool selector.

Changes:

- Added `trace_biopt_objective_steps` for deterministic validation time-step
  subsampling inside the TRACE-BiOpt search objective.
- Added per-step TRACE-BiOpt progress records for warm start, forward steps,
  exchange steps, and exchange stopping.
- Added `trace_biopt_initializer=auto`, which uses objective-forward
  construction for small/medium networks and posterior-certificate warm start
  for large networks, followed by the same `J(S)` exchange refinement.
- Updated the Stage15 weak-point launcher defaults to the validated auto
  initializer and `beta=2.0`.
- Added `scripts/generate_trace_biopt_dominance.py` and tests to produce
  `trace_biopt_best_baseline_delta.csv` / `TRACE_BIOPT_DOMINANCE.md`.

Evidence generated:

- Stage15 weak-point run completed for seed 25, 10% budget, 25 random layouts,
  on PeMS7_1026, Seattle, and PeMS7_228.
- `TRC-23-02333/trace_sl_results/stage15_biopt_weak_points/combined/TRACE_BIOPT_DOMINANCE.md`
  reports TRACE-BiOpt beating the best non-BiOpt baseline in all three rows:
  PeMS7_1026, PeMS7_228, and Seattle.

Verification:

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py TRC-23-02333/trace_biopt.py TRC-23-02333/summarize_trace_sl_rcss.py scripts/generate_trace_biopt_dominance.py`
- `pytest -q TRC-23-02333/test_transparent_estimator_eval.py TRC-23-02333/test_summarize_trace_sl_rcss.py scripts/test_generate_trace_biopt_dominance.py tests/test_stage12_runtime_fast_paths.py tests/test_stage12_runtime_trace_cache.py`
- `SEEDS=25 BUDGETS=0.10 scripts/run_stage15_biopt_weak_points.sh`

Remaining work:

- Promote the weak-point evidence to multi-seed Stage15 across all budgets.
- Generate paper-source claim contracts from Stage15 before making final TR-B
  dominance claims.
