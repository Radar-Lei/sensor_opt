---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-08, 2012-05-25
Test days: 2012-06-27, 2012-06-29
Budgets: [0.1]
Random layouts per budget: 1
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae          rmse          mape    
                                                              mean std      mean std      mean std
budget layout_type                   method                                                       
0.1    best_random_by_trace          gls_map              1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     gsp                  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     1.368000 NaN  3.227489 NaN  0.022230 NaN
       best_random_by_validation     gls_map              1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     gsp                  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     1.368000 NaN  3.227489 NaN  0.022230 NaN
       coverage                      gls_map              1.174829 NaN  2.591627 NaN  0.018200 NaN
                                     gsp                  1.174829 NaN  2.591627 NaN  0.018200 NaN
                                     historical_tod_mean  1.174829 NaN  2.591627 NaN  0.018200 NaN
                                     neighbor_average     1.174829 NaN  2.591627 NaN  0.018200 NaN
       degree                        gls_map              1.331939 NaN  3.203316 NaN  0.021684 NaN
                                     gsp                  1.331939 NaN  3.203316 NaN  0.021684 NaN
                                     historical_tod_mean  1.331939 NaN  3.203316 NaN  0.021684 NaN
                                     neighbor_average     1.331939 NaN  3.203316 NaN  0.021684 NaN
       graph_sampling_laplacian      gls_map              1.331537 NaN  3.213820 NaN  0.021726 NaN
                                     gsp                  1.331537 NaN  3.213820 NaN  0.021726 NaN
                                     historical_tod_mean  1.331537 NaN  3.213820 NaN  0.021726 NaN
                                     neighbor_average     1.331537 NaN  3.213820 NaN  0.021726 NaN
       greedy_a_trace                gls_map              1.383585 NaN  3.232667 NaN  0.022453 NaN
                                     gsp                  1.383585 NaN  3.232667 NaN  0.022453 NaN
                                     historical_tod_mean  1.383585 NaN  3.232667 NaN  0.022453 NaN
                                     neighbor_average     1.383585 NaN  3.232667 NaN  0.022453 NaN
       greedy_d_logdet               gls_map              1.228793 NaN  2.638540 NaN  0.018995 NaN
                                     gsp                  1.228793 NaN  2.638540 NaN  0.018995 NaN
                                     historical_tod_mean  1.228793 NaN  2.638540 NaN  0.018995 NaN
                                     neighbor_average     1.228793 NaN  2.638540 NaN  0.018995 NaN
       multistart_swap_by_validation gls_map              1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     gsp                  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     1.389744 NaN  3.232750 NaN  0.022558 NaN
       observability_proxy           gls_map              1.311720 NaN  3.149767 NaN  0.021404 NaN
                                     gsp                  1.311720 NaN  3.149767 NaN  0.021404 NaN
                                     historical_tod_mean  1.311720 NaN  3.149767 NaN  0.021404 NaN
                                     neighbor_average     1.311720 NaN  3.149767 NaN  0.021404 NaN
       qr_pod_modes                  gls_map              1.376293 NaN  3.229365 NaN  0.022337 NaN
                                     gsp                  1.376293 NaN  3.229365 NaN  0.022337 NaN
                                     historical_tod_mean  1.376293 NaN  3.229365 NaN  0.022337 NaN
                                     neighbor_average     1.376293 NaN  3.229365 NaN  0.022337 NaN
       random                        gls_map              1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     gsp                  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     1.368000 NaN  3.227489 NaN  0.022230 NaN
       rcss_selected                 gls_map              1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     gsp                  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     1.369012 NaN  3.221936 NaN  0.022273 NaN
       robust_coverage_cvar          gls_map              1.326000 NaN  3.183553 NaN  0.021637 NaN
                                     gsp                  1.326000 NaN  3.183553 NaN  0.021637 NaN
                                     historical_tod_mean  1.326000 NaN  3.183553 NaN  0.021637 NaN
                                     neighbor_average     1.326000 NaN  3.183553 NaN  0.021637 NaN
       scenario_average_a_trace      gls_map              1.367085 NaN  3.227811 NaN  0.022203 NaN
                                     gsp                  1.367085 NaN  3.227811 NaN  0.022203 NaN
                                     historical_tod_mean  1.367085 NaN  3.227811 NaN  0.022203 NaN
                                     neighbor_average     1.367085 NaN  3.227811 NaN  0.022203 NaN
       scenario_cvar_a_trace         gls_map              1.355500 NaN  3.206813 NaN  0.022080 NaN
                                     gsp                  1.355500 NaN  3.206813 NaN  0.022080 NaN
                                     historical_tod_mean  1.355500 NaN  3.206813 NaN  0.022080 NaN
                                     neighbor_average     1.355500 NaN  3.206813 NaN  0.022080 NaN
       swap_from_best_random_trace   gls_map              1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     gsp                  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     1.389744 NaN  3.232750 NaN  0.022558 NaN
       swap_from_greedy_a_trace      gls_map              1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     gsp                  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     1.369012 NaN  3.221936 NaN  0.022273 NaN
       swap_from_scenario_average    gls_map              1.393695 NaN  3.238405 NaN  0.022601 NaN
                                     gsp                  1.393695 NaN  3.238405 NaN  0.022601 NaN
                                     historical_tod_mean  1.393695 NaN  3.238405 NaN  0.022601 NaN
                                     neighbor_average     1.393695 NaN  3.238405 NaN  0.022601 NaN
       swap_from_scenario_cvar       gls_map              1.378012 NaN  3.230235 NaN  0.022389 NaN
                                     gsp                  1.378012 NaN  3.230235 NaN  0.022389 NaN
                                     historical_tod_mean  1.378012 NaN  3.230235 NaN  0.022389 NaN
                                     neighbor_average     1.378012 NaN  3.230235 NaN  0.022389 NaN
       top_variance                  gls_map              1.232780 NaN  3.150093 NaN  0.020283 NaN
                                     gsp                  1.232780 NaN  3.150093 NaN  0.020283 NaN
                                     historical_tod_mean  1.232780 NaN  3.150093 NaN  0.020283 NaN
                                     neighbor_average     1.232780 NaN  3.150093 NaN  0.020283 NaN
       validation_swap_selected      gls_map              1.373646 NaN  3.226636 NaN  0.022311 NaN
                                     gsp                  1.373646 NaN  3.226636 NaN  0.022311 NaN
                                     historical_tod_mean  1.373646 NaN  3.226636 NaN  0.022311 NaN
                                     neighbor_average     1.373646 NaN  3.226636 NaN  0.022311 NaN
```

## Best method per budget-layout row

```
 budget layout_type              method      mae     rmse
    0.1    coverage historical_tod_mean 1.174829 2.591627
```

## Certificate-error correlations

```
No stable certificate correlations were available.
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv