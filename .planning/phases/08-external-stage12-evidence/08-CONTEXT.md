# Phase 8: External Stage12 Evidence - Context

**Gathered:** 2026-05-25
**Status:** Blocked — performance optimization required before Stage12 retry
**Mode:** Updated after attempted real Stage12 execution

<domain>
## Phase Boundary

This phase is responsible for completing mandatory Stage12-style 10-split external evidence for PeMS7_1026 and Seattle before either dataset can support elevated external or transfer-style claims. After execution, the phase is explicitly blocked: real Stage12 runs did not produce complete ten-split aggregate evidence, and the observed runtime is not viable for continuing the milestone unchanged. The phase must preserve fail-closed evidence gates, raw-data hygiene, and traceable artifacts; it must not draft manuscript prose or reinterpret incomplete runs as Stage12 completion.

</domain>

<decisions>
## Implementation Decisions

### Post-Execution Disposition
- **D-01:** Phase 8 remains blocked because PeMS7_1026 and Seattle Stage12 ten-split evidence are incomplete and the real run is too slow to treat completion as a near-term waiting problem.
- **D-02:** The user observed that a real Stage12 run did not finish even one seed after roughly 16 hours. Downstream planning must treat this as a structural runtime blocker, not a transient execution delay.
- **D-03:** Do not advance Phase 9 or Phase 10 as normal v1.1 milestone work while Phase 8 remains blocked for performance reasons.
- **D-04:** The milestone should stop here and route first to a performance-optimization/replanning step before attempting to complete EVID-03/EVID-04.

### Optimization-First Strategy
- **D-05:** The next strategy is optimize first: improve runtime, scheduling, caching, parallelism, aggregation, or orchestration before retrying full Stage12 evidence generation.
- **D-06:** Optimization work may change runtime efficiency and job execution mechanics only. It must not change the Stage12 evidence standard, budgets, baseline portfolio, held-out-test requirement, or claim gate semantics.
- **D-07:** Reduced diagnostic or profiling runs may guide optimization, but they must not enter the external evidence contract as Stage12 evidence.
- **D-08:** Full ten-split Stage12 retry should not start until both PeMS7_1026 and Seattle can each complete at least one Stage12-compatible full seed in an acceptable runtime and produce traceable outputs that can be aggregated.

### Evidence Gate Standard
- **D-09:** PeMS7_1026 remains incomplete until the required ten-split aggregate artifacts exist, are generated from held-out test evidence, and are git-tracked or otherwise represented by committed traceability-safe summaries/manifests.
- **D-10:** Seattle remains blocked from core claims while `stage12_status.json` reports blocked or while complete tracked ten-split Stage12 aggregate evidence is absent.
- **D-11:** Missing p-values, paired comparisons, aggregate tables, or split counts must be explicitly marked as missing or blocked; no contract may imply completion from DRY_RUN, partial seed logs, or lower-power evidence.
- **D-12:** The machine gate must remain fail-closed with `v1_1_completion_allowed=false` until both external datasets satisfy the full Stage12 contract.

### Downstream Routing
- **D-13:** Phase 9 and Phase 10 should not be planned as ordinary next milestone phases until the Phase 8 runtime blocker is addressed or the roadmap is deliberately changed.
- **D-14:** Any downstream artifacts created before Stage12 completion must classify PeMS7_1026 and Seattle as blocked or conditional and must not allow Seattle into core claims.
- **D-15:** If the project chooses to continue without completed Stage12 external evidence, that must be an explicit roadmap/milestone decision, not an implicit consequence of moving past Phase 8.

### Claude's Discretion
- Choose the exact performance profiling and optimization plan in a later planning step, but preserve the runtime-only constraint and fail-closed evidence gates.
- Prefer improving the existing evaluator, launchers, job orchestration, and aggregation path over creating a separate duplicate experiment pipeline.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Milestone Scope
- `.planning/ROADMAP.md` — Phase 8 goal, blocked gate status, and Phase 9/10 dependency order.
- `.planning/REQUIREMENTS.md` — EVID-03 and EVID-04 remain unchecked; raw dataset commits and manuscript prose remain out of scope.
- `.planning/STATE.md` — Current milestone state is blocked at Phase 8 with EVID-03/EVID-04 incomplete.

### Phase 8 Evidence and Verification
- `.planning/phases/08-external-stage12-evidence/08-VERIFICATION.md` — Verification verdict is `BLOCKED_BY_GATE`; records incomplete PeMS7_1026 and Seattle evidence.
- `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json` — Machine-readable fail-closed gate with `v1_1_completion_allowed=false`, `pems7_1026_stage12_complete=false`, and `seattle_stage12_complete=false`.
- `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_contract.csv` — External evidence contract rows that must remain consistent with the gate.
- `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_contract.json` — JSON version of the external evidence contract.
- `TRC-23-02333/trace_sl_results/seattle_stage12_baseline_portfolio/stage12_status.json` — Seattle-specific blocker and `seattle_core_claim_blocked=true` status.

### Existing Runtime Path
- `scripts/run_stage12_pems7_1026.sh` — Current PeMS7_1026 Stage12 launcher surface; candidate for runtime-only optimization.
- `scripts/run_stage12_seattle.sh` — Current Seattle Stage12 launcher surface; candidate for runtime-only optimization.
- `scripts/run_stage12_pems7_228.sh` — Stage12 baseline portfolio launcher reference.
- `TRC-23-02333/transparent_estimator_eval.py` — Main evaluator; profiling and performance fixes should target this path rather than duplicating it.
- `TRC-23-02333/summarize_trace_sl_rcss.py` — Aggregation path and required Stage12 aggregate artifact schema.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `TRC-23-02333/transparent_estimator_eval.py` is the main evaluator for PeMS and Seattle-style inputs and writes per-seed metrics/layout/config artifacts.
- `TRC-23-02333/summarize_trace_sl_rcss.py` aggregates per-seed metrics into summary CSVs and Markdown reports including layout summaries, delta summaries, paired tests, ablation summaries, and win counts.
- `scripts/run_stage12_pems7_1026.sh`, `scripts/run_stage12_seattle.sh`, and `scripts/run_stage12_pems7_228.sh` define the current Stage12 launcher surfaces and should be optimized rather than replaced by unrelated pipelines.
- `scripts/generate_trace_sl_external_evidence_contracts.py` and its generated paper-source artifacts enforce the external-evidence gate.

### Established Patterns
- Research artifacts are CSV/JSON first, with Markdown summaries as generated human-readable views.
- Shell scripts expose data roots, output directories, seeds, budgets, and resource knobs through environment variables.
- Raw datasets stay ignored; committed artifacts should be curated summaries, manifests, scripts, and generated tables.
- There is no formal test runner; validation should use script-level regression checks, schema checks, smoke commands, and artifact existence/provenance checks.

### Integration Points
- Stage12 external outputs should live under `TRC-23-02333/trace_sl_results/` with clear dataset/stage names.
- The fail-closed gate lives under `TRC-23-02333/trace_sl_results/paper_sources/` and should remain the single machine-readable milestone gate.
- Roadmap, requirements, and state should continue to reflect blocked truth until complete Stage12 evidence exists.

</code_context>

<specifics>
## Specific Ideas

- Treat the 16-hour-without-one-seed observation as decisive evidence that Phase 8 needs performance work before retrying full Stage12.
- The next planning move should be performance optimization, not Phase 9/10 continuation and not manuscript writing.
- At least one Stage12-compatible full seed for each of PeMS7_1026 and Seattle must complete and aggregate successfully before launching a full ten-split retry.
- Runtime-only means preserving budgets, baseline portfolio, held-out-test semantics, split-count standard, and gate policy.

</specifics>

<deferred>
## Deferred Ideas

- Full PeMS7_1026 and Seattle ten-split Stage12 rerun is deferred until runtime-only optimization proves both datasets can complete at least one Stage12-compatible full seed.
- Phase 9 ablation/evidence classification is deferred while the v1.1 milestone is stopped at the Phase 8 performance blocker.
- Phase 10 theory/handoff package is deferred while the v1.1 milestone is stopped at the Phase 8 performance blocker.
- Manuscript prose belongs to a later writing milestone after the paper foundation is unblocked.

</deferred>

---

*Phase: 08-external-stage12-evidence*
*Context gathered: 2026-05-25*
