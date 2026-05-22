---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.1      validation_swap_selected 3.590056 0.307260     10
    0.1 multistart_swap_by_validation 3.594525 0.324835     10
    0.1                 rcss_selected 3.604982 0.293286     10
    0.1    swap_from_scenario_average 3.606083 0.301670     10
    0.1   swap_from_best_random_trace 3.614189 0.281401     10
    0.1      swap_from_greedy_a_trace 3.618489 0.301167     10
    0.1       swap_from_scenario_cvar 3.642754 0.274517     10
    0.1                greedy_a_trace 3.685979 0.343436     10
    0.1     best_random_by_validation 3.713110 0.323978     10
    0.1                  top_variance 3.730412 0.341240     10
    0.1          robust_coverage_cvar 3.735710 0.278681     10
    0.1          best_random_by_trace 3.755145 0.285011     10
    0.1      scenario_average_a_trace 3.771209 0.337125     10
    0.1         scenario_cvar_a_trace 3.788435 0.363404     10
    0.1                        random 3.833113 0.326246    500
    0.1                      coverage 3.917374 0.342939     10
    0.1                  qr_pod_modes 3.976937 0.335897     10
    0.1           observability_proxy 4.001340 0.321938     10
    0.1      graph_sampling_laplacian 4.132875 0.506233     10
    0.1                        degree 4.146553 0.299507     10
    0.1               greedy_d_logdet 4.555445 0.611738     10
    0.2      validation_swap_selected 3.354688 0.312941     10
    0.2                 rcss_selected 3.393473 0.290102     10
    0.2 multistart_swap_by_validation 3.396952 0.304817     10
    0.2                  top_variance 3.427610 0.338372     10
    0.2   swap_from_best_random_trace 3.442609 0.302418     10
    0.2     best_random_by_validation 3.449509 0.290911     10
    0.2      swap_from_greedy_a_trace 3.450542 0.308488     10
    0.2       swap_from_scenario_cvar 3.451704 0.269837     10
    0.2                greedy_a_trace 3.465389 0.323998     10
    0.2    swap_from_scenario_average 3.470548 0.302884     10
    0.2          robust_coverage_cvar 3.482083 0.248948     10
    0.2          best_random_by_trace 3.504184 0.279494     10
    0.2      scenario_average_a_trace 3.559834 0.288740     10
    0.2                        random 3.574559 0.293597    500
    0.2         scenario_cvar_a_trace 3.584608 0.340429     10
    0.2                      coverage 3.648157 0.341481     10
    0.2                  qr_pod_modes 3.784042 0.372491     10
    0.2           observability_proxy 3.923607 0.330187     10
    0.2      graph_sampling_laplacian 3.991709 0.444776     10
    0.2                        degree 4.111082 0.345335     10
    0.2               greedy_d_logdet 4.178236 0.478752     10
    0.3      validation_swap_selected 3.084223 0.239671     10
    0.3                 rcss_selected 3.182557 0.279200     10
    0.3                  top_variance 3.200391 0.291698     10
    0.3 multistart_swap_by_validation 3.204223 0.294221     10
    0.3     best_random_by_validation 3.246943 0.236188     10
    0.3       swap_from_scenario_cvar 3.300022 0.265764     10
    0.3          robust_coverage_cvar 3.305721 0.294014     10
    0.3   swap_from_best_random_trace 3.323290 0.287353     10
    0.3    swap_from_scenario_average 3.343261 0.277516     10
    0.3      swap_from_greedy_a_trace 3.349400 0.282460     10
    0.3                greedy_a_trace 3.350643 0.309428     10
    0.3          best_random_by_trace 3.369069 0.268790     10
    0.3                      coverage 3.377843 0.299050     10
    0.3      scenario_average_a_trace 3.378972 0.295024     10
    0.3         scenario_cvar_a_trace 3.401787 0.296027     10
    0.3                        random 3.403730 0.277685    500
    0.3                  qr_pod_modes 3.446503 0.314999     10
    0.3      graph_sampling_laplacian 3.804840 0.390244     10
    0.3               greedy_d_logdet 3.879257 0.435774     10
    0.3           observability_proxy 3.887171 0.358241     10
    0.3                        degree 3.976153 0.360831     10
```

## RCSS deltas, negative is better

```
 budget  validation_swap_selected_minus_random_mean  validation_swap_selected_minus_random_std  validation_swap_selected_minus_best_random_by_validation_mean  validation_swap_selected_minus_best_random_by_validation_std  validation_swap_selected_minus_top_variance_mean  validation_swap_selected_minus_top_variance_std  validation_swap_selected_minus_observability_proxy_mean  validation_swap_selected_minus_observability_proxy_std  validation_swap_selected_minus_greedy_a_trace_mean  validation_swap_selected_minus_greedy_a_trace_std  validation_swap_selected_minus_greedy_d_logdet_mean  validation_swap_selected_minus_greedy_d_logdet_std  validation_swap_selected_minus_graph_sampling_laplacian_mean  validation_swap_selected_minus_graph_sampling_laplacian_std  validation_swap_selected_minus_qr_pod_modes_mean  validation_swap_selected_minus_qr_pod_modes_std  validation_swap_selected_minus_scenario_cvar_a_trace_mean  validation_swap_selected_minus_scenario_cvar_a_trace_std  validation_swap_selected_minus_multistart_swap_by_validation_mean  validation_swap_selected_minus_multistart_swap_by_validation_std  validation_swap_selected_minus_swap_from_scenario_cvar_mean  validation_swap_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  rcss_selected_minus_observability_proxy_mean  rcss_selected_minus_observability_proxy_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_greedy_d_logdet_mean  rcss_selected_minus_greedy_d_logdet_std  rcss_selected_minus_graph_sampling_laplacian_mean  rcss_selected_minus_graph_sampling_laplacian_std  rcss_selected_minus_qr_pod_modes_mean  rcss_selected_minus_qr_pod_modes_std  rcss_selected_minus_scenario_cvar_a_trace_mean  rcss_selected_minus_scenario_cvar_a_trace_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std  robust_coverage_cvar_minus_observability_proxy_mean  robust_coverage_cvar_minus_observability_proxy_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_greedy_d_logdet_mean  robust_coverage_cvar_minus_greedy_d_logdet_std  robust_coverage_cvar_minus_graph_sampling_laplacian_mean  robust_coverage_cvar_minus_graph_sampling_laplacian_std  robust_coverage_cvar_minus_qr_pod_modes_mean  robust_coverage_cvar_minus_qr_pod_modes_std  robust_coverage_cvar_minus_scenario_cvar_a_trace_mean  robust_coverage_cvar_minus_scenario_cvar_a_trace_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std
    0.1                                   -0.243057                                   0.050225                                                      -0.123054                                                      0.058002                                         -0.140356                                         0.081935                                                -0.411284                                                0.078503                                           -0.095923                                           0.073720                                            -0.965389                                            0.346166                                                     -0.542819                                                     0.265789                                         -0.386881                                         0.095378                                                  -0.198379                                                  0.100377                                                          -0.004469                                                          0.057732                                                    -0.052698                                                    0.071804                        -0.228131                        0.061400                                           -0.108128                                           0.053601                              -0.125430                              0.097271                                     -0.396358                                     0.083508                                -0.080997                                0.072634                                 -0.950463                                 0.353226                                          -0.527893                                          0.280862                              -0.371955                              0.106064                                       -0.183453                                       0.121468                                                0.010457                                               0.043933                                         -0.037772                                         0.050065                               -0.097403                               0.082196                                                   0.022600                                                  0.102749                                      0.005298                                     0.116594                                            -0.265630                                            0.123507                                        0.049731                                       0.113978                                        -0.819734                                        0.389903                                                 -0.397165                                                 0.254906                                     -0.241227                                     0.093385                                              -0.052725                                              0.143535                                                       0.141185                                                      0.105649                                                 0.092956                                                0.090114
    0.2                                   -0.219871                                   0.060822                                                      -0.094821                                                      0.082305                                         -0.072923                                         0.056110                                                -0.568919                                                0.066519                                           -0.110701                                           0.058130                                            -0.823549                                            0.197610                                                     -0.637021                                                     0.169237                                         -0.429354                                         0.136916                                                  -0.229920                                                  0.129602                                                          -0.042265                                                          0.077947                                                    -0.097016                                                    0.072131                        -0.181086                        0.063724                                           -0.056037                                           0.065730                              -0.034138                              0.084255                                     -0.530135                                     0.083643                                -0.071917                                0.047492                                 -0.784764                                 0.218861                                          -0.598237                                          0.171438                              -0.390569                              0.137270                                       -0.191136                                       0.156312                                               -0.003480                                               0.048288                                         -0.058232                                         0.044473                               -0.092476                               0.094935                                                   0.032574                                                  0.100826                                      0.054473                                     0.123357                                            -0.441524                                            0.126546                                        0.016694                                       0.119749                                        -0.696153                                        0.249665                                                 -0.509626                                                 0.263651                                     -0.301959                                     0.189386                                              -0.102525                                              0.128297                                                       0.085131                                                      0.119527                                                 0.030379                                                0.095782
    0.3                                   -0.319507                                   0.064389                                                      -0.162720                                                      0.097499                                         -0.116168                                         0.096797                                                -0.802947                                                0.155960                                           -0.266419                                           0.104302                                            -0.795034                                            0.217080                                                     -0.720617                                                     0.173559                                         -0.362280                                         0.097205                                                  -0.317564                                                  0.155910                                                          -0.119999                                                          0.086798                                                    -0.215799                                                    0.070948                        -0.221173                        0.066614                                           -0.064387                                           0.095539                              -0.017835                              0.107747                                     -0.704614                                     0.140188                                -0.168086                                0.085783                                 -0.696700                                 0.186006                                          -0.622284                                          0.172832                              -0.263947                              0.109288                                       -0.219231                                       0.147859                                               -0.021666                                               0.051030                                         -0.117466                                         0.074546                               -0.098010                               0.113571                                                   0.058777                                                  0.094604                                      0.105329                                     0.156616                                            -0.581450                                            0.170909                                       -0.044922                                       0.131937                                        -0.573536                                        0.224938                                                 -0.499120                                                 0.192723                                     -0.140783                                     0.139562                                              -0.096067                                              0.088603                                                       0.101498                                                      0.128636                                                 0.005698                                                0.126807
```

## Winner counts

```
 budget                   best_layout  wins
    0.1 multistart_swap_by_validation     2
    0.1          robust_coverage_cvar     1
    0.1      swap_from_greedy_a_trace     2
    0.1    swap_from_scenario_average     1
    0.1       swap_from_scenario_cvar     1
    0.1      validation_swap_selected     3
    0.2 multistart_swap_by_validation     2
    0.2                        random     1
    0.2          robust_coverage_cvar     1
    0.2                  top_variance     1
    0.2      validation_swap_selected     5
    0.3                        random     1
    0.3                  top_variance     1
    0.3      validation_swap_selected     8
```

## Main ablation layouts

```
 budget                   layout_type     mean      std  count
    0.1      validation_swap_selected 3.590056 0.307260     10
    0.1 multistart_swap_by_validation 3.594525 0.324835     10
    0.1                 rcss_selected 3.604982 0.293286     10
    0.1                greedy_a_trace 3.685979 0.343436     10
    0.1     best_random_by_validation 3.713110 0.323978     10
    0.1                  top_variance 3.730412 0.341240     10
    0.1         scenario_cvar_a_trace 3.788435 0.363404     10
    0.1                  qr_pod_modes 3.976937 0.335897     10
    0.1           observability_proxy 4.001340 0.321938     10
    0.1      graph_sampling_laplacian 4.132875 0.506233     10
    0.1               greedy_d_logdet 4.555445 0.611738     10
    0.2      validation_swap_selected 3.354688 0.312941     10
    0.2                 rcss_selected 3.393473 0.290102     10
    0.2 multistart_swap_by_validation 3.396952 0.304817     10
    0.2                  top_variance 3.427610 0.338372     10
    0.2     best_random_by_validation 3.449509 0.290911     10
    0.2                greedy_a_trace 3.465389 0.323998     10
    0.2         scenario_cvar_a_trace 3.584608 0.340429     10
    0.2                  qr_pod_modes 3.784042 0.372491     10
    0.2           observability_proxy 3.923607 0.330187     10
    0.2      graph_sampling_laplacian 3.991709 0.444776     10
    0.2               greedy_d_logdet 4.178236 0.478752     10
    0.3      validation_swap_selected 3.084223 0.239671     10
    0.3                 rcss_selected 3.182557 0.279200     10
    0.3                  top_variance 3.200391 0.291698     10
    0.3 multistart_swap_by_validation 3.204223 0.294221     10
    0.3     best_random_by_validation 3.246943 0.236188     10
    0.3                greedy_a_trace 3.350643 0.309428     10
    0.3         scenario_cvar_a_trace 3.401787 0.296027     10
    0.3                  qr_pod_modes 3.446503 0.314999     10
    0.3      graph_sampling_laplacian 3.804840 0.390244     10
    0.3               greedy_d_logdet 3.879257 0.435774     10
    0.3           observability_proxy 3.887171 0.358241     10
```

## Paired delta tests

```
 budget                   layout                      baseline  delta_mean  delta_std  delta_sem  ci95_low  ci95_high  cohens_dz   paired_t_p  wilcoxon_p  win_count  count
    0.1 validation_swap_selected                        random   -0.243057   0.050225   0.015883 -0.278986  -0.207128  -4.839358 9.479071e-08    0.001953         10     10
    0.1 validation_swap_selected     best_random_by_validation   -0.123054   0.058002   0.018342 -0.164546  -0.081562  -2.121552 8.764091e-05    0.001953         10     10
    0.1 validation_swap_selected                  top_variance   -0.140356   0.081935   0.025910 -0.198969  -0.081743  -1.713010 4.234854e-04    0.001953         10     10
    0.1 validation_swap_selected           observability_proxy   -0.411284   0.078503   0.024825 -0.467442  -0.355126  -5.239079 4.745070e-08    0.001953         10     10
    0.1 validation_swap_selected                greedy_a_trace   -0.095923   0.073720   0.023312 -0.148659  -0.043187  -1.301178 2.618626e-03    0.001953         10     10
    0.1 validation_swap_selected               greedy_d_logdet   -0.965389   0.346166   0.109467 -1.213021  -0.717756  -2.788805 1.007891e-05    0.001953         10     10
    0.1 validation_swap_selected      graph_sampling_laplacian   -0.542819   0.265789   0.084050 -0.732953  -0.352685  -2.042290 1.170031e-04    0.001953         10     10
    0.1 validation_swap_selected                  qr_pod_modes   -0.386881   0.095378   0.030161 -0.455111  -0.318651  -4.056276 4.355816e-07    0.001953         10     10
    0.1 validation_swap_selected         scenario_cvar_a_trace   -0.198379   0.100377   0.031742 -0.270185  -0.126574  -1.976340 1.496818e-04    0.001953         10     10
    0.1 validation_swap_selected multistart_swap_by_validation   -0.004469   0.057732   0.018257 -0.045768   0.036830  -0.077413 8.121002e-01    0.769531          5     10
    0.1 validation_swap_selected       swap_from_scenario_cvar   -0.052698   0.071804   0.022706 -0.104063  -0.001332  -0.733911 4.542402e-02    0.130859          7     10
    0.1            rcss_selected                        random   -0.228131   0.061400   0.019416 -0.272054  -0.184208  -3.715495 9.214294e-07    0.001953         10     10
    0.1            rcss_selected     best_random_by_validation   -0.108128   0.053601   0.016950 -0.146471  -0.069784  -2.017289 1.283720e-04    0.001953         10     10
    0.1            rcss_selected                  top_variance   -0.125430   0.097271   0.030760 -0.195014  -0.055847  -1.289493 2.767391e-03    0.001953         10     10
    0.1            rcss_selected           observability_proxy   -0.396358   0.083508   0.026407 -0.456096  -0.336621  -4.746378 1.122004e-07    0.001953         10     10
    0.1            rcss_selected                greedy_a_trace   -0.080997   0.072634   0.022969 -0.132956  -0.029037  -1.115127 6.450890e-03    0.003906          9     10
    0.1            rcss_selected               greedy_d_logdet   -0.950463   0.353226   0.111700 -1.203145  -0.697780  -2.690809 1.347704e-05    0.001953         10     10
    0.1            rcss_selected      graph_sampling_laplacian   -0.527893   0.280862   0.088816 -0.728810  -0.326976  -1.879544 2.170363e-04    0.001953         10     10
    0.1            rcss_selected                  qr_pod_modes   -0.371955   0.106064   0.033540 -0.447828  -0.296081  -3.506898 1.503212e-06    0.001953         10     10
    0.1            rcss_selected         scenario_cvar_a_trace   -0.183453   0.121468   0.038411 -0.270346  -0.096561  -1.510305 1.006881e-03    0.003906          9     10
    0.1            rcss_selected multistart_swap_by_validation    0.010457   0.043933   0.013893 -0.020971   0.041885   0.238016 4.708751e-01    0.460938          4     10
    0.1            rcss_selected       swap_from_scenario_cvar   -0.037772   0.050065   0.015832 -0.073586  -0.001957  -0.754452 4.083842e-02    0.164062          5     10
    0.1     robust_coverage_cvar                        random   -0.097403   0.082196   0.025993 -0.156203  -0.038604  -1.185007 4.573537e-03    0.005859          9     10
    0.1     robust_coverage_cvar     best_random_by_validation    0.022600   0.102749   0.032492 -0.050902   0.096102   0.219956 5.042651e-01    0.431641          4     10
    0.1     robust_coverage_cvar                  top_variance    0.005298   0.116594   0.036870 -0.078108   0.088704   0.045438 8.889140e-01    0.921875          4     10
    0.1     robust_coverage_cvar           observability_proxy   -0.265630   0.123507   0.039056 -0.353981  -0.177279  -2.150737 7.894468e-05    0.001953         10     10
    0.1     robust_coverage_cvar                greedy_a_trace    0.049731   0.113978   0.036043 -0.031804   0.131267   0.436325 2.009641e-01    0.193359          2     10
    0.1     robust_coverage_cvar               greedy_d_logdet   -0.819734   0.389903   0.123298 -1.098654  -0.540815  -2.102408 9.391045e-05    0.001953         10     10
    0.1     robust_coverage_cvar      graph_sampling_laplacian   -0.397165   0.254906   0.080608 -0.579514  -0.214816  -1.558085 8.165950e-04    0.001953         10     10
    0.1     robust_coverage_cvar                  qr_pod_modes   -0.241227   0.093385   0.029531 -0.308031  -0.174423  -2.583133 1.873063e-05    0.001953         10     10
    0.1     robust_coverage_cvar         scenario_cvar_a_trace   -0.052725   0.143535   0.045390 -0.155404   0.049953  -0.367334 2.752724e-01    0.275391          7     10
    0.1     robust_coverage_cvar multistart_swap_by_validation    0.141185   0.105649   0.033409  0.065608   0.216761   1.336361 2.219863e-03    0.005859          1     10
    0.1     robust_coverage_cvar       swap_from_scenario_cvar    0.092956   0.090114   0.028497  0.028492   0.157420   1.031537 9.807215e-03    0.009766          1     10
    0.2 validation_swap_selected                        random   -0.219871   0.060822   0.019234 -0.263380  -0.176362  -3.615013 1.162783e-06    0.001953         10     10
    0.2 validation_swap_selected     best_random_by_validation   -0.094821   0.082305   0.026027 -0.153699  -0.035944  -1.152079 5.374118e-03    0.005859          9     10
    0.2 validation_swap_selected                  top_variance   -0.072923   0.056110   0.017744 -0.113061  -0.032784  -1.299631 2.637824e-03    0.005859          9     10
    0.2 validation_swap_selected           observability_proxy   -0.568919   0.066519   0.021035 -0.616504  -0.521335  -8.552757 6.254431e-10    0.001953         10     10
    0.2 validation_swap_selected                greedy_a_trace   -0.110701   0.058130   0.018382 -0.152285  -0.069117  -1.904360 1.970874e-04    0.001953         10     10
    0.2 validation_swap_selected               greedy_d_logdet   -0.823549   0.197610   0.062490 -0.964910  -0.682187  -4.167548 3.452676e-07    0.001953         10     10
    0.2 validation_swap_selected      graph_sampling_laplacian   -0.637021   0.169237   0.053517 -0.758086  -0.515957  -3.764082 8.250390e-07    0.001953         10     10
    0.2 validation_swap_selected                  qr_pod_modes   -0.429354   0.136916   0.043296 -0.527298  -0.331411  -3.135905 3.836405e-06    0.001953         10     10
    0.2 validation_swap_selected         scenario_cvar_a_trace   -0.229920   0.129602   0.040984 -0.322632  -0.137209  -1.774054 3.300019e-04    0.001953         10     10
    0.2 validation_swap_selected multistart_swap_by_validation   -0.042265   0.077947   0.024649 -0.098025   0.013495  -0.542221 1.205510e-01    0.193359          7     10
    0.2 validation_swap_selected       swap_from_scenario_cvar   -0.097016   0.072131   0.022810 -0.148615  -0.045417  -1.345008 2.132113e-03    0.001953         10     10
    0.2            rcss_selected                        random   -0.181086   0.063724   0.020151 -0.226672  -0.135501  -2.841753 8.644230e-06    0.001953         10     10
    0.2            rcss_selected     best_random_by_validation   -0.056037   0.065730   0.020786 -0.103057  -0.009017  -0.852532 2.455627e-02    0.027344          8     10
    0.2            rcss_selected                  top_variance   -0.034138   0.084255   0.026644 -0.094410   0.026135  -0.405171 2.321270e-01    0.250000          6     10
    0.2            rcss_selected           observability_proxy   -0.530135   0.083643   0.026450 -0.589970  -0.470300  -6.338028 8.910700e-09    0.001953         10     10
    0.2            rcss_selected                greedy_a_trace   -0.071917   0.047492   0.015018 -0.105890  -0.037943  -1.514303 9.892614e-04    0.009766          8     10
    0.2            rcss_selected               greedy_d_logdet   -0.784764   0.218861   0.069210 -0.941328  -0.628200  -3.585665 1.245886e-06    0.001953         10     10
    0.2            rcss_selected      graph_sampling_laplacian   -0.598237   0.171438   0.054214 -0.720876  -0.475597  -3.489514 1.567592e-06    0.001953         10     10
    0.2            rcss_selected                  qr_pod_modes   -0.390569   0.137270   0.043409 -0.488766  -0.292372  -2.845264 8.557369e-06    0.001953         10     10
    0.2            rcss_selected         scenario_cvar_a_trace   -0.191136   0.156312   0.049430 -0.302955  -0.079317  -1.222781 3.807483e-03    0.005859          9     10
    0.2            rcss_selected multistart_swap_by_validation   -0.003480   0.048288   0.015270 -0.038023   0.031063  -0.072065 8.248255e-01    1.000000          2     10
    0.2            rcss_selected       swap_from_scenario_cvar   -0.058232   0.044473   0.014064 -0.090046  -0.026417  -1.309355 2.519592e-03    0.005859          9     10
    0.2     robust_coverage_cvar                        random   -0.092476   0.094935   0.030021 -0.160388  -0.024564  -0.974100 1.313201e-02    0.019531          8     10
    0.2     robust_coverage_cvar     best_random_by_validation    0.032574   0.100826   0.031884 -0.039553   0.104700   0.323069 3.336291e-01    0.322266          3     10
    0.2     robust_coverage_cvar                  top_variance    0.054473   0.123357   0.039009 -0.033772   0.142717   0.441584 1.960711e-01    0.130859          3     10
    0.2     robust_coverage_cvar           observability_proxy   -0.441524   0.126546   0.040017 -0.532050  -0.350999  -3.489033 1.569416e-06    0.001953         10     10
    0.2     robust_coverage_cvar                greedy_a_trace    0.016694   0.119749   0.037868 -0.068969   0.102357   0.139407 6.697262e-01    0.431641          4     10
    0.2     robust_coverage_cvar               greedy_d_logdet   -0.696153   0.249665   0.078951 -0.874753  -0.517554  -2.788347 1.009240e-05    0.001953         10     10
    0.2     robust_coverage_cvar      graph_sampling_laplacian   -0.509626   0.263651   0.083374 -0.698231  -0.321022  -1.932960 1.765361e-04    0.001953         10     10
    0.2     robust_coverage_cvar                  qr_pod_modes   -0.301959   0.189386   0.059889 -0.437437  -0.166480  -1.594412 6.979122e-04    0.001953         10     10
    0.2     robust_coverage_cvar         scenario_cvar_a_trace   -0.102525   0.128297   0.040571 -0.194304  -0.010747  -0.799123 3.239183e-02    0.037109          7     10
    0.2     robust_coverage_cvar multistart_swap_by_validation    0.085131   0.119527   0.037798 -0.000374   0.170635   0.712231 5.081436e-02    0.064453          2     10
    0.2     robust_coverage_cvar       swap_from_scenario_cvar    0.030379   0.095782   0.030289 -0.038140   0.098897   0.317166 3.420783e-01    0.375000          4     10
    0.3 validation_swap_selected                        random   -0.319507   0.064389   0.020361 -0.365568  -0.273446  -4.962173 7.621277e-08    0.001953         10     10
    0.3 validation_swap_selected     best_random_by_validation   -0.162720   0.097499   0.030832 -0.232467  -0.092973  -1.668937 5.086896e-04    0.003906          9     10
    0.3 validation_swap_selected                  top_variance   -0.116168   0.096797   0.030610 -0.185413  -0.046923  -1.200113 4.249282e-03    0.013672          9     10
    0.3 validation_swap_selected           observability_proxy   -0.802947   0.155960   0.049319 -0.914514  -0.691381  -5.148429 5.526637e-08    0.001953         10     10
    0.3 validation_swap_selected                greedy_a_trace   -0.266419   0.104302   0.032983 -0.341033  -0.191806  -2.554312 2.049337e-05    0.001953         10     10
    0.3 validation_swap_selected               greedy_d_logdet   -0.795034   0.217080   0.068647 -0.950323  -0.639744  -3.662402 1.041220e-06    0.001953         10     10
    0.3 validation_swap_selected      graph_sampling_laplacian   -0.720617   0.173559   0.054884 -0.844774  -0.596461  -4.152007 3.565348e-07    0.001953         10     10
    0.3 validation_swap_selected                  qr_pod_modes   -0.362280   0.097205   0.030739 -0.431816  -0.292744  -3.726981 8.975679e-07    0.001953         10     10
    0.3 validation_swap_selected         scenario_cvar_a_trace   -0.317564   0.155910   0.049303 -0.429095  -0.206033  -2.036841 1.193840e-04    0.001953         10     10
    0.3 validation_swap_selected multistart_swap_by_validation   -0.119999   0.086798   0.027448 -0.182091  -0.057908  -1.382511 1.792166e-03    0.003906          9     10
    0.3 validation_swap_selected       swap_from_scenario_cvar   -0.215799   0.070948   0.022436 -0.266552  -0.165046  -3.041637 4.941503e-06    0.001953         10     10
    0.3            rcss_selected                        random   -0.221173   0.066614   0.021065 -0.268826  -0.173520  -3.320210 2.381618e-06    0.001953         10     10
    0.3            rcss_selected     best_random_by_validation   -0.064387   0.095539   0.030212 -0.132731   0.003958  -0.673930 6.190542e-02    0.074219          6     10
    0.3            rcss_selected                  top_variance   -0.017835   0.107747   0.034073 -0.094912   0.059243  -0.165522 6.133206e-01    0.769531          6     10
    0.3            rcss_selected           observability_proxy   -0.704614   0.140188   0.044331 -0.804898  -0.604330  -5.026220 6.815368e-08    0.001953         10     10
    0.3            rcss_selected                greedy_a_trace   -0.168086   0.085783   0.027127 -0.229451  -0.106721  -1.959444 1.595718e-04    0.001953         10     10
    0.3            rcss_selected               greedy_d_logdet   -0.696700   0.186006   0.058820 -0.829761  -0.563640  -3.745586 8.603526e-07    0.001953         10     10
    0.3            rcss_selected      graph_sampling_laplacian   -0.622284   0.172832   0.054654 -0.745920  -0.498647  -3.600506 1.203070e-06    0.001953         10     10
    0.3            rcss_selected                  qr_pod_modes   -0.263947   0.109288   0.034560 -0.342127  -0.185767  -2.415147 3.200246e-05    0.001953         10     10
    0.3            rcss_selected         scenario_cvar_a_trace   -0.219231   0.147859   0.046757 -0.325003  -0.113458  -1.482696 1.138155e-03    0.005859          9     10
    0.3            rcss_selected multistart_swap_by_validation   -0.021666   0.051030   0.016137 -0.058170   0.014838  -0.424577 2.122719e-01    0.312500          4     10
    0.3            rcss_selected       swap_from_scenario_cvar   -0.117466   0.074546   0.023573 -0.170792  -0.064139  -1.575754 7.563594e-04    0.001953         10     10
    0.3     robust_coverage_cvar                        random   -0.098010   0.113571   0.035914 -0.179253  -0.016766  -0.862984 2.326275e-02    0.037109          9     10
    0.3     robust_coverage_cvar     best_random_by_validation    0.058777   0.094604   0.029916 -0.008898   0.126453   0.621300 8.102687e-02    0.048828          2     10
    0.3     robust_coverage_cvar                  top_variance    0.105329   0.156616   0.049526 -0.006707   0.217366   0.672533 6.235148e-02    0.105469          3     10
    0.3     robust_coverage_cvar           observability_proxy   -0.581450   0.170909   0.054046 -0.703711  -0.459189  -3.402099 1.941045e-06    0.001953         10     10
    0.3     robust_coverage_cvar                greedy_a_trace   -0.044922   0.131937   0.041722 -0.139304   0.049460  -0.340482 3.096288e-01    0.322266          7     10
    0.3     robust_coverage_cvar               greedy_d_logdet   -0.573536   0.224938   0.071132 -0.734447  -0.412626  -2.549757 2.078829e-05    0.001953         10     10
    0.3     robust_coverage_cvar      graph_sampling_laplacian   -0.499120   0.192723   0.060944 -0.636986  -0.361254  -2.589828 1.834540e-05    0.001953         10     10
    0.3     robust_coverage_cvar                  qr_pod_modes   -0.140783   0.139562   0.044133 -0.240619  -0.040947  -1.008751 1.100746e-02    0.019531          8     10
    0.3     robust_coverage_cvar         scenario_cvar_a_trace   -0.096067   0.088603   0.028019 -0.159450  -0.032684  -1.084236 7.524208e-03    0.019531          8     10
    0.3     robust_coverage_cvar multistart_swap_by_validation    0.101498   0.128636   0.040678  0.009477   0.193519   0.789032 3.413297e-02    0.064453          2     10
    0.3     robust_coverage_cvar       swap_from_scenario_cvar    0.005698   0.126807   0.040100 -0.085014   0.096410   0.044937 8.901279e-01    0.769531          5     10
```

## Empirical certificate-error correlation summary

These correlations are empirical support for certificate-guided selection, not formal optimality guarantees.

```
                           pearson_mae                                     spearman_mae                                    
                                  mean       std       min       max count         mean       std       min       max count
method  certificate                                                                                                        
gls_map condition_number      0.812945  0.021001  0.778407  0.837528    10     0.854770  0.018890  0.811085  0.876709    10
        information_logdet   -0.701884  0.034823 -0.753767 -0.651900    10    -0.762494  0.025871 -0.800563 -0.709932    10
        posterior_trace       0.793096  0.024477  0.754966  0.834510    10     0.806771  0.020481  0.772722  0.838337    10
gsp     condition_number      0.150154  0.116605 -0.030651  0.307676    10     0.177874  0.149050 -0.107048  0.357253    10
        information_logdet   -0.176980  0.118805 -0.309802  0.017571    10    -0.203582  0.139144 -0.370364  0.052105    10
        posterior_trace       0.147813  0.116857 -0.030891  0.302893    10     0.160682  0.146824 -0.097422  0.320527    10
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.1                greedy_a_trace               1
    0.1 multistart_swap_by_validation               2
    0.1   swap_from_best_random_trace               1
    0.1      swap_from_greedy_a_trace               2
    0.1    swap_from_scenario_average               3
    0.1       swap_from_scenario_cvar               1
    0.2 multistart_swap_by_validation               4
    0.2       quality_coverage_sample               3
    0.2   swap_from_best_random_trace               1
    0.2    swap_from_scenario_average               1
    0.2                  top_variance               1
    0.3 multistart_swap_by_validation               4
    0.3       quality_coverage_sample               4
    0.3        random_validation_pool               1
    0.3          robust_coverage_cvar               1
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