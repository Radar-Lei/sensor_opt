---
gsd_state_version: 1.0
milestone: v1.2
milestone_name: TRACE-SL Transportation Research Part B Manuscript Drafting
status: drafting
last_updated: "2026-05-26T11:39:00.000Z"
last_activity: 2026-05-26
progress:
  total_phases: 6
  completed_phases: 0
  total_plans: 6
  completed_plans: 0
  percent: 0
---

# GSD State: TRACE-SL Transportation Research Part B Readiness

## Project Reference

See: .planning/PROJECT.md (updated 2026/05/26)

**Core value:** Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where formulation, theory, baselines, robustness tests, and held-out evidence support them.
**Current focus:** v1.2 TR Part B manuscript drafting from the frozen v1.1 paper-source foundation using `els-cas-templates` and `$paper-writing`.

## Current Position

Phase: Not started (defining requirements)
Plan: —
Status: Requirements and roadmap defined; first targeted TR-B manuscript revision completed in draft assurance mode
Last activity: 2026-05-26 — `$paper-writing` quick revision added formal theory, algorithm details, external baseline table, expanded related work, and reproducibility notes

Progress: [░░░░░░░░░░] 0%

## Performance Metrics

## Quick Tasks Completed

| Date | Quick ID | Slug | Summary |
|------|----------|------|---------|
| 2026-05-26 | 260526-r4c | trace-sl-tr-b-theory-algorithm-details-e | Revised TRACE-SL TR-B draft with formal theory, algorithm tables, external baseline comparisons, expanded experiments/related work, and compiled `paper/main.pdf`. |

**Velocity:**

- Total plans completed this milestone: 10
- Average duration: 6min
- Total execution time: 1.0 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 7. Claim and Main Table Contract | 2/2 | 10min | 5min |
| 8. External Stage12 Evidence | 5/5 | 44min | 9min |
| 8.5. Stage12 Performance Unblock | 1/4 | 3min | 3min |
| 9. Ablation and Evidence Classification | 3/3 | 14min | 5min |
| 10. Theory and Handoff Package | 1/1 | 4min | 4min |
| 07 | 2 | - | - |
| 08 | 1 | 5min | 5min |
| 08.5 | 4 | - | - |

**Historical Trend Before Closure:**

- Last 5 plans: 08-01, 08-02, 08-03, 08-04, 08-05
- Trend: Phase 8 initially produced fail-closed external Stage12 gate artifacts; the later formal closure run completed EVID-03/EVID-04 and opened the gate.

| Phase 08 P02 | 12min | 2 tasks | 1 files |
| Phase 08 P03 | blocked status | Seattle Stage12 | EVID-04 incomplete |
| Phase 08 P04 | pre-closure gate generated | 2 contract rows | later reopened by Stage12 closure |
| Phase 08.5 P01 | 3min | 3 tasks | 2 files |
| Phase 08.5 P02 | 6min | 3 tasks | 2 files |
| Phase 08.5 P03 | 11min | 3 tasks | 5 files |
| Phase 08.5 P04 | 80min | 3 tasks | 11 files |
| Phase 09 P01 | 5min | 2 tasks | 4 files |
| Phase 09 P02 | 4min | 2 tasks | 8 files |

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table. Recent decisions affecting current work:

- v1.1 must freeze claim-evidence-theory-experiment foundation before manuscript drafting.
- PeMS7_1026 Stage12 10-split external evidence is mandatory for stronger external PeMS claims.
- Seattle Stage12 10-split external/transfer-style evidence is mandatory before Seattle enters any core claim.
- Remaining Stage12 closure runs for EVID-03/EVID-04 must use max_jobs=1, with only one active dataset/split/seed job at a time.
- PeMS7_228 low-budget multistart caveat must remain visible in claim-facing artifacts.
- Raw traffic datasets remain local/ignored and must not be committed.
- Phase 7 claim-facing evidence uses held-out Stage12 PeMS7_228 test aggregates and paired comparisons, not validation MAE.
- PeMS7_1026 and Seattle have completed tracked Phase 8 Stage12 10-split evidence and may be used according to the regenerated external evidence gate.
- Robustness evidence remains stress-test or appendix routed unless a row explicitly declares multi-seed perturbation evidence.
- Keep Phase 7 contract outputs CSV/JSON-first, with Markdown as generated views rather than manuscript prose.
- Use the plan-required trace_sl_claim_contract_v1 schema marker as the machine-readable policy identifier.
- Treat PeMS7_1026 and Seattle as completed external Stage12 evidence lanes after Phase 8 closure; robustness evidence remains non-core stress-test/appendix evidence unless stronger perturbation evidence is added.
- External Stage12 completion requires existing, git-tracked aggregate artifacts and exactly ten split seeds; untracked aggregates remain pending_tracking rather than complete.
- Seattle is no longer blocked by the external gate because tracked ten-split Stage12 evidence is complete and `stage12_status.json` reports completion; still avoid universal transfer/generalization wording.
- [Phase 08 Closure]: PeMS7_1026 Stage12 formal closure completed ten split seeds 25-34 with tracked aggregate and seed-level artifacts; EVID-03 is complete.
- [Phase 08 Closure]: Seattle Stage12 formal closure completed ten split seeds 25-34, `stage12_status.json` reports completed, and tracked aggregate/seed-level artifacts exist; EVID-04 is complete.
- [Phase 08 Closure]: `paper_sources/external_evidence_gate.json` is the machine gate: `v1_1_completion_allowed=true`, `pems7_1026_stage12_complete=true`, `seattle_stage12_complete=true`, and `seattle_core_claim_blocked=false`.
- [Phase 8.5]: Stage12 performance unblock is required before Phase 9. Scope is runtime-only: fast validation, dense solve/posterior metric caching, progress checkpoints, and one full Stage12-compatible seed each for PeMS7_1026 and Seattle. Downscaled diagnostics and DRY_RUN outputs remain non-evidence.
- [Phase 08.5 Plan 01]: validation_mae computes only args.selection_method and no longer calls evaluate_layout or certificate during RCSS candidate scoring.
- [Phase 08.5 Plan 01]: solve_quadratic collapses scalar, vector, and time-constant observation weights into one Cholesky-backed SPD solve while preserving stacked lhs for true time-varying weights.
- [Phase 08.5]: Plan 02 posterior/scenario metric caching is explicit and local, using optional trace_cache dictionaries and Woodbury selected-sensor systems without changing RCSS or validation-swap search semantics.
- [Phase 08.5]: Plan 02 external evidence gate artifacts remain fail-closed; EVID-03 and EVID-04 are still incomplete after runtime-only cache work.
- [Phase 08.5 Plan 03]: Stage12 progress/checkpoint records serialize only metadata, stages, counts, budgets, seeds, and non-evidence feasibility markers; raw arrays and observation values are excluded.
- [Phase 08.5 Plan 03]: Stage12 launchers enable per-seed progress artifacts under OUTPUT_DIR/progress by default while preserving ten-split defaults and fail-closed evidence gates.
- [Phase 08.5 Plan 04]: RUN-04 complete; PeMS7_1026 and Seattle each completed one Stage12-compatible seed, while EVID-03/EVID-04 remain incomplete until ten-split evidence exists.
- [Phase 08.5 Plan 04]: validation-swap trial rows compute validation MAE only while selected rows keep full diagnostics; scalar-weight validation MAE uses selected-sensor Woodbury gains.
- [Phase 09 Plan 01]: Phase 9 ablation contracts use held-out Stage12 PeMS7_228 aggregates as the core evidence basis; validation MAE is selection evidence only, not held-out test evidence.
- [Phase 09 Plan 01]: PeMS7_1026 and Seattle classification preserves external_evidence_gate.json truth; Stage11, DRY_RUN, and one-seed Stage12 feasibility artifacts are non-evidence for EVID-03/EVID-04 completion.
- [Phase 09 Plan 01]: Robustness remains appendix-only/supporting stress-test evidence unless future multi-seed perturbation evidence is explicitly added.
- [Phase 09]: Plan 02 paper-source artifacts expose explicit ablation layer fields, evidence_class vocabulary, and fail-closed external gate snapshots for downstream writing without changing EVID-03/EVID-04.
- [Phase 09]: Plan 02 keeps PeMS7_1026 and Seattle conditional and non-core in dataset classification until complete tracked ten-split Stage12 aggregate evidence exists.
- [Phase 09 Plan 03]: Phase 9 requirements ABLT-01 through ABLT-04 and EVID-05 are complete because `ablation_contract.csv` and `dataset_evidence_classification.csv` exist as generated CSV/JSON-first paper-source artifacts.
- [Phase 09 Plan 03]: PeMS7_228 remains the core in-domain ablation dataset; PeMS7_1026 and Seattle remain non-core/conditional until `external_evidence_gate.json` allows EVID-03/EVID-04 ten-split Stage12 completion.
- [Phase 09 Plan 03]: Manuscript prose remains deferred; Phase 9 artifacts are row-level planning and paper-source evidence, not introduction, method, results, limitations, abstract, or conclusion text.
- [Phase 09 Plan 03]: Roadmap now lists 09-01, 09-02, and 09-03 as a complete three-wave Phase 9 structure; Phase 10 remains not started and ready for planning.
- [Phase 10 Plan 01]: Theory statement contracts provide row-level scoped statements for formulation, posterior trace identity, monotonicity, validation-aware one-swap local optimality, and RCSS workload complexity.
- [Phase 10 Plan 01]: Paper-foundation handoff manifest links claim/table/evidence/theory artifacts to committed generated sources and manifests without raw dataset paths or manuscript prose.
- [Phase 10 Plan 01]: Phase 10 completion did not change EVID-03/EVID-04; the later formal Stage12 closure run opened the external evidence gate.
- [v1.2]: User corrected the manuscript target from Transportation Science to Transportation Research Part B before writing began.
- [v1.2]: Use local `els-cas-templates/` as the paper source template and run `$paper-writing` with `assurance: submission`.
- [v1.2]: Skip additional pre-requirements research; base the writing milestone on `NARRATIVE_REPORT.md` and v1.1 paper-source artifacts.

### Pending Todos

None yet.

### Blockers/Concerns

- No active EVID-03/EVID-04 blocker remains after the formal Stage12 closure run.
- Downstream generated artifacts should remain synchronized with the completed external evidence gate during manuscript drafting.
- Submission assurance is required: proof, claim, citation, and external verifier artifacts must be present before declaring submission readiness.
- Paper generation should not commit raw datasets or introduce unsupported global optimality/generalization claims.

## Deferred Items

| Category | Item | Status | Deferred At |
|----------|------|--------|-------------|
| Submission packaging | SUBMIT-01 through SUBMIT-03 | Deferred to post-draft submission-preparation milestone | v1.2 scope definition |
| Theory/evidence patches | PATCH-01 through PATCH-03 | Deferred unless audits expose blockers | v1.2 scope definition |

## Session Continuity

Last session: 2026-05-26T00:00:00.000+08:00
Stopped at: v1.2 initialized for TR Part B manuscript drafting
Resume file: None
