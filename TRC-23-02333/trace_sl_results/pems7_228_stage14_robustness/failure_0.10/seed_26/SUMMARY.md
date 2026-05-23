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
0.1    best_random_by_trace          gls_map              1.432434 NaN  3.223281 NaN  0.023306 NaN
                                     gsp                  1.458229 NaN  3.236812 NaN  0.023699 NaN
                                     historical_tod_mean  1.354903 NaN  3.211860 NaN  0.022017 NaN
                                     neighbor_average     3.154267 NaN  4.257443 NaN  0.049416 NaN
       best_random_by_validation     gls_map              1.432434 NaN  3.223281 NaN  0.023306 NaN
                                     gsp                  1.458229 NaN  3.236812 NaN  0.023699 NaN
                                     historical_tod_mean  1.354903 NaN  3.211860 NaN  0.022017 NaN
                                     neighbor_average     3.154267 NaN  4.257443 NaN  0.049416 NaN
       coverage                      gls_map              1.997350 NaN  2.954888 NaN  0.030213 NaN
                                     gsp                  1.981644 NaN  2.966637 NaN  0.029877 NaN
                                     historical_tod_mean  1.178998 NaN  2.586233 NaN  0.018243 NaN
                                     neighbor_average     3.289855 NaN  4.174120 NaN  0.049787 NaN
       degree                        gls_map              1.586221 NaN  3.287843 NaN  0.025362 NaN
                                     gsp                  1.411830 NaN  3.210684 NaN  0.022792 NaN
                                     historical_tod_mean  1.345894 NaN  3.201649 NaN  0.021854 NaN
                                     neighbor_average     2.918035 NaN  4.078848 NaN  0.044916 NaN
       graph_sampling_laplacian      gls_map              1.387396 NaN  3.201718 NaN  0.022644 NaN
                                     gsp                  1.361827 NaN  3.205462 NaN  0.022224 NaN
                                     historical_tod_mean  1.325229 NaN  3.199121 NaN  0.021612 NaN
                                     neighbor_average     3.831884 NaN  5.073292 NaN  0.060083 NaN
       greedy_a_trace                gls_map              1.454997 NaN  3.267288 NaN  0.023519 NaN
                                     gsp                  1.385259 NaN  3.218159 NaN  0.022448 NaN
                                     historical_tod_mean  1.372198 NaN  3.217127 NaN  0.022264 NaN
                                     neighbor_average     2.990982 NaN  4.098638 NaN  0.046280 NaN
       greedy_d_logdet               gls_map              5.109949 NaN  6.402025 NaN  0.075693 NaN
                                     gsp                  2.160602 NaN  3.101670 NaN  0.032448 NaN
                                     historical_tod_mean  1.231316 NaN  2.633919 NaN  0.019006 NaN
                                     neighbor_average     3.183414 NaN  4.050543 NaN  0.047224 NaN
       multistart_swap_by_validation gls_map              1.429970 NaN  3.224425 NaN  0.023232 NaN
                                     gsp                  1.408310 NaN  3.221780 NaN  0.022885 NaN
                                     historical_tod_mean  1.376437 NaN  3.217095 NaN  0.022341 NaN
                                     neighbor_average     3.060386 NaN  4.135057 NaN  0.047424 NaN
       observability_proxy           gls_map              1.628263 NaN  3.312971 NaN  0.026190 NaN
                                     gsp                  1.340604 NaN  3.144193 NaN  0.021883 NaN
                                     historical_tod_mean  1.314855 NaN  3.138644 NaN  0.021429 NaN
                                     neighbor_average     3.299195 NaN  4.595793 NaN  0.051085 NaN
       qr_pod_modes                  gls_map              1.368555 NaN  3.195948 NaN  0.022284 NaN
                                     gsp                  1.387513 NaN  3.215674 NaN  0.022548 NaN
                                     historical_tod_mean  1.363623 NaN  3.213736 NaN  0.022130 NaN
                                     neighbor_average     2.927375 NaN  4.040317 NaN  0.044866 NaN
       random                        gls_map              1.432434 NaN  3.223281 NaN  0.023306 NaN
                                     gsp                  1.458229 NaN  3.236812 NaN  0.023699 NaN
                                     historical_tod_mean  1.354903 NaN  3.211860 NaN  0.022017 NaN
                                     neighbor_average     3.154267 NaN  4.257443 NaN  0.049416 NaN
       rcss_selected                 gls_map              1.449980 NaN  3.239334 NaN  0.023578 NaN
                                     gsp                  1.452891 NaN  3.232156 NaN  0.023643 NaN
                                     historical_tod_mean  1.357452 NaN  3.206423 NaN  0.022081 NaN
                                     neighbor_average     3.269404 NaN  4.479082 NaN  0.051093 NaN
       robust_coverage_cvar          gls_map              1.562399 NaN  3.248633 NaN  0.025279 NaN
                                     gsp                  1.434167 NaN  3.197193 NaN  0.023373 NaN
                                     historical_tod_mean  1.321341 NaN  3.170306 NaN  0.021543 NaN
                                     neighbor_average     3.175523 NaN  4.406013 NaN  0.049012 NaN
       scenario_average_a_trace      gls_map              1.350089 NaN  3.188963 NaN  0.021979 NaN
                                     gsp                  1.359110 NaN  3.212917 NaN  0.022068 NaN
                                     historical_tod_mean  1.358768 NaN  3.212950 NaN  0.022062 NaN
                                     neighbor_average     2.784702 NaN  3.996643 NaN  0.043222 NaN
       scenario_cvar_a_trace         gls_map              1.517234 NaN  3.265176 NaN  0.024610 NaN
                                     gsp                  1.473452 NaN  3.227912 NaN  0.023965 NaN
                                     historical_tod_mean  1.355024 NaN  3.194892 NaN  0.022049 NaN
                                     neighbor_average     3.047021 NaN  4.063013 NaN  0.046754 NaN
       swap_from_best_random_trace   gls_map              1.429970 NaN  3.224425 NaN  0.023232 NaN
                                     gsp                  1.408310 NaN  3.221780 NaN  0.022885 NaN
                                     historical_tod_mean  1.376437 NaN  3.217095 NaN  0.022341 NaN
                                     neighbor_average     3.060386 NaN  4.135057 NaN  0.047424 NaN
       swap_from_greedy_a_trace      gls_map              1.449980 NaN  3.239334 NaN  0.023578 NaN
                                     gsp                  1.452891 NaN  3.232156 NaN  0.023643 NaN
                                     historical_tod_mean  1.357452 NaN  3.206423 NaN  0.022081 NaN
                                     neighbor_average     3.269404 NaN  4.479082 NaN  0.051093 NaN
       swap_from_scenario_average    gls_map              1.397522 NaN  3.210258 NaN  0.022700 NaN
                                     gsp                  1.390483 NaN  3.222771 NaN  0.022559 NaN
                                     historical_tod_mean  1.382114 NaN  3.222837 NaN  0.022410 NaN
                                     neighbor_average     3.001610 NaN  4.154580 NaN  0.046823 NaN
       swap_from_scenario_cvar       gls_map              1.415163 NaN  3.219869 NaN  0.023002 NaN
                                     gsp                  1.400017 NaN  3.220128 NaN  0.022750 NaN
                                     historical_tod_mean  1.375435 NaN  3.217229 NaN  0.022329 NaN
                                     neighbor_average     3.154589 NaN  4.307022 NaN  0.048949 NaN
       top_variance                  gls_map              1.403457 NaN  3.139273 NaN  0.022850 NaN
                                     gsp                  1.260686 NaN  3.144705 NaN  0.020710 NaN
                                     historical_tod_mean  1.237440 NaN  3.141829 NaN  0.020314 NaN
                                     neighbor_average     2.931723 NaN  4.148124 NaN  0.045944 NaN
       validation_swap_selected      gls_map              1.361388 NaN  3.191805 NaN  0.022179 NaN
                                     gsp                  1.371327 NaN  3.211230 NaN  0.022287 NaN
                                     historical_tod_mean  1.362041 NaN  3.211100 NaN  0.022119 NaN
                                     neighbor_average     2.947182 NaN  4.087376 NaN  0.045909 NaN
```

## Best method per budget-layout row

```
 budget layout_type              method      mae     rmse
    0.1    coverage historical_tod_mean 1.178998 2.586233
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.102190     -0.147327 21
    gsp   condition_number     0.241414      0.500652 21
    gsp information_logdet     0.069169     -0.080834 21
gls_map    posterior_trace     0.612819      0.297262 21
gls_map   condition_number     0.901200      0.109518 21
gls_map information_logdet     0.484440     -0.221643 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv