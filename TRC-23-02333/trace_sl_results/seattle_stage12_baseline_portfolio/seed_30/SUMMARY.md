---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-16, 2015-01-26
Test days: 2015-01-25, 2015-01-28
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              2.945413       NaN   4.834446       NaN  0.075380       NaN
                                     gsp                  4.149854       NaN   6.548814       NaN  0.110064       NaN
                                     historical_tod_mean  5.646474       NaN   8.712528       NaN  0.143956       NaN
                                     neighbor_average     5.689348       NaN   9.254574       NaN  0.148313       NaN
       best_random_by_validation     gls_map              2.983705       NaN   4.933941       NaN  0.074098       NaN
                                     gsp                  4.140267       NaN   6.447921       NaN  0.107084       NaN
                                     historical_tod_mean  5.596779       NaN   8.612908       NaN  0.140359       NaN
                                     neighbor_average     5.226645       NaN   8.536459       NaN  0.127023       NaN
       coverage                      gls_map              3.021958       NaN   4.970956       NaN  0.077481       NaN
                                     gsp                  4.243650       NaN   6.702246       NaN  0.114316       NaN
                                     historical_tod_mean  5.744548       NaN   8.846461       NaN  0.147378       NaN
                                     neighbor_average     4.925924       NaN   7.942765       NaN  0.142200       NaN
       degree                        gls_map              3.354917       NaN   5.456446       NaN  0.087916       NaN
                                     gsp                  4.208705       NaN   6.637270       NaN  0.114544       NaN
                                     historical_tod_mean  5.705673       NaN   8.811715       NaN  0.147901       NaN
                                     neighbor_average     5.696718       NaN   9.491686       NaN  0.165082       NaN
       graph_sampling_laplacian      gls_map              3.580021       NaN   5.743057       NaN  0.091524       NaN
                                     gsp                  4.328101       NaN   6.763667       NaN  0.116179       NaN
                                     historical_tod_mean  5.787699       NaN   8.914294       NaN  0.148786       NaN
                                     neighbor_average     5.914461       NaN  10.248205       NaN  0.177701       NaN
       greedy_a_trace                gls_map              2.877035       NaN   4.731078       NaN  0.074280       NaN
                                     gsp                  4.194441       NaN   6.640601       NaN  0.112940       NaN
                                     historical_tod_mean  5.711811       NaN   8.785146       NaN  0.146451       NaN
                                     neighbor_average     4.993546       NaN   8.157444       NaN  0.142257       NaN
       greedy_d_logdet               gls_map              3.405743       NaN   5.371375       NaN  0.085467       NaN
                                     gsp                  4.510641       NaN   7.142236       NaN  0.122458       NaN
                                     historical_tod_mean  5.881930       NaN   8.966734       NaN  0.150667       NaN
                                     neighbor_average     5.474080       NaN   9.344900       NaN  0.178052       NaN
       multistart_swap_by_validation gls_map              2.863305       NaN   4.706691       NaN  0.073624       NaN
                                     gsp                  4.239170       NaN   6.701369       NaN  0.114080       NaN
                                     historical_tod_mean  5.722151       NaN   8.788164       NaN  0.147241       NaN
                                     neighbor_average     4.881135       NaN   8.040591       NaN  0.145620       NaN
       observability_proxy           gls_map              3.339718       NaN   5.401393       NaN  0.086646       NaN
                                     gsp                  4.230070       NaN   6.627183       NaN  0.113118       NaN
                                     historical_tod_mean  5.710438       NaN   8.810981       NaN  0.148186       NaN
                                     neighbor_average     5.598089       NaN   9.265253       NaN  0.160448       NaN
       qr_pod_modes                  gls_map              3.134955       NaN   5.043189       NaN  0.080534       NaN
                                     gsp                  4.259252       NaN   6.768849       NaN  0.116629       NaN
                                     historical_tod_mean  5.785397       NaN   8.861660       NaN  0.148673       NaN
                                     neighbor_average     5.148274       NaN   8.835200       NaN  0.164558       NaN
       random                        gls_map              3.090730  0.082356   5.063900  0.150677  0.078654  0.002949
                                     gsp                  4.203968  0.041648   6.605827  0.076953  0.111972  0.002176
                                     historical_tod_mean  5.696227  0.038220   8.772735  0.054638  0.145896  0.001825
                                     neighbor_average     5.131170  0.210385   8.515231  0.329242  0.144894  0.006901
       rcss_selected                 gls_map              2.932404       NaN   4.725463       NaN  0.071577       NaN
                                     gsp                  4.170731       NaN   6.458419       NaN  0.108881       NaN
                                     historical_tod_mean  5.634217       NaN   8.665128       NaN  0.143069       NaN
                                     neighbor_average     4.821536       NaN   7.917848       NaN  0.126999       NaN
       robust_coverage_cvar          gls_map              2.947028       NaN   4.896856       NaN  0.076028       NaN
                                     gsp                  4.190386       NaN   6.617248       NaN  0.112321       NaN
                                     historical_tod_mean  5.737923       NaN   8.824301       NaN  0.147516       NaN
                                     neighbor_average     4.886349       NaN   8.132065       NaN  0.143129       NaN
       scenario_average_a_trace      gls_map              3.043824       NaN   4.990322       NaN  0.075382       NaN
                                     gsp                  4.201478       NaN   6.632702       NaN  0.111798       NaN
                                     historical_tod_mean  5.717550       NaN   8.786303       NaN  0.145929       NaN
                                     neighbor_average     5.024271       NaN   8.527244       NaN  0.148783       NaN
       scenario_cvar_a_trace         gls_map              3.236876       NaN   5.417844       NaN  0.082810       NaN
                                     gsp                  4.285874       NaN   6.709587       NaN  0.113961       NaN
                                     historical_tod_mean  5.767826       NaN   8.846129       NaN  0.147564       NaN
                                     neighbor_average     5.032869       NaN   8.209127       NaN  0.147838       NaN
       swap_from_best_random_trace   gls_map              2.871099       NaN   4.665276       NaN  0.072974       NaN
                                     gsp                  4.245492       NaN   6.715731       NaN  0.113793       NaN
                                     historical_tod_mean  5.712415       NaN   8.776607       NaN  0.145654       NaN
                                     neighbor_average     5.029050       NaN   8.058911       NaN  0.141227       NaN
       swap_from_greedy_a_trace      gls_map              2.839402       NaN   4.661600       NaN  0.072696       NaN
                                     gsp                  4.247310       NaN   6.723040       NaN  0.114116       NaN
                                     historical_tod_mean  5.726221       NaN   8.801310       NaN  0.146989       NaN
                                     neighbor_average     5.073690       NaN   8.207352       NaN  0.146321       NaN
       swap_from_scenario_average    gls_map              2.886655       NaN   4.732846       NaN  0.074174       NaN
                                     gsp                  4.259285       NaN   6.749815       NaN  0.114234       NaN
                                     historical_tod_mean  5.742294       NaN   8.809145       NaN  0.146042       NaN
                                     neighbor_average     5.054828       NaN   8.263938       NaN  0.146329       NaN
       swap_from_scenario_cvar       gls_map              3.086584       NaN   5.131309       NaN  0.078860       NaN
                                     gsp                  4.249112       NaN   6.683864       NaN  0.113248       NaN
                                     historical_tod_mean  5.744519       NaN   8.819397       NaN  0.147355       NaN
                                     neighbor_average     5.144920       NaN   8.358856       NaN  0.150403       NaN
       top_variance                  gls_map              3.357206       NaN   5.210852       NaN  0.079158       NaN
                                     gsp                  4.059427       NaN   6.217311       NaN  0.097975       NaN
                                     historical_tod_mean  5.297992       NaN   8.115264       NaN  0.125331       NaN
                                     neighbor_average     7.848572       NaN  13.256072       NaN  0.156341       NaN
       validation_swap_selected      gls_map              2.937948       NaN   4.745020       NaN  0.071441       NaN
                                     gsp                  4.182834       NaN   6.466660       NaN  0.108942       NaN
                                     historical_tod_mean  5.638899       NaN   8.666559       NaN  0.143041       NaN
                                     neighbor_average     4.849904       NaN   7.962603       NaN  0.131046       NaN
0.2    best_random_by_trace          gls_map              2.761587       NaN   4.545245       NaN  0.070852       NaN
                                     gsp                  4.089536       NaN   6.402704       NaN  0.110784       NaN
                                     historical_tod_mean  5.694240       NaN   8.783075       NaN  0.147252       NaN
                                     neighbor_average     4.456134       NaN   7.549840       NaN  0.127983       NaN
       best_random_by_validation     gls_map              2.761139       NaN   4.482641       NaN  0.069369       NaN
                                     gsp                  4.074530       NaN   6.345115       NaN  0.106133       NaN
                                     historical_tod_mean  5.674057       NaN   8.749666       NaN  0.145605       NaN
                                     neighbor_average     4.815768       NaN   7.955656       NaN  0.130180       NaN
       coverage                      gls_map              2.690974       NaN   4.529429       NaN  0.069710       NaN
                                     gsp                  4.089436       NaN   6.431620       NaN  0.110345       NaN
                                     historical_tod_mean  5.750162       NaN   8.854381       NaN  0.148736       NaN
                                     neighbor_average     4.218978       NaN   6.903233       NaN  0.121476       NaN
       degree                        gls_map              3.240623       NaN   5.307088       NaN  0.084065       NaN
                                     gsp                  4.170903       NaN   6.516815       NaN  0.111732       NaN
                                     historical_tod_mean  5.767333       NaN   8.899854       NaN  0.151097       NaN
                                     neighbor_average     5.778054       NaN   9.679510       NaN  0.167131       NaN
       graph_sampling_laplacian      gls_map              3.396327       NaN   5.599121       NaN  0.087266       NaN
                                     gsp                  4.275952       NaN   6.599822       NaN  0.113238       NaN
                                     historical_tod_mean  5.804682       NaN   8.947429       NaN  0.149765       NaN
                                     neighbor_average     5.610593       NaN   9.586016       NaN  0.169922       NaN
       greedy_a_trace                gls_map              2.654087       NaN   4.395734       NaN  0.067402       NaN
                                     gsp                  4.172598       NaN   6.574650       NaN  0.112475       NaN
                                     historical_tod_mean  5.834956       NaN   8.943068       NaN  0.149093       NaN
                                     neighbor_average     4.417115       NaN   7.214604       NaN  0.125593       NaN
       greedy_d_logdet               gls_map              3.118875       NaN   4.994143       NaN  0.080273       NaN
                                     gsp                  4.356311       NaN   6.822874       NaN  0.119310       NaN
                                     historical_tod_mean  6.026444       NaN   9.171403       NaN  0.156475       NaN
                                     neighbor_average     5.057038       NaN   8.819450       NaN  0.171609       NaN
       multistart_swap_by_validation gls_map              2.677682       NaN   4.401934       NaN  0.069132       NaN
                                     gsp                  4.158409       NaN   6.532930       NaN  0.112961       NaN
                                     historical_tod_mean  5.823803       NaN   8.939697       NaN  0.150559       NaN
                                     neighbor_average     4.329055       NaN   7.128239       NaN  0.130174       NaN
       observability_proxy           gls_map              3.159612       NaN   5.192654       NaN  0.081024       NaN
                                     gsp                  4.169169       NaN   6.513092       NaN  0.110610       NaN
                                     historical_tod_mean  5.747846       NaN   8.868508       NaN  0.149941       NaN
                                     neighbor_average     5.650422       NaN   9.432324       NaN  0.160373       NaN
       qr_pod_modes                  gls_map              2.835197       NaN   4.618808       NaN  0.073844       NaN
                                     gsp                  4.239228       NaN   6.667006       NaN  0.117311       NaN
                                     historical_tod_mean  5.933860       NaN   9.074674       NaN  0.154891       NaN
                                     neighbor_average     4.645882       NaN   7.917575       NaN  0.149547       NaN
       random                        gls_map              2.820255  0.062238   4.672780  0.117666  0.071816  0.002365
                                     gsp                  4.097168  0.032795   6.386742  0.063897  0.108853  0.002559
                                     historical_tod_mean  5.704555  0.046381   8.789944  0.068825  0.146524  0.002364
                                     neighbor_average     4.646493  0.155329   7.757567  0.297837  0.127778  0.006083
       rcss_selected                 gls_map              2.660551       NaN   4.433372       NaN  0.067530       NaN
                                     gsp                  4.014937       NaN   6.271298       NaN  0.106246       NaN
                                     historical_tod_mean  5.602874       NaN   8.649745       NaN  0.143284       NaN
                                     neighbor_average     4.491950       NaN   7.441540       NaN  0.115348       NaN
       robust_coverage_cvar          gls_map              2.775787       NaN   4.533251       NaN  0.070390       NaN
                                     gsp                  4.166825       NaN   6.524187       NaN  0.112429       NaN
                                     historical_tod_mean  5.831413       NaN   8.941481       NaN  0.150762       NaN
                                     neighbor_average     4.487315       NaN   7.411318       NaN  0.135001       NaN
       scenario_average_a_trace      gls_map              2.827239       NaN   4.599224       NaN  0.070660       NaN
                                     gsp                  4.208154       NaN   6.591466       NaN  0.113870       NaN
                                     historical_tod_mean  5.870920       NaN   9.002432       NaN  0.151803       NaN
                                     neighbor_average     4.680063       NaN   7.902803       NaN  0.145132       NaN
       scenario_cvar_a_trace         gls_map              2.985899       NaN   4.873360       NaN  0.074505       NaN
                                     gsp                  4.239901       NaN   6.572298       NaN  0.112529       NaN
                                     historical_tod_mean  5.900155       NaN   9.003697       NaN  0.151812       NaN
                                     neighbor_average     4.496587       NaN   7.326290       NaN  0.133805       NaN
       swap_from_best_random_trace   gls_map              2.712857       NaN   4.414710       NaN  0.069653       NaN
                                     gsp                  4.188112       NaN   6.575533       NaN  0.114584       NaN
                                     historical_tod_mean  5.866493       NaN   8.985682       NaN  0.151546       NaN
                                     neighbor_average     4.419355       NaN   7.414964       NaN  0.134429       NaN
       swap_from_greedy_a_trace      gls_map              2.635593       NaN   4.336556       NaN  0.066743       NaN
                                     gsp                  4.193157       NaN   6.583639       NaN  0.112814       NaN
                                     historical_tod_mean  5.863204       NaN   8.940490       NaN  0.148835       NaN
                                     neighbor_average     4.340007       NaN   7.127430       NaN  0.124876       NaN
       swap_from_scenario_average    gls_map              2.684598       NaN   4.352171       NaN  0.067981       NaN
                                     gsp                  4.186637       NaN   6.546349       NaN  0.113324       NaN
                                     historical_tod_mean  5.864105       NaN   8.968784       NaN  0.151381       NaN
                                     neighbor_average     4.467206       NaN   7.413335       NaN  0.138923       NaN
       swap_from_scenario_cvar       gls_map              2.706566       NaN   4.422813       NaN  0.069005       NaN
                                     gsp                  4.209425       NaN   6.588233       NaN  0.113930       NaN
                                     historical_tod_mean  5.878396       NaN   8.981296       NaN  0.151451       NaN
                                     neighbor_average     4.420823       NaN   7.314891       NaN  0.135830       NaN
       top_variance                  gls_map              2.890204       NaN   4.596591       NaN  0.064529       NaN
                                     gsp                  3.787235       NaN   5.758625       NaN  0.085926       NaN
                                     historical_tod_mean  5.043142       NaN   7.665135       NaN  0.112050       NaN
                                     neighbor_average     6.162254       NaN  10.539569       NaN  0.119737       NaN
       validation_swap_selected      gls_map              2.632172       NaN   4.310887       NaN  0.064697       NaN
                                     gsp                  3.994976       NaN   6.227379       NaN  0.104719       NaN
                                     historical_tod_mean  5.567007       NaN   8.630279       NaN  0.142799       NaN
                                     neighbor_average     4.776470       NaN   7.537573       NaN  0.117489       NaN
0.3    best_random_by_trace          gls_map              2.561686       NaN   4.239242       NaN  0.065261       NaN
                                     gsp                  4.054859       NaN   6.328230       NaN  0.108743       NaN
                                     historical_tod_mean  5.725789       NaN   8.827662       NaN  0.147325       NaN
                                     neighbor_average     4.242199       NaN   6.897628       NaN  0.117169       NaN
       best_random_by_validation     gls_map              2.508223       NaN   4.095146       NaN  0.060006       NaN
                                     gsp                  3.951151       NaN   6.090235       NaN  0.100973       NaN
                                     historical_tod_mean  5.501257       NaN   8.478910       NaN  0.137284       NaN
                                     neighbor_average     4.238522       NaN   6.895116       NaN  0.102823       NaN
       coverage                      gls_map              2.518630       NaN   4.203373       NaN  0.064041       NaN
                                     gsp                  4.082954       NaN   6.385975       NaN  0.109610       NaN
                                     historical_tod_mean  5.741296       NaN   8.871196       NaN  0.149105       NaN
                                     neighbor_average     4.114562       NaN   6.541677       NaN  0.111150       NaN
       degree                        gls_map              3.104813       NaN   5.132336       NaN  0.079194       NaN
                                     gsp                  4.191818       NaN   6.536439       NaN  0.109697       NaN
                                     historical_tod_mean  5.821188       NaN   8.913051       NaN  0.149637       NaN
                                     neighbor_average     6.385883       NaN  10.759258       NaN  0.166975       NaN
       graph_sampling_laplacian      gls_map              3.221859       NaN   5.377604       NaN  0.082157       NaN
                                     gsp                  4.232278       NaN   6.530991       NaN  0.110941       NaN
                                     historical_tod_mean  5.748053       NaN   8.872243       NaN  0.147382       NaN
                                     neighbor_average     5.794519       NaN   9.855357       NaN  0.171472       NaN
       greedy_a_trace                gls_map              2.553452       NaN   4.194655       NaN  0.065951       NaN
                                     gsp                  4.240924       NaN   6.606339       NaN  0.115368       NaN
                                     historical_tod_mean  5.972698       NaN   9.128899       NaN  0.154472       NaN
                                     neighbor_average     4.107138       NaN   6.734726       NaN  0.119840       NaN
       greedy_d_logdet               gls_map              2.825130       NaN   4.601376       NaN  0.075267       NaN
                                     gsp                  4.333083       NaN   6.718644       NaN  0.120182       NaN
                                     historical_tod_mean  6.126207       NaN   9.326180       NaN  0.161699       NaN
                                     neighbor_average     4.629802       NaN   7.994862       NaN  0.157792       NaN
       multistart_swap_by_validation gls_map              2.518504       NaN   4.126063       NaN  0.064116       NaN
                                     gsp                  4.147968       NaN   6.432343       NaN  0.112104       NaN
                                     historical_tod_mean  5.839972       NaN   8.951873       NaN  0.151290       NaN
                                     neighbor_average     3.943223       NaN   6.339428       NaN  0.109135       NaN
       observability_proxy           gls_map              3.120411       NaN   5.132458       NaN  0.078724       NaN
                                     gsp                  4.200366       NaN   6.549427       NaN  0.109242       NaN
                                     historical_tod_mean  5.819574       NaN   8.910053       NaN  0.149137       NaN
                                     neighbor_average     6.346117       NaN  10.721635       NaN  0.166452       NaN
       qr_pod_modes                  gls_map              2.549291       NaN   4.155097       NaN  0.063236       NaN
                                     gsp                  4.179259       NaN   6.481277       NaN  0.110842       NaN
                                     historical_tod_mean  5.931184       NaN   9.041984       NaN  0.150426       NaN
                                     neighbor_average     4.056870       NaN   6.530155       NaN  0.115192       NaN
       random                        gls_map              2.676199  0.061765   4.422079  0.125725  0.066885  0.002489
                                     gsp                  4.068088  0.043043   6.295002  0.078227  0.106711  0.002878
                                     historical_tod_mean  5.694719  0.075240   8.769420  0.108399  0.145851  0.003687
                                     neighbor_average     4.318226  0.094723   7.101843  0.206993  0.114218  0.006236
       rcss_selected                 gls_map              2.448456       NaN   4.029973       NaN  0.061788       NaN
                                     gsp                  3.994096       NaN   6.241246       NaN  0.105857       NaN
                                     historical_tod_mean  5.592549       NaN   8.681431       NaN  0.143915       NaN
                                     neighbor_average     4.083811       NaN   6.483627       NaN  0.103988       NaN
       robust_coverage_cvar          gls_map              2.611776       NaN   4.293276       NaN  0.066269       NaN
                                     gsp                  4.192601       NaN   6.535429       NaN  0.112326       NaN
                                     historical_tod_mean  5.934053       NaN   9.077924       NaN  0.152997       NaN
                                     neighbor_average     4.113221       NaN   6.792584       NaN  0.123170       NaN
       scenario_average_a_trace      gls_map              2.684497       NaN   4.385832       NaN  0.067900       NaN
                                     gsp                  4.216813       NaN   6.532662       NaN  0.113191       NaN
                                     historical_tod_mean  5.975880       NaN   9.137926       NaN  0.154775       NaN
                                     neighbor_average     4.327164       NaN   7.119250       NaN  0.131742       NaN
       scenario_cvar_a_trace         gls_map              2.797543       NaN   4.571565       NaN  0.070855       NaN
                                     gsp                  4.254136       NaN   6.571016       NaN  0.113837       NaN
                                     historical_tod_mean  5.998807       NaN   9.128049       NaN  0.155164       NaN
                                     neighbor_average     4.335795       NaN   7.063884       NaN  0.126059       NaN
       swap_from_best_random_trace   gls_map              2.526904       NaN   4.145692       NaN  0.064533       NaN
                                     gsp                  4.171230       NaN   6.481280       NaN  0.112314       NaN
                                     historical_tod_mean  5.887079       NaN   9.010881       NaN  0.151635       NaN
                                     neighbor_average     4.108199       NaN   6.684453       NaN  0.118045       NaN
       swap_from_greedy_a_trace      gls_map              2.530941       NaN   4.136825       NaN  0.063525       NaN
                                     gsp                  4.218447       NaN   6.548387       NaN  0.112016       NaN
                                     historical_tod_mean  5.977186       NaN   9.096250       NaN  0.151551       NaN
                                     neighbor_average     4.136829       NaN   6.682232       NaN  0.116393       NaN
       swap_from_scenario_average    gls_map              2.562621       NaN   4.203126       NaN  0.063831       NaN
                                     gsp                  4.181170       NaN   6.473718       NaN  0.110263       NaN
                                     historical_tod_mean  5.943329       NaN   9.046283       NaN  0.150995       NaN
                                     neighbor_average     4.186878       NaN   6.844519       NaN  0.123234       NaN
       swap_from_scenario_cvar       gls_map              2.560718       NaN   4.135606       NaN  0.065423       NaN
                                     gsp                  4.231001       NaN   6.556315       NaN  0.114217       NaN
                                     historical_tod_mean  6.002264       NaN   9.136869       NaN  0.155291       NaN
                                     neighbor_average     4.225629       NaN   6.977745       NaN  0.130935       NaN
       top_variance                  gls_map              2.647805       NaN   4.272616       NaN  0.058289       NaN
                                     gsp                  3.592962       NaN   5.434776       NaN  0.078454       NaN
                                     historical_tod_mean  4.828060       NaN   7.292165       NaN  0.102813       NaN
                                     neighbor_average     5.339156       NaN   9.008563       NaN  0.103672       NaN
       validation_swap_selected      gls_map              2.441900       NaN   4.014577       NaN  0.061565       NaN
                                     gsp                  3.983094       NaN   6.219404       NaN  0.105511       NaN
                                     historical_tod_mean  5.564824       NaN   8.656671       NaN  0.143201       NaN
                                     neighbor_average     4.124056       NaN   6.547947       NaN  0.104695       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 2.839402 4.661600
    0.2 validation_swap_selected gls_map 2.632172 4.310887
    0.3 validation_swap_selected gls_map 2.441900 4.014577
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.568435      0.531242 210
    gsp   condition_number     0.567061      0.520011 210
    gsp information_logdet    -0.528007     -0.570588 210
gls_map    posterior_trace     0.889390      0.886533 210
gls_map   condition_number     0.864153      0.891654 210
gls_map information_logdet    -0.806396     -0.826399 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv