---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-27, 2012-06-22
Test days: 2012-05-02, 2012-05-09
Budgets: [0.2]
Random layouts per budget: 1
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae          rmse          mape    
                                                              mean std      mean std      mean std
budget layout_type                   method                                                       
0.2    best_random_by_trace          gls_map              1.159733 NaN  1.990229 NaN  0.016974 NaN
                                     gsp                  1.136176 NaN  1.973828 NaN  0.016605 NaN
                                     historical_tod_mean  1.095398 NaN  2.015734 NaN  0.015922 NaN
                                     neighbor_average     2.816850 NaN  3.431210 NaN  0.041481 NaN
       best_random_by_validation     gls_map              1.159733 NaN  1.990229 NaN  0.016974 NaN
                                     gsp                  1.136176 NaN  1.973828 NaN  0.016605 NaN
                                     historical_tod_mean  1.095398 NaN  2.015734 NaN  0.015922 NaN
                                     neighbor_average     2.816850 NaN  3.431210 NaN  0.041481 NaN
       coverage                      gls_map              1.171993 NaN  1.894464 NaN  0.017175 NaN
                                     gsp                  1.200031 NaN  1.873399 NaN  0.017622 NaN
                                     historical_tod_mean  0.951621 NaN  1.892028 NaN  0.013789 NaN
                                     neighbor_average     2.908974 NaN  3.545338 NaN  0.043126 NaN
       degree                        gls_map              1.591217 NaN  2.289516 NaN  0.023586 NaN
                                     gsp                  1.246682 NaN  1.852561 NaN  0.018486 NaN
                                     historical_tod_mean  0.980522 NaN  1.805267 NaN  0.014388 NaN
                                     neighbor_average     2.911905 NaN  3.557443 NaN  0.044120 NaN
       graph_sampling_laplacian      gls_map              1.396464 NaN  2.109162 NaN  0.020556 NaN
                                     gsp                  1.043826 NaN  1.851986 NaN  0.015245 NaN
                                     historical_tod_mean  1.002473 NaN  1.910693 NaN  0.014556 NaN
                                     neighbor_average     2.414286 NaN  2.970590 NaN  0.035852 NaN
       greedy_a_trace                gls_map              1.142206 NaN  1.923556 NaN  0.016776 NaN
                                     gsp                  1.154720 NaN  1.937309 NaN  0.016943 NaN
                                     historical_tod_mean  1.063709 NaN  1.984423 NaN  0.015475 NaN
                                     neighbor_average     2.593040 NaN  3.202843 NaN  0.038348 NaN
       greedy_d_logdet               gls_map              1.274014 NaN  2.011617 NaN  0.018812 NaN
                                     gsp                  1.347449 NaN  1.917530 NaN  0.019891 NaN
                                     historical_tod_mean  0.951854 NaN  1.832603 NaN  0.013853 NaN
                                     neighbor_average     2.682234 NaN  3.314921 NaN  0.039295 NaN
       multistart_swap_by_validation gls_map              1.194256 NaN  1.952828 NaN  0.017551 NaN
                                     gsp                  1.236425 NaN  1.964931 NaN  0.018163 NaN
                                     historical_tod_mean  1.052514 NaN  1.984762 NaN  0.015301 NaN
                                     neighbor_average     2.689744 NaN  3.245485 NaN  0.039663 NaN
       observability_proxy           gls_map              1.525919 NaN  2.292613 NaN  0.022579 NaN
                                     gsp                  1.284559 NaN  1.844294 NaN  0.019017 NaN
                                     historical_tod_mean  0.981992 NaN  1.797555 NaN  0.014362 NaN
                                     neighbor_average     2.683516 NaN  3.313734 NaN  0.039709 NaN
       qr_pod_modes                  gls_map              1.144907 NaN  1.889123 NaN  0.016910 NaN
                                     gsp                  1.196762 NaN  1.877347 NaN  0.017652 NaN
                                     historical_tod_mean  0.968516 NaN  1.875348 NaN  0.014122 NaN
                                     neighbor_average     2.594139 NaN  3.194107 NaN  0.038650 NaN
       random                        gls_map              1.159733 NaN  1.990229 NaN  0.016974 NaN
                                     gsp                  1.136176 NaN  1.973828 NaN  0.016605 NaN
                                     historical_tod_mean  1.095398 NaN  2.015734 NaN  0.015922 NaN
                                     neighbor_average     2.816850 NaN  3.431210 NaN  0.041481 NaN
       rcss_selected                 gls_map              1.026621 NaN  1.679818 NaN  0.015036 NaN
                                     gsp                  1.094449 NaN  1.700881 NaN  0.016070 NaN
                                     historical_tod_mean  0.928571 NaN  1.710873 NaN  0.013504 NaN
                                     neighbor_average     2.422894 NaN  2.919488 NaN  0.035891 NaN
       robust_coverage_cvar          gls_map              1.256858 NaN  2.002776 NaN  0.018549 NaN
                                     gsp                  1.271320 NaN  1.965850 NaN  0.018757 NaN
                                     historical_tod_mean  1.058159 NaN  1.978443 NaN  0.015435 NaN
                                     neighbor_average     2.748352 NaN  3.302859 NaN  0.041080 NaN
       scenario_average_a_trace      gls_map              1.334074 NaN  2.055849 NaN  0.019704 NaN
                                     gsp                  1.329788 NaN  1.983568 NaN  0.019653 NaN
                                     historical_tod_mean  1.034698 NaN  1.948150 NaN  0.015120 NaN
                                     neighbor_average     2.725824 NaN  3.246308 NaN  0.040630 NaN
       scenario_cvar_a_trace         gls_map              1.334074 NaN  2.055849 NaN  0.019704 NaN
                                     gsp                  1.329788 NaN  1.983568 NaN  0.019653 NaN
                                     historical_tod_mean  1.034698 NaN  1.948150 NaN  0.015120 NaN
                                     neighbor_average     2.725824 NaN  3.246308 NaN  0.040630 NaN
       swap_from_best_random_trace   gls_map              1.194256 NaN  1.952828 NaN  0.017551 NaN
                                     gsp                  1.236425 NaN  1.964931 NaN  0.018163 NaN
                                     historical_tod_mean  1.052514 NaN  1.984762 NaN  0.015301 NaN
                                     neighbor_average     2.689744 NaN  3.245485 NaN  0.039663 NaN
       swap_from_greedy_a_trace      gls_map              1.111213 NaN  1.850984 NaN  0.016337 NaN
                                     gsp                  1.175502 NaN  1.874394 NaN  0.017286 NaN
                                     historical_tod_mean  0.985247 NaN  1.903901 NaN  0.014327 NaN
                                     neighbor_average     2.644872 NaN  3.241993 NaN  0.039227 NaN
       swap_from_scenario_average    gls_map              1.241650 NaN  1.956974 NaN  0.018288 NaN
                                     gsp                  1.225797 NaN  1.976850 NaN  0.018026 NaN
                                     historical_tod_mean  1.080110 NaN  1.999119 NaN  0.015745 NaN
                                     neighbor_average     2.722894 NaN  3.280490 NaN  0.040215 NaN
       swap_from_scenario_cvar       gls_map              1.241650 NaN  1.956974 NaN  0.018288 NaN
                                     gsp                  1.225797 NaN  1.976850 NaN  0.018026 NaN
                                     historical_tod_mean  1.080110 NaN  1.999119 NaN  0.015745 NaN
                                     neighbor_average     2.722894 NaN  3.280490 NaN  0.040215 NaN
       top_variance                  gls_map              1.024277 NaN  1.745292 NaN  0.015155 NaN
                                     gsp                  1.010789 NaN  1.770483 NaN  0.014943 NaN
                                     historical_tod_mean  0.935989 NaN  1.790107 NaN  0.013748 NaN
                                     neighbor_average     3.077106 NaN  3.648231 NaN  0.046473 NaN
       validation_swap_selected      gls_map              1.059655 NaN  1.695472 NaN  0.015533 NaN
                                     gsp                  1.112775 NaN  1.707149 NaN  0.016347 NaN
                                     historical_tod_mean  0.922981 NaN  1.708490 NaN  0.013421 NaN
                                     neighbor_average     2.427839 NaN  2.923151 NaN  0.035983 NaN
```

## Best method per budget-layout row

```
 budget              layout_type              method      mae    rmse
    0.2 validation_swap_selected historical_tod_mean 0.922981 1.70849
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace     0.559390      0.792564 21
    gsp   condition_number     0.516232      0.402479 21
    gsp information_logdet    -0.662405     -0.848663 21
gls_map    posterior_trace     0.303804      0.084149 21
gls_map   condition_number     0.435792      0.544684 21
gls_map information_logdet    -0.042084     -0.016308 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv