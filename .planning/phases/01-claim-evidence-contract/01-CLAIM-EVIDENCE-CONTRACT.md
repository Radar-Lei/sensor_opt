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

_To be completed in Task 3 after the matrix rows are populated._

## Downstream Phase Routing

_To be completed in Task 3 after each claim row has a downstream owner._

## Non-Goals for Phase 1

- Do not implement new baselines; baseline portfolio work belongs to Phase 3.
- Do not run or regenerate experiments; core evidence audit/regeneration belongs to Phase 4, and robustness experiments belong to Phase 5.
- Do not edit TRACE-SL algorithms, evaluator code, launchers, or reconstruction methods.
- Do not read raw dataset files or make raw dataset paths Phase 1 evidence sources.
- Do not prove new theory; theorem-level posterior-error derivation belongs to Phase 2.
- Do not generate final paper tables or rewrite the final manuscript; manuscript integration belongs to Phase 7.
