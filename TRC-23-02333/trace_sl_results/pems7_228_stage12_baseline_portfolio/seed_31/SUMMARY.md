---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-25, 2012-06-06
Test days: 2012-06-01, 2012-06-08
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               4.256074       NaN   7.405726       NaN  0.114800       NaN
                                     gsp                   4.430325       NaN   7.853011       NaN  0.127395       NaN
                                     historical_tod_mean   4.444864       NaN   8.127632       NaN  0.137850       NaN
                                     neighbor_average      8.392549       NaN  12.883626       NaN  0.237845       NaN
       best_random_by_validation     gls_map               4.097987       NaN   7.302122       NaN  0.119998       NaN
                                     gsp                   4.401277       NaN   7.853284       NaN  0.133181       NaN
                                     historical_tod_mean   4.420464       NaN   8.157176       NaN  0.139642       NaN
                                     neighbor_average      8.520825       NaN  12.313080       NaN  0.241666       NaN
       coverage                      gls_map               4.333625       NaN   7.679311       NaN  0.130758       NaN
                                     gsp                   4.452162       NaN   7.919315       NaN  0.135013       NaN
                                     historical_tod_mean   4.477443       NaN   8.242350       NaN  0.142880       NaN
                                     neighbor_average      8.609592       NaN  13.145181       NaN  0.262002       NaN
       degree                        gls_map               4.523435       NaN   8.036648       NaN  0.131398       NaN
                                     gsp                   4.549826       NaN   8.096123       NaN  0.138335       NaN
                                     historical_tod_mean   4.543091       NaN   8.324835       NaN  0.144862       NaN
                                     neighbor_average      9.240295       NaN  14.051216       NaN  0.283703       NaN
       graph_sampling_laplacian      gls_map               5.271090       NaN   8.905581       NaN  0.133608       NaN
                                     gsp                   4.673534       NaN   8.045763       NaN  0.124442       NaN
                                     historical_tod_mean   4.369931       NaN   7.952345       NaN  0.128133       NaN
                                     neighbor_average     10.950086       NaN  16.617474       NaN  0.271270       NaN
       greedy_a_trace                gls_map               4.146897       NaN   7.072286       NaN  0.114518       NaN
                                     gsp                   4.433586       NaN   7.862241       NaN  0.132507       NaN
                                     historical_tod_mean   4.472795       NaN   8.168206       NaN  0.140965       NaN
                                     neighbor_average      8.175249       NaN  12.481981       NaN  0.251581       NaN
       greedy_d_logdet               gls_map               5.033460       NaN   8.093148       NaN  0.137163       NaN
                                     gsp                   4.532647       NaN   7.972690       NaN  0.134493       NaN
                                     historical_tod_mean   4.482565       NaN   8.174062       NaN  0.138687       NaN
                                     neighbor_average      8.933215       NaN  14.467552       NaN  0.304380       NaN
       multistart_swap_by_validation gls_map               4.035734       NaN   6.867650       NaN  0.114600       NaN
                                     gsp                   4.377405       NaN   7.807067       NaN  0.133713       NaN
                                     historical_tod_mean   4.444259       NaN   8.104664       NaN  0.141209       NaN
                                     neighbor_average      7.894177       NaN  12.237037       NaN  0.250495       NaN
       observability_proxy           gls_map               4.377089       NaN   7.761232       NaN  0.126164       NaN
                                     gsp                   4.480431       NaN   8.028427       NaN  0.138940       NaN
                                     historical_tod_mean   4.513175       NaN   8.275542       NaN  0.143869       NaN
                                     neighbor_average      8.979792       NaN  13.790950       NaN  0.276837       NaN
       qr_pod_modes                  gls_map               4.483486       NaN   7.475357       NaN  0.120892       NaN
                                     gsp                   4.510013       NaN   7.864922       NaN  0.129564       NaN
                                     historical_tod_mean   4.469318       NaN   8.107741       NaN  0.135974       NaN
                                     neighbor_average      8.043364       NaN  13.174874       NaN  0.276013       NaN
       random                        gls_map               4.295638  0.110562   7.412711  0.151795  0.120856  0.005417
                                     gsp                   4.417144  0.064816   7.831727  0.079327  0.130209  0.003895
                                     historical_tod_mean   4.426872  0.039657   8.121694  0.071100  0.138682  0.002978
                                     neighbor_average      8.389370  0.273757  12.698393  0.364421  0.239421  0.013943
       rcss_selected                 gls_map               4.017953       NaN   6.896156       NaN  0.109477       NaN
                                     gsp                   4.379532       NaN   7.826129       NaN  0.131178       NaN
                                     historical_tod_mean   4.448015       NaN   8.114842       NaN  0.140325       NaN
                                     neighbor_average      8.031043       NaN  12.411135       NaN  0.247070       NaN
       robust_coverage_cvar          gls_map               4.232199       NaN   7.403023       NaN  0.120929       NaN
                                     gsp                   4.403163       NaN   7.854702       NaN  0.130910       NaN
                                     historical_tod_mean   4.439324       NaN   8.153853       NaN  0.140324       NaN
                                     neighbor_average      7.903161       NaN  12.021282       NaN  0.241354       NaN
       scenario_average_a_trace      gls_map               4.155916       NaN   7.302437       NaN  0.115610       NaN
                                     gsp                   4.452574       NaN   7.950934       NaN  0.131304       NaN
                                     historical_tod_mean   4.506971       NaN   8.230012       NaN  0.142277       NaN
                                     neighbor_average      8.094607       NaN  12.105809       NaN  0.236518       NaN
       scenario_cvar_a_trace         gls_map               4.172953       NaN   7.159009       NaN  0.116726       NaN
                                     gsp                   4.370254       NaN   7.886038       NaN  0.134466       NaN
                                     historical_tod_mean   4.439066       NaN   8.137654       NaN  0.140941       NaN
                                     neighbor_average      8.458509       NaN  12.671927       NaN  0.254841       NaN
       swap_from_best_random_trace   gls_map               4.008176       NaN   6.863774       NaN  0.111625       NaN
                                     gsp                   4.380700       NaN   7.854317       NaN  0.132991       NaN
                                     historical_tod_mean   4.472149       NaN   8.143662       NaN  0.141610       NaN
                                     neighbor_average      8.132956       NaN  12.601570       NaN  0.257276       NaN
       swap_from_greedy_a_trace      gls_map               3.974061       NaN   6.847322       NaN  0.109038       NaN
                                     gsp                   4.395491       NaN   7.895814       NaN  0.132632       NaN
                                     historical_tod_mean   4.483703       NaN   8.186952       NaN  0.141378       NaN
                                     neighbor_average      8.053804       NaN  12.291125       NaN  0.245596       NaN
       swap_from_scenario_average    gls_map               3.988103       NaN   6.882758       NaN  0.110072       NaN
                                     gsp                   4.393391       NaN   7.889352       NaN  0.133216       NaN
                                     historical_tod_mean   4.480696       NaN   8.165177       NaN  0.141542       NaN
                                     neighbor_average      8.035210       NaN  12.541174       NaN  0.249924       NaN
       swap_from_scenario_cvar       gls_map               4.017953       NaN   6.896156       NaN  0.109477       NaN
                                     gsp                   4.379532       NaN   7.826129       NaN  0.131178       NaN
                                     historical_tod_mean   4.448015       NaN   8.114842       NaN  0.140325       NaN
                                     neighbor_average      8.031043       NaN  12.411135       NaN  0.247070       NaN
       top_variance                  gls_map               4.150546       NaN   7.404124       NaN  0.121631       NaN
                                     gsp                   4.191615       NaN   7.609405       NaN  0.124609       NaN
                                     historical_tod_mean   4.242138       NaN   7.897528       NaN  0.130024       NaN
                                     neighbor_average     12.490436       NaN  18.483129       NaN  0.252850       NaN
       validation_swap_selected      gls_map               4.027530       NaN   7.223080       NaN  0.119883       NaN
                                     gsp                   4.427992       NaN   7.944229       NaN  0.137617       NaN
                                     historical_tod_mean   4.428378       NaN   8.147516       NaN  0.141653       NaN
                                     neighbor_average      8.068076       NaN  12.707010       NaN  0.265842       NaN
0.2    best_random_by_trace          gls_map               3.852551       NaN   6.618490       NaN  0.104307       NaN
                                     gsp                   4.379827       NaN   7.735224       NaN  0.123639       NaN
                                     historical_tod_mean   4.420370       NaN   8.102483       NaN  0.135954       NaN
                                     neighbor_average      8.008759       NaN  12.154004       NaN  0.226634       NaN
       best_random_by_validation     gls_map               3.911844       NaN   6.755788       NaN  0.114322       NaN
                                     gsp                   4.316799       NaN   7.756406       NaN  0.134577       NaN
                                     historical_tod_mean   4.392084       NaN   8.087426       NaN  0.141996       NaN
                                     neighbor_average      7.789873       NaN  11.785831       NaN  0.229358       NaN
       coverage                      gls_map               4.091650       NaN   7.424151       NaN  0.127267       NaN
                                     gsp                   4.491486       NaN   8.090466       NaN  0.141187       NaN
                                     historical_tod_mean   4.561454       NaN   8.439697       NaN  0.149063       NaN
                                     neighbor_average      7.988642       NaN  12.071555       NaN  0.246536       NaN
       degree                        gls_map               4.550588       NaN   8.082770       NaN  0.132103       NaN
                                     gsp                   4.599545       NaN   8.193511       NaN  0.140389       NaN
                                     historical_tod_mean   4.665217       NaN   8.483007       NaN  0.148112       NaN
                                     neighbor_average      8.757299       NaN  13.405039       NaN  0.256765       NaN
       graph_sampling_laplacian      gls_map               4.922758       NaN   8.108264       NaN  0.123045       NaN
                                     gsp                   4.582322       NaN   7.870655       NaN  0.118848       NaN
                                     historical_tod_mean   4.255566       NaN   7.799306       NaN  0.122781       NaN
                                     neighbor_average      8.533290       NaN  12.433051       NaN  0.242159       NaN
       greedy_a_trace                gls_map               4.025550       NaN   6.697975       NaN  0.108889       NaN
                                     gsp                   4.517554       NaN   7.906797       NaN  0.138085       NaN
                                     historical_tod_mean   4.539378       NaN   8.258085       NaN  0.146202       NaN
                                     neighbor_average      7.885589       NaN  12.258536       NaN  0.259504       NaN
       greedy_d_logdet               gls_map               4.811117       NaN   7.789309       NaN  0.135890       NaN
                                     gsp                   4.630357       NaN   8.060940       NaN  0.137360       NaN
                                     historical_tod_mean   4.605366       NaN   8.353432       NaN  0.144725       NaN
                                     neighbor_average      8.824079       NaN  13.937238       NaN  0.303676       NaN
       multistart_swap_by_validation gls_map               3.914826       NaN   6.454078       NaN  0.103318       NaN
                                     gsp                   4.331280       NaN   7.638784       NaN  0.129572       NaN
                                     historical_tod_mean   4.360368       NaN   7.998862       NaN  0.138382       NaN
                                     neighbor_average      7.698286       NaN  11.835003       NaN  0.242660       NaN
       observability_proxy           gls_map               4.447932       NaN   7.816418       NaN  0.127938       NaN
                                     gsp                   4.620860       NaN   8.194954       NaN  0.142406       NaN
                                     historical_tod_mean   4.657729       NaN   8.508971       NaN  0.150387       NaN
                                     neighbor_average      9.295880       NaN  13.694518       NaN  0.275264       NaN
       qr_pod_modes                  gls_map               4.239362       NaN   7.065483       NaN  0.120539       NaN
                                     gsp                   4.438169       NaN   7.819452       NaN  0.130754       NaN
                                     historical_tod_mean   4.457871       NaN   8.150692       NaN  0.139589       NaN
                                     neighbor_average      8.171762       NaN  12.870077       NaN  0.271725       NaN
       random                        gls_map               4.000963  0.097613   6.887003  0.195370  0.110648  0.006383
                                     gsp                   4.404216  0.065435   7.777969  0.109524  0.129207  0.004839
                                     historical_tod_mean   4.432884  0.062022   8.123968  0.105267  0.139129  0.004306
                                     neighbor_average      8.071575  0.222031  12.329076  0.359565  0.229577  0.011970
       rcss_selected                 gls_map               3.914826       NaN   6.454078       NaN  0.103318       NaN
                                     gsp                   4.331280       NaN   7.638784       NaN  0.129572       NaN
                                     historical_tod_mean   4.360368       NaN   7.998862       NaN  0.138382       NaN
                                     neighbor_average      7.698286       NaN  11.835003       NaN  0.242660       NaN
       robust_coverage_cvar          gls_map               3.776268       NaN   6.538071       NaN  0.102911       NaN
                                     gsp                   4.264271       NaN   7.698881       NaN  0.128232       NaN
                                     historical_tod_mean   4.334286       NaN   8.026209       NaN  0.137684       NaN
                                     neighbor_average      8.044407       NaN  12.091422       NaN  0.227430       NaN
       scenario_average_a_trace      gls_map               3.985548       NaN   6.930274       NaN  0.102966       NaN
                                     gsp                   4.488938       NaN   7.832957       NaN  0.127090       NaN
                                     historical_tod_mean   4.401666       NaN   8.092913       NaN  0.137944       NaN
                                     neighbor_average      8.134419       NaN  12.190651       NaN  0.228685       NaN
       scenario_cvar_a_trace         gls_map               3.953226       NaN   6.847201       NaN  0.105573       NaN
                                     gsp                   4.329360       NaN   7.647985       NaN  0.123617       NaN
                                     historical_tod_mean   4.356282       NaN   7.946547       NaN  0.132054       NaN
                                     neighbor_average      8.033673       NaN  12.107794       NaN  0.230914       NaN
       swap_from_best_random_trace   gls_map               3.996483       NaN   6.745078       NaN  0.109197       NaN
                                     gsp                   4.513821       NaN   7.979502       NaN  0.139059       NaN
                                     historical_tod_mean   4.549567       NaN   8.304605       NaN  0.147341       NaN
                                     neighbor_average      7.996822       NaN  12.491187       NaN  0.264917       NaN
       swap_from_greedy_a_trace      gls_map               3.955258       NaN   6.688443       NaN  0.106998       NaN
                                     gsp                   4.475881       NaN   7.916168       NaN  0.136581       NaN
                                     historical_tod_mean   4.529253       NaN   8.263583       NaN  0.146112       NaN
                                     neighbor_average      7.858737       NaN  12.375299       NaN  0.262279       NaN
       swap_from_scenario_average    gls_map               3.889178       NaN   6.611803       NaN  0.102457       NaN
                                     gsp                   4.432217       NaN   7.844245       NaN  0.131656       NaN
                                     historical_tod_mean   4.492431       NaN   8.194480       NaN  0.142694       NaN
                                     neighbor_average      8.002679       NaN  12.352588       NaN  0.248580       NaN
       swap_from_scenario_cvar       gls_map               3.890564       NaN   6.615122       NaN  0.106855       NaN
                                     gsp                   4.456502       NaN   7.878316       NaN  0.135935       NaN
                                     historical_tod_mean   4.524204       NaN   8.228538       NaN  0.145025       NaN
                                     neighbor_average      7.694732       NaN  11.964625       NaN  0.251045       NaN
       top_variance                  gls_map               3.959456       NaN   7.154931       NaN  0.114024       NaN
                                     gsp                   4.103152       NaN   7.498708       NaN  0.120227       NaN
                                     historical_tod_mean   4.107013       NaN   7.762301       NaN  0.124578       NaN
                                     neighbor_average     10.760989       NaN  16.332003       NaN  0.218798       NaN
       validation_swap_selected      gls_map               3.872361       NaN   6.425246       NaN  0.103203       NaN
                                     gsp                   4.300875       NaN   7.642096       NaN  0.129625       NaN
                                     historical_tod_mean   4.336008       NaN   7.991677       NaN  0.137986       NaN
                                     neighbor_average      7.742854       NaN  11.842922       NaN  0.237385       NaN
0.3    best_random_by_trace          gls_map               3.633409       NaN   6.230718       NaN  0.090543       NaN
                                     gsp                   4.366141       NaN   7.650112       NaN  0.122111       NaN
                                     historical_tod_mean   4.333058       NaN   7.950848       NaN  0.132641       NaN
                                     neighbor_average      7.768051       NaN  12.022504       NaN  0.209351       NaN
       best_random_by_validation     gls_map               3.536588       NaN   6.071043       NaN  0.093082       NaN
                                     gsp                   4.134770       NaN   7.362510       NaN  0.117855       NaN
                                     historical_tod_mean   4.119720       NaN   7.682603       NaN  0.126480       NaN
                                     neighbor_average      7.704593       NaN  11.894396       NaN  0.193572       NaN
       coverage                      gls_map               3.866038       NaN   6.897868       NaN  0.120723       NaN
                                     gsp                   4.465667       NaN   8.088492       NaN  0.142200       NaN
                                     historical_tod_mean   4.534867       NaN   8.484744       NaN  0.151548       NaN
                                     neighbor_average      7.779834       NaN  11.640949       NaN  0.237752       NaN
       degree                        gls_map               4.504888       NaN   7.813394       NaN  0.126176       NaN
                                     gsp                   4.555900       NaN   8.107238       NaN  0.136594       NaN
                                     historical_tod_mean   4.621995       NaN   8.461566       NaN  0.146417       NaN
                                     neighbor_average      9.141570       NaN  13.931765       NaN  0.273699       NaN
       graph_sampling_laplacian      gls_map               4.442376       NaN   7.461722       NaN  0.112266       NaN
                                     gsp                   4.433580       NaN   7.642536       NaN  0.116270       NaN
                                     historical_tod_mean   4.303811       NaN   7.844108       NaN  0.124783       NaN
                                     neighbor_average      8.019579       NaN  12.543845       NaN  0.227480       NaN
       greedy_a_trace                gls_map               3.885756       NaN   6.516398       NaN  0.106291       NaN
                                     gsp                   4.546629       NaN   7.926467       NaN  0.133380       NaN
                                     historical_tod_mean   4.603441       NaN   8.328628       NaN  0.145043       NaN
                                     neighbor_average      7.757203       NaN  12.040716       NaN  0.259319       NaN
       greedy_d_logdet               gls_map               4.603428       NaN   7.296244       NaN  0.123553       NaN
                                     gsp                   4.444178       NaN   7.803769       NaN  0.131725       NaN
                                     historical_tod_mean   4.433044       NaN   8.169717       NaN  0.141307       NaN
                                     neighbor_average      8.613511       NaN  13.453429       NaN  0.292577       NaN
       multistart_swap_by_validation gls_map               3.633733       NaN   6.194994       NaN  0.099616       NaN
                                     gsp                   4.314558       NaN   7.638313       NaN  0.130524       NaN
                                     historical_tod_mean   4.339161       NaN   8.035098       NaN  0.140973       NaN
                                     neighbor_average      7.538942       NaN  11.568046       NaN  0.227728       NaN
       observability_proxy           gls_map               4.418808       NaN   7.683174       NaN  0.123900       NaN
                                     gsp                   4.594439       NaN   8.129096       NaN  0.137509       NaN
                                     historical_tod_mean   4.631307       NaN   8.468178       NaN  0.146660       NaN
                                     neighbor_average      8.991291       NaN  13.065011       NaN  0.255992       NaN
       qr_pod_modes                  gls_map               3.845534       NaN   6.593460       NaN  0.106782       NaN
                                     gsp                   4.393918       NaN   7.848903       NaN  0.131481       NaN
                                     historical_tod_mean   4.485834       NaN   8.243283       NaN  0.143035       NaN
                                     neighbor_average      7.805821       NaN  12.046640       NaN  0.257050       NaN
       random                        gls_map               3.791021  0.109041   6.545753  0.203951  0.103425  0.005861
                                     gsp                   4.381917  0.073084   7.761279  0.122539  0.128494  0.005335
                                     historical_tod_mean   4.423159  0.083516   8.131133  0.133983  0.139097  0.005313
                                     neighbor_average      7.937218  0.232765  12.239916  0.374319  0.221002  0.013456
       rcss_selected                 gls_map               3.501278       NaN   6.116797       NaN  0.094996       NaN
                                     gsp                   4.198448       NaN   7.530727       NaN  0.119843       NaN
                                     historical_tod_mean   4.290997       NaN   7.951236       NaN  0.131391       NaN
                                     neighbor_average      7.839433       NaN  11.899076       NaN  0.218190       NaN
       robust_coverage_cvar          gls_map               3.549819       NaN   6.198242       NaN  0.095229       NaN
                                     gsp                   4.181668       NaN   7.530074       NaN  0.119791       NaN
                                     historical_tod_mean   4.258057       NaN   7.900240       NaN  0.130496       NaN
                                     neighbor_average      7.747922       NaN  11.594407       NaN  0.205730       NaN
       scenario_average_a_trace      gls_map               3.796447       NaN   6.657008       NaN  0.101114       NaN
                                     gsp                   4.423402       NaN   7.898161       NaN  0.131383       NaN
                                     historical_tod_mean   4.475446       NaN   8.271137       NaN  0.144078       NaN
                                     neighbor_average      7.842566       NaN  11.811399       NaN  0.229222       NaN
       scenario_cvar_a_trace         gls_map               3.664454       NaN   6.302549       NaN  0.099690       NaN
                                     gsp                   4.243746       NaN   7.508710       NaN  0.122371       NaN
                                     historical_tod_mean   4.290285       NaN   7.877213       NaN  0.132149       NaN
                                     neighbor_average      7.727725       NaN  11.684098       NaN  0.220941       NaN
       swap_from_best_random_trace   gls_map               3.755062       NaN   6.352848       NaN  0.097634       NaN
                                     gsp                   4.406273       NaN   7.763958       NaN  0.130660       NaN
                                     historical_tod_mean   4.452613       NaN   8.148212       NaN  0.142124       NaN
                                     neighbor_average      7.424104       NaN  11.359489       NaN  0.227909       NaN
       swap_from_greedy_a_trace      gls_map               3.783945       NaN   6.478375       NaN  0.101898       NaN
                                     gsp                   4.504273       NaN   7.935342       NaN  0.131019       NaN
                                     historical_tod_mean   4.581578       NaN   8.307789       NaN  0.143054       NaN
                                     neighbor_average      7.744144       NaN  12.104030       NaN  0.252632       NaN
       swap_from_scenario_average    gls_map               3.871336       NaN   6.588722       NaN  0.105190       NaN
                                     gsp                   4.522113       NaN   8.036846       NaN  0.138717       NaN
                                     historical_tod_mean   4.618016       NaN   8.426363       NaN  0.150501       NaN
                                     neighbor_average      7.737503       NaN  11.930393       NaN  0.249773       NaN
       swap_from_scenario_cvar       gls_map               3.691585       NaN   6.334828       NaN  0.100018       NaN
                                     gsp                   4.394613       NaN   7.797567       NaN  0.128545       NaN
                                     historical_tod_mean   4.475930       NaN   8.192008       NaN  0.139473       NaN
                                     neighbor_average      7.613867       NaN  11.715652       NaN  0.240076       NaN
       top_variance                  gls_map               3.688576       NaN   6.850260       NaN  0.106200       NaN
                                     gsp                   3.962483       NaN   7.350703       NaN  0.115111       NaN
                                     historical_tod_mean   3.960151       NaN   7.595477       NaN  0.119107       NaN
                                     neighbor_average     10.343917       NaN  15.752493       NaN  0.212842       NaN
       validation_swap_selected      gls_map               3.397652       NaN   5.997817       NaN  0.093023       NaN
                                     gsp                   4.140498       NaN   7.477841       NaN  0.119945       NaN
                                     historical_tod_mean   4.256624       NaN   7.910228       NaN  0.131142       NaN
                                     neighbor_average      7.520324       NaN  11.490941       NaN  0.216394       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 3.974061 6.847322
    0.2     robust_coverage_cvar gls_map 3.776268 6.538071
    0.3 validation_swap_selected gls_map 3.397652 5.997817
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.178622      0.217093 210
    gsp   condition_number     0.175713      0.143070 210
    gsp information_logdet    -0.207910     -0.238288 210
gls_map    posterior_trace     0.754966      0.798226 210
gls_map   condition_number     0.816692      0.868240 210
gls_map information_logdet    -0.651900     -0.750309 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv