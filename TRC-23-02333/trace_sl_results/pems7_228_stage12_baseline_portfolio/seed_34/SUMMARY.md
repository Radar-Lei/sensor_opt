---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-14, 2012-06-15
Test days: 2012-05-11, 2012-06-22
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.904622       NaN   6.398527       NaN  0.098430       NaN
                                     gsp                   4.363070       NaN   7.395809       NaN  0.114549       NaN
                                     historical_tod_mean   4.369569       NaN   7.890686       NaN  0.121876       NaN
                                     neighbor_average      7.781812       NaN  11.320019       NaN  0.202438       NaN
       best_random_by_validation     gls_map               3.958526       NaN   6.545437       NaN  0.102547       NaN
                                     gsp                   4.335244       NaN   7.337167       NaN  0.116016       NaN
                                     historical_tod_mean   4.378532       NaN   7.900616       NaN  0.123758       NaN
                                     neighbor_average      8.191093       NaN  12.256462       NaN  0.208202       NaN
       coverage                      gls_map               4.139036       NaN   6.889275       NaN  0.105613       NaN
                                     gsp                   4.426873       NaN   7.550922       NaN  0.116065       NaN
                                     historical_tod_mean   4.459556       NaN   8.031694       NaN  0.125559       NaN
                                     neighbor_average      8.271149       NaN  12.493399       NaN  0.230243       NaN
       degree                        gls_map               4.367179       NaN   7.421771       NaN  0.119842       NaN
                                     gsp                   4.495247       NaN   7.639417       NaN  0.122767       NaN
                                     historical_tod_mean   4.501077       NaN   8.084693       NaN  0.128595       NaN
                                     neighbor_average      8.436572       NaN  12.906061       NaN  0.249915       NaN
       graph_sampling_laplacian      gls_map               4.384174       NaN   7.506400       NaN  0.110339       NaN
                                     gsp                   4.415497       NaN   7.654372       NaN  0.112616       NaN
                                     historical_tod_mean   4.440919       NaN   8.009125       NaN  0.121365       NaN
                                     neighbor_average      9.816469       NaN  15.337995       NaN  0.238537       NaN
       greedy_a_trace                gls_map               3.836454       NaN   6.386058       NaN  0.098268       NaN
                                     gsp                   4.421383       NaN   7.428419       NaN  0.116609       NaN
                                     historical_tod_mean   4.444470       NaN   7.950179       NaN  0.124129       NaN
                                     neighbor_average      7.729881       NaN  11.893834       NaN  0.224288       NaN
       greedy_d_logdet               gls_map               4.884751       NaN   7.752590       NaN  0.131087       NaN
                                     gsp                   4.434679       NaN   7.586615       NaN  0.119161       NaN
                                     historical_tod_mean   4.493502       NaN   8.047644       NaN  0.127280       NaN
                                     neighbor_average      8.384683       NaN  13.408773       NaN  0.270078       NaN
       multistart_swap_by_validation gls_map               3.763327       NaN   6.326003       NaN  0.097644       NaN
                                     gsp                   4.434533       NaN   7.439064       NaN  0.117761       NaN
                                     historical_tod_mean   4.435967       NaN   7.957452       NaN  0.124443       NaN
                                     neighbor_average      7.739304       NaN  11.980925       NaN  0.223643       NaN
       observability_proxy           gls_map               4.319183       NaN   7.309006       NaN  0.120091       NaN
                                     gsp                   4.469339       NaN   7.558547       NaN  0.122564       NaN
                                     historical_tod_mean   4.462381       NaN   8.010016       NaN  0.126823       NaN
                                     neighbor_average      8.362305       NaN  13.034448       NaN  0.247280       NaN
       qr_pod_modes                  gls_map               4.278776       NaN   7.080106       NaN  0.114552       NaN
                                     gsp                   4.448354       NaN   7.561239       NaN  0.119350       NaN
                                     historical_tod_mean   4.518533       NaN   8.080151       NaN  0.128513       NaN
                                     neighbor_average      7.798391       NaN  12.721111       NaN  0.257570       NaN
       random                        gls_map               4.100638  0.114316   6.875881  0.175202  0.107277  0.003352
                                     gsp                   4.410683  0.044883   7.474239  0.088061  0.116967  0.002825
                                     historical_tod_mean   4.444215  0.046302   7.994606  0.071567  0.125446  0.001947
                                     neighbor_average      7.930747  0.256742  12.122810  0.423185  0.220064  0.013872
       rcss_selected                 gls_map               3.763327       NaN   6.326003       NaN  0.097644       NaN
                                     gsp                   4.434533       NaN   7.439064       NaN  0.117761       NaN
                                     historical_tod_mean   4.435967       NaN   7.957452       NaN  0.124443       NaN
                                     neighbor_average      7.739304       NaN  11.980925       NaN  0.223643       NaN
       robust_coverage_cvar          gls_map               3.939402       NaN   6.429260       NaN  0.101011       NaN
                                     gsp                   4.416857       NaN   7.373954       NaN  0.116159       NaN
                                     historical_tod_mean   4.421049       NaN   7.933533       NaN  0.123890       NaN
                                     neighbor_average      7.770949       NaN  11.816690       NaN  0.219294       NaN
       scenario_average_a_trace      gls_map               4.080037       NaN   6.627563       NaN  0.100867       NaN
                                     gsp                   4.481349       NaN   7.413273       NaN  0.114703       NaN
                                     historical_tod_mean   4.473142       NaN   8.021076       NaN  0.125319       NaN
                                     neighbor_average      8.027631       NaN  11.934677       NaN  0.225723       NaN
       scenario_cvar_a_trace         gls_map               4.142632       NaN   6.762971       NaN  0.107253       NaN
                                     gsp                   4.464213       NaN   7.473562       NaN  0.117962       NaN
                                     historical_tod_mean   4.455338       NaN   7.975172       NaN  0.124853       NaN
                                     neighbor_average      7.708102       NaN  11.689788       NaN  0.213501       NaN
       swap_from_best_random_trace   gls_map               3.774861       NaN   6.303449       NaN  0.097591       NaN
                                     gsp                   4.423582       NaN   7.431110       NaN  0.117894       NaN
                                     historical_tod_mean   4.436938       NaN   7.953875       NaN  0.124617       NaN
                                     neighbor_average      7.725222       NaN  11.971592       NaN  0.224527       NaN
       swap_from_greedy_a_trace      gls_map               3.866207       NaN   6.485333       NaN  0.101773       NaN
                                     gsp                   4.439103       NaN   7.501440       NaN  0.118133       NaN
                                     historical_tod_mean   4.480339       NaN   8.035136       NaN  0.126458       NaN
                                     neighbor_average      7.674284       NaN  11.814846       NaN  0.226660       NaN
       swap_from_scenario_average    gls_map               3.765114       NaN   6.281709       NaN  0.096592       NaN
                                     gsp                   4.424508       NaN   7.421425       NaN  0.117684       NaN
                                     historical_tod_mean   4.443397       NaN   7.955360       NaN  0.124804       NaN
                                     neighbor_average      7.703032       NaN  11.947374       NaN  0.225399       NaN
       swap_from_scenario_cvar       gls_map               3.759644       NaN   6.270618       NaN  0.096066       NaN
                                     gsp                   4.414073       NaN   7.399648       NaN  0.116519       NaN
                                     historical_tod_mean   4.437340       NaN   7.929555       NaN  0.123687       NaN
                                     neighbor_average      7.751492       NaN  11.963514       NaN  0.223407       NaN
       top_variance                  gls_map               4.109238       NaN   6.925489       NaN  0.100037       NaN
                                     gsp                   4.288177       NaN   7.266347       NaN  0.105704       NaN
                                     historical_tod_mean   4.229912       NaN   7.663896       NaN  0.111008       NaN
                                     neighbor_average     11.863770       NaN  17.855276       NaN  0.227145       NaN
       validation_swap_selected      gls_map               3.805956       NaN   6.343042       NaN  0.097748       NaN
                                     gsp                   4.442606       NaN   7.403520       NaN  0.117206       NaN
                                     historical_tod_mean   4.405735       NaN   7.919698       NaN  0.123529       NaN
                                     neighbor_average      7.701365       NaN  11.976253       NaN  0.221166       NaN
0.2    best_random_by_trace          gls_map               3.740358       NaN   6.188387       NaN  0.098012       NaN
                                     gsp                   4.403046       NaN   7.351778       NaN  0.117353       NaN
                                     historical_tod_mean   4.426129       NaN   7.956696       NaN  0.124735       NaN
                                     neighbor_average      7.367741       NaN  11.266509       NaN  0.206515       NaN
       best_random_by_validation     gls_map               3.643131       NaN   6.247645       NaN  0.091408       NaN
                                     gsp                   4.321870       NaN   7.262511       NaN  0.109082       NaN
                                     historical_tod_mean   4.388296       NaN   7.886049       NaN  0.120704       NaN
                                     neighbor_average      7.828850       NaN  11.666483       NaN  0.194534       NaN
       coverage                      gls_map               3.835239       NaN   6.450122       NaN  0.099377       NaN
                                     gsp                   4.462614       NaN   7.521230       NaN  0.117046       NaN
                                     historical_tod_mean   4.498146       NaN   8.131367       NaN  0.127871       NaN
                                     neighbor_average      7.583048       NaN  11.518409       NaN  0.209285       NaN
       degree                        gls_map               4.391696       NaN   7.429070       NaN  0.120811       NaN
                                     gsp                   4.599026       NaN   7.742809       NaN  0.125112       NaN
                                     historical_tod_mean   4.607556       NaN   8.198498       NaN  0.130446       NaN
                                     neighbor_average      8.106085       NaN  12.579955       NaN  0.225050       NaN
       graph_sampling_laplacian      gls_map               4.243945       NaN   7.142470       NaN  0.104922       NaN
                                     gsp                   4.348392       NaN   7.422410       NaN  0.109704       NaN
                                     historical_tod_mean   4.361063       NaN   7.912001       NaN  0.117935       NaN
                                     neighbor_average      8.018379       NaN  11.880043       NaN  0.219143       NaN
       greedy_a_trace                gls_map               3.666750       NaN   6.144277       NaN  0.096300       NaN
                                     gsp                   4.467578       NaN   7.460022       NaN  0.119812       NaN
                                     historical_tod_mean   4.518277       NaN   8.057463       NaN  0.129405       NaN
                                     neighbor_average      7.552382       NaN  11.900468       NaN  0.236411       NaN
       greedy_d_logdet               gls_map               4.513132       NaN   7.151983       NaN  0.120672       NaN
                                     gsp                   4.502318       NaN   7.655318       NaN  0.121810       NaN
                                     historical_tod_mean   4.585497       NaN   8.199319       NaN  0.131715       NaN
                                     neighbor_average      8.265926       NaN  13.126531       NaN  0.269924       NaN
       multistart_swap_by_validation gls_map               3.565237       NaN   5.981291       NaN  0.092222       NaN
                                     gsp                   4.372183       NaN   7.376604       NaN  0.115740       NaN
                                     historical_tod_mean   4.454756       NaN   7.985529       NaN  0.125841       NaN
                                     neighbor_average      7.305619       NaN  11.335062       NaN  0.217630       NaN
       observability_proxy           gls_map               4.152464       NaN   6.853679       NaN  0.111020       NaN
                                     gsp                   4.499860       NaN   7.537996       NaN  0.121274       NaN
                                     historical_tod_mean   4.547934       NaN   8.138339       NaN  0.130734       NaN
                                     neighbor_average      9.060403       NaN  13.365212       NaN  0.254870       NaN
       qr_pod_modes                  gls_map               4.227323       NaN   6.631544       NaN  0.110280       NaN
                                     gsp                   4.452764       NaN   7.480620       NaN  0.119537       NaN
                                     historical_tod_mean   4.495084       NaN   8.059242       NaN  0.129187       NaN
                                     neighbor_average      7.763481       NaN  12.337277       NaN  0.250690       NaN
       random                        gls_map               3.785702  0.072522   6.385573  0.163051  0.098087  0.003796
                                     gsp                   4.404328  0.047325   7.374984  0.102561  0.115111  0.003201
                                     historical_tod_mean   4.430454  0.063197   7.980884  0.104902  0.124845  0.003255
                                     neighbor_average      7.638174  0.195018  11.724818  0.305903  0.206309  0.010516
       rcss_selected                 gls_map               3.565237       NaN   5.981291       NaN  0.092222       NaN
                                     gsp                   4.372183       NaN   7.376604       NaN  0.115740       NaN
                                     historical_tod_mean   4.454756       NaN   7.985529       NaN  0.125841       NaN
                                     neighbor_average      7.305619       NaN  11.335062       NaN  0.217630       NaN
       robust_coverage_cvar          gls_map               3.670499       NaN   6.052271       NaN  0.093352       NaN
                                     gsp                   4.439721       NaN   7.361283       NaN  0.115432       NaN
                                     historical_tod_mean   4.477413       NaN   8.007368       NaN  0.126176       NaN
                                     neighbor_average      7.415644       NaN  11.435936       NaN  0.207954       NaN
       scenario_average_a_trace      gls_map               3.796581       NaN   6.278642       NaN  0.095810       NaN
                                     gsp                   4.551539       NaN   7.489562       NaN  0.118216       NaN
                                     historical_tod_mean   4.544088       NaN   8.118118       NaN  0.128827       NaN
                                     neighbor_average      7.765308       NaN  11.943429       NaN  0.236417       NaN
       scenario_cvar_a_trace         gls_map               3.887238       NaN   6.295432       NaN  0.098323       NaN
                                     gsp                   4.501967       NaN   7.378192       NaN  0.117571       NaN
                                     historical_tod_mean   4.479036       NaN   7.988389       NaN  0.126581       NaN
                                     neighbor_average      7.788100       NaN  11.897221       NaN  0.225015       NaN
       swap_from_best_random_trace   gls_map               3.704937       NaN   6.061222       NaN  0.095556       NaN
                                     gsp                   4.469366       NaN   7.426825       NaN  0.119483       NaN
                                     historical_tod_mean   4.510337       NaN   8.050397       NaN  0.128849       NaN
                                     neighbor_average      7.531950       NaN  11.738305       NaN  0.233607       NaN
       swap_from_greedy_a_trace      gls_map               3.684787       NaN   6.112020       NaN  0.096559       NaN
                                     gsp                   4.457271       NaN   7.441446       NaN  0.119423       NaN
                                     historical_tod_mean   4.516348       NaN   8.054299       NaN  0.128923       NaN
                                     neighbor_average      7.650618       NaN  11.976731       NaN  0.239219       NaN
       swap_from_scenario_average    gls_map               3.705181       NaN   6.015092       NaN  0.095271       NaN
                                     gsp                   4.447000       NaN   7.380173       NaN  0.118447       NaN
                                     historical_tod_mean   4.510272       NaN   7.997761       NaN  0.128105       NaN
                                     neighbor_average      7.582526       NaN  11.932021       NaN  0.238184       NaN
       swap_from_scenario_cvar       gls_map               3.662652       NaN   6.039426       NaN  0.095217       NaN
                                     gsp                   4.408888       NaN   7.368835       NaN  0.117626       NaN
                                     historical_tod_mean   4.476126       NaN   7.961276       NaN  0.126411       NaN
                                     neighbor_average      7.444423       NaN  11.627870       NaN  0.223318       NaN
       top_variance                  gls_map               3.642536       NaN   6.027712       NaN  0.085470       NaN
                                     gsp                   4.096327       NaN   6.684722       NaN  0.094671       NaN
                                     historical_tod_mean   3.921821       NaN   7.105839       NaN  0.097613       NaN
                                     neighbor_average      9.832148       NaN  15.009468       NaN  0.185361       NaN
       validation_swap_selected      gls_map               3.545567       NaN   5.961101       NaN  0.091413       NaN
                                     gsp                   4.333858       NaN   7.307972       NaN  0.114259       NaN
                                     historical_tod_mean   4.410083       NaN   7.931697       NaN  0.124344       NaN
                                     neighbor_average      7.352337       NaN  11.303847       NaN  0.216502       NaN
0.3    best_random_by_trace          gls_map               3.632804       NaN   6.429587       NaN  0.099376       NaN
                                     gsp                   4.435052       NaN   7.597631       NaN  0.118026       NaN
                                     historical_tod_mean   4.534187       NaN   8.260843       NaN  0.129854       NaN
                                     neighbor_average      7.327397       NaN  11.513888       NaN  0.201068       NaN
       best_random_by_validation     gls_map               3.481070       NaN   5.913765       NaN  0.087637       NaN
                                     gsp                   4.320230       NaN   7.207576       NaN  0.111119       NaN
                                     historical_tod_mean   4.304286       NaN   7.837597       NaN  0.119984       NaN
                                     neighbor_average      7.521620       NaN  11.637652       NaN  0.183843       NaN
       coverage                      gls_map               3.514130       NaN   5.905765       NaN  0.091830       NaN
                                     gsp                   4.411074       NaN   7.413698       NaN  0.116447       NaN
                                     historical_tod_mean   4.409097       NaN   8.059665       NaN  0.126869       NaN
                                     neighbor_average      7.404205       NaN  11.110769       NaN  0.204092       NaN
       degree                        gls_map               4.216735       NaN   6.906863       NaN  0.112128       NaN
                                     gsp                   4.548252       NaN   7.515073       NaN  0.121698       NaN
                                     historical_tod_mean   4.549146       NaN   8.099953       NaN  0.129231       NaN
                                     neighbor_average      9.089295       NaN  13.913614       NaN  0.265065       NaN
       graph_sampling_laplacian      gls_map               4.091514       NaN   6.815159       NaN  0.099708       NaN
                                     gsp                   4.366233       NaN   7.395276       NaN  0.108188       NaN
                                     historical_tod_mean   4.400682       NaN   7.960720       NaN  0.117453       NaN
                                     neighbor_average      7.795805       NaN  12.391503       NaN  0.202260       NaN
       greedy_a_trace                gls_map               3.530700       NaN   5.964606       NaN  0.094897       NaN
                                     gsp                   4.477523       NaN   7.513500       NaN  0.120601       NaN
                                     historical_tod_mean   4.550228       NaN   8.165045       NaN  0.132369       NaN
                                     neighbor_average      7.244478       NaN  11.348331       NaN  0.230294       NaN
       greedy_d_logdet               gls_map               4.155091       NaN   6.764454       NaN  0.117404       NaN
                                     gsp                   4.497369       NaN   7.622384       NaN  0.123810       NaN
                                     historical_tod_mean   4.565115       NaN   8.264027       NaN  0.134490       NaN
                                     neighbor_average      8.074919       NaN  12.770504       NaN  0.266622       NaN
       multistart_swap_by_validation gls_map               3.319592       NaN   5.647367       NaN  0.088988       NaN
                                     gsp                   4.327466       NaN   7.284353       NaN  0.116887       NaN
                                     historical_tod_mean   4.365588       NaN   7.888544       NaN  0.126329       NaN
                                     neighbor_average      7.085680       NaN  10.949238       NaN  0.213002       NaN
       observability_proxy           gls_map               4.113013       NaN   6.812141       NaN  0.110177       NaN
                                     gsp                   4.530435       NaN   7.554991       NaN  0.122365       NaN
                                     historical_tod_mean   4.576342       NaN   8.169280       NaN  0.130932       NaN
                                     neighbor_average      8.987171       NaN  13.052183       NaN  0.242957       NaN
       qr_pod_modes                  gls_map               3.782043       NaN   6.084782       NaN  0.102267       NaN
                                     gsp                   4.458026       NaN   7.503399       NaN  0.121254       NaN
                                     historical_tod_mean   4.524390       NaN   8.138012       NaN  0.131819       NaN
                                     neighbor_average      7.384425       NaN  11.453928       NaN  0.234775       NaN
       random                        gls_map               3.622792  0.110314   6.131329  0.207776  0.093416  0.004086
                                     gsp                   4.428894  0.070033   7.389275  0.128233  0.115333  0.003113
                                     historical_tod_mean   4.461458  0.078610   8.025015  0.127808  0.125530  0.003300
                                     neighbor_average      7.419532  0.188300  11.499474  0.365761  0.199797  0.009488
       rcss_selected                 gls_map               3.319592       NaN   5.647367       NaN  0.088988       NaN
                                     gsp                   4.327466       NaN   7.284353       NaN  0.116887       NaN
                                     historical_tod_mean   4.365588       NaN   7.888544       NaN  0.126329       NaN
                                     neighbor_average      7.085680       NaN  10.949238       NaN  0.213002       NaN
       robust_coverage_cvar          gls_map               3.537249       NaN   5.941302       NaN  0.092435       NaN
                                     gsp                   4.498840       NaN   7.465325       NaN  0.119342       NaN
                                     historical_tod_mean   4.518246       NaN   8.092045       NaN  0.129941       NaN
                                     neighbor_average      7.178889       NaN  10.983339       NaN  0.201298       NaN
       scenario_average_a_trace      gls_map               3.647538       NaN   6.067357       NaN  0.093269       NaN
                                     gsp                   4.558037       NaN   7.525472       NaN  0.119595       NaN
                                     historical_tod_mean   4.560118       NaN   8.184808       NaN  0.130902       NaN
                                     neighbor_average      7.558168       NaN  11.593116       NaN  0.228810       NaN
       scenario_cvar_a_trace         gls_map               3.627117       NaN   5.958059       NaN  0.090785       NaN
                                     gsp                   4.487447       NaN   7.287203       NaN  0.114495       NaN
                                     historical_tod_mean   4.382708       NaN   7.891416       NaN  0.122616       NaN
                                     neighbor_average      7.441860       NaN  11.445628       NaN  0.200015       NaN
       swap_from_best_random_trace   gls_map               3.537699       NaN   5.991690       NaN  0.094130       NaN
                                     gsp                   4.469196       NaN   7.499924       NaN  0.119797       NaN
                                     historical_tod_mean   4.554462       NaN   8.168031       NaN  0.131975       NaN
                                     neighbor_average      7.310890       NaN  11.700738       NaN  0.233478       NaN
       swap_from_greedy_a_trace      gls_map               3.512134       NaN   5.811513       NaN  0.093481       NaN
                                     gsp                   4.435337       NaN   7.422308       NaN  0.118444       NaN
                                     historical_tod_mean   4.514924       NaN   8.073252       NaN  0.129953       NaN
                                     neighbor_average      7.126560       NaN  11.083040       NaN  0.219856       NaN
       swap_from_scenario_average    gls_map               3.475890       NaN   5.686280       NaN  0.091010       NaN
                                     gsp                   4.447905       NaN   7.428130       NaN  0.118733       NaN
                                     historical_tod_mean   4.530753       NaN   8.087510       NaN  0.130157       NaN
                                     neighbor_average      7.195206       NaN  11.280662       NaN  0.224137       NaN
       swap_from_scenario_cvar       gls_map               3.474003       NaN   5.757903       NaN  0.089877       NaN
                                     gsp                   4.400279       NaN   7.374270       NaN  0.115707       NaN
                                     historical_tod_mean   4.447055       NaN   8.018847       NaN  0.125114       NaN
                                     neighbor_average      7.096175       NaN  10.860819       NaN  0.199769       NaN
       top_variance                  gls_map               3.384471       NaN   5.727119       NaN  0.078424       NaN
                                     gsp                   3.882213       NaN   6.459881       NaN  0.088895       NaN
                                     historical_tod_mean   3.782458       NaN   6.899043       NaN  0.091971       NaN
                                     neighbor_average      9.197559       NaN  13.985723       NaN  0.175513       NaN
       validation_swap_selected      gls_map               3.237263       NaN   5.533583       NaN  0.086262       NaN
                                     gsp                   4.252736       NaN   7.168438       NaN  0.113776       NaN
                                     historical_tod_mean   4.268556       NaN   7.785329       NaN  0.123166       NaN
                                     neighbor_average      7.103250       NaN  10.904653       NaN  0.207300       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1  swap_from_scenario_cvar gls_map 3.759644 6.270618
    0.2 validation_swap_selected gls_map 3.545567 5.961101
    0.3 validation_swap_selected gls_map 3.237263 5.533583
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.030891     -0.097422 210
    gsp   condition_number    -0.030651     -0.107048 210
    gsp information_logdet     0.017571      0.052105 210
gls_map    posterior_trace     0.812968      0.810602 210
gls_map   condition_number     0.835873      0.876709 210
gls_map information_logdet    -0.702648     -0.761640 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv