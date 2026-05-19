---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.1   swap_from_best_random_trace 3.457137 0.195611      5
    0.1 multistart_swap_by_validation 3.461418 0.213635      5
    0.1      swap_from_greedy_a_trace 3.478960 0.225728      5
    0.1                 rcss_selected 3.483278 0.210160      5
    0.1    swap_from_scenario_average 3.485199 0.220688      5
    0.1       swap_from_scenario_cvar 3.501861 0.204773      5
    0.1         scenario_cvar_a_trace 3.503011 0.204385      5
    0.1                greedy_a_trace 3.540162 0.256561      5
    0.1          robust_coverage_cvar 3.548330 0.211797      5
    0.1     best_random_by_validation 3.567737 0.163324      5
    0.1                  top_variance 3.577951 0.242033      5
    0.1          best_random_by_trace 3.578889 0.162565      5
    0.1      scenario_average_a_trace 3.580944 0.229320      5
    0.1                        random 3.706717 0.210997   1000
    0.1                      coverage 3.808209 0.264816      5
    0.1                        degree 3.992988 0.234421      5
    0.1               greedy_d_logdet 4.302957 0.508004      5
    0.2 multistart_swap_by_validation 3.284701 0.213344      5
    0.2     best_random_by_validation 3.300467 0.213476      5
    0.2                  top_variance 3.318824 0.271250      5
    0.2                 rcss_selected 3.320581 0.203046      5
    0.2      swap_from_greedy_a_trace 3.328638 0.186602      5
    0.2   swap_from_best_random_trace 3.330276 0.183177      5
    0.2    swap_from_scenario_average 3.346354 0.228773      5
    0.2       swap_from_scenario_cvar 3.354106 0.221439      5
    0.2                greedy_a_trace 3.357878 0.206507      5
    0.2          robust_coverage_cvar 3.362810 0.210981      5
    0.2      scenario_average_a_trace 3.382347 0.204260      5
    0.2         scenario_cvar_a_trace 3.384566 0.227223      5
    0.2                        random 3.466809 0.195763   1000
    0.2          best_random_by_trace 3.499188 0.217860      5
    0.2                      coverage 3.528291 0.256392      5
    0.2                        degree 3.945454 0.255767      5
    0.2               greedy_d_logdet 4.000078 0.335024      5
    0.3                  top_variance 3.098213 0.206437      5
    0.3     best_random_by_validation 3.134493 0.141287      5
    0.3                 rcss_selected 3.158167 0.199403      5
    0.3 multistart_swap_by_validation 3.168685 0.197442      5
    0.3          robust_coverage_cvar 3.210966 0.221084      5
    0.3      scenario_average_a_trace 3.224780 0.180439      5
    0.3   swap_from_best_random_trace 3.229695 0.224504      5
    0.3    swap_from_scenario_average 3.246956 0.192258      5
    0.3         scenario_cvar_a_trace 3.254805 0.206696      5
    0.3                greedy_a_trace 3.260017 0.198208      5
    0.3       swap_from_scenario_cvar 3.266091 0.207672      5
    0.3      swap_from_greedy_a_trace 3.272410 0.188745      5
    0.3                      coverage 3.278006 0.193252      5
    0.3                        random 3.309539 0.189240   1000
    0.3          best_random_by_trace 3.396749 0.207022      5
    0.3               greedy_d_logdet 3.720418 0.273548      5
    0.3                        degree 3.806697 0.256169      5
```

## RCSS deltas, negative is better

```
 budget  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std
    0.1                        -0.223439                        0.041887                                           -0.084459                                           0.057859                                -0.056884                                0.052721                                         -0.018582                                         0.037889                                                0.021861                                               0.041177                              -0.094673                              0.074608                               -0.158386                               0.039217                                                  -0.019406                                                  0.053686                                        0.008168                                       0.053087                                                 0.046470                                                0.030889                                                       0.086913                                                      0.042807                                     -0.029620                                     0.072704
    0.2                        -0.146228                        0.058567                                            0.020114                                           0.034810                                -0.037297                                0.043466                                         -0.033525                                         0.021575                                                0.035880                                               0.051963                               0.001758                              0.112960                               -0.104000                               0.038360                                                   0.062342                                                  0.038468                                        0.004932                                       0.032007                                                 0.008704                                                0.042003                                                       0.078109                                                      0.037477                                      0.043986                                     0.094649
    0.3                        -0.151371                        0.029403                                            0.023674                                           0.083707                                -0.101850                                0.023929                                         -0.107924                                         0.047172                                               -0.010518                                               0.021880                               0.059954                              0.085703                               -0.098572                               0.066572                                                   0.076473                                                  0.119543                                       -0.049051                                       0.068769                                                -0.055125                                                0.084344                                                       0.042281                                                      0.065731                                      0.112753                                     0.085713
```

## Winner counts

```
 budget                   best_layout  wins
    0.1 multistart_swap_by_validation     1
    0.1         scenario_cvar_a_trace     1
    0.1   swap_from_best_random_trace     1
    0.1      swap_from_greedy_a_trace     1
    0.1    swap_from_scenario_average     1
    0.2 multistart_swap_by_validation     2
    0.2                        random     2
    0.2                  top_variance     1
    0.3                        random     3
    0.3                  top_variance     2
```

## Certificate stability

```
                           pearson_mae                               spearman_mae
                                  mean       std       min       max         mean       std       min       max
method  certificate
gls_map condition_number      0.830133  0.011700  0.810769  0.839850     0.861755  0.011867  0.844675  0.877012
        information_logdet   -0.822070  0.021349 -0.849052 -0.794468    -0.817889  0.012945 -0.837900 -0.808307
        posterior_trace       0.860581  0.016164  0.845192  0.882685     0.861392  0.011028  0.845714  0.875206
gsp     condition_number      0.151676  0.141613 -0.082578  0.273671     0.148756  0.146829 -0.099732  0.267256
        information_logdet   -0.169138  0.138566 -0.287419  0.063399    -0.190212  0.135030 -0.303984  0.040716
        posterior_trace       0.149772  0.141572 -0.084548  0.272371     0.166052  0.144472 -0.079955  0.293636
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.1                greedy_a_trace               1
    0.1 multistart_swap_by_validation               1
    0.1      swap_from_greedy_a_trace               2
    0.1    swap_from_scenario_average               1
    0.2 multistart_swap_by_validation               3
    0.2         scenario_cvar_a_trace               1
    0.2   swap_from_best_random_trace               1
    0.3 multistart_swap_by_validation               2
    0.3        random_validation_pool               1
    0.3          robust_coverage_cvar               2
```

## Output files

- combined_metrics.csv
- gls_map_layout_summary.csv
- gls_map_delta_summary.csv
- gls_map_per_split_winners.csv
- gls_map_win_counts.csv
- combined_rcss_candidates.csv
- rcss_selected_sources.csv