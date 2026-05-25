---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-05-22, 2012-06-25
Test days: 2012-06-04, 2012-06-05
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.594080       NaN   6.027894       NaN  0.093699       NaN
                                     gsp                   4.286093       NaN   7.199455       NaN  0.115157       NaN
                                     historical_tod_mean   4.311794       NaN   7.343692       NaN  0.117478       NaN
                                     neighbor_average      7.505260       NaN  11.322430       NaN  0.197685       NaN
       best_random_by_validation     gls_map               3.594080       NaN   6.027894       NaN  0.093699       NaN
                                     gsp                   4.286093       NaN   7.199455       NaN  0.115157       NaN
                                     historical_tod_mean   4.311794       NaN   7.343692       NaN  0.117478       NaN
                                     neighbor_average      7.505260       NaN  11.322430       NaN  0.197685       NaN
       coverage                      gls_map               3.721290       NaN   6.164810       NaN  0.094096       NaN
                                     gsp                   4.329009       NaN   7.210906       NaN  0.111773       NaN
                                     historical_tod_mean   4.324184       NaN   7.332370       NaN  0.115441       NaN
                                     neighbor_average      7.758895       NaN  11.499300       NaN  0.202329       NaN
       degree                        gls_map               4.209211       NaN   7.028355       NaN  0.110981       NaN
                                     gsp                   4.354119       NaN   7.261598       NaN  0.116270       NaN
                                     historical_tod_mean   4.320105       NaN   7.365311       NaN  0.118189       NaN
                                     neighbor_average      8.490983       NaN  12.569340       NaN  0.220932       NaN
       graph_sampling_laplacian      gls_map               4.771756       NaN   7.518871       NaN  0.122532       NaN
                                     gsp                   4.379790       NaN   7.284382       NaN  0.114820       NaN
                                     historical_tod_mean   4.350698       NaN   7.338431       NaN  0.115125       NaN
                                     neighbor_average      8.722001       NaN  13.693897       NaN  0.252489       NaN
       greedy_a_trace                gls_map               3.512020       NaN   5.859777       NaN  0.090531       NaN
                                     gsp                   4.278907       NaN   7.167300       NaN  0.112301       NaN
                                     historical_tod_mean   4.301836       NaN   7.299418       NaN  0.115197       NaN
                                     neighbor_average      7.201876       NaN  11.141100       NaN  0.200384       NaN
       greedy_d_logdet               gls_map               4.247024       NaN   6.817700       NaN  0.106202       NaN
                                     gsp                   4.273198       NaN   7.192135       NaN  0.109616       NaN
                                     historical_tod_mean   4.251704       NaN   7.223079       NaN  0.112401       NaN
                                     neighbor_average      7.990391       NaN  12.569064       NaN  0.237248       NaN
       multistart_swap_by_validation gls_map               3.549978       NaN   5.858168       NaN  0.089317       NaN
                                     gsp                   4.304448       NaN   7.142677       NaN  0.110350       NaN
                                     historical_tod_mean   4.289154       NaN   7.268565       NaN  0.113763       NaN
                                     neighbor_average      7.381394       NaN  11.286990       NaN  0.196193       NaN
       observability_proxy           gls_map               4.189331       NaN   7.029837       NaN  0.110451       NaN
                                     gsp                   4.346507       NaN   7.274804       NaN  0.116136       NaN
                                     historical_tod_mean   4.325026       NaN   7.377747       NaN  0.118302       NaN
                                     neighbor_average     10.609260       NaN  16.183114       NaN  0.238590       NaN
       qr_pod_modes                  gls_map               3.908341       NaN   6.218178       NaN  0.096120       NaN
                                     gsp                   4.260401       NaN   7.115695       NaN  0.107535       NaN
                                     historical_tod_mean   4.243953       NaN   7.207418       NaN  0.111603       NaN
                                     neighbor_average      7.503756       NaN  11.607986       NaN  0.216618       NaN
       random                        gls_map               3.694748  0.054631   6.217861  0.106816  0.096371  0.002323
                                     gsp                   4.322915  0.021621   7.230064  0.045927  0.114523  0.001957
                                     historical_tod_mean   4.336337  0.022099   7.367034  0.041840  0.117960  0.001721
                                     neighbor_average      7.525400  0.131410  11.601215  0.197755  0.202613  0.004447
       rcss_selected                 gls_map               3.512020       NaN   5.859777       NaN  0.090531       NaN
                                     gsp                   4.278907       NaN   7.167300       NaN  0.112301       NaN
                                     historical_tod_mean   4.301836       NaN   7.299418       NaN  0.115197       NaN
                                     neighbor_average      7.201876       NaN  11.141100       NaN  0.200384       NaN
       robust_coverage_cvar          gls_map               3.613966       NaN   6.081326       NaN  0.096763       NaN
                                     gsp                   4.296144       NaN   7.196484       NaN  0.116573       NaN
                                     historical_tod_mean   4.291165       NaN   7.308679       NaN  0.117743       NaN
                                     neighbor_average      7.529958       NaN  11.471685       NaN  0.208322       NaN
       scenario_average_a_trace      gls_map               3.722714       NaN   6.282765       NaN  0.101613       NaN
                                     gsp                   4.274071       NaN   7.218788       NaN  0.116713       NaN
                                     historical_tod_mean   4.291618       NaN   7.328538       NaN  0.118394       NaN
                                     neighbor_average      7.751980       NaN  11.802331       NaN  0.223804       NaN
       scenario_cvar_a_trace         gls_map               3.674666       NaN   6.153829       NaN  0.098710       NaN
                                     gsp                   4.260522       NaN   7.195547       NaN  0.116350       NaN
                                     historical_tod_mean   4.262512       NaN   7.292696       NaN  0.117495       NaN
                                     neighbor_average      7.599764       NaN  11.502318       NaN  0.212105       NaN
       swap_from_best_random_trace   gls_map               3.539309       NaN   5.885315       NaN  0.088622       NaN
                                     gsp                   4.273790       NaN   7.154999       NaN  0.110986       NaN
                                     historical_tod_mean   4.287597       NaN   7.280774       NaN  0.114175       NaN
                                     neighbor_average      7.550651       NaN  11.299020       NaN  0.199537       NaN
       swap_from_greedy_a_trace      gls_map               3.611307       NaN   5.915871       NaN  0.088509       NaN
                                     gsp                   4.281767       NaN   7.135848       NaN  0.108549       NaN
                                     historical_tod_mean   4.295305       NaN   7.261150       NaN  0.112468       NaN
                                     neighbor_average      7.183215       NaN  11.197551       NaN  0.202238       NaN
       swap_from_scenario_average    gls_map               3.624341       NaN   6.000415       NaN  0.094800       NaN
                                     gsp                   4.257363       NaN   7.186905       NaN  0.114875       NaN
                                     historical_tod_mean   4.284958       NaN   7.310025       NaN  0.117595       NaN
                                     neighbor_average      7.483922       NaN  11.529497       NaN  0.213655       NaN
       swap_from_scenario_cvar       gls_map               3.556240       NaN   5.970984       NaN  0.093152       NaN
                                     gsp                   4.259259       NaN   7.164338       NaN  0.114459       NaN
                                     historical_tod_mean   4.259937       NaN   7.275195       NaN  0.116887       NaN
                                     neighbor_average      7.445038       NaN  11.204003       NaN  0.205836       NaN
       top_variance                  gls_map               3.842044       NaN   6.345578       NaN  0.098054       NaN
                                     gsp                   4.216592       NaN   6.902503       NaN  0.108653       NaN
                                     historical_tod_mean   4.082420       NaN   6.934106       NaN  0.107789       NaN
                                     neighbor_average     10.852201       NaN  16.520418       NaN  0.218812       NaN
       validation_swap_selected      gls_map               3.502539       NaN   5.865939       NaN  0.090722       NaN
                                     gsp                   4.240418       NaN   7.127157       NaN  0.112007       NaN
                                     historical_tod_mean   4.274189       NaN   7.269196       NaN  0.114584       NaN
                                     neighbor_average      7.245667       NaN  11.156890       NaN  0.200910       NaN
0.2    best_random_by_trace          gls_map               3.390406       NaN   5.689964       NaN  0.085211       NaN
                                     gsp                   4.311479       NaN   7.149027       NaN  0.111685       NaN
                                     historical_tod_mean   4.312279       NaN   7.302385       NaN  0.115405       NaN
                                     neighbor_average      7.056569       NaN  11.075861       NaN  0.188195       NaN
       best_random_by_validation     gls_map               3.327994       NaN   5.534527       NaN  0.084032       NaN
                                     gsp                   4.233492       NaN   7.046557       NaN  0.108860       NaN
                                     historical_tod_mean   4.248271       NaN   7.205669       NaN  0.112755       NaN
                                     neighbor_average      7.331494       NaN  11.443081       NaN  0.190549       NaN
       coverage                      gls_map               3.400175       NaN   5.690453       NaN  0.085578       NaN
                                     gsp                   4.346592       NaN   7.253076       NaN  0.112647       NaN
                                     historical_tod_mean   4.349287       NaN   7.386835       NaN  0.116997       NaN
                                     neighbor_average      7.116683       NaN  10.976062       NaN  0.189196       NaN
       degree                        gls_map               4.181191       NaN   6.998680       NaN  0.111401       NaN
                                     gsp                   4.350169       NaN   7.256535       NaN  0.116114       NaN
                                     historical_tod_mean   4.304681       NaN   7.368936       NaN  0.118434       NaN
                                     neighbor_average      9.475897       NaN  13.499025       NaN  0.221539       NaN
       graph_sampling_laplacian      gls_map               4.286098       NaN   7.055028       NaN  0.109314       NaN
                                     gsp                   4.447010       NaN   7.297444       NaN  0.111358       NaN
                                     historical_tod_mean   4.379810       NaN   7.350087       NaN  0.114342       NaN
                                     neighbor_average      8.131888       NaN  12.114590       NaN  0.218310       NaN
       greedy_a_trace                gls_map               3.140910       NaN   5.145692       NaN  0.076774       NaN
                                     gsp                   4.213276       NaN   7.031893       NaN  0.106233       NaN
                                     historical_tod_mean   4.203568       NaN   7.155596       NaN  0.110480       NaN
                                     neighbor_average      7.045151       NaN  10.847764       NaN  0.193016       NaN
       greedy_d_logdet               gls_map               3.629014       NaN   5.853609       NaN  0.091825       NaN
                                     gsp                   4.273345       NaN   7.154399       NaN  0.110031       NaN
                                     historical_tod_mean   4.252713       NaN   7.240859       NaN  0.113661       NaN
                                     neighbor_average      7.589191       NaN  11.959473       NaN  0.225902       NaN
       multistart_swap_by_validation gls_map               3.192193       NaN   5.247803       NaN  0.078052       NaN
                                     gsp                   4.216356       NaN   7.032868       NaN  0.106883       NaN
                                     historical_tod_mean   4.239051       NaN   7.184985       NaN  0.110765       NaN
                                     neighbor_average      7.064107       NaN  10.916800       NaN  0.186716       NaN
       observability_proxy           gls_map               4.158140       NaN   6.959661       NaN  0.110023       NaN
                                     gsp                   4.339906       NaN   7.256583       NaN  0.115673       NaN
                                     historical_tod_mean   4.287574       NaN   7.364492       NaN  0.118163       NaN
                                     neighbor_average      9.931583       NaN  14.129481       NaN  0.229485       NaN
       qr_pod_modes                  gls_map               3.374224       NaN   5.426688       NaN  0.082750       NaN
                                     gsp                   4.251580       NaN   7.090454       NaN  0.108116       NaN
                                     historical_tod_mean   4.211121       NaN   7.185545       NaN  0.111768       NaN
                                     neighbor_average      7.340571       NaN  11.309468       NaN  0.210445       NaN
       random                        gls_map               3.407096  0.046623   5.751671  0.095819  0.088175  0.002181
                                     gsp                   4.336349  0.029760   7.222661  0.057981  0.114551  0.002369
                                     historical_tod_mean   4.341296  0.031747   7.374461  0.056050  0.118167  0.002222
                                     neighbor_average      7.211781  0.111750  11.315850  0.186299  0.194719  0.004758
       rcss_selected                 gls_map               3.160301       NaN   5.148240       NaN  0.076822       NaN
                                     gsp                   4.219396       NaN   7.026996       NaN  0.106221       NaN
                                     historical_tod_mean   4.198511       NaN   7.143319       NaN  0.110284       NaN
                                     neighbor_average      7.051319       NaN  10.936191       NaN  0.194989       NaN
       robust_coverage_cvar          gls_map               3.289183       NaN   5.492699       NaN  0.086999       NaN
                                     gsp                   4.231688       NaN   7.123572       NaN  0.114678       NaN
                                     historical_tod_mean   4.226401       NaN   7.254546       NaN  0.117553       NaN
                                     neighbor_average      7.396521       NaN  11.521705       NaN  0.206355       NaN
       scenario_average_a_trace      gls_map               3.418499       NaN   5.758550       NaN  0.092539       NaN
                                     gsp                   4.271986       NaN   7.204882       NaN  0.115967       NaN
                                     historical_tod_mean   4.277849       NaN   7.324640       NaN  0.119420       NaN
                                     neighbor_average      7.565752       NaN  11.801318       NaN  0.223033       NaN
       scenario_cvar_a_trace         gls_map               3.396339       NaN   5.719418       NaN  0.090267       NaN
                                     gsp                   4.262263       NaN   7.157880       NaN  0.115068       NaN
                                     historical_tod_mean   4.235828       NaN   7.266281       NaN  0.117600       NaN
                                     neighbor_average      7.367718       NaN  11.502664       NaN  0.206335       NaN
       swap_from_best_random_trace   gls_map               3.243384       NaN   5.426317       NaN  0.081106       NaN
                                     gsp                   4.269041       NaN   7.116100       NaN  0.110318       NaN
                                     historical_tod_mean   4.266292       NaN   7.260989       NaN  0.114619       NaN
                                     neighbor_average      6.879273       NaN  10.711715       NaN  0.186181       NaN
       swap_from_greedy_a_trace      gls_map               3.160301       NaN   5.148240       NaN  0.076822       NaN
                                     gsp                   4.219396       NaN   7.026996       NaN  0.106221       NaN
                                     historical_tod_mean   4.198511       NaN   7.143319       NaN  0.110284       NaN
                                     neighbor_average      7.051319       NaN  10.936191       NaN  0.194989       NaN
       swap_from_scenario_average    gls_map               3.328192       NaN   5.462200       NaN  0.085346       NaN
                                     gsp                   4.232531       NaN   7.123014       NaN  0.111742       NaN
                                     historical_tod_mean   4.247989       NaN   7.255425       NaN  0.115635       NaN
                                     neighbor_average      7.301751       NaN  11.411917       NaN  0.209952       NaN
       swap_from_scenario_cvar       gls_map               3.281002       NaN   5.418605       NaN  0.083974       NaN
                                     gsp                   4.227165       NaN   7.075776       NaN  0.111035       NaN
                                     historical_tod_mean   4.200920       NaN   7.192162       NaN  0.113976       NaN
                                     neighbor_average      7.127480       NaN  11.069954       NaN  0.200197       NaN
       top_variance                  gls_map               3.534422       NaN   5.875232       NaN  0.087818       NaN
                                     gsp                   4.075724       NaN   6.698514       NaN  0.102771       NaN
                                     historical_tod_mean   3.953475       NaN   6.736769       NaN  0.102367       NaN
                                     neighbor_average      9.134048       NaN  14.306038       NaN  0.188398       NaN
       validation_swap_selected      gls_map               3.158734       NaN   5.148781       NaN  0.076709       NaN
                                     gsp                   4.211501       NaN   7.020874       NaN  0.106002       NaN
                                     historical_tod_mean   4.188051       NaN   7.134571       NaN  0.110047       NaN
                                     neighbor_average      7.067064       NaN  10.958469       NaN  0.194965       NaN
0.3    best_random_by_trace          gls_map               3.179729       NaN   5.340107       NaN  0.077313       NaN
                                     gsp                   4.324313       NaN   7.131714       NaN  0.108416       NaN
                                     historical_tod_mean   4.308369       NaN   7.287239       NaN  0.111724       NaN
                                     neighbor_average      7.125086       NaN  11.186017       NaN  0.187356       NaN
       best_random_by_validation     gls_map               3.112789       NaN   5.197122       NaN  0.078319       NaN
                                     gsp                   4.278337       NaN   7.059759       NaN  0.109734       NaN
                                     historical_tod_mean   4.282522       NaN   7.229651       NaN  0.113631       NaN
                                     neighbor_average      6.932463       NaN  10.896172       NaN  0.183690       NaN
       coverage                      gls_map               3.244531       NaN   5.451894       NaN  0.082613       NaN
                                     gsp                   4.406002       NaN   7.277614       NaN  0.114820       NaN
                                     historical_tod_mean   4.388595       NaN   7.423447       NaN  0.118814       NaN
                                     neighbor_average      7.024967       NaN  11.074185       NaN  0.192013       NaN
       degree                        gls_map               3.992905       NaN   6.805826       NaN  0.107037       NaN
                                     gsp                   4.271357       NaN   7.234415       NaN  0.115065       NaN
                                     historical_tod_mean   4.223326       NaN   7.354974       NaN  0.117658       NaN
                                     neighbor_average      8.464823       NaN  13.039792       NaN  0.216951       NaN
       graph_sampling_laplacian      gls_map               4.213059       NaN   6.934602       NaN  0.104735       NaN
                                     gsp                   4.443274       NaN   7.254370       NaN  0.107458       NaN
                                     historical_tod_mean   4.367340       NaN   7.307921       NaN  0.111163       NaN
                                     neighbor_average      8.335416       NaN  12.632340       NaN  0.234146       NaN
       greedy_a_trace                gls_map               2.877000       NaN   4.665742       NaN  0.069848       NaN
                                     gsp                   4.215931       NaN   7.025271       NaN  0.106788       NaN
                                     historical_tod_mean   4.190491       NaN   7.150829       NaN  0.110906       NaN
                                     neighbor_average      6.829498       NaN  10.650424       NaN  0.192397       NaN
       greedy_d_logdet               gls_map               3.194964       NaN   5.197132       NaN  0.079762       NaN
                                     gsp                   4.220979       NaN   7.131151       NaN  0.109031       NaN
                                     historical_tod_mean   4.197836       NaN   7.220793       NaN  0.113029       NaN
                                     neighbor_average      7.281090       NaN  11.420134       NaN  0.211364       NaN
       multistart_swap_by_validation gls_map               2.987068       NaN   4.965518       NaN  0.072845       NaN
                                     gsp                   4.203323       NaN   6.995781       NaN  0.106082       NaN
                                     historical_tod_mean   4.189545       NaN   7.153099       NaN  0.110068       NaN
                                     neighbor_average      6.860837       NaN  10.737956       NaN  0.176744       NaN
       observability_proxy           gls_map               3.945777       NaN   6.715245       NaN  0.105307       NaN
                                     gsp                   4.262700       NaN   7.218769       NaN  0.114670       NaN
                                     historical_tod_mean   4.216020       NaN   7.342294       NaN  0.117324       NaN
                                     neighbor_average      8.522831       NaN  13.057072       NaN  0.215436       NaN
       qr_pod_modes                  gls_map               2.944808       NaN   4.767263       NaN  0.071724       NaN
                                     gsp                   4.233880       NaN   7.102606       NaN  0.107704       NaN
                                     historical_tod_mean   4.193164       NaN   7.209770       NaN  0.111902       NaN
                                     neighbor_average      6.883120       NaN  10.765089       NaN  0.196202       NaN
       random                        gls_map               3.203207  0.046355   5.413292  0.098017  0.082326  0.002644
                                     gsp                   4.345420  0.040715   7.222295  0.072639  0.114732  0.003011
                                     historical_tod_mean   4.343481  0.042855   7.380415  0.071822  0.118476  0.003026
                                     neighbor_average      7.057879  0.090918  11.137913  0.163075  0.190206  0.005358
       rcss_selected                 gls_map               2.862023       NaN   4.620982       NaN  0.069334       NaN
                                     gsp                   4.206264       NaN   7.003963       NaN  0.106321       NaN
                                     historical_tod_mean   4.169112       NaN   7.127346       NaN  0.110301       NaN
                                     neighbor_average      6.850121       NaN  10.618752       NaN  0.191977       NaN
       robust_coverage_cvar          gls_map               3.104025       NaN   5.231502       NaN  0.083469       NaN
                                     gsp                   4.219460       NaN   7.117279       NaN  0.115537       NaN
                                     historical_tod_mean   4.189146       NaN   7.243005       NaN  0.118535       NaN
                                     neighbor_average      7.406583       NaN  11.702526       NaN  0.209269       NaN
       scenario_average_a_trace      gls_map               3.163698       NaN   5.311092       NaN  0.084703       NaN
                                     gsp                   4.278379       NaN   7.229808       NaN  0.116610       NaN
                                     historical_tod_mean   4.242778       NaN   7.331625       NaN  0.120279       NaN
                                     neighbor_average      7.231782       NaN  11.343098       NaN  0.212737       NaN
       scenario_cvar_a_trace         gls_map               3.199699       NaN   5.402963       NaN  0.085117       NaN
                                     gsp                   4.255308       NaN   7.156848       NaN  0.114280       NaN
                                     historical_tod_mean   4.166166       NaN   7.226309       NaN  0.117347       NaN
                                     neighbor_average      7.335632       NaN  11.662505       NaN  0.208887       NaN
       swap_from_best_random_trace   gls_map               3.077465       NaN   5.117653       NaN  0.074620       NaN
                                     gsp                   4.273931       NaN   7.071029       NaN  0.107780       NaN
                                     historical_tod_mean   4.263385       NaN   7.228143       NaN  0.111093       NaN
                                     neighbor_average      6.907715       NaN  10.824825       NaN  0.184647       NaN
       swap_from_greedy_a_trace      gls_map               2.862023       NaN   4.620982       NaN  0.069334       NaN
                                     gsp                   4.206264       NaN   7.003963       NaN  0.106321       NaN
                                     historical_tod_mean   4.169112       NaN   7.127346       NaN  0.110301       NaN
                                     neighbor_average      6.850121       NaN  10.618752       NaN  0.191977       NaN
       swap_from_scenario_average    gls_map               3.068792       NaN   5.022504       NaN  0.075878       NaN
                                     gsp                   4.211575       NaN   7.079854       NaN  0.107746       NaN
                                     historical_tod_mean   4.187237       NaN   7.184499       NaN  0.112005       NaN
                                     neighbor_average      7.075083       NaN  11.026240       NaN  0.200233       NaN
       swap_from_scenario_cvar       gls_map               3.064523       NaN   5.009553       NaN  0.075565       NaN
                                     gsp                   4.204844       NaN   7.010875       NaN  0.106636       NaN
                                     historical_tod_mean   4.130015       NaN   7.100185       NaN  0.110063       NaN
                                     neighbor_average      7.017361       NaN  11.053402       NaN  0.195025       NaN
       top_variance                  gls_map               3.184615       NaN   5.313904       NaN  0.074563       NaN
                                     gsp                   3.861714       NaN   6.356564       NaN  0.092123       NaN
                                     historical_tod_mean   3.745587       NaN   6.403199       NaN  0.091883       NaN
                                     neighbor_average      8.753102       NaN  13.633742       NaN  0.173327       NaN
       validation_swap_selected      gls_map               2.847274       NaN   4.657312       NaN  0.071842       NaN
                                     gsp                   4.199680       NaN   7.029097       NaN  0.109053       NaN
                                     historical_tod_mean   4.168307       NaN   7.157304       NaN  0.112989       NaN
                                     neighbor_average      6.857348       NaN  10.622424       NaN  0.194221       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 3.502539 5.865939
    0.2           greedy_a_trace gls_map 3.140910 5.145692
    0.3 validation_swap_selected gls_map 2.847274 4.657312
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.085077     -0.150734 360
    gsp   condition_number    -0.084701     -0.186857 360
    gsp information_logdet     0.095660      0.129466 360
gls_map    posterior_trace     0.914453      0.931546 360
gls_map   condition_number     0.829293      0.898426 360
gls_map information_logdet    -0.841482     -0.883935 360
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv