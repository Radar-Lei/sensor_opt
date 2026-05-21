---
status: complete
---

# TRACE-SL RCSS Multi-Split Summary

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type     mean      std  count
    0.1      swap_from_greedy_a_trace 3.619095 0.206838      5
    0.1                greedy_a_trace 3.637739 0.220265      5
    0.1                 rcss_selected 3.644631 0.226200      5
    0.1      validation_swap_selected 3.655732 0.211662      5
    0.1 multistart_swap_by_validation 3.663893 0.209326      5
    0.1   swap_from_best_random_trace 3.688951 0.207948      5
    0.1       swap_from_scenario_cvar 3.692000 0.216493      5
    0.1    swap_from_scenario_average 3.729011 0.240729      5
    0.1     best_random_by_validation 3.743681 0.165420      5
    0.1          best_random_by_trace 3.783470 0.184906      5
    0.1          robust_coverage_cvar 3.787271 0.232012      5
    0.1         scenario_cvar_a_trace 3.823979 0.219275      5
    0.1                        random 3.826582 0.207817    500
    0.1                      coverage 3.839264 0.229479      5
    0.1                  top_variance 3.860194 0.277267      5
    0.1      scenario_average_a_trace 3.885937 0.261603      5
    0.1               greedy_d_logdet 4.333899 0.257939      5
    0.1                        degree 4.336862 0.308732      5
    0.2      swap_from_greedy_a_trace 3.253191 0.175987      5
    0.2                 rcss_selected 3.254124 0.180032      5
    0.2      validation_swap_selected 3.254730 0.182516      5
    0.2                greedy_a_trace 3.264202 0.184572      5
    0.2 multistart_swap_by_validation 3.343502 0.175863      5
    0.2       swap_from_scenario_cvar 3.391740 0.204996      5
    0.2    swap_from_scenario_average 3.402565 0.199598      5
    0.2   swap_from_best_random_trace 3.414027 0.170021      5
    0.2          robust_coverage_cvar 3.461746 0.199687      5
    0.2     best_random_by_validation 3.465260 0.155791      5
    0.2         scenario_cvar_a_trace 3.502703 0.216791      5
    0.2          best_random_by_trace 3.508289 0.191518      5
    0.2                      coverage 3.529206 0.199817      5
    0.2      scenario_average_a_trace 3.529479 0.200171      5
    0.2                        random 3.531680 0.178114    500
    0.2                  top_variance 3.585931 0.220529      5
    0.2               greedy_d_logdet 3.759441 0.213729      5
    0.2                        degree 4.197434 0.264373      5
    0.3      validation_swap_selected 2.995122 0.161954      5
    0.3      swap_from_greedy_a_trace 3.003493 0.162437      5
    0.3                 rcss_selected 3.006400 0.166303      5
    0.3                greedy_a_trace 3.014488 0.165428      5
    0.3 multistart_swap_by_validation 3.134239 0.138551      5
    0.3    swap_from_scenario_average 3.179775 0.170155      5
    0.3   swap_from_best_random_trace 3.201813 0.144261      5
    0.3       swap_from_scenario_cvar 3.215764 0.172050      5
    0.3     best_random_by_validation 3.248253 0.133058      5
    0.3          robust_coverage_cvar 3.278510 0.163825      5
    0.3          best_random_by_trace 3.318273 0.143176      5
    0.3                  top_variance 3.326630 0.160218      5
    0.3                        random 3.330918 0.155821    500
    0.3      scenario_average_a_trace 3.331107 0.183490      5
    0.3               greedy_d_logdet 3.343868 0.193844      5
    0.3         scenario_cvar_a_trace 3.349702 0.179944      5
    0.3                      coverage 3.386941 0.176039      5
    0.3                        degree 4.057302 0.234881      5
```

## RCSS deltas, negative is better

```
 budget  validation_swap_selected_minus_random_mean  validation_swap_selected_minus_random_std  validation_swap_selected_minus_best_random_by_validation_mean  validation_swap_selected_minus_best_random_by_validation_std  validation_swap_selected_minus_top_variance_mean  validation_swap_selected_minus_top_variance_std  validation_swap_selected_minus_greedy_a_trace_mean  validation_swap_selected_minus_greedy_a_trace_std  validation_swap_selected_minus_scenario_cvar_a_trace_mean  validation_swap_selected_minus_scenario_cvar_a_trace_std  validation_swap_selected_minus_multistart_swap_by_validation_mean  validation_swap_selected_minus_multistart_swap_by_validation_std  validation_swap_selected_minus_swap_from_scenario_cvar_mean  validation_swap_selected_minus_swap_from_scenario_cvar_std  rcss_selected_minus_random_mean  rcss_selected_minus_random_std  rcss_selected_minus_best_random_by_validation_mean  rcss_selected_minus_best_random_by_validation_std  rcss_selected_minus_top_variance_mean  rcss_selected_minus_top_variance_std  rcss_selected_minus_greedy_a_trace_mean  rcss_selected_minus_greedy_a_trace_std  rcss_selected_minus_scenario_cvar_a_trace_mean  rcss_selected_minus_scenario_cvar_a_trace_std  rcss_selected_minus_multistart_swap_by_validation_mean  rcss_selected_minus_multistart_swap_by_validation_std  rcss_selected_minus_swap_from_scenario_cvar_mean  rcss_selected_minus_swap_from_scenario_cvar_std  robust_coverage_cvar_minus_random_mean  robust_coverage_cvar_minus_random_std  robust_coverage_cvar_minus_best_random_by_validation_mean  robust_coverage_cvar_minus_best_random_by_validation_std  robust_coverage_cvar_minus_top_variance_mean  robust_coverage_cvar_minus_top_variance_std  robust_coverage_cvar_minus_greedy_a_trace_mean  robust_coverage_cvar_minus_greedy_a_trace_std  robust_coverage_cvar_minus_scenario_cvar_a_trace_mean  robust_coverage_cvar_minus_scenario_cvar_a_trace_std  robust_coverage_cvar_minus_multistart_swap_by_validation_mean  robust_coverage_cvar_minus_multistart_swap_by_validation_std  robust_coverage_cvar_minus_swap_from_scenario_cvar_mean  robust_coverage_cvar_minus_swap_from_scenario_cvar_std
    0.1                                   -0.170850                                   0.028768                                                      -0.087949                                                      0.053428                                         -0.204462                                         0.077112                                            0.017993                                           0.033128                                                  -0.168247                                                  0.023615                                                          -0.008161                                                          0.026782                                                    -0.036269                                                    0.018239                        -0.181951                        0.031323                                           -0.099049                                           0.064998                              -0.215563                              0.076981                                 0.006893                                0.023519                                       -0.179347                                       0.012440                                               -0.019262                                               0.032438                                         -0.047369                                         0.021910                               -0.039312                               0.025085                                                   0.043590                                                  0.072494                                     -0.072924                                     0.059169                                        0.149532                                       0.035869                                              -0.036708                                              0.028659                                                       0.123377                                                      0.035967                                                 0.095270                                                0.025427
    0.2                                   -0.276950                                   0.029180                                                      -0.210530                                                      0.050157                                         -0.331201                                         0.058708                                           -0.009472                                           0.006353                                                  -0.247973                                                  0.036456                                                          -0.088772                                                          0.021768                                                    -0.137010                                                    0.024543                        -0.277555                        0.034926                                           -0.211136                                           0.051643                              -0.331806                              0.062879                                -0.010078                                0.011150                                       -0.248578                                       0.041088                                               -0.089377                                               0.024464                                         -0.137615                                         0.029348                               -0.069933                               0.047763                                                  -0.003514                                                  0.067251                                     -0.124184                                     0.071094                                        0.197544                                       0.061040                                              -0.040956                                              0.056352                                                       0.118245                                                      0.051061                                                 0.070007                                                0.054609
    0.3                                   -0.335796                                   0.021486                                                      -0.253131                                                      0.038791                                         -0.331508                                         0.049945                                           -0.019365                                           0.017531                                                  -0.354580                                                  0.026769                                                          -0.139117                                                          0.031062                                                    -0.220642                                                    0.029192                        -0.324518                        0.019053                                           -0.241854                                           0.041773                              -0.320230                              0.047713                                -0.008088                                0.013848                                       -0.343303                                       0.022122                                               -0.127840                                               0.035795                                         -0.209365                                         0.023135                               -0.052408                               0.050173                                                   0.030257                                                  0.051060                                     -0.048119                                     0.061136                                        0.264023                                       0.058607                                              -0.071192                                              0.056943                                                       0.144271                                                      0.051258                                                 0.062746                                                0.063774
```

## Winner counts

```
 budget              best_layout  wins
    0.1           greedy_a_trace     1
    0.1 swap_from_greedy_a_trace     4
    0.2 swap_from_greedy_a_trace     4
    0.2 validation_swap_selected     1
    0.3           greedy_a_trace     1
    0.3 validation_swap_selected     4
```

## Main ablation layouts

```
 budget               layout_type     mean      std  count
    0.1            greedy_a_trace 3.637739 0.220265      5
    0.1             rcss_selected 3.644631 0.226200      5
    0.1  validation_swap_selected 3.655732 0.211662      5
    0.1 best_random_by_validation 3.743681 0.165420      5
    0.1     scenario_cvar_a_trace 3.823979 0.219275      5
    0.1              top_variance 3.860194 0.277267      5
    0.2             rcss_selected 3.254124 0.180032      5
    0.2  validation_swap_selected 3.254730 0.182516      5
    0.2            greedy_a_trace 3.264202 0.184572      5
    0.2 best_random_by_validation 3.465260 0.155791      5
    0.2     scenario_cvar_a_trace 3.502703 0.216791      5
    0.2              top_variance 3.585931 0.220529      5
    0.3  validation_swap_selected 2.995122 0.161954      5
    0.3             rcss_selected 3.006400 0.166303      5
    0.3            greedy_a_trace 3.014488 0.165428      5
    0.3 best_random_by_validation 3.248253 0.133058      5
    0.3              top_variance 3.326630 0.160218      5
    0.3     scenario_cvar_a_trace 3.349702 0.179944      5
```

## Paired delta tests

```
 budget                   layout                      baseline  delta_mean  delta_std  win_count  count  paired_t_p  wilcoxon_p
    0.1 validation_swap_selected                        random   -0.170850   0.028768          5      5    0.000186      0.0625
    0.1 validation_swap_selected     best_random_by_validation   -0.087949   0.053428          5      5    0.021189      0.0625
    0.1 validation_swap_selected                  top_variance   -0.204462   0.077112          5      5    0.004056      0.0625
    0.1 validation_swap_selected                greedy_a_trace    0.017993   0.033128          1      5    0.291356      0.3125
    0.1 validation_swap_selected         scenario_cvar_a_trace   -0.168247   0.023615          5      5    0.000091      0.0625
    0.1 validation_swap_selected multistart_swap_by_validation   -0.008161   0.026782          3      5    0.533033      0.4375
    0.1 validation_swap_selected       swap_from_scenario_cvar   -0.036269   0.018239          5      5    0.011278      0.0625
    0.1            rcss_selected                        random   -0.181951   0.031323          5      5    0.000203      0.0625
    0.1            rcss_selected     best_random_by_validation   -0.099049   0.064998          5      5    0.027089      0.0625
    0.1            rcss_selected                  top_variance   -0.215563   0.076981          5      5    0.003319      0.0625
    0.1            rcss_selected                greedy_a_trace    0.006893   0.023519          2      5    0.548041      1.0000
    0.1            rcss_selected         scenario_cvar_a_trace   -0.179347   0.012440          5      5    0.000006      0.0625
    0.1            rcss_selected multistart_swap_by_validation   -0.019262   0.032438          2      5    0.254956      0.5000
    0.1            rcss_selected       swap_from_scenario_cvar   -0.047369   0.021910          5      5    0.008434      0.0625
    0.1     robust_coverage_cvar                        random   -0.039312   0.025085          5      5    0.024802      0.0625
    0.1     robust_coverage_cvar     best_random_by_validation    0.043590   0.072494          1      5    0.249961      0.3125
    0.1     robust_coverage_cvar                  top_variance   -0.072924   0.059169          5      5    0.051065      0.0625
    0.1     robust_coverage_cvar                greedy_a_trace    0.149532   0.035869          0      5    0.000737      0.0625
    0.1     robust_coverage_cvar         scenario_cvar_a_trace   -0.036708   0.028659          4      5    0.045741      0.1250
    0.1     robust_coverage_cvar multistart_swap_by_validation    0.123377   0.035967          0      5    0.001553      0.0625
    0.1     robust_coverage_cvar       swap_from_scenario_cvar    0.095270   0.025427          0      5    0.001110      0.0625
    0.2 validation_swap_selected                        random   -0.276950   0.029180          5      5    0.000029      0.0625
    0.2 validation_swap_selected     best_random_by_validation   -0.210530   0.050157          5      5    0.000718      0.0625
    0.2 validation_swap_selected                  top_variance   -0.331201   0.058708          5      5    0.000227      0.0625
    0.2 validation_swap_selected                greedy_a_trace   -0.009472   0.006353          5      5    0.028993      0.0625
    0.2 validation_swap_selected         scenario_cvar_a_trace   -0.247973   0.036456          5      5    0.000109      0.0625
    0.2 validation_swap_selected multistart_swap_by_validation   -0.088772   0.021768          5      5    0.000802      0.0625
    0.2 validation_swap_selected       swap_from_scenario_cvar   -0.137010   0.024543          5      5    0.000237      0.0625
    0.2            rcss_selected                        random   -0.277555   0.034926          5      5    0.000059      0.0625
    0.2            rcss_selected     best_random_by_validation   -0.211136   0.051643          5      5    0.000795      0.0625
    0.2            rcss_selected                  top_variance   -0.331806   0.062879          5      5    0.000295      0.0625
    0.2            rcss_selected                greedy_a_trace   -0.010078   0.011150          3      5    0.113366      0.2500
    0.2            rcss_selected         scenario_cvar_a_trace   -0.248578   0.041088          5      5    0.000173      0.0625
    0.2            rcss_selected multistart_swap_by_validation   -0.089377   0.024464          5      5    0.001222      0.0625
    0.2            rcss_selected       swap_from_scenario_cvar   -0.137615   0.029348          5      5    0.000468      0.0625
    0.2     robust_coverage_cvar                        random   -0.069933   0.047763          5      5    0.030674      0.0625
    0.2     robust_coverage_cvar     best_random_by_validation   -0.003514   0.067251          1      5    0.912626      0.6250
    0.2     robust_coverage_cvar                  top_variance   -0.124184   0.071094          5      5    0.017454      0.0625
    0.2     robust_coverage_cvar                greedy_a_trace    0.197544   0.061040          0      5    0.001935      0.0625
    0.2     robust_coverage_cvar         scenario_cvar_a_trace   -0.040956   0.056352          4      5    0.179451      0.1875
    0.2     robust_coverage_cvar multistart_swap_by_validation    0.118245   0.051061          0      5    0.006615      0.0625
    0.2     robust_coverage_cvar       swap_from_scenario_cvar    0.070007   0.054609          0      5    0.045626      0.0625
    0.3 validation_swap_selected                        random   -0.335796   0.021486          5      5    0.000004      0.0625
    0.3 validation_swap_selected     best_random_by_validation   -0.253131   0.038791          5      5    0.000128      0.0625
    0.3 validation_swap_selected                  top_variance   -0.331508   0.049945          5      5    0.000120      0.0625
    0.3 validation_swap_selected                greedy_a_trace   -0.019365   0.017531          4      5    0.068941      0.1250
    0.3 validation_swap_selected         scenario_cvar_a_trace   -0.354580   0.026769          5      5    0.000008      0.0625
    0.3 validation_swap_selected multistart_swap_by_validation   -0.139117   0.031062          5      5    0.000559      0.0625
    0.3 validation_swap_selected       swap_from_scenario_cvar   -0.220642   0.029192          5      5    0.000072      0.0625
    0.3            rcss_selected                        random   -0.324518   0.019053          5      5    0.000003      0.0625
    0.3            rcss_selected     best_random_by_validation   -0.241854   0.041773          5      5    0.000205      0.0625
    0.3            rcss_selected                  top_variance   -0.320230   0.047713          5      5    0.000115      0.0625
    0.3            rcss_selected                greedy_a_trace   -0.008088   0.013848          3      5    0.261615      0.3750
    0.3            rcss_selected         scenario_cvar_a_trace   -0.343303   0.022122          5      5    0.000004      0.0625
    0.3            rcss_selected multistart_swap_by_validation   -0.127840   0.035795          5      5    0.001333      0.0625
    0.3            rcss_selected       swap_from_scenario_cvar   -0.209365   0.023135          5      5    0.000035      0.0625
    0.3     robust_coverage_cvar                        random   -0.052408   0.050173          4      5    0.079757      0.1250
    0.3     robust_coverage_cvar     best_random_by_validation    0.030257   0.051060          2      5    0.255776      0.3125
    0.3     robust_coverage_cvar                  top_variance   -0.048119   0.061136          5      5    0.153219      0.0625
    0.3     robust_coverage_cvar                greedy_a_trace    0.264023   0.058607          0      5    0.000546      0.0625
    0.3     robust_coverage_cvar         scenario_cvar_a_trace   -0.071192   0.056943          4      5    0.049031      0.1250
    0.3     robust_coverage_cvar multistart_swap_by_validation    0.144271   0.051258          0      5    0.003257      0.0625
    0.3     robust_coverage_cvar       swap_from_scenario_cvar    0.062746   0.063774          1      5    0.092650      0.1250
```

## Certificate stability

```
                           pearson_mae                               spearman_mae                              
                                  mean       std       min       max         mean       std       min       max
method  certificate                                                                                            
gls_map condition_number      0.839719  0.007945  0.831970  0.848682     0.892996  0.008377  0.884834  0.903774
        information_logdet   -0.922151  0.005063 -0.928442 -0.915006    -0.898160  0.003352 -0.900554 -0.892279
        posterior_trace       0.950369  0.003009  0.946221  0.954265     0.931494  0.005373  0.924682  0.939221
gsp     condition_number      0.052616  0.166386 -0.221081  0.209884    -0.027289  0.228583 -0.397974  0.213199
        information_logdet   -0.051907  0.156673 -0.194767  0.208560    -0.003172  0.192894 -0.195836  0.312728
        posterior_trace       0.052566  0.166229 -0.220942  0.209498     0.001690  0.200306 -0.322829  0.209997
```

## RCSS selected sources

```
 budget                        source  selected_count
    0.1                greedy_a_trace               2
    0.1 multistart_swap_by_validation               2
    0.1      swap_from_greedy_a_trace               1
    0.2                greedy_a_trace               2
    0.2      swap_from_greedy_a_trace               3
    0.3                greedy_a_trace               1
    0.3      swap_from_greedy_a_trace               4
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