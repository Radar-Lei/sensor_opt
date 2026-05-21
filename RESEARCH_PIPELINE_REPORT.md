# Research Pipeline Report

**Direction**: Strengthen TRACE-SL without narrowing the claim.
**Chosen method**: Robust Certified Sensor Search (RCSS) with quality-coverage OR-guided candidate generation and validation-aware swap refinement.
**Date**: 2026-05-18
**Pipeline stage**: implementation -> CPU experiments -> confirmatory analysis -> writing handoff

## Journey Summary

- Existing TRACE-SL Stage 6 showed strong certificate validity but insufficient dominance over validation-selected random layouts.
- Stage 7 added RCSS candidate scoring and showed strong gains over random mean, but 30% budget was still slightly behind best-random.
- Stage 8 tested fixed diagnostic weights on new split seeds and showed the existing candidate pool was not strong enough at 20% and 30%.
- Stage 9 added quality-coverage OR-guided candidates and confirmed RCSS wins over validation-selected random layouts at 10%, 20%, and 30% budgets.
- Stage 10 added validation-aware swap refinement and further widened the advantage, especially at 30% budget where it wins all five held-out splits.

## Implementation

Modified files:

- `TRC-23-02333/transparent_estimator_eval.py`
  - added posterior condition/logdet/CVaR helpers;
  - added robust coverage-CVaR layout;
  - added quality-coverage sampling;
  - added RCSS candidate scoring and outputs;
  - added validation-aware stochastic swap search.
- `TRC-23-02333/summarize_trace_sl_rcss.py`
  - added multi-split aggregation, delta tables, winner counts, and selected-source summaries.

Generated handoff:

- `NARRATIVE_REPORT.md`

## Key Stage 11 Ten-Split Result

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

Certificate stability remains strong:

- GLS posterior trace Spearman with MAE: 0.8513
- GLS condition number Spearman with MAE: 0.8592
- GLS information logdet Spearman with MAE: -0.8130

## PeMS7_1026 External Validation

Primary result directory:

- `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`

Mean GLS/MAP test MAE:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6557 | 3.7437 | 3.8266 | 3.8602 |
| 20% | 3.2547 | 3.4653 | 3.5317 | 3.5859 |
| 30% | 2.9951 | 3.2483 | 3.3309 | 3.3266 |

Validation-swap RCSS paired deltas against best-random by validation:

| Budget | Mean delta | Win count | paired t-test p | Wilcoxon p |
|---:|---:|---:|---:|---:|
| 10% | -0.0879 | 5/5 | 0.0212 | 0.0625 |
| 20% | -0.2105 | 5/5 | 0.0007 | 0.0625 |
| 30% | -0.2531 | 5/5 | 0.0001 | 0.0625 |

External certificate stability is very strong:

- GLS posterior trace Spearman with MAE: 0.9315
- GLS condition number Spearman with MAE: 0.8930
- GLS information logdet Spearman with MAE: -0.8982

## Seattle Heterogeneous-Network Validation

Primary result directory:

- `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`

Mean GLS/MAP test MAE:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.0677 | 3.1888 | 3.3204 | 3.5499 |
| 20% | 2.8036 | 2.9488 | 3.0172 | 3.0796 |
| 30% | 2.6182 | 2.7243 | 2.8449 | 2.8090 |

Validation-swap RCSS paired deltas against best-random by validation:

| Budget | Mean delta | Win count | paired t-test p | Wilcoxon p |
|---:|---:|---:|---:|---:|
| 10% | -0.1210 | 5/5 | 0.0013 | 0.0625 |
| 20% | -0.1452 | 5/5 | 0.0032 | 0.0625 |
| 30% | -0.1061 | 5/5 | 0.0025 | 0.0625 |

Seattle GLS/MAP certificate stability remains strong:

- GLS posterior trace Spearman with MAE: 0.8742
- GLS condition number Spearman with MAE: 0.8846
- GLS information logdet Spearman with MAE: -0.8307

## Writing Handoff

- `NARRATIVE_REPORT.md`: generated and updated with Stage 11 auto-weight framing and Seattle validation.
- Reproducibility entry points: `README.md`, `requirements.txt`, `scripts/run_stage11_pems7_228.sh`, `scripts/run_stage11_pems7_1026.sh`, `scripts/run_stage11_seattle.sh`, and `TRC-23-02333/trace_sl_results/README.md`.
- Venue: Transportation Science is the working target, but final venue is not fixed in code.
- Manual figures needed: yes, generate from PeMS7_228 ten-split, PeMS7_1026 external-validation, and Seattle heterogeneous-network CSV files.

Suggested next command:

```text
/paper-writing "NARRATIVE_REPORT.md" — venue: Transportation Science
```

## Remaining TODOs

- Generate publication figures from PeMS7_228 ten-split, PeMS7_1026 external-validation, and Seattle heterogeneous-network outputs.
- Optional: increase PeMS7_1026 or Seattle split count if a reviewer demands stronger nonparametric tests.
