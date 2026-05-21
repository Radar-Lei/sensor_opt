# Testing Patterns

**Analysis Date:** 2026/05/21

## Test Framework

**Runner:**
- Not detected. No `pytest`, `unittest`, `jest`, `vitest`, or other test runner configuration is present in `/home/samuel/projects/sensor_opt`.
- Config: Not detected. No `pytest.ini`, `pyproject.toml`, `setup.cfg`, `tox.ini`, `jest.config.*`, or `vitest.config.*` was found in `/home/samuel/projects/sensor_opt`.
- Test files: Not detected. No files matching common test patterns such as `test_*.py`, `*_test.py`, `*.test.*`, or `*.spec.*` were found under `/home/samuel/projects/sensor_opt`.

**Assertion Library:**
- Not detected. The repository does not currently use `pytest` assertions, `unittest`, or third-party assertion helpers.
- Scientific checks are embedded in runtime exceptions and output summaries inside `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Run Commands:**
```bash
python TRC-23-02333/transparent_estimator_eval.py --max-test-steps 1 --num-layouts 1 --budgets "0.10" --include-simple-baselines  # Smoke-run primary evaluator on default PeMS7_228 data
bash scripts/run_stage11_pems7_228.sh                                                                                # Run stage 11 PeMS7_228 experiment batch
python TRC-23-02333/summarize_trace_sl_rcss.py --input-root TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight --output-dir TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight  # Rebuild aggregate summaries
```

## Test File Organization

**Location:**
- Not detected. There is no dedicated `tests/` directory and no co-located test files in `/home/samuel/projects/sensor_opt`.
- Existing validation is experiment-driven through CLI scripts and generated artifacts in `TRC-23-02333/trace_sl_results/`.

**Naming:**
- Not detected for test files.
- If adding tests, follow Python conventions with `tests/test_transparent_estimator_eval.py` for functions in `TRC-23-02333/transparent_estimator_eval.py` and `tests/test_summarize_trace_sl_rcss.py` for `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Structure:**
```text
/home/samuel/projects/sensor_opt/
├── TRC-23-02333/
│   ├── transparent_estimator_eval.py       # Primary executable and algorithm functions
│   └── summarize_trace_sl_rcss.py          # Result aggregation executable
├── scripts/
│   ├── run_stage11_pems7_228.sh            # Batch experiment runner
│   ├── run_stage11_pems7_1026.sh           # Batch experiment runner
│   └── run_stage11_seattle.sh              # Batch experiment runner
└── tests/                                  # Not present; add here if formal tests are introduced
```

## Test Structure

**Suite Organization:**
```python
# Recommended structure for future tests of TRC-23-02333/transparent_estimator_eval.py

def test_metrics_returns_mae_rmse_mape_for_arrays():
    pred = np.array([[1.0, 3.0]])
    true = np.array([[2.0, 1.0]])

    result = metrics(pred, true)

    assert set(result) == {"mae", "rmse", "mape"}
    assert result["mae"] >= 0.0
```

**Patterns:**
- Current pattern: CLI smoke execution and artifact inspection rather than unit test suites.
- Setup pattern: create or point to dataset roots with `--data-root`; the default dataset path is computed in `TRC-23-02333/transparent_estimator_eval.py` as `TRC-23-02333/dataset/PeMS7_228`.
- Teardown pattern: output directories are created by the scripts and not automatically removed. `TRC-23-02333/transparent_estimator_eval.py` writes to `--output-dir`; shell runners write under `TRC-23-02333/trace_sl_results/`.
- Assertion pattern: verify existence and schema of generated files such as `metrics.csv`, `layouts.json`, `config.json`, `SUMMARY.md`, and `certificate_correlations.csv` produced by `TRC-23-02333/transparent_estimator_eval.py`.

## Mocking

**Framework:** Not detected

**Patterns:**
```python
# No mocking pattern currently exists in the repository.
# Prefer small synthetic NumPy arrays/DataFrames over mocks for future tests.

distance = np.array([[0.0, 1.0], [1.0, 0.0]])
sensors = np.array([0], dtype=int)
```

**What to Mock:**
- Avoid mocks for NumPy, pandas, SciPy, and scikit-learn numerical operations in `TRC-23-02333/transparent_estimator_eval.py`; use small deterministic arrays instead.
- Mock or isolate filesystem writes only when testing `write_summary` in `TRC-23-02333/transparent_estimator_eval.py` or the output generation in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- For CLI tests, prefer temporary directories for `--output-dir` instead of mocking `Path.write_text` or pandas `to_csv`.

**What NOT to Mock:**
- Do not mock `linalg.solve`, `linalg.inv`, `shortest_path`, `LedoitWolf`, `pearsonr`, or `spearmanr` when validating numerical behavior in `TRC-23-02333/transparent_estimator_eval.py`; these are core behavior dependencies.
- Do not mock the random number generator. Pass a deterministic `np.random.default_rng(seed)` to functions such as `quality_coverage_sample` in `TRC-23-02333/transparent_estimator_eval.py`.
- Do not mock pandas groupby/pivot behavior in `TRC-23-02333/summarize_trace_sl_rcss.py`; use minimal DataFrames or CSV fixtures.

## Fixtures and Factories

**Test Data:**
```python
# Recommended fixture style for future tests
train = np.array(
    [
        [10.0, 20.0, 30.0],
        [11.0, 19.0, 29.0],
        [12.0, 18.0, 28.0],
    ],
    dtype=float,
)
distance = np.array(
    [
        [0.0, 1.0, 2.0],
        [1.0, 0.0, 1.0],
        [2.0, 1.0, 0.0],
    ],
    dtype=float,
)
rng = np.random.default_rng(2026)
```

**Location:**
- Current repository data fixtures are real research datasets in `TRC-23-02333/dataset/PeMS7_228`, `TRC-23-02333/dataset/PeMS7_1026`, and `TRC-23-02333/dataset/Seattle`.
- Current result fixtures/artifacts are under `TRC-23-02333/trace_sl_results/`.
- If formal tests are added, place small synthetic fixtures under `tests/fixtures/` and avoid copying large files from `TRC-23-02333/dataset/`.

## Coverage

**Requirements:** None enforced

**View Coverage:**
```bash
# Not configured. If coverage is introduced, add pytest-cov to requirements and run:
pytest --cov=TRC-23-02333 --cov-report=term-missing
```

## Test Types

**Unit Tests:**
- Not currently present.
- Best candidates for unit tests in `TRC-23-02333/transparent_estimator_eval.py`: `parse_budgets`, `adjacency_to_distance`, `metrics`, `make_similarity`, `make_laplacian`, `normalize_minmax`, `coverage_penalty`, `parse_weight_grid`, and `rcss_candidate_scores`.
- Use synthetic arrays and deterministic seeds. Keep tests fast and independent of `TRC-23-02333/dataset/` unless intentionally testing loaders.

**Integration Tests:**
- Current integration validation is performed by running `TRC-23-02333/transparent_estimator_eval.py` with dataset paths and checking generated artifacts.
- Shell launchers in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh` serve as reproducible experiment integration runners.
- A lightweight integration test should run `TRC-23-02333/transparent_estimator_eval.py` with `--max-test-steps 1`, `--num-layouts 1`, and a temporary `--output-dir`, then assert `metrics.csv`, `metrics.json`, `layouts.json`, `config.json`, and `SUMMARY.md` exist.

**E2E Tests:**
- Not used as an automated framework.
- Manual end-to-end experiment flow: run one of `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, or `scripts/run_stage11_seattle.sh`; inspect CSV/JSON outputs and generated `SUMMARY.md` under `TRC-23-02333/trace_sl_results/`.

## Common Patterns

**Async Testing:**
```python
# Not applicable. The codebase is synchronous Python and Bash.
```

**Error Testing:**
```python
# Recommended future pattern for parser and validation errors
with pytest.raises(ValueError):
    parse_weight_grid("1 2 3")

with pytest.raises(ValueError):
    greedy_posterior_layout(base_matrix, sensor_count=1, obs_weight=1.0, objective="unsupported")
```

## CLI Smoke Checks

**Primary evaluator:**
- Use `TRC-23-02333/transparent_estimator_eval.py` for smoke checks. The script validates dataset files, computes train/validation/test splits, builds layouts, evaluates metrics, and writes outputs.
- Minimum useful command:
```bash
python TRC-23-02333/transparent_estimator_eval.py \
  --data-root TRC-23-02333/dataset/PeMS7_228 \
  --output-dir /tmp/trace_sl_smoke \
  --budgets "0.10" \
  --num-layouts 1 \
  --max-test-steps 1 \
  --include-simple-baselines
```

**Summary aggregator:**
- Use `TRC-23-02333/summarize_trace_sl_rcss.py` after one or more `seed_*/metrics.csv` outputs exist.
- The aggregator writes `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `gls_map_ablation_summary.csv`, `gls_map_per_split_winners.csv`, `gls_map_win_counts.csv`, optional RCSS/correlation CSVs, and `SUMMARY.md`.

## Regression Signals

**Numerical outputs:**
- Track changes in `mae`, `rmse`, `mape`, `posterior_trace`, `condition_number`, and `information_logdet` produced by `TRC-23-02333/transparent_estimator_eval.py`.
- Compare generated `metrics.csv` and `layouts.json` across fixed `--split-seed` and `--layout-seed` values for reproducibility.

**Artifact schema:**
- Preserve columns written in `metrics.csv`: dataset, budget, sensor_count, hidden_count, layout_type, layout_id, split_seed, layout_seed, validation_selected_mae, method, mae, rmse, mape, and certificate fields where applicable.
- Preserve files written by `TRC-23-02333/transparent_estimator_eval.py`: `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, `config.json`, and `SUMMARY.md`.

---

*Testing analysis: 2026/05/21*
