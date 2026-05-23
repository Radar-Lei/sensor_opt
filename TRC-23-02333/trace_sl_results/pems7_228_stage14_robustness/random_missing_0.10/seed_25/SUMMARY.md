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
0.1    best_random_by_trace          gls_map              1.178884 NaN  1.932714 NaN  0.017285 NaN
                                     gsp                  1.077478 NaN  1.907119 NaN  0.015758 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.438122 NaN  3.137782 NaN  0.036107 NaN
       best_random_by_validation     gls_map              1.178884 NaN  1.932714 NaN  0.017285 NaN
                                     gsp                  1.077478 NaN  1.907119 NaN  0.015758 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.438122 NaN  3.137782 NaN  0.036107 NaN
       coverage                      gls_map              1.097276 NaN  1.865411 NaN  0.016134 NaN
                                     gsp                  1.213248 NaN  1.897621 NaN  0.017873 NaN
                                     historical_tod_mean  1.002439 NaN  1.907490 NaN  0.014616 NaN
                                     neighbor_average     2.538126 NaN  3.220696 NaN  0.037650 NaN
       degree                        gls_map              1.190407 NaN  1.933950 NaN  0.017491 NaN
                                     gsp                  1.098544 NaN  1.885762 NaN  0.016109 NaN
                                     historical_tod_mean  1.021415 NaN  1.924166 NaN  0.014874 NaN
                                     neighbor_average     2.059654 NaN  2.697643 NaN  0.030301 NaN
       graph_sampling_laplacian      gls_map              1.059639 NaN  1.915904 NaN  0.015469 NaN
                                     gsp                  1.074055 NaN  1.899827 NaN  0.015706 NaN
                                     historical_tod_mean  1.041354 NaN  1.944015 NaN  0.015154 NaN
                                     neighbor_average     2.782276 NaN  3.414419 NaN  0.042031 NaN
       greedy_a_trace                gls_map              1.106196 NaN  1.955210 NaN  0.016161 NaN
                                     gsp                  1.096905 NaN  1.960382 NaN  0.016006 NaN
                                     historical_tod_mean  1.087841 NaN  1.983791 NaN  0.015833 NaN
                                     neighbor_average     2.162671 NaN  2.899145 NaN  0.032230 NaN
       greedy_d_logdet               gls_map              1.276135 NaN  1.959011 NaN  0.018800 NaN
                                     gsp                  1.292905 NaN  1.897261 NaN  0.019069 NaN
                                     historical_tod_mean  0.993963 NaN  1.876424 NaN  0.014481 NaN
                                     neighbor_average     2.205256 NaN  2.912867 NaN  0.032385 NaN
       multistart_swap_by_validation gls_map              1.095946 NaN  1.942470 NaN  0.016023 NaN
                                     gsp                  1.094259 NaN  1.947540 NaN  0.015990 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     2.284967 NaN  2.996442 NaN  0.033877 NaN
       observability_proxy           gls_map              1.461554 NaN  2.105355 NaN  0.021639 NaN
                                     gsp                  1.252910 NaN  1.821356 NaN  0.018520 NaN
                                     historical_tod_mean  0.971329 NaN  1.779450 NaN  0.014183 NaN
                                     neighbor_average     2.670228 NaN  3.489050 NaN  0.039793 NaN
       qr_pod_modes                  gls_map              1.149033 NaN  1.936981 NaN  0.016800 NaN
                                     gsp                  1.053844 NaN  1.935184 NaN  0.015358 NaN
                                     historical_tod_mean  1.051061 NaN  1.953103 NaN  0.015289 NaN
                                     neighbor_average     2.342378 NaN  3.109484 NaN  0.034264 NaN
       random                        gls_map              1.178884 NaN  1.932714 NaN  0.017285 NaN
                                     gsp                  1.077478 NaN  1.907119 NaN  0.015758 NaN
                                     historical_tod_mean  1.046866 NaN  1.949590 NaN  0.015231 NaN
                                     neighbor_average     2.438122 NaN  3.137782 NaN  0.036107 NaN
       rcss_selected                 gls_map              1.237713 NaN  1.913083 NaN  0.018294 NaN
                                     gsp                  1.179031 NaN  1.770190 NaN  0.017442 NaN
                                     historical_tod_mean  0.935890 NaN  1.742027 NaN  0.013706 NaN
                                     neighbor_average     2.447817 NaN  3.232132 NaN  0.036843 NaN
       robust_coverage_cvar          gls_map              1.097536 NaN  1.961980 NaN  0.016043 NaN
                                     gsp                  1.092413 NaN  1.953914 NaN  0.015944 NaN
                                     historical_tod_mean  1.083549 NaN  1.978200 NaN  0.015770 NaN
                                     neighbor_average     2.254549 NaN  2.900555 NaN  0.033366 NaN
       scenario_average_a_trace      gls_map              1.182561 NaN  1.893325 NaN  0.017416 NaN
                                     gsp                  1.093464 NaN  1.859432 NaN  0.016076 NaN
                                     historical_tod_mean  0.995646 NaN  1.890692 NaN  0.014527 NaN
                                     neighbor_average     2.421061 NaN  3.073295 NaN  0.035753 NaN
       scenario_cvar_a_trace         gls_map              1.229385 NaN  1.908135 NaN  0.018248 NaN
                                     gsp                  1.211197 NaN  1.781054 NaN  0.017943 NaN
                                     historical_tod_mean  0.961915 NaN  1.740801 NaN  0.014097 NaN
                                     neighbor_average     2.610654 NaN  3.482443 NaN  0.039240 NaN
       swap_from_best_random_trace   gls_map              1.095946 NaN  1.942470 NaN  0.016023 NaN
                                     gsp                  1.094259 NaN  1.947540 NaN  0.015990 NaN
                                     historical_tod_mean  1.083902 NaN  1.976261 NaN  0.015788 NaN
                                     neighbor_average     2.284967 NaN  2.996442 NaN  0.033877 NaN
       swap_from_greedy_a_trace      gls_map              1.093811 NaN  1.954555 NaN  0.015991 NaN
                                     gsp                  1.092655 NaN  1.947003 NaN  0.015970 NaN
                                     historical_tod_mean  1.080439 NaN  1.975844 NaN  0.015739 NaN
                                     neighbor_average     2.446902 NaN  3.253271 NaN  0.036607 NaN
       swap_from_scenario_average    gls_map              1.082237 NaN  1.950798 NaN  0.015809 NaN
                                     gsp                  1.087719 NaN  1.946166 NaN  0.015892 NaN
                                     historical_tod_mean  1.079707 NaN  1.975432 NaN  0.015724 NaN
                                     neighbor_average     2.224415 NaN  2.924522 NaN  0.032646 NaN
       swap_from_scenario_cvar       gls_map              1.198796 NaN  2.043366 NaN  0.017495 NaN
                                     gsp                  1.074161 NaN  1.959557 NaN  0.015642 NaN
                                     historical_tod_mean  1.075159 NaN  1.968041 NaN  0.015645 NaN
                                     neighbor_average     2.426496 NaN  3.113583 NaN  0.036056 NaN
       top_variance                  gls_map              1.202800 NaN  1.795556 NaN  0.017822 NaN
                                     gsp                  1.042772 NaN  1.738394 NaN  0.015400 NaN
                                     historical_tod_mean  0.947317 NaN  1.758529 NaN  0.013886 NaN
                                     neighbor_average     3.227057 NaN  3.978212 NaN  0.048919 NaN
       validation_swap_selected      gls_map              1.246528 NaN  1.929194 NaN  0.018425 NaN
                                     gsp                  1.164878 NaN  1.762820 NaN  0.017227 NaN
                                     historical_tod_mean  0.934524 NaN  1.741821 NaN  0.013684 NaN
                                     neighbor_average     2.932049 NaN  3.736937 NaN  0.044146 NaN
```

## Best method per budget-layout row

```
 budget              layout_type              method      mae     rmse
    0.1 validation_swap_selected historical_tod_mean 0.934524 1.741821
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.191438     -0.116612 21
    gsp   condition_number     0.316520      0.319870 21
    gsp information_logdet    -0.184979     -0.163518 21
gls_map    posterior_trace     0.349177      0.379805 21
gls_map   condition_number     0.146680      0.256026 21
gls_map information_logdet    -0.058757     -0.213029 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv