<!-- refreshed: 2026/05/21 -->
# Architecture

**Analysis Date:** 2026/05/21

## System Overview

```text
┌─────────────────────────────────────────────────────────────┐
│                 Shell Reproduction Entry Points             │
├──────────────────┬──────────────────┬───────────────────────┤
│  PeMS7_228 run   │ PeMS7_1026 run   │    Seattle run        │
│ `scripts/run_stage11_pems7_228.sh` │ `scripts/run_stage11_pems7_1026.sh` │ `scripts/run_stage11_seattle.sh` │
└────────┬─────────┴────────┬─────────┴──────────┬────────────┘
         │                  │                     │
         ▼                  ▼                     ▼
┌─────────────────────────────────────────────────────────────┐
│             TRACE-SL experiment and evaluator layer          │
│       `TRC-23-02333/transparent_estimator_eval.py`           │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                Multi-split aggregation layer                 │
│       `TRC-23-02333/summarize_trace_sl_rcss.py`              │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│             Datasets, SUMO scenarios, and artifacts          │
│ `TRC-23-02333/dataset/` → `TRC-23-02333/trace_sl_results/`  │
│ `sumo_scenarios/chengdu/`                                    │
└─────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| TRACE-SL evaluator | Loads PeMS/Seattle traffic datasets, builds train/validation/test splits, computes reconstruction baselines, generates sensor layouts, evaluates GLS/MAP and GSP reconstruction, and writes per-seed artifacts. | `TRC-23-02333/transparent_estimator_eval.py` |
| Dataset loaders | Auto-detect PeMS CSV datasets or Seattle NumPy datasets under the supplied data root and normalize them into arrays plus distance matrices. | `TRC-23-02333/transparent_estimator_eval.py` |
| Layout generators | Produce random, degree, top-variance, coverage, greedy posterior, scenario greedy, robust coverage-CVaR, RCSS, and validation-swap sensor layouts. | `TRC-23-02333/transparent_estimator_eval.py` |
| Reconstruction evaluators | Evaluate hidden-link reconstruction with historical time-of-day mean, neighbor average, GSP, and GLS/MAP methods. | `TRC-23-02333/transparent_estimator_eval.py` |
| Per-seed artifact writer | Writes `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.csv`, `rcss_candidates.json`, `certificate_correlations.csv`, `config.json`, and `SUMMARY.md`. | `TRC-23-02333/transparent_estimator_eval.py` |
| Multi-split summarizer | Combines `seed_*/metrics.csv`, candidate diagnostics, and certificate correlations into aggregate CSV files and a summary. | `TRC-23-02333/summarize_trace_sl_rcss.py` |
| Reproduction scripts | Parameterize Stage 11 experiment runs for PeMS7_228, PeMS7_1026, and Seattle, then invoke the summarizer. | `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh` |
| Curated result archive | Stores committed experiment outputs and aggregate reproducibility artifacts. | `TRC-23-02333/trace_sl_results/` |
| Documentation handoff | Describes result claims, data placement, reproduction commands, and research-stage context. | `README.md`, `RESEARCH_PIPELINE_REPORT.md`, `NARRATIVE_REPORT.md`, `TRC-23-02333/trace_sl_results/README.md` |
| SUMO scenario assets | Stores a Chengdu SUMO network, route file, SUMO config, and GUI config independent of the TRACE-SL Python pipeline. | `sumo_scenarios/chengdu/` |

## Pattern Overview

**Overall:** Script-oriented research pipeline with a monolithic numerical experiment driver and a separate aggregation script.

**Key Characteristics:**
- Use command-line scripts as entry points: run `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, or `scripts/run_stage11_seattle.sh` rather than importing an application package.
- Keep algorithmic stages in pure functions inside `TRC-23-02333/transparent_estimator_eval.py`; the `main()` function wires arguments, data, layouts, evaluation, and artifact writing.
- Represent experiment records as dictionaries and Pandas data frames; persist outputs as CSV/JSON/Markdown under `TRC-23-02333/trace_sl_results/`.
- Use file-system conventions instead of a database: inputs are under `TRC-23-02333/dataset/`, per-seed outputs are under `TRC-23-02333/trace_sl_results/<experiment>/seed_<n>/`, and aggregate outputs live directly under `TRC-23-02333/trace_sl_results/<experiment>/`.

## Layers

**Run Orchestration:**
- Purpose: Configure datasets, seeds, budgets, candidate counts, BLAS thread limits, and output directories.
- Location: `scripts/`
- Contains: Bash scripts `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Depends on: `python`, `TRC-23-02333/transparent_estimator_eval.py`, and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Used by: Developers reproducing Stage 11 experiments from `README.md`.

**Data Loading and Splitting:**
- Purpose: Convert dataset files into train, validation, and test arrays plus graph/distance matrices.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `load_pems_dataset()`, `load_seattle_dataset()`, `adjacency_to_distance()`, and `split_daily_frame()`.
- Depends on: `numpy`, `pandas`, `scipy.sparse.csgraph.shortest_path`, and dataset files under `TRC-23-02333/dataset/`.
- Used by: `main()` in `TRC-23-02333/transparent_estimator_eval.py`.

**Feature and Matrix Construction:**
- Purpose: Build time-of-day priors, graph Laplacian, covariance precision matrices, and scenario matrices for reconstruction/layout objectives.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `time_of_day_mean()`, `make_similarity()`, `make_laplacian()`, and `build_scenario_matrices()`.
- Depends on: arrays returned by `load_pems_dataset()` and `LedoitWolf` covariance estimation from `sklearn.covariance`.
- Used by: layout generation, RCSS scoring, GSP reconstruction, and GLS/MAP reconstruction in `TRC-23-02333/transparent_estimator_eval.py`.

**Layout Search:**
- Purpose: Generate candidate sensor sets and select/refine robust layouts.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `degree_layout()`, `top_variance_layout()`, `coverage_layout()`, `greedy_posterior_layout()`, `scenario_greedy_layout()`, `quality_coverage_sample()`, `robust_coverage_cvar_layout()`, `select_rcss_candidate()`, `select_auto_rcss_weights()`, `swap_trace_local_search()`, and `validation_swap_search()`.
- Depends on: distance matrices, precision matrices, scenario matrices, validation data, and CLI parameters parsed by `main()`.
- Used by: budget loops in `main()` in `TRC-23-02333/transparent_estimator_eval.py`.

**Reconstruction Evaluation:**
- Purpose: Compute hidden-link reconstruction predictions and metrics for every layout.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `historical_mean_predict()`, `neighbor_average_predict()`, `solve_quadratic()`, `certificate()`, `metrics()`, and `evaluate_layout()`.
- Depends on: normalized observations, sensor indices, Laplacian, covariance precision, and `scipy.linalg` solvers.
- Used by: `validation_mae()`, `make_rcss_row()`, and final layout evaluation loops in `main()`.

**Artifact Persistence:**
- Purpose: Store detailed per-seed experiment evidence and human-readable summaries.
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Contains: `write_summary()` and output writes in `main()`.
- Depends on: Pandas data frames, JSON serialization, and `Path.mkdir()`.
- Used by: shell scripts in `scripts/` and downstream aggregation in `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Aggregate Analysis:**
- Purpose: Merge seed-level outputs, compute layout summaries, deltas, paired tests, winner counts, certificate summaries, and selected-source counts.
- Location: `TRC-23-02333/summarize_trace_sl_rcss.py`
- Contains: `main()` only; aggregation is procedural.
- Depends on: `seed_*/metrics.csv`, optional `seed_*/certificate_correlations.csv`, optional `seed_*/rcss_candidates.csv`, `pandas`, and `scipy.stats`.
- Used by: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Research Documentation and Artifacts:**
- Purpose: Preserve paper-writing context, result interpretation, and reproducibility notes.
- Location: repository root, `refine-logs/`, `.planning/quick/`, `idea-stage/`, and `TRC-23-02333/trace_sl_results/`.
- Contains: `README.md`, `RESEARCH_PIPELINE_REPORT.md`, `MANIFEST.md`, `NARRATIVE_REPORT.md`, `refine-logs/*.md`, `.planning/quick/260518-trace-sl-cpu-pilot/*.md`, and `TRC-23-02333/trace_sl_results/README.md`.
- Depends on: checked-in CSV/JSON/Markdown experiment outputs under `TRC-23-02333/trace_sl_results/`.
- Used by: research handoff, paper writing, and GSD planning.

## Data Flow

### Stage 11 Experiment Path

1. A shell script selects dataset root, output directory, seeds, budgets, candidate counts, and thread limits (`scripts/run_stage11_pems7_228.sh:3`, `scripts/run_stage11_pems7_1026.sh:3`, `scripts/run_stage11_seattle.sh:3`).
2. The script invokes `python TRC-23-02333/transparent_estimator_eval.py` once per split seed with Stage 11 flags (`scripts/run_stage11_pems7_228.sh:25`, `scripts/run_stage11_pems7_1026.sh:25`, `scripts/run_stage11_seattle.sh:25`).
3. `main()` parses CLI flags and budgets (`TRC-23-02333/transparent_estimator_eval.py:697`).
4. `load_pems_dataset()` loads PeMS CSV files or delegates to `load_seattle_dataset()` when PeMS files are absent (`TRC-23-02333/transparent_estimator_eval.py:81`).
5. `split_daily_frame()` creates randomized train/validation/test daily splits by seed (`TRC-23-02333/transparent_estimator_eval.py:20`).
6. `main()` builds statistics, Laplacian, covariance precision, scenario matrices, and a GLS base matrix (`TRC-23-02333/transparent_estimator_eval.py:754`).
7. The budget loop generates random layouts, validation-selected random layouts, simple baselines, greedy layouts, scenario-greedy layouts, swap layouts, RCSS candidates, auto weights, and validation-swap layouts (`TRC-23-02333/transparent_estimator_eval.py:770`).
8. `evaluate_layout()` computes historical, neighbor, GSP, and GLS/MAP metrics for each layout (`TRC-23-02333/transparent_estimator_eval.py:599`).
9. `main()` writes seed-level outputs to the requested output directory (`TRC-23-02333/transparent_estimator_eval.py:998`).
10. The shell script invokes `TRC-23-02333/summarize_trace_sl_rcss.py` to aggregate all `seed_*` results (`scripts/run_stage11_pems7_228.sh:50`, `scripts/run_stage11_pems7_1026.sh:50`, `scripts/run_stage11_seattle.sh:50`).

### Multi-Split Aggregation Path

1. `TRC-23-02333/summarize_trace_sl_rcss.py` receives one or more `--input-root` directories and an `--output-dir` (`TRC-23-02333/summarize_trace_sl_rcss.py:7`).
2. It reads each `seed_*/metrics.csv` and attaches `split_seed` from the directory name (`TRC-23-02333/summarize_trace_sl_rcss.py:20`).
3. It optionally reads `seed_*/certificate_correlations.csv` and `seed_*/rcss_candidates.csv` (`TRC-23-02333/summarize_trace_sl_rcss.py:26`).
4. It writes `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `gls_map_ablation_summary.csv`, `gls_map_per_split_winners.csv`, and `gls_map_win_counts.csv` (`TRC-23-02333/summarize_trace_sl_rcss.py:41`).
5. It writes optional certificate and RCSS aggregate files when corresponding seed-level artifacts exist (`TRC-23-02333/summarize_trace_sl_rcss.py:117`).
6. It writes aggregate `SUMMARY.md` under `--output-dir` (`TRC-23-02333/summarize_trace_sl_rcss.py:204`).

### Dataset Dispatch Flow

1. `load_pems_dataset()` searches `--data-root` for `PeMSD7_V_*.csv` and `PeMSD7_W_*.csv` (`TRC-23-02333/transparent_estimator_eval.py:81`).
2. If both PeMS files exist, the function reads values and distances as CSV matrices (`TRC-23-02333/transparent_estimator_eval.py:87`).
3. If PeMS files are absent, the function delegates to `load_seattle_dataset()` (`TRC-23-02333/transparent_estimator_eval.py:86`).
4. `load_seattle_dataset()` expects `tensor.npz` and `Loop_Seattle_2015_A.npy` under the same data root (`TRC-23-02333/transparent_estimator_eval.py:58`).
5. `adjacency_to_distance()` converts Seattle adjacency into shortest-path distances (`TRC-23-02333/transparent_estimator_eval.py:46`).

**State Management:**
- Experiment state is local to function calls in `TRC-23-02333/transparent_estimator_eval.py`; random state uses `np.random.default_rng()` seeded from `--split-seed` and `--layout-seed`.
- The only module-level constant in the evaluator is `SLOTS_PER_DAY = 288` in `TRC-23-02333/transparent_estimator_eval.py`.
- Persistent state is file-based: per-seed and aggregate outputs live under `TRC-23-02333/trace_sl_results/`.

## Key Abstractions

**Sensor Layout:**
- Purpose: Represents selected sensor node indices for a budget.
- Examples: `sensors` arrays in `TRC-23-02333/transparent_estimator_eval.py`, serialized to `layouts.json` and `rcss_candidates.csv` under `TRC-23-02333/trace_sl_results/`.
- Pattern: NumPy arrays during computation, sorted integer lists when written to JSON/CSV.

**Budget:**
- Purpose: Controls sensor count as a fraction of graph nodes.
- Examples: `--budgets` in `scripts/run_stage11_pems7_228.sh`, `parse_budgets()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: CLI string converted to `list[float]`; `sensor_count = round(n_nodes * budget)` inside `main()`.

**Dataset Split:**
- Purpose: Provides train, validation, and test arrays for each split seed.
- Examples: `split_daily_frame()` and `args.val_days` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Date-based random split into train days, validation days, and test days.

**Reconstruction Method:**
- Purpose: Defines prediction strategy for hidden nodes.
- Examples: `historical_tod_mean`, `neighbor_average`, `gsp`, and `gls_map` rows generated in `evaluate_layout()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Method-specific metrics dictionaries appended to `rows` and written to `metrics.csv`.

**Certificate:**
- Purpose: Quantifies reconstruction matrix properties used for transparent layout diagnostics.
- Examples: `posterior_trace`, `condition_number`, and `information_logdet` from `certificate()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Numeric diagnostic fields attached to GSP/GLS rows and summarized by `summarize_correlations()`.

**RCSS Candidate Row:**
- Purpose: Represents one candidate layout plus validation and certificate diagnostics used for robust selection.
- Examples: `make_rcss_row()`, `rcss_candidate_scores()`, and `select_auto_rcss_weights()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Pattern: Mutable dictionary enriched with normalized weighted scores, selected flags, and source metadata.

**Aggregate Result Directory:**
- Purpose: Groups seed-level and aggregate evidence for one experiment stage.
- Examples: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`, `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`, and `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`.
- Pattern: Seed subdirectories contain raw per-seed files; parent directories contain combined CSV files and `SUMMARY.md`.

## Entry Points

**PeMS7_228 Stage 11 reproduction:**
- Location: `scripts/run_stage11_pems7_228.sh`
- Triggers: Manual shell execution from repository root, documented in `README.md`.
- Responsibilities: Run seeds `25 26 27 28 29` by default, write per-seed outputs to `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/seed_<seed>/`, and aggregate into the same output directory.

**PeMS7_1026 Stage 11 reproduction:**
- Location: `scripts/run_stage11_pems7_1026.sh`
- Triggers: Manual shell execution from repository root, documented in `README.md`.
- Responsibilities: Run external validation on `TRC-23-02333/dataset/PeMS7_1026` and write outputs to `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`.

**Seattle Stage 11 reproduction:**
- Location: `scripts/run_stage11_seattle.sh`
- Triggers: Manual shell execution from repository root.
- Responsibilities: Run heterogeneous-network validation on `TRC-23-02333/dataset/Seattle` and write outputs to `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`.

**Single-seed evaluator:**
- Location: `TRC-23-02333/transparent_estimator_eval.py`
- Triggers: Direct `python TRC-23-02333/transparent_estimator_eval.py ...` invocation.
- Responsibilities: Load one dataset split, generate/evaluate layouts for requested budgets, and write per-seed artifacts.

**Multi-split summarizer:**
- Location: `TRC-23-02333/summarize_trace_sl_rcss.py`
- Triggers: Direct `python TRC-23-02333/summarize_trace_sl_rcss.py --input-root ... --output-dir ...` invocation or shell scripts in `scripts/`.
- Responsibilities: Aggregate seed-level outputs into cross-split summaries and paired tests.

## Architectural Constraints

- **Threading:** Numerical threading is controlled in shell scripts by `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- **Global state:** Keep shared module state minimal; `SLOTS_PER_DAY` in `TRC-23-02333/transparent_estimator_eval.py` encodes 5-minute daily resolution for both PeMS and Seattle loaders.
- **Circular imports:** Not detected; `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` are standalone scripts and do not import each other.
- **Import model:** Use standard-library, NumPy, Pandas, SciPy, and scikit-learn imports directly in scripts; no package-level `__init__.py` or internal package import hierarchy is present under `TRC-23-02333/`.
- **Working directory:** Run shell scripts from repository root because scripts use relative paths such as `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/dataset/PeMS7_228`.
- **Data availability:** Datasets are not committed; place PeMS and Seattle data under `TRC-23-02333/dataset/` using the paths documented in `README.md`.
- **Result artifacts:** Treat `TRC-23-02333/trace_sl_results/` as a reproducibility archive; add curated outputs there and avoid overwriting published result directories without preserving traceability.

## Anti-Patterns

### Splitting one experiment stage across untracked ad hoc paths

**What happens:** New runs can write to arbitrary `--output-dir` values from `TRC-23-02333/transparent_estimator_eval.py`.
**Why it's wrong:** `TRC-23-02333/summarize_trace_sl_rcss.py` expects consistent `seed_*/metrics.csv`, `seed_*/certificate_correlations.csv`, and `seed_*/rcss_candidates.csv` layouts, and documentation points to curated directories under `TRC-23-02333/trace_sl_results/`.
**Do this instead:** Place new experiment stages under `TRC-23-02333/trace_sl_results/<dataset>_<stage_name>/` and aggregate with `TRC-23-02333/summarize_trace_sl_rcss.py`.

### Adding layout methods without artifact and summary coverage

**What happens:** Layout methods are appended as tuple records inside the budget loop in `TRC-23-02333/transparent_estimator_eval.py`.
**Why it's wrong:** New layout types that are not included in `layouts.json`, `metrics.csv`, `rcss_candidates.csv`, and aggregation baseline lists in `TRC-23-02333/summarize_trace_sl_rcss.py` become hard to compare across seeds.
**Do this instead:** When adding a layout method in `TRC-23-02333/transparent_estimator_eval.py`, also update `layout_records`, `rcss_records` when relevant, and `comparison_layouts`/`baseline_layouts` in `TRC-23-02333/summarize_trace_sl_rcss.py`.

### Hiding dataset-specific logic inside downstream algorithms

**What happens:** Dataset dispatch belongs in `load_pems_dataset()` and `load_seattle_dataset()` in `TRC-23-02333/transparent_estimator_eval.py`.
**Why it's wrong:** Layout and reconstruction functions expect normalized arrays plus a distance matrix, and embedding dataset-file assumptions in algorithms reduces cross-dataset reproducibility.
**Do this instead:** Add new dataset adapters near `load_pems_dataset()` and keep layout/evaluation functions dataset-agnostic in `TRC-23-02333/transparent_estimator_eval.py`.

### Treating SUMO scenario files as TRACE-SL evaluation inputs

**What happens:** `sumo_scenarios/chengdu/` stores SUMO files but the Python TRACE-SL pipeline reads PeMS/Seattle datasets from `TRC-23-02333/dataset/`.
**Why it's wrong:** `TRC-23-02333/transparent_estimator_eval.py` does not parse `.sumocfg`, `.net.xml`, or `.rou.xml` files.
**Do this instead:** Add a dedicated dataset adapter in `TRC-23-02333/transparent_estimator_eval.py` before using SUMO-derived data in TRACE-SL experiments.

## Error Handling

**Strategy:** Use fail-fast exceptions for missing required inputs and invalid CLI/configuration values; use guarded optional artifact loading in the summarizer.

**Patterns:**
- Raise `FileNotFoundError` when Seattle `tensor.npz` or `Loop_Seattle_2015_A.npy` is missing in `TRC-23-02333/transparent_estimator_eval.py`.
- Raise `ValueError` for invalid tensor shape, unsupported objectives, empty RCSS weight grids, unsupported selection methods, or missing RCSS candidates in `TRC-23-02333/transparent_estimator_eval.py`.
- Raise `SystemExit` when no seed metrics exist under summarizer input roots in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Check optional paths with `Path.exists()` before loading certificate correlations or RCSS candidates in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Shell scripts use `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

## Cross-Cutting Concerns

**Logging:** Use `print()` for terminal progress in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`; shell scripts tee per-seed logs to `TRC-23-02333/trace_sl_results/*_seed_<seed>.log`.
**Validation:** Use deterministic split seeds, validation-day MAE, inner validation/tuner split for auto RCSS weights, and paired tests in `TRC-23-02333/summarize_trace_sl_rcss.py`.
**Authentication:** Not applicable; the repository contains local scripts and local datasets only.
**Configuration:** Use CLI arguments in `TRC-23-02333/transparent_estimator_eval.py` and environment-variable defaults in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
**Reproducibility:** Preserve `config.json`, `layouts.json`, `metrics.csv`, `rcss_candidates.csv`, `swap_history.json`, and aggregate CSV files under `TRC-23-02333/trace_sl_results/` for every curated experiment.

---

*Architecture analysis: 2026/05/21*
