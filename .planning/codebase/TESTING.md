# Testing Patterns

**Analysis Date:** 2026/05/21

## Test Framework

**Runner:**
- Not detected. There is no `pytest.ini`, `pyproject.toml`, `tox.ini`, `setup.cfg`, `conftest.py`, `test_*.py`, `*_test.py`, `*.test.*`, or `*.spec.*` file under the scanned repository.
- Current validation is script-based and artifact-based through `python -m py_compile`, sanity/experiment runs of `TRC-23-02333/transparent_estimator_eval.py`, and aggregation with `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Evidence: `.planning/quick/260518-trace-sl-cpu-pilot/SUMMARY.md` records `python -m py_compile TRC-23-02333/transparent_estimator_eval.py` plus sanity and full pilot runs; `.planning/quick/260518-trace-sl-cpu-pilot/SUMMARY_STAGE5_OR_GUIDED.md` records the same compile gate plus a Stage 5 OR sanity run.

**Assertion Library:**
- Not detected. No unit-test assertion library is configured.
- Statistical checks use Pandas/SciPy calculations and persisted CSV summaries rather than test assertions: `ttest_rel` and `wilcoxon` in `TRC-23-02333/summarize_trace_sl_rcss.py`; `pearsonr` and `spearmanr` in `TRC-23-02333/transparent_estimator_eval.py`.

**Run Commands:**
```bash
python -m py_compile TRC-23-02333/transparent_estimator_eval.py TRC-23-02333/summarize_trace_sl_rcss.py  # Syntax check current Python scripts
bash scripts/run_stage11_pems7_228.sh                                                                    # Full Stage 11 PeMS7_228 reproducibility run
bash scripts/run_stage11_pems7_1026.sh                                                                   # Full Stage 11 PeMS7_1026 external-validation run
bash scripts/run_stage11_seattle.sh                                                                      # Full Stage 11 Seattle validation run
python TRC-23-02333/summarize_trace_sl_rcss.py --input-root <seed-result-dir> --output-dir <aggregate-dir> # Aggregate seed-level metrics
```

## Test File Organization

**Location:**
- No dedicated test directory or co-located test files are present.
- Validation artifacts live under `TRC-23-02333/trace_sl_results/`, with curated Stage 6--11, PeMS7_1026, and Seattle outputs documented in `TRC-23-02333/trace_sl_results/README.md`.
- Reproducibility launchers live under `scripts/`: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Historical quick validation summaries live under `.planning/quick/260518-trace-sl-cpu-pilot/`.

**Naming:**
- Use `seed_<N>/` subdirectories for split-level outputs: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/seed_25/`.
- Use `SUMMARY.md` for human-readable validation summaries inside each result directory: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md`.
- Use stable artifact names for machine-readable checks: `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, and `config.json` written by `TRC-23-02333/transparent_estimator_eval.py`.
- Use `combined_*` and summary CSV names for aggregate outputs: `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `gls_map_win_counts.csv`, and `certificate_correlation_summary.csv` written by `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Structure:**
```text
TRC-23-02333/trace_sl_results/
├── pems7_228_stage11_auto_weight/
│   ├── seed_25/
│   │   ├── metrics.csv
│   │   ├── metrics.json
│   │   ├── layouts.json
│   │   ├── swap_history.json
│   │   ├── rcss_candidates.csv
│   │   ├── certificate_correlations.csv
│   │   ├── config.json
│   │   └── SUMMARY.md
│   ├── seed_26/
│   └── SUMMARY.md
├── pems7_228_stage11_auto_weight_10split/
│   ├── combined_metrics.csv
│   ├── gls_map_layout_summary.csv
│   ├── gls_map_delta_summary.csv
│   ├── gls_map_paired_delta_tests.csv
│   ├── gls_map_win_counts.csv
│   └── SUMMARY.md
├── pems7_1026_stage11_auto_weight/
└── seattle_stage11_auto_weight_light/
```

## Test Structure

**Suite Organization:**
```python
# Current script-based validation pattern in TRC-23-02333/transparent_estimator_eval.py

def main():
    parser = argparse.ArgumentParser(description="TRACE-SL transparent estimator CPU pilot")
    # parse deterministic seeds and hyperparameters
    train, val, test, test_index, distance, val_days, test_days = load_pems_dataset(args.data_root, args.split_seed)
    # build matrices, generate layouts, evaluate rows
    frame.to_csv(output_dir / "metrics.csv", index=False)
    (output_dir / "config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    write_summary(output_dir, args, rows, correlations, test_days)

if __name__ == "__main__":
    main()
```

**Patterns:**
- Setup pattern: shell scripts define dataset path, output directory, split seeds, budget sweep, candidate counts, validation-swap parameters, and BLAS thread limits before invoking the Python driver. See `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Execution pattern: loop over split seeds, invoke `TRC-23-02333/transparent_estimator_eval.py` with deterministic `--split-seed` and `--layout-seed`, and stream output through `tee` to a per-seed log in the result directory.
- Aggregation pattern: after seed runs finish, invoke `TRC-23-02333/summarize_trace_sl_rcss.py` with one or more `--input-root` directories and one `--output-dir` to create aggregate CSVs and `SUMMARY.md`.
- Verification pattern: inspect persisted `SUMMARY.md`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, paired tests, and certificate correlation summaries under `TRC-23-02333/trace_sl_results/...`.

## Mocking

**Framework:** Not detected

**Patterns:**
```python
# No mocking pattern exists. Current validation uses real or locally placed datasets.
# Dataset loader fallback pattern in TRC-23-02333/transparent_estimator_eval.py:
value_files = sorted(data_root.glob("PeMSD7_V_*.csv"))
distance_files = sorted(data_root.glob("PeMSD7_W_*.csv"))
if not value_files or not distance_files:
    return load_seattle_dataset(data_root, seed)
```

**What to Mock:**
- If unit tests are added, mock filesystem inputs for loader edge cases in `TRC-23-02333/transparent_estimator_eval.py` only when tiny synthetic CSV/NPY fixtures cannot express the case.
- For pure numerical helpers such as `parse_budgets`, `normalize_minmax`, `metrics`, `coverage_penalty`, `posterior_trace_for_layout`, and `parse_weight_grid` in `TRC-23-02333/transparent_estimator_eval.py`, use direct inputs rather than mocks.

**What NOT to Mock:**
- Do not mock NumPy, Pandas, SciPy, or scikit-learn numerical routines used by `TRC-23-02333/transparent_estimator_eval.py`; validate behavior through small deterministic arrays.
- Do not mock the seed-level result structure when testing `TRC-23-02333/summarize_trace_sl_rcss.py`; use temporary directories containing minimal `seed_*/metrics.csv`, `certificate_correlations.csv`, and `rcss_candidates.csv` fixtures.
- Do not mock full Stage 11 runs in reproducibility checks; use the real script entry points in `scripts/` when validating published artifacts.

## Fixtures and Factories

**Test Data:**
```python
# Recommended minimal fixture shape for future unit tests around layout/evaluator helpers.
# Keep arrays tiny, deterministic, and explicit.
distance = np.array([
    [0.0, 1.0, 2.0],
    [1.0, 0.0, 1.0],
    [2.0, 1.0, 0.0],
])
train = np.array([
    [10.0, 11.0, 12.0],
    [13.0, 14.0, 15.0],
])
sensors = np.array([0, 2], dtype=int)
```

**Location:**
- Existing real data location is local-only and documented in `README.md`: `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, and `TRC-23-02333/dataset/Seattle/`.
- Existing committed validation outputs are under `TRC-23-02333/trace_sl_results/`.
- If adding automated unit tests, place test fixtures under a new test directory such as `tests/fixtures/` and keep them tiny enough to commit; do not commit real PeMS or Seattle datasets.

## Coverage

**Requirements:** None enforced

**View Coverage:**
```bash
# Not configured. No coverage tool or threshold is present.
```

## Test Types

