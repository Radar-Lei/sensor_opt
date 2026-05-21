<!-- GSD:project-start source:PROJECT.md -->
## Project

**TRACE-SL Transportation Science Readiness**

TRACE-SL is a research project on sparse traffic sensor placement for full-network traffic state reconstruction. The current codebase already contains a strong experimental prototype built around transparent GLS/MAP and GSP reconstruction, OR-guided candidate generation, posterior/certification diagnostics, RCSS selection, and validation-aware swap refinement. This project will turn that prototype into a Transportation Science-ready methodology paper, with TR Part B: Methodological kept as a higher-risk backup path if stronger theory and algorithmic analysis are completed.

**Core Value:** Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

### Constraints

- **Target venue:** Transportation Science is the primary submission target — it best matches transportation system design, optimization, computational experiments, and data-driven planning.
- **Backup venue:** TR Part B is possible only if the project adds stronger mathematical modeling, posterior-error theory, algorithmic properties, and generality beyond PeMS tuning.
- **Claim strategy:** Strong claims should be preserved and strengthened with evidence rather than narrowed prematurely — unsupported claims must be rephrased, tested, or moved to limitations.
- **Evidence standard:** Core claims must be supported by held-out test results, paired comparisons, statistical uncertainty, robustness checks, and reproducible artifacts.
- **Reproducibility:** Raw datasets stay local and ignored; curated result summaries, scripts, and non-sensitive artifacts should remain synchronized with paper claims.
- **Implementation state:** The current evaluator is monolithic and experiment-driven; changes should avoid breaking reproducibility and should be validated with smoke runs or aggregate checks.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->
## Technology Stack

## Languages
- Python 3.12.3 - Research/ML experiment driver and result aggregation in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Bash - Reproduction launchers and environment/thread controls in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Markdown - Research handoff and reproducibility documentation in `README.md`, `RESEARCH_PIPELINE_REPORT.md`, `NARRATIVE_REPORT.md`, `MANIFEST.md`, and `TRC-23-02333/trace_sl_results/README.md`.
- CSV/JSON - Experiment inputs and outputs under `TRC-23-02333/dataset/` and `TRC-23-02333/trace_sl_results/`.
## Runtime
- CPython 3.12.3 - Current local runtime detected with `python --version`; code uses Python standard library modules `argparse`, `json`, `math`, and `pathlib` in `TRC-23-02333/transparent_estimator_eval.py`.
- POSIX shell environment - Stage scripts use `#!/usr/bin/env bash` and `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- pip 24.0 - Installation path documented in `README.md` with `pip install -r requirements.txt`.
- Lockfile: missing - `requirements.txt` lists package names only and does not pin versions.
## Frameworks
- NumPy - Vectorized numerical arrays, random layout sampling, `.npy`/`.npz` dataset loading, matrix operations, and JSON-serializable experiment records in `TRC-23-02333/transparent_estimator_eval.py`.
- pandas - CSV dataset loading, datetime indexing, metric aggregation, and result writing in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- SciPy - Dense linear algebra (`scipy.linalg`), graph shortest paths (`scipy.sparse.csgraph.shortest_path`), and statistical tests/correlations (`scipy.stats`) in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- scikit-learn - Ledoit-Wolf covariance shrinkage via `sklearn.covariance.LedoitWolf` in `TRC-23-02333/transparent_estimator_eval.py`.
- Not detected - No pytest/unittest configuration or test dependencies were detected in `requirements.txt`; validation is currently experiment-driven through stage scripts and generated summaries in `TRC-23-02333/trace_sl_results/`.
- Bash stage launchers - Reproduce Stage 11 experiments with `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Python CLI scripts - Main runnable modules are `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- No build system detected - No `pyproject.toml`, `setup.py`, `Makefile`, Dockerfile, or CI configuration was detected at the repository root.
## Key Dependencies
- `numpy` - Required for traffic tensors, sensor-index arrays, posterior inverse updates, random candidate generation, and `.npy`/`.npz` Seattle loading in `TRC-23-02333/transparent_estimator_eval.py`.
- `pandas` - Required for PeMS CSV loading, date-based train/validation/test splits, experiment metric tables, and summary CSV outputs in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- `scipy` - Required for GLS/GSP solves, graph distances, paired t-tests, Wilcoxon tests, and certificate-error correlations in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- `scikit-learn` - Required for `LedoitWolf` covariance estimation used to build GLS precision matrices and robust scenario matrices in `TRC-23-02333/transparent_estimator_eval.py`.
- `requirements.txt` - Minimal dependency manifest containing `numpy`, `pandas`, `scipy`, and `scikit-learn`.
- BLAS/OpenMP thread variables - Reproduction scripts export `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh` to avoid oversubscription during parallel numerical work.
- Local artifact directories - Curated results are stored in `TRC-23-02333/trace_sl_results/`; large datasets are stored locally under `TRC-23-02333/dataset/` and ignored by Git via `.gitignore`.
## Configuration
- Configure a Python virtual environment as documented in `README.md`: create `.venv`, activate it, then run `pip install -r requirements.txt`.
- Stage scripts accept shell environment overrides before execution: `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, `NUM_LAYOUTS`, `RCSS_RANDOM_CANDIDATES`, `RCSS_QUALITY_CANDIDATES`, `SCENARIO_COUNT`, `VALIDATION_SWAP_STARTS`, `VALIDATION_SWAP_ITER`, `VALIDATION_SWAP_ADD_POOL`, `VALIDATION_SWAP_REMOVE_POOL`, and `THREADS_PER_JOB` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- `TRC-23-02333/transparent_estimator_eval.py` exposes CLI flags for dataset paths, budgets, random seeds, estimator settings, RCSS scoring weights, GSP/GLS hyperparameters, validation swap settings, and output directories.
- No `.env` files detected at repository root; secrets are not part of the runtime configuration.
- `requirements.txt` is the only dependency configuration file detected.
- `.gitignore` preserves reproducibility assets while ignoring large local datasets under `TRC-23-02333/dataset/` and local output/model artifacts such as `checkpoint.pth`, `checkpoints/`, `results/`, `test_results/`, `train_results/`, and `vali_results/`.
- `README.md` documents expected PeMS dataset placement and reproduction commands.
- `TRC-23-02333/trace_sl_results/README.md` documents the committed result-stage inventory and the current main method (`validation_swap_selected`).
## Platform Requirements
- Linux/POSIX shell environment for Bash stage scripts in `scripts/`.
- Python 3.12-compatible numerical environment with NumPy, pandas, SciPy, and scikit-learn installed from `requirements.txt`.
- Local PeMS datasets placed at `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv`, `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`, `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv`, and `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv` as documented in `README.md`.
- Local Seattle heterogeneous-network files placed under `TRC-23-02333/dataset/Seattle/`, including `tensor.npz` and `Loop_Seattle_2015_A.npy`, as required by `load_seattle_dataset` in `TRC-23-02333/transparent_estimator_eval.py`.
- Sufficient CPU/RAM for dense matrix inversion, covariance estimation, candidate scoring, and repeated validation evaluations in `TRC-23-02333/transparent_estimator_eval.py`; scripts default to `THREADS_PER_JOB=1` to control BLAS threading.
- Not applicable - This is a local research/ML experimentation repository with no service runtime, server entry point, container deployment, or cloud hosting configuration detected.
- Reproducibility target is local batch execution through `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`, writing artifacts to `TRC-23-02333/trace_sl_results/`.
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

## Naming Patterns
- Use lower_snake_case for Python research scripts: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Use `run_stage{N}_{dataset}.sh` naming for reproducible experiment launchers: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`.
- Keep dataset/result directory names aligned with paper or experiment labels: `TRC-23-02333/dataset/PeMS7_228`, `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight`.
- Use lower_snake_case verbs/nouns for pure computation and data-loading functions: `parse_budgets`, `split_daily_frame`, `load_pems_dataset`, `greedy_posterior_layout`, `validation_swap_search` in `TRC-23-02333/transparent_estimator_eval.py`.
- Prefer explicit domain terms in function names. Use suffixes such as `_layout`, `_predict`, `_for_layout`, `_candidate`, `_summary` to show output semantics: `coverage_layout`, `neighbor_average_predict`, `posterior_trace_for_layout`, `select_rcss_candidate`, `write_summary` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep command-line scripts with a single `main()` entry point and `if __name__ == "__main__": main()` guard: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Use lower_snake_case for local variables and CLI-derived fields: `data_root`, `output_dir`, `split_seed`, `layout_seed`, `sensor_count`, `scenario_matrices` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use short mathematical names only for established matrix/vector quantities: `lhs`, `rhs`, `tod`, `rng`, `gls_z`, `gsp_lhs` in `TRC-23-02333/transparent_estimator_eval.py`.
- Use plural names for collections and row lists: `metrics`, `correlations`, `rcss_candidates`, `paired_rows` in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Shell scripts use uppercase environment-variable names with defaults: `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, `THREADS_PER_JOB` in `scripts/run_stage11_pems7_228.sh` and `scripts/run_stage11_seattle.sh`.
- No custom classes or dataclasses are used in the Python source. Prefer NumPy arrays, pandas DataFrames, dictionaries, and tuples as the current style in `TRC-23-02333/transparent_estimator_eval.py`.
- Preserve integer sensor indices explicitly by converting arrays with `np.asarray(..., dtype=int)` or `np.array(..., dtype=int)`, as in `make_rcss_row`, `coverage_layout`, and `greedy_posterior_layout` in `TRC-23-02333/transparent_estimator_eval.py`.
- Serialize experiment records as dictionaries with primitive JSON-compatible values before writing: `layout_records`, `swap_records`, and `rcss_records` in `TRC-23-02333/transparent_estimator_eval.py`.
## Code Style
- No formatter configuration is detected. There is no `.prettierrc`, `pyproject.toml`, `setup.cfg`, `ruff.toml`, `.flake8`, or `pytest.ini` in `/home/samuel/projects/sensor_opt`.
- Follow the existing Python style: 4-space indentation, blank lines between top-level functions, no semicolons, and line continuations using parentheses for long expressions.
- Use f-strings for user-facing errors and generated summary lines: `raise FileNotFoundError(f"Expected tensor.npz and Loop_Seattle_2015_A.npy under {data_root}")` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep numerical constants close to the functions that need them unless globally meaningful. `SLOTS_PER_DAY = 288` is the only module-level constant in `TRC-23-02333/transparent_estimator_eval.py`.
- No linting tool configuration is detected in `/home/samuel/projects/sensor_opt`.
- Write code that remains compatible with standard Python style conventions: no unused imports, no wildcard imports, deterministic CLI parsing, and explicit exceptions.
- Prefer simple functions over nested class hierarchies. The current codebase is functional script-oriented in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
## Import Organization
- Not detected. There is no package-level alias configuration in `/home/samuel/projects/sensor_opt`.
- Use `Path(__file__).resolve().parent` for paths relative to a script location when defaults must be stable, as in the default dataset path in `TRC-23-02333/transparent_estimator_eval.py`.
- Use shell variables for experiment root paths in launchers, as in `DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_228}"` in `scripts/run_stage11_pems7_228.sh`.
## Error Handling
- Validate required input files before loading and raise clear exceptions. `load_seattle_dataset` raises `FileNotFoundError` when `tensor.npz` or `Loop_Seattle_2015_A.npy` is missing in `TRC-23-02333/transparent_estimator_eval.py`.
- Validate input shapes and unsupported options with `ValueError`. `load_seattle_dataset` checks tensor dimensionality, `greedy_posterior_layout` rejects unsupported objectives, and `parse_weight_grid` rejects invalid RCSS weight grids in `TRC-23-02333/transparent_estimator_eval.py`.
- Use `SystemExit` for CLI-level absence of expected experiment outputs. `TRC-23-02333/summarize_trace_sl_rcss.py` raises `SystemExit` when no `seed_*/metrics.csv` files are found.
- Prefer fail-fast behavior in shell launchers with `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Use numeric safeguards around divisions and matrix operations: `std = train.std(axis=0) + 1e-6`, `denom = np.maximum(np.abs(true), 1e-6)`, and covariance regularization with `1e-6 * np.eye(n_nodes)` in `TRC-23-02333/transparent_estimator_eval.py`.
## Logging
- Use `print()` for terminal summaries at the end of CLI scripts: grouped metrics and output directory messages in `TRC-23-02333/transparent_estimator_eval.py`; layout summary and summary path in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Shell launchers pipe experiment output through `tee` to per-seed log files: `2>&1 | tee "${OUTPUT_DIR}_seed_${seed}.log"` in `scripts/run_stage11_pems7_228.sh` and `scripts/run_stage11_seattle.sh`.
- Do not introduce structured logging unless the CLI surface is intentionally changed. Existing downstream artifacts rely on CSV/JSON/Markdown outputs rather than log parsing.
## Comments
- Comments are sparse in the current source. Prefer self-documenting function names and explicit variable names over inline comments in `TRC-23-02333/transparent_estimator_eval.py`.
- Add comments only for non-obvious algorithmic choices, numerical stability decisions, or experiment-design assumptions. Keep comments adjacent to the matrix/statistical operation they explain.
- Do not duplicate CLI argument names or straightforward pandas/NumPy transformations in comments.
- Not applicable. The repository contains Python and shell research scripts, not TypeScript.
- Python docstrings are not currently used. If adding reusable library-like functions, prefer concise docstrings that state inputs, outputs, and shape assumptions.
## Function Design
- Prefer small pure functions for numerical primitives, dataset loaders, layout heuristics, metrics, and serialization helpers. Examples include `metrics`, `make_laplacian`, `posterior_trace_for_layout`, and `coverage_penalty` in `TRC-23-02333/transparent_estimator_eval.py`.
- Keep orchestration in `main()` for CLI scripts. `main()` in `TRC-23-02333/transparent_estimator_eval.py` owns argument parsing, experiment loops, artifact writing, and final console output.
- When adding new algorithms, place the algorithm as a top-level function near related layout/selection helpers in `TRC-23-02333/transparent_estimator_eval.py`, then call it from `main()` under an explicit CLI flag.
- Pass arrays and configuration explicitly rather than relying on module globals. Existing functions pass `train`, `val`, `test`, `distance`, `laplacian`, `precision`, `mean`, `std`, `sensors`, and `args` explicitly in `TRC-23-02333/transparent_estimator_eval.py`.
- Use `args` for CLI-tunable experiment parameters, but keep core data arrays as separate parameters so functions remain testable.
- Pass random number generators explicitly for stochastic logic. `quality_coverage_sample` accepts `rng`, and `main()` creates `rng = np.random.default_rng(args.layout_seed)` in `TRC-23-02333/transparent_estimator_eval.py`.
- Return NumPy arrays for selected sensor layouts: `greedy_posterior_layout`, `scenario_greedy_layout`, `coverage_layout`, `quality_coverage_sample`, and `swap_trace_local_search` in `TRC-23-02333/transparent_estimator_eval.py`.
- Return dictionaries for metrics and certificates: `metrics` and `certificate` in `TRC-23-02333/transparent_estimator_eval.py`.
- Return tuples when a function naturally produces several artifacts, but keep tuple order stable and unpack immediately at call sites. Examples: `load_pems_dataset`, `evaluate_layout`, `select_auto_rcss_weights`, and `validation_swap_search` in `TRC-23-02333/transparent_estimator_eval.py`.
## Module Design
- There are no package exports or public APIs. Treat `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` as executable research scripts with importable helper functions.
- Keep side effects inside `main()` or explicit writer functions such as `write_summary` in `TRC-23-02333/transparent_estimator_eval.py` and summary writing in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Avoid top-level computation beyond constants and imports. Both Python scripts defer execution to `main()` guards.
- Not used. There is no Python package directory with `__init__.py` exports in `/home/samuel/projects/sensor_opt`.
- Do not add barrel-style import files unless the codebase is reorganized into a package with tests and reusable modules.
## Research Artifact Conventions
- Write machine-readable outputs as CSV and JSON before Markdown summaries. `TRC-23-02333/transparent_estimator_eval.py` writes `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, and `config.json`.
- Include experiment configuration in output artifacts. `config.json` in `TRC-23-02333/transparent_estimator_eval.py` records CLI args, validation/test days, scenario day indices, and data shapes.
- Use Markdown summaries for human-readable reports generated from the same in-memory rows, not as the only result source. `write_summary` in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` follow this pattern.
- Keep split and layout randomness separate. Use `--split-seed` for data splits and `--layout-seed` for layout sampling in `TRC-23-02333/transparent_estimator_eval.py`.
- Shell launchers should expose all experiment-scale knobs through environment variables with defaults, as in `scripts/run_stage11_pems7_228.sh`.
- Set BLAS/threading environment variables in shell launchers before running Python to keep CPU experiments reproducible and resource-bounded: `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS` in `scripts/run_stage11_pems7_228.sh`.
## Project Skills
- No `.claude/skills/` or `.agents/skills/` directory was detected in `/home/samuel/projects/sensor_opt`.
- No project-specific skill rules are available beyond repository files and the conventions documented here.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

## System Overview
```text
```
## Component Responsibilities
| Component | Responsibility | File |
|-----------|----------------|------|
| Stage 11 PeMS7_228 launcher | Defines default data root, output root, seeds, budgets, candidate counts, BLAS thread caps, and evaluator flags for the main in-domain TRACE-SL run. | `scripts/run_stage11_pems7_228.sh` |
| Stage 11 PeMS7_1026 launcher | Runs the same Stage 11 pipeline on the larger PeMS7_1026 dataset with lighter default candidate counts. | `scripts/run_stage11_pems7_1026.sh` |
| Stage 11 Seattle launcher | Runs the Stage 11 pipeline against the Seattle tensor/adjacency format. | `scripts/run_stage11_seattle.sh` |
| Dataset loaders | Auto-detect PeMS CSV value/distance files or Seattle tensor/adjacency files, convert them into train/validation/test arrays, and return graph distances. | `TRC-23-02333/transparent_estimator_eval.py` |
| Reconstruction evaluators | Evaluate historical time-of-day mean, neighbor average, GSP, and GLS/MAP reconstruction on hidden nodes. | `TRC-23-02333/transparent_estimator_eval.py` |
| Layout generators | Build random, degree, top-variance, coverage, greedy posterior, scenario-greedy, robust coverage/CVaR, trace-swap, and validation-swap layouts. | `TRC-23-02333/transparent_estimator_eval.py` |
| RCSS selector | Scores candidate layouts using validation MAE, posterior trace, scenario CVaR trace, condition number, and coverage penalty; optionally selects score weights using an inner validation split. | `TRC-23-02333/transparent_estimator_eval.py` |
| Result writer | Emits per-seed `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, `config.json`, and `SUMMARY.md`. | `TRC-23-02333/transparent_estimator_eval.py` |
| Multi-split summarizer | Combines `seed_*/metrics.csv`, candidate files, and certificate correlations into aggregate CSVs and a human-readable `SUMMARY.md`. | `TRC-23-02333/summarize_trace_sl_rcss.py` |
| Curated evidence store | Stores committed Stage 6--11 TRACE-SL result artifacts and aggregate tables. | `TRC-23-02333/trace_sl_results/` |
| Research context | Provides method framing, claim status, and reproducibility instructions for the current TRACE-SL evidence. | `README.md`, `NARRATIVE_REPORT.md`, `RESEARCH_PIPELINE_REPORT.md`, `refine-logs/` |
## Pattern Overview
- Use CLI arguments as the boundary between run configuration and experiment logic in `TRC-23-02333/transparent_estimator_eval.py`.
- Use deterministic split/layout seeds from shell scripts such as `scripts/run_stage11_pems7_228.sh` to make runs reproducible.
- Keep datasets in ignored local directories under `TRC-23-02333/dataset/` while committing curated result summaries under `TRC-23-02333/trace_sl_results/`.
- Write evidence as plain CSV/JSON/Markdown artifacts rather than through a database or service layer.
- Keep current method code in a single import-free local module; helper functions communicate through NumPy arrays, pandas frames, and argparse namespaces.
## Layers
- Purpose: Define experiment defaults, control computational thread count, run all split seeds, and invoke aggregation.
- Location: `scripts/`
- Contains: Bash launchers `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Depends on: Python entry points in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Used by: Humans and automation reproducing Stage 11 experiments from `README.md`.
- Purpose: Load traffic speed/value matrices and graph distances, impute Seattle missing values, and split days into train/validation/test partitions.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `load_pems_dataset`, `load_seattle_dataset`, `split_daily_frame`, and `adjacency_to_distance`.
- Depends on: Local files in `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, and `TRC-23-02333/dataset/Seattle/`.
- Used by: The evaluator `main()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Purpose: Standardize training data, compute time-of-day priors, graph Laplacians, Ledoit-Wolf covariance estimates, precision matrices, and scenario matrices.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `time_of_day_mean`, `make_similarity`, `make_laplacian`, `build_scenario_matrices`, and setup logic in `main()`.
- Depends on: `numpy`, `pandas`, `scipy.linalg`, `scipy.sparse.csgraph.shortest_path`, and `sklearn.covariance.LedoitWolf`.
- Used by: Reconstruction, layout generation, RCSS scoring, and validation swap logic in `TRC-23-02333/transparent_estimator_eval.py`.
- Purpose: Estimate hidden-node traffic values from selected sensor nodes and compute MAE/RMSE/MAPE plus numerical certificates.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `historical_mean_predict`, `neighbor_average_predict`, `solve_quadratic`, `certificate`, `metrics`, `evaluate_layout`, and `summarize_correlations`.
- Depends on: Train-derived priors, graph distances, graph Laplacian, precision matrix, selected sensor arrays, and CLI weights.
- Used by: `validation_mae`, `make_rcss_row`, the per-layout evaluation loop, and summary writing in `TRC-23-02333/transparent_estimator_eval.py`.
- Purpose: Generate candidate sensor sets for random baselines, topology baselines, posterior-greedy objectives, scenario/CVaR objectives, trace swap refinement, RCSS candidate pools, and validation-aware swaps.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `greedy_posterior_layout`, `scenario_greedy_layout`, `degree_layout`, `top_variance_layout`, `coverage_layout`, `quality_coverage_sample`, `robust_coverage_cvar_layout`, `swap_trace_local_search`, and `validation_swap_search`.
- Depends on: GLS posterior matrices, scenario matrices, graph distances, validation reconstruction MAE, and deterministic NumPy RNG.
- Used by: The budget loop in `main()`.
- Purpose: Deduplicate candidates, compute validation/certificate/coverage diagnostics, normalize scores, select candidates, and tune score weights with an inner validation split.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `normalize_minmax`, `coverage_penalty`, `posterior_*_for_layout`, `scenario_cvar_trace_for_layout`, `parse_weight_grid`, `rcss_candidate_scores`, `make_rcss_row`, `build_rcss_rows`, `select_rcss_candidate`, and `select_auto_rcss_weights`.
- Depends on: Candidate layouts from the search layer and validation/test arrays from the data layer.
- Used by: `--include-rcss`, `--rcss-auto-weights`, and `--include-validation-swap` branches in `main()`.
- Purpose: Persist reproducibility artifacts per split and aggregate them across splits.
- Location: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/trace_sl_results/`
- Contains: CSV, JSON, Markdown summaries, seed logs, and aggregate result directories.
- Depends on: pandas DataFrames, JSON serialization, and local filesystem paths.
- Used by: `README.md`, `TRC-23-02333/trace_sl_results/README.md`, and paper-writing handoff documents.
- Purpose: Preserve method framing, experiment plans, reports, and ARIS pipeline outputs.
- Location: `README.md`, `MANIFEST.md`, `NARRATIVE_REPORT.md`, `RESEARCH_PIPELINE_REPORT.md`, `idea-stage/`, `refine-logs/`
- Contains: Markdown reports and timestamped research artifacts.
- Depends on: Generated outputs in `TRC-23-02333/trace_sl_results/`.
- Used by: Planning, writing, and claim-tracking workflows.
## Data Flow
### Primary Stage 11 Request Path
### Dataset Loading Flow
### RCSS Candidate Selection Flow
### Multi-Split Aggregation Flow
- State is local to each process in `TRC-23-02333/transparent_estimator_eval.py`; data moves through arrays, dictionaries, pandas DataFrames, and argparse `args`.
- Randomness is controlled by `np.random.default_rng(args.layout_seed)` for layouts and `np.random.default_rng(seed)` for split selection in `TRC-23-02333/transparent_estimator_eval.py`.
- No persistent in-memory services, databases, caches, or global mutable state are used beyond the constant `SLOTS_PER_DAY` in `TRC-23-02333/transparent_estimator_eval.py`.
- Filesystem output under `TRC-23-02333/trace_sl_results/` is the durable state boundary.
## Key Abstractions
- Purpose: Represent train/validation/test traffic measurements plus graph distances and split dates.
- Examples: `load_pems_dataset()` and `load_seattle_dataset()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Return plain tuple `(train, val, test, test_index, distance, val_days, test_days)` consumed directly by `main()`.
- Purpose: Represent a selected subset of instrumented graph nodes for a budget.
- Examples: `greedy_posterior_layout()`, `coverage_layout()`, `robust_coverage_cvar_layout()`, and `validation_swap_search()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Use sorted NumPy integer arrays for computation and convert to Python lists for JSON/CSV output.
- Purpose: Store evaluation metrics and optional certificates for one method/layout/budget combination.
- Examples: `evaluate_layout()` rows and final `rows` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Build dictionaries with `method`, `mae`, `rmse`, `mape`, certificates, dataset, budget, split seed, and layout metadata.
- Purpose: Quantify uncertainty/conditioning of GSP and GLS/MAP systems for layout diagnostics.
- Examples: `certificate()`, `posterior_trace_for_layout()`, `posterior_condition_for_layout()`, `posterior_logdet_for_layout()`, and `scenario_cvar_trace_for_layout()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Compute numeric scalar features from posterior inverse or system matrix and correlate them with hidden-node MAE.
- Purpose: Represent one candidate layout with validation and certificate diagnostics for robust selection.
- Examples: `make_rcss_row()` and `rcss_candidate_scores()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Dictionary containing `source`, `layout_id`, `sensors`, `validation_mae`, `posterior_trace`, `scenario_cvar_trace`, `condition_number`, `coverage_penalty`, selected weights, and `rcss_score`.
- Purpose: Persist one seed run or aggregate evidence bundle.
- Examples: `metrics.csv`, `layouts.json`, `rcss_candidates.csv`, and `SUMMARY.md` written by `TRC-23-02333/transparent_estimator_eval.py`; `combined_metrics.csv` and `gls_map_layout_summary.csv` written by `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Pattern: Use flat files under `TRC-23-02333/trace_sl_results/<stage>/seed_<seed>/` and aggregate files under `TRC-23-02333/trace_sl_results/<stage>/`.
## Entry Points
- Location: `scripts/run_stage11_pems7_228.sh`
- Triggers: Shell execution from the repository root, as documented in `README.md`.
- Responsibilities: Run seeds `25 26 27 28 29` by default for `TRC-23-02333/dataset/PeMS7_228`, write per-seed outputs under `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/`, then aggregate them.
- Location: `scripts/run_stage11_pems7_1026.sh`
- Triggers: Shell execution from the repository root, as documented in `README.md`.
- Responsibilities: Run the same Stage 11 flags on `TRC-23-02333/dataset/PeMS7_1026` with default 100 random/RCSS candidates.
- Location: `scripts/run_stage11_seattle.sh`
- Triggers: Shell execution from the repository root.
- Responsibilities: Run the same Stage 11 flags on `TRC-23-02333/dataset/Seattle` with default 50 random/RCSS candidates.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Triggers: Direct `python TRC-23-02333/transparent_estimator_eval.py ...` invocation.
- Responsibilities: Load one dataset split, generate layouts for requested budgets, evaluate reconstruction methods, and write per-run artifacts.
- Location: `TRC-23-02333/summarize_trace_sl_rcss.py`
- Triggers: Direct `python TRC-23-02333/summarize_trace_sl_rcss.py --input-root ... --output-dir ...` invocation or launcher scripts.
- Responsibilities: Aggregate seed directories into combined metrics, deltas, tests, winner counts, certificate summaries, selected-source summaries, and Markdown summary.
## Architectural Constraints
- **Threading:** The Python code relies on NumPy/SciPy/scikit-learn BLAS backends. Shell launchers set `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS` to `THREADS_PER_JOB` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- **Global state:** The only module-level domain constant is `SLOTS_PER_DAY = 288` in `TRC-23-02333/transparent_estimator_eval.py`. Do not introduce mutable module-level experiment state; pass values through functions and CLI args.
- **Circular imports:** Not applicable. The Python implementation has two standalone scripts, and neither imports the other.
- **Working directory:** Shell launchers use repo-relative paths such as `TRC-23-02333/transparent_estimator_eval.py`; run them from `/home/samuel/projects/sensor_opt` or adapt paths explicitly.
- **Dataset availability:** `TRC-23-02333/dataset/` is ignored by `.gitignore` and must exist locally for full runs. Do not read or commit raw dataset contents unless the task explicitly requires data analysis.
- **Memory/scaling:** Posterior and precision operations use dense matrices and explicit inverses in `TRC-23-02333/transparent_estimator_eval.py`; candidate counts and validation-swap pool sizes should be tuned per dataset size.
- **Output ownership:** Curated reproducibility outputs live in `TRC-23-02333/trace_sl_results/`; ad hoc outputs should use a new subdirectory under that root and be reviewed against `.gitignore` before committing.
- **Project skills:** No `.claude/skills/` or `.agents/skills/` project skill directory is present in `/home/samuel/projects/sensor_opt`.
## Anti-Patterns
### Adding a New Pipeline as a Separate Copy of the Evaluator
### Writing Results Outside the TRACE-SL Artifact Tree
### Treating Validation MAE as Test Evidence
### Reading Dataset Files for Structural Tasks
## Error Handling
- Missing Seattle files raise `FileNotFoundError` in `load_seattle_dataset()` (`TRC-23-02333/transparent_estimator_eval.py:58`).
- Unexpected Seattle tensor shapes raise `ValueError` in `load_seattle_dataset()` (`TRC-23-02333/transparent_estimator_eval.py:66`).
- Unsupported greedy/scenario objectives raise `ValueError` in `greedy_posterior_layout()` and `scenario_greedy_layout()` (`TRC-23-02333/transparent_estimator_eval.py:167`, `TRC-23-02333/transparent_estimator_eval.py:205`).
- Empty RCSS candidate pools raise `ValueError` in `build_rcss_rows()` (`TRC-23-02333/transparent_estimator_eval.py:469`).
- Empty aggregate inputs raise `SystemExit` in `TRC-23-02333/summarize_trace_sl_rcss.py` (`TRC-23-02333/summarize_trace_sl_rcss.py:37`).
- Shell launchers stop on unset variables and failed commands through `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
## Cross-Cutting Concerns
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
