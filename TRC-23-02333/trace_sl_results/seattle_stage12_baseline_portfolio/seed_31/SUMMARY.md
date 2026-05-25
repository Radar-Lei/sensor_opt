---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-13, 2015-01-24
Test days: 2015-01-02, 2015-01-27
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.446406       NaN   5.536649       NaN  0.101323       NaN
                                     gsp                  4.244484       NaN   6.877766       NaN  0.139433       NaN
                                     historical_tod_mean  4.956976       NaN   8.405824       NaN  0.179431       NaN
                                     neighbor_average     5.649983       NaN   9.036432       NaN  0.188374       NaN
       best_random_by_validation     gls_map              3.341304       NaN   5.410742       NaN  0.095823       NaN
                                     gsp                  4.179061       NaN   6.735193       NaN  0.134503       NaN
                                     historical_tod_mean  4.902524       NaN   8.306310       NaN  0.173062       NaN
                                     neighbor_average     5.726070       NaN   9.396314       NaN  0.174579       NaN
       coverage                      gls_map              3.392008       NaN   5.317177       NaN  0.095444       NaN
                                     gsp                  4.224778       NaN   6.825765       NaN  0.134524       NaN
                                     historical_tod_mean  4.949046       NaN   8.379991       NaN  0.175431       NaN
                                     neighbor_average     5.602326       NaN   8.604355       NaN  0.169204       NaN
       degree                        gls_map              3.674761       NaN   5.890296       NaN  0.107661       NaN
                                     gsp                  4.186422       NaN   6.615870       NaN  0.129944       NaN
                                     historical_tod_mean  4.899627       NaN   8.315309       NaN  0.175209       NaN
                                     neighbor_average     6.422647       NaN  10.214735       NaN  0.202606       NaN
       graph_sampling_laplacian      gls_map              4.020866       NaN   6.532115       NaN  0.129375       NaN
                                     gsp                  4.569066       NaN   7.521579       NaN  0.158756       NaN
                                     historical_tod_mean  5.057559       NaN   8.584674       NaN  0.185862       NaN
                                     neighbor_average     6.503096       NaN  10.697430       NaN  0.233298       NaN
       greedy_a_trace                gls_map              3.242546       NaN   5.228230       NaN  0.096267       NaN
                                     gsp                  4.236719       NaN   6.862698       NaN  0.138900       NaN
                                     historical_tod_mean  4.950244       NaN   8.383245       NaN  0.177788       NaN
                                     neighbor_average     5.443819       NaN   8.786134       NaN  0.175825       NaN
       greedy_d_logdet               gls_map              4.088826       NaN   6.255108       NaN  0.115314       NaN
                                     gsp                  4.460872       NaN   7.187584       NaN  0.144888       NaN
                                     historical_tod_mean  5.070140       NaN   8.520587       NaN  0.182161       NaN
                                     neighbor_average     6.397308       NaN  10.501822       NaN  0.239559       NaN
       multistart_swap_by_validation gls_map              3.206658       NaN   5.113663       NaN  0.089448       NaN
                                     gsp                  4.220385       NaN   6.821212       NaN  0.135193       NaN
                                     historical_tod_mean  4.934980       NaN   8.331052       NaN  0.171926       NaN
                                     neighbor_average     5.828663       NaN   9.164540       NaN  0.171970       NaN
       observability_proxy           gls_map              3.641778       NaN   5.835623       NaN  0.107518       NaN
                                     gsp                  4.197148       NaN   6.638365       NaN  0.131073       NaN
                                     historical_tod_mean  4.897874       NaN   8.303733       NaN  0.175303       NaN
                                     neighbor_average     6.468443       NaN  10.361143       NaN  0.199643       NaN
       qr_pod_modes                  gls_map              3.547992       NaN   5.605851       NaN  0.104084       NaN
                                     gsp                  4.308886       NaN   6.953395       NaN  0.138970       NaN
                                     historical_tod_mean  5.023802       NaN   8.453217       NaN  0.180418       NaN
                                     neighbor_average     6.060030       NaN   9.705980       NaN  0.211216       NaN
       random                        gls_map              3.421023  0.063868   5.490537  0.135187  0.100450  0.004325
                                     gsp                  4.221951  0.047626   6.820613  0.117905  0.136865  0.004044
                                     historical_tod_mean  4.927719  0.035316   8.365473  0.059882  0.176548  0.002805
                                     neighbor_average     5.827199  0.264993   9.292525  0.407056  0.179151  0.009735
       rcss_selected                 gls_map              3.206658       NaN   5.113663       NaN  0.089448       NaN
                                     gsp                  4.220385       NaN   6.821212       NaN  0.135193       NaN
                                     historical_tod_mean  4.934980       NaN   8.331052       NaN  0.171926       NaN
                                     neighbor_average     5.828663       NaN   9.164540       NaN  0.171970       NaN
       robust_coverage_cvar          gls_map              3.335337       NaN   5.490522       NaN  0.103038       NaN
                                     gsp                  4.247710       NaN   6.897758       NaN  0.141030       NaN
                                     historical_tod_mean  4.976976       NaN   8.442086       NaN  0.180116       NaN
                                     neighbor_average     5.702769       NaN   9.002488       NaN  0.186467       NaN
       scenario_average_a_trace      gls_map              3.284920       NaN   5.277906       NaN  0.096752       NaN
                                     gsp                  4.241741       NaN   6.847870       NaN  0.139280       NaN
                                     historical_tod_mean  4.959365       NaN   8.390751       NaN  0.179016       NaN
                                     neighbor_average     5.791170       NaN   9.137002       NaN  0.189393       NaN
       scenario_cvar_a_trace         gls_map              3.328259       NaN   5.332929       NaN  0.099465       NaN
                                     gsp                  4.250423       NaN   6.860556       NaN  0.140976       NaN
                                     historical_tod_mean  4.985049       NaN   8.420452       NaN  0.180704       NaN
                                     neighbor_average     5.932311       NaN   9.440836       NaN  0.200464       NaN
       swap_from_best_random_trace   gls_map              3.260094       NaN   5.265154       NaN  0.097181       NaN
                                     gsp                  4.262371       NaN   6.929127       NaN  0.141145       NaN
                                     historical_tod_mean  4.972154       NaN   8.414610       NaN  0.178837       NaN
                                     neighbor_average     5.608716       NaN   9.060010       NaN  0.184345       NaN
       swap_from_greedy_a_trace      gls_map              3.242003       NaN   5.242052       NaN  0.096618       NaN
                                     gsp                  4.242889       NaN   6.885212       NaN  0.138778       NaN
                                     historical_tod_mean  4.953439       NaN   8.384732       NaN  0.176697       NaN
                                     neighbor_average     5.782169       NaN   8.999635       NaN  0.182368       NaN
       swap_from_scenario_average    gls_map              3.252283       NaN   5.323877       NaN  0.099253       NaN
                                     gsp                  4.264090       NaN   6.933306       NaN  0.142015       NaN
                                     historical_tod_mean  4.963981       NaN   8.408152       NaN  0.178213       NaN
                                     neighbor_average     5.666887       NaN   8.935947       NaN  0.183228       NaN
       swap_from_scenario_cvar       gls_map              3.260167       NaN   5.283140       NaN  0.098587       NaN
                                     gsp                  4.280892       NaN   6.957868       NaN  0.142226       NaN
                                     historical_tod_mean  4.968060       NaN   8.394087       NaN  0.178118       NaN
                                     neighbor_average     5.735482       NaN   8.945722       NaN  0.186953       NaN
       top_variance                  gls_map              3.620651       NaN   5.588453       NaN  0.096585       NaN
                                     gsp                  4.008520       NaN   6.279822       NaN  0.114606       NaN
                                     historical_tod_mean  4.541342       NaN   7.709570       NaN  0.143612       NaN
                                     neighbor_average     8.945616       NaN  14.626234       NaN  0.187429       NaN
       validation_swap_selected      gls_map              3.210231       NaN   5.082271       NaN  0.088124       NaN
                                     gsp                  4.177637       NaN   6.701431       NaN  0.130572       NaN
                                     historical_tod_mean  4.911919       NaN   8.283767       NaN  0.170127       NaN
                                     neighbor_average     5.805129       NaN   9.146749       NaN  0.169949       NaN
0.2    best_random_by_trace          gls_map              3.060418       NaN   4.931409       NaN  0.088013       NaN
                                     gsp                  4.168193       NaN   6.605754       NaN  0.131468       NaN
                                     historical_tod_mean  4.938290       NaN   8.349157       NaN  0.176649       NaN
                                     neighbor_average     5.294024       NaN   8.503389       NaN  0.153998       NaN
       best_random_by_validation     gls_map              2.971172       NaN   4.728366       NaN  0.082017       NaN
                                     gsp                  4.123078       NaN   6.508724       NaN  0.124784       NaN
                                     historical_tod_mean  4.876083       NaN   8.241935       NaN  0.168976       NaN
                                     neighbor_average     4.928461       NaN   7.730239       NaN  0.142039       NaN
       coverage                      gls_map              2.986320       NaN   4.728245       NaN  0.083639       NaN
                                     gsp                  4.163487       NaN   6.603581       NaN  0.129418       NaN
                                     historical_tod_mean  4.948264       NaN   8.368256       NaN  0.176778       NaN
                                     neighbor_average     4.667441       NaN   7.316687       NaN  0.140579       NaN
       degree                        gls_map              3.621600       NaN   5.843896       NaN  0.107625       NaN
                                     gsp                  4.259182       NaN   6.593421       NaN  0.128639       NaN
                                     historical_tod_mean  4.923029       NaN   8.312129       NaN  0.177240       NaN
                                     neighbor_average     6.568662       NaN  10.624133       NaN  0.206203       NaN
       graph_sampling_laplacian      gls_map              3.890138       NaN   6.380033       NaN  0.127155       NaN
                                     gsp                  4.510891       NaN   7.335817       NaN  0.155310       NaN
                                     historical_tod_mean  5.136936       NaN   8.722066       NaN  0.192598       NaN
                                     neighbor_average     6.557627       NaN  10.738917       NaN  0.240350       NaN
       greedy_a_trace                gls_map              2.967326       NaN   4.668448       NaN  0.083117       NaN
                                     gsp                  4.234555       NaN   6.668895       NaN  0.130711       NaN
                                     historical_tod_mean  5.004327       NaN   8.420750       NaN  0.178397       NaN
                                     neighbor_average     4.739971       NaN   7.560529       NaN  0.153135       NaN
       greedy_d_logdet               gls_map              3.539395       NaN   5.543385       NaN  0.104979       NaN
                                     gsp                  4.421741       NaN   7.018703       NaN  0.141834       NaN
                                     historical_tod_mean  5.193083       NaN   8.684830       NaN  0.188815       NaN
                                     neighbor_average     5.782048       NaN   9.565543       NaN  0.218585       NaN
       multistart_swap_by_validation gls_map              2.968053       NaN   4.718434       NaN  0.083115       NaN
                                     gsp                  4.204180       NaN   6.644694       NaN  0.130045       NaN
                                     historical_tod_mean  4.989401       NaN   8.401381       NaN  0.176125       NaN
                                     neighbor_average     4.818630       NaN   7.524317       NaN  0.151870       NaN
       observability_proxy           gls_map              3.509306       NaN   5.665035       NaN  0.103446       NaN
                                     gsp                  4.236756       NaN   6.557134       NaN  0.126624       NaN
                                     historical_tod_mean  4.893715       NaN   8.265729       NaN  0.174902       NaN
                                     neighbor_average     6.398981       NaN  10.234897       NaN  0.194468       NaN
       qr_pod_modes                  gls_map              3.119730       NaN   4.937037       NaN  0.089388       NaN
                                     gsp                  4.324384       NaN   6.843548       NaN  0.137777       NaN
                                     historical_tod_mean  5.102629       NaN   8.559335       NaN  0.183989       NaN
                                     neighbor_average     5.078829       NaN   8.045834       NaN  0.170405       NaN
       random                        gls_map              3.117606  0.053766   5.032657  0.109043  0.090089  0.003887
                                     gsp                  4.182416  0.041305   6.648590  0.093265  0.131756  0.004335
                                     historical_tod_mean  4.933974  0.047179   8.379538  0.086827  0.176987  0.004573
                                     neighbor_average     5.161541  0.143505   8.239860  0.290005  0.154882  0.009526
       rcss_selected                 gls_map              2.989704       NaN   4.733271       NaN  0.085980       NaN
                                     gsp                  4.237610       NaN   6.722547       NaN  0.135501       NaN
                                     historical_tod_mean  5.033300       NaN   8.475703       NaN  0.182609       NaN
                                     neighbor_average     5.037135       NaN   7.960089       NaN  0.167201       NaN
       robust_coverage_cvar          gls_map              3.099496       NaN   4.966977       NaN  0.091288       NaN
                                     gsp                  4.281196       NaN   6.760302       NaN  0.135940       NaN
                                     historical_tod_mean  5.056591       NaN   8.526158       NaN  0.183861       NaN
                                     neighbor_average     4.979143       NaN   7.888532       NaN  0.163295       NaN
       scenario_average_a_trace      gls_map              3.175008       NaN   5.030288       NaN  0.092235       NaN
                                     gsp                  4.331727       NaN   6.827314       NaN  0.138136       NaN
                                     historical_tod_mean  5.089236       NaN   8.550228       NaN  0.186434       NaN
                                     neighbor_average     5.227352       NaN   8.396827       NaN  0.180156       NaN
       scenario_cvar_a_trace         gls_map              3.111984       NaN   4.974162       NaN  0.091469       NaN
                                     gsp                  4.276861       NaN   6.755776       NaN  0.136478       NaN
                                     historical_tod_mean  5.083602       NaN   8.547204       NaN  0.185392       NaN
                                     neighbor_average     5.366813       NaN   8.571011       NaN  0.184660       NaN
       swap_from_best_random_trace   gls_map              3.004662       NaN   4.799366       NaN  0.086012       NaN
                                     gsp                  4.250732       NaN   6.703406       NaN  0.133300       NaN
                                     historical_tod_mean  5.043673       NaN   8.475884       NaN  0.181278       NaN
                                     neighbor_average     4.890338       NaN   7.675473       NaN  0.157051       NaN
       swap_from_greedy_a_trace      gls_map              2.988766       NaN   4.678428       NaN  0.082595       NaN
                                     gsp                  4.261207       NaN   6.716671       NaN  0.131937       NaN
                                     historical_tod_mean  5.036327       NaN   8.459113       NaN  0.179030       NaN
                                     neighbor_average     4.901615       NaN   7.795780       NaN  0.157826       NaN
       swap_from_scenario_average    gls_map              3.013934       NaN   4.793214       NaN  0.087230       NaN
                                     gsp                  4.261049       NaN   6.736181       NaN  0.135071       NaN
                                     historical_tod_mean  5.049691       NaN   8.490101       NaN  0.183628       NaN
                                     neighbor_average     4.922692       NaN   7.843490       NaN  0.169053       NaN
       swap_from_scenario_cvar       gls_map              2.989704       NaN   4.733271       NaN  0.085980       NaN
                                     gsp                  4.237610       NaN   6.722547       NaN  0.135501       NaN
                                     historical_tod_mean  5.033300       NaN   8.475703       NaN  0.182609       NaN
                                     neighbor_average     5.037135       NaN   7.960089       NaN  0.167201       NaN
       top_variance                  gls_map              3.180235       NaN   4.913110       NaN  0.077344       NaN
                                     gsp                  3.818080       NaN   5.821908       NaN  0.097998       NaN
                                     historical_tod_mean  4.212281       NaN   7.096273       NaN  0.120728       NaN
                                     neighbor_average     7.386446       NaN  12.227148       NaN  0.147855       NaN
       validation_swap_selected      gls_map              2.909383       NaN   4.575561       NaN  0.081788       NaN
                                     gsp                  4.135623       NaN   6.555764       NaN  0.129891       NaN
                                     historical_tod_mean  4.940232       NaN   8.352331       NaN  0.176356       NaN
                                     neighbor_average     5.044899       NaN   7.880433       NaN  0.159879       NaN
0.3    best_random_by_trace          gls_map              2.924852       NaN   4.706766       NaN  0.082211       NaN
                                     gsp                  4.229794       NaN   6.625911       NaN  0.127619       NaN
                                     historical_tod_mean  4.991336       NaN   8.426448       NaN  0.175978       NaN
                                     neighbor_average     4.539723       NaN   7.165815       NaN  0.137413       NaN
       best_random_by_validation     gls_map              2.798400       NaN   4.438766       NaN  0.076524       NaN
                                     gsp                  4.045843       NaN   6.401398       NaN  0.122562       NaN
                                     historical_tod_mean  4.792739       NaN   8.155564       NaN  0.165583       NaN
                                     neighbor_average     4.780633       NaN   7.384488       NaN  0.124264       NaN
       coverage                      gls_map              2.772957       NaN   4.422100       NaN  0.078042       NaN
                                     gsp                  4.185907       NaN   6.623448       NaN  0.131099       NaN
                                     historical_tod_mean  4.967559       NaN   8.431723       NaN  0.179631       NaN
                                     neighbor_average     4.514527       NaN   6.921454       NaN  0.128286       NaN
       degree                        gls_map              3.534430       NaN   5.646696       NaN  0.103692       NaN
                                     gsp                  4.253840       NaN   6.536550       NaN  0.124902       NaN
                                     historical_tod_mean  4.902821       NaN   8.211019       NaN  0.170947       NaN
                                     neighbor_average     7.143226       NaN  11.461253       NaN  0.196586       NaN
       graph_sampling_laplacian      gls_map              3.672421       NaN   5.937731       NaN  0.113957       NaN
                                     gsp                  4.407359       NaN   7.088434       NaN  0.146737       NaN
                                     historical_tod_mean  5.108410       NaN   8.700658       NaN  0.192011       NaN
                                     neighbor_average     6.729355       NaN  10.862317       NaN  0.226346       NaN
       greedy_a_trace                gls_map              2.859377       NaN   4.469040       NaN  0.080410       NaN
                                     gsp                  4.309235       NaN   6.731855       NaN  0.132395       NaN
                                     historical_tod_mean  5.132088       NaN   8.581591       NaN  0.183345       NaN
                                     neighbor_average     4.537459       NaN   7.228982       NaN  0.148322       NaN
       greedy_d_logdet               gls_map              3.256812       NaN   5.156638       NaN  0.098634       NaN
                                     gsp                  4.448646       NaN   6.977219       NaN  0.143936       NaN
                                     historical_tod_mean  5.302490       NaN   8.843632       NaN  0.197340       NaN
                                     neighbor_average     5.375331       NaN   8.827811       NaN  0.199596       NaN
       multistart_swap_by_validation gls_map              2.746810       NaN   4.295964       NaN  0.075115       NaN
                                     gsp                  4.155272       NaN   6.513053       NaN  0.126084       NaN
                                     historical_tod_mean  4.979590       NaN   8.345866       NaN  0.173955       NaN
                                     neighbor_average     4.453382       NaN   6.914922       NaN  0.128964       NaN
       observability_proxy           gls_map              3.517795       NaN   5.615334       NaN  0.102187       NaN
                                     gsp                  4.257706       NaN   6.538613       NaN  0.123633       NaN
                                     historical_tod_mean  4.888350       NaN   8.192990       NaN  0.169210       NaN
                                     neighbor_average     7.065986       NaN  11.393041       NaN  0.194836       NaN
       qr_pod_modes                  gls_map              2.867001       NaN   4.452629       NaN  0.079488       NaN
                                     gsp                  4.271531       NaN   6.665805       NaN  0.130788       NaN
                                     historical_tod_mean  5.110876       NaN   8.541826       NaN  0.182170       NaN
                                     neighbor_average     4.560739       NaN   7.163571       NaN  0.146158       NaN
       random                        gls_map              2.928062  0.053789   4.704942  0.112524  0.082584  0.003415
                                     gsp                  4.157241  0.049469   6.549264  0.092299  0.128048  0.004199
                                     historical_tod_mean  4.919346  0.062777   8.345291  0.105228  0.175278  0.005396
                                     neighbor_average     4.814934  0.122356   7.649725  0.267575  0.137734  0.007759
       rcss_selected                 gls_map              2.721196       NaN   4.336211       NaN  0.074337       NaN
                                     gsp                  4.053137       NaN   6.329270       NaN  0.122559       NaN
                                     historical_tod_mean  4.786463       NaN   8.130404       NaN  0.169447       NaN
                                     neighbor_average     4.588528       NaN   7.235264       NaN  0.123989       NaN
       robust_coverage_cvar          gls_map              2.857727       NaN   4.483874       NaN  0.080241       NaN
                                     gsp                  4.241444       NaN   6.626046       NaN  0.130046       NaN
                                     historical_tod_mean  5.070749       NaN   8.510830       NaN  0.182054       NaN
                                     neighbor_average     4.453445       NaN   7.009433       NaN  0.140258       NaN
       scenario_average_a_trace      gls_map              2.950367       NaN   4.632700       NaN  0.085618       NaN
                                     gsp                  4.332351       NaN   6.751326       NaN  0.135492       NaN
                                     historical_tod_mean  5.152473       NaN   8.638426       NaN  0.189429       NaN
                                     neighbor_average     4.807438       NaN   7.611793       NaN  0.164135       NaN
       scenario_cvar_a_trace         gls_map              2.906828       NaN   4.585818       NaN  0.083662       NaN
                                     gsp                  4.297754       NaN   6.724240       NaN  0.135994       NaN
                                     historical_tod_mean  5.135492       NaN   8.598594       NaN  0.187638       NaN
                                     neighbor_average     4.784604       NaN   7.535109       NaN  0.155918       NaN
       swap_from_best_random_trace   gls_map              2.877629       NaN   4.555659       NaN  0.082755       NaN
                                     gsp                  4.304891       NaN   6.745278       NaN  0.134568       NaN
                                     historical_tod_mean  5.130556       NaN   8.595162       NaN  0.185549       NaN
                                     neighbor_average     4.544712       NaN   7.147202       NaN  0.148041       NaN
       swap_from_greedy_a_trace      gls_map              2.803603       NaN   4.386552       NaN  0.077273       NaN
                                     gsp                  4.270858       NaN   6.662001       NaN  0.130167       NaN
                                     historical_tod_mean  5.095836       NaN   8.513970       NaN  0.180279       NaN
                                     neighbor_average     4.485515       NaN   7.060284       NaN  0.139227       NaN
       swap_from_scenario_average    gls_map              2.848423       NaN   4.433576       NaN  0.079758       NaN
                                     gsp                  4.287626       NaN   6.671998       NaN  0.131501       NaN
                                     historical_tod_mean  5.115852       NaN   8.524108       NaN  0.183112       NaN
                                     neighbor_average     4.545689       NaN   7.183134       NaN  0.145758       NaN
       swap_from_scenario_cvar       gls_map              2.843044       NaN   4.443462       NaN  0.079865       NaN
                                     gsp                  4.290181       NaN   6.707269       NaN  0.132988       NaN
                                     historical_tod_mean  5.123395       NaN   8.559315       NaN  0.184064       NaN
                                     neighbor_average     4.550214       NaN   7.142033       NaN  0.146563       NaN
       top_variance                  gls_map              2.930507       NaN   4.545608       NaN  0.066876       NaN
                                     gsp                  3.631102       NaN   5.488298       NaN  0.086094       NaN
                                     historical_tod_mean  3.959491       NaN   6.556324       NaN  0.103100       NaN
                                     neighbor_average     6.318361       NaN  10.516257       NaN  0.124717       NaN
       validation_swap_selected      gls_map              2.690246       NaN   4.246606       NaN  0.072998       NaN
                                     gsp                  4.002726       NaN   6.267307       NaN  0.121364       NaN
                                     historical_tod_mean  4.739812       NaN   8.078159       NaN  0.167835       NaN
                                     neighbor_average     4.662538       NaN   7.280999       NaN  0.123771       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1 multistart_swap_by_validation gls_map 3.206658 5.113663
    0.2      validation_swap_selected gls_map 2.909383 4.575561
    0.3      validation_swap_selected gls_map 2.690246 4.246606
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.254824      0.256575 210
    gsp   condition_number     0.255157      0.254891 210
    gsp information_logdet    -0.209109     -0.228138 210
gls_map    posterior_trace     0.893445      0.903942 210
gls_map   condition_number     0.889037      0.905136 210
gls_map information_logdet    -0.806612     -0.847489 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv