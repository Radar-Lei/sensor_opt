<!-- refreshed: 2026/05/21 -->
# Architecture

**Analysis Date:** 2026/05/21

## System Overview

```text
┌─────────────────────────────────────────────────────────────┐
│                  TRACE-SL CLI Experiment Layer               │
├──────────────────┬──────────────────┬───────────────────────┤
│  PeMS7_228 run   │  PeMS7_1026 run  │   Seattle run          │
│ `scripts/run_stage11_pems7_228.sh` │ `scripts/run_stage11_pems7_1026.sh` │ `scripts/run_stage11_seattle.sh` │
└────────┬─────────┴────────┬─────────┴──────────┬────────────┘
         │                  │                     │
         ▼                  ▼                     ▼
┌─────────────────────────────────────────────────────────────┐
│                Monolithic TRACE-SL Evaluator                 │
│        `TRC-23-02333/transparent_estimator_eval.py`          │
├─────────────────────────────────────────────────────────────┤
│ dataset loading → splitting → baselines → RCSS candidates →  │
│ validation/auto-weight selection → test evaluation → outputs │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│                 Result Aggregation and Evidence              │
│ `TRC-23-02333/summarize_trace_sl_rcss.py`                    │
│ `TRC-23-02333/trace_sl_results/`                             │
└─────────────────────────────────────────────────────────────┘
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

**Overall:** Script-oriented research pipeline with a monolithic numerical experiment driver and shell launchers.

**Key Characteristics:**
- Use CLI arguments as the boundary between run configuration and experiment logic in `TRC-23-02333/transparent_estimator_eval.py`.
- Use deterministic split/layout seeds from shell scripts such as `scripts/run_stage11_pems7_228.sh` to make runs reproducible.
- Keep datasets in ignored local directories under `TRC-23-02333/dataset/` while committing curated result summaries under `TRC-23-02333/trace_sl_results/`.
- Write evidence as plain CSV/JSON/Markdown artifacts rather than through a database or service layer.
- Keep current method code in a single import-free local module; helper functions communicate through NumPy arrays, pandas frames, and argparse namespaces.

## Layers

**Run Orchestration Layer:**
- Purpose: Define experiment defaults, control computational thread count, run all split seeds, and invoke aggregation.
- Location: `scripts/`
- Contains: Bash launchers `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Depends on: Python entry points in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Used by: Humans and automation reproducing Stage 11 experiments from `README.md`.

**Data Loading and Split Layer:**
- Purpose: Load traffic speed/value matrices and graph distances, impute Seattle missing values, and split days into train/validation/test partitions.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `load_pems_dataset`, `load_seattle_dataset`, `split_daily_frame`, and `adjacency_to_distance`.
- Depends on: Local files in `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, and `TRC-23-02333/dataset/Seattle/`.
- Used by: The evaluator `main()` in `TRC-23-02333/transparent_estimator_eval.py`.

**Preprocessing and Model Matrix Layer:**
- Purpose: Standardize training data, compute time-of-day priors, graph Laplacians, Ledoit-Wolf covariance estimates, precision matrices, and scenario matrices.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `time_of_day_mean`, `make_similarity`, `make_laplacian`, `build_scenario_matrices`, and setup logic in `main()`.
- Depends on: `numpy`, `pandas`, `scipy.linalg`, `scipy.sparse.csgraph.shortest_path`, and `sklearn.covariance.LedoitWolf`.
- Used by: Reconstruction, layout generation, RCSS scoring, and validation swap logic in `TRC-23-02333/transparent_estimator_eval.py`.

**Reconstruction Evaluation Layer:**
- Purpose: Estimate hidden-node traffic values from selected sensor nodes and compute MAE/RMSE/MAPE plus numerical certificates.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `historical_mean_predict`, `neighbor_average_predict`, `solve_quadratic`, `certificate`, `metrics`, `evaluate_layout`, and `summarize_correlations`.
- Depends on: Train-derived priors, graph distances, graph Laplacian, precision matrix, selected sensor arrays, and CLI weights.
- Used by: `validation_mae`, `make_rcss_row`, the per-layout evaluation loop, and summary writing in `TRC-23-02333/transparent_estimator_eval.py`.

**Sensor Layout Search Layer:**
- Purpose: Generate candidate sensor sets for random baselines, topology baselines, posterior-greedy objectives, scenario/CVaR objectives, trace swap refinement, RCSS candidate pools, and validation-aware swaps.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `greedy_posterior_layout`, `scenario_greedy_layout`, `degree_layout`, `top_variance_layout`, `coverage_layout`, `quality_coverage_sample`, `robust_coverage_cvar_layout`, `swap_trace_local_search`, and `validation_swap_search`.
- Depends on: GLS posterior matrices, scenario matrices, graph distances, validation reconstruction MAE, and deterministic NumPy RNG.
- Used by: The budget loop in `main()`.

**RCSS Selection Layer:**
- Purpose: Deduplicate candidates, compute validation/certificate/coverage diagnostics, normalize scores, select candidates, and tune score weights with an inner validation split.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `normalize_minmax`, `coverage_penalty`, `posterior_*_for_layout`, `scenario_cvar_trace_for_layout`, `parse_weight_grid`, `rcss_candidate_scores`, `make_rcss_row`, `build_rcss_rows`, `select_rcss_candidate`, and `select_auto_rcss_weights`.
- Depends on: Candidate layouts from the search layer and validation/test arrays from the data layer.
- Used by: `--include-rcss`, `--rcss-auto-weights`, and `--include-validation-swap` branches in `main()`.

**Artifact Output Layer:**
- Purpose: Persist reproducibility artifacts per split and aggregate them across splits.
- Location: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/trace_sl_results/`
- Contains: CSV, JSON, Markdown summaries, seed logs, and aggregate result directories.
- Depends on: pandas DataFrames, JSON serialization, and local filesystem paths.
- Used by: `README.md`, `TRC-23-02333/trace_sl_results/README.md`, and paper-writing handoff documents.

**Research Documentation Layer:**
- Purpose: Preserve method framing, experiment plans, reports, and ARIS pipeline outputs.
- Location: `README.md`, `MANIFEST.md`, `NARRATIVE_REPORT.md`, `RESEARCH_PIPELINE_REPORT.md`, `idea-stage/`, `refine-logs/`
- Contains: Markdown reports and timestamped research artifacts.
- Depends on: Generated outputs in `TRC-23-02333/trace_sl_results/`.
- Used by: Planning, writing, and claim-tracking workflows.

## Data Flow

### Primary Stage 11 Request Path

1. Run a launcher such as `scripts/run_stage11_pems7_228.sh`; the script sets `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, candidate counts, and BLAS thread environment variables (`scripts/run_stage11_pems7_228.sh:3`).
2. For each split seed, invoke `python TRC-23-02333/transparent_estimator_eval.py` with Stage 11 flags including `--include-simple-baselines`, `--include-greedy`, `--include-swap`, `--include-scenario-greedy`, `--include-rcss`, `--rcss-auto-weights`, and `--include-validation-swap` (`scripts/run_stage11_pems7_228.sh:25`).
3. Parse CLI arguments and budgets in `main()` (`TRC-23-02333/transparent_estimator_eval.py:697`).
4. Load PeMS CSVs or fall back to Seattle tensor loading via `load_pems_dataset()` (`TRC-23-02333/transparent_estimator_eval.py:81`).
5. Split days into train/validation/test arrays with `split_daily_frame()` (`TRC-23-02333/transparent_estimator_eval.py:20`).
6. Build standardized training data, time-of-day priors, graph Laplacian, Ledoit-Wolf precision matrix, scenario matrices, and GLS base matrix (`TRC-23-02333/transparent_estimator_eval.py:754`).
7. For each budget, create random layouts, validation-selected random layouts, trace-selected random layouts, optional simple baselines, greedy layouts, scenario-greedy layouts, trace-swap layouts, RCSS candidates, and validation-swap RCSS layouts (`TRC-23-02333/transparent_estimator_eval.py:770`).
8. Evaluate each layout on hidden nodes with `evaluate_layout()` for historical, neighbor average, GSP, and GLS/MAP methods (`TRC-23-02333/transparent_estimator_eval.py:599`).
9. Write per-seed metrics, layouts, swap history, RCSS candidates, certificate correlations, config, and `SUMMARY.md` to the requested output directory (`TRC-23-02333/transparent_estimator_eval.py:998`).
10. Aggregate seed outputs with `TRC-23-02333/summarize_trace_sl_rcss.py` and write combined summaries under the same output root (`scripts/run_stage11_pems7_228.sh:50`).

### Dataset Loading Flow

1. `load_pems_dataset()` looks for `PeMSD7_V_*.csv` and `PeMSD7_W_*.csv` under `--data-root` (`TRC-23-02333/transparent_estimator_eval.py:81`).
2. If both PeMS files exist, values become a timestamped pandas frame and distance comes from the PeMS W matrix (`TRC-23-02333/transparent_estimator_eval.py:87`).
3. If PeMS files are absent, `load_seattle_dataset()` expects `tensor.npz` and `Loop_Seattle_2015_A.npy` under `--data-root` (`TRC-23-02333/transparent_estimator_eval.py:58`).
4. Seattle adjacency is converted to shortest-path distance using `adjacency_to_distance()` (`TRC-23-02333/transparent_estimator_eval.py:46`).
5. Both loaders call `split_daily_frame()` and return train, validation, test, test index, distance, validation days, and test days (`TRC-23-02333/transparent_estimator_eval.py:20`).

### RCSS Candidate Selection Flow

1. Candidate pools start with validation-ranked random layouts, quality-coverage samples, topology baselines, posterior-greedy layouts, robust coverage/CVaR layout, scenario-greedy layouts, and trace-swap outputs (`TRC-23-02333/transparent_estimator_eval.py:859`).
2. `build_rcss_rows()` deduplicates sensor sets and builds diagnostics through `make_rcss_row()` (`TRC-23-02333/transparent_estimator_eval.py:469`).
3. `make_rcss_row()` records validation MAE, posterior trace, scenario CVaR trace, condition number, and coverage penalty for each candidate (`TRC-23-02333/transparent_estimator_eval.py:455`).
4. `select_auto_rcss_weights()` splits validation data into selector/tuner halves and searches the configured RCSS weight grid (`TRC-23-02333/transparent_estimator_eval.py:484`).
5. `rcss_candidate_scores()` min-max normalizes diagnostics and computes `rcss_score` (`TRC-23-02333/transparent_estimator_eval.py:424`).
6. Optional `validation_swap_search()` refines the best RCSS starts by swapping candidate nodes when validation MAE improves (`TRC-23-02333/transparent_estimator_eval.py:512`).
7. Selected RCSS and validation-swap layouts are evaluated on the held-out test split in the main budget loop (`TRC-23-02333/transparent_estimator_eval.py:967`).

### Multi-Split Aggregation Flow

1. `TRC-23-02333/summarize_trace_sl_rcss.py` accepts one or more `--input-root` directories and an `--output-dir` (`TRC-23-02333/summarize_trace_sl_rcss.py:7`).
2. It scans `seed_*/metrics.csv`, optional `certificate_correlations.csv`, and optional `rcss_candidates.csv` under every input root (`TRC-23-02333/summarize_trace_sl_rcss.py:20`).
3. It writes combined metrics and GLS/MAP layout summaries by budget/layout type (`TRC-23-02333/summarize_trace_sl_rcss.py:41`).
4. It computes RCSS deltas, paired tests, ablation summaries, per-split winners, certificate summaries, selected RCSS sources, and a Markdown summary (`TRC-23-02333/summarize_trace_sl_rcss.py:53`).

**State Management:**
- State is local to each process in `TRC-23-02333/transparent_estimator_eval.py`; data moves through arrays, dictionaries, pandas DataFrames, and argparse `args`.
- Randomness is controlled by `np.random.default_rng(args.layout_seed)` for layouts and `np.random.default_rng(seed)` for split selection in `TRC-23-02333/transparent_estimator_eval.py`.
- No persistent in-memory services, databases, caches, or global mutable state are used beyond the constant `SLOTS_PER_DAY` in `TRC-23-02333/transparent_estimator_eval.py`.
- Filesystem output under `TRC-23-02333/trace_sl_results/` is the durable state boundary.

## Key Abstractions

**Traffic Dataset Split:**
- Purpose: Represent train/validation/test traffic measurements plus graph distances and split dates.
- Examples: `load_pems_dataset()` and `load_seattle_dataset()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Return plain tuple `(train, val, test, test_index, distance, val_days, test_days)` consumed directly by `main()`.

