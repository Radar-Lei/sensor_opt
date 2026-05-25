---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-01, 2015-01-28
Test days: 2015-01-19, 2015-01-20
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.325003       NaN   5.534439       NaN  0.094015       NaN
                                     gsp                  4.005878       NaN   6.556648       NaN  0.123277       NaN
                                     historical_tod_mean  4.245272       NaN   7.177789       NaN  0.137987       NaN
                                     neighbor_average     5.490270       NaN   8.725954       NaN  0.174456       NaN
       best_random_by_validation     gls_map              3.257361       NaN   5.431366       NaN  0.091261       NaN
                                     gsp                  3.922945       NaN   6.434336       NaN  0.119457       NaN
                                     historical_tod_mean  4.182196       NaN   7.056234       NaN  0.132587       NaN
                                     neighbor_average     5.674024       NaN   9.116957       NaN  0.163120       NaN
       coverage                      gls_map              3.314982       NaN   5.427672       NaN  0.096275       NaN
                                     gsp                  3.988940       NaN   6.585373       NaN  0.126051       NaN
                                     historical_tod_mean  4.243458       NaN   7.158118       NaN  0.137032       NaN
                                     neighbor_average     5.659067       NaN   8.868982       NaN  0.172436       NaN
       degree                        gls_map              3.604448       NaN   5.977903       NaN  0.105665       NaN
                                     gsp                  3.975438       NaN   6.457226       NaN  0.120693       NaN
                                     historical_tod_mean  4.206468       NaN   7.089575       NaN  0.135646       NaN
                                     neighbor_average     6.505741       NaN  10.273764       NaN  0.196060       NaN
       graph_sampling_laplacian      gls_map              3.989507       NaN   6.399671       NaN  0.105622       NaN
                                     gsp                  4.282697       NaN   6.823279       NaN  0.122314       NaN
                                     historical_tod_mean  4.256306       NaN   7.101402       NaN  0.133703       NaN
                                     neighbor_average     6.847712       NaN  11.134442       NaN  0.206096       NaN
       greedy_a_trace                gls_map              3.171847       NaN   5.123486       NaN  0.086270       NaN
                                     gsp                  3.986500       NaN   6.477217       NaN  0.121246       NaN
                                     historical_tod_mean  4.216857       NaN   7.086704       NaN  0.134598       NaN
                                     neighbor_average     5.253830       NaN   8.429867       NaN  0.160947       NaN
       greedy_d_logdet               gls_map              3.903780       NaN   6.396185       NaN  0.120666       NaN
                                     gsp                  4.205658       NaN   6.966448       NaN  0.136220       NaN
                                     historical_tod_mean  4.335671       NaN   7.281215       NaN  0.140732       NaN
                                     neighbor_average     6.247972       NaN  10.460714       NaN  0.220512       NaN
       multistart_swap_by_validation gls_map              3.170696       NaN   5.150672       NaN  0.087884       NaN
                                     gsp                  3.964560       NaN   6.459341       NaN  0.121914       NaN
                                     historical_tod_mean  4.201641       NaN   7.059309       NaN  0.133689       NaN
                                     neighbor_average     5.661636       NaN   8.928015       NaN  0.166113       NaN
       observability_proxy           gls_map              3.541426       NaN   5.940706       NaN  0.103172       NaN
                                     gsp                  3.985245       NaN   6.496610       NaN  0.121328       NaN
                                     historical_tod_mean  4.204102       NaN   7.080639       NaN  0.135593       NaN
                                     neighbor_average     6.495035       NaN  10.385501       NaN  0.194002       NaN
       qr_pod_modes                  gls_map              3.440250       NaN   5.508944       NaN  0.093576       NaN
                                     gsp                  4.039445       NaN   6.592952       NaN  0.124935       NaN
                                     historical_tod_mean  4.262772       NaN   7.126609       NaN  0.135434       NaN
                                     neighbor_average     5.838110       NaN   9.600501       NaN  0.190234       NaN
       random                        gls_map              3.364650  0.069823   5.513847  0.123795  0.094723  0.003290
                                     gsp                  3.987741  0.042984   6.507659  0.063405  0.122501  0.002487
                                     historical_tod_mean  4.212822  0.030803   7.101110  0.047493  0.134829  0.002117
                                     neighbor_average     5.806330  0.231859   9.319632  0.335409  0.171983  0.008139
       rcss_selected                 gls_map              3.170696       NaN   5.150672       NaN  0.087884       NaN
                                     gsp                  3.964560       NaN   6.459341       NaN  0.121914       NaN
                                     historical_tod_mean  4.201641       NaN   7.059309       NaN  0.133689       NaN
                                     neighbor_average     5.661636       NaN   8.928015       NaN  0.166113       NaN
       robust_coverage_cvar          gls_map              3.308903       NaN   5.490618       NaN  0.097366       NaN
                                     gsp                  4.021862       NaN   6.583971       NaN  0.125492       NaN
                                     historical_tod_mean  4.267009       NaN   7.160853       NaN  0.137075       NaN
                                     neighbor_average     5.455606       NaN   8.957098       NaN  0.178125       NaN
       scenario_average_a_trace      gls_map              3.342297       NaN   5.647193       NaN  0.103402       NaN
                                     gsp                  4.066791       NaN   6.730085       NaN  0.130834       NaN
                                     historical_tod_mean  4.282993       NaN   7.201433       NaN  0.138863       NaN
                                     neighbor_average     5.674210       NaN   9.312432       NaN  0.186141       NaN
       scenario_cvar_a_trace         gls_map              3.386384       NaN   5.500274       NaN  0.097429       NaN
                                     gsp                  4.034403       NaN   6.587088       NaN  0.126167       NaN
                                     historical_tod_mean  4.276756       NaN   7.168444       NaN  0.137843       NaN
                                     neighbor_average     5.521770       NaN   9.131553       NaN  0.184764       NaN
       swap_from_best_random_trace   gls_map              3.156097       NaN   5.190794       NaN  0.087732       NaN
                                     gsp                  3.986834       NaN   6.512195       NaN  0.123637       NaN
                                     historical_tod_mean  4.222864       NaN   7.099900       NaN  0.135697       NaN
                                     neighbor_average     5.711276       NaN   9.031509       NaN  0.171702       NaN
       swap_from_greedy_a_trace      gls_map              3.181546       NaN   5.235296       NaN  0.091137       NaN
                                     gsp                  3.990975       NaN   6.542504       NaN  0.124856       NaN
                                     historical_tod_mean  4.228906       NaN   7.112311       NaN  0.136038       NaN
                                     neighbor_average     5.794691       NaN   9.073576       NaN  0.179062       NaN
       swap_from_scenario_average    gls_map              3.179055       NaN   5.158887       NaN  0.090414       NaN
                                     gsp                  3.979368       NaN   6.515519       NaN  0.122971       NaN
                                     historical_tod_mean  4.205769       NaN   7.068157       NaN  0.133573       NaN
                                     neighbor_average     5.567508       NaN   8.864460       NaN  0.168447       NaN
       swap_from_scenario_cvar       gls_map              3.212543       NaN   5.273939       NaN  0.092096       NaN
                                     gsp                  4.004547       NaN   6.542251       NaN  0.124229       NaN
                                     historical_tod_mean  4.222076       NaN   7.078659       NaN  0.134708       NaN
                                     neighbor_average     5.598326       NaN   8.985817       NaN  0.174187       NaN
       top_variance                  gls_map              3.498919       NaN   5.661998       NaN  0.092520       NaN
                                     gsp                  3.821412       NaN   6.170658       NaN  0.106513       NaN
                                     historical_tod_mean  3.888643       NaN   6.621391       NaN  0.114200       NaN
                                     neighbor_average     8.926608       NaN  14.453160       NaN  0.187990       NaN
       validation_swap_selected      gls_map              3.151337       NaN   5.117463       NaN  0.087387       NaN
                                     gsp                  3.957452       NaN   6.462131       NaN  0.121973       NaN
                                     historical_tod_mean  4.197015       NaN   7.054406       NaN  0.133575       NaN
                                     neighbor_average     5.465486       NaN   8.672946       NaN  0.160316       NaN
0.2    best_random_by_trace          gls_map              3.066294       NaN   4.949650       NaN  0.084479       NaN
                                     gsp                  3.997544       NaN   6.491720       NaN  0.123678       NaN
                                     historical_tod_mean  4.240159       NaN   7.139594       NaN  0.136879       NaN
                                     neighbor_average     4.999970       NaN   8.098828       NaN  0.150611       NaN
       best_random_by_validation     gls_map              2.993951       NaN   5.013002       NaN  0.087358       NaN
                                     gsp                  3.920544       NaN   6.444377       NaN  0.122149       NaN
                                     historical_tod_mean  4.198920       NaN   7.106411       NaN  0.136573       NaN
                                     neighbor_average     5.003564       NaN   8.049368       NaN  0.154448       NaN
       coverage                      gls_map              2.960455       NaN   4.805383       NaN  0.081545       NaN
                                     gsp                  3.959371       NaN   6.435724       NaN  0.121990       NaN
                                     historical_tod_mean  4.237512       NaN   7.127061       NaN  0.135880       NaN
                                     neighbor_average     4.719305       NaN   7.427144       NaN  0.139259       NaN
       degree                        gls_map              3.560477       NaN   5.978005       NaN  0.105675       NaN
                                     gsp                  4.056860       NaN   6.583898       NaN  0.124062       NaN
                                     historical_tod_mean  4.260233       NaN   7.178566       NaN  0.140041       NaN
                                     neighbor_average     6.331114       NaN  10.255071       NaN  0.197578       NaN
       graph_sampling_laplacian      gls_map              3.826860       NaN   6.126499       NaN  0.098419       NaN
                                     gsp                  4.221243       NaN   6.535077       NaN  0.116001       NaN
                                     historical_tod_mean  4.257069       NaN   7.056928       NaN  0.131526       NaN
                                     neighbor_average     6.459731       NaN  10.635075       NaN  0.192737       NaN
       greedy_a_trace                gls_map              3.000302       NaN   4.892439       NaN  0.083705       NaN
                                     gsp                  4.063946       NaN   6.591836       NaN  0.127389       NaN
                                     historical_tod_mean  4.329590       NaN   7.250180       NaN  0.141100       NaN
                                     neighbor_average     4.852320       NaN   7.997925       NaN  0.158564       NaN
       greedy_d_logdet               gls_map              3.587997       NaN   5.709076       NaN  0.099126       NaN
                                     gsp                  4.240257       NaN   6.885194       NaN  0.133794       NaN
                                     historical_tod_mean  4.449925       NaN   7.416285       NaN  0.144347       NaN
                                     neighbor_average     5.852239       NaN   9.878655       NaN  0.207172       NaN
       multistart_swap_by_validation gls_map              2.970860       NaN   4.805930       NaN  0.082291       NaN
                                     gsp                  4.017962       NaN   6.514036       NaN  0.124127       NaN
                                     historical_tod_mean  4.282738       NaN   7.159355       NaN  0.136919       NaN
                                     neighbor_average     4.769659       NaN   7.592821       NaN  0.144070       NaN
       observability_proxy           gls_map              3.453844       NaN   5.849832       NaN  0.103621       NaN
                                     gsp                  4.040194       NaN   6.570421       NaN  0.123661       NaN
                                     historical_tod_mean  4.242730       NaN   7.156341       NaN  0.139308       NaN
                                     neighbor_average     6.293358       NaN  10.101576       NaN  0.193348       NaN
       qr_pod_modes                  gls_map              3.114974       NaN   5.001687       NaN  0.086100       NaN
                                     gsp                  4.081687       NaN   6.611530       NaN  0.127748       NaN
                                     historical_tod_mean  4.327968       NaN   7.238522       NaN  0.140039       NaN
                                     neighbor_average     5.110207       NaN   8.304398       NaN  0.167097       NaN
       random                        gls_map              3.078236  0.042924   5.066395  0.096005  0.085867  0.002780
                                     gsp                  3.960339  0.030898   6.423673  0.060040  0.120403  0.002754
                                     historical_tod_mean  4.210990  0.035095   7.099665  0.056310  0.134716  0.002689
                                     neighbor_average     5.175617  0.178952   8.343739  0.317754  0.148238  0.005863
       rcss_selected                 gls_map              2.861810       NaN   4.757795       NaN  0.082230       NaN
                                     gsp                  3.873467       NaN   6.372698       NaN  0.120273       NaN
                                     historical_tod_mean  4.147576       NaN   7.057228       NaN  0.135065       NaN
                                     neighbor_average     5.104373       NaN   7.967111       NaN  0.138112       NaN
       robust_coverage_cvar          gls_map              3.147042       NaN   5.239003       NaN  0.092905       NaN
                                     gsp                  4.125801       NaN   6.685059       NaN  0.130077       NaN
                                     historical_tod_mean  4.379533       NaN   7.314125       NaN  0.142958       NaN
                                     neighbor_average     5.090350       NaN   8.439886       NaN  0.168996       NaN
       scenario_average_a_trace      gls_map              3.227149       NaN   5.441095       NaN  0.100172       NaN
                                     gsp                  4.171004       NaN   6.846895       NaN  0.135559       NaN
                                     historical_tod_mean  4.392779       NaN   7.381903       NaN  0.145443       NaN
                                     neighbor_average     5.274825       NaN   8.734323       NaN  0.177292       NaN
       scenario_cvar_a_trace         gls_map              3.245121       NaN   5.326588       NaN  0.092572       NaN
                                     gsp                  4.135336       NaN   6.698084       NaN  0.130194       NaN
                                     historical_tod_mean  4.388848       NaN   7.327099       NaN  0.143227       NaN
                                     neighbor_average     5.241200       NaN   8.667688       NaN  0.175509       NaN
       swap_from_best_random_trace   gls_map              3.047579       NaN   4.893782       NaN  0.082395       NaN
                                     gsp                  4.069161       NaN   6.584348       NaN  0.126211       NaN
                                     historical_tod_mean  4.314414       NaN   7.213980       NaN  0.139241       NaN
                                     neighbor_average     4.978741       NaN   8.047655       NaN  0.157111       NaN
       swap_from_greedy_a_trace      gls_map              3.004498       NaN   4.849296       NaN  0.081840       NaN
                                     gsp                  4.065938       NaN   6.568320       NaN  0.125970       NaN
                                     historical_tod_mean  4.330292       NaN   7.229806       NaN  0.139638       NaN
                                     neighbor_average     4.857886       NaN   7.893354       NaN  0.154134       NaN
       swap_from_scenario_average    gls_map              3.054910       NaN   4.935198       NaN  0.085508       NaN
                                     gsp                  4.060172       NaN   6.611541       NaN  0.127002       NaN
                                     historical_tod_mean  4.324446       NaN   7.235988       NaN  0.139429       NaN
                                     neighbor_average     5.045569       NaN   8.151048       NaN  0.159081       NaN
       swap_from_scenario_cvar       gls_map              3.027429       NaN   4.853476       NaN  0.084138       NaN
                                     gsp                  4.048487       NaN   6.565788       NaN  0.126002       NaN
                                     historical_tod_mean  4.313372       NaN   7.220944       NaN  0.139352       NaN
                                     neighbor_average     4.985363       NaN   8.164286       NaN  0.158662       NaN
       top_variance                  gls_map              3.142195       NaN   5.087232       NaN  0.078008       NaN
                                     gsp                  3.593914       NaN   5.780207       NaN  0.094046       NaN
                                     historical_tod_mean  3.646667       NaN   6.207561       NaN  0.100353       NaN
                                     neighbor_average     6.982759       NaN  11.456073       NaN  0.143218       NaN
       validation_swap_selected      gls_map              2.898240       NaN   4.696585       NaN  0.078861       NaN
                                     gsp                  3.942970       NaN   6.404714       NaN  0.120639       NaN
                                     historical_tod_mean  4.210890       NaN   7.070022       NaN  0.134273       NaN
                                     neighbor_average     4.764103       NaN   7.524259       NaN  0.139750       NaN
0.3    best_random_by_trace          gls_map              2.969830       NaN   4.900390       NaN  0.085451       NaN
                                     gsp                  4.044748       NaN   6.549238       NaN  0.126284       NaN
                                     historical_tod_mean  4.316362       NaN   7.271705       NaN  0.142259       NaN
                                     neighbor_average     4.808158       NaN   7.612528       NaN  0.137745       NaN
       best_random_by_validation     gls_map              2.833770       NaN   4.694282       NaN  0.080176       NaN
                                     gsp                  3.943811       NaN   6.408044       NaN  0.121637       NaN
                                     historical_tod_mean  4.214611       NaN   7.139433       NaN  0.137471       NaN
                                     neighbor_average     4.630162       NaN   7.373364       NaN  0.131188       NaN
       coverage                      gls_map              2.766788       NaN   4.451420       NaN  0.073901       NaN
                                     gsp                  3.975130       NaN   6.418738       NaN  0.120599       NaN
                                     historical_tod_mean  4.239330       NaN   7.131837       NaN  0.135205       NaN
                                     neighbor_average     4.522020       NaN   6.987141       NaN  0.124310       NaN
       degree                        gls_map              3.471425       NaN   5.852638       NaN  0.104926       NaN
                                     gsp                  4.076894       NaN   6.669673       NaN  0.127614       NaN
                                     historical_tod_mean  4.274118       NaN   7.192148       NaN  0.141470       NaN
                                     neighbor_average     6.906656       NaN  11.211855       NaN  0.200034       NaN
       graph_sampling_laplacian      gls_map              3.618108       NaN   5.735052       NaN  0.094958       NaN
                                     gsp                  4.151943       NaN   6.399437       NaN  0.113211       NaN
                                     historical_tod_mean  4.209265       NaN   6.968496       NaN  0.127243       NaN
                                     neighbor_average     6.594827       NaN  10.537025       NaN  0.195332       NaN
       greedy_a_trace                gls_map              2.883590       NaN   4.733681       NaN  0.082105       NaN
                                     gsp                  4.152294       NaN   6.703335       NaN  0.131638       NaN
                                     historical_tod_mean  4.421079       NaN   7.382519       NaN  0.145922       NaN
                                     neighbor_average     4.671561       NaN   7.635589       NaN  0.151169       NaN
       greedy_d_logdet               gls_map              3.321906       NaN   5.321173       NaN  0.091650       NaN
                                     gsp                  4.265924       NaN   6.898425       NaN  0.134635       NaN
                                     historical_tod_mean  4.519664       NaN   7.521601       NaN  0.147934       NaN
                                     neighbor_average     5.364781       NaN   8.823759       NaN  0.183164       NaN
       multistart_swap_by_validation gls_map              2.785437       NaN   4.488025       NaN  0.073585       NaN
                                     gsp                  4.015317       NaN   6.448745       NaN  0.119922       NaN
                                     historical_tod_mean  4.268970       NaN   7.176818       NaN  0.135073       NaN
                                     neighbor_average     4.695017       NaN   7.283188       NaN  0.124742       NaN
       observability_proxy           gls_map              3.453780       NaN   5.827766       NaN  0.104230       NaN
                                     gsp                  4.072610       NaN   6.663039       NaN  0.127187       NaN
                                     historical_tod_mean  4.262069       NaN   7.182397       NaN  0.140927       NaN
                                     neighbor_average     6.851946       NaN  11.144898       NaN  0.199128       NaN
       qr_pod_modes                  gls_map              2.916103       NaN   4.668838       NaN  0.078777       NaN
                                     gsp                  4.090754       NaN   6.621973       NaN  0.126091       NaN
                                     historical_tod_mean  4.360087       NaN   7.294351       NaN  0.139600       NaN
                                     neighbor_average     4.661605       NaN   7.338313       NaN  0.142086       NaN
       random                        gls_map              2.907579  0.057042   4.765708  0.116121  0.079412  0.003286
                                     gsp                  3.953833  0.054560   6.372750  0.101941  0.118745  0.004042
                                     historical_tod_mean  4.205749  0.059613   7.083980  0.102190  0.134024  0.004271
                                     neighbor_average     4.862656  0.155492   7.775760  0.295173  0.133576  0.006425
       rcss_selected                 gls_map              2.860142       NaN   4.596222       NaN  0.080061       NaN
                                     gsp                  4.101849       NaN   6.645788       NaN  0.128993       NaN
                                     historical_tod_mean  4.379374       NaN   7.324129       NaN  0.142345       NaN
                                     neighbor_average     4.655876       NaN   7.411821       NaN  0.139536       NaN
       robust_coverage_cvar          gls_map              2.995153       NaN   4.901636       NaN  0.085845       NaN
                                     gsp                  4.159853       NaN   6.709635       NaN  0.131385       NaN
                                     historical_tod_mean  4.438388       NaN   7.403662       NaN  0.145645       NaN
                                     neighbor_average     4.822173       NaN   7.789127       NaN  0.155312       NaN
       scenario_average_a_trace      gls_map              3.081334       NaN   5.180356       NaN  0.093714       NaN
                                     gsp                  4.204156       NaN   6.887385       NaN  0.136754       NaN
                                     historical_tod_mean  4.479577       NaN   7.514819       NaN  0.149709       NaN
                                     neighbor_average     5.078195       NaN   8.414087       NaN  0.174591       NaN
       scenario_cvar_a_trace         gls_map              3.098436       NaN   5.082944       NaN  0.090650       NaN
                                     gsp                  4.210091       NaN   6.797422       NaN  0.134779       NaN
                                     historical_tod_mean  4.483853       NaN   7.487549       NaN  0.149501       NaN
                                     neighbor_average     4.969152       NaN   8.036053       NaN  0.163810       NaN
       swap_from_best_random_trace   gls_map              2.903665       NaN   4.709421       NaN  0.081551       NaN
                                     gsp                  4.116012       NaN   6.630257       NaN  0.128690       NaN
                                     historical_tod_mean  4.401031       NaN   7.359396       NaN  0.144454       NaN
                                     neighbor_average     4.681257       NaN   7.435893       NaN  0.146500       NaN
       swap_from_greedy_a_trace      gls_map              2.860594       NaN   4.623661       NaN  0.077857       NaN
                                     gsp                  4.108872       NaN   6.635185       NaN  0.127182       NaN
                                     historical_tod_mean  4.382176       NaN   7.315813       NaN  0.140580       NaN
                                     neighbor_average     4.610289       NaN   7.377321       NaN  0.140132       NaN
       swap_from_scenario_average    gls_map              2.860142       NaN   4.596222       NaN  0.080061       NaN
                                     gsp                  4.101849       NaN   6.645788       NaN  0.128993       NaN
                                     historical_tod_mean  4.379374       NaN   7.324129       NaN  0.142345       NaN
                                     neighbor_average     4.655876       NaN   7.411821       NaN  0.139536       NaN
       swap_from_scenario_cvar       gls_map              2.915491       NaN   4.720900       NaN  0.084069       NaN
                                     gsp                  4.147633       NaN   6.727656       NaN  0.132820       NaN
                                     historical_tod_mean  4.433428       NaN   7.416291       NaN  0.147000       NaN
                                     neighbor_average     4.714781       NaN   7.632188       NaN  0.154362       NaN
       top_variance                  gls_map              2.826014       NaN   4.581077       NaN  0.069560       NaN
                                     gsp                  3.369656       NaN   5.391569       NaN  0.084926       NaN
                                     historical_tod_mean  3.435077       NaN   5.815399       NaN  0.090176       NaN
                                     neighbor_average     6.131091       NaN  10.169472       NaN  0.125955       NaN
       validation_swap_selected      gls_map              2.691428       NaN   4.436620       NaN  0.072553       NaN
                                     gsp                  3.819623       NaN   6.180170       NaN  0.114485       NaN
                                     historical_tod_mean  4.080299       NaN   6.904141       NaN  0.128631       NaN
                                     neighbor_average     4.670591       NaN   7.409804       NaN  0.122174       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 3.151337 5.117463
    0.2            rcss_selected gls_map 2.861810 4.757795
    0.3 validation_swap_selected gls_map 2.691428 4.436620
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.054115      0.090802 210
    gsp   condition_number     0.053334      0.025745 210
    gsp information_logdet    -0.022631     -0.097724 210
gls_map    posterior_trace     0.853605      0.859750 210
gls_map   condition_number     0.871219      0.871663 210
gls_map information_logdet    -0.757522     -0.804007 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv