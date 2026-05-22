# Phase 4: Core Experiment Evidence - Context

**Gathered:** 2026-05-22
**Status:** Ready for planning
**Mode:** Auto-selected decisions from `/gsd-autonomous --from 4 非必要不要询问我，请自动推进`

<domain>
## Phase Boundary

This phase produces the main held-out evidence package for TRACE-SL's Transportation Science performance and certificate-guided claims. It must audit or regenerate PeMS7_228 ten-split evidence for final method variants and core baselines, decide how PeMS7_1026 is framed or extended, curate or demote Seattle evidence, add paired deltas/confidence/effect-size/statistical summaries, report empirical certificate-error correlations, and provide runtime plus candidate-count sensitivity summaries for main claim settings.

The phase should work from existing evaluator, summarizer, run scripts, and curated `TRC-23-02333/trace_sl_results/` artifacts. It should not introduce new robustness stress tests beyond runtime/candidate sensitivity, rewrite the method/theory framing, broaden baseline families beyond Phase 3's implemented/evidence hooks, or draft the final manuscript.

</domain>

<decisions>
## Implementation Decisions

### Evidence Scope and Claim Discipline
- **D-01:** Treat held-out GLS/MAP test metrics in `metrics.csv`/`combined_metrics.csv` as final performance evidence; validation MAE remains selection evidence only.
- **D-02:** Preserve the strong TRACE-SL claim strategy from Phase 1, but route every comparison through audited artifacts and explicit caveats rather than unsupported prose.
- **D-03:** Keep `validation_swap_selected` and any Phase 3 final baseline/multistart portfolio labels stable; do not rename paper-facing rows unless the artifact mapping is updated everywhere.
- **D-04:** The 10% PeMS7_228 multistart caveat must remain visible in summaries rather than being hidden by post-hoc best-method selection.

### Dataset Evidence Decisions
- **D-05:** PeMS7_228 ten-split evidence is the primary core evidence bundle and should be audited first for all final method variants and core baselines.
- **D-06:** PeMS7_1026 should be extended to ten splits only if the existing scripts/data make it safe and tractable; otherwise document it as lower-power external evidence with effect-size/uncertainty language.
- **D-07:** Seattle evidence may be included as core only if its result directory, README guidance, scripts, and generated summaries are synchronized; otherwise it should be marked supporting/conditional or removed from core claims.
- **D-08:** Raw datasets under `TRC-23-02333/dataset/` must remain local and ignored; inspect loader expectations and artifact summaries, not raw dataset contents, unless a run command requires local data.

### Statistical Reporting
- **D-09:** Report paired deltas, confidence or bootstrap-style intervals, effect sizes, and suitable paired tests for each paper-visible comparison, not only p-values or winner counts.
- **D-10:** Use existing `TRC-23-02333/summarize_trace_sl_rcss.py` as the main aggregation point; extend it or add a small adjacent summary script only if current outputs cannot express required intervals/effect sizes.
- **D-11:** Certificate-error correlation summaries should remain empirical support for certificate-guided selection unless the formal theorem scope from Phase 2 explicitly applies.
- **D-12:** Runtime and candidate-count sensitivity should be summarized as evidence about practical tractability and selection stability, not as a full scalability claim.

### Execution and Artifact Strategy
- **D-13:** Prefer auditable regeneration/check scripts and committed summary artifacts over ad hoc notebook-style calculations.
- **D-14:** New result stages should live under descriptive `TRC-23-02333/trace_sl_results/<dataset>_stage<stage>_<descriptor>/` directories and must be reviewed against `.gitignore` before committing.
- **D-15:** Full expensive experiment reruns should be avoided unless existing artifacts are missing or stale; first audit current Stage 11/12 outputs and scripts.
- **D-16:** Validation should include smoke/aggregate checks that generated summaries contain required layout/method rows, split counts, budgets, and statistical columns.

### Claude's Discretion
The planner may choose whether Phase 4 is implemented by extending the existing summarizer, adding a focused evidence-audit script, adding Stage 12 launcher defaults, or only curating existing artifacts, as long as EXP-01..EXP-06 are explicitly satisfied or defensibly caveated. Bias toward minimal, reproducible changes in existing scripts and result summaries over broad refactors.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### GSD Scope and Requirements
- `.planning/ROADMAP.md` — Defines Phase 4 goal, EXP-01..EXP-06, success criteria, and Phase 3 dependency.
- `.planning/REQUIREMENTS.md` — Defines experiment evidence requirements and global evidence/claim constraints.
- `.planning/PROJECT.md` — Defines target venue, evidence standard, Seattle caveat, and dataset/reproducibility constraints.
- `.planning/STATE.md` — Current workflow state and active decisions.
- `.planning/phases/01-claim-evidence-contract/01-CONTEXT.md` — Locks claim strategy, validation/test separation, certificate terminology, and multistart caveat policy.
- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-MATRIX.md` — Claim/evidence matrix to update or reference when marking Phase 4 evidence status.
- `.planning/phases/02-formulation-and-theory-bridge/02-CONTEXT.md` — Locks posterior-certificate wording and theory boundaries.
- `.planning/phases/03-baseline-portfolio/03-CONTEXT.md` — Locks baseline naming, portfolio evidence hooks, and multistart comparator handling.
- `.planning/phases/03-baseline-portfolio/03-BASELINE-INVENTORY.md` — Baseline coverage inventory if present; use it to know which core baselines must appear in Phase 4 evidence.

### Current Experiment Sources
- `TRC-23-02333/transparent_estimator_eval.py` — Primary evaluator, layout generation, reconstruction metrics, certificate outputs, runtime-sensitive candidate settings, and artifact writer.
- `TRC-23-02333/summarize_trace_sl_rcss.py` — Multi-split aggregation, paired delta tests, ablation summaries, certificate summaries, and Markdown summaries.
- `scripts/run_stage11_pems7_228.sh` — Current main PeMS7_228 run launcher.
- `scripts/run_stage11_pems7_1026.sh` — Current PeMS7_1026 external-validation launcher.
- `scripts/run_stage11_seattle.sh` — Current Seattle launcher.
- `scripts/run_stage12_pems7_228.sh` — Stage 12 launcher present in the repo; inspect before deciding whether Phase 4 should reuse or update it.

### Current Result Artifacts
- `TRC-23-02333/trace_sl_results/README.md` — Curated result inventory and interpretation guidance.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md` — Primary PeMS7_228 ten-split evidence bundle.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/*.csv` — Aggregate PeMS7_228 statistics/correlation summaries.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/SUMMARY.md` — Current external PeMS7_1026 evidence bundle.
- `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/SUMMARY.md` — Conditional Seattle evidence bundle.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_extra/` and other Stage 6-11 result directories — Historical/supporting evidence to audit but not automatically elevate to core claims.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` — Explains evaluator layers, artifact flow, validation/test separation, and anti-patterns.
- `.planning/codebase/STRUCTURE.md` — Locates scripts, result artifacts, dataset boundary, and where new code/artifacts should go.
- `.planning/codebase/TESTING.md` — Defines smoke validation and artifact-schema checks.
- `.planning/codebase/CONVENTIONS.md` — Documents naming and reproducibility conventions.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `TRC-23-02333/summarize_trace_sl_rcss.py`: Existing aggregate mechanism for `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `gls_map_ablation_summary.csv`, `gls_map_per_split_winners.csv`, `gls_map_win_counts.csv`, `certificate_correlation_summary.csv`, and `SUMMARY.md`.
- `TRC-23-02333/transparent_estimator_eval.py`: Existing per-seed artifact writer for `metrics.csv`, `layouts.json`, `rcss_candidates.csv`, `certificate_correlations.csv`, `config.json`, and runtime-relevant configuration.
- Stage 11 scripts in `scripts/`: Reproducible launch patterns with deterministic seeds, budgets, candidate counts, and BLAS thread caps.
- `TRC-23-02333/trace_sl_results/`: Existing Stage 6-11, PeMS7_228 ten-split, PeMS7_1026, Seattle, and sanity result artifacts.

### Established Patterns
- The project is a script-oriented research pipeline; add focused CLI/script support instead of notebooks or copied evaluators.
- Evidence artifacts are CSV/JSON/Markdown under `TRC-23-02333/trace_sl_results/`; raw datasets stay ignored under `TRC-23-02333/dataset/`.
- Layouts are paper-visible via stable `layout_type` rows, and final claims should use held-out `method == "gls_map"` rows unless explicitly comparing reconstruction methods.
- No formal test suite exists; validate through deterministic smoke runs, aggregation checks, schema checks, and curated summaries.

### Integration Points
- Primary implementation target: `TRC-23-02333/summarize_trace_sl_rcss.py` if statistical intervals/effect sizes/candidate sensitivity summaries are missing.
- Secondary implementation target: `scripts/run_stage12_pems7_228.sh` or new launcher updates if Phase 4 requires reproducible evidence regeneration.
- Documentation/artifact targets: `TRC-23-02333/trace_sl_results/README.md`, phase-local audit summaries under `.planning/phases/04-core-experiment-evidence/`, and possibly claim/evidence matrix status updates.
- Validation target: smoke or audit commands that inspect generated CSV schemas and split/budget/layout coverage without reading or committing raw dataset files.

</code_context>

<specifics>
## Specific Ideas

- Start by auditing existing Stage 11/12 directories for split count, budget coverage, required final layout/baseline rows, and whether Phase 3 baseline additions are represented.
- Extend aggregation to include confidence intervals/bootstrap intervals and standardized or paired effect sizes if current summaries only contain deltas and paired tests.
- Produce a Phase 4 evidence audit table mapping EXP-01..EXP-06 to artifact paths, status, caveat, and paper claim implication.
- Treat PeMS7_1026 as lower-power external evidence unless ten-split outputs are already available or cheap to generate.
- Decide Seattle core/supporting status by checking whether `seattle_stage11_auto_weight_light` is documented consistently in the result README and scripts.
- Runtime/candidate sensitivity can be satisfied by summarizing existing configuration/runtime logs if present; otherwise add a minimal reproducible sensitivity run or explicitly mark as lower-priority evidence with a command to run.

</specifics>

<deferred>
## Deferred Ideas

- Sensor failure, observation noise, missing readings, nonuniform costs, temporal shift, and broad candidate-pool robustness belong to Phase 5.
- Paper-ready final figures/tables and manuscript prose belong to a later paper-writing/manuscript phase, though Phase 4 should generate reliable source tables.
- Refactoring the monolithic evaluator into modules and adding a full formal test suite belongs to v2 or Phase 6 only if needed for reproducibility checks.
- Committing or deleting raw datasets is out of scope and requires explicit user approval.

</deferred>

---

*Phase: 4-Core Experiment Evidence*
*Context gathered: 2026-05-22*
