# External Integrations

**Analysis Date:** 2026/05/21

## APIs & External Services

**External APIs:**
- None detected - `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` use local files and local numerical libraries only.
  - SDK/Client: Not applicable
  - Auth: Not applicable

**Research Datasets:**
- PeMS7_228 - Primary in-domain traffic speed and distance input documented in `README.md` and loaded by `load_pems_dataset` in `TRC-23-02333/transparent_estimator_eval.py`.
  - SDK/Client: Local CSV loading via `pandas.read_csv`
  - Auth: Not applicable; files are expected locally at `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv` and `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`
- PeMS7_1026 - External validation traffic speed and distance input documented in `README.md` and launched by `scripts/run_stage11_pems7_1026.sh`.
  - SDK/Client: Local CSV loading via `pandas.read_csv`
  - Auth: Not applicable; files are expected locally at `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv` and `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv`
- Seattle heterogeneous-network dataset - External heterogeneous-network validation input loaded by `load_seattle_dataset` in `TRC-23-02333/transparent_estimator_eval.py` and launched by `scripts/run_stage11_seattle.sh`.
  - SDK/Client: Local `.npz`/`.npy` loading via `numpy.load` and local CSV metadata files under `TRC-23-02333/dataset/Seattle/`
  - Auth: Not applicable; required files include `TRC-23-02333/dataset/Seattle/tensor.npz` and `TRC-23-02333/dataset/Seattle/Loop_Seattle_2015_A.npy`

**System Libraries:**
- BLAS/LAPACK-backed numerical stack - SciPy/NumPy dense linear algebra is used for covariance inversion, posterior certificates, and GLS/GSP solves in `TRC-23-02333/transparent_estimator_eval.py`.
  - SDK/Client: `numpy`, `scipy.linalg`, and installed BLAS backend
  - Auth: Not applicable

## Data Storage

**Databases:**
- None detected.
  - Connection: Not applicable
  - Client: Not applicable

**File Storage:**
- Local filesystem only.
  - Input datasets live under `TRC-23-02333/dataset/`; `.gitignore` excludes `dataset/` and `TRC-23-02333/dataset/` because datasets are large local artifacts.
  - Experiment outputs are written to `TRC-23-02333/trace_sl_results/` by `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
  - Per-seed outputs include `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, `config.json`, and `SUMMARY.md` under each configured output directory.
  - Aggregated outputs include `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `gls_map_ablation_summary.csv`, `gls_map_per_split_winners.csv`, `gls_map_win_counts.csv`, `combined_certificate_correlations.csv`, `certificate_correlation_summary.csv`, `combined_rcss_candidates.csv`, `rcss_selected_sources.csv`, and `SUMMARY.md` in aggregate directories such as `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`.

**Caching:**
- None implemented at application level.
- Python runtime bytecode cache may appear in `TRC-23-02333/__pycache__/`; `.gitignore` excludes `__pycache__/`.

## Authentication & Identity

**Auth Provider:**
- None.
  - Implementation: Not applicable; no web service, user identity, tokens, or credentialed API clients were detected.

## Monitoring & Observability

**Error Tracking:**
- None detected.

**Logs:**
- Stage scripts pipe stdout/stderr through `tee` to per-seed log files such as `${OUTPUT_DIR}_seed_${seed}.log` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Experiment scripts print grouped metrics and output paths to stdout in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Human-readable summaries are generated as Markdown files by `write_summary` in `TRC-23-02333/transparent_estimator_eval.py` and by `main` in `TRC-23-02333/summarize_trace_sl_rcss.py`.

## CI/CD & Deployment

**Hosting:**
- None detected - The repository is a local research codebase and has no deployment target.

**CI Pipeline:**
- None detected - No GitHub Actions, GitLab CI, tox, pytest, Docker, or build pipeline configuration was detected.

## Environment Configuration

**Required env vars:**
- None strictly required for the Python modules; defaults are supplied by `TRC-23-02333/transparent_estimator_eval.py` and the stage scripts.
- Optional script overrides in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`:
  - `DATA_ROOT` - Dataset root path, defaulting to `TRC-23-02333/dataset/PeMS7_228`, `TRC-23-02333/dataset/PeMS7_1026`, or `TRC-23-02333/dataset/Seattle` depending on script.
  - `OUTPUT_DIR` - Result directory under `TRC-23-02333/trace_sl_results/`.
  - `SEEDS` - Split seeds, defaulting to `25 26 27 28 29` in stage scripts.
  - `BUDGETS` - Sensor-budget fractions, defaulting to `0.10 0.20 0.30`.
  - `NUM_LAYOUTS` - Number of random layouts per budget.
  - `RCSS_RANDOM_CANDIDATES` and `RCSS_QUALITY_CANDIDATES` - Candidate pool sizes for Robust Certified Sensor Search.
  - `SCENARIO_COUNT` - Number of scenario matrices for CVaR-style robust scoring.
  - `VALIDATION_SWAP_STARTS`, `VALIDATION_SWAP_ITER`, `VALIDATION_SWAP_ADD_POOL`, and `VALIDATION_SWAP_REMOVE_POOL` - Validation-aware swap refinement controls.
  - `THREADS_PER_JOB`, `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, and `VECLIB_MAXIMUM_THREADS` - Numerical thread controls.

**Secrets location:**
- Not applicable - No `.env` files were detected and no credential files are required by the code.
- Dataset files are local non-secret research data under `TRC-23-02333/dataset/` and are ignored by `.gitignore`.

## Webhooks & Callbacks

**Incoming:**
- None - No HTTP server, API endpoint, or webhook listener was detected.

**Outgoing:**
- None - No outbound HTTP clients, SDK calls, message queues, or webhook publishers were detected.

---

*Integration audit: 2026/05/21*
