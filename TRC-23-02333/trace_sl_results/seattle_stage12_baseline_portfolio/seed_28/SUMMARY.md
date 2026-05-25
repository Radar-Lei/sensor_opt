---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-22, 2015-01-05
Test days: 2015-01-03, 2015-01-21
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.185281       NaN   5.285864       NaN  0.090387       NaN
                                     gsp                  4.307448       NaN   6.940457       NaN  0.130569       NaN
                                     historical_tod_mean  5.457268       NaN   8.747372       NaN  0.163456       NaN
                                     neighbor_average     5.405139       NaN   9.481432       NaN  0.177282       NaN
       best_random_by_validation     gls_map              3.021700       NaN   5.118711       NaN  0.088871       NaN
                                     gsp                  4.192018       NaN   6.871587       NaN  0.131612       NaN
                                     historical_tod_mean  5.395772       NaN   8.694963       NaN  0.163086       NaN
                                     neighbor_average     4.947222       NaN   8.376678       NaN  0.156845       NaN
       coverage                      gls_map              3.082301       NaN   5.135558       NaN  0.087364       NaN
                                     gsp                  4.201233       NaN   6.884513       NaN  0.130816       NaN
                                     historical_tod_mean  5.425623       NaN   8.750106       NaN  0.162511       NaN
                                     neighbor_average     5.039759       NaN   8.210038       NaN  0.152106       NaN
       degree                        gls_map              3.470721       NaN   5.716557       NaN  0.094267       NaN
                                     gsp                  4.282139       NaN   6.823742       NaN  0.124015       NaN
                                     historical_tod_mean  5.382603       NaN   8.664236       NaN  0.158400       NaN
                                     neighbor_average     5.796196       NaN   9.647309       NaN  0.175871       NaN
       graph_sampling_laplacian      gls_map              3.560715       NaN   6.058667       NaN  0.113281       NaN
                                     gsp                  4.287777       NaN   6.962153       NaN  0.133997       NaN
                                     historical_tod_mean  5.476012       NaN   8.841108       NaN  0.166317       NaN
                                     neighbor_average     5.604188       NaN   9.745164       NaN  0.197767       NaN
       greedy_a_trace                gls_map              2.942725       NaN   4.928589       NaN  0.085279       NaN
                                     gsp                  4.173863       NaN   6.772495       NaN  0.128076       NaN
                                     historical_tod_mean  5.399619       NaN   8.686705       NaN  0.161249       NaN
                                     neighbor_average     4.992445       NaN   8.362550       NaN  0.153198       NaN
       greedy_d_logdet               gls_map              3.648663       NaN   5.952994       NaN  0.111207       NaN
                                     gsp                  4.538251       NaN   7.426104       NaN  0.142218       NaN
                                     historical_tod_mean  5.561828       NaN   8.891201       NaN  0.168045       NaN
                                     neighbor_average     5.532098       NaN   9.660463       NaN  0.204498       NaN
       multistart_swap_by_validation gls_map              2.899817       NaN   4.846515       NaN  0.082763       NaN
                                     gsp                  4.164648       NaN   6.812970       NaN  0.128300       NaN
                                     historical_tod_mean  5.381386       NaN   8.659461       NaN  0.160409       NaN
                                     neighbor_average     5.284377       NaN   8.761541       NaN  0.156780       NaN
       observability_proxy           gls_map              3.395619       NaN   5.594341       NaN  0.093286       NaN
                                     gsp                  4.261791       NaN   6.785141       NaN  0.123635       NaN
                                     historical_tod_mean  5.377450       NaN   8.650470       NaN  0.158915       NaN
                                     neighbor_average     5.850994       NaN   9.806790       NaN  0.177267       NaN
       qr_pod_modes                  gls_map              3.411340       NaN   5.629679       NaN  0.101114       NaN
                                     gsp                  4.335487       NaN   7.094736       NaN  0.135370       NaN
                                     historical_tod_mean  5.500712       NaN   8.820498       NaN  0.165217       NaN
                                     neighbor_average     5.285097       NaN   9.147677       NaN  0.188899       NaN
       random                        gls_map              3.159129  0.082188   5.290086  0.154687  0.091645  0.004746
                                     gsp                  4.182804  0.048011   6.821087  0.077350  0.130212  0.002713
                                     historical_tod_mean  5.387829  0.040445   8.692803  0.060032  0.162227  0.002510
                                     neighbor_average     5.283257  0.207721   8.895273  0.375017  0.164031  0.010577
       rcss_selected                 gls_map              2.899817       NaN   4.846515       NaN  0.082763       NaN
                                     gsp                  4.164648       NaN   6.812970       NaN  0.128300       NaN
                                     historical_tod_mean  5.381386       NaN   8.659461       NaN  0.160409       NaN
                                     neighbor_average     5.284377       NaN   8.761541       NaN  0.156780       NaN
       robust_coverage_cvar          gls_map              3.060515       NaN   5.243052       NaN  0.093701       NaN
                                     gsp                  4.214775       NaN   6.924877       NaN  0.133281       NaN
                                     historical_tod_mean  5.440068       NaN   8.754371       NaN  0.164881       NaN
                                     neighbor_average     4.849949       NaN   8.320911       NaN  0.164923       NaN
       scenario_average_a_trace      gls_map              3.004807       NaN   4.963288       NaN  0.083250       NaN
                                     gsp                  4.233924       NaN   6.876183       NaN  0.130004       NaN
                                     historical_tod_mean  5.424653       NaN   8.710465       NaN  0.162217       NaN
                                     neighbor_average     5.396995       NaN   8.615508       NaN  0.164209       NaN
       scenario_cvar_a_trace         gls_map              3.107699       NaN   5.395203       NaN  0.097550       NaN
                                     gsp                  4.245211       NaN   6.999966       NaN  0.136458       NaN
                                     historical_tod_mean  5.478766       NaN   8.805910       NaN  0.166893       NaN
                                     neighbor_average     5.039940       NaN   8.918675       NaN  0.178160       NaN
       swap_from_best_random_trace   gls_map              2.944322       NaN   4.923237       NaN  0.084546       NaN
                                     gsp                  4.210928       NaN   6.856821       NaN  0.129475       NaN
                                     historical_tod_mean  5.416757       NaN   8.706709       NaN  0.162276       NaN
                                     neighbor_average     5.116693       NaN   8.557331       NaN  0.159450       NaN
       swap_from_greedy_a_trace      gls_map              2.898968       NaN   4.785680       NaN  0.079845       NaN
                                     gsp                  4.180159       NaN   6.803285       NaN  0.127414       NaN
                                     historical_tod_mean  5.392639       NaN   8.666780       NaN  0.160320       NaN
                                     neighbor_average     5.256995       NaN   8.654690       NaN  0.154948       NaN
       swap_from_scenario_average    gls_map              2.905370       NaN   4.817780       NaN  0.080660       NaN
                                     gsp                  4.177277       NaN   6.809794       NaN  0.127931       NaN
                                     historical_tod_mean  5.394296       NaN   8.674028       NaN  0.160483       NaN
                                     neighbor_average     5.415964       NaN   8.858235       NaN  0.158454       NaN
       swap_from_scenario_cvar       gls_map              2.956604       NaN   4.909972       NaN  0.083918       NaN
                                     gsp                  4.213451       NaN   6.845258       NaN  0.128628       NaN
                                     historical_tod_mean  5.406980       NaN   8.683462       NaN  0.161326       NaN
                                     neighbor_average     5.189674       NaN   8.680110       NaN  0.159143       NaN
       top_variance                  gls_map              3.436726       NaN   5.572119       NaN  0.090127       NaN
                                     gsp                  3.949765       NaN   6.312627       NaN  0.110518       NaN
                                     historical_tod_mean  4.951667       NaN   7.965623       NaN  0.136246       NaN
                                     neighbor_average     8.289769       NaN  14.386465       NaN  0.171072       NaN
       validation_swap_selected      gls_map              2.896677       NaN   4.838000       NaN  0.082550       NaN
                                     gsp                  4.154598       NaN   6.799887       NaN  0.127997       NaN
                                     historical_tod_mean  5.371191       NaN   8.653061       NaN  0.160234       NaN
                                     neighbor_average     5.290799       NaN   8.748182       NaN  0.156634       NaN
0.2    best_random_by_trace          gls_map              2.891650       NaN   4.824369       NaN  0.078864       NaN
                                     gsp                  4.134030       NaN   6.636529       NaN  0.126258       NaN
                                     historical_tod_mean  5.405569       NaN   8.709342       NaN  0.162852       NaN
                                     neighbor_average     4.733522       NaN   7.874316       NaN  0.132759       NaN
       best_random_by_validation     gls_map              2.813260       NaN   4.616634       NaN  0.073742       NaN
                                     gsp                  4.056938       NaN   6.454988       NaN  0.119965       NaN
                                     historical_tod_mean  5.284643       NaN   8.511627       NaN  0.154400       NaN
                                     neighbor_average     4.414896       NaN   7.256107       NaN  0.119452       NaN
       coverage                      gls_map              2.731629       NaN   4.551271       NaN  0.073809       NaN
                                     gsp                  4.100139       NaN   6.628861       NaN  0.125649       NaN
                                     historical_tod_mean  5.430314       NaN   8.739425       NaN  0.162036       NaN
                                     neighbor_average     4.250121       NaN   6.921757       NaN  0.120631       NaN
       degree                        gls_map              3.348931       NaN   5.594095       NaN  0.089869       NaN
                                     gsp                  4.257877       NaN   6.711821       NaN  0.117805       NaN
                                     historical_tod_mean  5.405214       NaN   8.651996       NaN  0.156371       NaN
                                     neighbor_average     5.691548       NaN   9.598933       NaN  0.181204       NaN
       graph_sampling_laplacian      gls_map              3.564351       NaN   6.166610       NaN  0.119304       NaN
                                     gsp                  4.298054       NaN   6.958226       NaN  0.138570       NaN
                                     historical_tod_mean  5.535916       NaN   8.946249       NaN  0.170768       NaN
                                     neighbor_average     5.726591       NaN   9.978122       NaN  0.200808       NaN
       greedy_a_trace                gls_map              2.727119       NaN   4.531523       NaN  0.077388       NaN
                                     gsp                  4.191763       NaN   6.774484       NaN  0.129488       NaN
                                     historical_tod_mean  5.513720       NaN   8.827967       NaN  0.164619       NaN
                                     neighbor_average     4.344378       NaN   7.279854       NaN  0.138187       NaN
       greedy_d_logdet               gls_map              3.339373       NaN   5.638757       NaN  0.105225       NaN
                                     gsp                  4.425263       NaN   7.177602       NaN  0.142575       NaN
                                     historical_tod_mean  5.753401       NaN   9.139371       NaN  0.176861       NaN
                                     neighbor_average     5.280295       NaN   9.353332       NaN  0.201405       NaN
       multistart_swap_by_validation gls_map              2.732630       NaN   4.440521       NaN  0.073617       NaN
                                     gsp                  4.147796       NaN   6.678020       NaN  0.126718       NaN
                                     historical_tod_mean  5.486001       NaN   8.760194       NaN  0.161950       NaN
                                     neighbor_average     4.337343       NaN   7.065830       NaN  0.130169       NaN
       observability_proxy           gls_map              3.237165       NaN   5.389908       NaN  0.084734       NaN
                                     gsp                  4.245971       NaN   6.692555       NaN  0.115807       NaN
                                     historical_tod_mean  5.371402       NaN   8.598994       NaN  0.153988       NaN
                                     neighbor_average     5.813059       NaN   9.714196       NaN  0.170209       NaN
       qr_pod_modes                  gls_map              2.881749       NaN   4.759835       NaN  0.082043       NaN
                                     gsp                  4.257588       NaN   6.921848       NaN  0.134954       NaN
                                     historical_tod_mean  5.620234       NaN   8.973137       NaN  0.170731       NaN
                                     neighbor_average     4.657541       NaN   7.860454       NaN  0.159482       NaN
       random                        gls_map              2.868748  0.055240   4.829795  0.145292  0.081704  0.005585
                                     gsp                  4.101785  0.045484   6.620239  0.102678  0.127162  0.004872
                                     historical_tod_mean  5.394704  0.067635   8.705904  0.108126  0.162746  0.004765
                                     neighbor_average     4.704681  0.165709   7.888874  0.318970  0.138947  0.011523
       rcss_selected                 gls_map              2.689621       NaN   4.458986       NaN  0.072280       NaN
                                     gsp                  4.001373       NaN   6.442185       NaN  0.121126       NaN
                                     historical_tod_mean  5.262146       NaN   8.505080       NaN  0.155854       NaN
                                     neighbor_average     4.560493       NaN   7.546316       NaN  0.121633       NaN
       robust_coverage_cvar          gls_map              2.810675       NaN   4.668579       NaN  0.079788       NaN
                                     gsp                  4.167184       NaN   6.785503       NaN  0.131986       NaN
                                     historical_tod_mean  5.527885       NaN   8.861919       NaN  0.168067       NaN
                                     neighbor_average     4.447182       NaN   7.380856       NaN  0.141890       NaN
       scenario_average_a_trace      gls_map              2.867173       NaN   4.786043       NaN  0.082979       NaN
                                     gsp                  4.234909       NaN   6.897606       NaN  0.135054       NaN
                                     historical_tod_mean  5.561210       NaN   8.912965       NaN  0.170001       NaN
                                     neighbor_average     4.703887       NaN   7.792331       NaN  0.155535       NaN
       scenario_cvar_a_trace         gls_map              2.948612       NaN   5.013990       NaN  0.086787       NaN
                                     gsp                  4.240797       NaN   6.868838       NaN  0.134659       NaN
                                     historical_tod_mean  5.613434       NaN   8.986397       NaN  0.171971       NaN
                                     neighbor_average     4.686057       NaN   8.125885       NaN  0.164276       NaN
       swap_from_best_random_trace   gls_map              2.773930       NaN   4.562944       NaN  0.076965       NaN
                                     gsp                  4.206959       NaN   6.739744       NaN  0.127909       NaN
                                     historical_tod_mean  5.531846       NaN   8.831458       NaN  0.165070       NaN
                                     neighbor_average     4.541062       NaN   7.497221       NaN  0.142592       NaN
       swap_from_greedy_a_trace      gls_map              2.734604       NaN   4.549071       NaN  0.078416       NaN
                                     gsp                  4.193137       NaN   6.807961       NaN  0.131541       NaN
                                     historical_tod_mean  5.536601       NaN   8.863173       NaN  0.166552       NaN
                                     neighbor_average     4.331464       NaN   7.336384       NaN  0.140935       NaN
       swap_from_scenario_average    gls_map              2.759752       NaN   4.611792       NaN  0.079701       NaN
                                     gsp                  4.221385       NaN   6.854373       NaN  0.133060       NaN
                                     historical_tod_mean  5.558837       NaN   8.898549       NaN  0.168902       NaN
                                     neighbor_average     4.608526       NaN   7.775056       NaN  0.154472       NaN
       swap_from_scenario_cvar       gls_map              2.728669       NaN   4.567583       NaN  0.078313       NaN
                                     gsp                  4.172036       NaN   6.803128       NaN  0.132371       NaN
                                     historical_tod_mean  5.516459       NaN   8.852678       NaN  0.167346       NaN
                                     neighbor_average     4.412973       NaN   7.495918       NaN  0.147535       NaN
       top_variance                  gls_map              2.878582       NaN   4.733192       NaN  0.071139       NaN
                                     gsp                  3.678820       NaN   5.773324       NaN  0.093148       NaN
                                     historical_tod_mean  4.644306       NaN   7.398662       NaN  0.115905       NaN
                                     neighbor_average     6.122170       NaN  10.729240       NaN  0.124275       NaN
       validation_swap_selected      gls_map              2.666447       NaN   4.446045       NaN  0.073333       NaN
                                     gsp                  3.944060       NaN   6.381107       NaN  0.120268       NaN
                                     historical_tod_mean  5.223507       NaN   8.461192       NaN  0.155104       NaN
                                     neighbor_average     4.471447       NaN   7.345486       NaN  0.122214       NaN
0.3    best_random_by_trace          gls_map              2.680492       NaN   4.564638       NaN  0.078253       NaN
                                     gsp                  4.116867       NaN   6.667220       NaN  0.129539       NaN
                                     historical_tod_mean  5.490704       NaN   8.861211       NaN  0.167015       NaN
                                     neighbor_average     4.271395       NaN   7.146771       NaN  0.124973       NaN
       best_random_by_validation     gls_map              2.578830       NaN   4.325661       NaN  0.070628       NaN
                                     gsp                  4.018436       NaN   6.438765       NaN  0.122123       NaN
                                     historical_tod_mean  5.309417       NaN   8.618449       NaN  0.159544       NaN
                                     neighbor_average     4.206095       NaN   7.063677       NaN  0.113493       NaN
       coverage                      gls_map              2.531174       NaN   4.181255       NaN  0.068448       NaN
                                     gsp                  4.097620       NaN   6.595276       NaN  0.125903       NaN
                                     historical_tod_mean  5.413246       NaN   8.748941       NaN  0.162612       NaN
                                     neighbor_average     4.121440       NaN   6.544671       NaN  0.109660       NaN
       degree                        gls_map              3.239832       NaN   5.375329       NaN  0.083798       NaN
                                     gsp                  4.224972       NaN   6.637103       NaN  0.114168       NaN
                                     historical_tod_mean  5.406591       NaN   8.560240       NaN  0.150864       NaN
                                     neighbor_average     6.382309       NaN  10.912436       NaN  0.171462       NaN
       graph_sampling_laplacian      gls_map              3.458729       NaN   5.895037       NaN  0.111148       NaN
                                     gsp                  4.296668       NaN   6.847339       NaN  0.137640       NaN
                                     historical_tod_mean  5.476192       NaN   8.862734       NaN  0.168466       NaN
                                     neighbor_average     6.046264       NaN  10.328974       NaN  0.201593       NaN
       greedy_a_trace                gls_map              2.615280       NaN   4.304471       NaN  0.072887       NaN
                                     gsp                  4.258938       NaN   6.801112       NaN  0.131072       NaN
                                     historical_tod_mean  5.658102       NaN   9.010762       NaN  0.169488       NaN
                                     neighbor_average     4.093319       NaN   6.767917       NaN  0.125760       NaN
       greedy_d_logdet               gls_map              3.045748       NaN   5.140682       NaN  0.094506       NaN
                                     gsp                  4.412702       NaN   7.067923       NaN  0.143133       NaN
                                     historical_tod_mean  5.885560       NaN   9.337225       NaN  0.183161       NaN
                                     neighbor_average     4.811864       NaN   8.463096       NaN  0.180456       NaN
       multistart_swap_by_validation gls_map              2.587415       NaN   4.297566       NaN  0.071972       NaN
                                     gsp                  4.165913       NaN   6.628351       NaN  0.127434       NaN
                                     historical_tod_mean  5.512822       NaN   8.828620       NaN  0.165406       NaN
                                     neighbor_average     4.004112       NaN   6.589764       NaN  0.118055       NaN
       observability_proxy           gls_map              3.236274       NaN   5.368122       NaN  0.083468       NaN
                                     gsp                  4.226450       NaN   6.646608       NaN  0.113633       NaN
                                     historical_tod_mean  5.406105       NaN   8.558077       NaN  0.149967       NaN
                                     neighbor_average     6.290413       NaN  10.811560       NaN  0.169873       NaN
       qr_pod_modes                  gls_map              2.657851       NaN   4.333394       NaN  0.074221       NaN
                                     gsp                  4.263711       NaN   6.845959       NaN  0.133354       NaN
                                     historical_tod_mean  5.702936       NaN   9.072677       NaN  0.171113       NaN
                                     neighbor_average     4.214540       NaN   6.872761       NaN  0.132838       NaN
       random                        gls_map              2.690018  0.047301   4.530119  0.131289  0.075378  0.004002
                                     gsp                  4.083837  0.041317   6.550909  0.080213  0.125871  0.003675
                                     historical_tod_mean  5.398032  0.065660   8.712001  0.098234  0.162813  0.004011
                                     neighbor_average     4.347000  0.117456   7.259104  0.248185  0.122398  0.007992
       rcss_selected                 gls_map              2.468820       NaN   4.150319       NaN  0.068488       NaN
                                     gsp                  3.927109       NaN   6.388801       NaN  0.122366       NaN
                                     historical_tod_mean  5.236890       NaN   8.514670       NaN  0.158202       NaN
                                     neighbor_average     4.164677       NaN   6.718456       NaN  0.109081       NaN
       robust_coverage_cvar          gls_map              2.708160       NaN   4.494004       NaN  0.079279       NaN
                                     gsp                  4.251352       NaN   6.866911       NaN  0.138587       NaN
                                     historical_tod_mean  5.679626       NaN   9.091329       NaN  0.177935       NaN
                                     neighbor_average     4.259303       NaN   7.113742       NaN  0.142618       NaN
       scenario_average_a_trace      gls_map              2.719384       NaN   4.553010       NaN  0.078716       NaN
                                     gsp                  4.229784       NaN   6.822042       NaN  0.135605       NaN
                                     historical_tod_mean  5.651877       NaN   9.043276       NaN  0.174289       NaN
                                     neighbor_average     4.347699       NaN   7.094389       NaN  0.138372       NaN
       scenario_cvar_a_trace         gls_map              2.813267       NaN   4.779060       NaN  0.084586       NaN
                                     gsp                  4.295856       NaN   6.931531       NaN  0.140253       NaN
                                     historical_tod_mean  5.737109       NaN   9.165712       NaN  0.179212       NaN
                                     neighbor_average     4.423806       NaN   7.609980       NaN  0.157693       NaN
       swap_from_best_random_trace   gls_map              2.626511       NaN   4.325484       NaN  0.074551       NaN
                                     gsp                  4.224476       NaN   6.800437       NaN  0.134333       NaN
                                     historical_tod_mean  5.651215       NaN   9.044088       NaN  0.173862       NaN
                                     neighbor_average     4.190536       NaN   7.012478       NaN  0.135863       NaN
       swap_from_greedy_a_trace      gls_map              2.615807       NaN   4.250954       NaN  0.070754       NaN
                                     gsp                  4.258191       NaN   6.792707       NaN  0.130119       NaN
                                     historical_tod_mean  5.678092       NaN   9.018363       NaN  0.169152       NaN
                                     neighbor_average     4.108793       NaN   6.750157       NaN  0.122649       NaN
       swap_from_scenario_average    gls_map              2.635644       NaN   4.300631       NaN  0.071863       NaN
                                     gsp                  4.255875       NaN   6.791289       NaN  0.131140       NaN
                                     historical_tod_mean  5.688748       NaN   9.030944       NaN  0.170524       NaN
                                     neighbor_average     4.167259       NaN   6.909530       NaN  0.127324       NaN
       swap_from_scenario_cvar       gls_map              2.621030       NaN   4.338530       NaN  0.075445       NaN
                                     gsp                  4.244672       NaN   6.837806       NaN  0.134891       NaN
                                     historical_tod_mean  5.667581       NaN   9.044286       NaN  0.172581       NaN
                                     neighbor_average     4.116177       NaN   6.834309       NaN  0.130646       NaN
       top_variance                  gls_map              2.661265       NaN   4.436512       NaN  0.064548       NaN
                                     gsp                  3.481809       NaN   5.464916       NaN  0.084396       NaN
                                     historical_tod_mean  4.411859       NaN   6.989916       NaN  0.104729       NaN
                                     neighbor_average     5.538338       NaN   9.713060       NaN  0.109497       NaN
       validation_swap_selected      gls_map              2.468228       NaN   4.020579       NaN  0.064917       NaN
                                     gsp                  3.960830       NaN   6.315338       NaN  0.119722       NaN
                                     historical_tod_mean  5.209469       NaN   8.458548       NaN  0.155345       NaN
                                     neighbor_average     4.143006       NaN   6.650304       NaN  0.110867       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 2.896677 4.838000
    0.2 validation_swap_selected gls_map 2.666447 4.446045
    0.3 validation_swap_selected gls_map 2.468228 4.020579
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.377046      0.378170 210
    gsp   condition_number     0.378224      0.399020 210
    gsp information_logdet    -0.339779     -0.406109 210
gls_map    posterior_trace     0.874245      0.879293 210
gls_map   condition_number     0.889486      0.898900 210
gls_map information_logdet    -0.775277     -0.813479 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv