# Technology Stack

**Analysis Date:** 2026/05/21

## Languages

**Primary:**
- Python 3.12.3 - TRACE-SL experiment driver and result aggregation in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Secondary:**
- Bash - Reproducibility launchers in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- XML - SUMO scenario configuration artifacts in `sumo_scenarios/chengdu/chengdu.sumocfg`, `sumo_scenarios/chengdu/chengdu.net.xml`, and `sumo_scenarios/chengdu/chengdu.rou.xml`.
- Markdown - Research handoff and result documentation in `README.md`, `MANIFEST.md`, `NARRATIVE_REPORT.md`, `RESEARCH_PIPELINE_REPORT.md`, and `TRC-23-02333/trace_sl_results/README.md`.

## Runtime

**Environment:**
- Python 3.12.3 observed locally via `python --version`.
- The project expects a Python virtual environment created with `python -m venv .venv`, activated with `source .venv/bin/activate`, and populated with `pip install -r requirements.txt` as documented in `README.md`.
- Shell scripts are POSIX-style Bash scripts using `#!/usr/bin/env bash` and `set -euo pipefail` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Package Manager:**
- pip - Dependencies are declared in `requirements.txt`.
- Lockfile: missing; `requirements.txt` contains unpinned package names only.

## Frameworks

**Core:**
- NumPy - Numerical array operations, random layout sampling, matrix metrics, `.npy`/`.npz` dataset loading in `TRC-23-02333/transparent_estimator_eval.py`.
- pandas - CSV dataset loading, time-indexed traffic frames, result table construction, and CSV output in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- SciPy - Dense linear algebra, shortest-path graph distances, Pearson/Spearman correlations, paired t-tests, and Wilcoxon tests in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- scikit-learn - Ledoit-Wolf covariance shrinkage via `sklearn.covariance.LedoitWolf` in `TRC-23-02333/transparent_estimator_eval.py`.

**Testing:**
- Not detected. No `pytest`, `unittest`, `jest`, `vitest`, or test configuration files were detected in the tracked codebase.
- Validation is experiment-driven: scripts write metrics and summaries to `TRC-23-02333/trace_sl_results/` and aggregation is performed by `TRC-23-02333/summarize_trace_sl_rcss.py`.

**Build/Dev:**
- No build system detected. The code is run directly with `python TRC-23-02333/transparent_estimator_eval.py` from the shell scripts in `scripts/`.
- No linting or formatting tool configuration detected at project root.
- No Dockerfile, compose file, Makefile, `pyproject.toml`, `setup.py`, or `setup.cfg` detected.

## Key Dependencies

**Critical:**
- `numpy` (unpinned) - Required by `TRC-23-02333/transparent_estimator_eval.py` for arrays, random number generation, finite-value handling, matrix traces, condition numbers, and JSON-serializable experiment records.
- `pandas` (unpinned) - Required by `TRC-23-02333/transparent_estimator_eval.py` for PeMS CSV ingestion and by `TRC-23-02333/summarize_trace_sl_rcss.py` for multi-split result aggregation.
- `scipy` (unpinned) - Required by `TRC-23-02333/transparent_estimator_eval.py` for `scipy.linalg`, graph shortest paths, and correlation statistics; required by `TRC-23-02333/summarize_trace_sl_rcss.py` for paired statistical tests.
- `scikit-learn` (unpinned) - Required by `TRC-23-02333/transparent_estimator_eval.py` for Ledoit-Wolf covariance estimation used by GLS/MAP precision matrices and scenario matrices.

**Infrastructure:**
- Python standard library `argparse`, `json`, `math`, and `pathlib` - CLI parsing, output serialization, scoring math, and filesystem access in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Bash and coreutils - Reproduction scripts set environment defaults, create output directories, run Python commands, and tee logs in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

## Configuration

**Environment:**
- No `.env` files detected at project root during the scan.
- Runtime configuration is passed through CLI flags in `TRC-23-02333/transparent_estimator_eval.py`, including `--data-root`, `--output-dir`, `--budgets`, `--num-layouts`, `--split-seed`, `--layout-seed`, `--include-rcss`, `--rcss-auto-weights`, and `--include-validation-swap`.
- Shell script defaults are environment-variable overridable in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`: `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, `NUM_LAYOUTS`, `RCSS_RANDOM_CANDIDATES`, `RCSS_QUALITY_CANDIDATES`, `SCENARIO_COUNT`, `VALIDATION_SWAP_STARTS`, `VALIDATION_SWAP_ITER`, `VALIDATION_SWAP_ADD_POOL`, `VALIDATION_SWAP_REMOVE_POOL`, and `THREADS_PER_JOB`.
- BLAS/thread controls are exported by all Stage 11 scripts: `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS`.

**Build:**
- `requirements.txt` - Unpinned Python dependency list.
- `README.md` - Environment setup and reproduction commands.
- `scripts/run_stage11_pems7_228.sh` - PeMS7_228 Stage 11 reproduction defaults: `NUM_LAYOUTS=200`, `RCSS_RANDOM_CANDIDATES=200`, `RCSS_QUALITY_CANDIDATES=200`, split seeds `25 26 27 28 29`, and output under `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight`.
- `scripts/run_stage11_pems7_1026.sh` - PeMS7_1026 Stage 11 reproduction defaults: `NUM_LAYOUTS=100`, candidate counts `100`, split seeds `25 26 27 28 29`, and output under `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight`.
- `scripts/run_stage11_seattle.sh` - Seattle Stage 11 light run defaults: `NUM_LAYOUTS=50`, candidate counts `50`, split seeds `25 26 27 28 29`, and output under `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light`.
- `sumo_scenarios/chengdu/chengdu.sumocfg` - SUMO scenario references `chengdu.net.xml`, `chengdu.rou.xml`, and `gui-settings.cfg`; no Python code currently invokes SUMO.

## Platform Requirements

**Development:**
- Python with pip and virtualenv support.
- CPU-oriented scientific Python stack; no GPU runtime is required by `TRC-23-02333/transparent_estimator_eval.py`.
- Sufficient RAM for dense covariance, precision, inverse, and shortest-path matrices in `TRC-23-02333/transparent_estimator_eval.py`; PeMS7_1026 uses dense 1026-node matrices.
- Local datasets must be placed under paths documented in `README.md`, such as `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv`, `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`, `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv`, and `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv`.
- Seattle runs expect `TRC-23-02333/dataset/Seattle/tensor.npz` and `TRC-23-02333/dataset/Seattle/Loop_Seattle_2015_A.npy`, as enforced by `load_seattle_dataset()` in `TRC-23-02333/transparent_estimator_eval.py`.

**Production:**
- Not applicable. This repository is a research experiment and reproducibility artifact, not a deployed service.
- Outputs are local files under `TRC-23-02333/trace_sl_results/`, including `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, `config.json`, and `SUMMARY.md` written by `TRC-23-02333/transparent_estimator_eval.py`.

---

*Stack analysis: 2026/05/21*
