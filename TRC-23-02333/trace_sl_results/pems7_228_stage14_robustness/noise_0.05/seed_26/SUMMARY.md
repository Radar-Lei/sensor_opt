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
0.1    best_random_by_trace          gls_map              1.451300 NaN  3.249357 NaN  0.023577 NaN
                                     gsp                  1.428635 NaN  3.240130 NaN  0.023244 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.984715 NaN  4.081877 NaN  0.046701 NaN
       best_random_by_validation     gls_map              1.451300 NaN  3.249357 NaN  0.023577 NaN
                                     gsp                  1.428635 NaN  3.240130 NaN  0.023244 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.984715 NaN  4.081877 NaN  0.046701 NaN
       coverage                      gls_map              1.901873 NaN  2.907282 NaN  0.028834 NaN
                                     gsp                  1.892273 NaN  2.913912 NaN  0.028596 NaN
                                     historical_tod_mean  1.174829 NaN  2.591627 NaN  0.018200 NaN
                                     neighbor_average     3.339350 NaN  4.250682 NaN  0.050657 NaN
       degree                        gls_map              1.613953 NaN  3.305658 NaN  0.025859 NaN
                                     gsp                  1.367172 NaN  3.206390 NaN  0.022184 NaN
                                     historical_tod_mean  1.331939 NaN  3.203316 NaN  0.021684 NaN
                                     neighbor_average     2.915285 NaN  4.059776 NaN  0.045151 NaN
       graph_sampling_laplacian      gls_map              1.389128 NaN  3.202886 NaN  0.022647 NaN
                                     gsp                  1.344376 NaN  3.214908 NaN  0.021948 NaN
                                     historical_tod_mean  1.331537 NaN  3.213820 NaN  0.021726 NaN
                                     neighbor_average     3.710081 NaN  4.951303 NaN  0.058247 NaN
       greedy_a_trace                gls_map              1.534063 NaN  3.310779 NaN  0.024656 NaN
                                     gsp                  1.422003 NaN  3.236841 NaN  0.022997 NaN
                                     historical_tod_mean  1.383585 NaN  3.232667 NaN  0.022453 NaN
                                     neighbor_average     2.939187 NaN  4.088971 NaN  0.045724 NaN
       greedy_d_logdet               gls_map              4.459956 NaN  5.686136 NaN  0.066221 NaN
                                     gsp                  2.116233 NaN  3.069237 NaN  0.031834 NaN
                                     historical_tod_mean  1.228793 NaN  2.638540 NaN  0.018995 NaN
                                     neighbor_average     3.144553 NaN  3.929238 NaN  0.046835 NaN
       multistart_swap_by_validation gls_map              1.434240 NaN  3.200129 NaN  0.023240 NaN
                                     gsp                  1.400885 NaN  3.233481 NaN  0.022757 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     3.039350 NaN  4.140605 NaN  0.047171 NaN
       observability_proxy           gls_map              1.630596 NaN  3.324021 NaN  0.026276 NaN
                                     gsp                  1.321950 NaN  3.151057 NaN  0.021594 NaN
                                     historical_tod_mean  1.311720 NaN  3.149767 NaN  0.021404 NaN
                                     neighbor_average     3.233333 NaN  4.564368 NaN  0.050235 NaN
       qr_pod_modes                  gls_map              1.388020 NaN  3.191213 NaN  0.022539 NaN
                                     gsp                  1.382643 NaN  3.229033 NaN  0.022457 NaN
                                     historical_tod_mean  1.376293 NaN  3.229365 NaN  0.022337 NaN
                                     neighbor_average     2.859512 NaN  4.007145 NaN  0.044056 NaN
       random                        gls_map              1.451300 NaN  3.249357 NaN  0.023577 NaN
                                     gsp                  1.428635 NaN  3.240130 NaN  0.023244 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.984715 NaN  4.081877 NaN  0.046701 NaN
       rcss_selected                 gls_map              1.505798 NaN  3.212739 NaN  0.024375 NaN
                                     gsp                  1.429113 NaN  3.235859 NaN  0.023277 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     3.258699 NaN  4.465821 NaN  0.050888 NaN
       robust_coverage_cvar          gls_map              1.522148 NaN  3.249311 NaN  0.024698 NaN
                                     gsp                  1.410571 NaN  3.201835 NaN  0.023024 NaN
                                     historical_tod_mean  1.326000 NaN  3.183553 NaN  0.021637 NaN
                                     neighbor_average     3.111382 NaN  4.345831 NaN  0.048051 NaN
       scenario_average_a_trace      gls_map              1.406526 NaN  3.216970 NaN  0.022772 NaN
                                     gsp                  1.402030 NaN  3.231058 NaN  0.022700 NaN
                                     historical_tod_mean  1.367085 NaN  3.227811 NaN  0.022203 NaN
                                     neighbor_average     2.758211 NaN  3.969388 NaN  0.042847 NaN
       scenario_cvar_a_trace         gls_map              1.546310 NaN  3.274546 NaN  0.025077 NaN
                                     gsp                  1.466133 NaN  3.236823 NaN  0.023872 NaN
                                     historical_tod_mean  1.355500 NaN  3.206813 NaN  0.022080 NaN
                                     neighbor_average     3.083740 NaN  4.128076 NaN  0.047547 NaN
       swap_from_best_random_trace   gls_map              1.434240 NaN  3.200129 NaN  0.023240 NaN
                                     gsp                  1.400885 NaN  3.233481 NaN  0.022757 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     3.039350 NaN  4.140605 NaN  0.047171 NaN
       swap_from_greedy_a_trace      gls_map              1.505798 NaN  3.212739 NaN  0.024375 NaN
                                     gsp                  1.429113 NaN  3.235859 NaN  0.023277 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     3.258699 NaN  4.465821 NaN  0.050888 NaN
       swap_from_scenario_average    gls_map              1.480542 NaN  3.199373 NaN  0.023901 NaN
                                     gsp                  1.398815 NaN  3.238687 NaN  0.022673 NaN
                                     historical_tod_mean  1.393695 NaN  3.238405 NaN  0.022601 NaN
                                     neighbor_average     2.942602 NaN  4.081022 NaN  0.045977 NaN
       swap_from_scenario_cvar       gls_map              1.452741 NaN  3.198580 NaN  0.023536 NaN
                                     gsp                  1.405077 NaN  3.233657 NaN  0.022849 NaN
                                     historical_tod_mean  1.378012 NaN  3.230235 NaN  0.022389 NaN
                                     neighbor_average     3.114309 NaN  4.268647 NaN  0.048584 NaN
       top_variance                  gls_map              1.463561 NaN  3.162870 NaN  0.023766 NaN
                                     gsp                  1.249615 NaN  3.152503 NaN  0.020569 NaN
                                     historical_tod_mean  1.232780 NaN  3.150093 NaN  0.020283 NaN
                                     neighbor_average     3.022114 NaN  4.207041 NaN  0.047390 NaN
       validation_swap_selected      gls_map              1.476109 NaN  3.191532 NaN  0.023837 NaN
                                     gsp                  1.376536 NaN  3.226752 NaN  0.022352 NaN
                                     historical_tod_mean  1.373646 NaN  3.226636 NaN  0.022311 NaN
                                     neighbor_average     3.009106 NaN  4.140955 NaN  0.046766 NaN
```

## Best method per budget-layout row

```
 budget layout_type              method      mae     rmse
    0.1    coverage historical_tod_mean 1.174829 2.591627
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.154391     -0.108214 21
    gsp   condition_number     0.244764      0.405476 21
    gsp information_logdet     0.069795      0.058670 21
gls_map    posterior_trace     0.507124      0.272490 21
gls_map   condition_number     0.842480      0.126467 21
gls_map information_logdet     0.500098     -0.168188 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv