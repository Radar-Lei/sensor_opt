# Phase 1: Claim-Evidence Contract - Context

**Gathered:** 2026-05-21
**Status:** Ready for planning

<domain>
## Phase Boundary

This phase delivers the paper-facing claim-evidence contract for TRACE-SL before additional experiments, theory writing, or manuscript drafting. It locks the strongest defensible contribution claims, defines what evidence each claim requires, constrains terminology around certificates, handles the 10% PeMS7_228 multistart caveat, and positions TRACE-SL against deterministic full-observability TSLP and black-box imputation/forecasting.

It does not implement new baselines, run new experiments, prove theory, generate final paper tables, or rewrite the full manuscript. Those belong to later phases.

</domain>

<decisions>
## Implementation Decisions

### Claim Set and Main Framing
- **D-01:** Preserve a strong main contribution claim: TRACE-SL should be framed as transparent reconstruction-aware sparse traffic sensor placement for full-network reconstruction, not as candidate-pool tuning or an ad hoc empirical heuristic.
- **D-02:** The contribution statement should emphasize the system-level design problem: select sparse sensors so a transparent GLS/MAP/GSP-style reconstruction model can recover hidden traffic states under limited budgets.
- **D-03:** The claim contract must separate method contribution, performance evidence, certificate evidence, and scope/limitations so later writing can strengthen unsupported claims with evidence rather than prematurely weakening them.

### Evidence Mapping Standard
- **D-04:** Every primary claim must map to one or more explicit evidence types: held-out test result, paired/statistical comparison, robustness test, external-network evidence, formal derivation/theory, reproducible artifact, or limitation wording.
- **D-05:** Validation MAE is selection evidence only, not final performance evidence. Final performance claims must point to held-out test metrics from curated result artifacts.
- **D-06:** The matrix should mark evidence status as present, needs audit, needs new experiment, theory-dependent, or wording-only limitation. This lets later phases route work without re-deciding the claim.

### Low-Budget Caveat Policy
- **D-07:** The 10% PeMS7_228 multistart-vs-RCSS issue must be treated as a predeclared comparator/portfolio issue or bounded low-budget caveat, not ignored and not handled by post-hoc best-method selection.
- **D-08:** Do not claim TRACE-SL is best at every budget against every comparator. Preferred wording is that the final predeclared TRACE-SL portfolio improves reconstruction over random, validation-selected random, and topology baselines across the reported budgets, while explicitly noting any stronger low-budget multistart behavior if confirmed.
- **D-09:** Later baseline/method phases should decide whether multistart validation refinement becomes a named comparator or a predeclared portfolio member, but Phase 1 must already reserve a row for it in the claim-evidence matrix.

### Certificate Terminology
- **D-10:** Use “certificate-guided”, “posterior-certificate-aware”, or “certificate diagnostics” language unless Phase 2 adds theorem-level formal certification.
- **D-11:** Current posterior trace, condition number, and logdet correlations support interpretability and empirical guidance claims, not formal certified optimality or guaranteed reconstruction-error bounds.
- **D-12:** The claim matrix must distinguish empirical certificate-error correlation evidence from theoretical posterior-error derivation evidence.

### Positioning Boundaries
- **D-13:** Position TRACE-SL against deterministic full-observability TSLP by emphasizing partial-observation reconstruction quality, uncertainty, validation performance, and deployment-like held-out error rather than full observability or counting-point coverage.
- **D-14:** Position TRACE-SL against black-box traffic imputation/forecasting by emphasizing transparent reconstruction models and sensor-layout design, not a learned predictor as the primary contribution.
- **D-15:** Seattle evidence should not be used as a core claim unless later phases curate repository-visible outputs and documentation consistency; Phase 1 should mark Seattle as conditional or supporting-only.

### Claude's Discretion
The planner may choose the exact format of the claim-evidence matrix, but it must be machine-auditable enough for later phases to update evidence status and paper wording. A Markdown table is acceptable if it includes claim ID, claim wording, evidence required, current evidence source, caveat/limitation wording, and downstream phase owner.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### GSD Scope and Requirements
- `.planning/ROADMAP.md` — Defines Phase 1 goal, requirements CLAIM-01..CLAIM-05, success criteria, and downstream phase dependencies.
- `.planning/REQUIREMENTS.md` — Defines claim/framing requirements and global out-of-scope constraints.
- `.planning/PROJECT.md` — Defines target venue, core value, active decisions, and known evidence caveats.
- `.planning/STATE.md` — Current workflow state and active decisions.

### Current Narrative and Claim Sources
- `README.md` — Current public-facing TRACE-SL overview, main claim, results, and reproduction entry points.
- `NARRATIVE_REPORT.md` — Writing handoff with current core claim, method summary, Stage 9-11 evidence, PeMS7_1026/Seattle discussion, certificate validity, and claim status.
- `TRC-23-02333/trace_sl_results/README.md` — Curated result inventory and guidance to use `validation_swap_selected` as the current main method.

### Evidence Artifacts to Reference, Not Recompute in Phase 1
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md` — Main PeMS7_228 ten-split evidence bundle for claim mapping.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/SUMMARY.md` — External PeMS7_1026 evidence bundle; note lower split count.
- `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/` — Conditional Seattle evidence; use only if later curation confirms it is repository-consistent.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` — Explains TRACE-SL evaluator, RCSS selection layer, result aggregation, and anti-patterns.
- `.planning/codebase/STRUCTURE.md` — Locates documentation, scripts, datasets, result artifacts, and research reports.
- `.planning/codebase/CONVENTIONS.md` — Documents research artifact conventions and reproducibility practices.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `TRC-23-02333/trace_sl_results/*/SUMMARY.md`: Existing aggregate evidence summaries should be referenced by the claim matrix instead of recomputing Phase 1 numbers.
- `TRC-23-02333/trace_sl_results/*/*.csv`: Existing CSV artifacts provide traceable evidence sources for later Phase 4 audit/statistical work.
- `README.md` and `NARRATIVE_REPORT.md`: Existing claim wording can be audited and transformed into a stronger claim-evidence contract.

### Established Patterns
- The project stores paper-visible evidence as CSV/JSON/Markdown under `TRC-23-02333/trace_sl_results/` and keeps raw datasets ignored.
- The evaluator separates validation-based layout selection from held-out test evaluation; this must be reflected in claim wording.
- Research documentation lives in Markdown at the repository root and `refine-logs/`; Phase 1 should add a planning artifact rather than modifying algorithm code.

### Integration Points
- The primary Phase 1 output should live under `.planning/phases/01-claim-evidence-contract/` and feed Phase 2-7 planning.
- If the planner creates a reusable claim matrix, later phases should update it rather than scatter claim status across unrelated reports.
- Do not read or commit raw files under `TRC-23-02333/dataset/` for this phase.

</code_context>

<specifics>
## Specific Ideas

- Strong claims should be preserved and made evidence-backed, not narrowed into a weak incremental heuristic story.
- The preferred terminology is “certificate-guided” until formal theory justifies stronger language.
- The 10% PeMS7_228 multistart caveat is a central reviewer-risk item and must appear explicitly in the contract.
- Transportation Science is the primary framing; TR Part B remains a backup/extension path requiring stronger theory.

</specifics>

<deferred>
## Deferred Ideas

- Implementing new baselines belongs to Phase 3.
- Regenerating/auditing core experiment evidence belongs to Phase 4.
- Running robustness, missingness, sensor-failure, cost, temporal-shift, or candidate-count experiments belongs to Phase 5.
- Writing the final manuscript belongs to Phase 7.

</deferred>

---

*Phase: 1-Claim-Evidence Contract*
*Context gathered: 2026-05-21*
