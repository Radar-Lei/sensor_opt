# Phase 2: Formulation and Theory Bridge - Context

**Gathered:** 2026-05-22
**Status:** Ready for planning
**Mode:** Auto-selected decisions from `/gsd-autonomous --only 2`

<domain>
## Phase Boundary

This phase turns TRACE-SL/RCSS from a strong empirical prototype into a formally stated reconstruction-aware sensor placement method. It must produce paper-facing formulation and theory artifacts: a budgeted sensor-set optimization problem, the tractable TRACE-SL/RCSS surrogate objective, a GLS/MAP posterior-error derivation, interpretation of posterior variance as an MAE-oriented empirical guide, algorithm complexity/local-optimality statements for validation-aware swap, and a TR Part B theory-gap note.

This phase should not run new baseline experiments, expand robustness tests, regenerate split evidence, curate Seattle outputs, or write the full manuscript. Those are downstream phases. Algorithm code may be inspected as the source of truth, but the default deliverable is method/theory documentation and manuscript-ready text, not changing the experiment pipeline.

</domain>

<decisions>
## Implementation Decisions

### Formalization Target
- **D-01:** Present TRACE-SL as a budgeted sparse sensor-set design problem for hidden-node reconstruction: choose a sensor set `S` with `|S| <= k` to minimize held-out reconstruction loss on unobserved nodes under a transparent reconstruction model.
- **D-02:** The formulation must explicitly distinguish train-derived reconstruction ingredients, validation-based layout selection, and held-out test evaluation. Validation MAE can define the surrogate and selection rule; it must not be described as final performance evidence.
- **D-03:** The method definition should use notation compatible with traffic networks: graph nodes/links, observed sensor subset `S`, hidden complement `H`, traffic state vector `x`, observations `y_S`, reconstruction map `\hat{x}_H(S)`, and budget fraction or cardinality budget `k`.

### TRACE-SL/RCSS Surrogate Definition
- **D-04:** Define RCSS as a predeclared tractable surrogate/algorithmic portfolio, not as post-hoc tuning. The surrogate score should include validation loss, posterior trace, scenario CVaR trace, condition number, and coverage penalty/term as named diagnostics.
- **D-05:** Auto-weight selection should be written as inner-validation model selection over a fixed weight grid using selector/tuner validation splits, matching the Stage 11 implementation and avoiding any claim of hand-tuned coefficients.
- **D-06:** Validation-aware swap should be defined as local refinement over a fixed add-node universe from the OR-guided candidate pool, accepting swaps only when validation GLS/MAP reconstruction loss improves.

### Posterior-Error Derivation
- **D-07:** Provide a linear-Gaussian GLS/MAP derivation showing that the posterior covariance over hidden states induces expected squared hidden-state error, so posterior trace is an A-optimal proxy for reconstruction uncertainty under the idealized model.
- **D-08:** State assumptions plainly: Gaussian/linear observation model, train-derived covariance or precision, regularized graph/precision prior, fixed sensor observations, and squared-error analysis. Do not overstate this as a formal MAE guarantee.
- **D-09:** Connect theory to MAE-oriented selection as an empirical bridge: lower posterior variance is expected to reduce squared reconstruction uncertainty and has observed correlation with MAE, but real traffic data, non-Gaussian errors, temporal shift, and validation selection make it a diagnostic rather than a certificate theorem.

### Algorithm Analysis
- **D-10:** Give validation-aware swap complexity in terms of candidate universe size, budget `k`, validation samples/time steps, reconstruction solve cost, number of starts, and swap iterations. Dense-solver scaling must be called out as a limitation.
- **D-11:** State local optimality for fixed-candidate validation-aware swap: at termination, no single remove/add swap from the fixed universe improves the chosen validation objective under the implemented acceptance rule.
- **D-12:** Keep “certificate-guided” / “posterior-certificate-aware” terminology unless the derivation is explicitly theorem-level and scoped to the linear-Gaussian squared-error setting; do not upgrade the project to broad “certified optimization”.

### TR Part B Extension Boundary
- **D-13:** Include an optional theory-gap note identifying what would be needed for a TR Part B-style contribution: monotonicity, approximate submodularity, approximation guarantees, stability under covariance perturbation, or stronger stochastic/bilevel optimization analysis.
- **D-14:** Treat advanced approximation/submodularity proofs as deferred v2 work unless they can be stated narrowly without additional implementation or experiments.

### Claude's Discretion
The planner may choose the exact artifact layout, but it should prioritize manuscript-ready method/theory text plus any supporting planning artifact over unnecessary code changes. If updating existing narrative files, preserve strong claims while adding the formal bridge rather than narrowing the contribution.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### GSD Scope and Requirements
- `.planning/ROADMAP.md` — Defines Phase 2 goal, THEORY-01..THEORY-06, success criteria, and dependencies.
- `.planning/REQUIREMENTS.md` — Defines formulation/theory requirements and global wording constraints around certification and evidence.
- `.planning/PROJECT.md` — Defines target venue, core value, active decisions, and known evidence caveats.
- `.planning/STATE.md` — Current workflow state and active decisions.
- `.planning/phases/01-claim-evidence-contract/01-CONTEXT.md` — Locks Phase 1 claim strategy, terminology boundaries, evidence standards, and multistart caveat handling.
- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-MATRIX.md` — Claim/evidence contract that Phase 2 must strengthen with formulation and theory evidence if present.

### Current Method and Narrative Sources
- `NARRATIVE_REPORT.md` — Current TRACE-SL narrative, RCSS method summary, evidence interpretation, and certificate validity language.
- `README.md` — Current public-facing overview and reproduction framing that may need method/theory wording alignment.
- `TRC-23-02333/trace_sl_results/README.md` — Curated evidence inventory and current main-method guidance.
- `refine-logs/WRITING_NOTES_GREEDY_OFFLINE_PLANNING.md` — Existing writing rationale that greedy/swap procedures are offline planning heuristics, if present.

### Implementation Source of Truth
- `TRC-23-02333/transparent_estimator_eval.py` — Defines GLS/MAP reconstruction, posterior diagnostics, RCSS scoring, auto-weight selection, candidate generation, and validation-aware swap behavior.
- `TRC-23-02333/summarize_trace_sl_rcss.py` — Defines aggregate certificate/error correlation and paired comparison artifacts.
- `scripts/run_stage11_pems7_228.sh` — Main Stage 11 launcher and predeclared method flags for PeMS7_228.
- `scripts/run_stage11_pems7_1026.sh` — External validation launcher using the same method family.
- `scripts/run_stage11_seattle.sh` — Seattle validation launcher; use only as conditional/non-core evidence until curation is resolved.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` — Explains TRACE-SL evaluator layers, RCSS selection, data flow, and anti-patterns.
- `.planning/codebase/STRUCTURE.md` — Locates scripts, result artifacts, narrative documents, and dataset boundaries.
- `.planning/codebase/CONVENTIONS.md` — Documents research artifact conventions and reproducibility practices.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `TRC-23-02333/transparent_estimator_eval.py`: Source for exact algorithm behavior, including `evaluate_layout`, `certificate`, `posterior_trace_for_layout`, `scenario_cvar_trace_for_layout`, `select_auto_rcss_weights`, `rcss_candidate_scores`, and `validation_swap_search`.
- `NARRATIVE_REPORT.md`: Existing method wording can be upgraded into formal manuscript-ready formulation and theory bridge.
- `.planning/phases/01-claim-evidence-contract/01-CONTEXT.md`: Provides locked terminology and evidence boundaries that Phase 2 must preserve.
- `TRC-23-02333/trace_sl_results/*/certificate_correlation_summary.csv` and aggregate summaries: Evidence for empirical certificate-error alignment; reference but do not recompute in Phase 2.

### Established Patterns
- The project separates validation-based layout selection from held-out test evaluation; Phase 2 wording must preserve this separation.
- The implementation is a monolithic research script with dense matrix operations; theory/complexity should describe current behavior without implying scalable sparse solvers already exist.
- Paper-visible evidence lives in committed CSV/JSON/Markdown summaries under `TRC-23-02333/trace_sl_results/`; raw datasets remain local and ignored.
- Current claim strategy preserves strong claims but constrains unsupported wording to evidence-backed or limitation-scoped statements.

### Integration Points
- Primary Phase 2 artifacts should live under `.planning/phases/02-formulation-and-theory-bridge/` and feed Phases 3–7.
- If manuscript/narrative files are edited, likely targets are `NARRATIVE_REPORT.md`, `README.md`, or a new phase-local method/theory artifact that later paper-writing consumes.
- Any algorithm description must be traceable to `TRC-23-02333/transparent_estimator_eval.py`; avoid inventing method steps that are not implemented.

</code_context>

<specifics>
## Specific Ideas

- Strengthen the paper by adding method/evidence/theory support rather than weakening TRACE-SL into an incremental heuristic.
- Use “certificate-guided” or “posterior-certificate-aware” unless the text is explicitly limited to the linear-Gaussian posterior trace identity.
- Frame greedy, trace-swap, RCSS, and validation-swap as offline planning/design heuristics for sensor placement, not online control policies.
- Treat posterior trace/logdet/condition/CVaR/coverage as transparent diagnostics and surrogate terms that guide selection and explain empirical performance.

</specifics>

<deferred>
## Deferred Ideas

- Implementing or expanding reviewer-grade baselines belongs to Phase 3.
- Regenerating core evidence, statistical comparisons, and certificate correlations belongs to Phase 4.
- Running robustness, missingness, cost, temporal-shift, or candidate-count stress tests belongs to Phase 5.
- Proving broad submodularity/approximation/stability guarantees belongs to v2/TR Part B extension work unless a narrow, correct statement falls naturally out of Phase 2.
- Writing the final Transportation Science manuscript package belongs to Phase 7.

</deferred>

---

*Phase: 2-Formulation and Theory Bridge*
*Context gathered: 2026-05-22*
