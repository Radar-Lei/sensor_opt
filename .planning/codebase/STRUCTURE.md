# Codebase Structure

**Analysis Date:** 2026/05/21

## Directory Layout

```
/home/samuel/projects/sensor_opt/
├── README.md                         # TRACE-SL overview, claims, data placement, and reproduction commands
├── requirements.txt                  # Minimal Python dependency list
├── MANIFEST.md                       # ARIS/research artifact manifest
├── NARRATIVE_REPORT.md               # Writing handoff and method narrative
├── RESEARCH_PIPELINE_REPORT.md       # Research pipeline progress report
├── idea-stage/                       # Idea discovery reports and candidate notes
├── refine-logs/                      # Experiment plans, review summaries, and refinement reports
├── scripts/                          # Reproduction shell launchers for Stage 11 experiments
├── sumo_scenarios/                   # SUMO scenario files for Chengdu traffic simulation assets
├── TRC-23-02333/                     # TRACE-SL implementation, datasets, and result artifacts
│   ├── transparent_estimator_eval.py # Main TRACE-SL evaluator and RCSS experiment driver
│   ├── summarize_trace_sl_rcss.py    # Multi-split aggregation script
│   ├── dataset/                      # Local ignored PeMS/Seattle datasets
│   └── trace_sl_results/             # Curated and local experiment outputs
└── .planning/codebase/               # Regenerated GSD codebase maps
```

## Directory Purposes

**Repository root `/home/samuel/projects/sensor_opt`:**
- Purpose: Holds project documentation, Python requirements, TRACE-SL implementation directories, and research workflow artifacts.
- Contains: Markdown reports, `.gitignore`, `requirements.txt`, `scripts/`, `TRC-23-02333/`, `sumo_scenarios/`, `idea-stage/`, `refine-logs/`, and `.planning/`.
- Key files: `README.md`, `requirements.txt`, `MANIFEST.md`, `NARRATIVE_REPORT.md`, `RESEARCH_PIPELINE_REPORT.md`, `.gitignore`.

**`TRC-23-02333/`:**
- Purpose: Primary TRACE-SL code and artifact workspace.
- Contains: Main evaluator, summarizer, ignored local datasets, curated result stages, Python cache files, and TRACE-SL outputs.
- Key files: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, `TRC-23-02333/trace_sl_results/README.md`.

**`TRC-23-02333/dataset/`:**
- Purpose: Local dataset placement for PeMS7_228, PeMS7_1026, and Seattle inputs.
- Contains: `TRC-23-02333/dataset/PeMS7_228/`, `TRC-23-02333/dataset/PeMS7_1026/`, and `TRC-23-02333/dataset/Seattle/`.
- Key files: `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv`, `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`, `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv`, `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv`, `TRC-23-02333/dataset/Seattle/tensor.npz`, `TRC-23-02333/dataset/Seattle/Loop_Seattle_2015_A.npy`.
- Special handling: Ignored by `.gitignore`; keep local datasets on disk but do not commit them.

**`TRC-23-02333/trace_sl_results/`:**
- Purpose: Stores TRACE-SL reproducibility outputs and aggregate evidence.
- Contains: Stage directories, seed logs, aggregate CSVs, per-seed outputs, and result README.
- Key files: `TRC-23-02333/trace_sl_results/README.md`, `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md`, `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/SUMMARY.md`.
- Committed scope: `.gitignore` curates Stage 6--11 PeMS7_228 outputs and PeMS7_1026 Stage 11 outputs; new stages need explicit review before commit.

**`scripts/`:**
- Purpose: Provides shell entry points for reproducing Stage 11 experiments.
- Contains: Bash launchers with environment-variable defaults for data roots, output directories, seeds, budgets, candidate counts, validation-swap settings, and BLAS thread caps.
- Key files: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`.

**`sumo_scenarios/`:**
- Purpose: Holds SUMO traffic simulation scenario assets separate from the current TRACE-SL PeMS/Seattle evaluator.
- Contains: `sumo_scenarios/chengdu/` with network, route, SUMO config, and GUI settings.
- Key files: `sumo_scenarios/chengdu/chengdu.net.xml`, `sumo_scenarios/chengdu/chengdu.rou.xml`, `sumo_scenarios/chengdu/chengdu.sumocfg`, `sumo_scenarios/chengdu/gui-settings.cfg`.

**`idea-stage/`:**
- Purpose: Holds idea discovery artifacts and timestamped research idea reports.
- Contains: Candidate reports and idea reports in Markdown.
- Key files: `idea-stage/IDEA_REPORT.md`, `idea-stage/IDEA_CANDIDATES.md`, `idea-stage/IDEA_REPORT_20260521_194859.md`.

**`refine-logs/`:**
- Purpose: Holds experiment plans, trackers, final proposals, pipeline summaries, refinement reports, and review summaries.
- Contains: Latest and timestamped Markdown files from ARIS research workflows.
- Key files: `refine-logs/EXPERIMENT_PLAN.md`, `refine-logs/EXPERIMENT_TRACKER.md`, `refine-logs/FINAL_PROPOSAL.md`, `refine-logs/WRITING_NOTES_GREEDY_OFFLINE_PLANNING.md`.

**`.planning/codebase/`:**
- Purpose: Holds regenerated GSD codebase maps consumed by planning/execution commands.
- Contains: `ARCHITECTURE.md`, `STRUCTURE.md`, and other codebase map documents when regenerated.
- Key files: `.planning/codebase/ARCHITECTURE.md`, `.planning/codebase/STRUCTURE.md`.

## Key File Locations

**Entry Points:**
- `scripts/run_stage11_pems7_228.sh`: Main Stage 11 PeMS7_228 reproducibility launcher.
- `scripts/run_stage11_pems7_1026.sh`: Stage 11 PeMS7_1026 external-validation launcher.
- `scripts/run_stage11_seattle.sh`: Stage 11 Seattle launcher.
- `TRC-23-02333/transparent_estimator_eval.py`: Direct single-run evaluator entry point.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: Direct aggregation entry point for one or more result roots.

**Configuration:**
- `requirements.txt`: Python package requirements: NumPy, pandas, SciPy, and scikit-learn.
- `.gitignore`: Dataset, result, and artifact tracking rules; keeps `TRC-23-02333/dataset/` ignored and curates committed result stages.
- `scripts/run_stage11_pems7_228.sh`: Default PeMS7_228 data/output roots, seeds, budgets, candidate counts, swap settings, and BLAS thread variables.
- `scripts/run_stage11_pems7_1026.sh`: Default PeMS7_1026 data/output roots and lighter candidate counts.
- `scripts/run_stage11_seattle.sh`: Default Seattle data/output roots and lighter candidate counts.
- `TRC-23-02333/transparent_estimator_eval.py`: CLI argument definitions for datasets, budgets, methods, RCSS, swap, seeds, and numerical weights.

**Core Logic:**
- `TRC-23-02333/transparent_estimator_eval.py`: Dataset loading, preprocessing, reconstruction, layout generation, RCSS scoring, validation swap, evaluation, and per-seed artifact writing.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: Multi-split aggregation, delta calculations, paired tests, certificate summaries, selected-source summaries, and aggregate Markdown writing.

**Dataset Inputs:**
- `TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv`: PeMS7_228 traffic value matrix expected by `load_pems_dataset()`.
- `TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv`: PeMS7_228 distance/weight matrix expected by `load_pems_dataset()`.
- `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv`: PeMS7_1026 traffic value matrix expected by `load_pems_dataset()`.
- `TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv`: PeMS7_1026 distance/weight matrix expected by `load_pems_dataset()`.
- `TRC-23-02333/dataset/Seattle/tensor.npz`: Seattle tensor expected by `load_seattle_dataset()`.
- `TRC-23-02333/dataset/Seattle/Loop_Seattle_2015_A.npy`: Seattle adjacency matrix expected by `load_seattle_dataset()`.

**Result Artifacts:**
- `TRC-23-02333/trace_sl_results/README.md`: Stage inventory and guidance for interpreting current outputs.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/`: Original five-split PeMS7_228 Stage 11 output root.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`: Ten-split PeMS7_228 Stage 11 aggregate output root.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`: PeMS7_1026 external-validation Stage 11 output root.
- `TRC-23-02333/trace_sl_results/<stage>/seed_<seed>/metrics.csv`: Per-seed evaluation table produced by `TRC-23-02333/transparent_estimator_eval.py`.
- `TRC-23-02333/trace_sl_results/<stage>/seed_<seed>/layouts.json`: Per-seed sensor layout metadata produced by `TRC-23-02333/transparent_estimator_eval.py`.
- `TRC-23-02333/trace_sl_results/<stage>/seed_<seed>/rcss_candidates.csv`: Per-seed RCSS candidate diagnostics produced by `TRC-23-02333/transparent_estimator_eval.py`.
- `TRC-23-02333/trace_sl_results/<stage>/combined_metrics.csv`: Aggregate metrics produced by `TRC-23-02333/summarize_trace_sl_rcss.py`.
- `TRC-23-02333/trace_sl_results/<stage>/SUMMARY.md`: Human-readable per-seed or aggregate summary.

**Testing:**
- Not detected. There is no dedicated `tests/` directory, no `*_test.py` files, and no pytest/unittest configuration in the repository structure.
- Use small smoke runs through `TRC-23-02333/transparent_estimator_eval.py --max-test-steps <N> --num-layouts <N> --output-dir TRC-23-02333/trace_sl_results/<smoke_dir>` when validating architectural changes.

**Documentation and Planning:**
- `README.md`: Top-level TRACE-SL method description, claims, data placement, and reproduction commands.
- `MANIFEST.md`: Research artifact manifest and lifecycle tracking.
- `NARRATIVE_REPORT.md`: Method narrative and writing handoff.
- `RESEARCH_PIPELINE_REPORT.md`: Research pipeline progress log.
- `refine-logs/`: Experiment/refinement documentation.
- `.planning/codebase/ARCHITECTURE.md`: Architecture map regenerated for GSD planning.
- `.planning/codebase/STRUCTURE.md`: Structure map regenerated for GSD planning.

## Naming Conventions

**Files:**
- Python scripts use snake_case: `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Shell launchers use `run_stage<stage>_<dataset>.sh`: `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`.
- Result directories encode dataset, stage, and method variant: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`.
- Per-seed directories use `seed_<number>`: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/seed_25/`.
- Result files use descriptive snake_case: `combined_metrics.csv`, `gls_map_layout_summary.csv`, `certificate_correlation_summary.csv`, `rcss_selected_sources.csv`.
- Markdown research artifacts use uppercase descriptive names: `README.md`, `MANIFEST.md`, `NARRATIVE_REPORT.md`, `refine-logs/EXPERIMENT_PLAN.md`.
- Timestamped research reports append compact datestamps: `idea-stage/IDEA_REPORT_20260521_194859.md`.

**Directories:**
- TRACE-SL result directories use lowercase dataset/stage/method names separated by underscores: `pems7_1026_stage11_auto_weight`.
- Dataset directories preserve source naming where applicable: `TRC-23-02333/dataset/PeMS7_228`, `TRC-23-02333/dataset/PeMS7_1026`, `TRC-23-02333/dataset/Seattle`.
- Research workflow directories use hyphenated names: `idea-stage/`, `refine-logs/`, `sumo_scenarios/`.

## Where to Add New Code

**New TRACE-SL Layout/Search Feature:**
- Primary code: Add a helper function in `TRC-23-02333/transparent_estimator_eval.py` near related layout functions such as `greedy_posterior_layout()`, `scenario_greedy_layout()`, `robust_coverage_cvar_layout()`, or `validation_swap_search()`.
- CLI wiring: Add argparse flags in `main()` in `TRC-23-02333/transparent_estimator_eval.py` and integrate them inside the budget loop.
- Run script wiring: Add environment-variable defaults or flags in `scripts/run_stage11_pems7_228.sh` and mirror only when needed in `scripts/run_stage11_pems7_1026.sh` or `scripts/run_stage11_seattle.sh`.
- Outputs: Add metadata fields to `layout_records`, `swap_records`, or `rcss_records` in `TRC-23-02333/transparent_estimator_eval.py`.

**New Reconstruction Evaluator:**
- Primary code: Add predictor/evaluator helpers in `TRC-23-02333/transparent_estimator_eval.py` near `historical_mean_predict()`, `neighbor_average_predict()`, and `solve_quadratic()`.
- Evaluation hook: Extend `evaluate_layout()` in `TRC-23-02333/transparent_estimator_eval.py` to append a new method row.
- Selection support: Add the method name to `--selection-method` choices in `TRC-23-02333/transparent_estimator_eval.py` if it should drive validation selection.
- Aggregation: Update `TRC-23-02333/summarize_trace_sl_rcss.py` if aggregate summaries should focus on the new method rather than `gls_map`.

**New Dataset Loader:**
- Primary code: Add a loader in `TRC-23-02333/transparent_estimator_eval.py` near `load_pems_dataset()` and `load_seattle_dataset()`.
- Integration: Extend `load_pems_dataset()` or create a dispatch helper keyed by `--data-root` contents.
- Data placement: Add local files under `TRC-23-02333/dataset/<DatasetName>/` and keep them ignored unless there is explicit approval to track small metadata.
- Reproduction script: Add `scripts/run_stage11_<dataset>.sh` following the pattern in `scripts/run_stage11_pems7_1026.sh`.

**New Aggregation Metric or Table:**
- Primary code: Add calculations in `TRC-23-02333/summarize_trace_sl_rcss.py` after `combined`/`gls` DataFrames are created.
- Outputs: Write new CSV files under the aggregate `output_dir` and list them in the generated `SUMMARY.md` output-file section.
- Documentation: Update `TRC-23-02333/trace_sl_results/README.md` only when the artifact is part of curated result interpretation.

**New Experiment Stage:**
- Primary code: Prefer reusing `TRC-23-02333/transparent_estimator_eval.py` with new CLI flags rather than creating a copy.
- Launcher: Add a new script under `scripts/` if the stage has reusable defaults, e.g. `scripts/run_stage12_<dataset>.sh`.
- Result location: Write to `TRC-23-02333/trace_sl_results/<dataset>_stage<stage>_<descriptor>/`.
- Git hygiene: Update `.gitignore` only if the new result stage is intentionally curated for commit.

**Utilities:**
- Shared numerical helpers: Add to `TRC-23-02333/transparent_estimator_eval.py` near related functions until the script is intentionally modularized.
- Result-only utilities: Add to `TRC-23-02333/summarize_trace_sl_rcss.py` if they only process generated artifacts.
- Shell utilities: Add to `scripts/` if they are reproducible run entry points; avoid placing executable logic in `refine-logs/` or `idea-stage/`.

**Tests or Validation Harnesses:**
- Current location: Not established.
- Recommended path for new automated tests: `tests/` at repository root, with small synthetic arrays and functions imported from `TRC-23-02333/transparent_estimator_eval.py` after accounting for the hyphenated directory name.
- Current smoke validation path: Write temporary outputs under `TRC-23-02333/trace_sl_results/<smoke_or_sanity_name>/` and keep them uncommitted unless curated.

**Research Documentation:**
- Method framing and claims: Update `README.md` and `NARRATIVE_REPORT.md`.
- Experiment plans and trackers: Update `refine-logs/EXPERIMENT_PLAN.md` and `refine-logs/EXPERIMENT_TRACKER.md`.
- New idea reports: Add to `idea-stage/` using the existing `IDEA_REPORT_YYYYMMDD_HHMMSS.md` naming pattern.

## Special Directories

**`TRC-23-02333/dataset/`:**
- Purpose: Local storage for large traffic datasets used by TRACE-SL loaders.
- Generated: No; populated manually or externally.
- Committed: No; ignored by `.gitignore`.

**`TRC-23-02333/trace_sl_results/`:**
- Purpose: Stores generated per-seed and aggregate TRACE-SL outputs.
- Generated: Yes; generated by `TRC-23-02333/transparent_estimator_eval.py` and `TRC-23-02333/summarize_trace_sl_rcss.py`.
- Committed: Partially; `.gitignore` allows curated Stage 6--11 PeMS7_228 outputs, PeMS7_1026 Stage 11 outputs, and selected logs.

**`TRC-23-02333/__pycache__/`:**
- Purpose: Python bytecode cache.
- Generated: Yes.
- Committed: No; ignored through `__pycache__/` in `.gitignore`.

**`scripts/`:**
- Purpose: Reproducible run launchers.
- Generated: No.
- Committed: Yes for curated scripts listed in `.gitignore` exceptions.

**`sumo_scenarios/`:**
- Purpose: SUMO traffic scenario assets separate from the current PeMS/Seattle numerical pipeline.
- Generated: No for checked-in scenario files.
- Committed: Yes.

**`idea-stage/`:**
- Purpose: Idea discovery and candidate reports.
- Generated: Yes by research workflow tools or manual research writing.
- Committed: Yes for current Markdown artifacts.

**`refine-logs/`:**
- Purpose: Experiment plans, trackers, proposal revisions, pipeline summaries, and review logs.
- Generated: Yes by research workflow tools or manual research writing.
- Committed: Yes for current Markdown artifacts.

**`.planning/codebase/`:**
- Purpose: GSD mapping documents for future planning and execution.
- Generated: Yes by `/gsd:map-codebase`.
- Committed: Project-dependent; current files are being regenerated after deletion.

**Project skill directories:**
- Purpose: Not applicable.
- Generated: Not detected.
- Committed: Not detected; neither `.claude/skills/` nor `.agents/skills/` exists in `/home/samuel/projects/sensor_opt`.

---

*Structure analysis: 2026/05/21*
