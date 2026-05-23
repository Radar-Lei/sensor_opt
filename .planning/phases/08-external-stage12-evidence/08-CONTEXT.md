# Phase 8: External Stage12 Evidence - Context

**Gathered:** 2026-05-23
**Status:** Ready for planning
**Mode:** Autonomous smart discuss with user-approved auto-advance preference

<domain>
## Phase Boundary

This phase completes mandatory Stage12-style 10-split external evidence for PeMS7_1026 and Seattle before either dataset can support elevated external or transfer-style claims. It must produce reproducibility-safe evidence artifacts, scripts, summaries, and milestone gates only. It must not draft manuscript prose, must not commit raw traffic datasets, and must not mark Seattle as core-claim eligible unless Seattle Stage12 10-split evidence succeeds and is traceable to committed summaries/tables/scripts/manifests.

</domain>

<decisions>
## Implementation Decisions

### External Evidence Scope
- PeMS7_1026 must receive Stage12 10-split evidence using the same budgets and reviewer-facing baseline portfolio as the PeMS7_228 main evidence wherever the existing evaluator supports it.
- Seattle must receive Stage12 10-split external/transfer-style evidence before any Seattle-backed core claim artifact is allowed.
- If Seattle Stage12 cannot be completed in this phase, the phase must preserve an explicit blocker that prevents v1.1 completion or keeps Seattle excluded from core claims.
- Do not reinterpret existing lower-power Stage11 evidence as sufficient Stage12 evidence unless planning verifies it exactly matches the Stage12 10-split contract.

### Evidence Standard
- External evidence must be held-out test evidence, not validation-selection evidence.
- Evidence artifacts should include aggregate summaries, paired deltas/p-values where available, baseline portfolio rows, split counts, budgets, provenance, and dataset labels.
- Contract/summary artifacts must distinguish completed evidence from blocked, conditional, or supporting evidence.
- Any missing paired-stat comparisons must be explicitly marked rather than presented as paired-test-supported evidence.

### Provenance and Raw Data Hygiene
- All paper-foundation pointers must target committed scripts, manifests, summaries, CSV/JSON tables, or generated Markdown artifacts.
- Raw traffic datasets under `TRC-23-02333/dataset/` are local ignored inputs and must not be committed, deleted, or exposed as evidence artifacts.
- Stage12 external evidence should be reproducible through scripts with documented environment variables and deterministic split/layout seeds.
- If large generated outputs are intentionally not committed, create committed aggregate summaries/manifests that are sufficient for paper-foundation traceability.

### Milestone Completion Gate
- Add or update an explicit gate artifact that says v1.1 cannot be completed with Seattle in core claims unless Seattle Stage12 10-split evidence is present and traceable.
- PeMS7_1026 and Seattle should remain outside Phase 7's core claim contract until this phase verifies their evidence status.
- The gate should be machine-checkable where practical, not only a narrative warning.

### Claude's Discretion
- Choose exact Stage12 directory names, script names, aggregate artifact names, and validation commands based on existing repository conventions.
- Prefer extending existing experiment launchers and summarizers over creating duplicate pipelines.
- Use DRY_RUN/smoke checks when full reruns are too expensive, but do not claim Stage12 completion unless the actual 10-split aggregate evidence exists.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `TRC-23-02333/transparent_estimator_eval.py` is the main evaluator for PeMS and Seattle-style inputs and writes per-seed metrics/layout/config artifacts.
- `TRC-23-02333/summarize_trace_sl_rcss.py` aggregates per-seed metrics into summary CSVs and Markdown reports including layout summaries, delta summaries, paired tests, ablation summaries, and win counts.
- Existing launchers include `scripts/run_stage11_pems7_1026.sh` and `scripts/run_stage11_seattle.sh`; these are likely analogs for Stage12 launchers.
- Phase 7 added `scripts/generate_trace_sl_claim_contracts.py` and paper-source contract artifacts that external-evidence classification should not contradict.

### Established Patterns
- Research artifacts are CSV/JSON first, with Markdown summaries as generated human-readable views.
- Shell scripts expose data roots, output directories, seeds, budgets, and resource knobs through environment variables.
- Raw datasets stay ignored; committed artifacts should be curated summaries, manifests, scripts, and generated tables.
- There is no formal test runner; validation should use script-level regression checks, schema checks, smoke commands, and artifact existence/provenance checks.

### Integration Points
- Stage12 external outputs should live under `TRC-23-02333/trace_sl_results/` with clear dataset/stage names.
- Paper-source README or a dedicated external-evidence gate artifact should link to the new evidence summaries without creating manuscript prose.
- `.planning/STATE.md`, `.planning/ROADMAP.md`, and phase summaries/verifications track GSD progress.

</code_context>

<specifics>
## Specific Ideas

- Treat Seattle as blocked from core claims by default and only unlock it through verified Stage12 10-split evidence.
- Reuse the same budgets and reviewer-facing baseline portfolio as the PeMS7_228 main table when feasible.
- Prefer committed aggregate summaries and manifests over committing large raw/per-step outputs.
- No manuscript drafting should occur in this phase.

</specifics>

<deferred>
## Deferred Ideas

- Dataset evidence classification across all datasets belongs to Phase 9.
- Theory/handoff package belongs to Phase 10.
- Manuscript prose belongs to a later writing milestone.

</deferred>
