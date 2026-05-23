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
0.2    best_random_by_trace          gls_map              1.111034 NaN  1.928549 NaN  0.016193 NaN
                                     gsp                  1.093667 NaN  1.957856 NaN  0.015929 NaN
                                     historical_tod_mean  1.080893 NaN  1.989276 NaN  0.015691 NaN
                                     neighbor_average     2.535165 NaN  3.087952 NaN  0.037157 NaN
       best_random_by_validation     gls_map              1.111034 NaN  1.928549 NaN  0.016193 NaN
                                     gsp                  1.093667 NaN  1.957856 NaN  0.015929 NaN
                                     historical_tod_mean  1.080893 NaN  1.989276 NaN  0.015691 NaN
                                     neighbor_average     2.535165 NaN  3.087952 NaN  0.037157 NaN
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
       multistart_swap_by_validation gls_map              1.262783 NaN  1.967066 NaN  0.018574 NaN
                                     gsp                  1.181971 NaN  1.962091 NaN  0.017365 NaN
                                     historical_tod_mean  1.059396 NaN  1.994245 NaN  0.015423 NaN
                                     neighbor_average     2.429487 NaN  3.042318 NaN  0.035956 NaN
       observability_proxy           gls_map              1.525919 NaN  2.292613 NaN  0.022579 NaN
                                     gsp                  1.284559 NaN  1.844294 NaN  0.019017 NaN
                                     historical_tod_mean  0.981992 NaN  1.797555 NaN  0.014362 NaN
                                     neighbor_average     2.683516 NaN  3.313734 NaN  0.039709 NaN
       qr_pod_modes                  gls_map              1.144907 NaN  1.889123 NaN  0.016910 NaN
                                     gsp                  1.196762 NaN  1.877347 NaN  0.017652 NaN
                                     historical_tod_mean  0.968516 NaN  1.875348 NaN  0.014122 NaN
                                     neighbor_average     2.594139 NaN  3.194107 NaN  0.038650 NaN
       random                        gls_map              1.111034 NaN  1.928549 NaN  0.016193 NaN
                                     gsp                  1.093667 NaN  1.957856 NaN  0.015929 NaN
                                     historical_tod_mean  1.080893 NaN  1.989276 NaN  0.015691 NaN
                                     neighbor_average     2.535165 NaN  3.087952 NaN  0.037157 NaN
       rcss_selected                 gls_map              1.108327 NaN  1.998405 NaN  0.016093 NaN
                                     gsp                  1.029985 NaN  1.934457 NaN  0.014930 NaN
                                     historical_tod_mean  1.029354 NaN  1.944044 NaN  0.014910 NaN
                                     neighbor_average     2.354029 NaN  2.867336 NaN  0.034625 NaN
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
       swap_from_best_random_trace   gls_map              1.262783 NaN  1.967066 NaN  0.018574 NaN
                                     gsp                  1.181971 NaN  1.962091 NaN  0.017365 NaN
                                     historical_tod_mean  1.059396 NaN  1.994245 NaN  0.015423 NaN
                                     neighbor_average     2.429487 NaN  3.042318 NaN  0.035956 NaN
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
       validation_swap_selected      gls_map              1.112770 NaN  1.987227 NaN  0.016170 NaN
                                     gsp                  1.034182 NaN  1.916888 NaN  0.015014 NaN
                                     historical_tod_mean  1.026552 NaN  1.942627 NaN  0.014868 NaN
                                     neighbor_average     2.352930 NaN  2.878446 NaN  0.034606 NaN
```

## Best method per budget-layout row

```
 budget  layout_type              method      mae     rmse
    0.2 top_variance historical_tod_mean 0.935989 1.790107
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace     0.427233      0.422048 21
    gsp   condition_number     0.395825      0.239400 21
    gsp information_logdet    -0.504641     -0.560339 21
gls_map    posterior_trace     0.263848      0.011089 21
gls_map   condition_number     0.399397      0.397260 21
gls_map information_logdet    -0.013747      0.068493 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv