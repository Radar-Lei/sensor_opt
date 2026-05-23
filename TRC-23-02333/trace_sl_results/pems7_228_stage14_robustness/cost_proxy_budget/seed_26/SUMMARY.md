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
0.1    best_random_by_trace          gls_map              1.419509 NaN  3.227075 NaN  0.023123 NaN
                                     gsp                  1.459245 NaN  3.249396 NaN  0.023727 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.984715 NaN  4.081877 NaN  0.046701 NaN
       best_random_by_validation     gls_map              1.419509 NaN  3.227075 NaN  0.023123 NaN
                                     gsp                  1.459245 NaN  3.249396 NaN  0.023727 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.984715 NaN  4.081877 NaN  0.046701 NaN
       cost_aware_coverage_proxy     gls_map              1.471781 NaN  3.236835 NaN  0.023945 NaN
                                     gsp                  1.491400 NaN  3.243563 NaN  0.024271 NaN
                                     historical_tod_mean  1.350244 NaN  3.201930 NaN  0.021998 NaN
                                     neighbor_average     3.041951 NaN  4.175955 NaN  0.046924 NaN
       coverage                      gls_map              1.924638 NaN  2.917435 NaN  0.029189 NaN
                                     gsp                  1.824972 NaN  2.872625 NaN  0.027617 NaN
                                     historical_tod_mean  1.174829 NaN  2.591627 NaN  0.018200 NaN
                                     neighbor_average     3.339350 NaN  4.250682 NaN  0.050657 NaN
       degree                        gls_map              1.560074 NaN  3.276214 NaN  0.025064 NaN
                                     gsp                  1.336887 NaN  3.203555 NaN  0.021754 NaN
                                     historical_tod_mean  1.331939 NaN  3.203316 NaN  0.021684 NaN
                                     neighbor_average     2.915285 NaN  4.059776 NaN  0.045151 NaN
       graph_sampling_laplacian      gls_map              1.378872 NaN  3.219029 NaN  0.022531 NaN
                                     gsp                  1.362798 NaN  3.218414 NaN  0.022250 NaN
                                     historical_tod_mean  1.331537 NaN  3.213820 NaN  0.021726 NaN
                                     neighbor_average     3.710081 NaN  4.951303 NaN  0.058247 NaN
       greedy_a_trace                gls_map              1.466601 NaN  3.282911 NaN  0.023720 NaN
                                     gsp                  1.392646 NaN  3.233334 NaN  0.022581 NaN
                                     historical_tod_mean  1.383585 NaN  3.232667 NaN  0.022453 NaN
                                     neighbor_average     2.939187 NaN  4.088971 NaN  0.045724 NaN
       greedy_d_logdet               gls_map              4.256844 NaN  5.464664 NaN  0.063252 NaN
                                     gsp                  2.046386 NaN  3.023020 NaN  0.030817 NaN
                                     historical_tod_mean  1.228793 NaN  2.638540 NaN  0.018995 NaN
                                     neighbor_average     3.144553 NaN  3.929238 NaN  0.046835 NaN
       multistart_swap_by_validation gls_map              1.415895 NaN  3.227111 NaN  0.023023 NaN
                                     gsp                  1.417559 NaN  3.236780 NaN  0.023037 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     3.039350 NaN  4.140605 NaN  0.047171 NaN
       observability_proxy           gls_map              1.615583 NaN  3.310552 NaN  0.026042 NaN
                                     gsp                  1.337218 NaN  3.155056 NaN  0.021855 NaN
                                     historical_tod_mean  1.311720 NaN  3.149767 NaN  0.021404 NaN
                                     neighbor_average     3.233333 NaN  4.564368 NaN  0.050235 NaN
       qr_pod_modes                  gls_map              1.373424 NaN  3.209572 NaN  0.022370 NaN
                                     gsp                  1.396830 NaN  3.230805 NaN  0.022702 NaN
                                     historical_tod_mean  1.376293 NaN  3.229365 NaN  0.022337 NaN
                                     neighbor_average     2.859512 NaN  4.007145 NaN  0.044056 NaN
       random                        gls_map              1.419509 NaN  3.227075 NaN  0.023123 NaN
                                     gsp                  1.459245 NaN  3.249396 NaN  0.023727 NaN
                                     historical_tod_mean  1.368000 NaN  3.227489 NaN  0.022230 NaN
                                     neighbor_average     2.984715 NaN  4.081877 NaN  0.046701 NaN
       rcss_selected                 gls_map              1.450510 NaN  3.251498 NaN  0.023602 NaN
                                     gsp                  1.458312 NaN  3.245683 NaN  0.023739 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     3.258699 NaN  4.465821 NaN  0.050888 NaN
       robust_coverage_cvar          gls_map              1.535105 NaN  3.263980 NaN  0.024912 NaN
                                     gsp                  1.444959 NaN  3.213048 NaN  0.023559 NaN
                                     historical_tod_mean  1.326000 NaN  3.183553 NaN  0.021637 NaN
                                     neighbor_average     3.111382 NaN  4.345831 NaN  0.048051 NaN
       scenario_average_a_trace      gls_map              1.377393 NaN  3.205306 NaN  0.022384 NaN
                                     gsp                  1.371639 NaN  3.228073 NaN  0.022268 NaN
                                     historical_tod_mean  1.367085 NaN  3.227811 NaN  0.022203 NaN
                                     neighbor_average     2.758211 NaN  3.969388 NaN  0.042847 NaN
       scenario_cvar_a_trace         gls_map              1.530234 NaN  3.296879 NaN  0.024848 NaN
                                     gsp                  1.502225 NaN  3.250606 NaN  0.024430 NaN
                                     historical_tod_mean  1.355500 NaN  3.206813 NaN  0.022080 NaN
                                     neighbor_average     3.083740 NaN  4.128076 NaN  0.047547 NaN
       swap_from_best_random_trace   gls_map              1.415895 NaN  3.227111 NaN  0.023023 NaN
                                     gsp                  1.417559 NaN  3.236780 NaN  0.023037 NaN
                                     historical_tod_mean  1.389744 NaN  3.232750 NaN  0.022558 NaN
                                     neighbor_average     3.039350 NaN  4.140605 NaN  0.047171 NaN
       swap_from_greedy_a_trace      gls_map              1.450510 NaN  3.251498 NaN  0.023602 NaN
                                     gsp                  1.458312 NaN  3.245683 NaN  0.023739 NaN
                                     historical_tod_mean  1.369012 NaN  3.221936 NaN  0.022273 NaN
                                     neighbor_average     3.258699 NaN  4.465821 NaN  0.050888 NaN
       swap_from_scenario_average    gls_map              1.410796 NaN  3.226298 NaN  0.022919 NaN
                                     gsp                  1.403103 NaN  3.238436 NaN  0.022768 NaN
                                     historical_tod_mean  1.393695 NaN  3.238405 NaN  0.022601 NaN
                                     neighbor_average     2.942602 NaN  4.081022 NaN  0.045977 NaN
       swap_from_scenario_cvar       gls_map              1.419213 NaN  3.232714 NaN  0.023098 NaN
                                     gsp                  1.426330 NaN  3.239182 NaN  0.023195 NaN
                                     historical_tod_mean  1.378012 NaN  3.230235 NaN  0.022389 NaN
                                     neighbor_average     3.114309 NaN  4.268647 NaN  0.048584 NaN
       top_variance                  gls_map              1.414859 NaN  3.160307 NaN  0.023060 NaN
                                     gsp                  1.269605 NaN  3.156866 NaN  0.020893 NaN
                                     historical_tod_mean  1.232780 NaN  3.150093 NaN  0.020283 NaN
                                     neighbor_average     3.022114 NaN  4.207041 NaN  0.047390 NaN
       validation_swap_selected      gls_map              1.372984 NaN  3.207411 NaN  0.022370 NaN
                                     gsp                  1.383614 NaN  3.226851 NaN  0.022490 NaN
                                     historical_tod_mean  1.373646 NaN  3.226636 NaN  0.022311 NaN
                                     neighbor_average     3.009106 NaN  4.140955 NaN  0.046766 NaN
```

## Best method per budget-layout row

```
 budget layout_type              method      mae     rmse
    0.1    coverage historical_tod_mean 1.174829 2.591627
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.161212     -0.050425 22
    gsp   condition_number     0.260368      0.499150 22
    gsp information_logdet     0.088487      0.133144 22
gls_map    posterior_trace     0.507542      0.357507 22
gls_map   condition_number     0.778939      0.318980 22
gls_map information_logdet     0.484411     -0.164873 22
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv