---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-07, 2015-01-12
Test days: 2015-01-02, 2015-01-28
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.116940       NaN   4.912201       NaN  0.077604       NaN
                                     gsp                  3.962405       NaN   6.243758       NaN  0.109579       NaN
                                     historical_tod_mean  4.312551       NaN   7.143324       NaN  0.127758       NaN
                                     neighbor_average     5.360976       NaN   8.484084       NaN  0.148360       NaN
       best_random_by_validation     gls_map              3.132477       NaN   4.858114       NaN  0.077041       NaN
                                     gsp                  3.968022       NaN   6.213869       NaN  0.109265       NaN
                                     historical_tod_mean  4.316359       NaN   7.128062       NaN  0.127766       NaN
                                     neighbor_average     5.366553       NaN   8.509336       NaN  0.151150       NaN
       coverage                      gls_map              3.167282       NaN   4.956444       NaN  0.079313       NaN
                                     gsp                  4.006826       NaN   6.342578       NaN  0.111545       NaN
                                     historical_tod_mean  4.349438       NaN   7.187550       NaN  0.128231       NaN
                                     neighbor_average     5.254687       NaN   8.193888       NaN  0.149588       NaN
       degree                        gls_map              3.463997       NaN   5.480486       NaN  0.090435       NaN
                                     gsp                  3.992662       NaN   6.264705       NaN  0.112675       NaN
                                     historical_tod_mean  4.334223       NaN   7.171409       NaN  0.129353       NaN
                                     neighbor_average     6.045780       NaN   9.773058       NaN  0.174729       NaN
       graph_sampling_laplacian      gls_map              3.776328       NaN   5.824029       NaN  0.096171       NaN
                                     gsp                  4.209904       NaN   6.571129       NaN  0.115798       NaN
                                     historical_tod_mean  4.407481       NaN   7.271358       NaN  0.131127       NaN
                                     neighbor_average     6.095192       NaN   9.907587       NaN  0.183869       NaN
       greedy_a_trace                gls_map              3.024605       NaN   4.755148       NaN  0.076981       NaN
                                     gsp                  3.993427       NaN   6.319591       NaN  0.111878       NaN
                                     historical_tod_mean  4.336426       NaN   7.152987       NaN  0.127716       NaN
                                     neighbor_average     5.292176       NaN   8.398867       NaN  0.148651       NaN
       greedy_d_logdet               gls_map              3.719993       NaN   5.627505       NaN  0.090781       NaN
                                     gsp                  4.203453       NaN   6.650774       NaN  0.118441       NaN
                                     historical_tod_mean  4.425691       NaN   7.264138       NaN  0.130728       NaN
                                     neighbor_average     5.825051       NaN   9.579991       NaN  0.188057       NaN
       multistart_swap_by_validation gls_map              2.996965       NaN   4.714438       NaN  0.075734       NaN
                                     gsp                  3.973455       NaN   6.278685       NaN  0.111443       NaN
                                     historical_tod_mean  4.324571       NaN   7.140278       NaN  0.128172       NaN
                                     neighbor_average     5.365023       NaN   8.446345       NaN  0.154069       NaN
       observability_proxy           gls_map              3.446068       NaN   5.415704       NaN  0.089146       NaN
                                     gsp                  3.986175       NaN   6.223601       NaN  0.111408       NaN
                                     historical_tod_mean  4.321980       NaN   7.149247       NaN  0.129418       NaN
                                     neighbor_average     6.072022       NaN   9.600063       NaN  0.171453       NaN
       qr_pod_modes                  gls_map              3.180609       NaN   4.987726       NaN  0.080463       NaN
                                     gsp                  4.041448       NaN   6.360650       NaN  0.112672       NaN
                                     historical_tod_mean  4.383936       NaN   7.193480       NaN  0.129610       NaN
                                     neighbor_average     5.566720       NaN   9.154251       NaN  0.177256       NaN
       random                        gls_map              3.228254  0.075528   5.102021  0.124977  0.081144  0.002641
                                     gsp                  3.986304  0.030585   6.271503  0.070173  0.110026  0.002152
                                     historical_tod_mean  4.321543  0.026170   7.146845  0.042218  0.127473  0.001554
                                     neighbor_average     5.473146  0.240845   8.792902  0.346640  0.153943  0.006150
       rcss_selected                 gls_map              2.975551       NaN   4.705004       NaN  0.075808       NaN
                                     gsp                  3.967814       NaN   6.280883       NaN  0.110806       NaN
                                     historical_tod_mean  4.326274       NaN   7.134937       NaN  0.127966       NaN
                                     neighbor_average     5.364493       NaN   8.403909       NaN  0.154547       NaN
       robust_coverage_cvar          gls_map              3.115745       NaN   4.885014       NaN  0.077304       NaN
                                     gsp                  3.982133       NaN   6.237013       NaN  0.109002       NaN
                                     historical_tod_mean  4.320768       NaN   7.131025       NaN  0.127167       NaN
                                     neighbor_average     5.285260       NaN   8.337742       NaN  0.150182       NaN
       scenario_average_a_trace      gls_map              3.092627       NaN   4.853976       NaN  0.078096       NaN
                                     gsp                  3.996764       NaN   6.302419       NaN  0.110729       NaN
                                     historical_tod_mean  4.349388       NaN   7.168422       NaN  0.127448       NaN
                                     neighbor_average     5.410172       NaN   8.451215       NaN  0.153750       NaN
       scenario_cvar_a_trace         gls_map              3.133158       NaN   4.886396       NaN  0.073532       NaN
                                     gsp                  3.971840       NaN   6.175051       NaN  0.105355       NaN
                                     historical_tod_mean  4.312111       NaN   7.091509       NaN  0.125329       NaN
                                     neighbor_average     5.419393       NaN   8.677391       NaN  0.149281       NaN
       swap_from_best_random_trace   gls_map              2.975551       NaN   4.705004       NaN  0.075808       NaN
                                     gsp                  3.967814       NaN   6.280883       NaN  0.110806       NaN
                                     historical_tod_mean  4.326274       NaN   7.134937       NaN  0.127966       NaN
                                     neighbor_average     5.364493       NaN   8.403909       NaN  0.154547       NaN
       swap_from_greedy_a_trace      gls_map              3.015894       NaN   4.751143       NaN  0.077817       NaN
                                     gsp                  4.006288       NaN   6.366086       NaN  0.113346       NaN
                                     historical_tod_mean  4.351318       NaN   7.167467       NaN  0.128258       NaN
                                     neighbor_average     5.437497       NaN   8.608712       NaN  0.155847       NaN
       swap_from_scenario_average    gls_map              3.009644       NaN   4.716210       NaN  0.077715       NaN
                                     gsp                  4.005191       NaN   6.373625       NaN  0.113709       NaN
                                     historical_tod_mean  4.347817       NaN   7.163280       NaN  0.128520       NaN
                                     neighbor_average     5.582167       NaN   8.763791       NaN  0.159986       NaN
       swap_from_scenario_cvar       gls_map              3.007819       NaN   4.740007       NaN  0.076984       NaN
                                     gsp                  3.991494       NaN   6.320966       NaN  0.112503       NaN
                                     historical_tod_mean  4.344634       NaN   7.153249       NaN  0.127816       NaN
                                     neighbor_average     5.515890       NaN   8.687151       NaN  0.154004       NaN
       top_variance                  gls_map              3.315445       NaN   5.091103       NaN  0.077379       NaN
                                     gsp                  3.746969       NaN   5.836987       NaN  0.094172       NaN
                                     historical_tod_mean  3.992514       NaN   6.636688       NaN  0.106621       NaN
                                     neighbor_average     8.667570       NaN  14.371801       NaN  0.174932       NaN
       validation_swap_selected      gls_map              2.964385       NaN   4.659208       NaN  0.074640       NaN
                                     gsp                  3.940299       NaN   6.232882       NaN  0.109242       NaN
                                     historical_tod_mean  4.302361       NaN   7.105344       NaN  0.127002       NaN
                                     neighbor_average     5.438027       NaN   8.506235       NaN  0.155275       NaN
