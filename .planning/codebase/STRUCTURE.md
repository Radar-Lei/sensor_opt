# Codebase Structure

**Analysis Date:** 2026/05/21

## Directory Layout

```text
/home/samuel/projects/sensor_opt/
├── README.md                         # TRACE-SL overview, data placement, and reproduction commands
├── requirements.txt                  # Python numerical dependency list
├── MANIFEST.md                       # Research artifact manifest maintained across stages
├── RESEARCH_PIPELINE_REPORT.md       # Current pipeline status and result handoff
├── NARRATIVE_REPORT.md               # Paper-writing narrative handoff
├── TRC-23-02333/                     # Main TRACE-SL implementation, dataset location, and outputs
│   ├── transparent_estimator_eval.py # Single-seed evaluator and layout-search driver
│   ├── summarize_trace_sl_rcss.py    # Multi-split aggregation and statistical summary script
│   ├── dataset/                      # Local uncommitted dataset placement
│   └── trace_sl_results/             # Curated CSV/JSON/Markdown experiment outputs
├── scripts/                          # Reproduction shell scripts for Stage 11 runs
│   ├── run_stage11_pems7_228.sh      # PeMS7_228 Stage 11 runner
│   ├── run_stage11_pems7_1026.sh     # PeMS7_1026 external-validation runner
│   └── run_stage11_seattle.sh        # Seattle heterogeneous-network runner
├── sumo_scenarios/                   # SUMO traffic simulation scenario assets
│   └── chengdu/                      # Chengdu SUMO network, routes, and config
├── refine-logs/                      # Research refinement, review, plan, tracker, and writing logs
├── idea-stage/                       # Idea discovery reports and candidate summaries
└── .planning/                        # GSD planning outputs and codebase maps
    ├── codebase/                     # GSD codebase map documents
    └── quick/                        # Quick-task plan and stage summaries
```

## Directory Purposes

**Repository root (`/home/samuel/projects/sensor_opt/`):**
- Purpose: Holds project-level documentation, dependency manifest, and research lifecycle records.
- Contains: `README.md`, `requirements.txt`, `MANIFEST.md`, `RESEARCH_PIPELINE_REPORT.md`, `NARRATIVE_REPORT.md`, and top-level research-output directories.
- Key files: `README.md`, `requirements.txt`, `RESEARCH_PIPELINE_REPORT.md`, `MANIFEST.md`.

**`TRC-23-02333/`:**
- Purpose: Main TRACE-SL code and experiment artifact area.
- Contains: Python experiment driver, Python aggregator, local dataset directory, Python bytecode cache, and result archive.
- Key files: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/trace_sl_results/README.md`.

**`TRC-23-02333/dataset/`:**
- Purpose: Local dataset placement for PeMS and Seattle inputs.
- Contains: Expected paths documented by `README.md`, including `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, and `TRC-23-02333/dataset/Seattle/`.
- Key files: `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv`, `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`, `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv`, `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv`, `TRC-23-02333/dataset/Seattle/tensor.npz`, `TRC-23-02333/dataset/Seattle/Loop_Seattle_2015_A.npy`.

**`TRC-23-02333/trace_sl_results/`:**
- Purpose: Stores checked-in reproducibility outputs for TRACE-SL stages and external validations.
- Contains: Stage directories, seed subdirectories, aggregate CSVs, logs, JSON outputs, and `SUMMARY.md` files.
- Key files: `TRC-23-02333/trace_sl_results/README.md`, `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md`, `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/SUMMARY.md`, `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/SUMMARY.md`.

**`scripts/`:**
- Purpose: Reproducible command wrappers for current Stage 11 experiments.
- Contains: Bash scripts with environment-variable defaults and BLAS thread controls.
- Key files: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`.

**`sumo_scenarios/chengdu/`:**
- Purpose: Stores SUMO scenario assets separate from the Python TRACE-SL PeMS/Seattle pipeline.
- Contains: SUMO network XML, route XML, SUMO config, and GUI settings.
- Key files: `sumo_scenarios/chengdu/chengdu.net.xml`, `sumo_scenarios/chengdu/chengdu.rou.xml`, `sumo_scenarios/chengdu/chengdu.sumocfg`, `sumo_scenarios/chengdu/gui-settings.cfg`.

**`refine-logs/`:**
- Purpose: Preserves research planning, refinement, review, tracker, pipeline, and writing-stage handoff documents.
- Contains: Timestamped and latest Markdown outputs from research workflow stages.
- Key files: `refine-logs/FINAL_PROPOSAL.md`, `refine-logs/EXPERIMENT_PLAN.md`, `refine-logs/EXPERIMENT_TRACKER.md`, `refine-logs/PIPELINE_SUMMARY.md`, `refine-logs/WRITING_NOTES_GREEDY_OFFLINE_PLANNING.md`.

**`idea-stage/`:**
- Purpose: Preserves idea-discovery reports and compact candidate descriptions.
- Contains: Timestamped and latest Markdown idea reports.
- Key files: `idea-stage/IDEA_REPORT.md`, `idea-stage/IDEA_CANDIDATES.md`.

**`.planning/codebase/`:**
- Purpose: Stores GSD codebase maps used by planning and execution commands.
- Contains: Stack, integration, convention, testing, architecture, and structure maps.
- Key files: `.planning/codebase/STACK.md`, `.planning/codebase/INTEGRATIONS.md`, `.planning/codebase/CONVENTIONS.md`, `.planning/codebase/TESTING.md`, `.planning/codebase/ARCHITECTURE.md`, `.planning/codebase/STRUCTURE.md`.

**`.planning/quick/260518-trace-sl-cpu-pilot/`:**
- Purpose: Stores GSD quick-task plan and stage summaries for the TRACE-SL CPU pilot evolution.
- Contains: Markdown plan and stage summary files.
- Key files: `.planning/quick/260518-trace-sl-cpu-pilot/PLAN.md`, `.planning/quick/260518-trace-sl-cpu-pilot/SUMMARY.md`, `.planning/quick/260518-trace-sl-cpu-pilot/SUMMARY_STAGE5_OR_GUIDED.md`.

## Key File Locations

**Entry Points:**
- `scripts/run_stage11_pems7_228.sh`: Reproduce PeMS7_228 Stage 11 split runs and aggregate outputs.
- `scripts/run_stage11_pems7_1026.sh`: Reproduce PeMS7_1026 external-validation split runs and aggregate outputs.
- `scripts/run_stage11_seattle.sh`: Reproduce Seattle heterogeneous-network split runs and aggregate outputs.
- `TRC-23-02333/transparent_estimator_eval.py`: Run one dataset/split experiment directly with CLI flags.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: Aggregate one or more result roots containing `seed_*` subdirectories.

**Configuration:**
- `requirements.txt`: Python package dependencies (`numpy`, `pandas`, `scipy`, `scikit-learn`).
- `scripts/run_stage11_pems7_228.sh`: Default PeMS7_228 `DATA_ROOT`, `OUTPUT_DIR`, `SEEDS`, `BUDGETS`, candidate counts, and thread variables.
- `scripts/run_stage11_pems7_1026.sh`: Default PeMS7_1026 external-validation configuration.
- `scripts/run_stage11_seattle.sh`: Default Seattle configuration.
- `TRC-23-02333/trace_sl_results/*/config.json`: Persisted CLI and split configuration for individual seed runs.

**Core Logic:**
- `TRC-23-02333/transparent_estimator_eval.py`: Dataset loading, splitting, layout generation, RCSS scoring, validation-aware swap, GSP/GLS/MAP evaluation, metric writing, and summary writing.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: Multi-split CSV aggregation, paired tests, winner counts, and aggregate Markdown summary generation.

**Testing:**
- `TRC-23-02333/trace_sl_results/sanity_loader_pems228/`: Loader sanity output for PeMS7_228.
- `TRC-23-02333/trace_sl_results/sanity_loader_pems1026/`: Loader sanity output for PeMS7_1026.
- `TRC-23-02333/trace_sl_results/sanity_loader_seattle/`: Loader sanity output for Seattle.
- `TRC-23-02333/trace_sl_results/block0_dual_sanity/`: Dual sanity run outputs.

**Documentation and Handoff:**
- `README.md`: Current project overview, primary results, dataset placement, and reproduction commands.
- `RESEARCH_PIPELINE_REPORT.md`: Current research pipeline stage and strongest evidence summary.
- `NARRATIVE_REPORT.md`: Paper-writing handoff.
- `TRC-23-02333/trace_sl_results/README.md`: Result-stage inventory and interpretation guidance.
- `MANIFEST.md`: Research artifact index.

**Result Artifacts:**
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/combined_metrics.csv`: Ten-split PeMS7_228 aggregate evaluation rows.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/gls_map_layout_summary.csv`: Ten-split PeMS7_228 GLS/MAP layout summary.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/combined_metrics.csv`: PeMS7_1026 external-validation aggregate rows.
- `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/combined_metrics.csv`: Seattle validation aggregate rows.

## Naming Conventions

**Files:**
- Python scripts use snake_case: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Reproduction shell scripts use `run_stage<stage>_<dataset>.sh`: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`.
- Result summaries use uppercase `SUMMARY.md` inside result directories: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md`.
- Aggregate CSVs use descriptive snake_case: `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `certificate_correlation_summary.csv`, `rcss_selected_sources.csv`.
- Per-seed logs use `<output_dir>_seed_<seed>.log`: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_seed_25.log`.
- Research documents use uppercase names or timestamp suffixes: `RESEARCH_PIPELINE_REPORT.md`, `refine-logs/FINAL_PROPOSAL_20260504_123915.md`.

**Directories:**
- Dataset result directories combine dataset, stage, and method: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/`, `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`, `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`.
- Per-seed directories use `seed_<integer>`: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/seed_25/`.
- Local dataset directories use dataset names expected by scripts: `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, `TRC-23-02333/dataset/Seattle/`.
- Planning directories use workflow names and dates: `.planning/quick/260518-trace-sl-cpu-pilot/`.

## Where to Add New Code

**New TRACE-SL layout method:**
- Primary code: Add the layout function near existing layout generators in `TRC-23-02333/transparent_estimator_eval.py`.
- Integration point: Add the layout tuple to the budget loop in `main()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Aggregation: Update comparison/baseline lists in `TRC-23-02333/summarize_trace_sl_rcss.py` if the new layout is part of main evidence.
- Tests/results: Write smoke or sanity outputs under a new directory such as `TRC-23-02333/trace_sl_results/<dataset>_<stage>_<method>/`.

**New reconstruction evaluator:**
- Primary code: Add predictor/evaluation helpers near `evaluate_layout()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Integration point: Append a method row in `evaluate_layout()` in `TRC-23-02333/transparent_estimator_eval.py`.
- CLI: Add a `--selection-method` choice in `TRC-23-02333/transparent_estimator_eval.py` if the method can drive validation selection.
- Aggregation: Ensure `TRC-23-02333/summarize_trace_sl_rcss.py` filters/summarizes the correct method rows if the main method changes.

**New dataset adapter:**
- Primary code: Add loader logic near `load_pems_dataset()` and `load_seattle_dataset()` in `TRC-23-02333/transparent_estimator_eval.py`.
- Data placement: Add local files under `TRC-23-02333/dataset/<DatasetName>/`.
- Runner: Add a script under `scripts/run_stage11_<dataset>.sh` following `scripts/run_stage11_pems7_1026.sh` or `scripts/run_stage11_seattle.sh`.
- Documentation: Update `README.md` and `TRC-23-02333/trace_sl_results/README.md` when the dataset has curated results.

**New experiment stage:**
- Primary code: Prefer CLI/environment changes in a new `scripts/run_stage<stage>_<dataset>.sh` over hard-coding experiment constants in `TRC-23-02333/transparent_estimator_eval.py`.
- Outputs: Use `TRC-23-02333/trace_sl_results/<dataset>_stage<stage>_<short_description>/`.
- Summary: Run `TRC-23-02333/summarize_trace_sl_rcss.py` after all seed runs.
- Documentation: Add result interpretation to `TRC-23-02333/trace_sl_results/README.md`, `RESEARCH_PIPELINE_REPORT.md`, or `README.md` as appropriate.

**New aggregation metric or table:**
- Primary code: Add aggregation logic in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Inputs: Reuse `combined`, `gls`, `pivot`, `correlations`, or `rcss` data frames already built in `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Outputs: Write a descriptive CSV to `--output-dir` and add it to the generated `SUMMARY.md` output-file list.

**New SUMO scenario asset:**
- Primary files: Add scenario files under `sumo_scenarios/<city_or_network>/`.
- Required files: Follow the Chengdu pattern with `<name>.net.xml`, `<name>.rou.xml`, `<name>.sumocfg`, and optional `gui-settings.cfg`.
- TRACE-SL use: Add a dataset conversion/loader path in `TRC-23-02333/transparent_estimator_eval.py` before treating SUMO scenario data as experiment input.

**Utilities:**
- Shared numerical helpers: Keep small helpers in `TRC-23-02333/transparent_estimator_eval.py` near related functions unless multiple scripts need them.
- Cross-script helpers: Create a new Python module under `TRC-23-02333/` only when both `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py` need the same logic.
- Shell wrappers: Put reproducibility wrappers in `scripts/` and use environment-variable defaults as in `scripts/run_stage11_pems7_228.sh`.

## Special Directories

**`TRC-23-02333/dataset/`:**
- Purpose: Local input data for PeMS and Seattle experiments.
- Generated: No; populated manually from external datasets.
- Committed: No for datasets; `README.md` states datasets are intentionally not committed.

**`TRC-23-02333/trace_sl_results/`:**
- Purpose: Curated reproducibility outputs and local sanity run outputs.
- Generated: Yes, by `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Committed: Yes for curated result stages and documented artifacts.

**`TRC-23-02333/__pycache__/`:**
- Purpose: Python bytecode cache generated by interpreter execution.
- Generated: Yes.
- Committed: Not intended for source changes.

**`.planning/codebase/`:**
- Purpose: GSD codebase map documents for stack, integrations, conventions, testing, architecture, and structure.
- Generated: Yes, by GSD mapping workflows.
- Committed: Yes when planning artifacts are tracked.

**`.planning/quick/260518-trace-sl-cpu-pilot/`:**
- Purpose: GSD quick-task planning and summary artifacts for TRACE-SL CPU pilot stages.
- Generated: Yes, by GSD quick workflows.
- Committed: Yes as planning/research documentation.

**`refine-logs/`:**
- Purpose: Research refinement and review history.
- Generated: Yes, by research workflow commands.
- Committed: Yes as research documentation.

**`idea-stage/`:**
- Purpose: Idea-discovery history and compact candidate reports.
- Generated: Yes, by idea-discovery workflow commands.
- Committed: Yes as research documentation.

**`sumo_scenarios/`:**
- Purpose: Standalone SUMO scenario assets.
- Generated: Mixed; XML/config files are scenario assets rather than TRACE-SL generated result artifacts.
- Committed: Yes.

---

*Structure analysis: 2026/05/21*
