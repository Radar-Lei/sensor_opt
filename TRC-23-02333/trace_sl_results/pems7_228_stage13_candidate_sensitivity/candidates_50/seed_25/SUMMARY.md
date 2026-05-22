---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-27, 2012-06-22
Test days: 2012-05-02, 2012-05-09
Budgets: [0.2]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape          
                                                              mean       std       mean       std      mean       std
budget layout_type                   method                                                                          
0.2    best_random_by_trace          gls_map              3.519920       NaN   6.112507       NaN  0.083882       NaN
                                     gsp                  3.869316       NaN   6.679440       NaN  0.092788       NaN
                                     historical_tod_mean  4.123039       NaN   7.078209       NaN  0.095589       NaN
                                     neighbor_average     7.042629       NaN  11.015091       NaN  0.178105       NaN
       best_random_by_validation     gls_map              3.345725       NaN   5.800312       NaN  0.079312       NaN
                                     gsp                  3.689595       NaN   6.478907       NaN  0.088912       NaN
                                     historical_tod_mean  3.957354       NaN   6.852487       NaN  0.091285       NaN
                                     neighbor_average     7.410294       NaN  11.529919       NaN  0.176105       NaN
       coverage                      gls_map              3.416141       NaN   5.936227       NaN  0.080959       NaN
                                     gsp                  3.768132       NaN   6.558833       NaN  0.090245       NaN
                                     historical_tod_mean  4.006775       NaN   6.934378       NaN  0.093819       NaN
                                     neighbor_average     7.014621       NaN  10.818484       NaN  0.179913       NaN
       degree                        gls_map              3.829607       NaN   6.524394       NaN  0.092461       NaN
                                     gsp                  3.841701       NaN   6.601869       NaN  0.090955       NaN
                                     historical_tod_mean  4.047049       NaN   6.917114       NaN  0.093250       NaN
                                     neighbor_average     7.597361       NaN  11.785041       NaN  0.191120       NaN
       greedy_a_trace                gls_map              3.336125       NaN   5.719964       NaN  0.078814       NaN
                                     gsp                  3.804803       NaN   6.600650       NaN  0.090442       NaN
                                     historical_tod_mean  4.038315       NaN   6.992463       NaN  0.094062       NaN
                                     neighbor_average     6.905161       NaN  10.655900       NaN  0.182962       NaN
       greedy_d_logdet               gls_map              3.913042       NaN   6.440231       NaN  0.093888       NaN
                                     gsp                  3.906417       NaN   6.679908       NaN  0.093461       NaN
                                     historical_tod_mean  4.105858       NaN   7.033330       NaN  0.095811       NaN
                                     neighbor_average     7.614150       NaN  12.291049       NaN  0.217743       NaN
       multistart_swap_by_validation gls_map              3.217681       NaN   5.528056       NaN  0.075933       NaN
                                     gsp                  3.738986       NaN   6.425069       NaN  0.087663       NaN
                                     historical_tod_mean  3.966168       NaN   6.807570       NaN  0.091127       NaN
                                     neighbor_average     6.807468       NaN  10.562390       NaN  0.175948       NaN
       random                        gls_map              3.440197  0.084784   5.943841  0.157533  0.081611  0.003207
                                     gsp                  3.757593  0.069458   6.523022  0.109781  0.089871  0.002687
                                     historical_tod_mean  3.993734  0.071561   6.890105  0.113502  0.092340  0.002185
                                     neighbor_average     7.236029  0.192672  11.207470  0.309088  0.180154  0.006978
       rcss_selected                 gls_map              3.217681       NaN   5.528056       NaN  0.075933       NaN
                                     gsp                  3.738986       NaN   6.425069       NaN  0.087663       NaN
                                     historical_tod_mean  3.966168       NaN   6.807570       NaN  0.091127       NaN
                                     neighbor_average     6.807468       NaN  10.562390       NaN  0.175948       NaN
       robust_coverage_cvar          gls_map              3.423059       NaN   5.887356       NaN  0.082975       NaN
                                     gsp                  3.797176       NaN   6.625258       NaN  0.092924       NaN
                                     historical_tod_mean  4.064233       NaN   7.031883       NaN  0.095167       NaN
                                     neighbor_average     7.004043       NaN  10.852815       NaN  0.184803       NaN
       scenario_average_a_trace      gls_map              3.508072       NaN   6.034653       NaN  0.082557       NaN
                                     gsp                  3.888385       NaN   6.677262       NaN  0.091717       NaN
                                     historical_tod_mean  4.090243       NaN   7.016650       NaN  0.094717       NaN
                                     neighbor_average     7.283535       NaN  11.229529       NaN  0.188550       NaN
       scenario_cvar_a_trace         gls_map              3.527221       NaN   6.069053       NaN  0.088217       NaN
                                     gsp                  3.839048       NaN   6.628053       NaN  0.094634       NaN
                                     historical_tod_mean  4.061698       NaN   6.992734       NaN  0.095420       NaN
                                     neighbor_average     7.347151       NaN  11.364138       NaN  0.194621       NaN
       swap_from_best_random_trace   gls_map              3.366928       NaN   5.752433       NaN  0.078284       NaN
                                     gsp                  3.817859       NaN   6.525751       NaN  0.088988       NaN
                                     historical_tod_mean  4.022487       NaN   6.909293       NaN  0.092163       NaN
                                     neighbor_average     6.964638       NaN  10.957725       NaN  0.183095       NaN
       swap_from_greedy_a_trace      gls_map              3.334105       NaN   5.772766       NaN  0.079024       NaN
                                     gsp                  3.791231       NaN   6.575399       NaN  0.089550       NaN
                                     historical_tod_mean  4.037070       NaN   6.977200       NaN  0.093336       NaN
                                     neighbor_average     6.952404       NaN  10.808307       NaN  0.185205       NaN
       swap_from_scenario_average    gls_map              3.330990       NaN   5.789079       NaN  0.078716       NaN
                                     gsp                  3.866015       NaN   6.640245       NaN  0.090669       NaN
                                     historical_tod_mean  4.067442       NaN   6.997129       NaN  0.094049       NaN
                                     neighbor_average     7.020744       NaN  10.912791       NaN  0.185909       NaN
       swap_from_scenario_cvar       gls_map              3.353092       NaN   5.665275       NaN  0.076932       NaN
                                     gsp                  3.778631       NaN   6.515956       NaN  0.088080       NaN
                                     historical_tod_mean  4.006747       NaN   6.909506       NaN  0.091864       NaN
                                     neighbor_average     6.939383       NaN  10.848473       NaN  0.179784       NaN
       top_variance                  gls_map              3.208909       NaN   5.455355       NaN  0.068936       NaN
                                     gsp                  3.310899       NaN   5.744711       NaN  0.073048       NaN
                                     historical_tod_mean  3.535287       NaN   6.035016       NaN  0.076835       NaN
                                     neighbor_average     9.188633       NaN  14.474583       NaN  0.176437       NaN
       validation_swap_selected      gls_map              3.227792       NaN   5.530884       NaN  0.076285       NaN
                                     gsp                  3.688818       NaN   6.378926       NaN  0.086764       NaN
                                     historical_tod_mean  3.924795       NaN   6.768177       NaN  0.090142       NaN
                                     neighbor_average     6.770238       NaN  10.449568       NaN  0.174123       NaN
```

## Best method per budget-layout row

```
 budget  layout_type  method      mae     rmse
    0.2 top_variance gls_map 3.208909 5.455355
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace     0.167439      0.190270 67
    gsp   condition_number     0.100566      0.116557 67
    gsp information_logdet    -0.266320     -0.196416 67
gls_map    posterior_trace     0.261811      0.161934 67
gls_map   condition_number     0.544775      0.328518 67
gls_map information_logdet     0.036121     -0.075769 67
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv