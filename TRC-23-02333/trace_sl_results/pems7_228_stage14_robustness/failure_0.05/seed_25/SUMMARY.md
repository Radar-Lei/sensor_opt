---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-27, 2012-06-22
Test days: 2012-05-02, 2012-05-09
Budgets: [0.1]
Random layouts per budget: 1
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae          rmse          mape    
                                                              mean std      mean std      mean std
budget layout_type                   method                                                       
0.1    best_random_by_trace          gls_map              1.140287 NaN  1.913607 NaN  0.016707 NaN
                                     gsp                  1.069907 NaN  1.903547 NaN  0.015644 NaN
                                     historical_tod_mean  1.041966 NaN  1.944854 NaN  0.015160 NaN
                                     neighbor_average     2.774595 NaN  3.384428 NaN  0.040861 NaN
       best_random_by_validation     gls_map              1.140287 NaN  1.913607 NaN  0.016707 NaN
                                     gsp                  1.069907 NaN  1.903547 NaN  0.015644 NaN
                                     historical_tod_mean  1.041966 NaN  1.944854 NaN  0.015160 NaN
                                     neighbor_average     2.774595 NaN  3.384428 NaN  0.040861 NaN
       coverage                      gls_map              1.109377 NaN  1.856170 NaN  0.016328 NaN
                                     gsp                  1.260114 NaN  1.912146 NaN  0.018581 NaN
                                     historical_tod_mean  1.001371 NaN  1.903635 NaN  0.014599 NaN
                                     neighbor_average     2.776052 NaN  3.347605 NaN  0.041492 NaN
       degree                        gls_map              1.205489 NaN  1.938580 NaN  0.017713 NaN
                                     gsp                  1.123248 NaN  1.883080 NaN  0.016487 NaN
                                     historical_tod_mean  1.016784 NaN  1.919496 NaN  0.014806 NaN
                                     neighbor_average     2.674434 NaN  3.213193 NaN  0.039500 NaN
       graph_sampling_laplacian      gls_map              1.078610 NaN  1.936572 NaN  0.015743 NaN
                                     gsp                  1.045400 NaN  1.922905 NaN  0.015232 NaN
                                     historical_tod_mean  1.042172 NaN  1.941122 NaN  0.015161 NaN
                                     neighbor_average     2.653560 NaN  3.225401 NaN  0.039829 NaN
       greedy_a_trace                gls_map              1.097693 NaN  1.954146 NaN  0.016032 NaN
                                     gsp                  1.093807 NaN  1.957374 NaN  0.015960 NaN
                                     historical_tod_mean  1.086044 NaN  1.979601 NaN  0.015809 NaN
                                     neighbor_average     2.578964 NaN  3.214757 NaN  0.038411 NaN
       greedy_d_logdet               gls_map              1.254113 NaN  1.927535 NaN  0.018475 NaN
                                     gsp                  1.217324 NaN  1.861960 NaN  0.017932 NaN
                                     historical_tod_mean  0.995146 NaN  1.873849 NaN  0.014500 NaN
                                     neighbor_average     2.527994 NaN  3.089037 NaN  0.037097 NaN
       multistart_swap_by_validation gls_map              1.093141 NaN  1.935790 NaN  0.015985 NaN
                                     gsp                  1.093641 NaN  1.939699 NaN  0.015988 NaN
                                     historical_tod_mean  1.079600 NaN  1.971506 NaN  0.015725 NaN
                                     neighbor_average     2.562298 NaN  3.226894 NaN  0.037861 NaN
       observability_proxy           gls_map              1.484446 NaN  2.124355 NaN  0.021981 NaN
                                     gsp                  1.262756 NaN  1.824736 NaN  0.018669 NaN
                                     historical_tod_mean  0.969442 NaN  1.775590 NaN  0.014156 NaN
                                     neighbor_average     2.904854 NaN  3.658905 NaN  0.043322 NaN
       qr_pod_modes                  gls_map              1.096381 NaN  1.890418 NaN  0.016029 NaN
                                     gsp                  1.057969 NaN  1.925479 NaN  0.015433 NaN
                                     historical_tod_mean  1.051966 NaN  1.950263 NaN  0.015304 NaN
                                     neighbor_average     2.570550 NaN  3.211744 NaN  0.037672 NaN
       random                        gls_map              1.140287 NaN  1.913607 NaN  0.016707 NaN
                                     gsp                  1.069907 NaN  1.903547 NaN  0.015644 NaN
                                     historical_tod_mean  1.041966 NaN  1.944854 NaN  0.015160 NaN
                                     neighbor_average     2.774595 NaN  3.384428 NaN  0.040861 NaN
       rcss_selected                 gls_map              1.234228 NaN  1.901658 NaN  0.018251 NaN
                                     gsp                  1.199607 NaN  1.781513 NaN  0.017761 NaN
                                     historical_tod_mean  0.939660 NaN  1.741885 NaN  0.013770 NaN
                                     neighbor_average     3.120550 NaN  3.809013 NaN  0.047079 NaN
       robust_coverage_cvar          gls_map              1.082217 NaN  1.961757 NaN  0.015811 NaN
                                     gsp                  1.086372 NaN  1.958977 NaN  0.015838 NaN
                                     historical_tod_mean  1.083483 NaN  1.974800 NaN  0.015770 NaN
                                     neighbor_average     2.832201 NaN  3.342011 NaN  0.041987 NaN
       scenario_average_a_trace      gls_map              1.283945 NaN  1.957905 NaN  0.018957 NaN
                                     gsp                  1.186624 NaN  1.874780 NaN  0.017485 NaN
                                     historical_tod_mean  0.996007 NaN  1.887570 NaN  0.014532 NaN
                                     neighbor_average     2.595146 NaN  3.233692 NaN  0.038465 NaN
       scenario_cvar_a_trace         gls_map              1.193430 NaN  1.889561 NaN  0.017660 NaN
                                     gsp                  1.132105 NaN  1.773289 NaN  0.016710 NaN
                                     historical_tod_mean  0.984587 NaN  1.780360 NaN  0.014399 NaN
                                     neighbor_average     2.762298 NaN  3.406570 NaN  0.041353 NaN
       swap_from_best_random_trace   gls_map              1.093141 NaN  1.935790 NaN  0.015985 NaN
                                     gsp                  1.093641 NaN  1.939699 NaN  0.015988 NaN
                                     historical_tod_mean  1.079600 NaN  1.971506 NaN  0.015725 NaN
                                     neighbor_average     2.562298 NaN  3.226894 NaN  0.037861 NaN
       swap_from_greedy_a_trace      gls_map              1.100947 NaN  1.955870 NaN  0.016092 NaN
                                     gsp                  1.092917 NaN  1.944127 NaN  0.015972 NaN
                                     historical_tod_mean  1.082002 NaN  1.973463 NaN  0.015760 NaN
                                     neighbor_average     2.806634 NaN  3.515706 NaN  0.041933 NaN
       swap_from_scenario_average    gls_map              1.100294 NaN  1.962893 NaN  0.016063 NaN
                                     gsp                  1.086314 NaN  1.945365 NaN  0.015865 NaN
                                     historical_tod_mean  1.081274 NaN  1.973053 NaN  0.015745 NaN
                                     neighbor_average     2.532039 NaN  3.202891 NaN  0.037221 NaN
       swap_from_scenario_cvar       gls_map              1.196289 NaN  2.038059 NaN  0.017462 NaN
                                     gsp                  1.069901 NaN  1.946777 NaN  0.015592 NaN
                                     historical_tod_mean  1.069939 NaN  1.963258 NaN  0.015569 NaN
                                     neighbor_average     2.644660 NaN  3.326331 NaN  0.039253 NaN
       top_variance                  gls_map              1.168138 NaN  1.759648 NaN  0.017289 NaN
                                     gsp                  1.024863 NaN  1.732083 NaN  0.015125 NaN
                                     historical_tod_mean  0.943143 NaN  1.754266 NaN  0.013825 NaN
                                     neighbor_average     3.386246 NaN  4.078761 NaN  0.051355 NaN
       validation_swap_selected      gls_map              1.317570 NaN  2.007171 NaN  0.019486 NaN
                                     gsp                  1.229112 NaN  1.796889 NaN  0.018198 NaN
                                     historical_tod_mean  0.940036 NaN  1.743564 NaN  0.013773 NaN
                                     neighbor_average     3.146602 NaN  3.843785 NaN  0.047368 NaN
```

## Best method per budget-layout row

```
 budget   layout_type              method     mae     rmse
    0.1 rcss_selected historical_tod_mean 0.93966 1.741885
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.291759     -0.231270 21
    gsp   condition_number     0.254355      0.179153 21
    gsp information_logdet    -0.337218     -0.214332 21
gls_map    posterior_trace     0.289478      0.382410 21
gls_map   condition_number     0.082105      0.271661 21
gls_map information_logdet    -0.040571     -0.050163 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv