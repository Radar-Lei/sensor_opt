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
0.1    best_random_by_trace          gls_map              1.174402 NaN  1.925281 NaN  0.017221 NaN
                                     gsp                  1.070704 NaN  1.898305 NaN  0.015660 NaN
                                     historical_tod_mean  1.037500 NaN  1.940179 NaN  0.015095 NaN
                                     neighbor_average     2.757005 NaN  3.372062 NaN  0.040598 NaN
       best_random_by_validation     gls_map              1.174402 NaN  1.925281 NaN  0.017221 NaN
                                     gsp                  1.070704 NaN  1.898305 NaN  0.015660 NaN
                                     historical_tod_mean  1.037500 NaN  1.940179 NaN  0.015095 NaN
                                     neighbor_average     2.757005 NaN  3.372062 NaN  0.040598 NaN
       coverage                      gls_map              1.192176 NaN  1.916708 NaN  0.017549 NaN
                                     gsp                  1.224778 NaN  1.897436 NaN  0.018041 NaN
                                     historical_tod_mean  1.004396 NaN  1.904081 NaN  0.014643 NaN
                                     neighbor_average     2.765862 NaN  3.343092 NaN  0.041271 NaN
       degree                        gls_map              1.235653 NaN  1.947849 NaN  0.018167 NaN
                                     gsp                  1.123149 NaN  1.880035 NaN  0.016481 NaN
                                     historical_tod_mean  1.018454 NaN  1.916388 NaN  0.014826 NaN
                                     neighbor_average     2.490338 NaN  2.967461 NaN  0.036630 NaN
       graph_sampling_laplacian      gls_map              1.074131 NaN  1.944433 NaN  0.015690 NaN
                                     gsp                  1.079753 NaN  1.928348 NaN  0.015792 NaN
                                     historical_tod_mean  1.057838 NaN  1.962886 NaN  0.015411 NaN
                                     neighbor_average     2.761675 NaN  3.399986 NaN  0.041718 NaN
       greedy_a_trace                gls_map              1.091207 NaN  1.941596 NaN  0.015942 NaN
                                     gsp                  1.089687 NaN  1.949278 NaN  0.015905 NaN
                                     historical_tod_mean  1.080217 NaN  1.974443 NaN  0.015723 NaN
                                     neighbor_average     2.518035 NaN  3.164489 NaN  0.037418 NaN
       greedy_d_logdet               gls_map              1.254404 NaN  1.939032 NaN  0.018479 NaN
                                     gsp                  1.271517 NaN  1.882152 NaN  0.018748 NaN
                                     historical_tod_mean  0.985580 NaN  1.867392 NaN  0.014359 NaN
                                     neighbor_average     2.636554 NaN  3.207010 NaN  0.038628 NaN
       multistart_swap_by_validation gls_map              1.092647 NaN  1.930025 NaN  0.015982 NaN
                                     gsp                  1.089435 NaN  1.935033 NaN  0.015928 NaN
                                     historical_tod_mean  1.074493 NaN  1.966750 NaN  0.015651 NaN
                                     neighbor_average     2.609984 NaN  3.281999 NaN  0.038682 NaN
       observability_proxy           gls_map              1.465875 NaN  2.115225 NaN  0.021702 NaN
                                     gsp                  1.271589 NaN  1.827555 NaN  0.018801 NaN
                                     historical_tod_mean  0.964336 NaN  1.771088 NaN  0.014081 NaN
                                     neighbor_average     2.852657 NaN  3.576814 NaN  0.042508 NaN
       qr_pod_modes                  gls_map              1.149739 NaN  1.937750 NaN  0.016803 NaN
                                     gsp                  1.052953 NaN  1.935644 NaN  0.015337 NaN
                                     historical_tod_mean  1.052114 NaN  1.949284 NaN  0.015304 NaN
                                     neighbor_average     2.654428 NaN  3.294842 NaN  0.038809 NaN
       random                        gls_map              1.174402 NaN  1.925281 NaN  0.017221 NaN
                                     gsp                  1.070704 NaN  1.898305 NaN  0.015660 NaN
                                     historical_tod_mean  1.037500 NaN  1.940179 NaN  0.015095 NaN
                                     neighbor_average     2.757005 NaN  3.372062 NaN  0.040598 NaN
       rcss_selected                 gls_map              1.246406 NaN  1.912513 NaN  0.018418 NaN
                                     gsp                  1.179229 NaN  1.765333 NaN  0.017442 NaN
                                     historical_tod_mean  0.929372 NaN  1.733782 NaN  0.013610 NaN
                                     neighbor_average     3.025443 NaN  3.703301 NaN  0.045519 NaN
       robust_coverage_cvar          gls_map              1.080272 NaN  1.951769 NaN  0.015789 NaN
                                     gsp                  1.081704 NaN  1.947853 NaN  0.015781 NaN
                                     historical_tod_mean  1.074879 NaN  1.968734 NaN  0.015644 NaN
                                     neighbor_average     2.742834 NaN  3.267220 NaN  0.040740 NaN
       scenario_average_a_trace      gls_map              1.198658 NaN  1.896744 NaN  0.017671 NaN
                                     gsp                  1.156268 NaN  1.865274 NaN  0.017021 NaN
                                     historical_tod_mean  1.004517 NaN  1.890916 NaN  0.014653 NaN
                                     neighbor_average     2.630113 NaN  3.266861 NaN  0.038959 NaN
       scenario_cvar_a_trace         gls_map              1.331587 NaN  2.008254 NaN  0.019780 NaN
                                     gsp                  1.289508 NaN  1.822678 NaN  0.019120 NaN
                                     historical_tod_mean  0.959517 NaN  1.734144 NaN  0.014062 NaN
                                     neighbor_average     2.981320 NaN  3.742646 NaN  0.044561 NaN
       swap_from_best_random_trace   gls_map              1.092647 NaN  1.930025 NaN  0.015982 NaN
                                     gsp                  1.089435 NaN  1.935033 NaN  0.015928 NaN
                                     historical_tod_mean  1.074493 NaN  1.966750 NaN  0.015651 NaN
                                     neighbor_average     2.609984 NaN  3.281999 NaN  0.038682 NaN
       swap_from_greedy_a_trace      gls_map              1.083965 NaN  1.942604 NaN  0.015848 NaN
                                     gsp                  1.085917 NaN  1.935209 NaN  0.015877 NaN
                                     historical_tod_mean  1.071775 NaN  1.966359 NaN  0.015612 NaN
                                     neighbor_average     2.793720 NaN  3.487968 NaN  0.041724 NaN
       swap_from_scenario_average    gls_map              1.074334 NaN  1.945810 NaN  0.015686 NaN
                                     gsp                  1.081480 NaN  1.939045 NaN  0.015795 NaN
                                     historical_tod_mean  1.074432 NaN  1.966715 NaN  0.015645 NaN
                                     neighbor_average     2.590016 NaN  3.236853 NaN  0.038018 NaN
       swap_from_scenario_cvar       gls_map              1.204895 NaN  2.037260 NaN  0.017589 NaN
                                     gsp                  1.066254 NaN  1.944714 NaN  0.015535 NaN
                                     historical_tod_mean  1.066836 NaN  1.958735 NaN  0.015525 NaN
                                     neighbor_average     2.636554 NaN  3.310261 NaN  0.039152 NaN
       top_variance                  gls_map              1.147603 NaN  1.743995 NaN  0.016981 NaN
                                     gsp                  1.018924 NaN  1.727357 NaN  0.015035 NaN
                                     historical_tod_mean  0.941087 NaN  1.750268 NaN  0.013793 NaN
                                     neighbor_average     3.441868 NaN  4.147983 NaN  0.052207 NaN
       validation_swap_selected      gls_map              1.259143 NaN  1.928180 NaN  0.018618 NaN
                                     gsp                  1.206596 NaN  1.781721 NaN  0.017861 NaN
                                     historical_tod_mean  0.941558 NaN  1.741079 NaN  0.013789 NaN
                                     neighbor_average     3.213043 NaN  3.924325 NaN  0.048349 NaN
```

## Best method per budget-layout row

```
 budget   layout_type              method      mae     rmse
    0.1 rcss_selected historical_tod_mean 0.929372 1.733782
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.207102     -0.220847 21
    gsp   condition_number     0.249304      0.155700 21
    gsp information_logdet    -0.254033     -0.274267 21
gls_map    posterior_trace     0.361893      0.343322 21
gls_map   condition_number     0.179646      0.203909 21
gls_map information_logdet    -0.015912     -0.013681 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv