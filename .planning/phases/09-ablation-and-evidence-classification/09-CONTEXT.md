# Phase 9: Ablation and Evidence Classification - Context

**Gathered:** 2026-05-25
**Status:** Ready for planning
**Mode:** Autonomous smart discuss with user instruction to continue without unnecessary questions

<domain>
## Phase Boundary

This phase freezes TRACE-SL ablation logic and dataset evidence classification for the Transportation Science paper foundation. It should curate and generate paper-source artifacts that explain the roles of random baselines, certificate candidate pools, validation selection, validation-aware swap refinement, and multistart variants using existing committed or reproducibility-safe evidence. It must not complete or imply completion of the missing PeMS7_1026/Seattle Stage12 ten-split evidence, must not elevate Seattle into core claims, must not treat one-seed feasibility runs as evidence, and must not draft manuscript prose.

</domain>

<decisions>
## Implementation Decisions

### Ablation Contract Scope
- Compare random mean, validation-selected random, certificate-only greedy, RCSS-selected, validation-swap-selected, and multistart validation-swap variants in one machine-readable ablation contract.
- Use held-out test aggregate artifacts as the evidence source wherever available; validation MAE remains selection evidence only.
- Preserve PeMS7_228 as the core ablation dataset because it has the strongest committed 10-split evidence and Phase 7 main-table support.
- If an ablation component is missing, label it missing/unsupported/conditional rather than synthesizing or rerunning expensive evidence without an explicit plan.

### Layer Interpretation
- Present RCSS as three separable layers: certificate-guided candidate generation, validation-based candidate selection, and validation-aware local refinement.
- Answer certificate-vs-random-pool, validation-selection, and validation-swap questions through curated artifact rows and explicit evidence-status fields.
- Keep multistart validation-swap visible as a serious comparator, especially for the PeMS7_228 low-budget caveat.
- Avoid kitchen-sink framing; every layer must map to a specific row family, comparison, or caveat.

### Dataset Evidence Classification
- Classify every dataset into core, external, supporting, conditional, or appendix-only using evidence strength, split count, held-out-test status, paired comparison availability, and gate status.
- PeMS7_228 should remain core in-domain evidence where Stage12/10-split main-table artifacts support it.
- PeMS7_1026 remains external/supporting or conditional until completed Stage12 10-split aggregate evidence exists; lower-power Stage11 and one-seed Stage12 feasibility artifacts must not satisfy EVID-03.
- Seattle remains conditional/blocked from core claims while Stage12 status or external evidence gate reports incomplete ten-split evidence.
- Robustness evidence remains stress-test or appendix-only unless multi-seed perturbation evidence is later added.

### Artifact Policy
- Generate CSV/JSON-first paper-source artifacts, with Markdown summaries only as generated views or concise indexes.
- Add schema/status fields that make blocked, conditional, missing, and complete evidence machine-checkable.
- Link every row back to existing committed summaries, generated tables, scripts, or manifests without touching raw datasets.
- Keep `external_evidence_gate.json` fail-closed and consistent with any new classification artifacts.

### Claude's Discretion
- Choose exact filenames and schema details following existing `TRC-23-02333/trace_sl_results/paper_sources/` conventions.
- Prefer adding focused generator/validator scripts under `scripts/` over manual table edits when artifacts are derived from existing evidence.
- Use lightweight validation commands and schema checks rather than expensive experiment reruns.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `TRC-23-02333/summarize_trace_sl_rcss.py` already produces `gls_map_ablation_summary.csv`, paired delta tests, win counts, selected-source summaries, and aggregate Markdown reports.
- `TRC-23-02333/trace_sl_results/paper_sources/` already contains claim, main-table, paired-delta, certificate-correlation, robustness, and external-evidence contracts.
- `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json` is the authoritative fail-closed gate for PeMS7_1026 and Seattle Stage12 completion.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/` and related curated PeMS7_228 roots contain core aggregate ablation evidence.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage12_feasibility_seed25/` and the Seattle feasibility counterpart, if present, are feasibility proof only and must be labeled non-evidence for ten-split claims.

### Established Patterns
- Research artifacts are CSV/JSON first, with Markdown summaries generated from the same source rows.
- Evidence gates fail closed when split counts, tracked aggregate artifacts, or status files do not satisfy the contract.
- Raw datasets under `TRC-23-02333/dataset/` stay local and ignored.
- There is no formal test framework; phase validation should use direct generator execution, schema checks, and artifact consistency checks.

### Integration Points
- New ablation and dataset-classification artifacts should live under `TRC-23-02333/trace_sl_results/paper_sources/`.
- Any generator should be placed in `scripts/` and consume only existing result summaries, contracts, and gate files.
- Roadmap, requirements, and state updates must mark ABLT-01 through ABLT-04 and EVID-05 truthfully while preserving EVID-03/EVID-04 as incomplete.

</code_context>

<specifics>
## Specific Ideas

- Produce an `ablation_contract.csv/json` that records component layer, dataset, evidence source, split count, comparison target, supported question, caveat tag, and claim route.
- Produce a `dataset_evidence_classification.csv/json` that records dataset, class, evidence status, allowed use, blocked use, required upgrade, and provenance.
- Include explicit non-evidence labels for Stage12 one-seed feasibility outputs so they cannot be mistaken for ten-split external evidence.
- Keep the PeMS7_228 10% multistart caveat visible in ablation artifacts, not only in narrative summaries.
- Do not write introduction, related work, method, results, abstract, conclusion, or limitations prose.

</specifics>

<deferred>
## Deferred Ideas

- Completing PeMS7_1026 and Seattle Stage12 ten-split evidence remains outside this phase and depends on future reruns after Phase 8.5 feasibility.
- Manuscript prose remains deferred to the next writing milestone.
- Theory-ready formulation, posterior trace identity, monotonicity, local optimality, complexity, and final handoff package belong to Phase 10.

</deferred>