**Sensor Layout:**
- Purpose: Represent a selected subset of instrumented graph nodes for a budget.
- Examples: `greedy_posterior_layout()`, `coverage_layout()`, `robust_coverage_cvar_layout()`, and `validation_swap_search()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Use sorted NumPy integer arrays for computation and convert to Python lists for JSON/CSV output.

**Reconstruction Method Row:**
- Purpose: Store evaluation metrics and optional certificates for one method/layout/budget combination.
- Examples: `evaluate_layout()` rows and final `rows` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Build dictionaries with `method`, `mae`, `rmse`, `mape`, certificates, dataset, budget, split seed, and layout metadata.

**Posterior Certificate:**
- Purpose: Quantify uncertainty/conditioning of GSP and GLS/MAP systems for layout diagnostics.
- Examples: `certificate()`, `posterior_trace_for_layout()`, `posterior_condition_for_layout()`, `posterior_logdet_for_layout()`, and `scenario_cvar_trace_for_layout()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Compute numeric scalar features from posterior inverse or system matrix and correlate them with hidden-node MAE.

**RCSS Candidate Row:**
- Purpose: Represent one candidate layout with validation and certificate diagnostics for robust selection.
- Examples: `make_rcss_row()` and `rcss_candidate_scores()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Dictionary containing `source`, `layout_id`, `sensors`, `validation_mae`, `posterior_trace`, `scenario_cvar_trace`, `condition_number`, `coverage_penalty`, selected weights, and `rcss_score`.

**Experiment Artifact Set:**
- Purpose: Persist one seed run or aggregate evidence bundle.
- Examples: `metrics.csv`, `layouts.json`, `rcss_candidates.csv`, and `SUMMARY.md` written by `TRC-23-02333/transparent_estimator_eval.py`; `combined_metrics.csv` and `gls_map_layout_summary.csv` written by `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Pattern: Use flat files under `TRC-23-02333/trace_sl_results/<stage>/seed_<seed>/` and aggregate files under `TRC-23-02333/trace_sl_results/<stage>/`.

## Entry Points

**PeMS7_228 Stage 11 run:**
- Location: `scripts/run_stage11_pems7_228.sh`
- Triggers: Shell execution from the repository root, as documented in `README.md`.
- Responsibilities: Run seeds `25 26 27 28 29` by default for `TRC-23-02333/dataset/PeMS7_228`, write per-seed outputs under `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/`, then aggregate them.

**PeMS7_1026 Stage 11 external validation:**
- Location: `scripts/run_stage11_pems7_1026.sh`
- Triggers: Shell execution from the repository root, as documented in `README.md`.
- Responsibilities: Run the same Stage 11 flags on `TRC-23-02333/dataset/PeMS7_1026` with default 100 random/RCSS candidates.

**Seattle Stage 11 run:**
- Location: `scripts/run_stage11_seattle.sh`
- Triggers: Shell execution from the repository root.
- Responsibilities: Run the same Stage 11 flags on `TRC-23-02333/dataset/Seattle` with default 50 random/RCSS candidates.

**Single-seed evaluator:**
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Triggers: Direct `python TRC-23-02333/transparent_estimator_eval.py ...` invocation.
- Responsibilities: Load one dataset split, generate layouts for requested budgets, evaluate reconstruction methods, and write per-run artifacts.

**Multi-split summarizer:**
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

**What happens:** A new experiment duplicates `TRC-23-02333/transparent_estimator_eval.py` and changes constants or candidate logic in a forked script.
**Why it's wrong:** The pipeline is already monolithic; copying it splits dataset loading, scoring, artifact schema, and summary behavior across multiple files.
**Do this instead:** Add a CLI flag or helper function in `TRC-23-02333/transparent_estimator_eval.py`, then wire it from a launcher in `scripts/`.

### Writing Results Outside the TRACE-SL Artifact Tree

**What happens:** A run writes outputs to an untracked ad hoc directory such as `results/` or a dataset directory.
**Why it's wrong:** `README.md` and `TRC-23-02333/trace_sl_results/README.md` point readers to `TRC-23-02333/trace_sl_results/`, and `.gitignore` is curated around that tree.
**Do this instead:** Use `--output-dir TRC-23-02333/trace_sl_results/<descriptive_stage>/seed_<seed>` for evaluator outputs and aggregate to `TRC-23-02333/trace_sl_results/<descriptive_stage>/`.

### Treating Validation MAE as Test Evidence

**What happens:** Candidate selection diagnostics from `validation_mae()` or `rcss_score` are reported as final performance.
**Why it's wrong:** The architecture separates validation-based layout selection from held-out test evaluation in `evaluate_layout()`.
**Do this instead:** Use final `metrics.csv`/`combined_metrics.csv` rows where `method == "gls_map"` and layout types such as `validation_swap_selected` are evaluated on `test` data.

### Reading Dataset Files for Structural Tasks

**What happens:** Mapping or planning tasks open large CSV/NPZ dataset contents under `TRC-23-02333/dataset/`.
**Why it's wrong:** Dataset files are large, ignored, and not needed to understand architecture; the loader code defines required schemas.
**Do this instead:** Inspect loader expectations in `TRC-23-02333/transparent_estimator_eval.py` and list dataset file presence only.

## Error Handling

**Strategy:** Fail fast with Python exceptions and shell `set -euo pipefail`; no retry, service recovery, or custom error hierarchy exists.

**Patterns:**
- Missing Seattle files raise `FileNotFoundError` in `load_seattle_dataset()` (`TRC-23-02333/transparent_estimator_eval.py:58`).
- Unexpected Seattle tensor shapes raise `ValueError` in `load_seattle_dataset()` (`TRC-23-02333/transparent_estimator_eval.py:66`).
- Unsupported greedy/scenario objectives raise `ValueError` in `greedy_posterior_layout()` and `scenario_greedy_layout()` (`TRC-23-02333/transparent_estimator_eval.py:167`, `TRC-23-02333/transparent_estimator_eval.py:205`).
- Empty RCSS candidate pools raise `ValueError` in `build_rcss_rows()` (`TRC-23-02333/transparent_estimator_eval.py:469`).
- Empty aggregate inputs raise `SystemExit` in `TRC-23-02333/summarize_trace_sl_rcss.py` (`TRC-23-02333/summarize_trace_sl_rcss.py:37`).
- Shell launchers stop on unset variables and failed commands through `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

## Cross-Cutting Concerns

**Logging:** Shell launchers pipe each seed's stdout/stderr through `tee` to seed logs such as `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_seed_25.log`. Python scripts print grouped metric tables and output locations from `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Validation:** Input validation is embedded in loaders, objective switches, RCSS grid parsing, and candidate availability checks in `TRC-23-02333/transparent_estimator_eval.py`; statistical validation is performed through held-out validation/test day splits and paired tests in `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Authentication:** Not applicable. The repository has no service authentication, API credentials, or network calls in the TRACE-SL execution path.

**Configuration:** Use CLI flags in `TRC-23-02333/transparent_estimator_eval.py` and environment-variable defaults in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Reproducibility:** Persist `config.json` per seed from `TRC-23-02333/transparent_estimator_eval.py`; use deterministic `--split-seed` and `--layout-seed`; aggregate seed directories with `TRC-23-02333/summarize_trace_sl_rcss.py`.

---

*Architecture analysis: 2026/05/21*
