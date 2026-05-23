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
0.1    best_random_by_trace          gls_map              1.145852 NaN  1.918715 NaN  0.016787 NaN
                                     gsp                  1.073267 NaN  1.908672 NaN  0.015692 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.772033 NaN  3.366695 NaN  0.040836 NaN
       best_random_by_validation     gls_map              1.145852 NaN  1.918715 NaN  0.016787 NaN
                                     gsp                  1.073267 NaN  1.908672 NaN  0.015692 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.772033 NaN  3.366695 NaN  0.040836 NaN
       cost_aware_coverage_proxy     gls_map              1.231569 NaN  1.949531 NaN  0.018131 NaN
                                     gsp                  1.321253 NaN  1.934121 NaN  0.019486 NaN
                                     historical_tod_mean  1.050183 NaN  1.925451 NaN  0.015314 NaN
                                     neighbor_average     2.671382 NaN  3.272872 NaN  0.039322 NaN
       coverage                      gls_map              1.112023 NaN  1.860939 NaN  0.016370 NaN
                                     gsp                  1.277462 NaN  1.922191 NaN  0.018842 NaN
                                     historical_tod_mean  1.002439 NaN  1.907490 NaN  0.014616 NaN
                                     neighbor_average     2.783415 NaN  3.348931 NaN  0.041623 NaN
       degree                        gls_map              1.208832 NaN  1.942650 NaN  0.017763 NaN
                                     gsp                  1.122966 NaN  1.887129 NaN  0.016482 NaN
                                     historical_tod_mean  1.021415 NaN  1.924166 NaN  0.014874 NaN
                                     neighbor_average     2.647480 NaN  3.193401 NaN  0.039129 NaN
       graph_sampling_laplacian      gls_map              1.059891 NaN  1.922650 NaN  0.015477 NaN
                                     gsp                  1.050465 NaN  1.916306 NaN  0.015327 NaN
                                     historical_tod_mean  1.041354 NaN  1.944015 NaN  0.015154 NaN
                                     neighbor_average     2.782276 NaN  3.414419 NaN  0.042031 NaN
       greedy_a_trace                gls_map              1.103271 NaN  1.951491 NaN  0.016118 NaN
                                     gsp                  1.100274 NaN  1.956625 NaN  0.016064 NaN
                                     historical_tod_mean  1.087841 NaN  1.983791 NaN  0.015833 NaN
                                     neighbor_average     2.557236 NaN  3.200411 NaN  0.038072 NaN
       greedy_d_logdet               gls_map              1.261054 NaN  1.943783 NaN  0.018577 NaN
                                     gsp                  1.255815 NaN  1.880281 NaN  0.018511 NaN
                                     historical_tod_mean  0.993963 NaN  1.876424 NaN  0.014481 NaN
                                     neighbor_average     2.575285 NaN  3.135899 NaN  0.037786 NaN
       multistart_swap_by_validation gls_map              1.098395 NaN  1.940559 NaN  0.016062 NaN
                                     gsp                  1.099039 NaN  1.944283 NaN  0.016068 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     2.568130 NaN  3.228273 NaN  0.037969 NaN
       observability_proxy           gls_map              1.459492 NaN  2.108845 NaN  0.021610 NaN
                                     gsp                  1.260935 NaN  1.825727 NaN  0.018641 NaN
                                     historical_tod_mean  0.971329 NaN  1.779450 NaN  0.014183 NaN
                                     neighbor_average     2.919187 NaN  3.642533 NaN  0.043525 NaN
       qr_pod_modes                  gls_map              1.124810 NaN  1.902793 NaN  0.016461 NaN
                                     gsp                  1.071888 NaN  1.918550 NaN  0.015660 NaN
                                     historical_tod_mean  1.051061 NaN  1.953103 NaN  0.015289 NaN
                                     neighbor_average     2.570244 NaN  3.224642 NaN  0.037655 NaN
       random                        gls_map              1.145852 NaN  1.918715 NaN  0.016787 NaN
                                     gsp                  1.073267 NaN  1.908672 NaN  0.015692 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.772033 NaN  3.366695 NaN  0.040836 NaN
       rcss_selected                 gls_map              1.230420 NaN  1.904061 NaN  0.018188 NaN
                                     gsp                  1.159410 NaN  1.761108 NaN  0.017147 NaN
                                     historical_tod_mean  0.935890 NaN  1.742027 NaN  0.013706 NaN
                                     neighbor_average     3.003252 NaN  3.699378 NaN  0.045182 NaN
       robust_coverage_cvar          gls_map              1.089078 NaN  1.967120 NaN  0.015913 NaN
                                     gsp                  1.088707 NaN  1.959556 NaN  0.015877 NaN
                                     historical_tod_mean  1.083549 NaN  1.978200 NaN  0.015770 NaN
                                     neighbor_average     2.812683 NaN  3.325022 NaN  0.041714 NaN
       scenario_average_a_trace      gls_map              1.264841 NaN  1.937679 NaN  0.018669 NaN
                                     gsp                  1.193267 NaN  1.879802 NaN  0.017583 NaN
                                     historical_tod_mean  0.995646 NaN  1.890692 NaN  0.014527 NaN
                                     neighbor_average     2.614797 NaN  3.248288 NaN  0.038771 NaN
       scenario_cvar_a_trace         gls_map              1.248453 NaN  1.914184 NaN  0.018540 NaN
                                     gsp                  1.270787 NaN  1.814901 NaN  0.018841 NaN
                                     historical_tod_mean  0.961915 NaN  1.740801 NaN  0.014097 NaN
                                     neighbor_average     2.904553 NaN  3.613420 NaN  0.043540 NaN
       swap_from_best_random_trace   gls_map              1.098395 NaN  1.940559 NaN  0.016062 NaN
                                     gsp                  1.099039 NaN  1.944283 NaN  0.016068 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     2.568130 NaN  3.228273 NaN  0.037969 NaN
       swap_from_greedy_a_trace      gls_map              1.093905 NaN  1.952211 NaN  0.015994 NaN
                                     gsp                  1.096872 NaN  1.944114 NaN  0.016039 NaN
                                     historical_tod_mean  1.080439 NaN  1.975844 NaN  0.015739 NaN
                                     neighbor_average     2.820813 NaN  3.534715 NaN  0.042182 NaN
       swap_from_scenario_average    gls_map              1.082450 NaN  1.953278 NaN  0.015810 NaN
                                     gsp                  1.089050 NaN  1.945039 NaN  0.015914 NaN
                                     historical_tod_mean  1.079707 NaN  1.975432 NaN  0.015724 NaN
                                     neighbor_average     2.535122 NaN  3.190284 NaN  0.037331 NaN
       swap_from_scenario_cvar       gls_map              1.193500 NaN  2.037881 NaN  0.017419 NaN
                                     gsp                  1.074774 NaN  1.951946 NaN  0.015662 NaN
                                     historical_tod_mean  1.075159 NaN  1.968041 NaN  0.015645 NaN
                                     neighbor_average     2.634634 NaN  3.313668 NaN  0.039046 NaN
       top_variance                  gls_map              1.149733 NaN  1.749237 NaN  0.017013 NaN
                                     gsp                  1.022750 NaN  1.735078 NaN  0.015091 NaN
                                     historical_tod_mean  0.947317 NaN  1.758529 NaN  0.013886 NaN
                                     neighbor_average     3.368943 NaN  4.064448 NaN  0.051098 NaN
       validation_swap_selected      gls_map              1.229144 NaN  1.905546 NaN  0.018166 NaN
                                     gsp                  1.174840 NaN  1.767377 NaN  0.017376 NaN
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
    gsp    posterior_trace    -0.287397     -0.092865 22
    gsp   condition_number     0.276987      0.253681 22
    gsp information_logdet    -0.268421     -0.169875 22
gls_map    posterior_trace     0.299344      0.375991 22
gls_map   condition_number     0.152691      0.362401 22
gls_map information_logdet     0.035608      0.036240 22
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv