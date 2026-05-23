---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: executing
stopped_at: Completed 06-01-PLAN.md
last_updated: "2026-05-23T04:22:39Z"
progress:
  total_phases: 6
  completed_phases: 5
  total_plans: 17
  completed_plans: 16
  percent: 94
---

# GSD State: TRACE-SL Transportation Science Readiness

**Initialized:** 2026/05/21
**Status:** Phase 06 In Progress

## Project Reference

See: .planning/PROJECT.md (updated 2026/05/21)

**Core value:** Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where formulation, theory, baselines, robustness tests, and held-out evidence support them.
**Current focus:** Phase 06 — reproducibility-and-artifact-curation

## Workflow Configuration

- **Mode:** YOLO
- **Granularity:** Standard
- **Execution:** Parallel where independent
- **Planning docs:** Committed to git
- **Research before each phase:** No
- **Plan check:** Yes
- **Verifier:** Yes
- **Model profile:** Balanced

## Current Roadmap

1. Claim-Evidence Contract
2. Formulation and Theory Bridge
3. Baseline Portfolio
4. Core Experiment Evidence
5. Robustness and Generality
6. Reproducibility and Artifact Curation

## Active Decisions

- Transportation Science is the primary target; TR Part B remains a backup/extension path.
- Strong claims should be preserved, not weakened, but every claim must be backed by evidence or constrained wording.
- Use “certificate-guided” unless later theory justifies formal certification language.
- Treat the low-budget multistart-vs-RCSS issue directly.
- Seattle evidence must be curated or removed from the core claim set.
- Phase 4 Plan 01 uses held-out GLS/MAP `combined_metrics.csv` rows as final performance evidence; validation MAE remains selection-only.
- Phase 4 Plan 01 marks missing Phase 3 portfolio rows in PeMS7_228 Stage 11 as Stage 12 regeneration-required.
- Phase 4 Plan 01 keeps PeMS7_1026 as lower-power external evidence and Seattle as curation-required until later Phase 4 plans close them.
- Phase 4 Plan 02 keeps the existing TRACE-SL summarizer as the main aggregation point while adding paired interval/effect-size statistics and empirical certificate-count summaries.
- Phase 4 Plan 03 regenerated complete PeMS7_228 Stage 12 ten-split baseline-portfolio evidence because no prior Stage 12 seed metrics existed and local data was available.
- Phase 4 Plan 03 keeps the 10% multistart caveat visible via Stage 12 paired layout-summary rows rather than hiding it with post-hoc method selection.
- Phase 4 Plan 06 uses `validate_phase4_evidence.py` as the final smoke/schema/status gate for EXP-01..EXP-06.
- Phase 4 Plan 06 limits final WARN statuses to PeMS7_1026 lower-power external evidence and Seattle supporting/conditional evidence.
- Phase 5 Plan 01 keeps validation selection unperturbed while applying robustness only at held-out evaluate_layout boundaries.
- Phase 5 Plan 02 uses `condition_group_columns(frame)` so robustness, candidate-count, and split condition columns are grouped before aggregate summaries.
- Phase 5 Plan 02 frames robustness tables as stress-test evidence for evaluated perturbations, not universal robustness proof.
- Stage 14 robustness uses a reduced PeMS7_228 bundle with nine stress-test conditions as artifact-backed evidence, not as a universal robustness proof.
- Stage 14 candidate sensitivity completed all 50/100/200/500 reduced runs locally, so no ROBUST-06 caveat artifact was needed.
- Phase 5 Plan 04 uses `validate_phase5_robustness.py` as the final fail-closed ROBUST-01..06 Stage 14 evidence gate.
- Phase 5 robustness claims are bounded to tested Stage 14 perturbations and candidate-pool settings, with ROBUST-06 caveats accepted only by validator-recognized `candidate_sensitivity_caveat.json`.
- Phase 6 Plan 01 represents raw datasets only through path-count hygiene metadata and excludes them from evidence artifact inventories.
- Phase 6 Plan 01 records latest input-affecting git commit while excluding generated manifest outputs to keep manifest reruns idempotent.
- Phase 6 Plan 02 generates manuscript-facing paper sources only from committed aggregate CSVs and fails closed on untracked, missing, empty, or out-of-scope sources.
- Phase 6 Plan 02 preserves `source_stage`, `source_dir`, and `source_csv` on every generated paper-source row for REPRO-01/04 traceability.
- Phase 6 Plan 02 exposes only curated Stage 14 and `paper_sources/` result directories through `.gitignore` exceptions; raw datasets remain ignored.

## Next Action

Execute Phase 06 Plan 03.

## Last Session

- **Completed:** 2026-05-23T04:22:39Z
- **Stopped At:** Completed 06-01-PLAN.md
- **Resume File:** None

## Performance Metrics

| Phase | Plan | Duration | Tasks | Files |
|-------|------|----------|-------|-------|
| 04-core-experiment-evidence | 02 | 12min | 2 | 2 |
| 04-core-experiment-evidence | 03 | 25min | 2 | 113 |
| 04-core-experiment-evidence | 06 | 6min | 2 | 4 |
| 05-robustness-and-generality | 01 | ~20min | 3 | 3 |
| Phase 05-robustness-and-generality P02 | 5min | 2 tasks | 3 files |
| 05-robustness-and-generality | 03 | 22min | 3 | 303 |
| 05-robustness-and-generality | 04 | 20min | 3 | 4 |
| 06-reproducibility-and-artifact-curation | 02 | 5min | 2 | 10 |
| 06-reproducibility-and-artifact-curation | 01 | 8min | 2 | 4 |
