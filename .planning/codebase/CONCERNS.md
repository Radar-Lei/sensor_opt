# Codebase Concerns

**Analysis Date:** 2026/05/21

## Tech Debt

**Monolithic experiment driver:**
- Issue: The core TRACE-SL implementation, CLI parsing, data loading, numerical solvers, layout generation, evaluation, artifact writing, and summary generation all live in one 1,024-line script.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Impact: Changes to one concern, such as a new layout generator or output schema, require editing a large orchestration file and increase regression risk across unrelated experiment paths.
- Fix approach: Extract stable modules under `TRC-23-02333/`, for example `data.py` for `load_pems_dataset`/`load_seattle_dataset`, `layouts.py` for `*_layout` functions, `evaluation.py` for `evaluate_layout`/`metrics`, and keep `TRC-23-02333/transparent_estimator_eval.py` as a thin CLI driver.

**Unpinned scientific dependencies:**
- Issue: Dependencies are listed without versions, so NumPy/Pandas/SciPy/scikit-learn numerical behavior and warning/error behavior can drift across environments.
- Files: `requirements.txt`
- Impact: Re-running Stage 11 artifacts may produce slightly different metrics, solver behavior, or CSV formatting after dependency upgrades, weakening reproducibility claims.
- Fix approach: Pin tested versions in `requirements.txt` or add a lockfile/constraints file, then record the environment in generated `config.json` from `TRC-23-02333/transparent_estimator_eval.py`.

**No automated unit-test or lint gate:**
- Issue: No `pytest.ini`, `pyproject.toml`, `tox.ini`, `setup.cfg`, `conftest.py`, or test files are present; validation is currently script/artifact based.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, `.planning/codebase/TESTING.md`
- Impact: Pure helpers such as `parse_weight_grid`, `normalize_minmax`, `coverage_layout`, `split_daily_frame`, and `summarize_correlations` can regress without fast feedback; full Stage 11 runs are too expensive for routine checks.
- Fix approach: Add a small `tests/` suite with synthetic arrays and temporary directories, and keep full scripts in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh` as integration/reproducibility checks.

**Large committed experiment artifacts:**
- Issue: The checked result tree contains many CSV/JSON/log artifacts; local scan found 631 files and about 153 MB under `TRC-23-02333/trace_sl_results/`, with 432 tracked artifact paths under `TRC-23-02333/trace_sl_results/` or `sumo_scenarios/`.
- Files: `TRC-23-02333/trace_sl_results/`, `sumo_scenarios/chengdu/chengdu.rou.xml`, `sumo_scenarios/chengdu/chengdu.net.xml`, `.gitignore`
- Impact: Repository clone/diff/review operations are heavier, and future commits can accidentally add large intermediate artifacts despite `.gitignore` curation.
- Fix approach: Keep only final aggregate CSV/Markdown summaries needed for paper reproducibility, move bulky per-seed JSON/log artifacts to releases or external storage, and update `TRC-23-02333/trace_sl_results/README.md` with checksums or download instructions.

**Duplicated shell launcher logic:**
- Issue: The three Stage 11 launchers repeat the same environment setup, seed loop, CLI flags, and aggregation pattern with only dataset defaults and seed offsets changed.
- Files: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`
- Impact: A change to one experiment flag, BLAS thread setting, logging path, or aggregation behavior can drift across datasets.
- Fix approach: Introduce one parameterized launcher such as `scripts/run_stage11.sh` and keep dataset-specific scripts as thin wrappers that set `DATA_ROOT`, `OUTPUT_DIR`, candidate counts, and layout seed offset.

## Known Bugs

**PeMS loader falls through to Seattle loader on partial PeMS inputs:**
- Symptoms: If either `PeMSD7_V_*.csv` or `PeMSD7_W_*.csv` is missing, the PeMS loader calls the Seattle loader, which then expects `tensor.npz` and `Loop_Seattle_2015_A.npy` under the same directory.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Trigger: Run `TRC-23-02333/transparent_estimator_eval.py --data-root <PeMS directory>` where only one PeMS CSV exists or file names do not match `PeMSD7_V_*.csv` and `PeMSD7_W_*.csv`.
- Workaround: Ensure both expected PeMS files exist at paths documented in `README.md`, for example `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv` and `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`.

**PeMS timestamp index assumes fixed weekday-only date range:**
- Symptoms: The PeMS loader builds timestamps for 2012-05-01 through 2012-06-30 weekdays and assigns them directly to the CSV value matrix without explicitly validating row count.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Trigger: Use a PeMS-like CSV whose row count differs from the hardcoded weekday 5-minute timestamp count.
- Workaround: Use the exact PeMS7_228 and PeMS7_1026 files documented in `README.md`, or add a row-count validation before constructing the `DataFrame`.

**Aggregation assumes `gls_map` rows exist for every split:**
- Symptoms: The summarizer filters `combined[combined["method"] == "gls_map"]` and then builds summaries, pivots, winners, and paired tests from that subset.
- Files: `TRC-23-02333/summarize_trace_sl_rcss.py`
- Trigger: Aggregate result directories produced with a future evaluator configuration that omits `gls_map` or changes method naming.
- Workaround: Use the current evaluator path in `TRC-23-02333/transparent_estimator_eval.py`, which always writes `gls_map`, or add explicit schema checks in `TRC-23-02333/summarize_trace_sl_rcss.py`.

## Security Considerations

**Local-only datasets are intentionally ignored but colocated with scripts:**
- Risk: Large licensed/raw traffic datasets can be accidentally copied into a non-ignored path or committed if ignore rules change.
- Files: `.gitignore`, `README.md`, `TRC-23-02333/dataset/`
- Current mitigation: `.gitignore` ignores `dataset/` and `TRC-23-02333/dataset/`; `README.md` states datasets are intentionally not committed.
- Recommendations: Keep datasets only under the documented ignored directories and review `git status` before any commit that touches `.gitignore` or `TRC-23-02333/`.

**Output directory is user-controlled:**
- Risk: `--output-dir` is accepted as an arbitrary path and `mkdir(parents=True, exist_ok=True)` plus multiple `write_text`/`to_csv` calls will create or overwrite files at that location.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`
- Current mitigation: Scripts are local research CLIs, not network services; shell launchers default to repository result directories under `TRC-23-02333/trace_sl_results/`.
- Recommendations: Do not run these scripts with untrusted `OUTPUT_DIR` or `--output-dir` values; add a safety confirmation or repository-root guard if scripts are exposed to automation.

**No secrets detected in scanned source paths:**
- Risk: Not detected in source files scanned for this concern map.
- Files: `requirements.txt`, `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`, `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`
- Current mitigation: No `.env` file or credential file was read; no external API credentials are required by the current scientific pipeline.
- Recommendations: Keep environment variables in launchers limited to non-secret runtime controls such as `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, and BLAS thread counts.

## Performance Bottlenecks

**Repeated dense matrix inversion and condition-number computation:**
- Problem: Layout scoring repeatedly calls dense `linalg.inv`, `np.linalg.cond`, and related matrix operations for each candidate, budget, scenario, and swap trial.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Cause: Functions such as `posterior_inverse_for_layout`, `posterior_trace_for_layout`, `posterior_condition_for_layout`, `scenario_cvar_trace_for_layout`, `certificate`, `greedy_posterior_layout`, and `robust_coverage_cvar_layout` work with dense matrices.
- Improvement path: Reuse factorizations where possible, prefer solve/Cholesky-based trace estimators for large networks, cache layout diagnostics keyed by sensor tuple, and keep Sherman-Morrison updates for local-search paths.

**Validation-swap search performs expensive nested candidate evaluation:**
- Problem: Each validation-swap iteration evaluates remove/add combinations and calls `make_rcss_row`, which calls validation reconstruction and several posterior diagnostics.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Cause: `validation_swap_search` loops over selected removal candidates and add-pool candidates, then filters trials only after full row construction.
- Improvement path: Pre-screen swaps with cheaper posterior or coverage scores, memoize `make_rcss_row` results for repeated sensor tuples, and expose smaller default pools for very large networks.

**Large JSON artifacts duplicate CSV data:**
- Problem: Per-seed outputs include `metrics.json`, `layouts.json`, and `rcss_candidates.json`; some `rcss_candidates.json` files exceed 1 MB each.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/trace_sl_results/`
- Cause: The evaluator writes both tabular CSV and verbose indented JSON for rows, layouts, swaps, RCSS candidates, and config.
- Improvement path: Keep compact CSV/Parquet for large tabular artifacts, compress JSON if nested structure is required, or make verbose JSON optional via a CLI flag.

## Fragile Areas

**Dataset loading and split logic:**
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `README.md`
- Why fragile: `load_pems_dataset` depends on filename globs and hardcoded PeMS calendar assumptions; `load_seattle_dataset` depends on `tensor.npz` shape `(nodes, days, 288)` and a specific adjacency filename.
- Safe modification: Add explicit validation for required file pairs, row counts, finite-value handling, and split sizes before changing date logic or supporting new datasets.
- Test coverage: No automated tests exist; add tiny synthetic PeMS CSV and Seattle `.npz`/`.npy` fixtures under a future `tests/fixtures/` directory.

**Summary schema and method names:**
- Files: `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/trace_sl_results/`
- Why fragile: The summarizer hardcodes `gls_map`, layout names such as `validation_swap_selected`, `rcss_selected`, `robust_coverage_cvar`, and output artifact names such as `metrics.csv` and `rcss_candidates.csv`.
- Safe modification: Treat method/layout names as a public artifact schema; when renaming methods, write backward-compatible aliases or schema-version fields in `config.json`.
- Test coverage: No schema tests exist; add temporary-directory tests for `TRC-23-02333/summarize_trace_sl_rcss.py` with minimal `seed_*/metrics.csv` and optional candidate/correlation files.

**Numerical stability of covariance-derived precision matrices:**
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Why fragile: Precision matrices use `LedoitWolf().fit(...).covariance_` and `linalg.inv(covariance + 1e-6 * I)`; solver calls use `assume_a="pos"` and can fail or produce unstable certificates if assumptions are violated.
- Safe modification: Keep positive-definite regularization explicit, check matrix symmetry/condition number before solving, and record failure diagnostics in output `config.json` or a new diagnostics artifact.
- Test coverage: No tests cover singular/near-singular matrices; add deterministic small matrices that verify guards in `certificate`, `solve_quadratic`, and posterior diagnostic helpers.

**Research reports and code can drift:**
- Files: `README.md`, `NARRATIVE_REPORT.md`, `RESEARCH_PIPELINE_REPORT.md`, `TRC-23-02333/trace_sl_results/`
- Why fragile: Claims and tables in Markdown reports are manually synchronized with CSV artifacts.
- Safe modification: Generate publication tables from checked CSV files where possible, and cite exact source files such as `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/gls_map_layout_summary.csv`.
- Test coverage: No automated consistency check exists between reports and CSV summaries.

## Scaling Limits

**Dense O(n²) to O(n³) numerical operations:**
- Current capacity: Existing scripts target PeMS7_228, PeMS7_1026, and Seattle; `README.md` documents PeMS7_1026 as a larger external-validation case with reduced default candidate counts.
- Limit: Dense matrix inversion, condition numbers, candidate scoring, and validation-swap loops become expensive as node count, candidate count, scenario count, and budget increase.
- Scaling path: Use sparse or low-rank approximations for large networks, reduce candidate pools adaptively, cache diagnostics, and add profiling around `validation_swap_search`, `robust_coverage_cvar_layout`, and `scenario_cvar_trace_for_layout` in `TRC-23-02333/transparent_estimator_eval.py`.

**Sequential seed execution:**
- Current capacity: Shell scripts loop over seeds sequentially while limiting BLAS threads via `THREADS_PER_JOB=1`.
- Limit: Multi-split studies scale linearly with the number of seeds and datasets.
- Scaling path: Add an optional parallel launcher that runs seeds concurrently with controlled `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS`, while keeping deterministic output directories from `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Repository size from reproducibility artifacts:**
- Current capacity: Local scan found about 153 MB across 631 files under `TRC-23-02333/trace_sl_results/`.
- Limit: Adding more split seeds, datasets, or verbose per-seed JSON/log outputs can make the repository cumbersome for review and distribution.
- Scaling path: Store raw per-seed artifacts externally, commit only aggregate summaries, and document reproduction commands in `README.md` and `TRC-23-02333/trace_sl_results/README.md`.

