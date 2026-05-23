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
0.1    best_random_by_trace          gls_map              1.058377 NaN  1.919050 NaN  0.015437 NaN
                                     gsp                  1.043278 NaN  1.921029 NaN  0.015210 NaN
                                     historical_tod_mean  1.040000 NaN  1.938881 NaN  0.015136 NaN
                                     neighbor_average     2.738413 NaN  3.345348 NaN  0.040398 NaN
       best_random_by_validation     gls_map              1.058377 NaN  1.919050 NaN  0.015437 NaN
                                     gsp                  1.043278 NaN  1.921029 NaN  0.015210 NaN
                                     historical_tod_mean  1.040000 NaN  1.938881 NaN  0.015136 NaN
                                     neighbor_average     2.738413 NaN  3.345348 NaN  0.040398 NaN
       coverage                      gls_map              1.092667 NaN  1.855721 NaN  0.016052 NaN
                                     gsp                  1.226469 NaN  1.895926 NaN  0.018064 NaN
                                     historical_tod_mean  1.004095 NaN  1.903249 NaN  0.014637 NaN
                                     neighbor_average     2.720476 NaN  3.291563 NaN  0.040633 NaN
       degree                        gls_map              1.178678 NaN  1.915978 NaN  0.017318 NaN
                                     gsp                  1.085989 NaN  1.866827 NaN  0.015924 NaN
                                     historical_tod_mean  1.014548 NaN  1.907352 NaN  0.014773 NaN
                                     neighbor_average     2.595873 NaN  3.117873 NaN  0.038153 NaN
       graph_sampling_laplacian      gls_map              1.082939 NaN  1.943953 NaN  0.015829 NaN
                                     gsp                  1.070461 NaN  1.915259 NaN  0.015654 NaN
                                     historical_tod_mean  1.047595 NaN  1.950148 NaN  0.015258 NaN
                                     neighbor_average     2.653333 NaN  3.232981 NaN  0.039840 NaN
       greedy_a_trace                gls_map              1.081105 NaN  1.939619 NaN  0.015789 NaN
                                     gsp                  1.072770 NaN  1.945747 NaN  0.015641 NaN
                                     historical_tod_mean  1.070774 NaN  1.961103 NaN  0.015588 NaN
                                     neighbor_average     2.464127 NaN  3.063109 NaN  0.036644 NaN
       greedy_d_logdet               gls_map              1.435398 NaN  2.041966 NaN  0.021165 NaN
                                     gsp                  1.367480 NaN  1.929275 NaN  0.020198 NaN
                                     historical_tod_mean  0.990905 NaN  1.863341 NaN  0.014449 NaN
                                     neighbor_average     2.504127 NaN  3.015284 NaN  0.036850 NaN
       multistart_swap_by_validation gls_map              1.066438 NaN  1.933343 NaN  0.015576 NaN
                                     gsp                  1.072930 NaN  1.927996 NaN  0.015671 NaN
                                     historical_tod_mean  1.066905 NaN  1.954189 NaN  0.015539 NaN
                                     neighbor_average     2.492857 NaN  3.075002 NaN  0.036795 NaN
       observability_proxy           gls_map              1.527308 NaN  2.161199 NaN  0.022611 NaN
                                     gsp                  1.264613 NaN  1.817344 NaN  0.018696 NaN
                                     historical_tod_mean  0.961857 NaN  1.763662 NaN  0.014046 NaN
                                     neighbor_average     2.843492 NaN  3.594269 NaN  0.042369 NaN
       qr_pod_modes                  gls_map              1.122005 NaN  1.927778 NaN  0.016390 NaN
                                     gsp                  1.057258 NaN  1.944454 NaN  0.015383 NaN
                                     historical_tod_mean  1.045440 NaN  1.937439 NaN  0.015210 NaN
                                     neighbor_average     2.481587 NaN  3.101034 NaN  0.036337 NaN
       random                        gls_map              1.058377 NaN  1.919050 NaN  0.015437 NaN
                                     gsp                  1.043278 NaN  1.921029 NaN  0.015210 NaN
                                     historical_tod_mean  1.040000 NaN  1.938881 NaN  0.015136 NaN
                                     neighbor_average     2.738413 NaN  3.345348 NaN  0.040398 NaN
       rcss_selected                 gls_map              1.223213 NaN  1.885511 NaN  0.018080 NaN
                                     gsp                  1.199056 NaN  1.773737 NaN  0.017751 NaN
                                     historical_tod_mean  0.940595 NaN  1.737681 NaN  0.013784 NaN
                                     neighbor_average     3.346508 NaN  4.061573 NaN  0.050552 NaN
       robust_coverage_cvar          gls_map              1.073329 NaN  1.932401 NaN  0.015691 NaN
                                     gsp                  1.080377 NaN  1.928462 NaN  0.015780 NaN
                                     historical_tod_mean  1.068202 NaN  1.956541 NaN  0.015550 NaN
                                     neighbor_average     2.793333 NaN  3.351501 NaN  0.041598 NaN
       scenario_average_a_trace      gls_map              1.242779 NaN  1.933048 NaN  0.018317 NaN
                                     gsp                  1.103429 NaN  1.856895 NaN  0.016222 NaN
                                     historical_tod_mean  1.009690 NaN  1.893013 NaN  0.014732 NaN
                                     neighbor_average     2.595873 NaN  3.226348 NaN  0.038489 NaN
       scenario_cvar_a_trace         gls_map              1.215452 NaN  1.918499 NaN  0.017955 NaN
                                     gsp                  1.102722 NaN  1.764770 NaN  0.016254 NaN
                                     historical_tod_mean  0.989262 NaN  1.782734 NaN  0.014463 NaN
                                     neighbor_average     2.896825 NaN  3.593276 NaN  0.043183 NaN
       swap_from_best_random_trace   gls_map              1.066438 NaN  1.933343 NaN  0.015576 NaN
                                     gsp                  1.072930 NaN  1.927996 NaN  0.015671 NaN
                                     historical_tod_mean  1.066905 NaN  1.954189 NaN  0.015539 NaN
                                     neighbor_average     2.492857 NaN  3.075002 NaN  0.036795 NaN
       swap_from_greedy_a_trace      gls_map              1.098921 NaN  1.949057 NaN  0.016057 NaN
                                     gsp                  1.071259 NaN  1.931471 NaN  0.015645 NaN
                                     historical_tod_mean  1.066821 NaN  1.955027 NaN  0.015541 NaN
                                     neighbor_average     2.668889 NaN  3.337602 NaN  0.039948 NaN
       swap_from_scenario_average    gls_map              1.087488 NaN  1.945588 NaN  0.015879 NaN
                                     gsp                  1.070762 NaN  1.927418 NaN  0.015639 NaN
                                     historical_tod_mean  1.063964 NaN  1.954470 NaN  0.015494 NaN
                                     neighbor_average     2.738730 NaN  3.425258 NaN  0.040316 NaN
       swap_from_scenario_cvar       gls_map              1.193414 NaN  2.031433 NaN  0.017420 NaN
                                     gsp                  1.057152 NaN  1.932134 NaN  0.015401 NaN
                                     historical_tod_mean  1.057190 NaN  1.945258 NaN  0.015385 NaN
                                     neighbor_average     2.569841 NaN  3.169005 NaN  0.037991 NaN
       top_variance                  gls_map              1.313676 NaN  1.895307 NaN  0.019465 NaN
                                     gsp                  1.062322 NaN  1.736752 NaN  0.015697 NaN
                                     historical_tod_mean  0.941893 NaN  1.745254 NaN  0.013808 NaN
                                     neighbor_average     3.713810 NaN  4.448241 NaN  0.056316 NaN
       validation_swap_selected      gls_map              1.340284 NaN  2.030716 NaN  0.019823 NaN
                                     gsp                  1.226799 NaN  1.787924 NaN  0.018165 NaN
                                     historical_tod_mean  0.934893 NaN  1.730994 NaN  0.013694 NaN
                                     neighbor_average     3.101587 NaN  3.828334 NaN  0.046741 NaN
```

## Best method per budget-layout row

```
 budget              layout_type              method      mae     rmse
    0.1 validation_swap_selected historical_tod_mean 0.934893 1.730994
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.120675     -0.038436 21
    gsp   condition_number     0.260302      0.227362 21
    gsp information_logdet    -0.130481     -0.081433 21
gls_map    posterior_trace     0.322342      0.297720 21
gls_map   condition_number     0.077854     -0.065798 21
gls_map information_logdet     0.130949      0.157003 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv