# Coding Conventions

**Analysis Date:** 2026/05/21

## Naming Patterns

**Files:**
- Use lower_snake_case for Python research scripts: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Use `run_stage{N}_{dataset}.sh` naming for reproducible experiment launchers: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`.
- Keep dataset/result directory names aligned with paper or experiment labels: `TRC-23-02333/dataset/PeMS7_228`, `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight`.

**Functions:**
- Use lower_snake_case verbs/nouns for pure computation and data-loading functions: `parse_budgets`, `split_daily_frame`, `load_pems_dataset`, `greedy_posterior_layout`, `validation_swap_search` in `TRC-23-02333/transparent_estimator_eval.py`.
- Prefer explicit domain terms in function names. Use suffixes such as `_layout`, `_predict`, `_for_layout`, `_candidate`, `_summary` to show output semantics: `coverage_layout`, `neighbor_average_predict`, `posterior_trace_for_layout`, `select_rcss_candidate`, `write_summary` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep command-line scripts with a single `main()` entry point and `if __name__ == "__main__": main()` guard: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Variables:**
- Use lower_snake_case for local variables and CLI-derived fields: `data_root`, `output_dir`, `split_seed`, `layout_seed`, `sensor_count`, `scenario_matrices` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use short mathematical names only for established matrix/vector quantities: `lhs`, `rhs`, `tod`, `rng`, `gls_z`, `gsp_lhs` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use plural names for collections and row lists: `metrics`, `correlations`, `rcss_candidates`, `paired_rows` in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Shell scripts use uppercase environment-variable names with defaults: `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, `THREADS_PER_JOB` in `scripts/run_stage11_pems7_228.sh` and `scripts/run_stage11_seattle.sh`.

**Types:**
- No custom classes or dataclasses are used in the Python source. Prefer NumPy arrays, pandas DataFrames, dictionaries, and tuples as the current style in `TRC-23-02333/transparent_estimator_eval.py`.
- Preserve integer sensor indices explicitly by converting arrays with `np.asarray(..., dtype=int)` or `np.array(..., dtype=int)`, as in `make_rcss_row`, `coverage_layout`, and `greedy_posterior_layout` in `TRC-23-02333/transparent_estimator_eval.py`.
- Serialize experiment records as dictionaries with primitive JSON-compatible values before writing: `layout_records`, `swap_records`, and `rcss_records` in `TRC-23-02333/transparent_estimator_eval.py`.

## Code Style

**Formatting:**
- No formatter configuration is detected. There is no `.prettierrc`, `pyproject.toml`, `setup.cfg`, `ruff.toml`, `.flake8`, or `pytest.ini` in `/home/samuel/projects/sensor_opt`.
- Follow the existing Python style: 4-space indentation, blank lines between top-level functions, no semicolons, and line continuations using parentheses for long expressions.
- Use f-strings for user-facing errors and generated summary lines: `raise FileNotFoundError(f"Expected tensor.npz and Loop_Seattle_2015_A.npy under {data_root}")` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep numerical constants close to the functions that need them unless globally meaningful. `SLOTS_PER_DAY = 288` is the only module-level constant in `TRC-23-02333/transparent_estimator_eval.py`.

**Linting:**
- No linting tool configuration is detected in `/home/samuel/projects/sensor_opt`.
- Write code that remains compatible with standard Python style conventions: no unused imports, no wildcard imports, deterministic CLI parsing, and explicit exceptions.
- Prefer simple functions over nested class hierarchies. The current codebase is functional script-oriented in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.

## Import Organization

**Order:**
1. Python standard library imports first: `argparse`, `json`, `math`, `pathlib.Path` in `TRC-23-02333/transparent_estimator_eval.py`.
2. Third-party scientific imports second: `numpy`, `pandas`, `scipy`, `sklearn` in `TRC-23-02333/transparent_estimator_eval.py`.
3. No local package imports are used because the research scripts are standalone files in `TRC-23-02333/`.

**Path Aliases:**
- Not detected. There is no package-level alias configuration in `/home/samuel/projects/sensor_opt`.
- Use `Path(__file__).resolve().parent` for paths relative to a script location when defaults must be stable, as in the default dataset path in `TRC-23-02333/transparent_estimator_eval.py`.
- Use shell variables for experiment root paths in launchers, as in `DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_228}"` in `scripts/run_stage11_pems7_228.sh`.

## Error Handling

**Patterns:**
- Validate required input files before loading and raise clear exceptions. `load_seattle_dataset` raises `FileNotFoundError` when `tensor.npz` or `Loop_Seattle_2015_A.npy` is missing in `TRC-23-02333/transparent_estimator_eval.py`.
- Validate input shapes and unsupported options with `ValueError`. `load_seattle_dataset` checks tensor dimensionality, `greedy_posterior_layout` rejects unsupported objectives, and `parse_weight_grid` rejects invalid RCSS weight grids in `TRC-23-02333/transparent_estimator_eval.py`.
- Use `SystemExit` for CLI-level absence of expected experiment outputs. `TRC-23-02333/summarize_trace_sl_rcss.py` raises `SystemExit` when no `seed_*/metrics.csv` files are found.
- Prefer fail-fast behavior in shell launchers with `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Use numeric safeguards around divisions and matrix operations: `std = train.std(axis=0) + 1e-6`, `denom = np.maximum(np.abs(true), 1e-6)`, and covariance regularization with `1e-6 * np.eye(n_nodes)` in `TRC-23-02333/transparent_estimator_eval.py`.

## Logging

**Framework:** console

**Patterns:**
- Use `print()` for terminal summaries at the end of CLI scripts: grouped metrics and output directory messages in `TRC-23-02333/transparent_estimator_eval.py`; layout summary and summary path in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Shell launchers pipe experiment output through `tee` to per-seed log files: `2>&1 | tee "${OUTPUT_DIR}_seed_${seed}.log"` in `scripts/run_stage11_pems7_228.sh` and `scripts/run_stage11_seattle.sh`.
- Do not introduce structured logging unless the CLI surface is intentionally changed. Existing downstream artifacts rely on CSV/JSON/Markdown outputs rather than log parsing.

## Comments

**When to Comment:**
- Comments are sparse in the current source. Prefer self-documenting function names and explicit variable names over inline comments in `TRC-23-02333/transparent_estimator_eval.py`.
- Add comments only for non-obvious algorithmic choices, numerical stability decisions, or experiment-design assumptions. Keep comments adjacent to the matrix/statistical operation they explain.
- Do not duplicate CLI argument names or straightforward pandas/NumPy transformations in comments.

**JSDoc/TSDoc:**
- Not applicable. The repository contains Python and shell research scripts, not TypeScript.
- Python docstrings are not currently used. If adding reusable library-like functions, prefer concise docstrings that state inputs, outputs, and shape assumptions.

## Function Design

**Size:**
- Prefer small pure functions for numerical primitives, dataset loaders, layout heuristics, metrics, and serialization helpers. Examples include `metrics`, `make_laplacian`, `posterior_trace_for_layout`, and `coverage_penalty` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep orchestration in `main()` for CLI scripts. `main()` in `TRC-23-02333/transparent_estimator_eval.py` owns argument parsing, experiment loops, artifact writing, and final console output.
- When adding new algorithms, place the algorithm as a top-level function near related layout/selection helpers in `TRC-23-02333/transparent_estimator_eval.py`, then call it from `main()` under an explicit CLI flag.

**Parameters:**
- Pass arrays and configuration explicitly rather than relying on module globals. Existing functions pass `train`, `val`, `test`, `distance`, `laplacian`, `precision`, `mean`, `std`, `sensors`, and `args` explicitly in `TRC-23-02333/transparent_estimator_eval.py`.
- Use `args` for CLI-tunable experiment parameters, but keep core data arrays as separate parameters so functions remain testable.
- Pass random number generators explicitly for stochastic logic. `quality_coverage_sample` accepts `rng`, and `main()` creates `rng = np.random.default_rng(args.layout_seed)` in `TRC-23-02333/transparent_estimator_eval.py`.

**Return Values:**
- Return NumPy arrays for selected sensor layouts: `greedy_posterior_layout`, `scenario_greedy_layout`, `coverage_layout`, `quality_coverage_sample`, and `swap_trace_local_search` in `TRC-23-02333/transparent_estimator_eval.py`.
- Return dictionaries for metrics and certificates: `metrics` and `certificate` in `TRC-23-02333/transparent_estimator_eval.py`.
- Return tuples when a function naturally produces several artifacts, but keep tuple order stable and unpack immediately at call sites. Examples: `load_pems_dataset`, `evaluate_layout`, `select_auto_rcss_weights`, and `validation_swap_search` in `TRC-23-02333/transparent_estimator_eval.py`.

## Module Design

**Exports:**
- There are no package exports or public APIs. Treat `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` as executable research scripts with importable helper functions.
- Keep side effects inside `main()` or explicit writer functions such as `write_summary` in `TRC-23-02333/transparent_estimator_eval.py` and summary writing in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Avoid top-level computation beyond constants and imports. Both Python scripts defer execution to `main()` guards.

**Barrel Files:**
- Not used. There is no Python package directory with `__init__.py` exports in `/home/samuel/projects/sensor_opt`.
- Do not add barrel-style import files unless the codebase is reorganized into a package with tests and reusable modules.

## Research Artifact Conventions

**Outputs:**
- Write machine-readable outputs as CSV and JSON before Markdown summaries. `TRC-23-02333/transparent_estimator_eval.py` writes `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, and `config.json`.
- Include experiment configuration in output artifacts. `config.json` in `TRC-23-02333/transparent_estimator_eval.py` records CLI args, validation/test days, scenario day indices, and data shapes.
- Use Markdown summaries for human-readable reports generated from the same in-memory rows, not as the only result source. `write_summary` in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` follow this pattern.

**Reproducibility:**
- Keep split and layout randomness separate. Use `--split-seed` for data splits and `--layout-seed` for layout sampling in `TRC-23-02333/transparent_estimator_eval.py`.
- Shell launchers should expose all experiment-scale knobs through environment variables with defaults, as in `scripts/run_stage11_pems7_228.sh`.
- Set BLAS/threading environment variables in shell launchers before running Python to keep CPU experiments reproducible and resource-bounded: `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS` in `scripts/run_stage11_pems7_228.sh`.

## Project Skills

- No `.claude/skills/` or `.agents/skills/` directory was detected in `/home/samuel/projects/sensor_opt`.
- No project-specific skill rules are available beyond repository files and the conventions documented here.

---

*Convention analysis: 2026/05/21*