## Dependencies at Risk

**scikit-learn LedoitWolf API and numerical behavior:**
- Risk: `LedoitWolf().fit(...).covariance_` behavior can vary with scikit-learn and dependency versions.
- Impact: Precision matrices in `TRC-23-02333/transparent_estimator_eval.py` can shift, affecting posterior certificates, layout selection, and final metrics.
- Migration plan: Pin scikit-learn in `requirements.txt`; if needed, persist covariance/precision diagnostics and add regression tests on small arrays.

**SciPy linear algebra and statistical tests:**
- Risk: `scipy.linalg.solve`, `scipy.linalg.inv`, `scipy.stats.ttest_rel`, and `scipy.stats.wilcoxon` are central to evaluation and aggregation.
- Impact: Solver tolerances and statistical-test handling of NaN/zero-difference cases can affect output metrics and p-values in `TRC-23-02333/trace_sl_results/` summaries.
- Migration plan: Pin SciPy, record version metadata in `config.json`, and add tests for paired-delta summaries in `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Pandas CSV parsing/serialization:**
- Risk: `pd.read_csv`, `DataFrame.to_csv`, `pivot_table`, and groupby aggregation are used for both seed-level and aggregate artifacts.
- Impact: CSV dtype inference or formatting changes can alter summary outputs and downstream paper tables.
- Migration plan: Pin Pandas, specify critical dtypes where appropriate, and add schema checks for `metrics.csv`, `rcss_candidates.csv`, and aggregate CSVs.

## Missing Critical Features

**Fast automated regression suite:**
- Problem: There is no quick command that validates core helpers without full datasets and long experiment runs.
- Blocks: Safe refactoring of `TRC-23-02333/transparent_estimator_eval.py`, reliable dependency upgrades, and confident changes to loader/summarizer behavior.

**Schema/version metadata for artifacts:**
- Problem: Output artifacts record configuration but do not declare an explicit schema version for `metrics.csv`, `layouts.json`, `rcss_candidates.csv`, or aggregate CSV files.
- Blocks: Backward-compatible evolution of method names, layout names, and summary columns in `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Publication figure generation scripts:**
- Problem: `RESEARCH_PIPELINE_REPORT.md` lists publication figures as remaining work, but no figure-generation script is present in the scanned source files.
- Blocks: Reproducible paper figures from `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`, `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`, and `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`.

## Test Coverage Gaps

**Pure numerical helpers:**
- What's not tested: `parse_budgets`, `metrics`, `normalize_minmax`, `adjacency_to_distance`, `coverage_layout`, `coverage_penalty`, `parse_weight_grid`, and posterior diagnostic helpers.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Risk: Small changes can alter layout scores, MAPE/RMSE/MAE calculations, or edge-case handling without immediate detection.
- Priority: High

**Dataset loaders:**
- What's not tested: PeMS glob handling, Seattle tensor shape validation, missing-file errors, finite-value imputation, and day split reproducibility.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `README.md`
- Risk: New datasets or renamed files can fail late or produce misleading splits.
- Priority: High

**Aggregation and statistical summaries:**
- What's not tested: Multi-root aggregation, paired t/Wilcoxon outputs, winner counts, optional correlation/candidate files, and behavior when layouts are missing.
- Files: `TRC-23-02333/summarize_trace_sl_rcss.py`
- Risk: Paper-facing CSV and `SUMMARY.md` outputs can drift or silently omit comparisons.
- Priority: High

**Shell reproducibility launchers:**
- What's not tested: Environment-variable overrides, output directory creation, per-seed log naming, and final aggregation invocation.
- Files: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`
- Risk: A launcher can appear valid but write to the wrong result directory or run inconsistent Stage 11 flags.
- Priority: Medium

---

*Concerns audit: 2026/05/21*
