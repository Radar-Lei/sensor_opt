# Phase 1: Claim-Evidence Contract

**Status:** Draft contract for downstream phases  
**Date:** 2026-05-21

## Phase Boundary

This phase delivers the paper-facing claim-evidence contract for TRACE-SL before additional experiments, theory writing, or manuscript drafting. It locks the strongest defensible contribution claims, defines what evidence each claim requires, constrains terminology around certificates, handles the 10% PeMS7_228 multistart caveat, and positions TRACE-SL against deterministic full-observability TSLP and black-box imputation/forecasting.

It does not implement new baselines, run new experiments, prove theory, generate final paper tables, or rewrite the full manuscript. Those belong to later phases.

For Phase 1 execution, this means:

- No new experiments.
- No algorithm edits.
- No baseline implementation.
- No raw dataset reads.
- No final manuscript writing.

## Source Register

### Planning and Claim-Scope Sources

- `.planning/PROJECT.md` — project value, target venue, constraints, and active decisions.
- `.planning/STATE.md` — current workflow state and active decisions for Phase 1.
- `.planning/ROADMAP.md` — Phase 1 goal, requirements CLAIM-01..CLAIM-05, and downstream phase responsibilities.
- `.planning/REQUIREMENTS.md` — claim/framing requirements and global out-of-scope constraints.
- `.planning/phases/01-claim-evidence-contract/01-CONTEXT.md` — user decisions D-01..D-15 and Phase 1 boundary.
- `.planning/phases/01-claim-evidence-contract/01-PATTERNS.md` — artifact structure, evidence vocabulary, and source hygiene patterns.
- `README.md` — current public-facing TRACE-SL framing and reproduction entry points.
- `NARRATIVE_REPORT.md` — current method summary, evidence narrative, and claim status.

### Curated Evidence Sources to Reference, Not Recompute

- `TRC-23-02333/trace_sl_results/README.md` — curated result inventory and current main-method guidance.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md` — main in-domain PeMS7_228 ten-split evidence summary.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/gls_map_layout_summary.csv` — held-out GLS/MAP layout-level performance summary.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/gls_map_delta_summary.csv` — held-out deltas against curated baselines.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/gls_map_paired_delta_tests.csv` — paired/statistical comparison evidence.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/certificate_correlation_summary.csv` — aggregate certificate-error correlation evidence.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/combined_rcss_candidates.csv` — candidate-level RCSS diagnostics for later audit.
- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/rcss_selected_sources.csv` — selected candidate source counts and low-budget comparator context.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/SUMMARY.md` — external PeMS7_1026 evidence summary with lower split count.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/gls_map_layout_summary.csv` — external-network held-out layout performance summary.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/gls_map_paired_delta_tests.csv` — external-network paired/statistical comparison evidence.
- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/certificate_correlation_summary.csv` — external-network certificate-error correlation evidence.
- `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/` — conditional/supporting-only Seattle evidence pending Phase 4 curation.

Raw dataset paths are not Phase 1 evidence sources and must not be read or cited as evidence inputs in this contract.

## Claim-Evidence Matrix

Evidence status taxonomy: present | needs audit | needs new experiment | theory-dependent | wording-only limitation

Evidence type vocabulary: held-out test result | paired/statistical comparison | robustness test | external-network evidence | formal derivation/theory | reproducible artifact | limitation wording

Validation MAE is selection evidence only, never final performance evidence. Final performance claims must point to held-out test metrics from curated result artifacts.

| Claim ID | Requirement | Claim wording | Evidence required | Current evidence source | Evidence status | Caveat / limitation wording | Downstream phase owner |
|---|---|---|---|---|---|---|---|
| C-01 | CLAIM-01 | TRACE-SL is transparent reconstruction-aware sparse traffic sensor placement for full-network reconstruction: it selects sparse sensors so transparent GLS/MAP/GSP-style reconstruction can recover hidden traffic states under limited budgets, rather than acting as candidate-pool tuning or an ad hoc empirical heuristic. | reproducible artifact; formal derivation/theory; held-out test result showing the fixed transparent reconstruction model is evaluated on hidden links after layout selection. | `README.md`; `NARRATIVE_REPORT.md`; `TRC-23-02333/trace_sl_results/README.md`; `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md`; `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/SUMMARY.md`. | needs audit | Current artifacts support the framing, but Phase 2 must formalize the design problem and Phase 4 must audit that paper wording consistently distinguishes layout design from estimator invention. | Phase 2 for formulation; Phase 4 for evidence audit; Phase 7 for manuscript wording. |
| C-02 | CLAIM-02 | Primary contribution claims are separated into method contribution, performance evidence, certificate evidence, and scope/limitations so unsupported claims are strengthened with evidence, theory, or limitation wording rather than weakened prematurely. | held-out test result; paired/statistical comparison; robustness test; external-network evidence; formal derivation/theory; reproducible artifact; limitation wording. | `NARRATIVE_REPORT.md`; PeMS7_228 curated CSVs `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `certificate_correlation_summary.csv`; PeMS7_1026 curated `SUMMARY.md` and paired-test/certificate summaries; `.planning/REQUIREMENTS.md`. | needs audit | Held-out PeMS evidence and external-network evidence are present, but robustness tests, confidence/effect-size audit, and theory support remain downstream; validation MAE is selection evidence only and cannot substitute for final performance evidence. | Phase 4 for held-out audit/statistics; Phase 5 for robustness; Phase 2 for theory; Phase 6 for artifact curation. |
| C-03 | CLAIM-03 | The performance claim is bounded: the predeclared TRACE-SL portfolio can claim reconstruction improvements over random, validation-selected random, and topology/variance baselines where held-out results support it, while the 10% PeMS7_228 multistart-vs-RCSS issue is reserved as a predeclared comparator/portfolio issue or bounded low-budget caveat. | held-out test result; paired/statistical comparison; reproducible artifact; limitation wording; explicit Phase 3 decision on whether multistart validation refinement is a named comparator or portfolio member. | `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md` lines with 10% `multistart_swap_by_validation` mean 3.578255 versus `validation_swap_selected` mean 3.605467; `gls_map_paired_delta_tests.csv`; `rcss_selected_sources.csv`; PeMS7_1026 `SUMMARY.md`. | present | Do not use post-hoc best-method-per-budget selection. At 10% PeMS7_228, multistart validation refinement can outperform validation-swap RCSS, so Phase 3 must predeclare its role before Phase 4 reporting. | Phase 3 for comparator/portfolio resolution; Phase 4 for final audit/statistics; Phase 7 for caveat wording. |
| C-04 | CLAIM-04 | Certificate language is limited to certificate-guided, posterior-certificate-aware, or certificate diagnostics. Posterior trace, condition number, and information logdet correlations are empirical guidance and interpretability evidence, while theorem-level posterior-error derivation is a separate Phase 2 theory-dependent claim. | empirical certificate-error correlation evidence; formal derivation/theory; held-out test result linked to certificate diagnostics; reproducible artifact; limitation wording. | `NARRATIVE_REPORT.md`; `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md`; `certificate_correlation_summary.csv`; `combined_certificate_correlations.csv`; PeMS7_1026 certificate summaries. | theory-dependent | Current correlations support interpretability and empirical guidance only; they do not prove certified optimality or guaranteed error bounds unless Phase 2 adds theorem-level support. | Phase 2 for posterior-error derivation; Phase 4 for certificate-error audit; Phase 7 for terminology control. |
| C-05 | CLAIM-05 | TRACE-SL is positioned against deterministic full-observability TSLP by emphasizing partial-observation reconstruction quality, uncertainty, validation performance, and held-out error; it is positioned against black-box imputation/forecasting by emphasizing transparent reconstruction models and sensor-layout design rather than a learned predictor. Seattle evidence is conditional/supporting-only unless Phase 4 curates repository-visible outputs and documentation consistency. | external-network evidence; held-out test result; paired/statistical comparison; reproducible artifact; limitation wording; repository-visible Seattle curation if Seattle becomes core. | `README.md`; `NARRATIVE_REPORT.md`; `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/SUMMARY.md`; conditional `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`; `.planning/PROJECT.md`. | needs audit | PeMS7_1026 can support external-network positioning with lower split count; Seattle must remain conditional/supporting-only and non-core until Phase 4 curation succeeds. | Phase 4 for Seattle and external evidence audit; Phase 6 for reproducible artifact curation; Phase 7 for related-work positioning. |

## Reserved Caveats and Guardrails

- **No “best at all budgets” claim (D-08):** The contract prohibits unsupported wording that TRACE-SL is best at all budgets or against every comparator. Claims must be scoped to supported held-out test evidence and named baselines.
- **No formal “certified” branding without theorem-level support (D-10, D-11):** Use certificate-guided, posterior-certificate-aware, or certificate diagnostics only. Posterior trace, condition number, and information logdet correlations are empirical guidance and interpretability evidence, not formal certified optimality or guaranteed reconstruction-error bounds.
- **No validation MAE as final performance evidence (D-05):** Validation MAE can select, tune, or refine layouts; it cannot be cited as final performance evidence. Final performance claims require held-out test metrics and paired/statistical comparison evidence from curated artifacts.
- **No non-curated Seattle result as core evidence (D-15):** Seattle evidence remains conditional/supporting-only unless Phase 4 curates repository-visible outputs, verifies documentation consistency, and confirms that paper-facing artifacts can trace the numbers.
- **No post-hoc best-method-per-budget selection (D-07):** The 10% PeMS7_228 multistart-vs-RCSS issue must be handled as a predeclared comparator/portfolio issue or bounded low-budget caveat, not by selecting whichever method wins after seeing held-out test outcomes.
- **No conflation of empirical correlation with theory (D-12):** Empirical certificate-error correlations and theoretical posterior-error derivations must remain separate evidence channels until Phase 2 establishes theorem-level support.
- **No raw-data evidence dependency:** The contract may reference curated summaries and CSVs under `TRC-23-02333/trace_sl_results/`, but must not require reading raw dataset files as Phase 1 evidence sources.

## Downstream Phase Routing

| Downstream phase | Routed responsibility | Related rows / decisions |
|---|---|---|
| Phase 2: Formulation and Theory Bridge | Formalize the reconstruction-aware sparse sensor design problem, define the TRACE-SL/RCSS surrogate, and decide whether posterior certificates support theorem-level language. | C-01, C-04; D-01, D-02, D-10, D-11, D-12 |
| Phase 3: Baseline Portfolio | Resolve whether multistart validation refinement is a named comparator or predeclared portfolio member; strengthen reviewer-grade baselines without post-hoc selection. | C-03; D-07, D-08, D-09 |
| Phase 4: Core Experiment Evidence | Audit PeMS7_228 held-out results, paired/statistical comparisons, PeMS7_1026 lower-power external evidence, certificate correlations, and Seattle curation if Seattle is retained. | C-01, C-02, C-03, C-04, C-05; D-04, D-05, D-13, D-15 |
| Phase 5: Robustness and Generality | Add robustness evidence for sensor failure, observation noise, missing readings, nonuniform costs, temporal shift, and candidate-count sensitivity. | C-02; D-03, D-04 |
| Phase 6: Reproducibility and Artifact Curation | Ensure all paper-visible evidence is traceable to curated scripts, summaries, and non-sensitive artifacts; preserve raw dataset hygiene. | C-02, C-05; D-04, D-15 |
| Phase 7: Transportation Science Manuscript Package | Integrate the locked claim wording, caveats, positioning against TSLP and black-box imputation/forecasting, and limitation language into the manuscript. | C-01..C-05; D-01..D-15 |

## Self-Check

- [x] CLAIM-01 is covered by C-01.
- [x] CLAIM-02 is covered by C-02.
- [x] CLAIM-03 is covered by C-03.
- [x] CLAIM-04 is covered by C-04.
- [x] CLAIM-05 is covered by C-05.
- [x] D-01 is covered: TRACE-SL is framed as transparent reconstruction-aware sparse traffic sensor placement, not candidate-pool tuning or an ad hoc empirical heuristic.
- [x] D-02 is covered: the sparse sensor design problem is tied to transparent GLS/MAP/GSP-style full-network reconstruction under limited budgets.
- [x] D-03 is covered: method contribution, performance evidence, certificate evidence, and scope/limitations are separated.
- [x] D-04 is covered: every primary claim row maps to explicit evidence types.
- [x] D-05 is covered: validation MAE is selection evidence only, not final performance evidence.
- [x] D-06 is covered: evidence status taxonomy is present | needs audit | needs new experiment | theory-dependent | wording-only limitation.
- [x] D-07 is covered: the 10% PeMS7_228 multistart issue is predeclared as comparator/portfolio or bounded-caveat work.
- [x] D-08 is covered: unsupported “best at all budgets” wording is prohibited.
- [x] D-09 is covered: C-03 reserves multistart validation refinement for later validation as comparator or portfolio member.
- [x] D-10 is covered: certificate wording is limited to certificate-guided, posterior-certificate-aware, or certificate diagnostics unless Phase 2 adds theorem-level support.
- [x] D-11 is covered: posterior trace, condition number, and information logdet correlations are interpretability and empirical guidance only.
- [x] D-12 is covered: empirical certificate-error correlation and theoretical posterior-error derivation are separate evidence tracks.
- [x] D-13 is covered: positioning against deterministic full-observability TSLP emphasizes partial-observation reconstruction quality, uncertainty, validation performance, and held-out error.
- [x] D-14 is covered: positioning against black-box imputation/forecasting emphasizes transparent reconstruction models and sensor-layout design.
- [x] D-15 is covered: Seattle evidence is conditional/supporting-only unless Phase 4 curation succeeds.
- [x] Deferred ideas are excluded: no new experiments, algorithm changes, baseline implementation, raw dataset reads, or final manuscript writing are assigned to Phase 1.
- [x] Raw dataset paths are not used as Phase 1 evidence sources.

## Non-Goals for Phase 1

- Do not implement new baselines; baseline portfolio work belongs to Phase 3.
- Do not run or regenerate experiments; core evidence audit/regeneration belongs to Phase 4, and robustness experiments belong to Phase 5.
- Do not edit TRACE-SL algorithms, evaluator code, launchers, or reconstruction methods.
- Do not read raw dataset files or make raw dataset paths Phase 1 evidence sources.
- Do not prove new theory; theorem-level posterior-error derivation belongs to Phase 2.
- Do not generate final paper tables or rewrite the final manuscript; manuscript integration belongs to Phase 7.
