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
    0.1    swap_from_scenario_average 3.485199 0.220688      5
    0.1      validation_swap_selected 3.486339 0.212975      5
    0.1       swap_from_scenario_cvar 3.501861 0.204773      5
    0.1         scenario_cvar_a_trace 3.503011 0.204385      5
    0.1                 rcss_selected 3.510710 0.223765      5
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
    0.2      validation_swap_selected 3.233630 0.191443      5
    0.2                 rcss_selected 3.282164 0.169942      5
    0.2 multistart_swap_by_validation 3.298851 0.184091      5
    0.2     best_random_by_validation 3.310544 0.185326      5
    0.2                  top_variance 3.318824 0.271250      5
    0.2      swap_from_greedy_a_trace 3.328638 0.186602      5
    0.2    swap_from_scenario_average 3.346354 0.228773      5
    0.2       swap_from_scenario_cvar 3.354106 0.221439      5
    0.2                greedy_a_trace 3.357878 0.206507      5
    0.2          robust_coverage_cvar 3.362810 0.210981      5
    0.2   swap_from_best_random_trace 3.366693 0.213715      5
    0.2      scenario_average_a_trace 3.382347 0.204260      5
    0.2         scenario_cvar_a_trace 3.384566 0.227223      5
    0.2          best_random_by_trace 3.455330 0.209056      5
    0.2                        random 3.461664 0.192299   1000
    0.2                      coverage 3.528291 0.256392      5
    0.2                        degree 3.945454 0.255767      5
    0.2               greedy_d_logdet 4.000078 0.335024      5
    0.3      validation_swap_selected 2.997072 0.184917      5
    0.3                 rcss_selected 3.050880 0.211117      5
    0.3     best_random_by_validation 3.091900 0.158028      5
    0.3                  top_variance 3.098213 0.206437      5
    0.3 multistart_swap_by_validation 3.118744 0.187476      5
    0.3   swap_from_best_random_trace 3.208823 0.163651      5
    0.3          robust_coverage_cvar 3.210966 0.221084      5
    0.3      scenario_average_a_trace 3.224780 0.180439      5
    0.3    swap_from_scenario_average 3.246956 0.192258      5
    0.3         scenario_cvar_a_trace 3.254805 0.206696      5
    0.3                greedy_a_trace 3.260017 0.198208      5
    0.3       swap_from_scenario_cvar 3.266091 0.207672      5
    0.3      swap_from_greedy_a_trace 3.272410 0.188745      5
    0.3                      coverage 3.278006 0.193252      5
    0.3          best_random_by_trace 3.295348 0.197361      5
    0.3                        random 3.314711 0.190938   1000
    0.3               greedy_d_logdet 3.720418 0.273548      5
    0.3                        degree 3.806697 0.256169      5
```

## RCSS deltas, negative is better

```
 budget  validation_swap_selected_minus_random_mean  validation_swap_selected_minus_random_std  validation_swap_selected_minus_best_random_by_validation_mean  validation_swap_selected_minus_best_random_by_validation_std  validation_swap_selected_minus_top_variance_mean  validation_swap_selected_minus_top_variance_std  validation_swap_selected_minus_greedy_a_trace_mean  validation_swap_selected_minus_greedy_a_trace_std  validation_swap_selected_minus_scenario_cvar_a_trace_mean  validation_swap_selected_minus_scenario_cvar_a_trace_std  validation_swap_selected_minus_multistart_swap_by_validation_mean  validation_swap_selected_minus_multistart_swap_by_validation_std  validation_swap_selected_minus_swap_from_scenario_cvar_mean  validation_swap_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_scenario_cvar_a_trace_mean  rcss_selected_minus_scenario_cvar_a_trace_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_scenario_cvar_a_trace_mean  robust_coverage_cvar_minus_scenario_cvar_a_trace_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std
    0.1                                   -0.220377                                   0.082033                                                      -0.081397                                                      0.078740                                         -0.091611                                         0.110071                                           -0.053823                                           0.064509                                                  -0.016671                                                  0.127037                                                           0.024922                                                          0.054856                                                    -0.015521                                                    0.078700                        -0.196007                        0.059171                                           -0.057027                                           0.081869                              -0.067241                              0.081946                                -0.029453                                0.044218                                        0.007699                                       0.107625                                                0.049292                                               0.039327                                          0.008849                                         0.059498                               -0.158386                               0.039217                                                  -0.019406                                                  0.053686                                     -0.029620                                     0.072704                                        0.008168                                       0.053087                                               0.045320                                              0.077824                                                       0.086913                                                      0.042807                                                 0.046470                                                0.030889
    0.2                                   -0.228035                                   0.063219                                                      -0.076914                                                      0.011235                                         -0.085194                                         0.110757                                           -0.124248                                           0.047786                                                  -0.150936                                                  0.061585                                                          -0.065221                                                          0.069208                                                    -0.120476                                                    0.082176                        -0.179501                        0.072668                                           -0.028380                                           0.041070                              -0.036660                              0.121085                                -0.075714                                0.067677                                       -0.102403                                       0.078013                                               -0.016687                                               0.082788                                         -0.071942                                         0.101515                               -0.098855                               0.036657                                                   0.052266                                                  0.059225                                      0.043986                                     0.094649                                        0.004932                                       0.032007                                              -0.021756                                              0.067187                                                       0.063959                                                      0.049894                                                 0.008704                                                0.042003
    0.3                                   -0.317639                                   0.069732                                                      -0.094828                                                      0.057847                                         -0.101141                                         0.054001                                           -0.262945                                           0.072635                                                  -0.257733                                                  0.119381                                                          -0.121672                                                          0.037844                                                    -0.269019                                                    0.102045                        -0.263831                        0.094057                                           -0.041019                                           0.085527                              -0.047333                              0.056633                                -0.209137                                0.093450                                       -0.203925                                       0.138283                                               -0.067864                                               0.060637                                         -0.215211                                         0.122828                               -0.103745                               0.068551                                                   0.119067                                                  0.076880                                      0.112753                                     0.085713                                       -0.049051                                       0.068769                                              -0.043839                                              0.087344                                                       0.092222                                                      0.044462                                                -0.055125                                                0.084344
```

## Winner counts

```
 budget                   best_layout  wins
    0.1 multistart_swap_by_validation     1
    0.1         scenario_cvar_a_trace     1
    0.1      swap_from_greedy_a_trace     1
    0.1    swap_from_scenario_average     1
    0.1      validation_swap_selected     1
    0.2 multistart_swap_by_validation     1
    0.2                        random     1
    0.2                  top_variance     2
    0.2      validation_swap_selected     1
    0.3      validation_swap_selected     5
```

## Main ablation layouts

```
 budget               layout_type     mean      std  count
    0.1  validation_swap_selected 3.486339 0.212975      5
    0.1     scenario_cvar_a_trace 3.503011 0.204385      5
    0.1             rcss_selected 3.510710 0.223765      5
    0.1            greedy_a_trace 3.540162 0.256561      5
    0.1 best_random_by_validation 3.567737 0.163324      5
    0.1              top_variance 3.577951 0.242033      5
    0.2  validation_swap_selected 3.233630 0.191443      5
    0.2             rcss_selected 3.282164 0.169942      5
    0.2 best_random_by_validation 3.310544 0.185326      5
    0.2              top_variance 3.318824 0.271250      5
    0.2            greedy_a_trace 3.357878 0.206507      5
    0.2     scenario_cvar_a_trace 3.384566 0.227223      5
    0.3  validation_swap_selected 2.997072 0.184917      5
    0.3             rcss_selected 3.050880 0.211117      5
    0.3 best_random_by_validation 3.091900 0.158028      5
    0.3              top_variance 3.098213 0.206437      5
    0.3     scenario_cvar_a_trace 3.254805 0.206696      5
    0.3            greedy_a_trace 3.260017 0.198208      5
```

## Paired delta tests

```
 budget                   layout                      baseline  delta_mean  delta_std  win_count  count  paired_t_p  wilcoxon_p
    0.1 validation_swap_selected                        random   -0.220377   0.082033          5      5    0.003866      0.0625
    0.1 validation_swap_selected     best_random_by_validation   -0.081397   0.078740          4      5    0.081895      0.1250
    0.1 validation_swap_selected                  top_variance   -0.091611   0.110071          5      5    0.136232      0.0625
    0.1 validation_swap_selected                greedy_a_trace   -0.053823   0.064509          4      5    0.135511      0.1875
    0.1 validation_swap_selected         scenario_cvar_a_trace   -0.016671   0.127037          2      5    0.783778      0.8125
    0.1 validation_swap_selected multistart_swap_by_validation    0.024922   0.054856          2      5    0.367139      0.4375
    0.1 validation_swap_selected       swap_from_scenario_cvar   -0.015521   0.078700          1      5    0.682004      0.6250
    0.1            rcss_selected                        random   -0.196007   0.059171          5      5    0.001772      0.0625
    0.1            rcss_selected     best_random_by_validation   -0.057027   0.081869          4      5    0.194333      0.1875
    0.1            rcss_selected                  top_variance   -0.067241   0.081946          5      5    0.140443      0.0625
    0.1            rcss_selected                greedy_a_trace   -0.029453   0.044218          4      5    0.210624      0.1875
    0.1            rcss_selected         scenario_cvar_a_trace    0.007699   0.107625          2      5    0.880666      0.8125
    0.1            rcss_selected multistart_swap_by_validation    0.049292   0.039327          0      5    0.048679      0.1250
    0.1            rcss_selected       swap_from_scenario_cvar    0.008849   0.059498          1      5    0.756156      0.6250
    0.1     robust_coverage_cvar                        random   -0.158386   0.039217          5      5    0.000833      0.0625
    0.1     robust_coverage_cvar     best_random_by_validation   -0.019406   0.053686          4      5    0.464255      0.6250
    0.1     robust_coverage_cvar                  top_variance   -0.029620   0.072704          3      5    0.413831      0.6250
    0.1     robust_coverage_cvar                greedy_a_trace    0.008168   0.053087          1      5    0.748135      0.6250
    0.1     robust_coverage_cvar         scenario_cvar_a_trace    0.045320   0.077824          1      5    0.262788      0.3125
    0.1     robust_coverage_cvar multistart_swap_by_validation    0.086913   0.042807          0      5    0.010497      0.0625
    0.1     robust_coverage_cvar       swap_from_scenario_cvar    0.046470   0.030889          0      5    0.028201      0.0625
    0.2 validation_swap_selected                        random   -0.228035   0.063219          5      5    0.001283      0.0625
    0.2 validation_swap_selected     best_random_by_validation   -0.076914   0.011235          5      5    0.000106      0.0625
    0.2 validation_swap_selected                  top_variance   -0.085194   0.110757          3      5    0.160557      0.3125
    0.2 validation_swap_selected                greedy_a_trace   -0.124248   0.047786          5      5    0.004356      0.0625
    0.2 validation_swap_selected         scenario_cvar_a_trace   -0.150936   0.061585          5      5    0.005398      0.0625
    0.2 validation_swap_selected multistart_swap_by_validation   -0.065221   0.069208          4      5    0.102811      0.1250
    0.2 validation_swap_selected       swap_from_scenario_cvar   -0.120476   0.082176          5      5    0.030551      0.0625
    0.2            rcss_selected                        random   -0.179501   0.072668          5      5    0.005247      0.0625
    0.2            rcss_selected     best_random_by_validation   -0.028380   0.041070          3      5    0.197201      0.3125
    0.2            rcss_selected                  top_variance   -0.036660   0.121085          3      5    0.535541      0.6250
    0.2            rcss_selected                greedy_a_trace   -0.075714   0.067677          4      5    0.066651      0.1250
    0.2            rcss_selected         scenario_cvar_a_trace   -0.102403   0.078013          4      5    0.042595      0.1250
    0.2            rcss_selected multistart_swap_by_validation   -0.016687   0.082788          2      5    0.675551      0.7500
    0.2            rcss_selected       swap_from_scenario_cvar   -0.071942   0.101515          4      5    0.188219      0.1875
    0.2     robust_coverage_cvar                        random   -0.098855   0.036657          5      5    0.003812      0.0625
    0.2     robust_coverage_cvar     best_random_by_validation    0.052266   0.059225          1      5    0.119710      0.1875
    0.2     robust_coverage_cvar                  top_variance    0.043986   0.094649          2      5    0.357411      0.4375
    0.2     robust_coverage_cvar                greedy_a_trace    0.004932   0.032007          2      5    0.747783      0.8125
    0.2     robust_coverage_cvar         scenario_cvar_a_trace   -0.021756   0.067187          2      5    0.509095      0.8125
    0.2     robust_coverage_cvar multistart_swap_by_validation    0.063959   0.049894          1      5    0.045633      0.1250
    0.2     robust_coverage_cvar       swap_from_scenario_cvar    0.008704   0.042003          3      5    0.667200      0.8125
    0.3 validation_swap_selected                        random   -0.317639   0.069732          5      5    0.000523      0.0625
    0.3 validation_swap_selected     best_random_by_validation   -0.094828   0.057847          5      5    0.021475      0.0625
    0.3 validation_swap_selected                  top_variance   -0.101141   0.054001          5      5    0.013828      0.0625
    0.3 validation_swap_selected                greedy_a_trace   -0.262945   0.072635          5      5    0.001266      0.0625
    0.3 validation_swap_selected         scenario_cvar_a_trace   -0.257733   0.119381          5      5    0.008477      0.0625
    0.3 validation_swap_selected multistart_swap_by_validation   -0.121672   0.037844          5      5    0.001983      0.0625
    0.3 validation_swap_selected       swap_from_scenario_cvar   -0.269019   0.102045          5      5    0.004142      0.0625
    0.3            rcss_selected                        random   -0.263831   0.094057          5      5    0.003298      0.0625
    0.3            rcss_selected     best_random_by_validation   -0.041019   0.085527          4      5    0.343919      0.4375
    0.3            rcss_selected                  top_variance   -0.047333   0.056633          3      5    0.135010      0.3125
    0.3            rcss_selected                greedy_a_trace   -0.209137   0.093450          5      5    0.007468      0.0625
    0.3            rcss_selected         scenario_cvar_a_trace   -0.203925   0.138283          5      5    0.030003      0.0625
    0.3            rcss_selected multistart_swap_by_validation   -0.067864   0.060637          5      5    0.066582      0.0625
    0.3            rcss_selected       swap_from_scenario_cvar   -0.215211   0.122828          5      5    0.017278      0.0625
    0.3     robust_coverage_cvar                        random   -0.103745   0.068551          5      5    0.027682      0.0625
    0.3     robust_coverage_cvar     best_random_by_validation    0.119067   0.076880          0      5    0.025745      0.0625
    0.3     robust_coverage_cvar                  top_variance    0.112753   0.085713          1      5    0.042326      0.1250
    0.3     robust_coverage_cvar                greedy_a_trace   -0.049051   0.068769          4      5    0.185958      0.3125
    0.3     robust_coverage_cvar         scenario_cvar_a_trace   -0.043839   0.087344          4      5    0.324542      0.3125
    0.3     robust_coverage_cvar multistart_swap_by_validation    0.092222   0.044462          0      5    0.009749      0.0625
    0.3     robust_coverage_cvar       swap_from_scenario_cvar   -0.055125   0.084344          3      5    0.217701      0.3125
```

## Certificate stability

```
                           pearson_mae                               spearman_mae                              
                                  mean       std       min       max         mean       std       min       max
method  certificate                                                                                            
gls_map condition_number      0.829074  0.012922  0.807036  0.840619     0.852765  0.010396  0.840918  0.863910
        information_logdet   -0.815986  0.021204 -0.837977 -0.788129    -0.808131  0.011099 -0.823370 -0.797829
        posterior_trace       0.854989  0.016749  0.834530  0.872573     0.845977  0.010465  0.829307  0.855879
gsp     condition_number      0.146681  0.138256 -0.083552  0.259667     0.154651  0.150557 -0.097505  0.279777
        information_logdet   -0.151824  0.136195 -0.264203  0.076825    -0.179271  0.142990 -0.289326  0.064247
        posterior_trace       0.143870  0.138281 -0.086417  0.257379     0.154454  0.152920 -0.104985  0.277480
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.1 multistart_swap_by_validation               1
    0.1       quality_coverage_sample               1
    0.1          robust_coverage_cvar               1
    0.1      swap_from_greedy_a_trace               1
    0.1    swap_from_scenario_average               1
    0.2 multistart_swap_by_validation               2
    0.2       quality_coverage_sample               3
    0.3       quality_coverage_sample               5
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