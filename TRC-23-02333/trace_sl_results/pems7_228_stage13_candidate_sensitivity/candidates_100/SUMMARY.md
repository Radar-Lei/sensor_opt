---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.2      validation_swap_selected 3.158137      NaN      1
    0.2                 rcss_selected 3.175395      NaN      1
    0.2                  top_variance 3.208909      NaN      1
    0.2   swap_from_best_random_trace 3.264642      NaN      1
    0.2     best_random_by_validation 3.316469      NaN      1
    0.2 multistart_swap_by_validation 3.316486      NaN      1
    0.2    swap_from_scenario_average 3.330990      NaN      1
    0.2      swap_from_greedy_a_trace 3.334105      NaN      1
    0.2                greedy_a_trace 3.336125      NaN      1
    0.2       swap_from_scenario_cvar 3.353092      NaN      1
    0.2                      coverage 3.416141      NaN      1
    0.2          robust_coverage_cvar 3.423059      NaN      1
    0.2                        random 3.444332 0.076274     50
    0.2          best_random_by_trace 3.454068      NaN      1
    0.2      scenario_average_a_trace 3.508072      NaN      1
    0.2         scenario_cvar_a_trace 3.527221      NaN      1
    0.2                        degree 3.829607      NaN      1
    0.2               greedy_d_logdet 3.913042      NaN      1
```

## RCSS deltas, negative is better

```
 budget  validation_swap_selected_minus_random_mean  validation_swap_selected_minus_random_std  validation_swap_selected_minus_best_random_by_validation_mean  validation_swap_selected_minus_best_random_by_validation_std  validation_swap_selected_minus_top_variance_mean  validation_swap_selected_minus_top_variance_std  validation_swap_selected_minus_greedy_a_trace_mean  validation_swap_selected_minus_greedy_a_trace_std  validation_swap_selected_minus_greedy_d_logdet_mean  validation_swap_selected_minus_greedy_d_logdet_std  validation_swap_selected_minus_scenario_cvar_a_trace_mean  validation_swap_selected_minus_scenario_cvar_a_trace_std  validation_swap_selected_minus_multistart_swap_by_validation_mean  validation_swap_selected_minus_multistart_swap_by_validation_std  validation_swap_selected_minus_swap_from_scenario_cvar_mean  validation_swap_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_greedy_d_logdet_mean  rcss_selected_minus_greedy_d_logdet_std  rcss_selected_minus_scenario_cvar_a_trace_mean  rcss_selected_minus_scenario_cvar_a_trace_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_greedy_d_logdet_mean  robust_coverage_cvar_minus_greedy_d_logdet_std  robust_coverage_cvar_minus_scenario_cvar_a_trace_mean  robust_coverage_cvar_minus_scenario_cvar_a_trace_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std
    0.2                                   -0.286195                                        NaN                                                      -0.158333                                                           NaN                                         -0.050772                                              NaN                                           -0.177989                                                NaN                                            -0.754906                                                 NaN                                                  -0.369085                                                       NaN                                                          -0.158349                                                               NaN                                                    -0.194955                                                         NaN                        -0.268937                             NaN                                           -0.141074                                                NaN                              -0.033513                                   NaN                                 -0.16073                                     NaN                                 -0.737647                                      NaN                                       -0.351826                                            NaN                                                -0.14109                                                    NaN                                         -0.177696                                              NaN                               -0.021273                                    NaN                                                   0.106589                                                       NaN                                       0.21415                                          NaN                                        0.086933                                            NaN                                        -0.489984                                             NaN                                              -0.104163                                                   NaN                                                       0.106573                                                           NaN                                                 0.069967                                                     NaN
```

## Winner counts

```
 budget              best_layout  wins
    0.2 validation_swap_selected     1
```

## Main ablation layouts

```
 budget                   layout_type     mean  std  count
    0.2      validation_swap_selected 3.158137  NaN      1
    0.2                 rcss_selected 3.175395  NaN      1
    0.2                  top_variance 3.208909  NaN      1
    0.2     best_random_by_validation 3.316469  NaN      1
    0.2 multistart_swap_by_validation 3.316486  NaN      1
    0.2                greedy_a_trace 3.336125  NaN      1
    0.2         scenario_cvar_a_trace 3.527221  NaN      1
    0.2               greedy_d_logdet 3.913042  NaN      1
```

## Paired delta tests

```
 budget                   layout                      baseline  delta_mean  delta_std delta_sem ci95_low ci95_high cohens_dz paired_t_p wilcoxon_p  win_count  count
    0.2 validation_swap_selected                        random   -0.286195        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected     best_random_by_validation   -0.158333        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected                  top_variance   -0.050772        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected                greedy_a_trace   -0.177989        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected               greedy_d_logdet   -0.754906        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected         scenario_cvar_a_trace   -0.369085        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected multistart_swap_by_validation   -0.158349        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected       swap_from_scenario_cvar   -0.194955        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                        random   -0.268937        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected     best_random_by_validation   -0.141074        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                  top_variance   -0.033513        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                greedy_a_trace   -0.160730        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected               greedy_d_logdet   -0.737647        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected         scenario_cvar_a_trace   -0.351826        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected multistart_swap_by_validation   -0.141090        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected       swap_from_scenario_cvar   -0.177696        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar                        random   -0.021273        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar     best_random_by_validation    0.106589        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar                  top_variance    0.214150        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar                greedy_a_trace    0.086933        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar               greedy_d_logdet   -0.489984        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar         scenario_cvar_a_trace   -0.104163        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar multistart_swap_by_validation    0.106573        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar       swap_from_scenario_cvar    0.069967        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
```

## Empirical certificate-error correlation summary

These correlations are empirical support for certificate-guided selection, not formal optimality guarantees.

```
                           pearson_mae                               spearman_mae                              
                                  mean std       min       max count         mean std       min       max count
method  certificate                                                                                            
gls_map condition_number      0.484680 NaN  0.484680  0.484680     1     0.231033 NaN  0.231033  0.231033     1
        information_logdet    0.125581 NaN  0.125581  0.125581     1     0.058227 NaN  0.058227  0.058227     1
        posterior_trace       0.177775 NaN  0.177775  0.177775     1     0.146267 NaN  0.146267  0.146267     1
gsp     condition_number     -0.053575 NaN -0.053575 -0.053575     1     0.008980 NaN  0.008980  0.008980     1
        information_logdet   -0.310342 NaN -0.310342 -0.310342     1    -0.306741 NaN -0.306741 -0.306741     1
        posterior_trace       0.205183 NaN  0.205183  0.205183     1     0.242248 NaN  0.242248  0.242248     1
```

## RCSS selected sources

```
 budget                  source  selected_count
    0.2 quality_coverage_sample               1
```

## Candidate-count sensitivity and practical tractability

Candidate-count sensitivity is summarized as practical tractability and selection stability evidence, not as a broad scalability claim.

### Candidate source and diagnostic stability

```
 budget                        source  candidate_row_count  selected_count  validation_mae_mean  validation_mae_std  selected_validation_mae_mean  selected_validation_mae_std  posterior_trace_mean  posterior_trace_std  selected_posterior_trace_mean  selected_posterior_trace_std  scenario_cvar_trace_mean  scenario_cvar_trace_std  selected_scenario_cvar_trace_mean  selected_scenario_cvar_trace_std  condition_number_mean  condition_number_std  selected_condition_number_mean  selected_condition_number_std  coverage_penalty_mean  coverage_penalty_std  selected_coverage_penalty_mean  selected_coverage_penalty_std  rcss_score_mean  rcss_score_std  selected_rcss_score_mean  selected_rcss_score_std
    0.2                      coverage                    1               0             3.806302                 NaN                           NaN                          NaN            304.991762                  NaN                            NaN                           NaN                211.563068                      NaN                                NaN                               NaN            1283.125553                   NaN                             NaN                            NaN               0.038631                   NaN                             NaN                            NaN         0.296684             NaN                       NaN                      NaN
    0.2                        degree                    1               0             4.201601                 NaN                           NaN                          NaN            345.528309                  NaN                            NaN                           NaN                252.758514                      NaN                                NaN                               NaN            1652.502374                   NaN                             NaN                            NaN               0.140011                   NaN                             NaN                            NaN         0.593106             NaN                       NaN                      NaN
    0.2                greedy_a_trace                    1               0             3.587372                 NaN                           NaN                          NaN            252.784716                  NaN                            NaN                           NaN                174.724202                      NaN                                NaN                               NaN             827.442907                   NaN                             NaN                            NaN               0.035484                   NaN                             NaN                            NaN         0.132516             NaN                       NaN                      NaN
    0.2               greedy_d_logdet                    1               0             4.744223                 NaN                           NaN                          NaN            285.708365                  NaN                            NaN                           NaN                197.797307                      NaN                                NaN                               NaN            2495.738822                   NaN                             NaN                            NaN               0.048895                   NaN                             NaN                            NaN         1.000000             NaN                       NaN                      NaN
    0.2 multistart_swap_by_validation                    1               0             3.492041                 NaN                           NaN                          NaN            252.225648                  NaN                            NaN                           NaN                176.217909                      NaN                                NaN                               NaN             825.787365                   NaN                             NaN                            NaN               0.035354                   NaN                             NaN                            NaN         0.061030             NaN                       NaN                      NaN
    0.2       quality_coverage_sample                  100               1             3.611623            0.088840                      3.410653                          NaN            300.727211             6.378758                     297.240828                           NaN                205.613661                11.310509                         204.191809                               NaN             964.883244            121.414985                      966.696086                            NaN               0.036449              0.001481                        0.038101                            NaN         0.150701        0.066618                       0.0                      NaN
    0.2        random_validation_pool                   50               0             3.704520            0.096977                           NaN                          NaN            300.077546             6.750216                            NaN                           NaN                202.321465                 9.394565                                NaN                               NaN             968.258371            144.233220                             NaN                            NaN               0.040840              0.003329                             NaN                            NaN         0.220362        0.072720                       NaN                      NaN
    0.2          robust_coverage_cvar                    1               0             3.572752                 NaN                           NaN                          NaN            276.625379                  NaN                            NaN                           NaN                136.506162                      NaN                                NaN                               NaN             847.092535                   NaN                             NaN                            NaN               0.032460                   NaN                             NaN                            NaN         0.121553             NaN                       NaN                      NaN
    0.2      scenario_average_a_trace                    1               0             3.715095                 NaN                           NaN                          NaN            276.606804                  NaN                            NaN                           NaN                135.610404                      NaN                                NaN                               NaN             843.376774                   NaN                             NaN                            NaN               0.038633                   NaN                             NaN                            NaN         0.228291             NaN                       NaN                      NaN
    0.2         scenario_cvar_a_trace                    1               0             3.709168                 NaN                           NaN                          NaN            280.127282                  NaN                            NaN                           NaN                132.649550                      NaN                                NaN                               NaN             796.919542                   NaN                             NaN                            NaN               0.046398                   NaN                             NaN                            NaN         0.223847             NaN                       NaN                      NaN
    0.2   swap_from_best_random_trace                    1               0             3.541852                 NaN                           NaN                          NaN            252.579331                  NaN                            NaN                           NaN                173.198913                      NaN                                NaN                               NaN             861.619384                   NaN                             NaN                            NaN               0.036964                   NaN                             NaN                            NaN         0.098382             NaN                       NaN                      NaN
    0.2      swap_from_greedy_a_trace                    1               0             3.577630                 NaN                           NaN                          NaN            249.306393                  NaN                            NaN                           NaN                178.425470                      NaN                                NaN                               NaN             854.546557                   NaN                             NaN                            NaN               0.035231                   NaN                             NaN                            NaN         0.125211             NaN                       NaN                      NaN
    0.2    swap_from_scenario_average                    1               0             3.620579                 NaN                           NaN                          NaN            251.116887                  NaN                            NaN                           NaN                172.161338                      NaN                                NaN                               NaN             850.139037                   NaN                             NaN                            NaN               0.037729                   NaN                             NaN                            NaN         0.157417             NaN                       NaN                      NaN
    0.2       swap_from_scenario_cvar                    1               0             3.504293                 NaN                           NaN                          NaN            252.207840                  NaN                            NaN                           NaN                172.418704                      NaN                                NaN                               NaN             843.817608                   NaN                             NaN                            NaN               0.036401                   NaN                             NaN                            NaN         0.070218             NaN                       NaN                      NaN
    0.2                  top_variance                    1               0             3.662078                 NaN                           NaN                          NaN            365.345975                  NaN                            NaN                           NaN                270.485533                      NaN                                NaN                               NaN            1514.637683                   NaN                             NaN                            NaN               0.060086                   NaN                             NaN                            NaN         0.188535             NaN                       NaN                      NaN
    0.2               validation_swap                    3               0             3.302896            0.009881                           NaN                          NaN            297.798219             6.107605                            NaN                           NaN                200.767057                 3.680426                                NaN                               NaN             973.076545            181.526273                             NaN                            NaN               0.037199              0.002851                             NaN                            NaN         0.584233        0.520851                       NaN                      NaN
```

### Runtime / tractability evidence

No measured timing artifact was present in these inputs, so EXP-06 runtime closure must come from Stage 13 measured outputs.

## Output files

- combined_metrics.csv
- gls_map_layout_summary.csv
- gls_map_delta_summary.csv
- gls_map_paired_delta_tests.csv
- gls_map_ablation_summary.csv
- gls_map_per_split_winners.csv
- gls_map_win_counts.csv
- combined_certificate_correlations.csv
- certificate_correlation_summary.csv
- combined_rcss_candidates.csv
- rcss_selected_sources.csv
- candidate_sensitivity_summary.csv