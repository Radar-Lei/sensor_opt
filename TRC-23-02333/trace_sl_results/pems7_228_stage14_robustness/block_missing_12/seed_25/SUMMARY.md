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
0.1    best_random_by_trace          gls_map              1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     gsp                  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     1.046866 NaN  1.949590 NaN  0.015231 NaN
       best_random_by_validation     gls_map              1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     gsp                  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     1.046866 NaN  1.949590 NaN  0.015231 NaN
       coverage                      gls_map              1.002439 NaN  1.907490 NaN  0.014616 NaN
                                     gsp                  1.002439 NaN  1.907490 NaN  0.014616 NaN
                                     historical_tod_mean  1.002439 NaN  1.907490 NaN  0.014616 NaN
                                     neighbor_average     1.002439 NaN  1.907490 NaN  0.014616 NaN
       degree                        gls_map              1.021415 NaN  1.924166 NaN  0.014874 NaN
                                     gsp                  1.021415 NaN  1.924166 NaN  0.014874 NaN
                                     historical_tod_mean  1.021415 NaN  1.924166 NaN  0.014874 NaN
                                     neighbor_average     1.021415 NaN  1.924166 NaN  0.014874 NaN
       graph_sampling_laplacian      gls_map              1.041354 NaN  1.944015 NaN  0.015154 NaN
                                     gsp                  1.041354 NaN  1.944015 NaN  0.015154 NaN
                                     historical_tod_mean  1.041354 NaN  1.944015 NaN  0.015154 NaN
                                     neighbor_average     1.041354 NaN  1.944015 NaN  0.015154 NaN
       greedy_a_trace                gls_map              1.087841 NaN  1.983791 NaN  0.015833 NaN
                                     gsp                  1.087841 NaN  1.983791 NaN  0.015833 NaN
                                     historical_tod_mean  1.087841 NaN  1.983791 NaN  0.015833 NaN
                                     neighbor_average     1.087841 NaN  1.983791 NaN  0.015833 NaN
       greedy_d_logdet               gls_map              0.993963 NaN  1.876424 NaN  0.014481 NaN
                                     gsp                  0.993963 NaN  1.876424 NaN  0.014481 NaN
                                     historical_tod_mean  0.993963 NaN  1.876424 NaN  0.014481 NaN
                                     neighbor_average     0.993963 NaN  1.876424 NaN  0.014481 NaN
       multistart_swap_by_validation gls_map              1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     gsp                  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     1.083902 NaN  1.976261 NaN  0.015788 NaN
       observability_proxy           gls_map              0.971329 NaN  1.779450 NaN  0.014183 NaN
                                     gsp                  0.971329 NaN  1.779450 NaN  0.014183 NaN
                                     historical_tod_mean  0.971329 NaN  1.779450 NaN  0.014183 NaN
                                     neighbor_average     0.971329 NaN  1.779450 NaN  0.014183 NaN
       qr_pod_modes                  gls_map              1.051061 NaN  1.953103 NaN  0.015289 NaN
                                     gsp                  1.051061 NaN  1.953103 NaN  0.015289 NaN
                                     historical_tod_mean  1.051061 NaN  1.953103 NaN  0.015289 NaN
                                     neighbor_average     1.051061 NaN  1.953103 NaN  0.015289 NaN
       random                        gls_map              1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     gsp                  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     1.046866 NaN  1.949590 NaN  0.015231 NaN
       rcss_selected                 gls_map              0.935890 NaN  1.742027 NaN  0.013706 NaN
                                     gsp                  0.935890 NaN  1.742027 NaN  0.013706 NaN
                                     historical_tod_mean  0.935890 NaN  1.742027 NaN  0.013706 NaN
                                     neighbor_average     0.935890 NaN  1.742027 NaN  0.013706 NaN
       robust_coverage_cvar          gls_map              1.083549 NaN  1.978200 NaN  0.015770 NaN
                                     gsp                  1.083549 NaN  1.978200 NaN  0.015770 NaN
                                     historical_tod_mean  1.083549 NaN  1.978200 NaN  0.015770 NaN
                                     neighbor_average     1.083549 NaN  1.978200 NaN  0.015770 NaN
       scenario_average_a_trace      gls_map              0.995646 NaN  1.890692 NaN  0.014527 NaN
                                     gsp                  0.995646 NaN  1.890692 NaN  0.014527 NaN
                                     historical_tod_mean  0.995646 NaN  1.890692 NaN  0.014527 NaN
                                     neighbor_average     0.995646 NaN  1.890692 NaN  0.014527 NaN
       scenario_cvar_a_trace         gls_map              0.961915 NaN  1.740801 NaN  0.014097 NaN
                                     gsp                  0.961915 NaN  1.740801 NaN  0.014097 NaN
                                     historical_tod_mean  0.961915 NaN  1.740801 NaN  0.014097 NaN
                                     neighbor_average     0.961915 NaN  1.740801 NaN  0.014097 NaN
       swap_from_best_random_trace   gls_map              1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     gsp                  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     1.083902 NaN  1.976261 NaN  0.015788 NaN
       swap_from_greedy_a_trace      gls_map              1.080439 NaN  1.975844 NaN  0.015739 NaN
                                     gsp                  1.080439 NaN  1.975844 NaN  0.015739 NaN
                                     historical_tod_mean  1.080439 NaN  1.975844 NaN  0.015739 NaN
                                     neighbor_average     1.080439 NaN  1.975844 NaN  0.015739 NaN
       swap_from_scenario_average    gls_map              1.079707 NaN  1.975432 NaN  0.015724 NaN
                                     gsp                  1.079707 NaN  1.975432 NaN  0.015724 NaN
                                     historical_tod_mean  1.079707 NaN  1.975432 NaN  0.015724 NaN
                                     neighbor_average     1.079707 NaN  1.975432 NaN  0.015724 NaN
       swap_from_scenario_cvar       gls_map              1.075159 NaN  1.968041 NaN  0.015645 NaN
                                     gsp                  1.075159 NaN  1.968041 NaN  0.015645 NaN
                                     historical_tod_mean  1.075159 NaN  1.968041 NaN  0.015645 NaN
                                     neighbor_average     1.075159 NaN  1.968041 NaN  0.015645 NaN
       top_variance                  gls_map              0.947317 NaN  1.758529 NaN  0.013886 NaN
                                     gsp                  0.947317 NaN  1.758529 NaN  0.013886 NaN
                                     historical_tod_mean  0.947317 NaN  1.758529 NaN  0.013886 NaN
                                     neighbor_average     0.947317 NaN  1.758529 NaN  0.013886 NaN
       validation_swap_selected      gls_map              0.934524 NaN  1.741821 NaN  0.013684 NaN
                                     gsp                  0.934524 NaN  1.741821 NaN  0.013684 NaN
                                     historical_tod_mean  0.934524 NaN  1.741821 NaN  0.013684 NaN
                                     neighbor_average     0.934524 NaN  1.741821 NaN  0.013684 NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 0.934524 1.741821
```

## Certificate-error correlations

```
No stable certificate correlations were available.
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv