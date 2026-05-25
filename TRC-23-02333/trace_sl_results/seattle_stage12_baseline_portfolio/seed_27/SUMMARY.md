---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-16, 2015-01-12
Test days: 2015-01-25, 2015-01-26
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.123932       NaN   5.213153       NaN  0.079095       NaN
                                     gsp                  4.212730       NaN   6.740482       NaN  0.112156       NaN
                                     historical_tod_mean  5.668386       NaN   8.767501       NaN  0.140805       NaN
                                     neighbor_average     4.921359       NaN   8.075162       NaN  0.137631       NaN
       best_random_by_validation     gls_map              3.035381       NaN   4.980425       NaN  0.076159       NaN
                                     gsp                  4.231656       NaN   6.655748       NaN  0.109552       NaN
                                     historical_tod_mean  5.598813       NaN   8.648064       NaN  0.138165       NaN
                                     neighbor_average     4.945372       NaN   8.290251       NaN  0.132657       NaN
       coverage                      gls_map              3.112870       NaN   5.238040       NaN  0.080520       NaN
                                     gsp                  4.267934       NaN   6.786831       NaN  0.112324       NaN
                                     historical_tod_mean  5.675616       NaN   8.787203       NaN  0.141231       NaN
                                     neighbor_average     4.966808       NaN   8.020228       NaN  0.140028       NaN
       degree                        gls_map              3.439105       NaN   5.795729       NaN  0.094002       NaN
                                     gsp                  4.250518       NaN   6.825134       NaN  0.116528       NaN
                                     historical_tod_mean  5.655707       NaN   8.772254       NaN  0.142046       NaN
                                     neighbor_average     5.676447       NaN   9.647633       NaN  0.159340       NaN
       graph_sampling_laplacian      gls_map              3.700965       NaN   6.063190       NaN  0.091840       NaN
                                     gsp                  4.341118       NaN   6.836029       NaN  0.113247       NaN
                                     historical_tod_mean  5.729492       NaN   8.864812       NaN  0.142504       NaN
                                     neighbor_average     5.910356       NaN  10.290275       NaN  0.175070       NaN
       greedy_a_trace                gls_map              2.984872       NaN   5.048367       NaN  0.073789       NaN
                                     gsp                  4.243966       NaN   6.774328       NaN  0.110961       NaN
                                     historical_tod_mean  5.664575       NaN   8.744502       NaN  0.139114       NaN
                                     neighbor_average     4.803664       NaN   7.859211       NaN  0.133276       NaN
       greedy_d_logdet               gls_map              3.553859       NaN   5.829740       NaN  0.096818       NaN
                                     gsp                  4.547678       NaN   7.305370       NaN  0.124066       NaN
                                     historical_tod_mean  5.831580       NaN   8.944738       NaN  0.146015       NaN
                                     neighbor_average     5.411602       NaN   9.365869       NaN  0.176206       NaN
       multistart_swap_by_validation gls_map              2.944367       NaN   4.936324       NaN  0.070886       NaN
                                     gsp                  4.236131       NaN   6.746583       NaN  0.108827       NaN
                                     historical_tod_mean  5.642934       NaN   8.698812       NaN  0.137038       NaN
                                     neighbor_average     5.022306       NaN   8.248191       NaN  0.132300       NaN
       observability_proxy           gls_map              3.401358       NaN   5.635400       NaN  0.089108       NaN
                                     gsp                  4.264645       NaN   6.756891       NaN  0.113038       NaN
                                     historical_tod_mean  5.652568       NaN   8.745588       NaN  0.141137       NaN
                                     neighbor_average     5.437633       NaN   9.222674       NaN  0.153967       NaN
       qr_pod_modes                  gls_map              3.243260       NaN   5.467984       NaN  0.087147       NaN
                                     gsp                  4.280215       NaN   6.925135       NaN  0.116613       NaN
                                     historical_tod_mean  5.735602       NaN   8.836632       NaN  0.143181       NaN
                                     neighbor_average     5.175569       NaN   9.031167       NaN  0.164922       NaN
       random                        gls_map              3.160054  0.068044   5.286023  0.132303  0.080703  0.003305
                                     gsp                  4.224732  0.045244   6.731602  0.071478  0.111661  0.002044
                                     historical_tod_mean  5.639527  0.037498   8.728933  0.055242  0.139885  0.001750
                                     neighbor_average     5.040716  0.201879   8.430114  0.343137  0.140220  0.006702
       rcss_selected                 gls_map              2.944367       NaN   4.936324       NaN  0.070886       NaN
                                     gsp                  4.236131       NaN   6.746583       NaN  0.108827       NaN
                                     historical_tod_mean  5.642934       NaN   8.698812       NaN  0.137038       NaN
                                     neighbor_average     5.022306       NaN   8.248191       NaN  0.132300       NaN
       robust_coverage_cvar          gls_map              3.186443       NaN   5.472437       NaN  0.084407       NaN
                                     gsp                  4.294774       NaN   6.817534       NaN  0.112951       NaN
                                     historical_tod_mean  5.706048       NaN   8.800816       NaN  0.141300       NaN
                                     neighbor_average     4.789559       NaN   8.136582       NaN  0.142212       NaN
       scenario_average_a_trace      gls_map              3.051749       NaN   5.051157       NaN  0.076427       NaN
                                     gsp                  4.256795       NaN   6.774259       NaN  0.111806       NaN
                                     historical_tod_mean  5.672321       NaN   8.763026       NaN  0.140728       NaN
                                     neighbor_average     4.972927       NaN   8.221011       NaN  0.140765       NaN
       scenario_cvar_a_trace         gls_map              3.087376       NaN   5.236701       NaN  0.077302       NaN
                                     gsp                  4.276401       NaN   6.817205       NaN  0.112430       NaN
                                     historical_tod_mean  5.717328       NaN   8.802425       NaN  0.141047       NaN
                                     neighbor_average     5.009532       NaN   8.396658       NaN  0.142110       NaN
       swap_from_best_random_trace   gls_map              2.966025       NaN   4.969828       NaN  0.072718       NaN
                                     gsp                  4.257901       NaN   6.807728       NaN  0.111166       NaN
                                     historical_tod_mean  5.672917       NaN   8.749586       NaN  0.138926       NaN
                                     neighbor_average     5.090694       NaN   8.348471       NaN  0.139559       NaN
       swap_from_greedy_a_trace      gls_map              2.963226       NaN   5.012723       NaN  0.075779       NaN
                                     gsp                  4.289931       NaN   6.858329       NaN  0.113586       NaN
                                     historical_tod_mean  5.678771       NaN   8.765832       NaN  0.140726       NaN
                                     neighbor_average     4.969398       NaN   8.059404       NaN  0.138783       NaN
       swap_from_scenario_average    gls_map              2.932712       NaN   4.894676       NaN  0.072015       NaN
                                     gsp                  4.245621       NaN   6.770208       NaN  0.110590       NaN
                                     historical_tod_mean  5.642167       NaN   8.708787       NaN  0.138259       NaN
                                     neighbor_average     4.945173       NaN   7.908327       NaN  0.131621       NaN
       swap_from_scenario_cvar       gls_map              2.903891       NaN   4.910455       NaN  0.072569       NaN
                                     gsp                  4.238842       NaN   6.792682       NaN  0.111303       NaN
                                     historical_tod_mean  5.672896       NaN   8.752238       NaN  0.139135       NaN
                                     neighbor_average     4.856157       NaN   7.993500       NaN  0.133625       NaN
       top_variance                  gls_map              3.398889       NaN   5.320933       NaN  0.080800       NaN
                                     gsp                  4.039912       NaN   6.218956       NaN  0.096333       NaN
                                     historical_tod_mean  5.210979       NaN   7.986809       NaN  0.119040       NaN
                                     neighbor_average     7.304834       NaN  12.248208       NaN  0.148447       NaN
       validation_swap_selected      gls_map              2.928393       NaN   4.881703       NaN  0.071757       NaN
                                     gsp                  4.240517       NaN   6.746958       NaN  0.110054       NaN
                                     historical_tod_mean  5.633214       NaN   8.698465       NaN  0.137854       NaN
                                     neighbor_average     4.963234       NaN   7.944401       NaN  0.132919       NaN
0.2    best_random_by_trace          gls_map              2.873121       NaN   4.899210       NaN  0.075363       NaN
                                     gsp                  4.143098       NaN   6.569489       NaN  0.111477       NaN
                                     historical_tod_mean  5.710057       NaN   8.854067       NaN  0.143103       NaN
                                     neighbor_average     4.484331       NaN   7.599078       NaN  0.130063       NaN
       best_random_by_validation     gls_map              2.770547       NaN   4.785408       NaN  0.073499       NaN
                                     gsp                  4.094740       NaN   6.547162       NaN  0.111057       NaN
                                     historical_tod_mean  5.645949       NaN   8.765610       NaN  0.141675       NaN
                                     neighbor_average     4.367048       NaN   7.296896       NaN  0.121812       NaN
       coverage                      gls_map              2.749888       NaN   4.636586       NaN  0.070031       NaN
                                     gsp                  4.108725       NaN   6.520528       NaN  0.108822       NaN
                                     historical_tod_mean  5.669180       NaN   8.762884       NaN  0.140985       NaN
                                     neighbor_average     4.121728       NaN   6.765740       NaN  0.114127       NaN
       degree                        gls_map              3.302117       NaN   5.546818       NaN  0.089344       NaN
                                     gsp                  4.222270       NaN   6.674036       NaN  0.113143       NaN
                                     historical_tod_mean  5.710214       NaN   8.826513       NaN  0.143990       NaN
                                     neighbor_average     5.761216       NaN   9.814458       NaN  0.163106       NaN
       graph_sampling_laplacian      gls_map              3.517085       NaN   5.920390       NaN  0.090631       NaN
                                     gsp                  4.286898       NaN   6.707789       NaN  0.113016       NaN
                                     historical_tod_mean  5.744244       NaN   8.903129       NaN  0.144448       NaN
                                     neighbor_average     5.481660       NaN   9.307536       NaN  0.162078       NaN
       greedy_a_trace                gls_map              2.751684       NaN   4.667805       NaN  0.069804       NaN
                                     gsp                  4.203536       NaN   6.694470       NaN  0.112792       NaN
                                     historical_tod_mean  5.796820       NaN   8.917901       NaN  0.144289       NaN
                                     neighbor_average     4.281450       NaN   7.026173       NaN  0.122251       NaN
       greedy_d_logdet               gls_map              3.252019       NaN   5.439956       NaN  0.091343       NaN
                                     gsp                  4.401471       NaN   7.031537       NaN  0.123161       NaN
                                     historical_tod_mean  5.988209       NaN   9.166662       NaN  0.152570       NaN
                                     neighbor_average     5.004837       NaN   8.908013       NaN  0.170831       NaN
       multistart_swap_by_validation gls_map              2.730568       NaN   4.637799       NaN  0.071461       NaN
                                     gsp                  4.172554       NaN   6.642820       NaN  0.112742       NaN
                                     historical_tod_mean  5.759231       NaN   8.851085       NaN  0.143290       NaN
                                     neighbor_average     4.233434       NaN   6.945955       NaN  0.120445       NaN
       observability_proxy           gls_map              3.213680       NaN   5.425014       NaN  0.086076       NaN
                                     gsp                  4.209732       NaN   6.662778       NaN  0.111868       NaN
                                     historical_tod_mean  5.688142       NaN   8.795967       NaN  0.142784       NaN
                                     neighbor_average     5.575130       NaN   9.399452       NaN  0.157037       NaN
       qr_pod_modes                  gls_map              2.882416       NaN   4.866460       NaN  0.074314       NaN
                                     gsp                  4.262155       NaN   6.794620       NaN  0.116152       NaN
                                     historical_tod_mean  5.869639       NaN   9.010293       NaN  0.146933       NaN
                                     neighbor_average     4.492794       NaN   7.566587       NaN  0.137812       NaN
       random                        gls_map              2.857402  0.048041   4.846133  0.128393  0.073331  0.003065
                                     gsp                  4.109007  0.033949   6.533177  0.078697  0.109468  0.003012
                                     historical_tod_mean  5.650212  0.052879   8.749673  0.085794  0.140531  0.002798
                                     neighbor_average     4.524866  0.135425   7.554417  0.241753  0.122542  0.005865
       rcss_selected                 gls_map              2.699507       NaN   4.463731       NaN  0.065994       NaN
                                     gsp                  4.074108       NaN   6.448480       NaN  0.106272       NaN
                                     historical_tod_mean  5.593091       NaN   8.680028       NaN  0.138653       NaN
                                     neighbor_average     4.411466       NaN   7.279968       NaN  0.113989       NaN
       robust_coverage_cvar          gls_map              2.926987       NaN   4.981569       NaN  0.075983       NaN
                                     gsp                  4.261112       NaN   6.752882       NaN  0.114578       NaN
                                     historical_tod_mean  5.843389       NaN   8.971081       NaN  0.145843       NaN
                                     neighbor_average     4.368251       NaN   7.391176       NaN  0.131784       NaN
       scenario_average_a_trace      gls_map              2.903352       NaN   4.823547       NaN  0.074782       NaN
                                     gsp                  4.231693       NaN   6.728696       NaN  0.114663       NaN
                                     historical_tod_mean  5.814313       NaN   8.955196       NaN  0.145916       NaN
                                     neighbor_average     4.570618       NaN   7.716081       NaN  0.138969       NaN
       scenario_cvar_a_trace         gls_map              2.978966       NaN   5.116776       NaN  0.076264       NaN
                                     gsp                  4.309042       NaN   6.805436       NaN  0.114403       NaN
                                     historical_tod_mean  5.889860       NaN   9.015856       NaN  0.146432       NaN
                                     neighbor_average     4.697093       NaN   7.937553       NaN  0.141038       NaN
       swap_from_best_random_trace   gls_map              2.839564       NaN   4.782223       NaN  0.073181       NaN
                                     gsp                  4.198914       NaN   6.670790       NaN  0.113153       NaN
                                     historical_tod_mean  5.777981       NaN   8.911789       NaN  0.144233       NaN
                                     neighbor_average     4.342963       NaN   7.316727       NaN  0.132427       NaN
       swap_from_greedy_a_trace      gls_map              2.744798       NaN   4.650832       NaN  0.069505       NaN
                                     gsp                  4.208769       NaN   6.692744       NaN  0.113372       NaN
                                     historical_tod_mean  5.815916       NaN   8.924253       NaN  0.144855       NaN
                                     neighbor_average     4.343726       NaN   7.225355       NaN  0.127962       NaN
       swap_from_scenario_average    gls_map              2.766549       NaN   4.669407       NaN  0.069958       NaN
                                     gsp                  4.203924       NaN   6.708598       NaN  0.114099       NaN
                                     historical_tod_mean  5.820513       NaN   8.937873       NaN  0.145251       NaN
                                     neighbor_average     4.400082       NaN   7.370613       NaN  0.132596       NaN
       swap_from_scenario_cvar       gls_map              2.790796       NaN   4.731297       NaN  0.070267       NaN
                                     gsp                  4.262834       NaN   6.760075       NaN  0.113818       NaN
                                     historical_tod_mean  5.851475       NaN   8.962718       NaN  0.145197       NaN
                                     neighbor_average     4.448731       NaN   7.344914       NaN  0.126460       NaN
       top_variance                  gls_map              2.907090       NaN   4.706690       NaN  0.065635       NaN
                                     gsp                  3.729438       NaN   5.716142       NaN  0.084082       NaN
                                     historical_tod_mean  4.954008       NaN   7.531754       NaN  0.106921       NaN
                                     neighbor_average     5.853710       NaN   9.973383       NaN  0.112999       NaN
       validation_swap_selected      gls_map              2.670233       NaN   4.365371       NaN  0.062249       NaN
                                     gsp                  4.037825       NaN   6.332125       NaN  0.101448       NaN
                                     historical_tod_mean  5.522125       NaN   8.539314       NaN  0.132784       NaN
                                     neighbor_average     4.287743       NaN   6.998576       NaN  0.104101       NaN
0.3    best_random_by_trace          gls_map              2.754640       NaN   4.662320       NaN  0.072760       NaN
                                     gsp                  4.201729       NaN   6.635226       NaN  0.114573       NaN
                                     historical_tod_mean  5.803915       NaN   8.980914       NaN  0.147749       NaN
                                     neighbor_average     4.185217       NaN   7.088971       NaN  0.122809       NaN
       best_random_by_validation     gls_map              2.634747       NaN   4.413834       NaN  0.065440       NaN
                                     gsp                  4.034347       NaN   6.342409       NaN  0.106227       NaN
                                     historical_tod_mean  5.575420       NaN   8.611968       NaN  0.138242       NaN
                                     neighbor_average     4.251029       NaN   6.943576       NaN  0.104752       NaN
       coverage                      gls_map              2.570863       NaN   4.339593       NaN  0.065953       NaN
                                     gsp                  4.091252       NaN   6.510453       NaN  0.110537       NaN
                                     historical_tod_mean  5.672531       NaN   8.809666       NaN  0.143141       NaN
                                     neighbor_average     4.035193       NaN   6.412774       NaN  0.107021       NaN
       degree                        gls_map              3.158041       NaN   5.370705       NaN  0.083917       NaN
                                     gsp                  4.214112       NaN   6.678832       NaN  0.111516       NaN
                                     historical_tod_mean  5.762686       NaN   8.853051       NaN  0.143246       NaN
                                     neighbor_average     6.279758       NaN  10.655429       NaN  0.163630       NaN
       graph_sampling_laplacian      gls_map              3.383514       NaN   5.839426       NaN  0.087829       NaN
                                     gsp                  4.259443       NaN   6.662436       NaN  0.112101       NaN
                                     historical_tod_mean  5.677921       NaN   8.813257       NaN  0.142541       NaN
                                     neighbor_average     5.657944       NaN   9.703976       NaN  0.166205       NaN
       greedy_a_trace                gls_map              2.616759       NaN   4.439328       NaN  0.067523       NaN
                                     gsp                  4.248874       NaN   6.756750       NaN  0.115997       NaN
                                     historical_tod_mean  5.916521       NaN   9.084209       NaN  0.148542       NaN
                                     neighbor_average     3.994423       NaN   6.473119       NaN  0.113404       NaN
       greedy_d_logdet               gls_map              2.986291       NaN   5.172500       NaN  0.087819       NaN
                                     gsp                  4.404886       NaN   7.013662       NaN  0.127382       NaN
                                     historical_tod_mean  6.115507       NaN   9.366123       NaN  0.159733       NaN
                                     neighbor_average     4.640614       NaN   8.258091       NaN  0.163154       NaN
       multistart_swap_by_validation gls_map              2.595352       NaN   4.326294       NaN  0.065234       NaN
                                     gsp                  4.149123       NaN   6.510124       NaN  0.110476       NaN
                                     historical_tod_mean  5.774050       NaN   8.872081       NaN  0.143867       NaN
                                     neighbor_average     3.921534       NaN   6.394171       NaN  0.106078       NaN
       observability_proxy           gls_map              3.161312       NaN   5.344765       NaN  0.083739       NaN
                                     gsp                  4.214922       NaN   6.676699       NaN  0.111601       NaN
                                     historical_tod_mean  5.756132       NaN   8.840463       NaN  0.143203       NaN
                                     neighbor_average     6.221465       NaN  10.568440       NaN  0.162701       NaN
       qr_pod_modes                  gls_map              2.645777       NaN   4.523615       NaN  0.070681       NaN
                                     gsp                  4.247309       NaN   6.775920       NaN  0.118487       NaN
                                     historical_tod_mean  5.912398       NaN   9.118698       NaN  0.150934       NaN
                                     neighbor_average     4.196350       NaN   7.003444       NaN  0.128856       NaN
       random                        gls_map              2.716245  0.054471   4.612484  0.121572  0.069275  0.002815
                                     gsp                  4.094746  0.047804   6.476610  0.075721  0.108822  0.002742
                                     historical_tod_mean  5.658969  0.067664   8.758259  0.090165  0.140898  0.002952
                                     neighbor_average     4.259614  0.099385   7.043623  0.213813  0.112625  0.005655
       rcss_selected                 gls_map              2.548009       NaN   4.303807       NaN  0.064235       NaN
                                     gsp                  4.023488       NaN   6.378596       NaN  0.106757       NaN
                                     historical_tod_mean  5.557503       NaN   8.633184       NaN  0.138025       NaN
                                     neighbor_average     3.989695       NaN   6.479046       NaN  0.100415       NaN
       robust_coverage_cvar          gls_map              2.808201       NaN   4.835635       NaN  0.073438       NaN
                                     gsp                  4.342925       NaN   6.832837       NaN  0.118294       NaN
                                     historical_tod_mean  6.015979       NaN   9.182828       NaN  0.152096       NaN
                                     neighbor_average     4.219020       NaN   7.088381       NaN  0.126517       NaN
       scenario_average_a_trace      gls_map              2.755497       NaN   4.638791       NaN  0.073827       NaN
                                     gsp                  4.276099       NaN   6.797416       NaN  0.119213       NaN
                                     historical_tod_mean  5.951513       NaN   9.166213       NaN  0.151985       NaN
                                     neighbor_average     4.351918       NaN   7.388538       NaN  0.135274       NaN
       scenario_cvar_a_trace         gls_map              2.821042       NaN   4.864869       NaN  0.075318       NaN
                                     gsp                  4.335156       NaN   6.844736       NaN  0.119308       NaN
                                     historical_tod_mean  6.029618       NaN   9.223000       NaN  0.153090       NaN
                                     neighbor_average     4.343741       NaN   7.296813       NaN  0.132718       NaN
       swap_from_best_random_trace   gls_map              2.645185       NaN   4.423257       NaN  0.069803       NaN
                                     gsp                  4.225427       NaN   6.673691       NaN  0.115866       NaN
                                     historical_tod_mean  5.881572       NaN   9.039455       NaN  0.148742       NaN
                                     neighbor_average     4.003017       NaN   6.619221       NaN  0.116010       NaN
       swap_from_greedy_a_trace      gls_map              2.625415       NaN   4.349062       NaN  0.067648       NaN
                                     gsp                  4.279217       NaN   6.743687       NaN  0.116815       NaN
                                     historical_tod_mean  5.961361       NaN   9.098669       NaN  0.149681       NaN
                                     neighbor_average     4.037826       NaN   6.625553       NaN  0.118658       NaN
       swap_from_scenario_average    gls_map              2.603362       NaN   4.332533       NaN  0.067092       NaN
                                     gsp                  4.216533       NaN   6.695316       NaN  0.115709       NaN
                                     historical_tod_mean  5.901503       NaN   9.059169       NaN  0.148225       NaN
                                     neighbor_average     4.054641       NaN   6.700818       NaN  0.119653       NaN
       swap_from_scenario_cvar       gls_map              2.645267       NaN   4.484187       NaN  0.069857       NaN
                                     gsp                  4.281796       NaN   6.789907       NaN  0.117383       NaN
                                     historical_tod_mean  5.975724       NaN   9.163488       NaN  0.151202       NaN
                                     neighbor_average     4.170506       NaN   6.948385       NaN  0.124907       NaN
       top_variance                  gls_map              2.697529       NaN   4.458872       NaN  0.059593       NaN
                                     gsp                  3.540297       NaN   5.444823       NaN  0.076986       NaN
                                     historical_tod_mean  4.757918       NaN   7.204342       NaN  0.098872       NaN
                                     neighbor_average     5.107801       NaN   8.659976       NaN  0.098843       NaN
       validation_swap_selected      gls_map              2.514539       NaN   4.242249       NaN  0.063340       NaN
                                     gsp                  3.989912       NaN   6.338558       NaN  0.105712       NaN
                                     historical_tod_mean  5.523839       NaN   8.597193       NaN  0.136981       NaN
                                     neighbor_average     4.005230       NaN   6.474365       NaN  0.099844       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1  swap_from_scenario_cvar gls_map 2.903891 4.910455
    0.2 validation_swap_selected gls_map 2.670233 4.365371
    0.3 validation_swap_selected gls_map 2.514539 4.242249
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.502396      0.471570 210
    gsp   condition_number     0.501866      0.428385 210
    gsp information_logdet    -0.451728     -0.481976 210
gls_map    posterior_trace     0.889259      0.874212 210
gls_map   condition_number     0.884703      0.894949 210
gls_map information_logdet    -0.793873     -0.814040 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv