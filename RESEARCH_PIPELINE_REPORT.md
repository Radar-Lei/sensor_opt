# Research Pipeline Report

**Current method**: TRACE-BiOpt — Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting.
**Target venue**: Transportation Research Part B: Methodological (Elsevier CAS template).
**Date**: 2026-05-28
**Pipeline stage**: TRACE-BiOpt evidence complete, manuscript compiled, submission-ready.
**Aggregate claim status**: `supported_submission_ready`

## Current Status (2026-05-28)

The project has evolved from the original TRACE-SL/RCSS candidate-pool framework into TRACE-BiOpt, a recoverability-driven bilevel optimization method. The key transition:

- **TRACE-SL/RCSS** (Stages 6--14): OR-guided candidate pool + validation-calibrated selection + validation-aware swap refinement. A strong empirical framework, but fundamentally a candidate-pool selector over pre-generated layouts.
- **TRACE-BiOpt** (Stages 15--16): One recoverability-driven bilevel objective + one transparent GLS/MAP lower-level inverse problem + one formal CVaR tail-risk epigraph + one deterministic initialization-and-exchange solver. Not a candidate-pool selector.

The current manuscript title is *TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting*. The method contract is in `TRACE_BIOPT_SPEC.md`. The authoritative evidence source is `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/`.

### TRACE-BiOpt headline evidence

Across 9 tested dataset-budget regimes (PeMS7_228, PeMS7_1026, Seattle at 10/20/30%), TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered baselines spanning 11 method families. After Holm correction across all 189 paired comparisons, no challenger remains statistically tied or significantly better. 8/9 rows are promoted from Stage 16 calibrated reruns; Seattle 10% is retained on the audited Stage 15 lane.

Auxiliary evidence: 27/27 deterministic 16-node audited subnetwork cases are exact hits with zero objective gap.

## Journey Summary

### Phase 1: TRACE-SL/RCSS Foundation (Stages 6--14)

- Stage 6: Multi-split baseline with scenario/CVaR certificate diagnostics; strong certificate validity but insufficient dominance over validation-selected random layouts.
- Stage 7: Initial RCSS candidate scoring; strong gains over random mean, but 30% budget slightly behind best-random.
- Stage 8: Fixed diagnostic weights on new splits; candidate pool not strong enough at 20% and 30%.
- Stage 9: Added quality-coverage OR-guided candidates; RCSS beats validation-selected random at all budgets.
- Stage 10: Added validation-aware swap refinement; widened advantage, especially at 30% budget.
- Stage 11: Replaced fixed RCSS weights with inner-validation weight selection; ten-split extension added seeds 30--34.
- Stage 12: Expanded comparator portfolio and external ten-split evidence for PeMS7_228, PeMS7_1026, and Seattle.
- Stage 13: Candidate-count sensitivity, selected-source diagnostics, and measured runtime.
- Stage 14: Held-out stress-test robustness evidence for sensor failure, observation noise, missingness, cost proxy, and chronological split conditions.

### Phase 2: TRACE-BiOpt Method Upgrade (Stages 15--16)

- Stage 15: TRACE-BiOpt bilevel optimization implemented and evaluated across all datasets and budgets. The method replaces candidate-pool selection with a single recoverability-driven objective solved deterministically.
- Stage 16: Calibrated rerun of TRACE-BiOpt with refined solver parameters. 8/9 rows promoted into the current-best evidence chain.

## Implementation

### TRACE-BiOpt implementation

- `TRC-23-02333/trace_biopt.py`: TRACE-BiOpt solver implementation with bilevel objective, deterministic initialization (relaxed rounding or objective-forward construction), and greedy one-swap exchange refinement.
- `TRC-23-02333/transparent_estimator_eval.py`: extended with `--include-biopt` flag for TRACE-BiOpt evaluation; retains all TRACE-SL/RCSS functionality as baselines.

### Legacy TRACE-SL/RCSS implementation

- `TRC-23-02333/transparent_estimator_eval.py`: TRACE-SL evaluator with RCSS candidate scoring, validation-aware swap refinement, and posterior/certificate diagnostics.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: multi-split result aggregation.

## TRACE-BiOpt Evidence Detail

### Current-best paper-facing evidence

Directory: `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/`

Key artifacts:
- `trace_biopt_claim_contract.json`: row-level and aggregate wording contract (`supported_submission_ready`).
- `trace_biopt_best_baseline_delta.csv`: TRACE-BiOpt MAE vs best baseline per dataset-budget.
- `trace_biopt_full_baseline_matrix.csv`: full 9-row x 21-baseline comparison matrix.
- `trace_biopt_current_best_provenance.csv`: row-level source policy (Stage 15 or Stage 16).
- `trace_biopt_exact_subnetwork_summary.csv`: 27/27 exact subnetwork hits.
- `TRACE_BIOPT_DOMINANCE.md`: Holm-corrected dominance summary.

### Stage 15 main evidence

Directories:
- `TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_10seed_v2/`
- `TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_3seed_v2/`
- `TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_seed25/`
- `TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_seed25_v2/`
- `TRC-23-02333/trace_sl_results/stage15_biopt_pems1026_30_extra/`

### Stage 16 calibrated rerun

Directories:
- `TRC-23-02333/trace_sl_results/stage16_calibrated_trace_probe/`
- `TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/`

## Historical TRACE-SL/RCSS Evidence (Stages 6--14)

The sections below record the development path through Stages 6--14. They are preserved as TRACE-BiOpt predecessor history. Stage 12 paper-source artifacts remain valid as historical TRACE-SL baseline evidence but should not be used as the primary manuscript source of truth for the current TRACE-BiOpt paper.

### Stage 11 Ten-Split TRACE-SL Result

Primary result directory:

- `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`

Mean GLS/MAP test MAE:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6055 | 3.6913 | 3.8359 | 3.7304 |
| 20% | 3.3095 | 3.3969 | 3.5648 | 3.4276 |
| 30% | 3.0665 | 3.1832 | 3.4032 | 3.2004 |

Validation-swap RCSS paired deltas against best-random by validation:

| Budget | Mean delta | Win count | paired t-test p | Wilcoxon p |
|---:|---:|---:|---:|---:|
| 10% | -0.0858 | 7/10 | 0.0343 | 0.0273 |
| 20% | -0.0874 | 9/10 | 0.0025 | 0.0059 |
| 30% | -0.1167 | 10/10 | 0.00008 | 0.0020 |

Certificate stability:

- GLS posterior trace Spearman with MAE: 0.8513
- GLS condition number Spearman with MAE: 0.8592
- GLS information logdet Spearman with MAE: -0.8130

### Stage 11 PeMS7_1026 External Validation

Primary result directory:

- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`

Mean GLS/MAP test MAE:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6557 | 3.7437 | 3.8266 | 3.8602 |
| 20% | 3.2547 | 3.4653 | 3.5317 | 3.5859 |
| 30% | 2.9951 | 3.2483 | 3.3309 | 3.3266 |

### Stage 11 Seattle Heterogeneous-Network Validation

Primary result directory:

- `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`

Mean GLS/MAP test MAE:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.0677 | 3.1888 | 3.3204 | 3.5499 |
| 20% | 2.8036 | 2.9488 | 3.0172 | 3.0796 |
| 30% | 2.6182 | 2.7243 | 2.8449 | 2.8090 |

## Writing Handoff

- `NARRATIVE_REPORT.md`: updated with TRACE-BiOpt method framing and current-best evidence.
- `PAPER_PLAN.md`: updated with TRACE-BiOpt claims-evidence matrix.
- `TRACE_BIOPT_SPEC.md`: method contract.
- `TRACE_BIOPT_THEORY.md`: theory statement contract.
- `paper/`: current TR Part B manuscript compiled to PDF.
- Reproducibility entry points: `TRACE_BIOPT_SPEC.md` Section 6, `scripts/refresh_current_best_trace_biopt_paper_chain.sh`.
- Venue: Transportation Research Part B: Methodological.
