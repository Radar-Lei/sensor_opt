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
0.1    best_random_by_trace          gls_map              1.421120 NaN  3.202628 NaN  0.023118 NaN
                                     gsp                  1.453493 NaN  3.217384 NaN  0.023605 NaN
                                     historical_tod_mean  1.341214 NaN  3.189147 NaN  0.021786 NaN
                                     neighbor_average     3.109365 NaN  4.253946 NaN  0.048832 NaN
       best_random_by_validation     gls_map              1.421120 NaN  3.202628 NaN  0.023118 NaN
                                     gsp                  1.453493 NaN  3.217384 NaN  0.023605 NaN
                                     historical_tod_mean  1.341214 NaN  3.189147 NaN  0.021786 NaN
                                     neighbor_average     3.109365 NaN  4.253946 NaN  0.048832 NaN
       coverage                      gls_map              2.099731 NaN  3.052216 NaN  0.031600 NaN
                                     gsp                  2.147664 NaN  3.078480 NaN  0.032269 NaN
                                     historical_tod_mean  1.177512 NaN  2.581081 NaN  0.018198 NaN
                                     neighbor_average     3.242857 NaN  4.159276 NaN  0.048867 NaN
       degree                        gls_map              1.587376 NaN  3.269339 NaN  0.025394 NaN
                                     gsp                  1.346364 NaN  3.170585 NaN  0.021827 NaN
                                     historical_tod_mean  1.318619 NaN  3.168275 NaN  0.021434 NaN
                                     neighbor_average     2.902540 NaN  4.009581 NaN  0.044623 NaN
       graph_sampling_laplacian      gls_map              1.363065 NaN  3.200718 NaN  0.022191 NaN
                                     gsp                  1.369200 NaN  3.196032 NaN  0.022269 NaN
                                     historical_tod_mean  1.344262 NaN  3.193282 NaN  0.021835 NaN
                                     neighbor_average     3.365238 NaN  4.602426 NaN  0.052875 NaN
       greedy_a_trace                gls_map              1.459936 NaN  3.254814 NaN  0.023546 NaN
                                     gsp                  1.380649 NaN  3.196930 NaN  0.022344 NaN
                                     historical_tod_mean  1.356381 NaN  3.194626 NaN  0.022001 NaN
                                     neighbor_average     2.883016 NaN  3.981475 NaN  0.044651 NaN
       greedy_d_logdet               gls_map              5.617547 NaN  6.969729 NaN  0.083111 NaN
                                     gsp                  2.412477 NaN  3.278205 NaN  0.036103 NaN
                                     historical_tod_mean  1.231333 NaN  2.622770 NaN  0.018987 NaN
                                     neighbor_average     3.123968 NaN  3.964212 NaN  0.046311 NaN
       multistart_swap_by_validation gls_map              1.380761 NaN  3.180676 NaN  0.022442 NaN
                                     gsp                  1.407425 NaN  3.205132 NaN  0.022834 NaN
                                     historical_tod_mean  1.375750 NaN  3.201261 NaN  0.022287 NaN
                                     neighbor_average     2.971587 NaN  4.142438 NaN  0.046001 NaN
       observability_proxy           gls_map              1.629349 NaN  3.298384 NaN  0.026161 NaN
                                     gsp                  1.302321 NaN  3.115333 NaN  0.021243 NaN
                                     historical_tod_mean  1.295417 NaN  3.114763 NaN  0.021109 NaN
                                     neighbor_average     3.056349 NaN  4.350213 NaN  0.047474 NaN
       qr_pod_modes                  gls_map              1.404996 NaN  3.185977 NaN  0.022845 NaN
                                     gsp                  1.394816 NaN  3.198476 NaN  0.022659 NaN
                                     historical_tod_mean  1.351905 NaN  3.191624 NaN  0.021930 NaN
                                     neighbor_average     2.846984 NaN  3.902716 NaN  0.043733 NaN
       random                        gls_map              1.421120 NaN  3.202628 NaN  0.023118 NaN
                                     gsp                  1.453493 NaN  3.217384 NaN  0.023605 NaN
                                     historical_tod_mean  1.341214 NaN  3.189147 NaN  0.021786 NaN
                                     neighbor_average     3.109365 NaN  4.253946 NaN  0.048832 NaN
       rcss_selected                 gls_map              1.495143 NaN  3.251964 NaN  0.024246 NaN
                                     gsp                  1.457247 NaN  3.216403 NaN  0.023684 NaN
                                     historical_tod_mean  1.341417 NaN  3.183687 NaN  0.021813 NaN
                                     neighbor_average     3.047778 NaN  4.188107 NaN  0.047413 NaN
       robust_coverage_cvar          gls_map              1.619375 NaN  3.274037 NaN  0.026132 NaN
                                     gsp                  1.444690 NaN  3.183065 NaN  0.023513 NaN
                                     historical_tod_mean  1.302226 NaN  3.146354 NaN  0.021235 NaN
                                     neighbor_average     3.338889 NaN  4.497815 NaN  0.051457 NaN
       scenario_average_a_trace      gls_map              1.359273 NaN  3.158529 NaN  0.022092 NaN
                                     gsp                  1.343129 NaN  3.190043 NaN  0.021807 NaN
                                     historical_tod_mean  1.342274 NaN  3.190144 NaN  0.021791 NaN
                                     neighbor_average     2.731111 NaN  3.887682 NaN  0.042467 NaN
       scenario_cvar_a_trace         gls_map              1.507337 NaN  3.237399 NaN  0.024450 NaN
                                     gsp                  1.475710 NaN  3.210687 NaN  0.023977 NaN
                                     historical_tod_mean  1.346381 NaN  3.174942 NaN  0.021895 NaN
                                     neighbor_average     3.010635 NaN  4.080439 NaN  0.046670 NaN
       swap_from_best_random_trace   gls_map              1.380761 NaN  3.180676 NaN  0.022442 NaN
                                     gsp                  1.407425 NaN  3.205132 NaN  0.022834 NaN
                                     historical_tod_mean  1.375750 NaN  3.201261 NaN  0.022287 NaN
                                     neighbor_average     2.971587 NaN  4.142438 NaN  0.046001 NaN
       swap_from_greedy_a_trace      gls_map              1.495143 NaN  3.251964 NaN  0.024246 NaN
                                     gsp                  1.457247 NaN  3.216403 NaN  0.023684 NaN
                                     historical_tod_mean  1.341417 NaN  3.183687 NaN  0.021813 NaN
                                     neighbor_average     3.047778 NaN  4.188107 NaN  0.047413 NaN
       swap_from_scenario_average    gls_map              1.380589 NaN  3.187546 NaN  0.022425 NaN
                                     gsp                  1.372563 NaN  3.199725 NaN  0.022267 NaN
                                     historical_tod_mean  1.363393 NaN  3.199731 NaN  0.022104 NaN
                                     neighbor_average     2.859524 NaN  4.057461 NaN  0.044390 NaN
       swap_from_scenario_cvar       gls_map              1.417361 NaN  3.204666 NaN  0.023016 NaN
                                     gsp                  1.383411 NaN  3.197529 NaN  0.022480 NaN
                                     historical_tod_mean  1.356190 NaN  3.194154 NaN  0.022015 NaN
                                     neighbor_average     3.156508 NaN  4.308581 NaN  0.049138 NaN
       top_variance                  gls_map              1.407695 NaN  3.126990 NaN  0.022887 NaN
                                     gsp                  1.258003 NaN  3.124315 NaN  0.020639 NaN
                                     historical_tod_mean  1.231048 NaN  3.120749 NaN  0.020183 NaN
                                     neighbor_average     2.852698 NaN  4.051463 NaN  0.044891 NaN
       validation_swap_selected      gls_map              1.374776 NaN  3.184608 NaN  0.022381 NaN
                                     gsp                  1.357519 NaN  3.188775 NaN  0.022056 NaN
                                     historical_tod_mean  1.345940 NaN  3.188330 NaN  0.021850 NaN
                                     neighbor_average     2.798413 NaN  3.845412 NaN  0.043252 NaN
```

## Best method per budget-layout row

```
 budget layout_type              method      mae     rmse
    0.1    coverage historical_tod_mean 1.177512 2.581081
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace     0.017969      0.152542 21
    gsp   condition_number     0.203685      0.189048 21
    gsp information_logdet     0.153680      0.147327 21
gls_map    posterior_trace     0.722975      0.320730 21
gls_map   condition_number     0.885672      0.195567 21
gls_map information_logdet     0.496024     -0.127771 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv