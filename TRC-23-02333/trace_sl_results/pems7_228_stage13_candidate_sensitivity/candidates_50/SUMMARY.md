---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.2                  top_variance 3.208909      NaN      1
    0.2 multistart_swap_by_validation 3.217681      NaN      1
    0.2                 rcss_selected 3.217681      NaN      1
    0.2      validation_swap_selected 3.227792      NaN      1
    0.2    swap_from_scenario_average 3.330990      NaN      1
    0.2      swap_from_greedy_a_trace 3.334105      NaN      1
    0.2                greedy_a_trace 3.336125      NaN      1
    0.2     best_random_by_validation 3.345725      NaN      1
    0.2       swap_from_scenario_cvar 3.353092      NaN      1
    0.2   swap_from_best_random_trace 3.366928      NaN      1
    0.2                      coverage 3.416141      NaN      1
    0.2          robust_coverage_cvar 3.423059      NaN      1
    0.2                        random 3.440197 0.084784     50
    0.2      scenario_average_a_trace 3.508072      NaN      1
    0.2          best_random_by_trace 3.519920      NaN      1
    0.2         scenario_cvar_a_trace 3.527221      NaN      1
    0.2                        degree 3.829607      NaN      1
    0.2               greedy_d_logdet 3.913042      NaN      1
```

## RCSS deltas, negative is better

```
 budget  validation_swap_selected_minus_random_mean  validation_swap_selected_minus_random_std  validation_swap_selected_minus_best_random_by_validation_mean  validation_swap_selected_minus_best_random_by_validation_std  validation_swap_selected_minus_top_variance_mean  validation_swap_selected_minus_top_variance_std  validation_swap_selected_minus_greedy_a_trace_mean  validation_swap_selected_minus_greedy_a_trace_std  validation_swap_selected_minus_greedy_d_logdet_mean  validation_swap_selected_minus_greedy_d_logdet_std  validation_swap_selected_minus_scenario_cvar_a_trace_mean  validation_swap_selected_minus_scenario_cvar_a_trace_std  validation_swap_selected_minus_multistart_swap_by_validation_mean  validation_swap_selected_minus_multistart_swap_by_validation_std  validation_swap_selected_minus_swap_from_scenario_cvar_mean  validation_swap_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_greedy_d_logdet_mean  rcss_selected_minus_greedy_d_logdet_std  rcss_selected_minus_scenario_cvar_a_trace_mean  rcss_selected_minus_scenario_cvar_a_trace_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_greedy_d_logdet_mean  robust_coverage_cvar_minus_greedy_d_logdet_std  robust_coverage_cvar_minus_scenario_cvar_a_trace_mean  robust_coverage_cvar_minus_scenario_cvar_a_trace_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std
    0.2                                   -0.212405                                        NaN                                                      -0.117934                                                           NaN                                          0.018883                                              NaN                                           -0.108334                                                NaN                                            -0.685251                                                 NaN                                                   -0.29943                                                       NaN                                                           0.010111                                                               NaN                                                      -0.1253                                                         NaN                        -0.222516                             NaN                                           -0.128045                                                NaN                               0.008772                                   NaN                                -0.118445                                     NaN                                 -0.695362                                      NaN                                       -0.309541                                            NaN                                                     0.0                                                    NaN                                         -0.135411                                              NaN                               -0.017138                                    NaN                                                   0.077334                                                       NaN                                       0.21415                                          NaN                                        0.086933                                            NaN                                        -0.489984                                             NaN                                              -0.104163                                                   NaN                                                       0.205378                                                           NaN                                                 0.069967                                                     NaN
```

## Winner counts

```
 budget  best_layout  wins
    0.2 top_variance     1
```

## Main ablation layouts

```
 budget                   layout_type     mean  std  count
    0.2                  top_variance 3.208909  NaN      1
    0.2 multistart_swap_by_validation 3.217681  NaN      1
    0.2                 rcss_selected 3.217681  NaN      1
    0.2      validation_swap_selected 3.227792  NaN      1
    0.2                greedy_a_trace 3.336125  NaN      1
    0.2     best_random_by_validation 3.345725  NaN      1
    0.2         scenario_cvar_a_trace 3.527221  NaN      1
    0.2               greedy_d_logdet 3.913042  NaN      1
```

## Paired delta tests

```
 budget                   layout                      baseline  delta_mean  delta_std delta_sem ci95_low ci95_high cohens_dz paired_t_p wilcoxon_p  win_count  count
    0.2 validation_swap_selected                        random   -0.212405        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected     best_random_by_validation   -0.117934        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected                  top_variance    0.018883        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2 validation_swap_selected                greedy_a_trace   -0.108334        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected               greedy_d_logdet   -0.685251        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected         scenario_cvar_a_trace   -0.299430        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2 validation_swap_selected multistart_swap_by_validation    0.010111        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2 validation_swap_selected       swap_from_scenario_cvar   -0.125300        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                        random   -0.222516        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected     best_random_by_validation   -0.128045        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected                  top_variance    0.008772        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2            rcss_selected                greedy_a_trace   -0.118445        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected               greedy_d_logdet   -0.695362        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected         scenario_cvar_a_trace   -0.309541        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2            rcss_selected multistart_swap_by_validation    0.000000        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2            rcss_selected       swap_from_scenario_cvar   -0.135411        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar                        random   -0.017138        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar     best_random_by_validation    0.077334        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar                  top_variance    0.214150        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar                greedy_a_trace    0.086933        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar               greedy_d_logdet   -0.489984        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar         scenario_cvar_a_trace   -0.104163        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          1      1
    0.2     robust_coverage_cvar multistart_swap_by_validation    0.205378        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
    0.2     robust_coverage_cvar       swap_from_scenario_cvar    0.069967        NaN      <NA>     <NA>      <NA>      <NA>       <NA>       <NA>          0      1
```

## Empirical certificate-error correlation summary

These correlations are empirical support for certificate-guided selection, not formal optimality guarantees.

```
                           pearson_mae                               spearman_mae                              
                                  mean std       min       max count         mean std       min       max count
method  certificate                                                                                            
gls_map condition_number      0.544775 NaN  0.544775  0.544775     1     0.328518 NaN  0.328518  0.328518     1
        information_logdet    0.036121 NaN  0.036121  0.036121     1    -0.075769 NaN -0.075769 -0.075769     1
        posterior_trace       0.261811 NaN  0.261811  0.261811     1     0.161934 NaN  0.161934  0.161934     1
gsp     condition_number      0.100566 NaN  0.100566  0.100566     1     0.116557 NaN  0.116557  0.116557     1
        information_logdet   -0.266320 NaN -0.266320 -0.266320     1    -0.196416 NaN -0.196416 -0.196416     1
        posterior_trace       0.167439 NaN  0.167439  0.167439     1     0.190270 NaN  0.190270  0.190270     1
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.2 multistart_swap_by_validation               1
```

## Candidate-count sensitivity and practical tractability

Candidate-count sensitivity is summarized as practical tractability and selection stability evidence, not as a broad scalability claim.

### Candidate source and diagnostic stability

```
 budget                        source  candidate_row_count  selected_count  validation_mae_mean  validation_mae_std  selected_validation_mae_mean  selected_validation_mae_std  posterior_trace_mean  posterior_trace_std  selected_posterior_trace_mean  selected_posterior_trace_std  scenario_cvar_trace_mean  scenario_cvar_trace_std  selected_scenario_cvar_trace_mean  selected_scenario_cvar_trace_std  condition_number_mean  condition_number_std  selected_condition_number_mean  selected_condition_number_std  coverage_penalty_mean  coverage_penalty_std  selected_coverage_penalty_mean  selected_coverage_penalty_std  rcss_score_mean  rcss_score_std  selected_rcss_score_mean  selected_rcss_score_std
    0.2                      coverage                    1               0             3.806302                 NaN                           NaN                          NaN            304.991762                  NaN                            NaN                           NaN                211.563068                      NaN                                NaN                               NaN            1283.125553                   NaN                             NaN                            NaN               0.038631                   NaN                             NaN                            NaN         0.275610             NaN                       NaN                      NaN
    0.2                        degree                    1               0             4.201601                 NaN                           NaN                          NaN            345.528309                  NaN                            NaN                           NaN                252.758514                      NaN                                NaN                               NaN            1652.502374                   NaN                             NaN                            NaN               0.140011                   NaN                             NaN                            NaN         0.580914             NaN                       NaN                      NaN
    0.2                greedy_a_trace                    1               0             3.587372                 NaN                           NaN                          NaN            252.784716                  NaN                            NaN                           NaN                174.724202                      NaN                                NaN                               NaN             827.442907                   NaN                             NaN                            NaN               0.035484                   NaN                             NaN                            NaN         0.106522             NaN                       NaN                      NaN
    0.2               greedy_d_logdet                    1               0             4.744223                 NaN                           NaN                          NaN            285.708365                  NaN                            NaN                           NaN                197.797307                      NaN                                NaN                               NaN            2495.738822                   NaN                             NaN                            NaN               0.048895                   NaN                             NaN                            NaN         1.000000             NaN                       NaN                      NaN
    0.2 multistart_swap_by_validation                    1               1             3.449450                 NaN                       3.44945                          NaN            256.535399                  NaN                     256.535399                           NaN                181.068385                      NaN                         181.068385                               NaN             766.339406                   NaN                      766.339406                            NaN               0.035700                   NaN                          0.0357                            NaN         0.000000             NaN                       0.0                      NaN
    0.2       quality_coverage_sample                   50               0             3.613949            0.081470                           NaN                          NaN            302.162829             5.904996                            NaN                           NaN                207.114139                12.270687                                NaN                               NaN             985.964353            114.338274                             NaN                            NaN               0.036181              0.001479                             NaN                            NaN         0.127048        0.062922                       NaN                      NaN
    0.2        random_validation_pool                   50               0             3.727228            0.106580                           NaN                          NaN            299.792554             6.274722                            NaN                           NaN                200.164691                10.570974                                NaN                               NaN             937.188720            131.466407                             NaN                            NaN               0.041276              0.003920                             NaN                            NaN         0.214538        0.082315                       NaN                      NaN
    0.2          robust_coverage_cvar                    1               0             3.572752                 NaN                           NaN                          NaN            276.625379                  NaN                            NaN                           NaN                136.506162                      NaN                                NaN                               NaN             847.092535                   NaN                             NaN                            NaN               0.032460                   NaN                             NaN                            NaN         0.095231             NaN                       NaN                      NaN
    0.2      scenario_average_a_trace                    1               0             3.715095                 NaN                           NaN                          NaN            276.606804                  NaN                            NaN                           NaN                135.610404                      NaN                                NaN                               NaN             843.376774                   NaN                             NaN                            NaN               0.038633                   NaN                             NaN                            NaN         0.205167             NaN                       NaN                      NaN
    0.2         scenario_cvar_a_trace                    1               0             3.709168                 NaN                           NaN                          NaN            280.127282                  NaN                            NaN                           NaN                132.649550                      NaN                                NaN                               NaN             796.919542                   NaN                             NaN                            NaN               0.046398                   NaN                             NaN                            NaN         0.200590             NaN                       NaN                      NaN
    0.2   swap_from_best_random_trace                    1               0             3.674591                 NaN                           NaN                          NaN            254.496666                  NaN                            NaN                           NaN                174.141992                      NaN                                NaN                               NaN             857.256893                   NaN                             NaN                            NaN               0.035099                   NaN                             NaN                            NaN         0.173885             NaN                       NaN                      NaN
    0.2      swap_from_greedy_a_trace                    1               0             3.577630                 NaN                           NaN                          NaN            249.306393                  NaN                            NaN                           NaN                178.425470                      NaN                                NaN                               NaN             854.546557                   NaN                             NaN                            NaN               0.035231                   NaN                             NaN                            NaN         0.098999             NaN                       NaN                      NaN
    0.2    swap_from_scenario_average                    1               0             3.620579                 NaN                           NaN                          NaN            251.116887                  NaN                            NaN                           NaN                172.161338                      NaN                                NaN                               NaN             850.139037                   NaN                             NaN                            NaN               0.037729                   NaN                             NaN                            NaN         0.132169             NaN                       NaN                      NaN
    0.2       swap_from_scenario_cvar                    1               0             3.504293                 NaN                           NaN                          NaN            252.207840                  NaN                            NaN                           NaN                172.418704                      NaN                                NaN                               NaN             843.817608                   NaN                             NaN                            NaN               0.036401                   NaN                             NaN                            NaN         0.042357             NaN                       NaN                      NaN
    0.2                  top_variance                    1               0             3.662078                 NaN                           NaN                          NaN            365.345975                  NaN                            NaN                           NaN                270.485533                      NaN                                NaN                               NaN            1514.637683                   NaN                             NaN                            NaN               0.060086                   NaN                             NaN                            NaN         0.164220             NaN                       NaN                      NaN
    0.2               validation_swap                    3               0             3.367259            0.030405                           NaN                          NaN            285.085914            22.127809                            NaN                           NaN                198.176732                 7.768224                                NaN                               NaN             967.984149            238.869329                             NaN                            NaN               0.037334              0.001015                             NaN                            NaN         0.392871        0.533320                       NaN                      NaN
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