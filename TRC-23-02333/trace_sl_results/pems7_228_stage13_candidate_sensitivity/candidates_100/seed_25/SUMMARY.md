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
0.2    best_random_by_trace          gls_map              3.454068       NaN   5.834514       NaN  0.078312       NaN
                                     gsp                  3.829877       NaN   6.474300       NaN  0.086816       NaN
                                     historical_tod_mean  3.940524       NaN   6.758675       NaN  0.088883       NaN
                                     neighbor_average     7.476519       NaN  11.668661       NaN  0.182420       NaN
       best_random_by_validation     gls_map              3.316469       NaN   5.721891       NaN  0.074629       NaN
                                     gsp                  3.700222       NaN   6.410803       NaN  0.085254       NaN
                                     historical_tod_mean  3.931260       NaN   6.795977       NaN  0.088782       NaN
                                     neighbor_average     7.402874       NaN  11.313245       NaN  0.168073       NaN
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
       multistart_swap_by_validation gls_map              3.316486       NaN   5.767860       NaN  0.076582       NaN
                                     gsp                  3.789250       NaN   6.546869       NaN  0.088587       NaN
                                     historical_tod_mean  4.023235       NaN   6.943084       NaN  0.092047       NaN
                                     neighbor_average     7.024274       NaN  11.113809       NaN  0.182559       NaN
       random                        gls_map              3.444332  0.076274   5.951553  0.137472  0.081926  0.003003
                                     gsp                  3.751838  0.068957   6.520380  0.102069  0.089978  0.002557
                                     historical_tod_mean  3.993523  0.068450   6.885226  0.110605  0.092454  0.002124
                                     neighbor_average     7.270894  0.189573  11.320136  0.302125  0.181252  0.006544
       rcss_selected                 gls_map              3.175395       NaN   5.462943       NaN  0.075540       NaN
                                     gsp                  3.599508       NaN   6.286936       NaN  0.087859       NaN
                                     historical_tod_mean  3.886418       NaN   6.665377       NaN  0.089998       NaN
                                     neighbor_average     6.856260       NaN  10.514242       NaN  0.163545       NaN
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
       swap_from_best_random_trace   gls_map              3.264642       NaN   5.602342       NaN  0.078326       NaN
                                     gsp                  3.777089       NaN   6.455248       NaN  0.088790       NaN
                                     historical_tod_mean  3.962610       NaN   6.806082       NaN  0.091416       NaN
                                     neighbor_average     7.020131       NaN  10.791032       NaN  0.181339       NaN
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
       validation_swap_selected      gls_map              3.158137       NaN   5.436442       NaN  0.075394       NaN
                                     gsp                  3.564440       NaN   6.261758       NaN  0.086716       NaN
                                     historical_tod_mean  3.854327       NaN   6.637095       NaN  0.089390       NaN
                                     neighbor_average     6.892237       NaN  10.518166       NaN  0.161894       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.2 validation_swap_selected gls_map 3.158137 5.436442
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace     0.205183      0.242248 67
    gsp   condition_number    -0.053575      0.008980 67
    gsp information_logdet    -0.310342     -0.306741 67
gls_map    posterior_trace     0.177775      0.146267 67
gls_map   condition_number     0.484680      0.231033 67
gls_map information_logdet     0.125581      0.058227 67
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv