# Codebase Concerns

**Analysis Date:** 2026/05/21

## Tech Debt

**Monolithic TRACE-SL experiment driver:**
- Issue: `TRC-23-02333/transparent_estimator_eval.py` combines dataset loading, preprocessing, matrix construction, layout generation, RCSS scoring, validation-swap search, evaluation, serialization, and CLI parsing in one 1,024-line script.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Impact: Small changes to one concern can affect unrelated experiment behavior; reuse is difficult; targeted testing is difficult because most logic is wired through `main()` and shared argument state.
- Fix approach: Split into importable modules under `TRC-23-02333/` or a package directory: `data.py` for `load_pems_dataset()` / `load_seattle_dataset()`, `models.py` for GLS/GSP reconstruction, `layouts.py` for greedy/swap/coverage layouts, `rcss.py` for candidate scoring and validation swap, and `cli.py` for orchestration. Keep `TRC-23-02333/transparent_estimator_eval.py` as a thin command-line wrapper.

**Implicit experiment configuration in shell scripts:**
- Issue: Stage 11 settings live as environment-variable defaults in shell scripts rather than a versioned experiment config file.
- Files: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`, `TRC-23-02333/transparent_estimator_eval.py`
- Impact: Reproducing exact runs depends on shell defaults, current working directory, and manually supplied overrides; comparing PeMS7_228, PeMS7_1026, and Seattle settings requires reading multiple scripts.
- Fix approach: Add checked-in YAML/JSON config files such as `TRC-23-02333/configs/stage11_pems7_228.json`, load them in `TRC-23-02333/transparent_estimator_eval.py`, and let shell scripts only choose config paths and seed ranges.

**Unpinned Python dependencies:**
- Issue: `requirements.txt` lists package names without versions.
- Files: `requirements.txt`, `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`
- Impact: Numerical output can drift across `numpy`, `pandas`, `scipy`, and `scikit-learn` releases; paper tables and p-values can become hard to reproduce on a fresh environment.
- Fix approach: Pin tested versions in `requirements.txt` or add `requirements-lock.txt`; record `python --version` and package versions into each run's `config.json` in `TRC-23-02333/transparent_estimator_eval.py`.

**Result curation is split between README claims and `.gitignore` allowlist:**
- Issue: `.gitignore` allowlists selected `TRC-23-02333/trace_sl_results/` stages, but current documentation references additional artifacts such as Seattle validation and extra PeMS splits.
- Files: `.gitignore`, `README.md`, `RESEARCH_PIPELINE_REPORT.md`, `NARRATIVE_REPORT.md`, `TRC-23-02333/trace_sl_results/README.md`
- Impact: Important reproducibility outputs can remain local and ignored even when reports cite them; future commits can omit evidence needed to support current claims.
- Fix approach: Keep `.gitignore` allowlist synchronized with the current claim set, especially `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/` and any aggregate directories cited by `README.md` or `NARRATIVE_REPORT.md`.

## Known Bugs

**Selected-source summary omits validation-swap final selections:**
- Symptoms: The current main method is `validation_swap_selected`, but candidate-source summaries count only rows where `selected` is `True` for the pre-swap `rcss_best`; validation-swap rows are appended to `rcss_all` but are not marked as selected.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/trace_sl_results/README.md`, `NARRATIVE_REPORT.md`
- Trigger: Run `TRC-23-02333/transparent_estimator_eval.py` with `--include-rcss --include-validation-swap`, then aggregate with `TRC-23-02333/summarize_trace_sl_rcss.py`; `rcss_selected_sources.csv` reports pre-swap RCSS sources rather than final validation-swap winners.
- Workaround: Treat `TRC-23-02333/trace_sl_results/*/rcss_selected_sources.csv` as pre-swap mechanism diagnostics, not as final selected-layout source counts.

**PeMS loader silently falls back to Seattle loader when PeMS files are missing:**
- Symptoms: Missing `PeMSD7_V_*.csv` or `PeMSD7_W_*.csv` under a PeMS data root causes `load_pems_dataset()` to call `load_seattle_dataset()`, producing an error about missing `tensor.npz` / `Loop_Seattle_2015_A.npy` instead of a PeMS-specific missing-file error.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `README.md`
- Trigger: Run `python TRC-23-02333/transparent_estimator_eval.py --data-root TRC-23-02333/dataset/PeMS7_228` when local PeMS CSVs are absent.
- Workaround: Ensure `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv` and `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv` exist before running PeMS experiments.

**Shell entry points assume repository-root working directory:**
- Symptoms: Scripts call `python TRC-23-02333/transparent_estimator_eval.py` using relative paths.
- Files: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`
- Trigger: Launch a script from a directory other than `/home/samuel/projects/sensor_opt`.
- Workaround: Run scripts from `/home/samuel/projects/sensor_opt`, or set `DATA_ROOT` and `OUTPUT_DIR` carefully and invoke the Python script with an absolute path.

## Security Considerations

**Local data and result paths are unrestricted:**
- Risk: `--data-root` and `--output-dir` accept arbitrary local paths; a mistaken `--output-dir` can overwrite existing result CSV/JSON/SUMMARY files in that directory.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`
- Current mitigation: Scripts default to project-local `TRC-23-02333/trace_sl_results/...` output paths and create output directories with `mkdir -p` / `Path.mkdir()`.
- Recommendations: Add explicit overwrite controls such as `--overwrite`, refuse non-empty `--output-dir` unless explicitly allowed, and write a run manifest before writing result artifacts.

**Dataset contents are intentionally local and ignored:**
- Risk: Large raw datasets under `TRC-23-02333/dataset/` are ignored and can contain licensed or non-redistributable traffic data.
- Files: `.gitignore`, `README.md`, `TRC-23-02333/transparent_estimator_eval.py`
- Current mitigation: `.gitignore` excludes `dataset/` and `TRC-23-02333/dataset/`; `README.md` documents local data placement only.
- Recommendations: Keep raw datasets out of commits; add checksums and source/license notes in a non-secret manifest such as `TRC-23-02333/dataset/README.md` if redistribution terms permit metadata.

## Performance Bottlenecks

**Dense matrix inversion and repeated solves limit larger-network scaling:**
- Problem: Layout scoring repeatedly computes dense inverses and condition numbers for GLS posterior matrices.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Cause: Functions such as `certificate()`, `posterior_inverse_for_layout()`, `posterior_trace_for_layout()`, `posterior_condition_for_layout()`, `scenario_cvar_trace_for_layout()`, `greedy_posterior_layout()`, `scenario_greedy_layout()`, and `robust_coverage_cvar_layout()` use `linalg.inv()` / `np.linalg.cond()` on dense matrices inside candidate loops.
- Improvement path: Replace full inversions with Cholesky factorization (`scipy.linalg.cho_factor` / `cho_solve`) for SPD systems, cache posterior traces per candidate, use rank-one updates where available, and add sparse or low-rank approximations for networks above PeMS7_1026 scale.

**Validation-aware swap search evaluates many full layouts:**
- Problem: Each accepted or rejected swap trial calls `make_rcss_row()`, which calls `validation_mae()` and `evaluate_layout()` for complete validation reconstruction.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`
- Cause: `validation_swap_search()` explores remove/add pools for multiple starts and iterations; each trial performs GLS/GSP solves over validation time steps.
- Improvement path: Pre-filter swaps with cheap posterior-gain scores, batch evaluate candidate sensors, memoize validation MAE by sorted sensor tuple, and expose profiling output in `config.json` or a run log.

**Aggregation loads every seed CSV into memory:**
- Problem: Multi-split aggregation concatenates all `metrics.csv`, `certificate_correlations.csv`, and `rcss_candidates.csv` files before summarizing.
- Files: `TRC-23-02333/summarize_trace_sl_rcss.py`
- Cause: `pd.concat()` is used over all seed outputs without chunking or schema checks.
- Improvement path: Keep current approach for small split counts; for large sweeps, stream metrics by budget/layout or add an optional `--summary-only` mode that avoids retaining full candidate tables.

## Fragile Areas

**Dataset loaders have hard-coded formats and calendar assumptions:**
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `README.md`
- Why fragile: PeMS loading assumes files named `PeMSD7_V_*.csv` and `PeMSD7_W_*.csv`, a fixed 2012 weekday timestamp range, and values aligned with generated timestamps; Seattle loading assumes `tensor.npz` key `arr_0`, 288 slots per day, and `Loop_Seattle_2015_A.npy`.
- Safe modification: Add explicit `--dataset-type {pems,seattle}`, validate shapes before building `DataFrame`s, and report expected vs actual row/node counts in `config.json`.
- Test coverage: No automated loader tests are detected for `TRC-23-02333/transparent_estimator_eval.py`.

**RCSS scoring depends on normalized candidate-pool composition:**
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `NARRATIVE_REPORT.md`, `TRC-23-02333/trace_sl_results/README.md`
- Why fragile: `rcss_candidate_scores()` min-max normalizes validation MAE, posterior trace, scenario CVaR, condition number, and coverage over the current candidate list; adding or removing candidate generators changes every normalized score.
- Safe modification: Treat candidate-pool changes as method changes; record source counts, selected weights, and candidate-generation parameters in result summaries; rerun paired comparisons whenever `rcss-random-candidates`, `rcss-quality-candidates`, or candidate source lists change.
- Test coverage: No regression tests are detected for ranking stability or score normalization in `TRC-23-02333/transparent_estimator_eval.py`.

**Statistical summaries assume paired layout columns exist and remain comparable:**
- Files: `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/trace_sl_results/*/combined_metrics.csv`, `TRC-23-02333/trace_sl_results/*/gls_map_paired_delta_tests.csv`
- Why fragile: `pivot_table()` and fixed layout lists drive delta and paired-test outputs; missing layout types or renamed layout labels silently remove comparisons from summary rows.
- Safe modification: Add required-layout validation for the main claim set: `validation_swap_selected`, `best_random_by_validation`, `random`, and `top_variance`; fail with a clear message when required columns are absent.
- Test coverage: No automated tests are detected for `TRC-23-02333/summarize_trace_sl_rcss.py`.

## Scaling Limits

**Dense GLS/MAP computation:**
- Current capacity: Current scripts target PeMS7_228 with 200 random and 200 quality candidates per split, PeMS7_1026 with 100 random and 100 quality candidates per split, and Seattle with 50 random and 50 quality candidates per split.
- Limit: Dense inversions and candidate-by-candidate validation become expensive as node count, candidate count, scenario count, or split count increases.
- Scaling path: Add sparse graph-aware solvers, cache candidate metrics, parallelize seed/budget jobs explicitly, and write profiling metadata from `TRC-23-02333/transparent_estimator_eval.py`.

**External-validation statistical power:**
- Current capacity: `RESEARCH_PIPELINE_REPORT.md` and `NARRATIVE_REPORT.md` cite 10 PeMS7_228 splits and five-split PeMS7_1026 / Seattle validations.
- Limit: Five-split external validations can yield Wilcoxon p-values of 0.0625 even with 5/5 wins, which is sensitive to reviewer expectations for nonparametric evidence.
- Scaling path: Increase PeMS7_1026 and Seattle split counts through `scripts/run_stage11_pems7_1026.sh` and `scripts/run_stage11_seattle.sh`, then aggregate with `TRC-23-02333/summarize_trace_sl_rcss.py`.

## Dependencies at Risk

**Scientific Python API and numeric drift:**
- Risk: Unpinned `numpy`, `pandas`, `scipy`, and `scikit-learn` versions can change linear algebra tolerances, CSV parsing defaults, statistical test behavior, or Ledoit-Wolf covariance estimates.
- Impact: Tables in `TRC-23-02333/trace_sl_results/*/SUMMARY.md`, `NARRATIVE_REPORT.md`, and `RESEARCH_PIPELINE_REPORT.md` can differ across machines.
- Migration plan: Pin dependency versions in `requirements.txt`, record package versions in every `TRC-23-02333/trace_sl_results/*/config.json`, and add a smoke test that checks a small run against expected schema and approximate metric ranges.

**SciPy statistical-test behavior:**
- Risk: `ttest_rel()` and `wilcoxon()` behavior around NaNs, zero deltas, and small samples can vary by SciPy version.
- Impact: `TRC-23-02333/summarize_trace_sl_rcss.py` writes p-values used in `NARRATIVE_REPORT.md` and `RESEARCH_PIPELINE_REPORT.md`.
- Migration plan: Pin SciPy, store raw paired deltas alongside p-values, and include exact test settings in generated `SUMMARY.md` files.

## Missing Critical Features

**Automated tests and CI:**
- Problem: No `pytest`, unit test files, or CI configuration are detected in the repository.
- Blocks: Safe refactoring of `TRC-23-02333/transparent_estimator_eval.py`, validation of loader behavior, regression protection for RCSS ranking, and schema guarantees for result summaries.

**Publication figure generation:**
- Problem: Reports identify needed figures, but no committed figure-generation script is detected.
- Blocks: Reproducible paper figures from `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`, `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`, and `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`.

**Run provenance and data fingerprints:**
- Problem: `config.json` records CLI settings and split shapes, but not git commit, package versions, input file checksums, host information, or elapsed runtime.
- Blocks: Full reproducibility audits for `TRC-23-02333/trace_sl_results/*/` outputs.

## Test Coverage Gaps

**Dataset loading:**
- What's not tested: PeMS CSV detection, Seattle tensor loading, missing-file behavior, shape validation, calendar alignment, and NaN imputation.
- Files: `TRC-23-02333/transparent_estimator_eval.py`, `README.md`
- Risk: Dataset changes can produce misleading splits or confusing errors.
- Priority: High

**Numerical reconstruction and certificates:**
- What's not tested: `solve_quadratic()`, `certificate()`, GLS/GSP MAE calculation, posterior trace/logdet/condition metrics, and hidden-node selection.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Risk: Numerical regressions can change core evidence without immediate detection.
- Priority: High

**Layout algorithms and RCSS ranking:**
- What's not tested: Greedy A/D layout selection, scenario-CVaR layout generation, quality-coverage sampling, RCSS min-max scoring, auto-weight selection, and validation-swap acceptance.
- Files: `TRC-23-02333/transparent_estimator_eval.py`
- Risk: Candidate-source or scoring changes can invalidate comparisons in `TRC-23-02333/trace_sl_results/*/`.
- Priority: High

**Aggregation outputs:**
- What's not tested: Multi-root aggregation, required output files, paired-test rows, selected-source summaries, and behavior when layout columns are missing.
- Files: `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/trace_sl_results/README.md`
- Risk: Summary CSVs can silently omit comparisons that support the main claim.
- Priority: Medium

---

*Concerns audit: 2026/05/21*
