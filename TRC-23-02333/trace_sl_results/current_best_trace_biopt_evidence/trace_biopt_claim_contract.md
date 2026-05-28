# TRACE-BiOpt Claim Contract

Schema: `trace_biopt_claim_contract_v1`

Aggregate allowed wording:

> Across the tested datasets and 10/20/30 percent budgets, TRACE-BiOpt has the lowest mean held-out GLS/MAP MAE against the pre-registered non-BiOpt baseline set.

Required aggregate caveat:

> All nine tested dataset-budget rows satisfy the paired-dominance gate; claims still remain restricted to the tested datasets and the pre-registered non-BiOpt baseline set.

| claim_id | claim_status | evidence_strength | trace_biopt_mean | best_baseline_mean | best_baseline_layout | trace_minus_best_baseline | paired_count | paired_win_count | paired_paired_t_p |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BIOPT-PeMS7_1026-10pct | supported_submission_ready | submission_ready_paired_dominance | 3.60465 | 3.73426 | swap_from_greedy_a_trace | -0.129614 | 10 | 10 | 1.89737e-06 |
| BIOPT-PeMS7_1026-20pct | supported_submission_ready | submission_ready_paired_dominance | 3.22309 | 3.34667 | validation_swap_selected | -0.123577 | 10 | 10 | 9.80855e-08 |
| BIOPT-PeMS7_1026-30pct | supported_submission_ready | submission_ready_paired_dominance | 3.0365 | 3.07404 | validation_swap_selected | -0.0375415 | 10 | 10 | 4.74508e-05 |
| BIOPT-PeMS7_228-10pct | supported_submission_ready | submission_ready_paired_dominance | 3.45332 | 3.5957 | validation_swap_selected | -0.142379 | 10 | 10 | 2.77959e-05 |
| BIOPT-PeMS7_228-20pct | supported_submission_ready | submission_ready_paired_dominance | 3.04362 | 3.31984 | validation_swap_selected | -0.276224 | 10 | 10 | 3.70148e-09 |
| BIOPT-PeMS7_228-30pct | supported_submission_ready | submission_ready_paired_dominance | 2.74136 | 3.07726 | validation_swap_selected | -0.335903 | 10 | 10 | 1.70161e-09 |
| BIOPT-Seattle-10pct | supported_submission_ready | submission_ready_paired_dominance | 3.04161 | 3.09733 | rcss_selected | -0.0557176 | 10 | 10 | 0.00208353 |
| BIOPT-Seattle-20pct | supported_submission_ready | submission_ready_paired_dominance | 2.73298 | 2.81571 | validation_swap_selected | -0.0827233 | 10 | 10 | 2.06428e-05 |
| BIOPT-Seattle-30pct | supported_submission_ready | submission_ready_paired_dominance | 2.51438 | 2.60958 | validation_swap_selected | -0.0952063 | 10 | 10 | 2.5861e-05 |
