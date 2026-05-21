---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.1 multistart_swap_by_validation 3.578255 0.296331     10
    0.1   swap_from_best_random_trace 3.598399 0.291192     10
    0.1                 rcss_selected 3.602807 0.293477     10
    0.1      validation_swap_selected 3.605467 0.287149     10
    0.1    swap_from_scenario_average 3.608135 0.291747     10
    0.1      swap_from_greedy_a_trace 3.618489 0.301167     10
    0.1       swap_from_scenario_cvar 3.631524 0.307982     10
    0.1          robust_coverage_cvar 3.673948 0.328744     10
    0.1                greedy_a_trace 3.685979 0.343436     10
    0.1         scenario_cvar_a_trace 3.687415 0.377051     10
    0.1      scenario_average_a_trace 3.688937 0.320762     10
    0.1     best_random_by_validation 3.691262 0.305074     10
    0.1                  top_variance 3.730412 0.341240     10
    0.1          best_random_by_trace 3.740093 0.309229     10
    0.1                        random 3.835865 0.324598   2000
    0.1                      coverage 3.917374 0.342939     10
    0.1                        degree 4.146553 0.299507     10
    0.1               greedy_d_logdet 4.555445 0.611738     10
    0.2      validation_swap_selected 3.309508 0.286047     10
    0.2                 rcss_selected 3.376168 0.266483     10
    0.2     best_random_by_validation 3.396877 0.288660     10
    0.2 multistart_swap_by_validation 3.397042 0.283949     10
    0.2                  top_variance 3.427610 0.338372     10
    0.2          robust_coverage_cvar 3.439815 0.288589     10
    0.2       swap_from_scenario_cvar 3.446701 0.290780     10
    0.2      swap_from_greedy_a_trace 3.450542 0.308488     10
    0.2    swap_from_scenario_average 3.451680 0.295112     10
    0.2                greedy_a_trace 3.465389 0.323998     10
    0.2         scenario_cvar_a_trace 3.468041 0.296913     10
    0.2   swap_from_best_random_trace 3.472290 0.283301     10
    0.2      scenario_average_a_trace 3.503000 0.294501     10
    0.2          best_random_by_trace 3.563667 0.319607     10
    0.2                        random 3.564792 0.292848   2000
    0.2                      coverage 3.648157 0.341481     10
    0.2                        degree 4.111082 0.345335     10
    0.2               greedy_d_logdet 4.178236 0.478752     10
    0.3      validation_swap_selected 3.066530 0.249741     10
    0.3                 rcss_selected 3.133037 0.246068     10
    0.3     best_random_by_validation 3.183207 0.273145     10
    0.3                  top_variance 3.200391 0.291698     10
    0.3 multistart_swap_by_validation 3.219579 0.294179     10
    0.3          robust_coverage_cvar 3.293380 0.277334     10
    0.3   swap_from_best_random_trace 3.316706 0.300728     10
    0.3         scenario_cvar_a_trace 3.326025 0.291669     10
    0.3    swap_from_scenario_average 3.326517 0.280134     10
    0.3       swap_from_scenario_cvar 3.334236 0.283352     10
    0.3      scenario_average_a_trace 3.334910 0.297826     10
    0.3      swap_from_greedy_a_trace 3.349400 0.282460     10
    0.3                greedy_a_trace 3.350643 0.309428     10
    0.3                      coverage 3.377843 0.299050     10
    0.3                        random 3.403231 0.275716   2000
    0.3          best_random_by_trace 3.408842 0.297710     10
    0.3               greedy_d_logdet 3.879257 0.435774     10
    0.3                        degree 3.976153 0.360831     10
```

## RCSS deltas, negative is better

```
 budget  validation_swap_selected_minus_random_mean  validation_swap_selected_minus_random_std  validation_swap_selected_minus_best_random_by_validation_mean  validation_swap_selected_minus_best_random_by_validation_std  validation_swap_selected_minus_top_variance_mean  validation_swap_selected_minus_top_variance_std  validation_swap_selected_minus_greedy_a_trace_mean  validation_swap_selected_minus_greedy_a_trace_std  validation_swap_selected_minus_scenario_cvar_a_trace_mean  validation_swap_selected_minus_scenario_cvar_a_trace_std  validation_swap_selected_minus_multistart_swap_by_validation_mean  validation_swap_selected_minus_multistart_swap_by_validation_std  validation_swap_selected_minus_swap_from_scenario_cvar_mean  validation_swap_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_scenario_cvar_a_trace_mean  rcss_selected_minus_scenario_cvar_a_trace_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_scenario_cvar_a_trace_mean  robust_coverage_cvar_minus_scenario_cvar_a_trace_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std
    0.1                                   -0.230397                                   0.095087                                                      -0.085795                                                      0.108878                                         -0.124945                                         0.106588                                           -0.080511                                           0.084633                                                  -0.081947                                                  0.140820                                                           0.027213                                                          0.042666                                                    -0.026056                                                    0.063379                        -0.233057                        0.084842                                           -0.088455                                           0.109819                              -0.127605                              0.107032                                -0.083171                                0.078189                                       -0.084607                                       0.142834                                                0.024553                                               0.037540                                         -0.028716                                         0.067179                               -0.161917                               0.037796                                                  -0.017315                                                  0.050738                                     -0.056465                                     0.059765                                       -0.012031                                       0.089611                                              -0.013467                                              0.089450                                                       0.095693                                                      0.076925                                                 0.042424                                                0.070642
    0.2                                   -0.255284                                   0.064423                                                      -0.087369                                                      0.066490                                         -0.118102                                         0.111053                                           -0.155881                                           0.087972                                                  -0.158532                                                  0.066492                                                          -0.087534                                                          0.081698                                                    -0.137193                                                    0.072476                        -0.188624                        0.074723                                           -0.020709                                           0.095831                              -0.051442                              0.124170                                -0.089221                                0.108317                                       -0.091872                                       0.084900                                               -0.020874                                               0.093082                                         -0.070533                                         0.087098                               -0.124977                               0.046636                                                   0.042938                                                  0.066598                                      0.012205                                     0.095801                                       -0.025574                                       0.074288                                              -0.028225                                              0.059709                                                       0.042774                                                      0.064133                                                -0.006886                                                0.045343
    0.3                                   -0.336701                                   0.055446                                                      -0.116677                                                      0.054352                                         -0.133861                                         0.071279                                           -0.284113                                           0.092302                                                  -0.259496                                                  0.108220                                                          -0.153050                                                          0.058222                                                    -0.267707                                                    0.087320                        -0.270194                        0.087499                                           -0.050170                                           0.089586                              -0.067354                              0.098694                                -0.217606                                0.128525                                       -0.192988                                       0.140283                                               -0.086542                                               0.091036                                         -0.201199                                         0.119427                               -0.109851                               0.069360                                                   0.110173                                                  0.072873                                      0.092989                                     0.090958                                       -0.057263                                       0.087190                                              -0.032645                                              0.066230                                                       0.073801                                                      0.073684                                                -0.040856                                                0.063813
```

## Winner counts

```
 budget                   best_layout  wins
    0.1 multistart_swap_by_validation     2
    0.1                        random     1
    0.1         scenario_cvar_a_trace     1
    0.1      swap_from_greedy_a_trace     1
    0.1    swap_from_scenario_average     2
    0.1       swap_from_scenario_cvar     1
    0.1      validation_swap_selected     2
    0.2 multistart_swap_by_validation     1
    0.2                        random     2
    0.2                  top_variance     2
    0.2      validation_swap_selected     5
    0.3                 rcss_selected     1
    0.3      validation_swap_selected     9
```

## Main ablation layouts

```
 budget               layout_type     mean      std  count
    0.1             rcss_selected 3.602807 0.293477     10
    0.1  validation_swap_selected 3.605467 0.287149     10
    0.1            greedy_a_trace 3.685979 0.343436     10
    0.1     scenario_cvar_a_trace 3.687415 0.377051     10
    0.1 best_random_by_validation 3.691262 0.305074     10
    0.1              top_variance 3.730412 0.341240     10
    0.2  validation_swap_selected 3.309508 0.286047     10
    0.2             rcss_selected 3.376168 0.266483     10
    0.2 best_random_by_validation 3.396877 0.288660     10
    0.2              top_variance 3.427610 0.338372     10
    0.2            greedy_a_trace 3.465389 0.323998     10
    0.2     scenario_cvar_a_trace 3.468041 0.296913     10
    0.3  validation_swap_selected 3.066530 0.249741     10
    0.3             rcss_selected 3.133037 0.246068     10
    0.3 best_random_by_validation 3.183207 0.273145     10
    0.3              top_variance 3.200391 0.291698     10
    0.3     scenario_cvar_a_trace 3.326025 0.291669     10
    0.3            greedy_a_trace 3.350643 0.309428     10
```

## Paired delta tests

```
 budget                   layout                      baseline  delta_mean  delta_std  win_count  count   paired_t_p  wilcoxon_p
    0.1 validation_swap_selected                        random   -0.230397   0.095087         10     10 3.118882e-05    0.001953
    0.1 validation_swap_selected     best_random_by_validation   -0.085795   0.108878          7     10 3.431785e-02    0.027344
    0.1 validation_swap_selected                  top_variance   -0.124945   0.106588         10     10 4.868367e-03    0.001953
    0.1 validation_swap_selected                greedy_a_trace   -0.080511   0.084633          9     10 1.475716e-02    0.009766
    0.1 validation_swap_selected         scenario_cvar_a_trace   -0.081947   0.140820          6     10 9.887740e-02    0.275391
    0.1 validation_swap_selected multistart_swap_by_validation    0.027213   0.042666          3     10 7.449269e-02    0.083984
    0.1 validation_swap_selected       swap_from_scenario_cvar   -0.026056   0.063379          5     10 2.258881e-01    0.322266
    0.1            rcss_selected                        random   -0.233057   0.084842         10     10 1.139907e-05    0.001953
    0.1            rcss_selected     best_random_by_validation   -0.088455   0.109819          8     10 3.134362e-02    0.037109
    0.1            rcss_selected                  top_variance   -0.127605   0.107032         10     10 4.415613e-03    0.001953
    0.1            rcss_selected                greedy_a_trace   -0.083171   0.078189          9     10 8.338702e-03    0.005859
    0.1            rcss_selected         scenario_cvar_a_trace   -0.084607   0.142834          7     10 9.382356e-02    0.160156
    0.1            rcss_selected multistart_swap_by_validation    0.024553   0.037540          1     10 6.855874e-02    0.093750
    0.1            rcss_selected       swap_from_scenario_cvar   -0.028716   0.067179          5     10 2.094524e-01    0.250000
    0.1     robust_coverage_cvar                        random   -0.161917   0.037796         10     10 2.723849e-07    0.001953
    0.1     robust_coverage_cvar     best_random_by_validation   -0.017315   0.050738          7     10 3.085898e-01    0.431641
    0.1     robust_coverage_cvar                  top_variance   -0.056465   0.059765          8     10 1.525842e-02    0.027344
    0.1     robust_coverage_cvar                greedy_a_trace   -0.012031   0.089611          5     10 6.811236e-01    0.695312
    0.1     robust_coverage_cvar         scenario_cvar_a_trace   -0.013467   0.089450          6     10 6.453521e-01    0.695312
    0.1     robust_coverage_cvar multistart_swap_by_validation    0.095693   0.076925          0     10 3.438252e-03    0.001953
    0.1     robust_coverage_cvar       swap_from_scenario_cvar    0.042424   0.070642          2     10 9.001842e-02    0.105469
    0.2 validation_swap_selected                        random   -0.255284   0.064423         10     10 5.320806e-07    0.001953
    0.2 validation_swap_selected     best_random_by_validation   -0.087369   0.066490          9     10 2.464864e-03    0.005859
    0.2 validation_swap_selected                  top_variance   -0.118102   0.111053          8     10 8.349176e-03    0.009766
    0.2 validation_swap_selected                greedy_a_trace   -0.155881   0.087972         10     10 3.328483e-04    0.001953
    0.2 validation_swap_selected         scenario_cvar_a_trace   -0.158532   0.066492         10     10 3.542655e-05    0.001953
    0.2 validation_swap_selected multistart_swap_by_validation   -0.087534   0.081698          8     10 8.022456e-03    0.009766
    0.2 validation_swap_selected       swap_from_scenario_cvar   -0.137193   0.072476         10     10 2.060058e-04    0.001953
    0.2            rcss_selected                        random   -0.188624   0.074723         10     10 2.252408e-05    0.001953
    0.2            rcss_selected     best_random_by_validation   -0.020709   0.095831          6     10 5.115780e-01    0.375000
    0.2            rcss_selected                  top_variance   -0.051442   0.124170          6     10 2.226106e-01    0.322266
    0.2            rcss_selected                greedy_a_trace   -0.089221   0.108317          8     10 2.851417e-02    0.013672
    0.2            rcss_selected         scenario_cvar_a_trace   -0.091872   0.084900          8     10 7.604094e-03    0.013672
    0.2            rcss_selected multistart_swap_by_validation   -0.020874   0.093082          4     10 4.961987e-01    0.562500
    0.2            rcss_selected       swap_from_scenario_cvar   -0.070533   0.087098          8     10 3.064346e-02    0.048828
    0.2     robust_coverage_cvar                        random   -0.124977   0.046636         10     10 1.392946e-05    0.001953
    0.2     robust_coverage_cvar     best_random_by_validation    0.042938   0.066598          4     10 7.190342e-02    0.160156
    0.2     robust_coverage_cvar                  top_variance    0.012205   0.095801          5     10 6.964465e-01    0.695312
    0.2     robust_coverage_cvar                greedy_a_trace   -0.025574   0.074288          5     10 3.046080e-01    0.492188
    0.2     robust_coverage_cvar         scenario_cvar_a_trace   -0.028225   0.059709          5     10 1.691641e-01    0.375000
    0.2     robust_coverage_cvar multistart_swap_by_validation    0.042774   0.064133          3     10 6.416568e-02    0.083984
    0.2     robust_coverage_cvar       swap_from_scenario_cvar   -0.006886   0.045343          6     10 6.425074e-01    0.625000
    0.3 validation_swap_selected                        random   -0.336701   0.055446         10     10 1.299187e-08    0.001953
    0.3 validation_swap_selected     best_random_by_validation   -0.116677   0.054352         10     10 8.008658e-05    0.001953
    0.3 validation_swap_selected                  top_variance   -0.133861   0.071279         10     10 2.183585e-04    0.001953
    0.3 validation_swap_selected                greedy_a_trace   -0.284113   0.092302         10     10 4.477322e-06    0.001953
    0.3 validation_swap_selected         scenario_cvar_a_trace   -0.259496   0.108220         10     10 3.387080e-05    0.001953
    0.3 validation_swap_selected multistart_swap_by_validation   -0.153050   0.058222         10     10 1.627282e-05    0.001953
    0.3 validation_swap_selected       swap_from_scenario_cvar   -0.267707   0.087320         10     10 4.627815e-06    0.001953
    0.3            rcss_selected                        random   -0.270194   0.087499         10     10 4.360014e-06    0.001953
    0.3            rcss_selected     best_random_by_validation   -0.050170   0.089586          6     10 1.103452e-01    0.203125
    0.3            rcss_selected                  top_variance   -0.067354   0.098694          6     10 5.924934e-02    0.083984
    0.3            rcss_selected                greedy_a_trace   -0.217606   0.128525         10     10 4.598907e-04    0.001953
    0.3            rcss_selected         scenario_cvar_a_trace   -0.192988   0.140283         10     10 1.849283e-03    0.001953
    0.3            rcss_selected multistart_swap_by_validation   -0.086542   0.091036          9     10 1.480717e-02    0.003906
    0.3            rcss_selected       swap_from_scenario_cvar   -0.201199   0.119427         10     10 4.762373e-04    0.001953
    0.3     robust_coverage_cvar                        random   -0.109851   0.069360         10     10 7.306207e-04    0.001953
    0.3     robust_coverage_cvar     best_random_by_validation    0.110173   0.072873          0     10 9.999914e-04    0.001953
    0.3     robust_coverage_cvar                  top_variance    0.092989   0.090958          2     10 1.027482e-02    0.027344
    0.3     robust_coverage_cvar                greedy_a_trace   -0.057263   0.087190          8     10 6.760927e-02    0.083984
    0.3     robust_coverage_cvar         scenario_cvar_a_trace   -0.032645   0.066230          7     10 1.534944e-01    0.130859
    0.3     robust_coverage_cvar multistart_swap_by_validation    0.073801   0.073684          2     10 1.141574e-02    0.013672
    0.3     robust_coverage_cvar       swap_from_scenario_cvar   -0.040856   0.063813          6     10 7.356515e-02    0.105469
```

## Certificate stability

```
                           pearson_mae                               spearman_mae                              
                                  mean       std       min       max         mean       std       min       max
method  certificate                                                                                            
gls_map condition_number      0.832714  0.015955  0.806602  0.857588     0.859243  0.010964  0.840918  0.872474
        information_logdet   -0.820913  0.017046 -0.839010 -0.788129    -0.813041  0.010970 -0.830466 -0.797829
        posterior_trace       0.861249  0.015121  0.834530  0.885216     0.851310  0.010223  0.829307  0.866054
gsp     condition_number      0.126598  0.123165 -0.083552  0.280195     0.133357  0.128353 -0.097505  0.284471
        information_logdet   -0.131849  0.123318 -0.288363  0.076825    -0.159171  0.126845 -0.324830  0.064247
        posterior_trace       0.124222  0.123547 -0.086417  0.279751     0.124038  0.137277 -0.104985  0.278202
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.1 multistart_swap_by_validation               4
    0.1       quality_coverage_sample               1
    0.1          robust_coverage_cvar               1
    0.1      swap_from_greedy_a_trace               2
    0.1    swap_from_scenario_average               1
    0.1       swap_from_scenario_cvar               1
    0.2 multistart_swap_by_validation               4
    0.2       quality_coverage_sample               5
    0.2          robust_coverage_cvar               1
    0.3       quality_coverage_sample               9
    0.3        random_validation_pool               1
```

## Output files

- combined_metrics.csv
- gls_map_layout_summary.csv
- gls_map_delta_summary.csv
- gls_map_paired_delta_tests.csv
- gls_map_ablation_summary.csv
- gls_map_per_split_winners.csv
- gls_map_win_counts.csv
- combined_rcss_candidates.csv
- rcss_selected_sources.csv