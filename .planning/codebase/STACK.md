# Technology Stack

**Analysis Date:** 2026/05/21

## Languages

**Primary:**
- Python 3.12.3 - Research/ML experiment driver and result aggregation in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Bash - Reproduction launchers and environment/thread controls in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Secondary:**
- Markdown - Research handoff and reproducibility documentation in `README.md`, `RESEARCH_PIPELINE_REPORT.md`, `NARRATIVE_REPORT.md`, `MANIFEST.md`, and `TRC-23-02333/trace_sl_results/README.md`.
- CSV/JSON - Experiment inputs and outputs under `TRC-23-02333/dataset/` and `TRC-23-02333/trace_sl_results/`.

## Runtime

**Environment:**
- CPython 3.12.3 - Current local runtime detected with `python --version`; code uses Python standard library modules `argparse`, `json`, `math`, and `pathlib` in `TRC-23-02333/transparent_estimator_eval.py`.
- POSIX shell environment - Stage scripts use `#!/usr/bin/env bash` and `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Package Manager:**
- pip 24.0 - Installation path documented in `README.md` with `pip install -r requirements.txt`.
- Lockfile: missing - `requirements.txt` lists package names only and does not pin versions.

## Frameworks

**Core:**
- NumPy - Vectorized numerical arrays, random layout sampling, `.npy`/`.npz` dataset loading, matrix operations, and JSON-serializable experiment records in `TRC-23-02333/transparent_estimator_eval.py`.
- pandas - CSV dataset loading, datetime indexing, metric aggregation, and result writing in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- SciPy - Dense linear algebra (`scipy.linalg`), graph shortest paths (`scipy.sparse.csgraph.shortest_path`), and statistical tests/correlations (`scipy.stats`) in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- scikit-learn - Ledoit-Wolf covariance shrinkage via `sklearn.covariance.LedoitWolf` in `TRC-23-02333/transparent_estimator_eval.py`.

**Testing:**
- Not detected - No pytest/unittest configuration or test dependencies were detected in `requirements.txt`; validation is currently experiment-driven through stage scripts and generated summaries in `TRC-23-02333/trace_sl_results/`.

**Build/Dev:**
- Bash stage launchers - Reproduce Stage 11 experiments with `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Python CLI scripts - Main runnable modules are `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- No build system detected - No `pyproject.toml`, `setup.py`, `Makefile`, Dockerfile, or CI configuration was detected at the repository root.

## Key Dependencies

**Critical:**
- `numpy` - Required for traffic tensors, sensor-index arrays, posterior inverse updates, random candidate generation, and `.npy`/`.npz` Seattle loading in `TRC-23-02333/transparent_estimator_eval.py`.
- `pandas` - Required for PeMS CSV loading, date-based train/validation/test splits, experiment metric tables, and summary CSV outputs in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- `scipy` - Required for GLS/GSP solves, graph distances, paired t-tests, Wilcoxon tests, and certificate-error correlations in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- `scikit-learn` - Required for `LedoitWolf` covariance estimation used to build GLS precision matrices and robust scenario matrices in `TRC-23-02333/transparent_estimator_eval.py`.

**Infrastructure:**
- `requirements.txt` - Minimal dependency manifest containing `numpy`, `pandas`, `scipy`, and `scikit-learn`.
- BLAS/OpenMP thread variables - Reproduction scripts export `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh` to avoid oversubscription during parallel numerical work.
- Local artifact directories - Curated results are stored in `TRC-23-02333/trace_sl_results/`; large datasets are stored locally under `TRC-23-02333/dataset/` and ignored by Git via `.gitignore`.

## Configuration

**Environment:**
- Configure a Python virtual environment as documented in `README.md`: create `.venv`, activate it, then run `pip install -r requirements.txt`.
- Stage scripts accept shell environment overrides before execution: `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, `NUM_LAYOUTS`, `RCSS_RANDOM_CANDIDATES`, `RCSS_QUALITY_CANDIDATES`, `SCENARIO_COUNT`, `VALIDATION_SWAP_STARTS`, `VALIDATION_SWAP_ITER`, `VALIDATION_SWAP_ADD_POOL`, `VALIDATION_SWAP_REMOVE_POOL`, and `THREADS_PER_JOB` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- `TRC-23-02333/transparent_estimator_eval.py` exposes CLI flags for dataset paths, budgets, random seeds, estimator settings, RCSS scoring weights, GSP/GLS hyperparameters, validation swap settings, and output directories.
- No `.env` files detected at repository root; secrets are not part of the runtime configuration.

**Build:**
- `requirements.txt` is the only dependency configuration file detected.
- `.gitignore` preserves reproducibility assets while ignoring large local datasets under `TRC-23-02333/dataset/` and local output/model artifacts such as `checkpoint.pth`, `checkpoints/`, `results/`, `test_results/`, `train_results/`, and `vali_results/`.
- `README.md` documents expected PeMS dataset placement and reproduction commands.
- `TRC-23-02333/trace_sl_results/README.md` documents the committed result-stage inventory and the current main method (`validation_swap_selected`).

## Platform Requirements

**Development:**
- Linux/POSIX shell environment for Bash stage scripts in `scripts/`.
- Python 3.12-compatible numerical environment with NumPy, pandas, SciPy, and scikit-learn installed from `requirements.txt`.
- Local PeMS datasets placed at `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv`, `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`, `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv`, and `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv` as documented in `README.md`.
- Local Seattle heterogeneous-network files placed under `TRC-23-02333/dataset/Seattle/`, including `tensor.npz` and `Loop_Seattle_2015_A.npy`, as required by `load_seattle_dataset` in `TRC-23-02333/transparent_estimator_eval.py`.
- Sufficient CPU/RAM for dense matrix inversion, covariance estimation, candidate scoring, and repeated validation evaluations in `TRC-23-02333/transparent_estimator_eval.py`; scripts default to `THREADS_PER_JOB=1` to control BLAS threading.

**Production:**
- Not applicable - This is a local research/ML experimentation repository with no service runtime, server entry point, container deployment, or cloud hosting configuration detected.
- Reproducibility target is local batch execution through `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`, writing artifacts to `TRC-23-02333/trace_sl_results/`.

---

*Stack analysis: 2026/05/21*
