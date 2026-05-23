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
0.1    best_random_by_trace          gls_map              1.388398 NaN  3.207695 NaN  0.022620 NaN
                                     gsp                  1.407367 NaN  3.234022 NaN  0.022901 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.574175 NaN  3.979163 NaN  0.040342 NaN
       best_random_by_validation     gls_map              1.388398 NaN  3.207695 NaN  0.022620 NaN
                                     gsp                  1.407367 NaN  3.234022 NaN  0.022901 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.574175 NaN  3.979163 NaN  0.040342 NaN
       coverage                      gls_map              2.097036 NaN  3.076243 NaN  0.031669 NaN
                                     gsp                  2.079254 NaN  3.036801 NaN  0.031321 NaN
                                     historical_tod_mean  1.174829 NaN  2.591627 NaN  0.018200 NaN
                                     neighbor_average     2.844585 NaN  3.928804 NaN  0.043042 NaN
       degree                        gls_map              1.459330 NaN  3.250434 NaN  0.023688 NaN
                                     gsp                  1.375209 NaN  3.211728 NaN  0.022426 NaN
                                     historical_tod_mean  1.331939 NaN  3.203316 NaN  0.021684 NaN
                                     neighbor_average     2.699350 NaN  3.998525 NaN  0.042165 NaN
       graph_sampling_laplacian      gls_map              1.368948 NaN  3.215929 NaN  0.022376 NaN
                                     gsp                  1.358803 NaN  3.217520 NaN  0.022185 NaN
                                     historical_tod_mean  1.331537 NaN  3.213820 NaN  0.021726 NaN
                                     neighbor_average     3.205703 NaN  4.630685 NaN  0.050263 NaN
       greedy_a_trace                gls_map              1.462512 NaN  3.280942 NaN  0.023662 NaN
                                     gsp                  1.398001 NaN  3.233838 NaN  0.022656 NaN
                                     historical_tod_mean  1.383585 NaN  3.232667 NaN  0.022453 NaN
                                     neighbor_average     2.428728 NaN  3.870300 NaN  0.038207 NaN
       greedy_d_logdet               gls_map              4.547507 NaN  5.764979 NaN  0.067519 NaN
                                     gsp                  2.146786 NaN  3.090092 NaN  0.032279 NaN
                                     historical_tod_mean  1.228793 NaN  2.638540 NaN  0.018995 NaN
                                     neighbor_average     2.225329 NaN  3.267799 NaN  0.033410 NaN
       multistart_swap_by_validation gls_map              1.413812 NaN  3.232345 NaN  0.022980 NaN
                                     gsp                  1.401813 NaN  3.233619 NaN  0.022773 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     2.407195 NaN  3.810577 NaN  0.037538 NaN
       observability_proxy           gls_map              1.587942 NaN  3.284873 NaN  0.025629 NaN
                                     gsp                  1.338450 NaN  3.155463 NaN  0.021876 NaN
                                     historical_tod_mean  1.311720 NaN  3.149767 NaN  0.021404 NaN
                                     neighbor_average     2.899439 NaN  4.432032 NaN  0.045332 NaN
       qr_pod_modes                  gls_map              1.380100 NaN  3.213363 NaN  0.022483 NaN
                                     gsp                  1.398537 NaN  3.231131 NaN  0.022731 NaN
                                     historical_tod_mean  1.376293 NaN  3.229365 NaN  0.022337 NaN
                                     neighbor_average     2.354451 NaN  3.685357 NaN  0.036704 NaN
       random                        gls_map              1.388398 NaN  3.207695 NaN  0.022620 NaN
                                     gsp                  1.407367 NaN  3.234022 NaN  0.022901 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.574175 NaN  3.979163 NaN  0.040342 NaN
       rcss_selected                 gls_map              1.443455 NaN  3.253028 NaN  0.023494 NaN
                                     gsp                  1.437321 NaN  3.238569 NaN  0.023408 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     2.414309 NaN  3.915198 NaN  0.037829 NaN
       robust_coverage_cvar          gls_map              1.569882 NaN  3.293394 NaN  0.025446 NaN
                                     gsp                  1.488809 NaN  3.228760 NaN  0.024234 NaN
                                     historical_tod_mean  1.326000 NaN  3.183553 NaN  0.021637 NaN
                                     neighbor_average     2.419154 NaN  3.911223 NaN  0.037875 NaN
       scenario_average_a_trace      gls_map              1.359149 NaN  3.201125 NaN  0.022142 NaN
                                     gsp                  1.375314 NaN  3.227749 NaN  0.022357 NaN
                                     historical_tod_mean  1.367085 NaN  3.227811 NaN  0.022203 NaN
                                     neighbor_average     2.169618 NaN  3.716228 NaN  0.034091 NaN
       scenario_cvar_a_trace         gls_map              1.520627 NaN  3.280463 NaN  0.024702 NaN
                                     gsp                  1.553850 NaN  3.271758 NaN  0.025225 NaN
                                     historical_tod_mean  1.355500 NaN  3.206813 NaN  0.022080 NaN
                                     neighbor_average     2.482114 NaN  3.830714 NaN  0.038883 NaN
       swap_from_best_random_trace   gls_map              1.413812 NaN  3.232345 NaN  0.022980 NaN
                                     gsp                  1.401813 NaN  3.233619 NaN  0.022773 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     2.407195 NaN  3.810577 NaN  0.037538 NaN
       swap_from_greedy_a_trace      gls_map              1.443455 NaN  3.253028 NaN  0.023494 NaN
                                     gsp                  1.437321 NaN  3.238569 NaN  0.023408 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     2.414309 NaN  3.915198 NaN  0.037829 NaN
       swap_from_scenario_average    gls_map              1.415006 NaN  3.231387 NaN  0.022997 NaN
                                     gsp                  1.415526 NaN  3.239940 NaN  0.022977 NaN
                                     historical_tod_mean  1.393695 NaN  3.238405 NaN  0.022601 NaN
                                     neighbor_average     2.428293 NaN  3.803596 NaN  0.038110 NaN
       swap_from_scenario_cvar       gls_map              1.409923 NaN  3.229432 NaN  0.022962 NaN
                                     gsp                  1.420684 NaN  3.237625 NaN  0.023104 NaN
                                     historical_tod_mean  1.378012 NaN  3.230235 NaN  0.022389 NaN
                                     neighbor_average     2.509228 NaN  3.896685 NaN  0.039255 NaN
       top_variance                  gls_map              1.415258 NaN  3.154309 NaN  0.023047 NaN
                                     gsp                  1.261257 NaN  3.154865 NaN  0.020759 NaN
                                     historical_tod_mean  1.232780 NaN  3.150093 NaN  0.020283 NaN
                                     neighbor_average     2.681171 NaN  3.933680 NaN  0.042145 NaN
       validation_swap_selected      gls_map              1.373213 NaN  3.207631 NaN  0.022376 NaN
                                     gsp                  1.380272 NaN  3.226579 NaN  0.022432 NaN
                                     historical_tod_mean  1.373646 NaN  3.226636 NaN  0.022311 NaN
                                     neighbor_average     2.388480 NaN  3.756473 NaN  0.037374 NaN
```

## Best method per budget-layout row

```
 budget layout_type              method      mae     rmse
    0.1    coverage historical_tod_mean 1.174829 2.591627
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.067818      0.271186 21
    gsp   condition_number    -0.059074      0.348110 21
    gsp information_logdet     0.087346      0.292047 21
gls_map    posterior_trace     0.617555      0.297262 21
gls_map   condition_number     0.879363      0.204694 21
gls_map information_logdet     0.543128      0.022164 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv