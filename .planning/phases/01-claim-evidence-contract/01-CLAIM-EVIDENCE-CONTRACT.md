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
