---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.2      validation_swap_selected 3.192964 0.040215      4
    0.2                 rcss_selected 3.196538 0.024413      4
    0.2                  top_variance 3.208909 0.000000      4
    0.2 multistart_swap_by_validation 3.267083 0.057045      4
    0.2   swap_from_best_random_trace 3.315785 0.059055      4
    0.2    swap_from_scenario_average 3.330990 0.000000      4
    0.2     best_random_by_validation 3.331097 0.016891      4
    0.2      swap_from_greedy_a_trace 3.334105 0.000000      4
    0.2                greedy_a_trace 3.336125 0.000000      4
    0.2       swap_from_scenario_cvar 3.353092 0.000000      4
    0.2                      coverage 3.416141 0.000000      4
    0.2          robust_coverage_cvar 3.423059 0.000000      4
    0.2                        random 3.442265 0.080058    200
    0.2          best_random_by_trace 3.486994 0.038020      4
    0.2      scenario_average_a_trace 3.508072 0.000000      4
    0.2         scenario_cvar_a_trace 3.527221 0.000000      4
    0.2                        degree 3.829607 0.000000      4
    0.2               greedy_d_logdet 3.913042 0.000000      4
```

## RCSS deltas, negative is better

```
 budget  validation_swap_selected_minus_random_mean  validation_swap_selected_minus_random_std  validation_swap_selected_minus_best_random_by_validation_mean  validation_swap_selected_minus_best_random_by_validation_std  validation_swap_selected_minus_top_variance_mean  validation_swap_selected_minus_top_variance_std  validation_swap_selected_minus_greedy_a_trace_mean  validation_swap_selected_minus_greedy_a_trace_std  validation_swap_selected_minus_greedy_d_logdet_mean  validation_swap_selected_minus_greedy_d_logdet_std  validation_swap_selected_minus_scenario_cvar_a_trace_mean  validation_swap_selected_minus_scenario_cvar_a_trace_std  validation_swap_selected_minus_multistart_swap_by_validation_mean  validation_swap_selected_minus_multistart_swap_by_validation_std  validation_swap_selected_minus_swap_from_scenario_cvar_mean  validation_swap_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_greedy_d_logdet_mean  rcss_selected_minus_greedy_d_logdet_std  rcss_selected_minus_scenario_cvar_a_trace_mean  rcss_selected_minus_scenario_cvar_a_trace_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_greedy_d_logdet_mean  robust_coverage_cvar_minus_greedy_d_logdet_std  robust_coverage_cvar_minus_scenario_cvar_a_trace_mean  robust_coverage_cvar_minus_scenario_cvar_a_trace_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std
    0.2                                     -0.2493                                        NaN                                                      -0.138133                                                           NaN                                         -0.015945                                              NaN                                           -0.143161                                                NaN                                            -0.720078                                                 NaN                                                  -0.334257                                                       NaN                                                          -0.074119                                                               NaN                                                    -0.160127                                                         NaN                        -0.245727                             NaN                                           -0.134559                                                NaN                              -0.012371                                   NaN                                -0.139587                                     NaN                                 -0.716504                                      NaN                                       -0.330683                                            NaN                                               -0.070545                                                    NaN                                         -0.156554                                              NaN                               -0.019206                                    NaN                                                   0.091961                                                       NaN                                       0.21415                                          NaN                                        0.086933                                            NaN                                        -0.489984                                             NaN                                              -0.104163                                                   NaN                                                       0.155976                                                           NaN                                                 0.069967                                                     NaN
```

## Winner counts

```
 budget              best_layout  wins
    0.2 validation_swap_selected     1
```

## Main ablation layouts

```
 budget                   layout_type     mean      std  count
    0.2      validation_swap_selected 3.192964 0.040215      4
    0.2                 rcss_selected 3.196538 0.024413      4
    0.2                  top_variance 3.208909 0.000000      4
    0.2 multistart_swap_by_validation 3.267083 0.057045      4
    0.2     best_random_by_validation 3.331097 0.016891      4
    0.2                greedy_a_trace 3.336125 0.000000      4
    0.2         scenario_cvar_a_trace 3.527221 0.000000      4
    0.2               greedy_d_logdet 3.913042 0.000000      4
```

## Paired delta tests

```
 budget                   layout                      baseline  delta_mean  delta_std delta_sem ci95_low ci95_high cohens_dz paired_t_p wilcoxon_p  win_count  count
    0.2 validation_swap_selected                        random   -0.249300        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected     best_random_by_validation   -0.138133        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected                  top_variance   -0.015945        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected                greedy_a_trace   -0.143161        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected               greedy_d_logdet   -0.720078        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected         scenario_cvar_a_trace   -0.334257        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected multistart_swap_by_validation   -0.074119        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected       swap_from_scenario_cvar   -0.160127        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                        random   -0.245727        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected     best_random_by_validation   -0.134559        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                  top_variance   -0.012371        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                greedy_a_trace   -0.139587        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected               greedy_d_logdet   -0.716504        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected         scenario_cvar_a_trace   -0.330683        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected multistart_swap_by_validation   -0.070545        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected       swap_from_scenario_cvar   -0.156554        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar                        random   -0.019206        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar     best_random_by_validation    0.091961        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar                  top_variance    0.214150        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar                greedy_a_trace    0.086933        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar               greedy_d_logdet   -0.489984        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar         scenario_cvar_a_trace   -0.104163        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar multistart_swap_by_validation    0.155976        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar       swap_from_scenario_cvar    0.069967        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
```

## Empirical certificate-error correlation summary

These correlations are empirical support for certificate-guided selection, not formal optimality guarantees.

```
                           pearson_mae                                     spearman_mae                                    
                                  mean       std       min       max count         mean       std       min       max count
method  certificate                                                                                                        
gls_map condition_number      0.514728  0.034696  0.484680  0.544775     4     0.279775  0.056283  0.231033  0.328518     4
        information_logdet    0.080851  0.051650  0.036121  0.125581     4    -0.008771  0.077363 -0.075769  0.058227     4
        posterior_trace       0.219793  0.048518  0.177775  0.261811     4     0.154100  0.009046  0.146267  0.161934     4
gsp     condition_number      0.023495  0.088993 -0.053575  0.100566     4     0.062768  0.062110  0.008980  0.116557     4
        information_logdet   -0.288331  0.025416 -0.310342 -0.266320     4    -0.251578  0.063696 -0.306741 -0.196416     4
        posterior_trace       0.186311  0.021792  0.167439  0.205183     4     0.216259  0.030009  0.190270  0.242248     4
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.2 multistart_swap_by_validation               2
    0.2       quality_coverage_sample               2
```

## Candidate-count sensitivity and practical tractability

Candidate-count sensitivity is summarized as practical tractability and selection stability evidence, not as a broad scalability claim.

### Candidate source and diagnostic stability

```
 budget                        source  candidate_row_count  selected_count  validation_mae_mean  validation_mae_std  selected_validation_mae_mean  selected_validation_mae_std  posterior_trace_mean  posterior_trace_std  selected_posterior_trace_mean  selected_posterior_trace_std  scenario_cvar_trace_mean  scenario_cvar_trace_std  selected_scenario_cvar_trace_mean  selected_scenario_cvar_trace_std  condition_number_mean  condition_number_std  selected_condition_number_mean  selected_condition_number_std  coverage_penalty_mean  coverage_penalty_std  selected_coverage_penalty_mean  selected_coverage_penalty_std  rcss_score_mean  rcss_score_std  selected_rcss_score_mean  selected_rcss_score_std
    0.2                      coverage                    4               0             3.806302            0.000000                           NaN                          NaN            304.991762             0.000000                            NaN                           NaN                211.563068                 0.000000                                NaN                               NaN            1283.125553              0.000000                             NaN                            NaN               0.038631              0.000000                             NaN                            NaN         0.286147        0.012167                       NaN                      NaN
    0.2                        degree                    4               0             4.201601            0.000000                           NaN                          NaN            345.528309             0.000000                            NaN                           NaN                252.758514                 0.000000                                NaN                               NaN            1652.502374              0.000000                             NaN                            NaN               0.140011              0.000000                             NaN                            NaN         0.587010        0.007039                       NaN                      NaN
    0.2                greedy_a_trace                    4               0             3.587372            0.000000                           NaN                          NaN            252.784716             0.000000                            NaN                           NaN                174.724202                 0.000000                                NaN                               NaN             827.442907              0.000000                             NaN                            NaN               0.035484              0.000000                             NaN                            NaN         0.119519        0.015007                       NaN                      NaN
    0.2               greedy_d_logdet                    4               0             4.744223            0.000000                           NaN                          NaN            285.708365             0.000000                            NaN                           NaN                197.797307                 0.000000                                NaN                               NaN            2495.738822              0.000000                             NaN                            NaN               0.048895              0.000000                             NaN                            NaN         1.000000        0.000000                       NaN                      NaN
    0.2 multistart_swap_by_validation                    4               2             3.470745            0.024590                      3.449450                          0.0            254.380524             2.488236                     256.535399                           0.0                178.643147                 2.800424                         181.068385                               0.0             796.063386             34.322295                      766.339406                            0.0               0.035527              0.000200                        0.035700                            0.0         0.030515        0.035236                       0.0                      0.0
    0.2       quality_coverage_sample                  300               2             3.612398            0.086041                      3.410653                          0.0            301.205750             6.231567                     297.240828                           0.0                206.113820                11.600312                         204.191809                               0.0             971.910280            118.936785                      966.696086                            0.0               0.036360              0.001479                        0.038101                            0.0         0.142817        0.066040                       0.0                      0.0
    0.2        random_validation_pool                  200               0             3.715874            0.101759                           NaN                          NaN            299.935050             6.469076                            NaN                           NaN                201.243078                 9.983129                                NaN                               NaN             952.723545            137.836052                             NaN                            NaN               0.041058              0.003616                             NaN                            NaN         0.217450        0.077133                       NaN                      NaN
    0.2          robust_coverage_cvar                    4               0             3.572752            0.000000                           NaN                          NaN            276.625379             0.000000                            NaN                           NaN                136.506162                 0.000000                                NaN                               NaN             847.092535              0.000000                             NaN                            NaN               0.032460              0.000000                             NaN                            NaN         0.108392        0.015197                       NaN                      NaN
    0.2      scenario_average_a_trace                    4               0             3.715095            0.000000                           NaN                          NaN            276.606804             0.000000                            NaN                           NaN                135.610404                 0.000000                                NaN                               NaN             843.376774              0.000000                             NaN                            NaN               0.038633              0.000000                             NaN                            NaN         0.216729        0.013351                       NaN                      NaN
    0.2         scenario_cvar_a_trace                    4               0             3.709168            0.000000                           NaN                          NaN            280.127282             0.000000                            NaN                           NaN                132.649550                 0.000000                                NaN                               NaN             796.919542              0.000000                             NaN                            NaN               0.046398              0.000000                             NaN                            NaN         0.212218        0.013427                       NaN                      NaN
    0.2   swap_from_best_random_trace                    4               0             3.608221            0.076637                           NaN                          NaN            253.537999             1.106974                            NaN                           NaN                173.670453                 0.544487                                NaN                               NaN             859.438138              2.518685                             NaN                            NaN               0.036032              0.001077                             NaN                            NaN         0.136133        0.043592                       NaN                      NaN
    0.2      swap_from_greedy_a_trace                    4               0             3.577630            0.000000                           NaN                          NaN            249.306393             0.000000                            NaN                           NaN                178.425470                 0.000000                                NaN                               NaN             854.546557              0.000000                             NaN                            NaN               0.035231              0.000000                             NaN                            NaN         0.112105        0.015134                       NaN                      NaN
    0.2    swap_from_scenario_average                    4               0             3.620579            0.000000                           NaN                          NaN            251.116887             0.000000                            NaN                           NaN                172.161338                 0.000000                                NaN                               NaN             850.139037              0.000000                             NaN                            NaN               0.037729              0.000000                             NaN                            NaN         0.144793        0.014577                       NaN                      NaN
    0.2       swap_from_scenario_cvar                    4               0             3.504293            0.000000                           NaN                          NaN            252.207840             0.000000                            NaN                           NaN                172.418704                 0.000000                                NaN                               NaN             843.817608              0.000000                             NaN                            NaN               0.036401              0.000000                             NaN                            NaN         0.056288        0.016085                       NaN                      NaN
    0.2                  top_variance                    4               0             3.662078            0.000000                           NaN                          NaN            365.345975             0.000000                            NaN                           NaN                270.485533                 0.000000                                NaN                               NaN            1514.637683              0.000000                             NaN                            NaN               0.060086              0.000000                             NaN                            NaN         0.176378        0.014038                       NaN                      NaN
    0.2               validation_swap                   12               0             3.335077            0.038749                           NaN                          NaN            291.442066            15.352166                            NaN                           NaN                199.471894                 5.357176                                NaN                               NaN             970.530347            180.936748                             NaN                            NaN               0.037267              0.001826                             NaN                            NaN         0.488552        0.460506                       NaN                      NaN
```

### Measured runtime / tractability evidence

```
 candidate_count   status  runtime_seconds  std  min  max  count
              50 complete             71.0  0.0   71   71      2
             100 complete             69.0  0.0   69   69      2
```

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
- runtime_candidate_sensitivity.csv