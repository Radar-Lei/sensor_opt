# Phase 7: Claim and Main Table Contract - Context

**Gathered:** 2026-05-23
**Status:** Ready for planning
**Mode:** Autonomous smart discuss with user-approved auto-advance preference

<domain>
## Phase Boundary

This phase freezes the Transportation Science-facing claim contract and the main PeMS7_228 result-table contract. It must produce paper-foundation artifacts only: no manuscript prose, no new introduction/results text, and no unsupported elevation of PeMS7_1026, Seattle, or robustness evidence. The phase should make it easy for a later writing milestone to state what TRACE-SL can claim, what it cannot claim, which PeMS7_228 rows constitute the main in-domain table, and where the low-budget multistart caveat must appear.

</domain>

<decisions>
## Implementation Decisions

### Claim Framing
- Frame TRACE-SL as transparent reconstruction-aware sparse sensor layout design for hidden-network traffic reconstruction under budget constraints.
- Avoid toy-project, heuristic-only, or baseline-beating-only framing; the contract should connect formulation, posterior/certificate diagnostics, validation selection, and held-out reconstruction evidence.
- Preserve strong publishable claims when they are tied to explicit evidence, but mark claims requiring stronger theory as TR Part B-level extensions rather than Transportation Science-ready claims.
- Treat validation MAE as selection evidence only; claim-facing evidence must be held-out test evidence with paired comparisons where available.

### Forbidden and Conditional Wording
- Maintain an explicit forbidden wording list: optimal, certified, globally robust, guaranteed MAE improvement, and generalizes across networks.
- Permit only bounded variants such as certificate-guided, posterior-certificate-aware, stress-tested, improves in the tested setting, or external evidence when supported by the corresponding artifact.
- Require the PeMS7_228 10% low-budget multistart caveat in every claim-facing artifact that discusses main-table results or method dominance.
- Keep robustness evidence in a stress-test or appendix lane unless multi-seed perturbation evidence is added later.

### Main Table Contract
- Freeze the main in-domain table around the existing Stage12-or-equivalent PeMS7_228 10-split baseline portfolio and `validation_swap_selected` as the main TRACE-SL row.
- Include reviewer-facing baselines where available: validation-selected random, random mean, top variance, greedy A-trace, graph sampling, observability, QR/POD-style baselines, and multistart validation-swap variants.
- Prefer table fields that expose budget, method/layout type, held-out test MAE/RMSE/MAPE where available, paired deltas, p-values, and caveat tags.
- Do not let the table imply TRACE-SL is best at every budget; the 10% budget exception must be visible rather than hidden in prose.

### Evidence Routing
- PeMS7_228 is the main in-domain evidence source for this phase.
- PeMS7_1026 and Seattle remain outside this phase's core claim contract until Phase 8 completes mandatory Stage12 10-split external evidence.
- Robustness evidence supports stress-test/appendix claims only in this phase.
- Dataset evidence classification is deferred to Phase 9 except where needed to keep Phase 7 claims from overreaching.

### Claude's Discretion
- Choose exact artifact filenames, table schemas, and validation checks based on existing repository conventions.
- Prefer machine-readable CSV/JSON contracts plus concise Markdown summaries generated from or pointing to those data sources.
- If existing Stage12 naming differs from roadmap wording, map to the strongest committed PeMS7_228 10-split aggregate artifacts without inventing missing results.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `TRC-23-02333/summarize_trace_sl_rcss.py` already creates aggregate CSV/Markdown summaries including layout summaries, delta summaries, paired tests, ablation summaries, winner counts, and certificate-related outputs.
- `TRC-23-02333/transparent_estimator_eval.py` writes per-seed `metrics.csv`, `metrics.json`, `layouts.json`, `swap_history.json`, `rcss_candidates.*`, `certificate_correlations.csv`, `config.json`, and `SUMMARY.md`.
- Existing curated PeMS7_228 result roots under `TRC-23-02333/trace_sl_results/` should be used as evidence sources rather than rerunning expensive experiments unless planning finds a missing generated summary.

### Established Patterns
- Research artifacts are stored as CSV/JSON first, with Markdown summaries for human-readable interpretation.
- Shell launchers expose reproducibility knobs through environment variables and keep raw datasets local/ignored.
- There is no formal unit-test framework; validation should use schema checks, artifact existence checks, and lightweight smoke/consistency scripts where appropriate.

### Integration Points
- Claim/table contract artifacts should live in a committed, reproducibility-safe location and point back to `TRC-23-02333/trace_sl_results/` summaries, scripts, and manifests.
- Existing `.planning` phase artifacts should record planning, execution summaries, and verification for GSD traceability.
- Raw files under `TRC-23-02333/dataset/` must not be committed or deleted.

</code_context>

<specifics>
## Specific Ideas

- The claim contract should explicitly separate Transportation Science-ready claims from TR Part B-level extensions.
- The main table contract should be reviewer-facing, not just a convenience table for internal comparison.
- The multistart caveat should be attached to claim/table rows or caveat fields, not buried only in narrative text.
- No manuscript drafting should occur in this phase.

</specifics>

<deferred>
## Deferred Ideas

- PeMS7_1026 and Seattle Stage12 10-split evidence completion is Phase 8.
- Ablation evidence classification and dataset evidence classification are Phase 9.
- Theory-ready formulation, monotonicity, local optimality, complexity, and reproducibility handoff package are Phase 10.
- Manuscript prose belongs to a later writing milestone after v1.1.

</deferred>
