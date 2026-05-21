# External Integrations

**Analysis Date:** 2026/05/21

## APIs & External Services

**Research datasets:**
- PeMS7_228 - Primary in-domain traffic speed/distance dataset for TRACE-SL reproduction.
  - SDK/Client: Local CSV loading through `pandas.read_csv()` in `TRC-23-02333/transparent_estimator_eval.py`.
  - Auth: Not applicable; expected local files are `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv` and `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv` as documented in `README.md`.
- PeMS7_1026 - External PeMS validation dataset for larger-network Stage 11 runs.
  - SDK/Client: Local CSV loading through `pandas.read_csv()` in `TRC-23-02333/transparent_estimator_eval.py`.
  - Auth: Not applicable; expected local files are `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv` and `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv` as documented in `README.md`.
- Seattle loop-detector dataset - Heterogeneous-network validation dataset.
  - SDK/Client: Local `.npz`/`.npy` loading through `numpy.load()` in `TRC-23-02333/transparent_estimator_eval.py`.
  - Auth: Not applicable; expected local files are `TRC-23-02333/dataset/Seattle/tensor.npz` and `TRC-23-02333/dataset/Seattle/Loop_Seattle_2015_A.npy`.

**Simulation artifacts:**
- SUMO Chengdu scenario - Static traffic-simulation scenario assets under `sumo_scenarios/chengdu/`.
  - SDK/Client: Not invoked by current Python scripts; `sumo_scenarios/chengdu/chengdu.sumocfg` references `chengdu.net.xml`, `chengdu.rou.xml`, and `gui-settings.cfg`.
  - Auth: Not applicable.

**Cloud APIs:**
- Not detected. No Stripe, Supabase, AWS, Azure, GCP, OpenAI, Anthropic, database SDK, HTTP API client, or webhook integration is imported by `TRC-23-02333/transparent_estimator_eval.py` or `TRC-23-02333/summarize_trace_sl_rcss.py`.

## Data Storage

**Databases:**
- Not detected.
  - Connection: Not applicable.
  - Client: Not applicable.

**File Storage:**
- Local filesystem only.
  - Inputs: `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, and `TRC-23-02333/dataset/Seattle/`.
  - Outputs: `TRC-23-02333/trace_sl_results/`.
  - Per-run outputs from `TRC-23-02333/transparent_estimator_eval.py`: `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, `config.json`, and `SUMMARY.md`.
  - Aggregated outputs from `TRC-23-02333/summarize_trace_sl_rcss.py`: `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `gls_map_ablation_summary.csv`, `gls_map_per_split_winners.csv`, `gls_map_win_counts.csv`, `combined_certificate_correlations.csv`, `certificate_correlation_summary.csv`, `combined_rcss_candidates.csv`, `rcss_selected_sources.csv`, and `SUMMARY.md`.

**Caching:**
- None detected as a dedicated cache service.
- Python bytecode cache directories such as `TRC-23-02333/__pycache__/` may exist locally and are ignored by `.gitignore`.

## Authentication & Identity

**Auth Provider:**
- None.
  - Implementation: Not applicable. The repository runs local experiment scripts and does not implement users, sessions, tokens, or service authentication.

## Monitoring & Observability

**Error Tracking:**
- None.

**Logs:**
- Local shell logs through `tee` in `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.
- Stage scripts write logs such as `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_seed_25.log` and `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight_seed_25.log`.
- Python scripts print grouped metric summaries and output locations to stdout in `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.

## CI/CD & Deployment

**Hosting:**
- None detected. This is a local research/reproducibility repository.

**CI Pipeline:**
- None detected. No GitHub Actions, GitLab CI, CircleCI, Jenkins, or other CI configuration files were detected during the tech scan.

## Environment Configuration

**Required env vars:**
- None required for credentials.
- Optional experiment overrides consumed by the Stage 11 scripts:
  - `DATA_ROOT` - Input dataset root, e.g. `TRC-23-02333/dataset/PeMS7_228` in `scripts/run_stage11_pems7_228.sh`.
  - `OUTPUT_DIR` - Result directory under `TRC-23-02333/trace_sl_results/`.
  - `SEEDS` - Split seeds; defaults are `25 26 27 28 29` in all Stage 11 scripts.
  - `BUDGETS` - Sensor-budget fractions; defaults to `0.10 0.20 0.30`.
  - `NUM_LAYOUTS` - Random layouts per budget.
  - `RCSS_RANDOM_CANDIDATES` - Number of validation-ranked random candidates.
  - `RCSS_QUALITY_CANDIDATES` - Number of quality-coverage candidates.
  - `SCENARIO_COUNT` - Number of scenario matrices used by scenario/CVaR layout generators.
  - `VALIDATION_SWAP_STARTS`, `VALIDATION_SWAP_ITER`, `VALIDATION_SWAP_ADD_POOL`, `VALIDATION_SWAP_REMOVE_POOL` - Validation-aware swap controls.
  - `THREADS_PER_JOB` - Shared default for BLAS/threading environment exports.
  - `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS` - Thread limits exported by `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, and `scripts/run_stage11_seattle.sh`.

**Secrets location:**
- Not applicable. No secret files or environment-variable secrets are required for the current code.
- `.gitignore` excludes large local datasets with `dataset/` and `TRC-23-02333/dataset/`; these paths are data placement locations, not secret stores.

## Webhooks & Callbacks

**Incoming:**
- None. There is no server, API endpoint, webhook handler, or callback route in the current codebase.

**Outgoing:**
- None. The code does not make outbound HTTP calls or publish events; it reads local datasets and writes local result artifacts.

---

*Integration audit: 2026/05/21*
