---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-09, 2015-01-10
Test days: 2015-01-23, 2015-01-25
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.279553       NaN   5.503335       NaN  0.097112       NaN
                                     gsp                  4.549367       NaN   7.335840       NaN  0.136897       NaN
                                     historical_tod_mean  6.631890       NaN  10.147426       NaN  0.193355       NaN
                                     neighbor_average     5.397053       NaN   9.120909       NaN  0.182018       NaN
       best_random_by_validation     gls_map              3.212863       NaN   5.345873       NaN  0.089686       NaN
                                     gsp                  4.509757       NaN   7.204849       NaN  0.131049       NaN
                                     historical_tod_mean  6.538059       NaN   9.975708       NaN  0.185369       NaN
                                     neighbor_average     5.302175       NaN   8.650453       NaN  0.151234       NaN
       coverage                      gls_map              3.272579       NaN   5.473160       NaN  0.095098       NaN
                                     gsp                  4.535090       NaN   7.297604       NaN  0.134760       NaN
                                     historical_tod_mean  6.595547       NaN  10.091839       NaN  0.190962       NaN
                                     neighbor_average     5.322644       NaN   8.465263       NaN  0.165656       NaN
       degree                        gls_map              3.622115       NaN   5.927628       NaN  0.104755       NaN
                                     gsp                  4.458591       NaN   7.121490       NaN  0.130983       NaN
                                     historical_tod_mean  6.506682       NaN   9.998837       NaN  0.188888       NaN
                                     neighbor_average     6.114638       NaN  10.016371       NaN  0.192287       NaN
       graph_sampling_laplacian      gls_map              3.905070       NaN   6.431649       NaN  0.117155       NaN
                                     gsp                  4.623146       NaN   7.453721       NaN  0.141544       NaN
                                     historical_tod_mean  6.653009       NaN  10.191268       NaN  0.195383       NaN
                                     neighbor_average     6.365392       NaN  10.873683       NaN  0.206670       NaN
       greedy_a_trace                gls_map              3.060085       NaN   5.132841       NaN  0.088638       NaN
                                     gsp                  4.485189       NaN   7.268793       NaN  0.133911       NaN
                                     historical_tod_mean  6.550431       NaN  10.018355       NaN  0.189565       NaN
                                     neighbor_average     5.501907       NaN   8.751142       NaN  0.166273       NaN
       greedy_d_logdet               gls_map              3.864484       NaN   6.181268       NaN  0.113902       NaN
                                     gsp                  4.875637       NaN   7.909025       NaN  0.149636       NaN
                                     historical_tod_mean  6.789620       NaN  10.283230       NaN  0.197307       NaN
                                     neighbor_average     6.267890       NaN  10.820729       NaN  0.229315       NaN
       multistart_swap_by_validation gls_map              3.105530       NaN   5.136527       NaN  0.088216       NaN
                                     gsp                  4.498843       NaN   7.242272       NaN  0.133330       NaN
                                     historical_tod_mean  6.551912       NaN  10.014431       NaN  0.189459       NaN
                                     neighbor_average     5.359459       NaN   8.656288       NaN  0.168906       NaN
       observability_proxy           gls_map              3.572946       NaN   5.883768       NaN  0.103372       NaN
                                     gsp                  4.498454       NaN   7.199324       NaN  0.132720       NaN
                                     historical_tod_mean  6.531020       NaN  10.028786       NaN  0.190329       NaN
                                     neighbor_average     6.033468       NaN   9.960327       NaN  0.183320       NaN
       qr_pod_modes                  gls_map              3.429714       NaN   5.645353       NaN  0.100990       NaN
                                     gsp                  4.533814       NaN   7.353206       NaN  0.136395       NaN
                                     historical_tod_mean  6.651284       NaN  10.150843       NaN  0.193169       NaN
                                     neighbor_average     5.854396       NaN   9.825748       NaN  0.197716       NaN
       random                        gls_map              3.301504  0.067447   5.504212  0.116485  0.096311  0.003514
                                     gsp                  4.473404  0.042927   7.208414  0.079007  0.133677  0.002463
                                     historical_tod_mean  6.540274  0.033120  10.016784  0.049679  0.189323  0.002145
                                     neighbor_average     5.583615  0.236427   9.122310  0.309930  0.169915  0.007072
       rcss_selected                 gls_map              3.076403       NaN   5.139671       NaN  0.089179       NaN
                                     gsp                  4.544690       NaN   7.362571       NaN  0.136660       NaN
                                     historical_tod_mean  6.578879       NaN  10.056900       NaN  0.190885       NaN
                                     neighbor_average     5.596731       NaN   8.867243       NaN  0.174633       NaN
       robust_coverage_cvar          gls_map              3.200210       NaN   5.415257       NaN  0.095989       NaN
                                     gsp                  4.512278       NaN   7.311779       NaN  0.136288       NaN
                                     historical_tod_mean  6.612964       NaN  10.082750       NaN  0.191230       NaN
                                     neighbor_average     5.511012       NaN   9.208068       NaN  0.185881       NaN
       scenario_average_a_trace      gls_map              3.154660       NaN   5.307915       NaN  0.092933       NaN
                                     gsp                  4.496547       NaN   7.289016       NaN  0.134821       NaN
                                     historical_tod_mean  6.585570       NaN  10.048652       NaN  0.190084       NaN
                                     neighbor_average     5.615898       NaN   9.139251       NaN  0.182820       NaN
       scenario_cvar_a_trace         gls_map              3.196936       NaN   5.363576       NaN  0.095388       NaN
                                     gsp                  4.527711       NaN   7.328303       NaN  0.135632       NaN
                                     historical_tod_mean  6.624858       NaN  10.088968       NaN  0.191087       NaN
                                     neighbor_average     6.057841       NaN  10.010116       NaN  0.192894       NaN
       swap_from_best_random_trace   gls_map              3.076403       NaN   5.139671       NaN  0.089179       NaN
                                     gsp                  4.544690       NaN   7.362571       NaN  0.136660       NaN
                                     historical_tod_mean  6.578879       NaN  10.056900       NaN  0.190885       NaN
                                     neighbor_average     5.596731       NaN   8.867243       NaN  0.174633       NaN
       swap_from_greedy_a_trace      gls_map              3.088671       NaN   5.138481       NaN  0.087450       NaN
                                     gsp                  4.529747       NaN   7.319520       NaN  0.133822       NaN
                                     historical_tod_mean  6.577205       NaN  10.034157       NaN  0.188547       NaN
                                     neighbor_average     5.719559       NaN   9.004949       NaN  0.171006       NaN
       swap_from_scenario_average    gls_map              3.113486       NaN   5.166724       NaN  0.088191       NaN
                                     gsp                  4.524361       NaN   7.318425       NaN  0.134343       NaN
                                     historical_tod_mean  6.577432       NaN  10.038353       NaN  0.189143       NaN
                                     neighbor_average     5.657813       NaN   8.965246       NaN  0.173179       NaN
       swap_from_scenario_cvar       gls_map              3.156320       NaN   5.182138       NaN  0.088923       NaN
                                     gsp                  4.549853       NaN   7.331684       NaN  0.134307       NaN
                                     historical_tod_mean  6.598968       NaN  10.060747       NaN  0.189876       NaN
                                     neighbor_average     5.549888       NaN   8.742099       NaN  0.168980       NaN
       top_variance                  gls_map              3.530254       NaN   5.587393       NaN  0.093849       NaN
                                     gsp                  4.327368       NaN   6.742845       NaN  0.117664       NaN
                                     historical_tod_mean  6.054678       NaN   9.206083       NaN  0.160759       NaN
                                     neighbor_average     8.532889       NaN  13.867219       NaN  0.179909       NaN
       validation_swap_selected      gls_map              3.099870       NaN   5.106179       NaN  0.087551       NaN
                                     gsp                  4.498762       NaN   7.251923       NaN  0.133780       NaN
                                     historical_tod_mean  6.522123       NaN   9.990883       NaN  0.188851       NaN
                                     neighbor_average     5.409478       NaN   8.638140       NaN  0.162730       NaN
0.2    best_random_by_trace          gls_map              3.022380       NaN   5.065290       NaN  0.084061       NaN
                                     gsp                  4.347498       NaN   6.826156       NaN  0.123432       NaN
                                     historical_tod_mean  6.540108       NaN  10.009201       NaN  0.187555       NaN
                                     neighbor_average     4.867260       NaN   8.222521       NaN  0.149183       NaN
       best_random_by_validation     gls_map              2.896802       NaN   4.839970       NaN  0.082606       NaN
                                     gsp                  4.306925       NaN   6.810419       NaN  0.124408       NaN
                                     historical_tod_mean  6.481282       NaN   9.914778       NaN  0.185157       NaN
                                     neighbor_average     4.880694       NaN   7.911860       NaN  0.137656       NaN
       coverage                      gls_map              2.854469       NaN   4.799393       NaN  0.083395       NaN
                                     gsp                  4.344003       NaN   6.930645       NaN  0.129296       NaN
                                     historical_tod_mean  6.595747       NaN  10.080510       NaN  0.192201       NaN
                                     neighbor_average     4.480313       NaN   7.235590       NaN  0.137940       NaN
       degree                        gls_map              3.473535       NaN   5.782750       NaN  0.102750       NaN
                                     gsp                  4.445256       NaN   7.054306       NaN  0.131026       NaN
                                     historical_tod_mean  6.589420       NaN  10.133868       NaN  0.194181       NaN
                                     neighbor_average     6.248422       NaN  10.231451       NaN  0.195702       NaN
       graph_sampling_laplacian      gls_map              3.652369       NaN   6.092066       NaN  0.107999       NaN
                                     gsp                  4.498308       NaN   7.080339       NaN  0.132096       NaN
                                     historical_tod_mean  6.685878       NaN  10.227060       NaN  0.196470       NaN
                                     neighbor_average     6.144363       NaN  10.397061       NaN  0.203978       NaN
       greedy_a_trace                gls_map              2.838312       NaN   4.738382       NaN  0.082394       NaN
                                     gsp                  4.443330       NaN   7.112492       NaN  0.133003       NaN
                                     historical_tod_mean  6.729657       NaN  10.242421       NaN  0.196485       NaN
                                     neighbor_average     4.780084       NaN   7.845857       NaN  0.159296       NaN
       greedy_d_logdet               gls_map              3.417596       NaN   5.554380       NaN  0.102924       NaN
                                     gsp                  4.626879       NaN   7.372605       NaN  0.140657       NaN
                                     historical_tod_mean  6.972135       NaN  10.507159       NaN  0.205223       NaN
                                     neighbor_average     5.653715       NaN   9.867545       NaN  0.213735       NaN
       multistart_swap_by_validation gls_map              2.857253       NaN   4.720369       NaN  0.081702       NaN
                                     gsp                  4.407872       NaN   7.012643       NaN  0.131195       NaN
                                     historical_tod_mean  6.664955       NaN  10.151994       NaN  0.193124       NaN
                                     neighbor_average     4.720653       NaN   7.676560       NaN  0.149524       NaN
       observability_proxy           gls_map              3.362580       NaN   5.643073       NaN  0.098801       NaN
                                     gsp                  4.432870       NaN   7.062020       NaN  0.130553       NaN
                                     historical_tod_mean  6.576722       NaN  10.115887       NaN  0.193225       NaN
                                     neighbor_average     6.218935       NaN  10.221522       NaN  0.189134       NaN
       qr_pod_modes                  gls_map              3.010374       NaN   4.949674       NaN  0.086848       NaN
                                     gsp                  4.475297       NaN   7.093219       NaN  0.133134       NaN
                                     historical_tod_mean  6.759221       NaN  10.236682       NaN  0.195953       NaN
                                     neighbor_average     4.851124       NaN   8.140511       NaN  0.165087       NaN
       random                        gls_map              2.980593  0.057000   4.997199  0.118614  0.085489  0.003402
                                     gsp                  4.342423  0.043030   6.878725  0.083719  0.126969  0.003356
                                     historical_tod_mean  6.534137  0.062015  10.005852  0.096738  0.188883  0.003958
                                     neighbor_average     4.978175  0.164973   8.153818  0.307332  0.145985  0.008864
       rcss_selected                 gls_map              2.808088       NaN   4.656484       NaN  0.077500       NaN
                                     gsp                  4.260889       NaN   6.746093       NaN  0.124177       NaN
                                     historical_tod_mean  6.415656       NaN   9.859139       NaN  0.184637       NaN
                                     neighbor_average     4.716507       NaN   7.565728       NaN  0.131171       NaN
       robust_coverage_cvar          gls_map              2.932577       NaN   4.935930       NaN  0.084444       NaN
                                     gsp                  4.433962       NaN   7.032197       NaN  0.129363       NaN
                                     historical_tod_mean  6.697640       NaN  10.180407       NaN  0.193095       NaN
                                     neighbor_average     4.724860       NaN   7.783801       NaN  0.152297       NaN
       scenario_average_a_trace      gls_map              2.971137       NaN   5.000442       NaN  0.087763       NaN
                                     gsp                  4.442933       NaN   7.075001       NaN  0.131516       NaN
                                     historical_tod_mean  6.730928       NaN  10.225574       NaN  0.195253       NaN
                                     neighbor_average     5.078877       NaN   8.384433       NaN  0.165833       NaN
       scenario_cvar_a_trace         gls_map              2.986301       NaN   4.999978       NaN  0.088272       NaN
                                     gsp                  4.456923       NaN   7.062049       NaN  0.131369       NaN
                                     historical_tod_mean  6.755569       NaN  10.249372       NaN  0.195835       NaN
                                     neighbor_average     5.053597       NaN   8.420384       NaN  0.164943       NaN
       swap_from_best_random_trace   gls_map              2.876941       NaN   4.703024       NaN  0.081109       NaN
                                     gsp                  4.442815       NaN   7.022305       NaN  0.130838       NaN
                                     historical_tod_mean  6.707772       NaN  10.195825       NaN  0.194393       NaN
                                     neighbor_average     4.661569       NaN   7.564914       NaN  0.151801       NaN
       swap_from_greedy_a_trace      gls_map              2.843152       NaN   4.706844       NaN  0.082508       NaN
                                     gsp                  4.451254       NaN   7.094025       NaN  0.133319       NaN
                                     historical_tod_mean  6.739819       NaN  10.227607       NaN  0.195616       NaN
                                     neighbor_average     4.607651       NaN   7.661442       NaN  0.155251       NaN
       swap_from_scenario_average    gls_map              2.895261       NaN   4.760911       NaN  0.082300       NaN
                                     gsp                  4.408653       NaN   6.988586       NaN  0.129684       NaN
                                     historical_tod_mean  6.701264       NaN  10.175912       NaN  0.194300       NaN
                                     neighbor_average     4.814110       NaN   7.956165       NaN  0.159644       NaN
       swap_from_scenario_cvar       gls_map              2.858535       NaN   4.720359       NaN  0.080856       NaN
                                     gsp                  4.429941       NaN   7.038713       NaN  0.130564       NaN
                                     historical_tod_mean  6.728380       NaN  10.211092       NaN  0.193826       NaN
                                     neighbor_average     4.868835       NaN   7.941590       NaN  0.156713       NaN
       top_variance                  gls_map              3.120089       NaN   5.035887       NaN  0.079093       NaN
                                     gsp                  4.009890       NaN   6.160426       NaN  0.100293       NaN
                                     historical_tod_mean  5.727443       NaN   8.630261       NaN  0.140467       NaN
                                     neighbor_average     7.089694       NaN  11.809349       NaN  0.143951       NaN
       validation_swap_selected      gls_map              2.790083       NaN   4.628681       NaN  0.077104       NaN
                                     gsp                  4.239944       NaN   6.730527       NaN  0.123616       NaN
                                     historical_tod_mean  6.387619       NaN   9.833395       NaN  0.183946       NaN
                                     neighbor_average     4.721400       NaN   7.558801       NaN  0.133849       NaN
0.3    best_random_by_trace          gls_map              2.774065       NaN   4.610034       NaN  0.078616       NaN
                                     gsp                  4.355751       NaN   6.836403       NaN  0.127096       NaN
                                     historical_tod_mean  6.627710       NaN  10.095471       NaN  0.192081       NaN
                                     neighbor_average     4.574277       NaN   7.439112       NaN  0.135459       NaN
       best_random_by_validation     gls_map              2.724423       NaN   4.519366       NaN  0.075470       NaN
                                     gsp                  4.290688       NaN   6.681221       NaN  0.120745       NaN
                                     historical_tod_mean  6.419664       NaN   9.872823       NaN  0.184710       NaN
                                     neighbor_average     4.399130       NaN   7.127346       NaN  0.129504       NaN
       coverage                      gls_map              2.647921       NaN   4.450263       NaN  0.076166       NaN
                                     gsp                  4.335806       NaN   6.838300       NaN  0.127058       NaN
                                     historical_tod_mean  6.563971       NaN  10.066884       NaN  0.191937       NaN
                                     neighbor_average     4.393567       NaN   6.946231       NaN  0.126150       NaN
       degree                        gls_map              3.348170       NaN   5.637481       NaN  0.097881       NaN
                                     gsp                  4.444500       NaN   7.079392       NaN  0.129636       NaN
                                     historical_tod_mean  6.670814       NaN  10.190037       NaN  0.192613       NaN
                                     neighbor_average     6.991594       NaN  11.551150       NaN  0.193623       NaN
       graph_sampling_laplacian      gls_map              3.476304       NaN   5.873190       NaN  0.101331       NaN
                                     gsp                  4.441059       NaN   6.962053       NaN  0.129105       NaN
                                     historical_tod_mean  6.609946       NaN  10.131156       NaN  0.194076       NaN
                                     neighbor_average     6.446860       NaN  10.821293       NaN  0.209299       NaN
       greedy_a_trace                gls_map              2.695744       NaN   4.464303       NaN  0.077458       NaN
                                     gsp                  4.466993       NaN   7.060136       NaN  0.132833       NaN
                                     historical_tod_mean  6.873580       NaN  10.397627       NaN  0.201071       NaN
                                     neighbor_average     4.388787       NaN   7.245347       NaN  0.146342       NaN
       greedy_d_logdet               gls_map              3.116552       NaN   5.102102       NaN  0.094581       NaN
                                     gsp                  4.615231       NaN   7.225021       NaN  0.139834       NaN
                                     historical_tod_mean  7.076685       NaN  10.643700       NaN  0.210315       NaN
                                     neighbor_average     5.282327       NaN   9.042303       NaN  0.192610       NaN
       multistart_swap_by_validation gls_map              2.709559       NaN   4.491397       NaN  0.078090       NaN
                                     gsp                  4.406215       NaN   6.886647       NaN  0.128442       NaN
                                     historical_tod_mean  6.698665       NaN  10.225349       NaN  0.196202       NaN
                                     neighbor_average     4.482665       NaN   7.231378       NaN  0.143799       NaN
       observability_proxy           gls_map              3.343711       NaN   5.611764       NaN  0.097231       NaN
                                     gsp                  4.444506       NaN   7.089779       NaN  0.129778       NaN
                                     historical_tod_mean  6.677773       NaN  10.194051       NaN  0.192565       NaN
                                     neighbor_average     6.874957       NaN  11.384025       NaN  0.191682       NaN
       qr_pod_modes                  gls_map              2.777842       NaN   4.647182       NaN  0.082488       NaN
                                     gsp                  4.505577       NaN   7.108489       NaN  0.134552       NaN
                                     historical_tod_mean  6.914888       NaN  10.446780       NaN  0.202303       NaN
                                     neighbor_average     4.543873       NaN   7.530770       NaN  0.152411       NaN
       random                        gls_map              2.821895  0.046800   4.722062  0.106261  0.080317  0.003110
                                     gsp                  4.335845  0.048844   6.804577  0.083770  0.125688  0.003198
                                     historical_tod_mean  6.549681  0.083357  10.026963  0.109516  0.189740  0.004238
                                     neighbor_average     4.628555  0.129933   7.563406  0.244188  0.134093  0.007644
       rcss_selected                 gls_map              2.635731       NaN   4.320613       NaN  0.070859       NaN
                                     gsp                  4.213970       NaN   6.554877       NaN  0.117856       NaN
                                     historical_tod_mean  6.317295       NaN   9.705602       NaN  0.179295       NaN
                                     neighbor_average     4.679395       NaN   7.719165       NaN  0.118990       NaN
       robust_coverage_cvar          gls_map              2.805656       NaN   4.703805       NaN  0.080907       NaN
                                     gsp                  4.486242       NaN   7.072802       NaN  0.131838       NaN
                                     historical_tod_mean  6.900958       NaN  10.405047       NaN  0.199499       NaN
                                     neighbor_average     4.386562       NaN   7.125477       NaN  0.140349       NaN
       scenario_average_a_trace      gls_map              2.856845       NaN   4.799132       NaN  0.084339       NaN
                                     gsp                  4.507128       NaN   7.071357       NaN  0.132968       NaN
                                     historical_tod_mean  6.907779       NaN  10.449959       NaN  0.201945       NaN
                                     neighbor_average     4.758858       NaN   7.917733       NaN  0.161938       NaN
       scenario_cvar_a_trace         gls_map              2.905235       NaN   4.844868       NaN  0.086928       NaN
                                     gsp                  4.533142       NaN   7.134475       NaN  0.136517       NaN
                                     historical_tod_mean  7.000216       NaN  10.535978       NaN  0.205724       NaN
                                     neighbor_average     4.718568       NaN   7.935918       NaN  0.162216       NaN
       swap_from_best_random_trace   gls_map              2.699508       NaN   4.455297       NaN  0.076976       NaN
                                     gsp                  4.435339       NaN   6.978257       NaN  0.131135       NaN
                                     historical_tod_mean  6.815020       NaN  10.306344       NaN  0.198260       NaN
                                     neighbor_average     4.263481       NaN   6.920525       NaN  0.134151       NaN
       swap_from_greedy_a_trace      gls_map              2.715796       NaN   4.451229       NaN  0.075278       NaN
                                     gsp                  4.490771       NaN   7.051261       NaN  0.131362       NaN
                                     historical_tod_mean  6.924012       NaN  10.413162       NaN  0.199832       NaN
                                     neighbor_average     4.406269       NaN   7.149318       NaN  0.141637       NaN
       swap_from_scenario_average    gls_map              2.715809       NaN   4.443575       NaN  0.076409       NaN
                                     gsp                  4.465061       NaN   6.997960       NaN  0.130386       NaN
                                     historical_tod_mean  6.870322       NaN  10.350930       NaN  0.198091       NaN
                                     neighbor_average     4.387661       NaN   7.095062       NaN  0.139506       NaN
       swap_from_scenario_cvar       gls_map              2.725942       NaN   4.489637       NaN  0.078478       NaN
                                     gsp                  4.475113       NaN   7.044474       NaN  0.131765       NaN
                                     historical_tod_mean  6.888932       NaN  10.396104       NaN  0.199562       NaN
                                     neighbor_average     4.429127       NaN   7.185891       NaN  0.141571       NaN
       top_variance                  gls_map              2.876536       NaN   4.661312       NaN  0.069443       NaN
                                     gsp                  3.804580       NaN   5.831204       NaN  0.090629       NaN
                                     historical_tod_mean  5.491431       NaN   8.220776       NaN  0.128082       NaN
                                     neighbor_average     5.997982       NaN  10.045207       NaN  0.122429       NaN
       validation_swap_selected      gls_map              2.620318       NaN   4.288467       NaN  0.071615       NaN
                                     gsp                  4.172699       NaN   6.538220       NaN  0.118267       NaN
                                     historical_tod_mean  6.323528       NaN   9.699272       NaN  0.179912       NaN
                                     neighbor_average     4.461427       NaN   7.200518       NaN  0.117767       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1           greedy_a_trace gls_map 3.060085 5.132841
    0.2 validation_swap_selected gls_map 2.790083 4.628681
    0.3 validation_swap_selected gls_map 2.620318 4.288467
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.580189      0.504918 210
    gsp   condition_number     0.580551      0.530450 210
    gsp information_logdet    -0.519595     -0.526199 210
gls_map    posterior_trace     0.905453      0.897954 210
gls_map   condition_number     0.901394      0.918959 210
gls_map information_logdet    -0.806730     -0.837255 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv