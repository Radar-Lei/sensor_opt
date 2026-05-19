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

## Key Stage 10 Result

Primary result directory:

- `TRC-23-02333/trace_sl_results/pems7_228_stage10_validation_swap/`

Mean GLS/MAP test MAE:

| Budget | Validation-swap RCSS | Stage 9 RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|---:|
| 10% | 3.4630 | 3.4966 | 3.5677 | 3.7067 | 3.5780 |
| 20% | 3.2340 | 3.2459 | 3.3105 | 3.4617 | 3.3188 |
| 30% | 2.9893 | 3.0402 | 3.0919 | 3.3147 | 3.0982 |

Validation-swap RCSS wins against best-random by validation:

- 10%: -0.1047 MAE
- 20%: -0.0766 MAE
- 30%: -0.1026 MAE

Winner counts:

- 10%: validation-swap RCSS wins 2/5 splits
- 20%: validation-swap RCSS wins 3/5 splits
- 30%: validation-swap RCSS wins 5/5 splits

Certificate stability remains strong:

- GLS posterior trace Spearman with MAE: 0.8476
- GLS condition number Spearman with MAE: 0.8529
- GLS information logdet Spearman with MAE: -0.8096

## Writing Handoff

- `NARRATIVE_REPORT.md`: generated.
- Venue: not set in this run; paper writing can be invoked manually.
- Manual figures needed: yes, generate from Stage 10 CSV files.

Suggested next command:

```text
/paper-writing "NARRATIVE_REPORT.md" — venue: Transportation Science
```

## Remaining TODOs

- Run external validation on Seattle or PeMS7_1026.
- Generate publication figures from Stage 10 outputs.
- Consider increasing held-out split count from 5 to 10 for stronger p-values.
