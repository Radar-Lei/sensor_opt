---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-26, 2012-06-27
Test days: 2012-06-28, 2012-06-29
Budgets: [0.1]
Random layouts per budget: 1
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae          rmse          mape    
                                                              mean std      mean std      mean std
budget layout_type                   method                                                       
0.1    best_random_by_trace          gls_map              1.255866 NaN  2.298942 NaN  0.019998 NaN
                                     gsp                  1.222407 NaN  2.324572 NaN  0.019491 NaN
                                     historical_tod_mean  1.113512 NaN  2.278470 NaN  0.017748 NaN
                                     neighbor_average     2.944228 NaN  4.003725 NaN  0.046010 NaN
       best_random_by_validation     gls_map              1.255866 NaN  2.298942 NaN  0.019998 NaN
                                     gsp                  1.222407 NaN  2.324572 NaN  0.019491 NaN
                                     historical_tod_mean  1.113512 NaN  2.278470 NaN  0.017748 NaN
                                     neighbor_average     2.944228 NaN  4.003725 NaN  0.046010 NaN
       coverage                      gls_map              1.242426 NaN  2.316718 NaN  0.019778 NaN
                                     gsp                  1.151322 NaN  2.274724 NaN  0.018429 NaN
                                     historical_tod_mean  1.089098 NaN  2.249371 NaN  0.017419 NaN
                                     neighbor_average     2.953984 NaN  4.011417 NaN  0.046189 NaN
       degree                        gls_map              1.219190 NaN  2.351286 NaN  0.019418 NaN
                                     gsp                  1.233214 NaN  2.334889 NaN  0.019623 NaN
                                     historical_tod_mean  1.144439 NaN  2.301117 NaN  0.018204 NaN
                                     neighbor_average     3.072846 NaN  4.384825 NaN  0.047911 NaN
       graph_sampling_laplacian      gls_map              1.192117 NaN  2.278245 NaN  0.018875 NaN
                                     gsp                  1.179978 NaN  2.263181 NaN  0.018661 NaN
                                     historical_tod_mean  1.080171 NaN  2.239368 NaN  0.017235 NaN
                                     neighbor_average     3.054959 NaN  4.216334 NaN  0.048119 NaN
       greedy_a_trace                gls_map              1.259283 NaN  2.344273 NaN  0.019982 NaN
                                     gsp                  1.133082 NaN  2.283216 NaN  0.018068 NaN
                                     historical_tod_mean  1.113890 NaN  2.278312 NaN  0.017746 NaN
                                     neighbor_average     2.867480 NaN  4.189747 NaN  0.044790 NaN
       greedy_d_logdet               gls_map              1.510034 NaN  2.470506 NaN  0.023708 NaN
                                     gsp                  1.154853 NaN  2.300086 NaN  0.018359 NaN
                                     historical_tod_mean  1.137000 NaN  2.295790 NaN  0.018065 NaN
                                     neighbor_average     2.754634 NaN  3.690738 NaN  0.042189 NaN
       multistart_swap_by_validation gls_map              1.206787 NaN  2.316523 NaN  0.019196 NaN
                                     gsp                  1.186023 NaN  2.307316 NaN  0.018885 NaN
                                     historical_tod_mean  1.145439 NaN  2.295078 NaN  0.018218 NaN
                                     neighbor_average     2.921138 NaN  4.224192 NaN  0.045686 NaN
       observability_proxy           gls_map              1.263357 NaN  2.340732 NaN  0.019842 NaN
                                     gsp                  1.133832 NaN  2.262366 NaN  0.017938 NaN
                                     historical_tod_mean  1.132073 NaN  2.262171 NaN  0.017908 NaN
                                     neighbor_average     2.863740 NaN  3.943235 NaN  0.043778 NaN
       qr_pod_modes                  gls_map              1.214142 NaN  2.343863 NaN  0.019344 NaN
                                     gsp                  1.170865 NaN  2.297386 NaN  0.018635 NaN
                                     historical_tod_mean  1.133854 NaN  2.286492 NaN  0.018025 NaN
                                     neighbor_average     2.780976 NaN  4.049850 NaN  0.042922 NaN
       random                        gls_map              1.255866 NaN  2.298942 NaN  0.019998 NaN
                                     gsp                  1.222407 NaN  2.324572 NaN  0.019491 NaN
                                     historical_tod_mean  1.113512 NaN  2.278470 NaN  0.017748 NaN
                                     neighbor_average     2.944228 NaN  4.003725 NaN  0.046010 NaN
       rcss_selected                 gls_map              1.251601 NaN  2.397251 NaN  0.019905 NaN
                                     gsp                  1.161566 NaN  2.304182 NaN  0.018492 NaN
                                     historical_tod_mean  1.118817 NaN  2.291663 NaN  0.017797 NaN
                                     neighbor_average     2.620488 NaN  3.740239 NaN  0.040884 NaN
       robust_coverage_cvar          gls_map              1.251601 NaN  2.397251 NaN  0.019905 NaN
                                     gsp                  1.161566 NaN  2.304182 NaN  0.018492 NaN
                                     historical_tod_mean  1.118817 NaN  2.291663 NaN  0.017797 NaN
                                     neighbor_average     2.620488 NaN  3.740239 NaN  0.040884 NaN
       scenario_average_a_trace      gls_map              1.255052 NaN  2.376380 NaN  0.019993 NaN
                                     gsp                  1.187199 NaN  2.306809 NaN  0.018919 NaN
                                     historical_tod_mean  1.119890 NaN  2.281907 NaN  0.017843 NaN
                                     neighbor_average     2.997236 NaN  4.204747 NaN  0.046812 NaN
       scenario_cvar_a_trace         gls_map              1.252236 NaN  2.377508 NaN  0.019896 NaN
                                     gsp                  1.190941 NaN  2.314899 NaN  0.018950 NaN
                                     historical_tod_mean  1.132256 NaN  2.296787 NaN  0.018008 NaN
                                     neighbor_average     2.754309 NaN  3.796692 NaN  0.042887 NaN
       swap_from_best_random_trace   gls_map              1.206787 NaN  2.316523 NaN  0.019196 NaN
                                     gsp                  1.186023 NaN  2.307316 NaN  0.018885 NaN
                                     historical_tod_mean  1.145439 NaN  2.295078 NaN  0.018218 NaN
                                     neighbor_average     2.921138 NaN  4.224192 NaN  0.045686 NaN
       swap_from_greedy_a_trace      gls_map              1.221296 NaN  2.311005 NaN  0.019364 NaN
                                     gsp                  1.130134 NaN  2.279586 NaN  0.018002 NaN
                                     historical_tod_mean  1.126415 NaN  2.278958 NaN  0.017938 NaN
                                     neighbor_average     3.107480 NaN  4.411681 NaN  0.048422 NaN
       swap_from_scenario_average    gls_map              1.368847 NaN  2.176536 NaN  0.021034 NaN
                                     gsp                  1.138023 NaN  2.153780 NaN  0.017805 NaN
                                     historical_tod_mean  1.082110 NaN  2.144139 NaN  0.017007 NaN
                                     neighbor_average     2.763577 NaN  3.698185 NaN  0.041903 NaN
       swap_from_scenario_cvar       gls_map              1.310301 NaN  2.289588 NaN  0.020600 NaN
                                     gsp                  1.129342 NaN  2.251726 NaN  0.017937 NaN
                                     historical_tod_mean  1.123793 NaN  2.252242 NaN  0.017860 NaN
                                     neighbor_average     3.209756 NaN  4.571491 NaN  0.049854 NaN
       top_variance                  gls_map              1.113218 NaN  2.263792 NaN  0.017833 NaN
                                     gsp                  1.064364 NaN  2.234997 NaN  0.017033 NaN
                                     historical_tod_mean  1.061220 NaN  2.235233 NaN  0.016988 NaN
                                     neighbor_average     2.993333 NaN  4.169507 NaN  0.047055 NaN
       validation_swap_selected      gls_map              1.249540 NaN  2.395327 NaN  0.019873 NaN
                                     gsp                  1.159206 NaN  2.303100 NaN  0.018454 NaN
                                     historical_tod_mean  1.121049 NaN  2.291886 NaN  0.017831 NaN
                                     neighbor_average     2.662927 NaN  3.753188 NaN  0.041472 NaN
```

## Best method per budget-layout row

```
 budget  layout_type              method     mae     rmse
    0.1 top_variance historical_tod_mean 1.06122 2.235233
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae  n
    gsp    posterior_trace    -0.107459     -0.208605 21
    gsp   condition_number     0.433584      0.203390 21
    gsp information_logdet    -0.229244     -0.528031 21
gls_map    posterior_trace     0.015929      0.002608 21
gls_map   condition_number     0.417134     -0.129074 21
gls_map information_logdet     0.687428      0.292047 21
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv