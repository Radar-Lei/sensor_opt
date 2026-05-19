---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.1       swap_from_scenario_cvar 3.372469 0.042099      5
    0.1 multistart_swap_by_validation 3.377142 0.101328      5
    0.1                 rcss_selected 3.377142 0.101328      5
    0.1   swap_from_best_random_trace 3.398849 0.105633      5
    0.1      swap_from_greedy_a_trace 3.412826 0.131512      5
    0.1                greedy_a_trace 3.440722 0.105644      5
    0.1    swap_from_scenario_average 3.442661 0.089378      5
    0.1         scenario_cvar_a_trace 3.459142 0.085022      5
    0.1          robust_coverage_cvar 3.460024 0.099352      5
    0.1          best_random_by_trace 3.463084 0.076731      5
    0.1                  top_variance 3.493043 0.097953      5
    0.1     best_random_by_validation 3.497601 0.125110      5
    0.1      scenario_average_a_trace 3.512178 0.112309      5
    0.1                        random 3.603940 0.118420   1000
    0.1                      coverage 3.715243 0.128354      5
    0.1                        degree 3.959334 0.160237      5
    0.1               greedy_d_logdet 4.340139 0.348030      5
    0.2 multistart_swap_by_validation 3.223117 0.074434      5
    0.2                 rcss_selected 3.227016 0.076495      5
    0.2                  top_variance 3.229828 0.141165      5
    0.2     best_random_by_validation 3.230318 0.094159      5
    0.2                greedy_a_trace 3.237308 0.078358      5
    0.2   swap_from_best_random_trace 3.241641 0.099994      5
    0.2      swap_from_greedy_a_trace 3.245650 0.084935      5
    0.2          robust_coverage_cvar 3.251668 0.090075      5
    0.2       swap_from_scenario_cvar 3.256805 0.081937      5
    0.2         scenario_cvar_a_trace 3.257865 0.083087      5
    0.2    swap_from_scenario_average 3.277387 0.074242      5
    0.2      scenario_average_a_trace 3.298777 0.126871      5
    0.2                        random 3.382680 0.110145   1000
    0.2                      coverage 3.432801 0.112142      5
    0.2          best_random_by_trace 3.441952 0.128409      5
    0.2                        degree 3.868993 0.169360      5
    0.2               greedy_d_logdet 4.039084 0.284304      5
    0.3     best_random_by_validation 3.035571 0.047879      5
    0.3                 rcss_selected 3.046615 0.059134      5
    0.3                  top_variance 3.053434 0.125164      5
    0.3 multistart_swap_by_validation 3.061071 0.061415      5
    0.3         scenario_cvar_a_trace 3.097043 0.075180      5
    0.3          robust_coverage_cvar 3.112031 0.092951      5
    0.3       swap_from_scenario_cvar 3.117451 0.108215      5
    0.3   swap_from_best_random_trace 3.127791 0.101916      5
    0.3                greedy_a_trace 3.131481 0.079994      5
    0.3    swap_from_scenario_average 3.138910 0.106436      5
    0.3      scenario_average_a_trace 3.154179 0.066689      5
    0.3      swap_from_greedy_a_trace 3.161523 0.105184      5
    0.3                      coverage 3.210594 0.057290      5
    0.3                        random 3.241932 0.112091   1000
    0.3          best_random_by_trace 3.333494 0.087290      5
    0.3               greedy_d_logdet 3.637190 0.155435      5
    0.3                        degree 3.742602 0.166955      5
```

## RCSS deltas, negative is better

```
 budget  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std
    0.1                        -0.226798                        0.019454                                           -0.120459                                           0.107702                                -0.063580                                0.030832                                          0.004673                                         0.067531                                                0.000000                                               0.000000                              -0.115901                              0.070013                               -0.143916                               0.041347                                                  -0.037577                                                  0.112584                                        0.019302                                       0.052091                                                 0.087555                                                0.084009                                                       0.082882                                                      0.050138                                     -0.033019                                     0.091709
    0.2                        -0.155664                        0.018650                                           -0.003301                                           0.039960                                -0.010292                                0.039839                                         -0.029788                                         0.041766                                                0.003900                                               0.008720                              -0.002812                              0.082928                               -0.131013                               0.027811                                                   0.021350                                                  0.051203                                        0.014360                                       0.025354                                                -0.005137                                                0.027200                                                       0.028551                                                      0.045584                                      0.021840                                     0.075672
    0.3                        -0.195317                        0.055453                                            0.011044                                           0.072304                                -0.084866                                0.065412                                         -0.070836                                         0.074080                                               -0.014456                                               0.032325                              -0.006819                              0.106502                               -0.129902                               0.025200                                                   0.076460                                                  0.082260                                       -0.019450                                       0.035656                                                -0.005420                                                0.027503                                                       0.050959                                                      0.092679                                      0.058597                                     0.088542
```

## Winner counts

```
 budget                   best_layout  wins
    0.1 multistart_swap_by_validation     1
    0.1      swap_from_greedy_a_trace     1
    0.1       swap_from_scenario_cvar     3
    0.2                        random     3
    0.2                  top_variance     2
    0.3 multistart_swap_by_validation     1
    0.3                        random     2
    0.3   swap_from_best_random_trace     1
    0.3                  top_variance     1
```

## Certificate stability

```
                           pearson_mae                               spearman_mae
                                  mean       std       min       max         mean       std       min       max
method  certificate
gls_map condition_number      0.821071  0.008244  0.811175  0.829945     0.851824  0.009486  0.843754  0.862335
        information_logdet   -0.803159  0.021556 -0.824928 -0.772033    -0.806246  0.007757 -0.817503 -0.796859
        posterior_trace       0.845427  0.017141  0.821020  0.866873     0.853942  0.006653  0.847137  0.862524
gsp     condition_number      0.187872  0.130238  0.003362  0.363964     0.183496  0.124466  0.002848  0.347654
        information_logdet   -0.204646  0.122687 -0.367252 -0.027449    -0.235641  0.112680 -0.385053 -0.071214
        posterior_trace       0.186330  0.130506  0.001012  0.362063     0.215823  0.117460  0.044099  0.355652
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.1 multistart_swap_by_validation               4
    0.1   swap_from_best_random_trace               1
    0.2 multistart_swap_by_validation               4
    0.2   swap_from_best_random_trace               1
    0.3 multistart_swap_by_validation               4
    0.3          robust_coverage_cvar               1
```

## Output files

- combined_metrics.csv
- gls_map_layout_summary.csv
- gls_map_delta_summary.csv
- gls_map_per_split_winners.csv
- gls_map_win_counts.csv
- combined_rcss_candidates.csv
- rcss_selected_sources.csv