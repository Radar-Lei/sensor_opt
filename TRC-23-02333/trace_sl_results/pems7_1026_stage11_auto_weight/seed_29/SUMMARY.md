---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-05-21, 2012-05-16
Test days: 2012-05-11, 2012-05-14
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape          
                                                              mean       std       mean       std      mean       std
budget layout_type                   method                                                                          
0.1    best_random_by_trace          gls_map              3.820627       NaN   6.463164       NaN  0.097002       NaN
                                     gsp                  4.485616       NaN   7.583355       NaN  0.114534       NaN
                                     historical_tod_mean  4.694439       NaN   8.073548       NaN  0.119633       NaN
                                     neighbor_average     7.238045       NaN  11.257781       NaN  0.193749       NaN
       best_random_by_validation     gls_map              3.798539       NaN   6.395322       NaN  0.094942       NaN
                                     gsp                  4.511594       NaN   7.580990       NaN  0.113723       NaN
                                     historical_tod_mean  4.714063       NaN   8.073173       NaN  0.119577       NaN
                                     neighbor_average     7.425544       NaN  11.525913       NaN  0.190222       NaN
       coverage                      gls_map              3.899590       NaN   6.468040       NaN  0.094463       NaN
                                     gsp                  4.490005       NaN   7.578393       NaN  0.110618       NaN
                                     historical_tod_mean  4.716286       NaN   8.075765       NaN  0.117950       NaN
                                     neighbor_average     7.513421       NaN  11.461602       NaN  0.188245       NaN
       degree                        gls_map              4.620424       NaN   7.552506       NaN  0.111747       NaN
                                     gsp                  4.624133       NaN   7.678637       NaN  0.112364       NaN
                                     historical_tod_mean  4.626730       NaN   7.952470       NaN  0.116881       NaN
                                     neighbor_average     8.294433       NaN  12.419559       NaN  0.201934       NaN
       greedy_a_trace                gls_map              3.733123       NaN   6.161658       NaN  0.092473       NaN
                                     gsp                  4.508478       NaN   7.575887       NaN  0.112414       NaN
                                     historical_tod_mean  4.697306       NaN   8.046761       NaN  0.118405       NaN
                                     neighbor_average     7.177019       NaN  11.239877       NaN  0.200154       NaN
       greedy_d_logdet               gls_map              4.417057       NaN   7.035814       NaN  0.110417       NaN
                                     gsp                  4.483902       NaN   7.679251       NaN  0.114714       NaN
                                     historical_tod_mean  4.665884       NaN   8.066298       NaN  0.119456       NaN
                                     neighbor_average     7.987196       NaN  12.682688       NaN  0.239030       NaN
       multistart_swap_by_validation gls_map              3.726723       NaN   6.187781       NaN  0.093287       NaN
                                     gsp                  4.492455       NaN   7.546585       NaN  0.114338       NaN
                                     historical_tod_mean  4.692379       NaN   8.050613       NaN  0.119644       NaN
                                     neighbor_average     7.097842       NaN  10.892086       NaN  0.190657       NaN
       random                        gls_map              3.899517  0.056991   6.481905  0.085705  0.096740  0.001649
                                     gsp                  4.508235  0.027669   7.576325  0.044783  0.113479  0.001139
                                     historical_tod_mean  4.706762  0.023123   8.072327  0.034921  0.119504  0.000840
                                     neighbor_average     7.474938  0.145673  11.566998  0.190934  0.194722  0.004067
       rcss_selected                 gls_map              3.726723       NaN   6.187781       NaN  0.093287       NaN
                                     gsp                  4.492455       NaN   7.546585       NaN  0.114338       NaN
                                     historical_tod_mean  4.692379       NaN   8.050613       NaN  0.119644       NaN
                                     neighbor_average     7.097842       NaN  10.892086       NaN  0.190657       NaN
       robust_coverage_cvar          gls_map              3.827643       NaN   6.405927       NaN  0.096010       NaN
                                     gsp                  4.457260       NaN   7.583131       NaN  0.114316       NaN
                                     historical_tod_mean  4.663796       NaN   8.046965       NaN  0.119323       NaN
                                     neighbor_average     7.530542       NaN  11.582188       NaN  0.203937       NaN
       scenario_average_a_trace      gls_map              3.983275       NaN   6.724317       NaN  0.101240       NaN
                                     gsp                  4.504527       NaN   7.647239       NaN  0.115217       NaN
                                     historical_tod_mean  4.711107       NaN   8.104911       NaN  0.120483       NaN
                                     neighbor_average     7.505369       NaN  11.762853       NaN  0.210999       NaN
       scenario_cvar_a_trace         gls_map              3.897610       NaN   6.570212       NaN  0.099090       NaN
                                     gsp                  4.455487       NaN   7.614365       NaN  0.114955       NaN
                                     historical_tod_mean  4.669404       NaN   8.057426       NaN  0.119566       NaN
                                     neighbor_average     7.614760       NaN  11.826208       NaN  0.209362       NaN
       swap_from_best_random_trace   gls_map              3.739224       NaN   6.295469       NaN  0.094969       NaN
                                     gsp                  4.461896       NaN   7.592348       NaN  0.114581       NaN
                                     historical_tod_mean  4.681051       NaN   8.067147       NaN  0.119696       NaN
                                     neighbor_average     7.120424       NaN  11.096200       NaN  0.196103       NaN
       swap_from_greedy_a_trace      gls_map              3.687448       NaN   6.123574       NaN  0.091097       NaN
                                     gsp                  4.500010       NaN   7.584323       NaN  0.112733       NaN
                                     historical_tod_mean  4.690449       NaN   8.040910       NaN  0.118414       NaN
                                     neighbor_average     7.222612       NaN  11.301559       NaN  0.199691       NaN
       swap_from_scenario_average    gls_map              3.806628       NaN   6.410531       NaN  0.096066       NaN
                                     gsp                  4.492462       NaN   7.616541       NaN  0.113868       NaN
                                     historical_tod_mean  4.692925       NaN   8.072948       NaN  0.119749       NaN
                                     neighbor_average     7.294442       NaN  11.349959       NaN  0.203319       NaN
       swap_from_scenario_cvar       gls_map              3.748457       NaN   6.272752       NaN  0.094134       NaN
                                     gsp                  4.446193       NaN   7.573692       NaN  0.113504       NaN
                                     historical_tod_mean  4.653597       NaN   8.026299       NaN  0.118913       NaN
                                     neighbor_average     7.420725       NaN  11.471609       NaN  0.203549       NaN
       top_variance                  gls_map              3.926147       NaN   6.523410       NaN  0.093613       NaN
                                     gsp                  4.323643       NaN   7.153730       NaN  0.103915       NaN
                                     historical_tod_mean  4.422628       NaN   7.573530       NaN  0.107601       NaN
                                     neighbor_average     9.585454       NaN  14.851442       NaN  0.195900       NaN
       validation_swap_selected      gls_map              3.694175       NaN   6.136255       NaN  0.091553       NaN
                                     gsp                  4.466968       NaN   7.565649       NaN  0.112749       NaN
                                     historical_tod_mean  4.664617       NaN   8.016041       NaN  0.117994       NaN
                                     neighbor_average     7.254597       NaN  11.327481       NaN  0.201073       NaN
0.2    best_random_by_trace          gls_map              3.486986       NaN   5.755035       NaN  0.084825       NaN
                                     gsp                  4.485473       NaN   7.440351       NaN  0.112061       NaN
                                     historical_tod_mean  4.673307       NaN   7.994871       NaN  0.117760       NaN
                                     neighbor_average     7.013046       NaN  10.889053       NaN  0.181145       NaN
       best_random_by_validation     gls_map              3.469395       NaN   5.783536       NaN  0.085672       NaN
                                     gsp                  4.467395       NaN   7.411791       NaN  0.111362       NaN
                                     historical_tod_mean  4.636208       NaN   7.977202       NaN  0.118148       NaN
                                     neighbor_average     7.039653       NaN  11.020664       NaN  0.182428       NaN
       coverage                      gls_map              3.563496       NaN   5.915822       NaN  0.085419       NaN
                                     gsp                  4.513200       NaN   7.562091       NaN  0.111325       NaN
                                     historical_tod_mean  4.742500       NaN   8.116681       NaN  0.118915       NaN
                                     neighbor_average     7.069849       NaN  11.040104       NaN  0.180905       NaN
       degree                        gls_map              4.384715       NaN   7.186598       NaN  0.108404       NaN
                                     gsp                  4.518108       NaN   7.503727       NaN  0.110926       NaN
                                     historical_tod_mean  4.582785       NaN   7.917712       NaN  0.116184       NaN
                                     neighbor_average     8.642694       NaN  12.653925       NaN  0.202888       NaN
       greedy_a_trace                gls_map              3.344119       NaN   5.525748       NaN  0.082794       NaN
                                     gsp                  4.438941       NaN   7.482592       NaN  0.111646       NaN
                                     historical_tod_mean  4.647944       NaN   8.017265       NaN  0.117788       NaN
                                     neighbor_average     6.974878       NaN  10.898555       NaN  0.195218       NaN
       greedy_d_logdet               gls_map              3.788783       NaN   6.185470       NaN  0.094538       NaN
                                     gsp                  4.425361       NaN   7.556210       NaN  0.113020       NaN
                                     historical_tod_mean  4.650691       NaN   8.073801       NaN  0.119678       NaN
                                     neighbor_average     7.571059       NaN  12.033863       NaN  0.224779       NaN
       multistart_swap_by_validation gls_map              3.397184       NaN   5.619769       NaN  0.083676       NaN
                                     gsp                  4.456128       NaN   7.455337       NaN  0.112761       NaN
                                     historical_tod_mean  4.662910       NaN   8.008731       NaN  0.118705       NaN
                                     neighbor_average     6.868628       NaN  10.690605       NaN  0.182815       NaN
       random                        gls_map              3.580701  0.042543   5.958866  0.077161  0.087635  0.001474
                                     gsp                  4.509846  0.029507   7.520288  0.042379  0.113095  0.001337
                                     historical_tod_mean  4.707698  0.028083   8.073037  0.040440  0.119482  0.001152
                                     neighbor_average     7.159552  0.089004  11.216614  0.145727  0.185907  0.004135
       rcss_selected                 gls_map              3.344119       NaN   5.525748       NaN  0.082794       NaN
                                     gsp                  4.438941       NaN   7.482592       NaN  0.111646       NaN
                                     historical_tod_mean  4.647944       NaN   8.017265       NaN  0.117788       NaN
                                     neighbor_average     6.974878       NaN  10.898555       NaN  0.195218       NaN
       robust_coverage_cvar          gls_map              3.482636       NaN   5.781379       NaN  0.086018       NaN
                                     gsp                  4.434361       NaN   7.509959       NaN  0.113379       NaN
                                     historical_tod_mean  4.649901       NaN   8.047522       NaN  0.119575       NaN
                                     neighbor_average     7.230122       NaN  11.310537       NaN  0.197154       NaN
       scenario_average_a_trace      gls_map              3.623919       NaN   6.059158       NaN  0.091173       NaN
                                     gsp                  4.482384       NaN   7.608399       NaN  0.115566       NaN
                                     historical_tod_mean  4.709592       NaN   8.138632       NaN  0.121732       NaN
                                     neighbor_average     7.282651       NaN  11.440738       NaN  0.207252       NaN
       scenario_cvar_a_trace         gls_map              3.581970       NaN   5.952226       NaN  0.088883       NaN
                                     gsp                  4.429950       NaN   7.521263       NaN  0.114081       NaN
                                     historical_tod_mean  4.643324       NaN   8.050549       NaN  0.119846       NaN
                                     neighbor_average     7.314331       NaN  11.520296       NaN  0.202454       NaN
       swap_from_best_random_trace   gls_map              3.397184       NaN   5.619769       NaN  0.083676       NaN
                                     gsp                  4.456128       NaN   7.455337       NaN  0.112761       NaN
                                     historical_tod_mean  4.662910       NaN   8.008731       NaN  0.118705       NaN
                                     neighbor_average     6.868628       NaN  10.690605       NaN  0.182815       NaN
       swap_from_greedy_a_trace      gls_map              3.331182       NaN   5.552222       NaN  0.082924       NaN
                                     gsp                  4.437784       NaN   7.486625       NaN  0.111734       NaN
                                     historical_tod_mean  4.642245       NaN   8.014152       NaN  0.117775       NaN
                                     neighbor_average     7.050447       NaN  11.072148       NaN  0.198457       NaN
       swap_from_scenario_average    gls_map              3.508939       NaN   5.851250       NaN  0.087915       NaN
                                     gsp                  4.452772       NaN   7.562896       NaN  0.114197       NaN
                                     historical_tod_mean  4.673378       NaN   8.090244       NaN  0.120010       NaN
                                     neighbor_average     7.195796       NaN  11.362347       NaN  0.205673       NaN
       swap_from_scenario_cvar       gls_map              3.468336       NaN   5.754691       NaN  0.086463       NaN
                                     gsp                  4.406033       NaN   7.509274       NaN  0.113878       NaN
                                     historical_tod_mean  4.625220       NaN   8.034530       NaN  0.119639       NaN
                                     neighbor_average     7.227440       NaN  11.347734       NaN  0.203245       NaN
       top_variance                  gls_map              3.668996       NaN   6.085787       NaN  0.084104       NaN
                                     gsp                  4.164245       NaN   6.887831       NaN  0.096279       NaN
                                     historical_tod_mean  4.221789       NaN   7.269553       NaN  0.099362       NaN
                                     neighbor_average     9.006687       NaN  14.230906       NaN  0.179882       NaN
       validation_swap_selected      gls_map              3.338069       NaN   5.516712       NaN  0.082661       NaN
                                     gsp                  4.428901       NaN   7.475699       NaN  0.111282       NaN
                                     historical_tod_mean  4.636614       NaN   8.008897       NaN  0.117455       NaN
                                     neighbor_average     7.014632       NaN  10.908824       NaN  0.194738       NaN
0.3    best_random_by_trace          gls_map              3.348800       NaN   5.655248       NaN  0.083253       NaN
                                     gsp                  4.522220       NaN   7.532963       NaN  0.114640       NaN
                                     historical_tod_mean  4.729622       NaN   8.119106       NaN  0.121634       NaN
                                     neighbor_average     7.136429       NaN  11.152981       NaN  0.185234       NaN
       best_random_by_validation     gls_map              3.292553       NaN   5.504793       NaN  0.081084       NaN
                                     gsp                  4.431504       NaN   7.429506       NaN  0.112138       NaN
                                     historical_tod_mean  4.611332       NaN   7.985520       NaN  0.117934       NaN
                                     neighbor_average     6.912692       NaN  10.790332       NaN  0.180398       NaN
       coverage                      gls_map              3.418305       NaN   5.655355       NaN  0.081295       NaN
                                     gsp                  4.576028       NaN   7.605737       NaN  0.113139       NaN
                                     historical_tod_mean  4.811549       NaN   8.194280       NaN  0.120895       NaN
                                     neighbor_average     6.976474       NaN  11.017161       NaN  0.181292       NaN
       degree                        gls_map              4.182665       NaN   6.879227       NaN  0.101190       NaN
                                     gsp                  4.390855       NaN   7.339766       NaN  0.107573       NaN
                                     historical_tod_mean  4.493384       NaN   7.821830       NaN  0.113741       NaN
                                     neighbor_average     8.050829       NaN  12.529813       NaN  0.201188       NaN
       greedy_a_trace                gls_map              3.073773       NaN   5.064135       NaN  0.076485       NaN
                                     gsp                  4.394316       NaN   7.432912       NaN  0.112036       NaN
                                     historical_tod_mean  4.621688       NaN   8.021764       NaN  0.118453       NaN
                                     neighbor_average     6.813500       NaN  10.674651       NaN  0.194442       NaN
       greedy_d_logdet               gls_map              3.400153       NaN   5.557386       NaN  0.085853       NaN
                                     gsp                  4.369862       NaN   7.453405       NaN  0.112366       NaN
                                     historical_tod_mean  4.597252       NaN   8.043158       NaN  0.119518       NaN
                                     neighbor_average     7.404008       NaN  11.745799       NaN  0.215641       NaN
       multistart_swap_by_validation gls_map              3.173642       NaN   5.303342       NaN  0.078600       NaN
                                     gsp                  4.397839       NaN   7.414753       NaN  0.112086       NaN
                                     historical_tod_mean  4.595230       NaN   7.982338       NaN  0.118171       NaN
                                     neighbor_average     6.702238       NaN  10.431262       NaN  0.178527       NaN
       random                        gls_map              3.377740  0.044418   5.621831  0.085350  0.082091  0.001803
                                     gsp                  4.516477  0.039212   7.499982  0.064297  0.113114  0.001883
                                     historical_tod_mean  4.710272  0.045413   8.073396  0.066631  0.119492  0.001802
                                     neighbor_average     7.033507  0.091925  11.082478  0.169359  0.182434  0.004523
       rcss_selected                 gls_map              3.051713       NaN   5.017099       NaN  0.075833       NaN
                                     gsp                  4.352813       NaN   7.380117       NaN  0.110658       NaN
                                     historical_tod_mean  4.576364       NaN   7.965244       NaN  0.117157       NaN
                                     neighbor_average     6.837802       NaN  10.712250       NaN  0.193334       NaN
       robust_coverage_cvar          gls_map              3.270261       NaN   5.484658       NaN  0.080764       NaN
                                     gsp                  4.416431       NaN   7.481448       NaN  0.112952       NaN
                                     historical_tod_mean  4.615618       NaN   8.054500       NaN  0.119346       NaN
                                     neighbor_average     7.198554       NaN  11.489452       NaN  0.195145       NaN
       scenario_average_a_trace      gls_map              3.388955       NaN   5.699170       NaN  0.085238       NaN
                                     gsp                  4.484171       NaN   7.597620       NaN  0.115556       NaN
                                     historical_tod_mean  4.700112       NaN   8.167774       NaN  0.122357       NaN
                                     neighbor_average     7.216473       NaN  11.597503       NaN  0.204938       NaN
       scenario_cvar_a_trace         gls_map              3.393865       NaN   5.654571       NaN  0.083729       NaN
                                     gsp                  4.427642       NaN   7.506228       NaN  0.113553       NaN
                                     historical_tod_mean  4.628706       NaN   8.069440       NaN  0.119971       NaN
                                     neighbor_average     7.270666       NaN  11.536984       NaN  0.198707       NaN
       swap_from_best_random_trace   gls_map              3.232049       NaN   5.421936       NaN  0.081257       NaN
                                     gsp                  4.450226       NaN   7.470541       NaN  0.114132       NaN
                                     historical_tod_mean  4.658098       NaN   8.057705       NaN  0.120952       NaN
                                     neighbor_average     6.966886       NaN  10.850282       NaN  0.184741       NaN
       swap_from_greedy_a_trace      gls_map              3.051713       NaN   5.017099       NaN  0.075833       NaN
                                     gsp                  4.352813       NaN   7.380117       NaN  0.110658       NaN
                                     historical_tod_mean  4.576364       NaN   7.965244       NaN  0.117157       NaN
                                     neighbor_average     6.837802       NaN  10.712250       NaN  0.193334       NaN
       swap_from_scenario_average    gls_map              3.231576       NaN   5.405917       NaN  0.080292       NaN
                                     gsp                  4.435636       NaN   7.535362       NaN  0.113468       NaN
                                     historical_tod_mean  4.659955       NaN   8.110958       NaN  0.120299       NaN
                                     neighbor_average     7.108255       NaN  11.382213       NaN  0.201370       NaN
       swap_from_scenario_cvar       gls_map              3.286341       NaN   5.481863       NaN  0.081968       NaN
                                     gsp                  4.422009       NaN   7.525980       NaN  0.114677       NaN
                                     historical_tod_mean  4.633443       NaN   8.090806       NaN  0.121008       NaN
                                     neighbor_average     7.154832       NaN  11.393296       NaN  0.201366       NaN
       top_variance                  gls_map              3.419954       NaN   5.682090       NaN  0.076209       NaN
                                     gsp                  3.992104       NaN   6.599526       NaN  0.090032       NaN
                                     historical_tod_mean  4.007540       NaN   6.930647       NaN  0.092129       NaN
                                     neighbor_average     8.625462       NaN  13.465803       NaN  0.168229       NaN
       validation_swap_selected      gls_map              3.031047       NaN   4.980231       NaN  0.075052       NaN
                                     gsp                  4.326817       NaN   7.335085       NaN  0.109458       NaN
                                     historical_tod_mean  4.543735       NaN   7.924668       NaN  0.116007       NaN
                                     neighbor_average     6.820389       NaN  10.677049       NaN  0.191610       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 3.687448 6.123574
    0.2 swap_from_greedy_a_trace gls_map 3.331182 5.552222
    0.3 validation_swap_selected gls_map 3.031047 4.980231
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.044924     -0.011033 351
    gsp   condition_number     0.045149     -0.017348 351
    gsp information_logdet    -0.040751      0.001538 351
gls_map    posterior_trace     0.949388      0.933609 351
gls_map   condition_number     0.848682      0.903774 351
gls_map information_logdet    -0.915006     -0.898713 351
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv