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
0.1    best_random_by_trace          gls_map              1.419649 NaN  3.219129 NaN  0.023125 NaN
                                     gsp                  1.459555 NaN  3.243275 NaN  0.023725 NaN
                                     historical_tod_mean  1.361699 NaN  3.219649 NaN  0.022127 NaN
                                     neighbor_average     2.966019 NaN  4.061763 NaN  0.046409 NaN
       best_random_by_validation     gls_map              1.419649 NaN  3.219129 NaN  0.023125 NaN
                                     gsp                  1.459555 NaN  3.243275 NaN  0.023725 NaN
                                     historical_tod_mean  1.361699 NaN  3.219649 NaN  0.022127 NaN
                                     neighbor_average     2.966019 NaN  4.061763 NaN  0.046409 NaN
       coverage                      gls_map              1.920982 NaN  2.917001 NaN  0.029156 NaN
                                     gsp                  1.827646 NaN  2.871166 NaN  0.027652 NaN
                                     historical_tod_mean  1.174041 NaN  2.586291 NaN  0.018184 NaN
                                     neighbor_average     3.323625 NaN  4.233964 NaN  0.050430 NaN
       degree                        gls_map              1.562463 NaN  3.271866 NaN  0.025088 NaN
                                     gsp                  1.330155 NaN  3.195745 NaN  0.021645 NaN
                                     historical_tod_mean  1.325813 NaN  3.195535 NaN  0.021584 NaN
                                     neighbor_average     2.884790 NaN  3.983460 NaN  0.044536 NaN
       graph_sampling_laplacian      gls_map              1.368100 NaN  3.211410 NaN  0.022354 NaN
                                     gsp                  1.354743 NaN  3.209970 NaN  0.022116 NaN
                                     historical_tod_mean  1.327415 NaN  3.206186 NaN  0.021654 NaN
                                     neighbor_average     3.694822 NaN  4.939428 NaN  0.058004 NaN
       greedy_a_trace                gls_map              1.456724 NaN  3.271880 NaN  0.023568 NaN
                                     gsp                  1.383100 NaN  3.225218 NaN  0.022433 NaN
                                     historical_tod_mean  1.378604 NaN  3.224907 NaN  0.022370 NaN
                                     neighbor_average     2.950647 NaN  4.098632 NaN  0.045897 NaN
       greedy_d_logdet               gls_map              4.363606 NaN  5.584453 NaN  0.064799 NaN
                                     gsp                  2.053860 NaN  3.026433 NaN  0.030921 NaN
                                     historical_tod_mean  1.223604 NaN  2.632151 NaN  0.018914 NaN
                                     neighbor_average     3.149029 NaN  3.951920 NaN  0.046805 NaN
       multistart_swap_by_validation gls_map              1.414537 NaN  3.220708 NaN  0.022997 NaN
                                     gsp                  1.412397 NaN  3.229198 NaN  0.022953 NaN
                                     historical_tod_mean  1.382998 NaN  3.224893 NaN  0.022448 NaN
                                     neighbor_average     3.076699 NaN  4.214693 NaN  0.047856 NaN
       observability_proxy           gls_map              1.605786 NaN  3.300590 NaN  0.025884 NaN
                                     gsp                  1.332911 NaN  3.147793 NaN  0.021783 NaN
                                     historical_tod_mean  1.305473 NaN  3.142114 NaN  0.021302 NaN
                                     neighbor_average     3.231230 NaN  4.563771 NaN  0.050188 NaN
       qr_pod_modes                  gls_map              1.366432 NaN  3.201607 NaN  0.022256 NaN
                                     gsp                  1.389484 NaN  3.222757 NaN  0.022581 NaN
                                     historical_tod_mean  1.370619 NaN  3.221550 NaN  0.022244 NaN
                                     neighbor_average     2.832362 NaN  3.956195 NaN  0.043600 NaN
       random                        gls_map              1.419649 NaN  3.219129 NaN  0.023125 NaN
                                     gsp                  1.459555 NaN  3.243275 NaN  0.023725 NaN
                                     historical_tod_mean  1.361699 NaN  3.219649 NaN  0.022127 NaN
                                     neighbor_average     2.966019 NaN  4.061763 NaN  0.046409 NaN
       rcss_selected                 gls_map              1.449412 NaN  3.245580 NaN  0.023580 NaN
                                     gsp                  1.456799 NaN  3.239314 NaN  0.023710 NaN
                                     historical_tod_mean  1.362367 NaN  3.214106 NaN  0.022165 NaN
                                     neighbor_average     3.325890 NaN  4.555019 NaN  0.052001 NaN
       robust_coverage_cvar          gls_map              1.630966 NaN  3.318113 NaN  0.026315 NaN
                                     gsp                  1.455518 NaN  3.210600 NaN  0.023706 NaN
                                     historical_tod_mean  1.322779 NaN  3.176151 NaN  0.021578 NaN
                                     neighbor_average     3.122168 NaN  4.345755 NaN  0.048140 NaN
       scenario_average_a_trace      gls_map              1.429211 NaN  3.248740 NaN  0.023113 NaN
                                     gsp                  1.401927 NaN  3.230226 NaN  0.022685 NaN
                                     historical_tod_mean  1.375825 NaN  3.227521 NaN  0.022314 NaN
                                     neighbor_average     2.761812 NaN  3.970791 NaN  0.042861 NaN
       scenario_cvar_a_trace         gls_map              1.564387 NaN  3.319644 NaN  0.025355 NaN
                                     gsp                  1.509531 NaN  3.247262 NaN  0.024530 NaN
                                     historical_tod_mean  1.350206 NaN  3.199074 NaN  0.021991 NaN
                                     neighbor_average     3.111003 NaN  4.140758 NaN  0.047852 NaN
       swap_from_best_random_trace   gls_map              1.414537 NaN  3.220708 NaN  0.022997 NaN
                                     gsp                  1.412397 NaN  3.229198 NaN  0.022953 NaN
                                     historical_tod_mean  1.382998 NaN  3.224893 NaN  0.022448 NaN
                                     neighbor_average     3.076699 NaN  4.214693 NaN  0.047856 NaN
       swap_from_greedy_a_trace      gls_map              1.449412 NaN  3.245580 NaN  0.023580 NaN
                                     gsp                  1.456799 NaN  3.239314 NaN  0.023710 NaN
                                     historical_tod_mean  1.362367 NaN  3.214106 NaN  0.022165 NaN
                                     neighbor_average     3.325890 NaN  4.555019 NaN  0.052001 NaN
       swap_from_scenario_average    gls_map              1.402256 NaN  3.218287 NaN  0.022778 NaN
                                     gsp                  1.397497 NaN  3.230808 NaN  0.022669 NaN
                                     historical_tod_mean  1.390716 NaN  3.230993 NaN  0.022547 NaN
                                     neighbor_average     2.912298 NaN  4.087068 NaN  0.045427 NaN
       swap_from_scenario_cvar       gls_map              1.420390 NaN  3.227736 NaN  0.023104 NaN
                                     gsp                  1.428266 NaN  3.233353 NaN  0.023220 NaN
                                     historical_tod_mean  1.373350 NaN  3.222516 NaN  0.022310 NaN
                                     neighbor_average     3.134304 NaN  4.288887 NaN  0.048831 NaN
       top_variance                  gls_map              1.417522 NaN  3.156791 NaN  0.023094 NaN
                                     gsp                  1.275707 NaN  3.152110 NaN  0.020981 NaN
                                     historical_tod_mean  1.231517 NaN  3.143168 NaN  0.020254 NaN
                                     neighbor_average     2.969903 NaN  4.196489 NaN  0.046627 NaN
       validation_swap_selected      gls_map              1.366351 NaN  3.199337 NaN  0.022261 NaN
                                     gsp                  1.377542 NaN  3.219049 NaN  0.022392 NaN
                                     historical_tod_mean  1.366978 NaN  3.218794 NaN  0.022203 NaN
                                     neighbor_average     3.040291 NaN  4.201900 NaN  0.047357 NaN
```

## Best method per budget-layout row

```
 budget layout_type              method      mae     rmse
    0.1    coverage historical_tod_mean 1.174041 2.586291
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.147097     -0.062581 21
    gsp   condition_number     0.247647      0.511082 21
    gsp information_logdet     0.079970      0.031291 21
gls_map    posterior_trace     0.449996      0.217731 21
gls_map   condition_number     0.661460      0.151239 21
gls_map information_logdet     0.503951      0.009126 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv