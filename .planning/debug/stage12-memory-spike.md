---
status: resolved
trigger: "$gsd-debug 请帮我做内存修复"
created: 2026-05-25
updated: 2026-05-25
---

# Debug Session: Stage12 Memory Spike

## Symptoms

- Expected behavior: External Stage12 PeMS7_1026 and Seattle runs should execute with bounded memory when `MAX_JOBS=1`.
- Actual behavior: During PeMS7_1026 Stage12 formal evidence run, memory usage continued rising sharply even with a single evaluator process.
- Error messages: No Python exception; user observed large sustained memory growth and interrupted the run.
- Timeline: Reproduced while trying to close v1.1 EVID-03/EVID-04 blockers on 2026-05-25.
- Reproduction: Run `MAX_JOBS=1 THREADS_PER_JOB=1 bash scripts/run_stage12_pems7_1026.sh`; memory rises during seed 25 validation-swap at budget 0.10.

## Current Focus

- hypothesis: Stage12 repeatedly allocates large dense prediction and posterior arrays inside validation-swap and full layout evaluation, and retains unnecessary per-trial objects long enough to cause high peak memory.
- test: Inspect validation and evaluation paths, add streaming/low-allocation metric computation, and verify dry-run plus unit tests.
- expecting: Validation-swap no longer materializes full prediction matrices for hidden nodes on every trial; launcher defaults prevent concurrent seed amplification.
- next_action: Re-run formal Stage12 only with `MAX_JOBS=1` and an explicit `MAX_RSS_MB` guard after reviewing available memory.

## Evidence

- timestamp: 2026-05-25
  observation: PeMS7_1026 formal seed 25 reached budget 0.10 validation-swap start 3 iteration 6 with no metrics output before the run was stopped.
- timestamp: 2026-05-25
  observation: After killing Stage12, no `transparent_estimator_eval.py` process remained. Only progress/checkpoint partial artifacts existed.
- timestamp: 2026-05-25
  observation: External Stage12 launchers had default `MAX_JOBS=2`; this was changed to `MAX_JOBS=1` to avoid accidental process-level memory amplification.

## Eliminated

- hypothesis: OOM was solely caused by multi-seed parallelism.
  reason: Memory rose under explicit `MAX_JOBS=1`; process-level concurrency was a multiplier, not the root cause.

## Resolution

- root_cause: Full Stage12 PeMS7_1026 combines large dense covariance/precision work with repeated dense validation-swap evaluations. Two avoidable amplifiers were present: QR/POD used full SVD over a tall traffic matrix, and validation MAE constructed full-node prediction matrices even though only hidden-node MAE was needed. Launchers also defaulted to two concurrent seed processes.
- fix: Replaced QR/POD full SVD with covariance eigendecomposition over node covariance, changed cached GLS/GSP validation MAE to compute hidden-node predictions only, added process RSS progress reporting plus optional `--max-rss-mb` fail-fast guard, defaulted external Stage12 launchers to `MAX_JOBS=1`, and exposed `MAX_RSS_MB` through both launchers.
- verification: `python -m unittest tests.test_stage12_runtime_fast_paths tests.test_stage12_runtime_trace_cache -v` passed; `python TRC-23-02333/test_transparent_estimator_eval.py` passed; launcher dry-runs show `--max-rss-mb` propagation; a reduced PeMS7_1026 real smoke completed to `/tmp/stage12_memory_smoke_pems1026` with peak RSS about 1.37GB.
- files_changed: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/test_transparent_estimator_eval.py`, `tests/test_stage12_runtime_fast_paths.py`, `scripts/run_stage12_pems7_1026.sh`, `scripts/run_stage12_seattle.sh`, `.planning/debug/stage12-memory-spike.md`