0.2    best_random_by_trace          gls_map              2.918555       NaN   4.715718       NaN  0.073831       NaN
                                     gsp                  4.016694       NaN   6.236000       NaN  0.109290       NaN
                                     historical_tod_mean  4.374972       NaN   7.217332       NaN  0.129405       NaN
                                     neighbor_average     4.771631       NaN   7.780317       NaN  0.131161       NaN
       best_random_by_validation     gls_map              2.948273       NaN   4.657989       NaN  0.070404       NaN
                                     gsp                  3.931915       NaN   6.035931       NaN  0.102354       NaN
                                     historical_tod_mean  4.282748       NaN   7.062021       NaN  0.124597       NaN
                                     neighbor_average     4.981725       NaN   8.080553       NaN  0.126121       NaN
       coverage                      gls_map              2.818095       NaN   4.482372       NaN  0.071183       NaN
                                     gsp                  3.964942       NaN   6.187572       NaN  0.109033       NaN
                                     historical_tod_mean  4.354497       NaN   7.190460       NaN  0.129530       NaN
                                     neighbor_average     4.480235       NaN   7.072710       NaN  0.127076       NaN
       degree                        gls_map              3.404567       NaN   5.377021       NaN  0.087069       NaN
                                     gsp                  4.050767       NaN   6.260429       NaN  0.111378       NaN
                                     historical_tod_mean  4.380334       NaN   7.230205       NaN  0.132454       NaN
                                     neighbor_average     6.069707       NaN   9.923517       NaN  0.176669       NaN
       graph_sampling_laplacian      gls_map              3.611481       NaN   5.636385       NaN  0.091039       NaN
                                     gsp                  4.202011       NaN   6.476930       NaN  0.112922       NaN
                                     historical_tod_mean  4.435670       NaN   7.311424       NaN  0.132274       NaN
                                     neighbor_average     6.095458       NaN   9.857432       NaN  0.181505       NaN
       greedy_a_trace                gls_map              2.827320       NaN   4.466336       NaN  0.072660       NaN
                                     gsp                  4.069172       NaN   6.352457       NaN  0.113882       NaN
                                     historical_tod_mean  4.442441       NaN   7.288836       NaN  0.132597       NaN
                                     neighbor_average     4.631463       NaN   7.460828       NaN  0.139814       NaN
       greedy_d_logdet               gls_map              3.359634       NaN   5.137215       NaN  0.083344       NaN
                                     gsp                  4.215624       NaN   6.543117       NaN  0.117159       NaN
                                     historical_tod_mean  4.534120       NaN   7.411893       NaN  0.135939       NaN
                                     neighbor_average     5.488844       NaN   9.225784       NaN  0.182745       NaN
       multistart_swap_by_validation gls_map              2.835618       NaN   4.416571       NaN  0.070571       NaN
                                     gsp                  4.027935       NaN   6.241406       NaN  0.110590       NaN
                                     historical_tod_mean  4.401162       NaN   7.231879       NaN  0.130550       NaN
                                     neighbor_average     4.693628       NaN   7.625213       NaN  0.138569       NaN
       observability_proxy           gls_map              3.323621       NaN   5.258330       NaN  0.083586       NaN
                                     gsp                  4.037934       NaN   6.237582       NaN  0.110084       NaN
                                     historical_tod_mean  4.354713       NaN   7.191454       NaN  0.131060       NaN
                                     neighbor_average     5.976887       NaN   9.676649       NaN  0.168922       NaN
       qr_pod_modes                  gls_map              2.908532       NaN   4.535822       NaN  0.073381       NaN
                                     gsp                  4.070563       NaN   6.325968       NaN  0.113225       NaN
                                     historical_tod_mean  4.440617       NaN   7.266645       NaN  0.132882       NaN
                                     neighbor_average     4.787216       NaN   7.820738       NaN  0.149262       NaN
       random                        gls_map              2.961993  0.067780   4.692240  0.112473  0.073666  0.002331
                                     gsp                  3.967899  0.042633   6.149103  0.067197  0.107106  0.002127
                                     historical_tod_mean  4.320444  0.044815   7.141304  0.063454  0.127484  0.002315
                                     neighbor_average     4.924844  0.121899   7.902622  0.200702  0.133828  0.005709
       rcss_selected                 gls_map              2.751689       NaN   4.311092       NaN  0.067304       NaN
                                     gsp                  3.906057       NaN   6.064283       NaN  0.105748       NaN
                                     historical_tod_mean  4.245320       NaN   7.042749       NaN  0.125153       NaN
                                     neighbor_average     4.578352       NaN   7.286489       NaN  0.118545       NaN
       robust_coverage_cvar          gls_map              2.828562       NaN   4.445820       NaN  0.070339       NaN
                                     gsp                  4.006448       NaN   6.205374       NaN  0.109202       NaN
                                     historical_tod_mean  4.376231       NaN   7.190893       NaN  0.128980       NaN
                                     neighbor_average     4.715510       NaN   7.561719       NaN  0.132860       NaN
       scenario_average_a_trace      gls_map              2.929337       NaN   4.592154       NaN  0.074429       NaN
                                     gsp                  4.108382       NaN   6.402347       NaN  0.114177       NaN
                                     historical_tod_mean  4.464123       NaN   7.322595       NaN  0.132771       NaN
                                     neighbor_average     4.852480       NaN   7.754379       NaN  0.143361       NaN
       scenario_cvar_a_trace         gls_map              2.896675       NaN   4.514544       NaN  0.070492       NaN
                                     gsp                  4.034598       NaN   6.232169       NaN  0.109052       NaN
                                     historical_tod_mean  4.383607       NaN   7.196594       NaN  0.129009       NaN
                                     neighbor_average     4.962222       NaN   7.956344       NaN  0.141096       NaN
       swap_from_best_random_trace   gls_map              2.874421       NaN   4.550277       NaN  0.073493       NaN
                                     gsp                  4.077929       NaN   6.348725       NaN  0.113592       NaN
                                     historical_tod_mean  4.447898       NaN   7.291310       NaN  0.132462       NaN
                                     neighbor_average     4.696516       NaN   7.575600       NaN  0.140135       NaN
       swap_from_greedy_a_trace      gls_map              2.805235       NaN   4.412709       NaN  0.071279       NaN
                                     gsp                  4.052899       NaN   6.323231       NaN  0.112835       NaN
                                     historical_tod_mean  4.435622       NaN   7.267654       NaN  0.131227       NaN
                                     neighbor_average     4.589669       NaN   7.387982       NaN  0.136899       NaN
       swap_from_scenario_average    gls_map              2.823757       NaN   4.453737       NaN  0.071655       NaN
                                     gsp                  4.060269       NaN   6.342268       NaN  0.112737       NaN
                                     historical_tod_mean  4.445432       NaN   7.281268       NaN  0.130969       NaN
                                     neighbor_average     4.660811       NaN   7.390385       NaN  0.136224       NaN
       swap_from_scenario_cvar       gls_map              2.809441       NaN   4.364220       NaN  0.069154       NaN
                                     gsp                  4.028568       NaN   6.234006       NaN  0.109528       NaN
                                     historical_tod_mean  4.398404       NaN   7.197208       NaN  0.128751       NaN
                                     neighbor_average     4.664738       NaN   7.494479       NaN  0.134098       NaN
       top_variance                  gls_map              2.928891       NaN   4.563324       NaN  0.065515       NaN
                                     gsp                  3.578237       NaN   5.484225       NaN  0.083854       NaN
                                     historical_tod_mean  3.736119       NaN   6.185234       NaN  0.093080       NaN
                                     neighbor_average     6.616644       NaN  10.925226       NaN  0.128277       NaN
       validation_swap_selected      gls_map              2.730938       NaN   4.255169       NaN  0.066132       NaN
                                     gsp                  3.880606       NaN   6.011543       NaN  0.103972       NaN
                                     historical_tod_mean  4.213655       NaN   6.990767       NaN  0.123515       NaN
                                     neighbor_average     4.723846       NaN   7.533592       NaN  0.118729       NaN
0.3    best_random_by_trace          gls_map              2.744142       NaN   4.327436       NaN  0.067002       NaN
                                     gsp                  3.970738       NaN   6.093203       NaN  0.105242       NaN
                                     historical_tod_mean  4.336434       NaN   7.128162       NaN  0.127162       NaN
                                     neighbor_average     4.418353       NaN   7.017864       NaN  0.119114       NaN
       best_random_by_validation     gls_map              2.676420       NaN   4.266567       NaN  0.065241       NaN
                                     gsp                  3.889415       NaN   5.993399       NaN  0.102282       NaN
                                     historical_tod_mean  4.208418       NaN   6.967439       NaN  0.120993       NaN
                                     neighbor_average     4.462941       NaN   7.179147       NaN  0.109274       NaN
       coverage                      gls_map              2.625128       NaN   4.155227       NaN  0.064504       NaN
                                     gsp                  3.984046       NaN   6.152298       NaN  0.107495       NaN
                                     historical_tod_mean  4.349392       NaN   7.181593       NaN  0.128914       NaN
                                     neighbor_average     4.380387       NaN   6.762895       NaN  0.115460       NaN
       degree                        gls_map              3.313358       NaN   5.196652       NaN  0.081570       NaN
                                     gsp                  4.062117       NaN   6.243205       NaN  0.108508       NaN
                                     historical_tod_mean  4.377780       NaN   7.175277       NaN  0.129437       NaN
                                     neighbor_average     6.764560       NaN  11.021834       NaN  0.175760       NaN
       graph_sampling_laplacian      gls_map              3.437469       NaN   5.420752       NaN  0.085366       NaN
                                     gsp                  4.155502       NaN   6.399832       NaN  0.109945       NaN
                                     historical_tod_mean  4.418734       NaN   7.285890       NaN  0.130007       NaN
                                     neighbor_average     6.307853       NaN  10.176940       NaN  0.183276       NaN
       greedy_a_trace                gls_map              2.671544       NaN   4.200537       NaN  0.067935       NaN
                                     gsp                  4.098671       NaN   6.330869       NaN  0.112931       NaN
                                     historical_tod_mean  4.482622       NaN   7.331839       NaN  0.132995       NaN
                                     neighbor_average     4.313942       NaN   6.885687       NaN  0.125030       NaN
       greedy_d_logdet               gls_map              3.052515       NaN   4.694915       NaN  0.076891       NaN
                                     gsp                  4.224047       NaN   6.483413       NaN  0.117503       NaN
                                     historical_tod_mean  4.593069       NaN   7.487350       NaN  0.139488       NaN
                                     neighbor_average     5.052796       NaN   8.368803       NaN  0.165498       NaN
       multistart_swap_by_validation gls_map              2.639671       NaN   4.199116       NaN  0.066527       NaN
                                     gsp                  4.021669       NaN   6.217997       NaN  0.110318       NaN
                                     historical_tod_mean  4.408721       NaN   7.247356       NaN  0.130780       NaN
                                     neighbor_average     4.374124       NaN   6.829189       NaN  0.122267       NaN
       observability_proxy           gls_map              3.308161       NaN   5.189149       NaN  0.080672       NaN
                                     gsp                  4.061241       NaN   6.241573       NaN  0.107822       NaN
                                     historical_tod_mean  4.366555       NaN   7.165962       NaN  0.128685       NaN
                                     neighbor_average     6.687946       NaN  10.950066       NaN  0.174455       NaN
       qr_pod_modes                  gls_map              2.692737       NaN   4.196589       NaN  0.066041       NaN
                                     gsp                  4.056366       NaN   6.244486       NaN  0.109076       NaN
                                     historical_tod_mean  4.435444       NaN   7.275412       NaN  0.129840       NaN
                                     neighbor_average     4.337125       NaN   6.783145       NaN  0.122626       NaN
       random                        gls_map              2.812652  0.066209   4.468510  0.114854  0.069506  0.002257
                                     gsp                  3.970661  0.056745   6.121891  0.094322  0.105999  0.002962
                                     historical_tod_mean  4.323520  0.064960   7.145013  0.104212  0.127307  0.003792
                                     neighbor_average     4.606922  0.101523   7.367326  0.202218  0.121553  0.006147
       rcss_selected                 gls_map              2.584072       NaN   4.106600       NaN  0.064361       NaN
                                     gsp                  3.875320       NaN   6.037800       NaN  0.105132       NaN
                                     historical_tod_mean  4.230730       NaN   7.074916       NaN  0.125431       NaN
                                     neighbor_average     4.339610       NaN   6.703977       NaN  0.110655       NaN
       robust_coverage_cvar          gls_map              2.663501       NaN   4.169783       NaN  0.066194       NaN
                                     gsp                  4.028661       NaN   6.195537       NaN  0.108605       NaN
                                     historical_tod_mean  4.408769       NaN   7.230622       NaN  0.130081       NaN
                                     neighbor_average     4.354816       NaN   6.943147       NaN  0.121772       NaN
       scenario_average_a_trace      gls_map              2.834873       NaN   4.469990       NaN  0.071439       NaN
                                     gsp                  4.194195       NaN   6.451228       NaN  0.115318       NaN
                                     historical_tod_mean  4.567394       NaN   7.447706       NaN  0.136895       NaN
                                     neighbor_average     4.561298       NaN   7.426203       NaN  0.139669       NaN
       scenario_cvar_a_trace         gls_map              2.766422       NaN   4.354789       NaN  0.068062       NaN
                                     gsp                  4.118085       NaN   6.313005       NaN  0.110783       NaN
                                     historical_tod_mean  4.488544       NaN   7.326671       NaN  0.132658       NaN
                                     neighbor_average     4.423215       NaN   7.086745       NaN  0.127213       NaN
       swap_from_best_random_trace   gls_map              2.689786       NaN   4.235622       NaN  0.067449       NaN
                                     gsp                  4.086098       NaN   6.270462       NaN  0.111881       NaN
                                     historical_tod_mean  4.473761       NaN   7.309883       NaN  0.134032       NaN
                                     neighbor_average     4.353023       NaN   6.898727       NaN  0.127155       NaN
       swap_from_greedy_a_trace      gls_map              2.648592       NaN   4.136811       NaN  0.066697       NaN
                                     gsp                  4.101901       NaN   6.322328       NaN  0.113366       NaN
                                     historical_tod_mean  4.498500       NaN   7.343135       NaN  0.133988       NaN
                                     neighbor_average     4.328121       NaN   6.881597       NaN  0.127120       NaN
       swap_from_scenario_average    gls_map              2.669689       NaN   4.153778       NaN  0.066881       NaN
                                     gsp                  4.116261       NaN   6.333445       NaN  0.113548       NaN
                                     historical_tod_mean  4.511071       NaN   7.359685       NaN  0.134694       NaN
                                     neighbor_average     4.331694       NaN   6.895138       NaN  0.128131       NaN
       swap_from_scenario_cvar       gls_map              2.660555       NaN   4.136803       NaN  0.065650       NaN
                                     gsp                  4.067244       NaN   6.238420       NaN  0.110552       NaN
                                     historical_tod_mean  4.451404       NaN   7.266788       NaN  0.131864       NaN
                                     neighbor_average     4.300270       NaN   6.715005       NaN  0.122793       NaN
       top_variance                  gls_map              2.734538       NaN   4.341725       NaN  0.060545       NaN
                                     gsp                  3.421582       NaN   5.249272       NaN  0.077568       NaN
                                     historical_tod_mean  3.552304       NaN   5.869781       NaN  0.084845       NaN
                                     neighbor_average     5.741221       NaN   9.351760       NaN  0.111989       NaN
       validation_swap_selected      gls_map              2.562225       NaN   4.046675       NaN  0.062756       NaN
                                     gsp                  3.852043       NaN   5.981344       NaN  0.103065       NaN
                                     historical_tod_mean  4.198077       NaN   7.021748       NaN  0.123652       NaN
                                     neighbor_average     4.462049       NaN   6.821453       NaN  0.112396       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 2.964385 4.659208
    0.2 validation_swap_selected gls_map 2.730938 4.255169
    0.3 validation_swap_selected gls_map 2.562225 4.046675
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.026506     -0.037163 210
    gsp   condition_number     0.027357      0.002764 210
    gsp information_logdet     0.014037      0.040342 210
gls_map    posterior_trace     0.867652      0.879522 210
gls_map   condition_number     0.857098      0.887511 210
gls_map information_logdet    -0.778143     -0.819188 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv