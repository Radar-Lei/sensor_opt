---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-13, 2012-06-08
Test days: 2012-05-07, 2012-05-30
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.427969       NaN   5.919458       NaN  0.082186       NaN
                                     gsp                   3.672307       NaN   6.350023       NaN  0.088287       NaN
                                     historical_tod_mean   3.898074       NaN   6.849089       NaN  0.091157       NaN
                                     neighbor_average      7.316889       NaN  11.450523       NaN  0.194604       NaN
       best_random_by_validation     gls_map               3.366858       NaN   5.880048       NaN  0.082320       NaN
                                     gsp                   3.608165       NaN   6.282926       NaN  0.087528       NaN
                                     historical_tod_mean   3.878380       NaN   6.793981       NaN  0.091003       NaN
                                     neighbor_average      7.271106       NaN  11.406261       NaN  0.189270       NaN
       coverage                      gls_map               3.576208       NaN   6.075505       NaN  0.085773       NaN
                                     gsp                   3.721344       NaN   6.425346       NaN  0.090033       NaN
                                     historical_tod_mean   3.872928       NaN   6.838673       NaN  0.091417       NaN
                                     neighbor_average      7.528220       NaN  11.863063       NaN  0.200456       NaN
       degree                        gls_map               3.744527       NaN   6.566654       NaN  0.087805       NaN
                                     gsp                   3.827449       NaN   6.716318       NaN  0.089400       NaN
                                     historical_tod_mean   3.908854       NaN   6.886101       NaN  0.091379       NaN
                                     neighbor_average      8.088245       NaN  12.740808       NaN  0.207836       NaN
       graph_sampling_laplacian      gls_map               3.618935       NaN   6.146280       NaN  0.085595       NaN
                                     gsp                   3.620195       NaN   6.196453       NaN  0.086821       NaN
                                     historical_tod_mean   3.788393       NaN   6.589399       NaN  0.088096       NaN
                                     neighbor_average      8.360416       NaN  13.212579       NaN  0.200607       NaN
       greedy_a_trace                gls_map               3.298545       NaN   5.784946       NaN  0.079261       NaN
                                     gsp                   3.749746       NaN   6.415077       NaN  0.088528       NaN
                                     historical_tod_mean   3.880670       NaN   6.828874       NaN  0.090855       NaN
                                     neighbor_average      7.118372       NaN  11.185999       NaN  0.193909       NaN
       greedy_d_logdet               gls_map               3.917772       NaN   6.380912       NaN  0.096769       NaN
                                     gsp                   3.770299       NaN   6.488133       NaN  0.091991       NaN
                                     historical_tod_mean   3.888358       NaN   6.859711       NaN  0.091399       NaN
                                     neighbor_average      7.513673       NaN  12.478248       NaN  0.221050       NaN
       multistart_swap_by_validation gls_map               3.269611       NaN   5.629275       NaN  0.078420       NaN
                                     gsp                   3.726865       NaN   6.353029       NaN  0.088632       NaN
                                     historical_tod_mean   3.865485       NaN   6.766565       NaN  0.090653       NaN
                                     neighbor_average      7.117211       NaN  11.080851       NaN  0.192608       NaN
       observability_proxy           gls_map               3.590991       NaN   6.292121       NaN  0.085712       NaN
                                     gsp                   3.758792       NaN   6.651092       NaN  0.087641       NaN
                                     historical_tod_mean   3.873913       NaN   6.829232       NaN  0.090185       NaN
                                     neighbor_average      7.532018       NaN  12.097507       NaN  0.193370       NaN
       qr_pod_modes                  gls_map               3.656185       NaN   6.169025       NaN  0.088101       NaN
                                     gsp                   3.743352       NaN   6.390007       NaN  0.089224       NaN
                                     historical_tod_mean   3.882856       NaN   6.821873       NaN  0.090283       NaN
                                     neighbor_average      7.028497       NaN  11.530481       NaN  0.203415       NaN
       random                        gls_map               3.444590  0.084869   5.952663  0.126647  0.082191  0.002096
                                     gsp                   3.664824  0.057945   6.351242  0.080815  0.087633  0.001481
                                     historical_tod_mean   3.856571  0.034961   6.787144  0.062817  0.090199  0.000981
                                     neighbor_average      7.338100  0.235336  11.495955  0.351334  0.188504  0.006533
       rcss_selected                 gls_map               3.294029       NaN   5.748087       NaN  0.078595       NaN
                                     gsp                   3.728338       NaN   6.376038       NaN  0.088058       NaN
                                     historical_tod_mean   3.871195       NaN   6.788745       NaN  0.090235       NaN
                                     neighbor_average      6.939381       NaN  10.939496       NaN  0.187353       NaN
       robust_coverage_cvar          gls_map               3.454215       NaN   5.776667       NaN  0.081680       NaN
                                     gsp                   3.665702       NaN   6.237021       NaN  0.087117       NaN
                                     historical_tod_mean   3.804535       NaN   6.701135       NaN  0.089203       NaN
                                     neighbor_average      7.422549       NaN  11.172327       NaN  0.189118       NaN
       scenario_average_a_trace      gls_map               3.372171       NaN   5.869339       NaN  0.079378       NaN
                                     gsp                   3.680087       NaN   6.426294       NaN  0.086932       NaN
                                     historical_tod_mean   3.863057       NaN   6.810521       NaN  0.090299       NaN
                                     neighbor_average      7.393766       NaN  11.622475       NaN  0.193098       NaN
       scenario_cvar_a_trace         gls_map               3.233584       NaN   5.626679       NaN  0.076611       NaN
                                     gsp                   3.614233       NaN   6.269198       NaN  0.086634       NaN
                                     historical_tod_mean   3.825078       NaN   6.745641       NaN  0.089223       NaN
                                     neighbor_average      7.487309       NaN  11.467779       NaN  0.194815       NaN
       swap_from_best_random_trace   gls_map               3.357148       NaN   5.753806       NaN  0.080504       NaN
                                     gsp                   3.740910       NaN   6.369419       NaN  0.088215       NaN
                                     historical_tod_mean   3.860196       NaN   6.763901       NaN  0.090130       NaN
                                     neighbor_average      6.939017       NaN  10.894584       NaN  0.188024       NaN
       swap_from_greedy_a_trace      gls_map               3.252684       NaN   5.613618       NaN  0.077698       NaN
                                     gsp                   3.713994       NaN   6.333119       NaN  0.088231       NaN
                                     historical_tod_mean   3.851169       NaN   6.748324       NaN  0.090162       NaN
                                     neighbor_average      7.130670       NaN  11.059027       NaN  0.190551       NaN
       swap_from_scenario_average    gls_map               3.294029       NaN   5.748087       NaN  0.078595       NaN
                                     gsp                   3.728338       NaN   6.376038       NaN  0.088058       NaN
                                     historical_tod_mean   3.871195       NaN   6.788745       NaN  0.090235       NaN
                                     neighbor_average      6.939381       NaN  10.939496       NaN  0.187353       NaN
       swap_from_scenario_cvar       gls_map               3.363056       NaN   5.849006       NaN  0.078527       NaN
                                     gsp                   3.769387       NaN   6.432278       NaN  0.089005       NaN
                                     historical_tod_mean   3.873597       NaN   6.809607       NaN  0.091055       NaN
                                     neighbor_average      7.020119       NaN  11.187312       NaN  0.194425       NaN
       top_variance                  gls_map               3.302614       NaN   5.749662       NaN  0.077476       NaN
                                     gsp                   3.380443       NaN   5.973763       NaN  0.080096       NaN
                                     historical_tod_mean   3.636535       NaN   6.385029       NaN  0.083585       NaN
                                     neighbor_average     10.161157       NaN  15.979864       NaN  0.199835       NaN
       validation_swap_selected      gls_map               3.205678       NaN   5.505802       NaN  0.076397       NaN
                                     gsp                   3.661464       NaN   6.276604       NaN  0.087228       NaN
                                     historical_tod_mean   3.830739       NaN   6.717306       NaN  0.089603       NaN
                                     neighbor_average      7.195558       NaN  11.226071       NaN  0.192910       NaN
0.2    best_random_by_trace          gls_map               3.201436       NaN   5.499442       NaN  0.075025       NaN
                                     gsp                   3.587461       NaN   6.226507       NaN  0.086073       NaN
                                     historical_tod_mean   3.801929       NaN   6.730528       NaN  0.089498       NaN
                                     neighbor_average      7.370422       NaN  11.461715       NaN  0.187955       NaN
       best_random_by_validation     gls_map               3.161685       NaN   5.459007       NaN  0.072672       NaN
                                     gsp                   3.519820       NaN   6.143529       NaN  0.082980       NaN
                                     historical_tod_mean   3.746893       NaN   6.653781       NaN  0.086172       NaN
                                     neighbor_average      7.187471       NaN  11.498967       NaN  0.169500       NaN
       coverage                      gls_map               3.261246       NaN   5.716533       NaN  0.078723       NaN
                                     gsp                   3.637450       NaN   6.379599       NaN  0.089764       NaN
                                     historical_tod_mean   3.888532       NaN   6.915098       NaN  0.092950       NaN
                                     neighbor_average      7.028219       NaN  10.993721       NaN  0.187723       NaN
       degree                        gls_map               3.617164       NaN   6.263671       NaN  0.087069       NaN
                                     gsp                   3.721028       NaN   6.480138       NaN  0.087902       NaN
                                     historical_tod_mean   3.943139       NaN   6.875640       NaN  0.091441       NaN
                                     neighbor_average      7.515680       NaN  11.980899       NaN  0.194205       NaN
       graph_sampling_laplacian      gls_map               3.554386       NaN   5.946783       NaN  0.085726       NaN
                                     gsp                   3.564651       NaN   6.124951       NaN  0.087393       NaN
                                     historical_tod_mean   3.685447       NaN   6.503971       NaN  0.086519       NaN
                                     neighbor_average      7.342349       NaN  11.494153       NaN  0.195402       NaN
       greedy_a_trace                gls_map               3.144382       NaN   5.373038       NaN  0.075690       NaN
                                     gsp                   3.708852       NaN   6.318548       NaN  0.089531       NaN
                                     historical_tod_mean   3.905744       NaN   6.826407       NaN  0.092082       NaN
                                     neighbor_average      7.136211       NaN  11.274782       NaN  0.201610       NaN
       greedy_d_logdet               gls_map               3.645134       NaN   5.952973       NaN  0.085953       NaN
                                     gsp                   3.754206       NaN   6.446615       NaN  0.090310       NaN
                                     historical_tod_mean   3.931390       NaN   6.909515       NaN  0.092191       NaN
                                     neighbor_average      7.456650       NaN  12.145015       NaN  0.218106       NaN
       multistart_swap_by_validation gls_map               3.112603       NaN   5.338086       NaN  0.074555       NaN
                                     gsp                   3.627504       NaN   6.285465       NaN  0.088471       NaN
                                     historical_tod_mean   3.853948       NaN   6.793443       NaN  0.091063       NaN
                                     neighbor_average      6.988139       NaN  11.078061       NaN  0.197456       NaN
       observability_proxy           gls_map               3.490892       NaN   6.178241       NaN  0.084206       NaN
                                     gsp                   3.753278       NaN   6.631264       NaN  0.089112       NaN
                                     historical_tod_mean   3.995379       NaN   7.022566       NaN  0.093521       NaN
                                     neighbor_average      7.581715       NaN  11.776668       NaN  0.197919       NaN
       qr_pod_modes                  gls_map               3.445871       NaN   5.658856       NaN  0.082963       NaN
                                     gsp                   3.680796       NaN   6.252044       NaN  0.090389       NaN
                                     historical_tod_mean   3.835998       NaN   6.732208       NaN  0.091172       NaN
                                     neighbor_average      7.344316       NaN  11.852719       NaN  0.213390       NaN
       random                        gls_map               3.226482  0.058535   5.624456  0.108917  0.076436  0.001640
                                     gsp                   3.628243  0.066440   6.276546  0.095445  0.087041  0.001703
                                     historical_tod_mean   3.853008  0.061106   6.783683  0.097844  0.090177  0.001573
                                     neighbor_average      7.156799  0.150165  11.307446  0.260095  0.181014  0.006948
       rcss_selected                 gls_map               3.146358       NaN   5.360321       NaN  0.073973       NaN
                                     gsp                   3.667574       NaN   6.288433       NaN  0.086640       NaN
                                     historical_tod_mean   3.890799       NaN   6.797396       NaN  0.090669       NaN
                                     neighbor_average      6.852006       NaN  10.843044       NaN  0.187962       NaN
       robust_coverage_cvar          gls_map               3.126119       NaN   5.328462       NaN  0.073502       NaN
                                     gsp                   3.509918       NaN   6.105348       NaN  0.083674       NaN
                                     historical_tod_mean   3.733449       NaN   6.641794       NaN  0.087423       NaN
                                     neighbor_average      7.325786       NaN  11.200185       NaN  0.180714       NaN
       scenario_average_a_trace      gls_map               3.144579       NaN   5.384106       NaN  0.072371       NaN
                                     gsp                   3.619739       NaN   6.223498       NaN  0.085310       NaN
                                     historical_tod_mean   3.798661       NaN   6.722334       NaN  0.088618       NaN
                                     neighbor_average      7.139231       NaN  10.983240       NaN  0.180950       NaN
       scenario_cvar_a_trace         gls_map               3.096617       NaN   5.357386       NaN  0.073026       NaN
                                     gsp                   3.541630       NaN   6.157994       NaN  0.085301       NaN
                                     historical_tod_mean   3.741777       NaN   6.656836       NaN  0.087674       NaN
                                     neighbor_average      7.486203       NaN  11.313807       NaN  0.179246       NaN
       swap_from_best_random_trace   gls_map               3.182745       NaN   5.291196       NaN  0.075229       NaN
                                     gsp                   3.620696       NaN   6.210545       NaN  0.087320       NaN
                                     historical_tod_mean   3.832376       NaN   6.718029       NaN  0.090293       NaN
                                     neighbor_average      7.017803       NaN  11.021050       NaN  0.191092       NaN
       swap_from_greedy_a_trace      gls_map               3.118137       NaN   5.380128       NaN  0.074282       NaN
                                     gsp                   3.707752       NaN   6.374036       NaN  0.089278       NaN
                                     historical_tod_mean   3.918242       NaN   6.863750       NaN  0.091986       NaN
                                     neighbor_average      7.001058       NaN  11.139033       NaN  0.196247       NaN
       swap_from_scenario_average    gls_map               3.146358       NaN   5.360321       NaN  0.073973       NaN
                                     gsp                   3.667574       NaN   6.288433       NaN  0.086640       NaN
                                     historical_tod_mean   3.890799       NaN   6.797396       NaN  0.090669       NaN
                                     neighbor_average      6.852006       NaN  10.843044       NaN  0.187962       NaN
       swap_from_scenario_cvar       gls_map               3.171650       NaN   5.362885       NaN  0.073180       NaN
                                     gsp                   3.701970       NaN   6.305445       NaN  0.088676       NaN
                                     historical_tod_mean   3.859058       NaN   6.787766       NaN  0.090938       NaN
                                     neighbor_average      6.892969       NaN  10.979978       NaN  0.192310       NaN
       top_variance                  gls_map               3.015254       NaN   5.380285       NaN  0.070011       NaN
                                     gsp                   3.240028       NaN   5.763665       NaN  0.076030       NaN
                                     historical_tod_mean   3.474279       NaN   6.164916       NaN  0.079408       NaN
                                     neighbor_average      9.315921       NaN  14.908244       NaN  0.180837       NaN
       validation_swap_selected      gls_map               2.948697       NaN   5.240119       NaN  0.068807       NaN
                                     gsp                   3.464472       NaN   6.087277       NaN  0.081307       NaN
                                     historical_tod_mean   3.742863       NaN   6.637458       NaN  0.085612       NaN
                                     neighbor_average      6.950404       NaN  10.604521       NaN  0.166002       NaN
0.3    best_random_by_trace          gls_map               3.147107       NaN   5.567829       NaN  0.073325       NaN
                                     gsp                   3.739407       NaN   6.506249       NaN  0.089541       NaN
                                     historical_tod_mean   4.028389       NaN   7.063688       NaN  0.094384       NaN
                                     neighbor_average      6.969595       NaN  10.855233       NaN  0.171964       NaN
       best_random_by_validation     gls_map               2.945786       NaN   5.219602       NaN  0.067924       NaN
                                     gsp                   3.510767       NaN   6.170628       NaN  0.083390       NaN
                                     historical_tod_mean   3.771837       NaN   6.748609       NaN  0.086946       NaN
                                     neighbor_average      6.957566       NaN  10.836948       NaN  0.174282       NaN
       coverage                      gls_map               3.084519       NaN   5.417426       NaN  0.073053       NaN
                                     gsp                   3.586717       NaN   6.304464       NaN  0.088007       NaN
                                     historical_tod_mean   3.826094       NaN   6.877436       NaN  0.091490       NaN
                                     neighbor_average      6.955843       NaN  10.686813       NaN  0.179718       NaN
       degree                        gls_map               3.522199       NaN   6.056583       NaN  0.085267       NaN
                                     gsp                   3.649239       NaN   6.338102       NaN  0.086998       NaN
                                     historical_tod_mean   3.917088       NaN   6.848187       NaN  0.090937       NaN
                                     neighbor_average      7.994215       NaN  12.672860       NaN  0.211334       NaN
       graph_sampling_laplacian      gls_map               3.346835       NaN   5.706443       NaN  0.079592       NaN
                                     gsp                   3.556105       NaN   6.083531       NaN  0.087061       NaN
                                     historical_tod_mean   3.703360       NaN   6.535236       NaN  0.087345       NaN
                                     neighbor_average      6.875616       NaN  11.226019       NaN  0.182383       NaN
       greedy_a_trace                gls_map               3.056360       NaN   5.238556       NaN  0.074811       NaN
                                     gsp                   3.692522       NaN   6.334776       NaN  0.091286       NaN
                                     historical_tod_mean   3.903668       NaN   6.882628       NaN  0.093614       NaN
                                     neighbor_average      6.817190       NaN  10.757959       NaN  0.196131       NaN
       greedy_d_logdet               gls_map               3.440676       NaN   5.640431       NaN  0.081813       NaN
                                     gsp                   3.637851       NaN   6.286756       NaN  0.088628       NaN
                                     historical_tod_mean   3.843886       NaN   6.846821       NaN  0.090747       NaN
                                     neighbor_average      7.651496       NaN  12.320914       NaN  0.220919       NaN
       multistart_swap_by_validation gls_map               2.924741       NaN   5.024289       NaN  0.069976       NaN
                                     gsp                   3.589838       NaN   6.168244       NaN  0.086732       NaN
                                     historical_tod_mean   3.790969       NaN   6.713560       NaN  0.088965       NaN
                                     neighbor_average      6.683771       NaN  10.613138       NaN  0.181509       NaN
       observability_proxy           gls_map               3.436587       NaN   6.006780       NaN  0.082876       NaN
                                     gsp                   3.658373       NaN   6.379388       NaN  0.087062       NaN
                                     historical_tod_mean   3.940039       NaN   6.879140       NaN  0.091467       NaN
                                     neighbor_average      7.733577       NaN  11.777394       NaN  0.194300       NaN
       qr_pod_modes                  gls_map               3.066511       NaN   5.125525       NaN  0.074814       NaN
                                     gsp                   3.548646       NaN   6.107794       NaN  0.086963       NaN
                                     historical_tod_mean   3.771479       NaN   6.669659       NaN  0.089118       NaN
                                     neighbor_average      6.974422       NaN  11.021627       NaN  0.197850       NaN
       random                        gls_map               3.100657  0.080375   5.418705  0.138291  0.072873  0.002500
                                     gsp                   3.623962  0.079237   6.256290  0.112723  0.086909  0.002369
                                     historical_tod_mean   3.854895  0.075922   6.791268  0.115763  0.089999  0.002136
                                     neighbor_average      7.025559  0.173455  11.106227  0.299106  0.177355  0.007662
       rcss_selected                 gls_map               2.964338       NaN   5.090073       NaN  0.069676       NaN
                                     gsp                   3.441613       NaN   6.026281       NaN  0.082826       NaN
                                     historical_tod_mean   3.657031       NaN   6.566143       NaN  0.086306       NaN
                                     neighbor_average      7.527208       NaN  11.681813       NaN  0.186759       NaN
       robust_coverage_cvar          gls_map               2.964338       NaN   5.090073       NaN  0.069676       NaN
                                     gsp                   3.441613       NaN   6.026281       NaN  0.082826       NaN
                                     historical_tod_mean   3.657031       NaN   6.566143       NaN  0.086306       NaN
                                     neighbor_average      7.527208       NaN  11.681813       NaN  0.186759       NaN
       scenario_average_a_trace      gls_map               3.007700       NaN   5.177482       NaN  0.070057       NaN
                                     gsp                   3.593655       NaN   6.234020       NaN  0.085702       NaN
                                     historical_tod_mean   3.808478       NaN   6.795018       NaN  0.089721       NaN
                                     neighbor_average      6.931906       NaN  10.785273       NaN  0.177415       NaN
       scenario_cvar_a_trace         gls_map               2.999618       NaN   5.185294       NaN  0.071118       NaN
                                     gsp                   3.448527       NaN   6.001359       NaN  0.083574       NaN
                                     historical_tod_mean   3.671570       NaN   6.538738       NaN  0.086645       NaN
                                     neighbor_average      7.085665       NaN  10.928210       NaN  0.171222       NaN
       swap_from_best_random_trace   gls_map               3.109490       NaN   5.316126       NaN  0.074784       NaN
                                     gsp                   3.732122       NaN   6.422213       NaN  0.091542       NaN
                                     historical_tod_mean   3.982963       NaN   6.985165       NaN  0.094673       NaN
                                     neighbor_average      6.816174       NaN  10.903351       NaN  0.191826       NaN
       swap_from_greedy_a_trace      gls_map               3.045886       NaN   5.183429       NaN  0.073011       NaN
                                     gsp                   3.696635       NaN   6.285470       NaN  0.089362       NaN
                                     historical_tod_mean   3.908652       NaN   6.832244       NaN  0.091799       NaN
                                     neighbor_average      6.850710       NaN  10.843495       NaN  0.194911       NaN
       swap_from_scenario_average    gls_map               3.079325       NaN   5.184612       NaN  0.074303       NaN
                                     gsp                   3.670136       NaN   6.270615       NaN  0.089819       NaN
                                     historical_tod_mean   3.903892       NaN   6.853167       NaN  0.092515       NaN
                                     neighbor_average      6.930619       NaN  11.072973       NaN  0.195996       NaN
       swap_from_scenario_cvar       gls_map               3.073500       NaN   5.112778       NaN  0.073030       NaN
                                     gsp                   3.592902       NaN   6.132535       NaN  0.087241       NaN
                                     historical_tod_mean   3.794967       NaN   6.668217       NaN  0.089558       NaN
                                     neighbor_average      6.848087       NaN  10.745043       NaN  0.185825       NaN
       top_variance                  gls_map               2.890031       NaN   5.119386       NaN  0.064888       NaN
                                     gsp                   3.099940       NaN   5.504848       NaN  0.070969       NaN
                                     historical_tod_mean   3.308552       NaN   5.849745       NaN  0.074326       NaN
                                     neighbor_average      8.996992       NaN  14.234406       NaN  0.171446       NaN
       validation_swap_selected      gls_map               2.826152       NaN   4.861736       NaN  0.066758       NaN
                                     gsp                   3.488656       NaN   6.035857       NaN  0.083172       NaN
                                     historical_tod_mean   3.695111       NaN   6.589559       NaN  0.086125       NaN
                                     neighbor_average      6.741172       NaN  10.515527       NaN  0.173083       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 3.205678 5.505802
    0.2 validation_swap_selected gls_map 2.948697 5.240119
    0.3 validation_swap_selected gls_map 2.826152 4.861736
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.302893      0.320527 210
    gsp   condition_number     0.307676      0.357253 210
    gsp information_logdet    -0.309802     -0.328000 210
gls_map    posterior_trace     0.797100      0.804677 210
gls_map   condition_number     0.817460      0.852213 210
gls_map information_logdet    -0.721064     -0.771128 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv