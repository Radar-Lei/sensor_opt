---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-15, 2015-01-06
Test days: 2015-01-07, 2015-01-19
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.398851       NaN   5.476701       NaN  0.094986       NaN
                                     gsp                  3.992401       NaN   6.619187       NaN  0.126704       NaN
                                     historical_tod_mean  4.205048       NaN   7.128715       NaN  0.138911       NaN
                                     neighbor_average     5.692484       NaN   8.951293       NaN  0.163258       NaN
       best_random_by_validation     gls_map              3.342346       NaN   5.521464       NaN  0.096614       NaN
                                     gsp                  3.994122       NaN   6.595459       NaN  0.125889       NaN
                                     historical_tod_mean  4.216261       NaN   7.130272       NaN  0.137765       NaN
                                     neighbor_average     5.207925       NaN   8.490702       NaN  0.153901       NaN
       coverage                      gls_map              3.372940       NaN   5.527749       NaN  0.098743       NaN
                                     gsp                  4.051037       NaN   6.714917       NaN  0.130996       NaN
                                     historical_tod_mean  4.264464       NaN   7.230560       NaN  0.143766       NaN
                                     neighbor_average     5.494631       NaN   8.657759       NaN  0.173944       NaN
       degree                        gls_map              3.751062       NaN   6.163767       NaN  0.111968       NaN
                                     gsp                  4.057618       NaN   6.652075       NaN  0.128577       NaN
                                     historical_tod_mean  4.243958       NaN   7.177932       NaN  0.143310       NaN
                                     neighbor_average     6.290146       NaN  10.105004       NaN  0.200178       NaN
       graph_sampling_laplacian      gls_map              4.214337       NaN   6.761496       NaN  0.116247       NaN
                                     gsp                  4.361842       NaN   6.971971       NaN  0.130126       NaN
                                     historical_tod_mean  4.266861       NaN   7.158969       NaN  0.140054       NaN
                                     neighbor_average     6.917139       NaN  11.294025       NaN  0.210102       NaN
       greedy_a_trace                gls_map              3.255697       NaN   5.303032       NaN  0.093993       NaN
                                     gsp                  4.040958       NaN   6.656959       NaN  0.128933       NaN
                                     historical_tod_mean  4.240915       NaN   7.158362       NaN  0.140822       NaN
                                     neighbor_average     5.324467       NaN   8.455478       NaN  0.158169       NaN
       greedy_d_logdet               gls_map              3.953178       NaN   6.480927       NaN  0.121553       NaN
                                     gsp                  4.279139       NaN   7.069165       NaN  0.141460       NaN
                                     historical_tod_mean  4.392973       NaN   7.390112       NaN  0.148388       NaN
                                     neighbor_average     6.197304       NaN  10.439497       NaN  0.224119       NaN
       multistart_swap_by_validation gls_map              3.225111       NaN   5.228978       NaN  0.091623       NaN
                                     gsp                  4.029722       NaN   6.636015       NaN  0.127765       NaN
                                     historical_tod_mean  4.241472       NaN   7.150380       NaN  0.140077       NaN
                                     neighbor_average     5.522368       NaN   8.763186       NaN  0.167637       NaN
       observability_proxy           gls_map              3.683691       NaN   6.140747       NaN  0.111553       NaN
                                     gsp                  4.065586       NaN   6.706651       NaN  0.131215       NaN
                                     historical_tod_mean  4.247020       NaN   7.188225       NaN  0.143996       NaN
                                     neighbor_average     6.225584       NaN  10.054383       NaN  0.194517       NaN
       qr_pod_modes                  gls_map              3.671095       NaN   5.979768       NaN  0.113234       NaN
                                     gsp                  4.139866       NaN   6.888568       NaN  0.135681       NaN
                                     historical_tod_mean  4.333438       NaN   7.312353       NaN  0.146357       NaN
                                     neighbor_average     5.721661       NaN   9.566336       NaN  0.201215       NaN
       random                        gls_map              3.465288  0.073353   5.696384  0.132905  0.097824  0.003849
                                     gsp                  4.046593  0.034666   6.652757  0.072010  0.126951  0.003214
                                     historical_tod_mean  4.235905  0.028915   7.164533  0.053579  0.140200  0.002304
                                     neighbor_average     5.645317  0.227211   9.081200  0.329757  0.167241  0.007857
       rcss_selected                 gls_map              3.213466       NaN   5.331602       NaN  0.094129       NaN
                                     gsp                  4.027537       NaN   6.683519       NaN  0.129769       NaN
                                     historical_tod_mean  4.246598       NaN   7.185220       NaN  0.141566       NaN
                                     neighbor_average     5.519588       NaN   8.889644       NaN  0.168242       NaN
       robust_coverage_cvar          gls_map              3.408384       NaN   5.560225       NaN  0.092250       NaN
                                     gsp                  4.062743       NaN   6.599978       NaN  0.125777       NaN
                                     historical_tod_mean  4.266237       NaN   7.159726       NaN  0.140614       NaN
                                     neighbor_average     5.338605       NaN   8.679348       NaN  0.167669       NaN
       scenario_average_a_trace      gls_map              3.421193       NaN   5.630199       NaN  0.099411       NaN
                                     gsp                  4.104296       NaN   6.809156       NaN  0.133293       NaN
                                     historical_tod_mean  4.310770       NaN   7.280681       NaN  0.144952       NaN
                                     neighbor_average     5.605104       NaN   9.078001       NaN  0.177940       NaN
       scenario_cvar_a_trace         gls_map              3.400736       NaN   5.514785       NaN  0.092240       NaN
                                     gsp                  4.049134       NaN   6.629903       NaN  0.126482       NaN
                                     historical_tod_mean  4.261440       NaN   7.172382       NaN  0.140549       NaN
                                     neighbor_average     5.443215       NaN   8.729462       NaN  0.169551       NaN
       swap_from_best_random_trace   gls_map              3.213466       NaN   5.331602       NaN  0.094129       NaN
                                     gsp                  4.027537       NaN   6.683519       NaN  0.129769       NaN
                                     historical_tod_mean  4.246598       NaN   7.185220       NaN  0.141566       NaN
                                     neighbor_average     5.519588       NaN   8.889644       NaN  0.168242       NaN
       swap_from_greedy_a_trace      gls_map              3.253221       NaN   5.423804       NaN  0.096463       NaN
                                     gsp                  4.047667       NaN   6.712931       NaN  0.131576       NaN
                                     historical_tod_mean  4.263386       NaN   7.197676       NaN  0.142549       NaN
                                     neighbor_average     5.717091       NaN   9.257420       NaN  0.180839       NaN
       swap_from_scenario_average    gls_map              3.272495       NaN   5.347519       NaN  0.092491       NaN
                                     gsp                  4.055785       NaN   6.679610       NaN  0.129067       NaN
                                     historical_tod_mean  4.256349       NaN   7.178305       NaN  0.141126       NaN
                                     neighbor_average     5.837543       NaN   9.161143       NaN  0.177540       NaN
       swap_from_scenario_cvar       gls_map              3.254610       NaN   5.397897       NaN  0.095654       NaN
                                     gsp                  4.040727       NaN   6.688783       NaN  0.129921       NaN
                                     historical_tod_mean  4.260531       NaN   7.202303       NaN  0.142134       NaN
                                     neighbor_average     5.791987       NaN   9.066723       NaN  0.178167       NaN
       top_variance                  gls_map              3.697053       NaN   6.145772       NaN  0.101475       NaN
                                     gsp                  3.921599       NaN   6.424252       NaN  0.113192       NaN
                                     historical_tod_mean  3.934963       NaN   6.746135       NaN  0.119701       NaN
                                     neighbor_average     9.055699       NaN  14.764889       NaN  0.186173       NaN
       validation_swap_selected      gls_map              3.212997       NaN   5.322175       NaN  0.093885       NaN
                                     gsp                  4.022414       NaN   6.678427       NaN  0.129732       NaN
                                     historical_tod_mean  4.241178       NaN   7.176741       NaN  0.141301       NaN
                                     neighbor_average     5.485122       NaN   8.853340       NaN  0.167092       NaN
0.2    best_random_by_trace          gls_map              3.110506       NaN   5.152224       NaN  0.087577       NaN
                                     gsp                  4.056763       NaN   6.677749       NaN  0.128694       NaN
                                     historical_tod_mean  4.293052       NaN   7.240916       NaN  0.142029       NaN
                                     neighbor_average     5.024186       NaN   8.148891       NaN  0.150761       NaN
       best_random_by_validation     gls_map              3.090696       NaN   5.097303       NaN  0.086326       NaN
                                     gsp                  4.015024       NaN   6.558502       NaN  0.125527       NaN
                                     historical_tod_mean  4.237989       NaN   7.147738       NaN  0.140266       NaN
                                     neighbor_average     5.237128       NaN   8.439265       NaN  0.142283       NaN
       coverage                      gls_map              3.010518       NaN   4.874709       NaN  0.084138       NaN
                                     gsp                  4.036415       NaN   6.597903       NaN  0.127327       NaN
                                     historical_tod_mean  4.255789       NaN   7.200428       NaN  0.142486       NaN
                                     neighbor_average     4.634567       NaN   7.313841       NaN  0.138183       NaN
       degree                        gls_map              3.690425       NaN   6.151391       NaN  0.111075       NaN
                                     gsp                  4.119061       NaN   6.755149       NaN  0.133652       NaN
                                     historical_tod_mean  4.315100       NaN   7.302046       NaN  0.149799       NaN
                                     neighbor_average     6.349648       NaN  10.360835       NaN  0.195452       NaN
       graph_sampling_laplacian      gls_map              3.991308       NaN   6.385019       NaN  0.102868       NaN
                                     gsp                  4.344117       NaN   6.768463       NaN  0.125133       NaN
                                     historical_tod_mean  4.266614       NaN   7.123423       NaN  0.137882       NaN
                                     neighbor_average     6.213032       NaN  10.168808       NaN  0.186001       NaN
       greedy_a_trace                gls_map              3.089820       NaN   5.048239       NaN  0.089223       NaN
                                     gsp                  4.133148       NaN   6.781296       NaN  0.132946       NaN
                                     historical_tod_mean  4.357873       NaN   7.344393       NaN  0.147387       NaN
                                     neighbor_average     4.786225       NaN   7.802924       NaN  0.154859       NaN
       greedy_d_logdet               gls_map              3.694864       NaN   6.013604       NaN  0.109356       NaN
                                     gsp                  4.309749       NaN   7.021873       NaN  0.140417       NaN
                                     historical_tod_mean  4.489444       NaN   7.505717       NaN  0.153521       NaN
                                     neighbor_average     5.803574       NaN   9.769293       NaN  0.211279       NaN
       multistart_swap_by_validation gls_map              3.035101       NaN   4.921609       NaN  0.084210       NaN
                                     gsp                  4.083967       NaN   6.676570       NaN  0.127437       NaN
                                     historical_tod_mean  4.311877       NaN   7.244606       NaN  0.141532       NaN
                                     neighbor_average     4.725242       NaN   7.552272       NaN  0.137066       NaN
       observability_proxy           gls_map              3.594007       NaN   6.047508       NaN  0.108834       NaN
                                     gsp                  4.108397       NaN   6.759225       NaN  0.133842       NaN
                                     historical_tod_mean  4.302366       NaN   7.290813       NaN  0.149234       NaN
                                     neighbor_average     6.183326       NaN  10.015503       NaN  0.190277       NaN
       qr_pod_modes                  gls_map              3.194246       NaN   5.157125       NaN  0.090178       NaN
                                     gsp                  4.150802       NaN   6.757954       NaN  0.131754       NaN
                                     historical_tod_mean  4.366619       NaN   7.316587       NaN  0.146859       NaN
                                     neighbor_average     5.057026       NaN   8.153733       NaN  0.163452       NaN
       random                        gls_map              3.144240  0.048033   5.186523  0.141965  0.088041  0.004016
                                     gsp                  4.041313  0.035925   6.592277  0.081627  0.124963  0.003569
                                     historical_tod_mean  4.242965  0.042160   7.172428  0.074098  0.140502  0.003368
                                     neighbor_average     5.124587  0.141737   8.257124  0.280429  0.145909  0.007404
       rcss_selected                 gls_map              2.916501       NaN   4.792680       NaN  0.081914       NaN
                                     gsp                  3.905159       NaN   6.455666       NaN  0.123461       NaN
                                     historical_tod_mean  4.126108       NaN   7.041586       NaN  0.137724       NaN
                                     neighbor_average     4.955316       NaN   7.752545       NaN  0.133342       NaN
       robust_coverage_cvar          gls_map              3.095314       NaN   5.069793       NaN  0.085559       NaN
                                     gsp                  4.116264       NaN   6.678957       NaN  0.129191       NaN
                                     historical_tod_mean  4.334410       NaN   7.279643       NaN  0.144837       NaN
                                     neighbor_average     4.786864       NaN   7.770851       NaN  0.146997       NaN
       scenario_average_a_trace      gls_map              3.305626       NaN   5.398990       NaN  0.097649       NaN
                                     gsp                  4.182056       NaN   6.881818       NaN  0.137043       NaN
                                     historical_tod_mean  4.394592       NaN   7.424167       NaN  0.151533       NaN
                                     neighbor_average     5.055930       NaN   8.344108       NaN  0.169076       NaN
       scenario_cvar_a_trace         gls_map              3.179518       NaN   5.161897       NaN  0.090672       NaN
                                     gsp                  4.141786       NaN   6.738501       NaN  0.132266       NaN
                                     historical_tod_mean  4.363314       NaN   7.328182       NaN  0.148135       NaN
                                     neighbor_average     5.026878       NaN   8.044098       NaN  0.163090       NaN
       swap_from_best_random_trace   gls_map              3.056129       NaN   4.986872       NaN  0.086219       NaN
                                     gsp                  4.116153       NaN   6.726278       NaN  0.130975       NaN
                                     historical_tod_mean  4.339153       NaN   7.274910       NaN  0.144151       NaN
                                     neighbor_average     4.828596       NaN   7.840614       NaN  0.148351       NaN
       swap_from_greedy_a_trace      gls_map              3.064664       NaN   4.920309       NaN  0.085302       NaN
                                     gsp                  4.112495       NaN   6.708575       NaN  0.129742       NaN
                                     historical_tod_mean  4.331949       NaN   7.282740       NaN  0.144395       NaN
                                     neighbor_average     4.744078       NaN   7.635852       NaN  0.147320       NaN
       swap_from_scenario_average    gls_map              3.080305       NaN   5.010874       NaN  0.087752       NaN
                                     gsp                  4.131578       NaN   6.764359       NaN  0.133149       NaN
                                     historical_tod_mean  4.358680       NaN   7.330441       NaN  0.147767       NaN
                                     neighbor_average     4.891181       NaN   8.014852       NaN  0.161159       NaN
       swap_from_scenario_cvar       gls_map              3.073374       NaN   4.976801       NaN  0.086257       NaN
                                     gsp                  4.133036       NaN   6.727873       NaN  0.131502       NaN
                                     historical_tod_mean  4.349473       NaN   7.296540       NaN  0.146226       NaN
                                     neighbor_average     4.900072       NaN   7.854933       NaN  0.154634       NaN
       top_variance                  gls_map              3.272318       NaN   5.378266       NaN  0.086796       NaN
                                     gsp                  3.675248       NaN   6.068268       NaN  0.103340       NaN
                                     historical_tod_mean  3.727252       NaN   6.417342       NaN  0.109067       NaN
                                     neighbor_average     6.721883       NaN  11.106544       NaN  0.140200       NaN
       validation_swap_selected      gls_map              2.922390       NaN   4.797445       NaN  0.082131       NaN
                                     gsp                  3.914524       NaN   6.471873       NaN  0.124195       NaN
                                     historical_tod_mean  4.139714       NaN   7.052935       NaN  0.138011       NaN
                                     neighbor_average     4.930267       NaN   7.743132       NaN  0.133776       NaN
0.3    best_random_by_trace          gls_map              2.973264       NaN   4.825894       NaN  0.078955       NaN
                                     gsp                  4.103655       NaN   6.628458       NaN  0.122865       NaN
                                     historical_tod_mean  4.304273       NaN   7.250628       NaN  0.140443       NaN
                                     neighbor_average     4.644614       NaN   7.520313       NaN  0.130850       NaN
       best_random_by_validation     gls_map              2.858883       NaN   4.716179       NaN  0.078196       NaN
                                     gsp                  3.933616       NaN   6.501092       NaN  0.120462       NaN
                                     historical_tod_mean  4.167986       NaN   7.131635       NaN  0.135296       NaN
                                     neighbor_average     4.668083       NaN   7.335864       NaN  0.121004       NaN
       coverage                      gls_map              2.803679       NaN   4.488552       NaN  0.076092       NaN
                                     gsp                  4.053439       NaN   6.602105       NaN  0.126245       NaN
                                     historical_tod_mean  4.265616       NaN   7.221081       NaN  0.142104       NaN
                                     neighbor_average     4.460906       NaN   6.942921       NaN  0.123686       NaN
       degree                        gls_map              3.609572       NaN   6.062056       NaN  0.108926       NaN
                                     gsp                  4.170554       NaN   6.875744       NaN  0.137647       NaN
                                     historical_tod_mean  4.336586       NaN   7.336280       NaN  0.151966       NaN
                                     neighbor_average     6.804428       NaN  11.184743       NaN  0.196804       NaN
       graph_sampling_laplacian      gls_map              3.702089       NaN   5.924367       NaN  0.096199       NaN
                                     gsp                  4.263540       NaN   6.628658       NaN  0.118243       NaN
                                     historical_tod_mean  4.232142       NaN   7.051474       NaN  0.130843       NaN
                                     neighbor_average     6.321609       NaN  10.094175       NaN  0.183259       NaN
       greedy_a_trace                gls_map              2.958763       NaN   4.866289       NaN  0.086211       NaN
                                     gsp                  4.214221       NaN   6.862748       NaN  0.135291       NaN
                                     historical_tod_mean  4.444096       NaN   7.465406       NaN  0.151687       NaN
                                     neighbor_average     4.516486       NaN   7.375925       NaN  0.144990       NaN
       greedy_d_logdet               gls_map              3.383166       NaN   5.451553       NaN  0.095675       NaN
                                     gsp                  4.335672       NaN   7.013457       NaN  0.139608       NaN
                                     historical_tod_mean  4.545169       NaN   7.570636       NaN  0.155769       NaN
                                     neighbor_average     5.218127       NaN   8.646828       NaN  0.180108       NaN
       multistart_swap_by_validation gls_map              2.840543       NaN   4.719206       NaN  0.081031       NaN
                                     gsp                  4.077348       NaN   6.713086       NaN  0.128959       NaN
                                     historical_tod_mean  4.322053       NaN   7.332029       NaN  0.145148       NaN
                                     neighbor_average     4.582288       NaN   7.164338       NaN  0.127042       NaN
       observability_proxy           gls_map              3.596783       NaN   6.055687       NaN  0.108567       NaN
                                     gsp                  4.170822       NaN   6.881371       NaN  0.137776       NaN
                                     historical_tod_mean  4.329316       NaN   7.332899       NaN  0.151858       NaN
                                     neighbor_average     6.730997       NaN  11.098937       NaN  0.195684       NaN
       qr_pod_modes                  gls_map              2.963004       NaN   4.723726       NaN  0.081342       NaN
                                     gsp                  4.179671       NaN   6.756281       NaN  0.130996       NaN
                                     historical_tod_mean  4.404912       NaN   7.362661       NaN  0.146933       NaN
                                     neighbor_average     4.618350       NaN   7.224409       NaN  0.140307       NaN
       random                        gls_map              2.955719  0.060109   4.861007  0.118795  0.081521  0.003203
                                     gsp                  4.036587  0.055069   6.564460  0.088769  0.123820  0.003403
                                     historical_tod_mean  4.236646  0.054878   7.164060  0.084965  0.140356  0.003534
                                     neighbor_average     4.725547  0.122789   7.556625  0.267223  0.130408  0.006944
       rcss_selected                 gls_map              2.745251       NaN   4.440085       NaN  0.072300       NaN
                                     gsp                  3.936762       NaN   6.419650       NaN  0.119606       NaN
                                     historical_tod_mean  4.146587       NaN   7.038030       NaN  0.134536       NaN
                                     neighbor_average     4.524315       NaN   7.158890       NaN  0.115276       NaN
       robust_coverage_cvar          gls_map              2.915464       NaN   4.710347       NaN  0.080326       NaN
                                     gsp                  4.148389       NaN   6.690956       NaN  0.129451       NaN
                                     historical_tod_mean  4.367769       NaN   7.305676       NaN  0.146319       NaN
                                     neighbor_average     4.449828       NaN   7.139617       NaN  0.133100       NaN
       scenario_average_a_trace      gls_map              3.041524       NaN   4.942243       NaN  0.089229       NaN
                                     gsp                  4.200963       NaN   6.890730       NaN  0.137700       NaN
                                     historical_tod_mean  4.429955       NaN   7.494452       NaN  0.154490       NaN
                                     neighbor_average     4.662105       NaN   7.580513       NaN  0.156044       NaN
       scenario_cvar_a_trace         gls_map              3.042044       NaN   4.868990       NaN  0.085290       NaN
                                     gsp                  4.199355       NaN   6.798505       NaN  0.133213       NaN
                                     historical_tod_mean  4.438735       NaN   7.417867       NaN  0.150382       NaN
                                     neighbor_average     4.745092       NaN   7.603179       NaN  0.149218       NaN
       swap_from_best_random_trace   gls_map              2.969734       NaN   4.773994       NaN  0.080689       NaN
                                     gsp                  4.180495       NaN   6.774227       NaN  0.131483       NaN
                                     historical_tod_mean  4.418297       NaN   7.409006       NaN  0.148322       NaN
                                     neighbor_average     4.602042       NaN   7.336185       NaN  0.138493       NaN
       swap_from_greedy_a_trace      gls_map              2.919568       NaN   4.734808       NaN  0.083487       NaN
                                     gsp                  4.189315       NaN   6.821075       NaN  0.133831       NaN
                                     historical_tod_mean  4.427905       NaN   7.423922       NaN  0.149467       NaN
                                     neighbor_average     4.512795       NaN   7.280283       NaN  0.140685       NaN
       swap_from_scenario_average    gls_map              2.962067       NaN   4.829436       NaN  0.087250       NaN
                                     gsp                  4.203737       NaN   6.869164       NaN  0.138548       NaN
                                     historical_tod_mean  4.449535       NaN   7.477324       NaN  0.154758       NaN
                                     neighbor_average     4.563193       NaN   7.474026       NaN  0.154394       NaN
       swap_from_scenario_cvar       gls_map              2.938691       NaN   4.778072       NaN  0.085508       NaN
                                     gsp                  4.169767       NaN   6.815190       NaN  0.135905       NaN
                                     historical_tod_mean  4.419596       NaN   7.426933       NaN  0.152163       NaN
                                     neighbor_average     4.597093       NaN   7.424076       NaN  0.150323       NaN
       top_variance                  gls_map              2.903193       NaN   4.769302       NaN  0.074855       NaN
                                     gsp                  3.455593       NaN   5.706164       NaN  0.094081       NaN
                                     historical_tod_mean  3.538011       NaN   6.115244       NaN  0.099902       NaN
                                     neighbor_average     5.953598       NaN   9.833834       NaN  0.124693       NaN
       validation_swap_selected      gls_map              2.709062       NaN   4.384380       NaN  0.071167       NaN
                                     gsp                  3.899423       NaN   6.375211       NaN  0.118438       NaN
                                     historical_tod_mean  4.111061       NaN   6.994695       NaN  0.133222       NaN
                                     neighbor_average     4.543207       NaN   7.177179       NaN  0.114986       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 3.212997 5.322175
    0.2            rcss_selected gls_map 2.916501 4.792680
    0.3 validation_swap_selected gls_map 2.709062 4.384380
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.015687     -0.036202 210
    gsp   condition_number    -0.016144     -0.093730 210
    gsp information_logdet     0.045059      0.033991 210
gls_map    posterior_trace     0.861811      0.866187 210
gls_map   condition_number     0.873427      0.874711 210
gls_map information_logdet    -0.766380     -0.812088 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv