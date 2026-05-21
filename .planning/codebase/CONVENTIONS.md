# Coding Conventions

**Analysis Date:** 2026/05/21

## Naming Patterns

**Files:**
- Use lowercase snake_case for Python scripts: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Use `run_stage*_*.sh` for reproducibility shell entry points: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`.
- Use uppercase Markdown names for top-level reports and manifests: `README.md`, `MANIFEST.md`, `NARRATIVE_REPORT.md`, `RESEARCH_PIPELINE_REPORT.md`.
- Use result-directory names that encode dataset, stage, and method: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`, `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`.

**Functions:**
- Use lowercase snake_case verbs/nouns for Python functions: `parse_budgets`, `split_daily_frame`, `load_pems_dataset`, `make_laplacian`, `evaluate_layout`, `summarize_correlations`, `write_summary` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use domain-specific prefixes consistently:
  - `load_*` for data loaders: `load_pems_dataset`, `load_seattle_dataset` in `TRC-23-02333/transparent_estimator_eval.py`.
  - `make_*` for constructed matrices/statistics: `make_similarity`, `make_laplacian`, `make_rcss_row` in `TRC-23-02333/transparent_estimator_eval.py`.
  - `*_layout` for sensor-placement heuristics: `degree_layout`, `top_variance_layout`, `coverage_layout`, `greedy_posterior_layout`, `scenario_greedy_layout`, `robust_coverage_cvar_layout` in `TRC-23-02333/transparent_estimator_eval.py`.
  - `*_for_layout` for deterministic layout diagnostics: `posterior_trace_for_layout`, `posterior_condition_for_layout`, `posterior_logdet_for_layout`, `scenario_cvar_trace_for_layout` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep CLI entry points in a zero-argument `main()` and guard with `if __name__ == "__main__": main()` as in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Variables:**
- Use lowercase snake_case for local variables: `input_roots`, `output_dir`, `layout_summary`, `paired_rows` in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Use concise mathematical names only where they map directly to numerical formulas: `lhs`, `rhs`, `tod`, `rng`, `gls_z`, `gsp_lhs`, `train_z` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use plural collection names for lists and arrays: `metrics`, `correlations`, `rcss_candidates`, `layout_records`, `swap_records`, `random_layouts` in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Use explicit result-row dictionaries with stable CSV/JSON key names: `method`, `mae`, `rmse`, `mape`, `budget`, `layout_type`, `split_seed`, `layout_seed` in `TRC-23-02333/transparent_estimator_eval.py`.

**Types:**
- No static typing configuration is present. Function signatures in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` omit type hints.
- Represent numeric matrices and vectors as NumPy arrays (`np.array`, `np.asarray`, `np.zeros`, `np.full`) in `TRC-23-02333/transparent_estimator_eval.py`.
- Represent tabular inputs and outputs as Pandas `DataFrame` objects and CSV files in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Represent CLI configuration as an `argparse.Namespace`, then serialize `vars(args)` to `config.json` in `TRC-23-02333/transparent_estimator_eval.py`.

## Code Style

**Formatting:**
- No formatter configuration detected: no `pyproject.toml`, `setup.cfg`, `.flake8`, `ruff.toml`, `.prettierrc`, `eslint.config.*`, or `biome.json` exists under the scanned project root.
- Use standard Python indentation with 4 spaces, as in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Keep imports grouped at the top of files with standard library first, then third-party libraries, separated by a blank line: `argparse`, `json`, `math`, `Path`, then `numpy`, `pandas`, `scipy`, `sklearn` in `TRC-23-02333/transparent_estimator_eval.py`.
- Prefer one expression per line for dense numeric operations when readability is preserved; split long argument lists across multiple lines as in `select_auto_rcss_weights(...)` and `validation_swap_search(...)` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep shell scripts strict with `#!/usr/bin/env bash` and `set -euo pipefail` as in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Linting:**
- No linting tool is configured. Use `python -m py_compile TRC-23-02333/transparent_estimator_eval.py TRC-23-02333/summarize_trace_sl_rcss.py` as the lightweight syntax gate.
- Avoid introducing dependencies on unconfigured formatters or linters unless the project adds their config files at the root.

## Import Organization

**Order:**
1. Python standard library modules: `argparse`, `json`, `math`, `pathlib.Path` in `TRC-23-02333/transparent_estimator_eval.py`; `argparse`, `pathlib.Path` in `TRC-23-02333/summarize_trace_sl_rcss.py`.
2. Third-party scientific stack: `numpy`, `pandas`, `scipy`, `sklearn` in `TRC-23-02333/transparent_estimator_eval.py`; `pandas`, `scipy.stats` in `TRC-23-02333/summarize_trace_sl_rcss.py`.
3. Local imports are not used. Keep these scripts self-contained unless a new shared module is introduced under `TRC-23-02333/`.

**Path Aliases:**
- Not applicable. No package import aliases or module path aliases are configured.
- Use `Path(__file__).resolve().parent` for script-relative default paths, as in the default PeMS data root in `TRC-23-02333/transparent_estimator_eval.py`.
- Use repository-relative paths in shell scripts and documentation: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, and `TRC-23-02333/trace_sl_results/...` in `scripts/run_stage11_pems7_228.sh` and `README.md`.

## Error Handling

**Patterns:**
- Raise `FileNotFoundError` when required dataset files are absent: `load_seattle_dataset` in `TRC-23-02333/transparent_estimator_eval.py` checks `tensor.npz` and `Loop_Seattle_2015_A.npy`.
- Raise `ValueError` for invalid shapes, unsupported objectives, empty RCSS grids, and missing selection methods: `load_seattle_dataset`, `greedy_posterior_layout`, `scenario_greedy_layout`, `parse_weight_grid`, and `validation_mae` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use `SystemExit` for CLI aggregation precondition failures: `TRC-23-02333/summarize_trace_sl_rcss.py` exits with `No seed metrics found under ...` when no `seed_*/metrics.csv` files are found.
- Prefer explicit numeric guards for unstable cases: `normalize_minmax` handles all-nonfinite or constant input, `metrics` clamps the MAPE denominator, and `swap_trace_local_search` skips invalid Sherman-Morrison removal denominators in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep shell scripts fail-fast with `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

## Logging

**Framework:** console

**Patterns:**
- Use `print(...)` for final tabular status and output-location messages in CLI scripts: `TRC-23-02333/transparent_estimator_eval.py` prints grouped MAE/RMSE means and `Wrote outputs to ...`; `TRC-23-02333/summarize_trace_sl_rcss.py` prints `layout_summary` and `Wrote summary to ...`.
- Use shell `tee` to preserve per-seed logs while streaming progress: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh` write `${OUTPUT_DIR}_seed_${seed}.log`.
- Persist machine-readable diagnostics to CSV/JSON rather than relying on logs: `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, and `config.json` are written by `TRC-23-02333/transparent_estimator_eval.py`.

## Comments

**When to Comment:**
- Inline comments are sparse. Prefer clear function names, explicit variable names, and output artifact names over narrative comments in code.
- Use Markdown reports for methodological explanation and experiment interpretation: `README.md`, `RESEARCH_PIPELINE_REPORT.md`, `NARRATIVE_REPORT.md`, and `TRC-23-02333/trace_sl_results/README.md`.
- In shell scripts, encode tunable parameters as environment-variable defaults near the top rather than burying comments in command invocations: `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, `NUM_LAYOUTS`, and RCSS parameters in `scripts/run_stage11_pems7_228.sh`.

**JSDoc/TSDoc:**
- Not applicable. This is a Python/shell research codebase.
- Python docstrings are not currently used in the main scripts. If adding docstrings, keep them short and focused on algorithmic intent for functions such as new layout generators or evaluators in `TRC-23-02333/transparent_estimator_eval.py`.

## Function Design

**Size:**
- Most helper functions are compact and single-purpose, e.g. `parse_budgets`, `adjacency_to_distance`, `metrics`, `coverage_penalty`, and `normalize_minmax` in `TRC-23-02333/transparent_estimator_eval.py`.
- The experiment driver `main()` in `TRC-23-02333/transparent_estimator_eval.py` is intentionally orchestration-heavy: it parses CLI arguments, loads datasets, constructs matrices, generates layouts, evaluates metrics, and writes artifacts. Add new algorithms as helper functions, then call them from `main()`.
- Keep aggregation logic in `TRC-23-02333/summarize_trace_sl_rcss.py` as DataFrame transformations and output writes; extract helpers only when adding repeated statistical summaries.

**Parameters:**
- Pass explicit arrays and matrices into numerical helpers instead of reading global state: `evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args)` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use `args` for CLI-configured hyperparameters that are shared across the experiment: `args.obs_weight`, `args.selection_method`, `args.cvar_tail_fraction`, `args.validation_swap_iter` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use deterministic seeds from CLI arguments and shell defaults: `--split-seed`, `--layout-seed`, `SEEDS`, and dataset-specific layout seed offsets in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Return Values:**
- Return NumPy arrays for layouts: `degree_layout`, `coverage_layout`, `greedy_posterior_layout`, `scenario_greedy_layout`, and `swap_trace_local_search` in `TRC-23-02333/transparent_estimator_eval.py`.
- Return `(rows, hidden)` from `evaluate_layout` in `TRC-23-02333/transparent_estimator_eval.py`, where `rows` is a list of metric dictionaries ready for DataFrame serialization.
- Return dictionaries for row-level metrics and certificates: `metrics`, `certificate`, and `make_rcss_row` in `TRC-23-02333/transparent_estimator_eval.py`.
- Return explicit history lists for iterative search routines: `swap_trace_local_search` and `validation_swap_search` in `TRC-23-02333/transparent_estimator_eval.py`.

## Module Design

**Exports:**
- There is no package-level API. `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` are executable scripts with helper functions and a `main()` entry point.
- Keep new reusable experiment logic in helper functions above `main()` in `TRC-23-02333/transparent_estimator_eval.py` unless it becomes shared by multiple scripts.
- Keep result aggregation logic in `TRC-23-02333/summarize_trace_sl_rcss.py` when it consumes seed directories and produces aggregate CSV/Markdown outputs.

**Barrel Files:**
- Not used. There are no `__init__.py` barrel modules or package exports.
- Do not add import barrels unless the repository is converted into an installable Python package.

## Project-Specific Constraints

- Project skill directories were checked; no `.claude/skills/` or `.agents/skills/` directory is present under `/home/samuel/projects/sensor_opt`.
- Do not read or commit dataset directories that may be local-only. `README.md` states datasets are intentionally not committed and should be placed under `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, or `TRC-23-02333/dataset/Seattle/`.
- Preserve reproducibility artifacts under `TRC-23-02333/trace_sl_results/`; `TRC-23-02333/trace_sl_results/README.md` identifies curated result stages and key Stage 11 output files.

---

*Convention analysis: 2026/05/21*