**Unit Tests:**
- Not present.
- Suitable future unit-test targets are pure helpers in `TRC-23-02333/transparent_estimator_eval.py`: `parse_budgets`, `adjacency_to_distance`, `metrics`, `normalize_minmax`, `coverage_layout`, `parse_weight_grid`, `rcss_candidate_scores`, and `summarize_correlations`.
- Use deterministic arrays and seeds for any unit tests that exercise layout selection helpers such as `quality_coverage_sample` and `swap_trace_local_search` in `TRC-23-02333/transparent_estimator_eval.py`.

**Integration Tests:**
- Current integration validation is performed by running experiment scripts and checking generated artifacts.
- The main integration driver is `TRC-23-02333/transparent_estimator_eval.py`, which loads a dataset, splits train/validation/test days, builds Laplacian and GLS precision matrices, generates random/baseline/RCSS layouts, evaluates reconstruction metrics, and writes seed-level artifacts.
- The aggregate integration driver is `TRC-23-02333/summarize_trace_sl_rcss.py`, which reads `seed_*/metrics.csv`, optional `certificate_correlations.csv`, optional `rcss_candidates.csv`, and writes combined summaries.
- Evidence of successful integration checks is recorded in `.planning/quick/260518-trace-sl-cpu-pilot/SUMMARY.md`, `.planning/quick/260518-trace-sl-cpu-pilot/SUMMARY_STAGE5_OR_GUIDED.md`, `RESEARCH_PIPELINE_REPORT.md`, and the curated result directories listed in `TRC-23-02333/trace_sl_results/README.md`.

**E2E Tests:**
- No separate E2E framework is used.
- The closest E2E checks are full Stage 11 script runs:
  - `scripts/run_stage11_pems7_228.sh` writes seed outputs and aggregates to `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/`.
  - `scripts/run_stage11_pems7_1026.sh` writes seed outputs and aggregates to `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`.
  - `scripts/run_stage11_seattle.sh` writes seed outputs and aggregates to `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`.

## Common Patterns

**Async Testing:**
```bash
# No async test runner is present. Parallelism is controlled by shell/process environment.
THREADS_PER_JOB=1 SEEDS="25 26 27 28 29" bash scripts/run_stage11_pems7_228.sh
```
- The scripts set `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS` from `THREADS_PER_JOB` to avoid BLAS oversubscription: see `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- The current scripts run seed jobs sequentially in a shell `for seed in ${SEEDS}; do ... done` loop.

**Error Testing:**
```python
# Existing code raises explicit exceptions for bad inputs in TRC-23-02333/transparent_estimator_eval.py.
if tensor.ndim != 3 or tensor.shape[2] != SLOTS_PER_DAY:
    raise ValueError(f"Expected Seattle tensor shape (nodes, days, {SLOTS_PER_DAY}), got {tensor.shape}")

if not rows:
    raise ValueError("RCSS requires at least one candidate layout")
```
- Future tests should assert `FileNotFoundError` for missing Seattle files in `load_seattle_dataset` in `TRC-23-02333/transparent_estimator_eval.py`.
- Future tests should assert `ValueError` for invalid RCSS weight-grid entries in `parse_weight_grid` in `TRC-23-02333/transparent_estimator_eval.py`.
- Future tests should assert `SystemExit` when `TRC-23-02333/summarize_trace_sl_rcss.py` receives an input root with no `seed_*/metrics.csv` files.

## Reproducibility Checks

- Confirm scripts compile before running expensive experiments:
```bash
python -m py_compile TRC-23-02333/transparent_estimator_eval.py TRC-23-02333/summarize_trace_sl_rcss.py
```
- Confirm required local datasets exist before full runs. `README.md` documents expected paths:
  - `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv`
  - `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`
  - `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv`
  - `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv`
  - Seattle loader expects `tensor.npz` and `Loop_Seattle_2015_A.npy` under `TRC-23-02333/dataset/Seattle/`.
- Confirm aggregate outputs contain the current primary method `validation_swap_selected` and baseline comparisons against `best_random_by_validation`, `random`, and `top_variance`, as directed by `TRC-23-02333/trace_sl_results/README.md`.

---

*Testing analysis: 2026/05/21*
