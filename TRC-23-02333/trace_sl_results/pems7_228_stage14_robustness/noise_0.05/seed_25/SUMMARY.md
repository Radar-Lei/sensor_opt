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
0.1    best_random_by_trace          gls_map              1.194625 NaN  1.932168 NaN  0.017533 NaN
                                     gsp                  1.102550 NaN  1.902209 NaN  0.016148 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.772033 NaN  3.366695 NaN  0.040836 NaN
       best_random_by_validation     gls_map              1.194625 NaN  1.932168 NaN  0.017533 NaN
                                     gsp                  1.102550 NaN  1.902209 NaN  0.016148 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.772033 NaN  3.366695 NaN  0.040836 NaN
       coverage                      gls_map              1.205720 NaN  1.898114 NaN  0.017792 NaN
                                     gsp                  1.338149 NaN  1.950567 NaN  0.019756 NaN
                                     historical_tod_mean  1.002439 NaN  1.907490 NaN  0.014616 NaN
                                     neighbor_average     2.783415 NaN  3.348931 NaN  0.041623 NaN
       degree                        gls_map              1.289656 NaN  1.985581 NaN  0.018976 NaN
                                     gsp                  1.173186 NaN  1.894748 NaN  0.017242 NaN
                                     historical_tod_mean  1.021415 NaN  1.924166 NaN  0.014874 NaN
                                     neighbor_average     2.647480 NaN  3.193401 NaN  0.039129 NaN
       graph_sampling_laplacian      gls_map              1.102724 NaN  1.932163 NaN  0.016138 NaN
                                     gsp                  1.071172 NaN  1.901066 NaN  0.015660 NaN
                                     historical_tod_mean  1.041354 NaN  1.944015 NaN  0.015154 NaN
                                     neighbor_average     2.782276 NaN  3.414419 NaN  0.042031 NaN
       greedy_a_trace                gls_map              1.127720 NaN  1.936825 NaN  0.016508 NaN
                                     gsp                  1.122831 NaN  1.944888 NaN  0.016428 NaN
                                     historical_tod_mean  1.087841 NaN  1.983791 NaN  0.015833 NaN
                                     neighbor_average     2.557236 NaN  3.200411 NaN  0.038072 NaN
       greedy_d_logdet               gls_map              1.340588 NaN  1.979728 NaN  0.019790 NaN
                                     gsp                  1.316069 NaN  1.908539 NaN  0.019417 NaN
                                     historical_tod_mean  0.993963 NaN  1.876424 NaN  0.014481 NaN
                                     neighbor_average     2.575285 NaN  3.135899 NaN  0.037786 NaN
       multistart_swap_by_validation gls_map              1.159084 NaN  1.925096 NaN  0.016991 NaN
                                     gsp                  1.123881 NaN  1.935566 NaN  0.016460 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     2.568130 NaN  3.228273 NaN  0.037969 NaN
       observability_proxy           gls_map              1.539924 NaN  2.184352 NaN  0.022815 NaN
                                     gsp                  1.322688 NaN  1.860640 NaN  0.019571 NaN
                                     historical_tod_mean  0.971329 NaN  1.779450 NaN  0.014183 NaN
                                     neighbor_average     2.919187 NaN  3.642533 NaN  0.043525 NaN
       qr_pod_modes                  gls_map              1.200565 NaN  1.905589 NaN  0.017621 NaN
                                     gsp                  1.100612 NaN  1.911638 NaN  0.016109 NaN
                                     historical_tod_mean  1.051061 NaN  1.953103 NaN  0.015289 NaN
                                     neighbor_average     2.570244 NaN  3.224642 NaN  0.037655 NaN
       random                        gls_map              1.194625 NaN  1.932168 NaN  0.017533 NaN
                                     gsp                  1.102550 NaN  1.902209 NaN  0.016148 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.772033 NaN  3.366695 NaN  0.040836 NaN
       rcss_selected                 gls_map              1.301582 NaN  1.981985 NaN  0.019246 NaN
                                     gsp                  1.216032 NaN  1.788765 NaN  0.017998 NaN
                                     historical_tod_mean  0.935890 NaN  1.742027 NaN  0.013706 NaN
                                     neighbor_average     3.003252 NaN  3.699378 NaN  0.045182 NaN
       robust_coverage_cvar          gls_map              1.110804 NaN  1.935659 NaN  0.016263 NaN
                                     gsp                  1.102259 NaN  1.945201 NaN  0.016109 NaN
                                     historical_tod_mean  1.083549 NaN  1.978200 NaN  0.015770 NaN
                                     neighbor_average     2.812683 NaN  3.325022 NaN  0.041714 NaN
       scenario_average_a_trace      gls_map              1.351394 NaN  1.985333 NaN  0.019964 NaN
                                     gsp                  1.250020 NaN  1.899945 NaN  0.018439 NaN
                                     historical_tod_mean  0.995646 NaN  1.890692 NaN  0.014527 NaN
                                     neighbor_average     2.614797 NaN  3.248288 NaN  0.038771 NaN
       scenario_cvar_a_trace         gls_map              1.450654 NaN  2.074678 NaN  0.021559 NaN
                                     gsp                  1.332747 NaN  1.854031 NaN  0.019772 NaN
                                     historical_tod_mean  0.961915 NaN  1.740801 NaN  0.014097 NaN
                                     neighbor_average     2.904553 NaN  3.613420 NaN  0.043540 NaN
       swap_from_best_random_trace   gls_map              1.159084 NaN  1.925096 NaN  0.016991 NaN
                                     gsp                  1.123881 NaN  1.935566 NaN  0.016460 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     2.568130 NaN  3.228273 NaN  0.037969 NaN
       swap_from_greedy_a_trace      gls_map              1.132619 NaN  1.943512 NaN  0.016605 NaN
                                     gsp                  1.122647 NaN  1.934687 NaN  0.016447 NaN
                                     historical_tod_mean  1.080439 NaN  1.975844 NaN  0.015739 NaN
                                     neighbor_average     2.820813 NaN  3.534715 NaN  0.042182 NaN
       swap_from_scenario_average    gls_map              1.115535 NaN  1.941073 NaN  0.016318 NaN
                                     gsp                  1.112783 NaN  1.934775 NaN  0.016290 NaN
                                     historical_tod_mean  1.079707 NaN  1.975432 NaN  0.015724 NaN
                                     neighbor_average     2.535122 NaN  3.190284 NaN  0.037331 NaN
       swap_from_scenario_cvar       gls_map              1.150489 NaN  1.995043 NaN  0.016812 NaN
                                     gsp                  1.083552 NaN  1.933836 NaN  0.015824 NaN
                                     historical_tod_mean  1.075159 NaN  1.968041 NaN  0.015645 NaN
                                     neighbor_average     2.634634 NaN  3.313668 NaN  0.039046 NaN
       top_variance                  gls_map              1.192607 NaN  1.766549 NaN  0.017667 NaN
                                     gsp                  1.060564 NaN  1.741938 NaN  0.015671 NaN
                                     historical_tod_mean  0.947317 NaN  1.758529 NaN  0.013886 NaN
                                     neighbor_average     3.368943 NaN  4.064448 NaN  0.051098 NaN
       validation_swap_selected      gls_map              1.341410 NaN  2.015016 NaN  0.019850 NaN
                                     gsp                  1.232748 NaN  1.796570 NaN  0.018246 NaN
                                     historical_tod_mean  0.934524 NaN  1.741821 NaN  0.013684 NaN
                                     neighbor_average     3.126992 NaN  3.825420 NaN  0.046999 NaN
```

## Best method per budget-layout row

```
 budget              layout_type              method      mae     rmse
    0.1 validation_swap_selected historical_tod_mean 0.934524 1.741821
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.284294     -0.150489 21
    gsp   condition_number     0.172747      0.133550 21
    gsp information_logdet    -0.320298     -0.285993 21
gls_map    posterior_trace     0.318477      0.371987 21
gls_map   condition_number     0.125670      0.353746 21
gls_map information_logdet     0.032760     -0.009772 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv