---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-06-18, 2012-06-27
Test days: 2012-05-17, 2012-05-21
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.609768       NaN   6.263269       NaN  0.097769       NaN
                                     gsp                   4.020033       NaN   6.958271       NaN  0.109092       NaN
                                     historical_tod_mean   4.106567       NaN   7.150275       NaN  0.109722       NaN
                                     neighbor_average      7.260504       NaN  11.442758       NaN  0.204402       NaN
       best_random_by_validation     gls_map               3.609851       NaN   6.178915       NaN  0.092408       NaN
                                     gsp                   3.961078       NaN   6.893324       NaN  0.103966       NaN
                                     historical_tod_mean   4.068147       NaN   7.084924       NaN  0.105734       NaN
                                     neighbor_average      7.391985       NaN  11.416955       NaN  0.196192       NaN
       coverage                      gls_map               3.671964       NaN   6.305959       NaN  0.094829       NaN
                                     gsp                   4.017269       NaN   6.947701       NaN  0.104816       NaN
                                     historical_tod_mean   4.087774       NaN   7.122510       NaN  0.106639       NaN
                                     neighbor_average      7.712062       NaN  11.602900       NaN  0.199157       NaN
       degree                        gls_map               4.052749       NaN   6.916458       NaN  0.107553       NaN
                                     gsp                   3.978986       NaN   6.986223       NaN  0.107257       NaN
                                     historical_tod_mean   4.025291       NaN   7.052255       NaN  0.107178       NaN
                                     neighbor_average      8.299594       NaN  12.135937       NaN  0.218529       NaN
       graph_sampling_laplacian      gls_map               4.347112       NaN   7.199917       NaN  0.109021       NaN
                                     gsp                   4.096251       NaN   7.017961       NaN  0.106374       NaN
                                     historical_tod_mean   4.126658       NaN   7.129298       NaN  0.106371       NaN
                                     neighbor_average      8.330705       NaN  13.192128       NaN  0.239120       NaN
       greedy_a_trace                gls_map               3.454787       NaN   5.922480       NaN  0.090310       NaN
                                     gsp                   3.963949       NaN   6.849777       NaN  0.104220       NaN
                                     historical_tod_mean   4.053685       NaN   7.039432       NaN  0.105436       NaN
                                     neighbor_average      7.192979       NaN  11.293151       NaN  0.203432       NaN
       greedy_d_logdet               gls_map               4.132423       NaN   6.623065       NaN  0.099200       NaN
                                     gsp                   3.956372       NaN   6.807782       NaN  0.097267       NaN
                                     historical_tod_mean   3.967041       NaN   6.897079       NaN  0.098352       NaN
                                     neighbor_average      8.296212       NaN  12.742141       NaN  0.230573       NaN
       multistart_swap_by_validation gls_map               3.507680       NaN   5.945654       NaN  0.089682       NaN
                                     gsp                   3.974967       NaN   6.851028       NaN  0.103802       NaN
                                     historical_tod_mean   4.051263       NaN   7.036071       NaN  0.105089       NaN
                                     neighbor_average      7.176007       NaN  11.062296       NaN  0.197621       NaN
       observability_proxy           gls_map               4.021571       NaN   6.870002       NaN  0.106526       NaN
                                     gsp                   3.972120       NaN   6.966326       NaN  0.106513       NaN
                                     historical_tod_mean   4.021275       NaN   7.039847       NaN  0.106837       NaN
                                     neighbor_average     10.265985       NaN  15.180580       NaN  0.230277       NaN
       qr_pod_modes                  gls_map               3.744604       NaN   6.147920       NaN  0.092593       NaN
                                     gsp                   3.920514       NaN   6.769190       NaN  0.099670       NaN
                                     historical_tod_mean   3.987401       NaN   6.926666       NaN  0.100893       NaN
                                     neighbor_average      7.607976       NaN  11.893911       NaN  0.217631       NaN
       random                        gls_map               3.663011  0.040959   6.295307  0.066738  0.097137  0.002026
                                     gsp                   4.001726  0.023179   6.933820  0.042153  0.107001  0.001765
                                     historical_tod_mean   4.091212  0.021132   7.121335  0.039896  0.107908  0.001582
                                     neighbor_average      7.493247  0.144523  11.680681  0.210344  0.200762  0.004243
       rcss_selected                 gls_map               3.517085       NaN   6.045581       NaN  0.094956       NaN
                                     gsp                   3.934000       NaN   6.858525       NaN  0.107494       NaN
                                     historical_tod_mean   4.022152       NaN   7.045435       NaN  0.107614       NaN
                                     neighbor_average      7.418406       NaN  11.471081       NaN  0.212238       NaN
       robust_coverage_cvar          gls_map               3.622030       NaN   6.316009       NaN  0.098581       NaN
                                     gsp                   3.960970       NaN   6.921081       NaN  0.108087       NaN
                                     historical_tod_mean   4.052901       NaN   7.108222       NaN  0.108504       NaN
                                     neighbor_average      7.793071       NaN  11.819523       NaN  0.213845       NaN
       scenario_average_a_trace      gls_map               3.679856       NaN   6.376799       NaN  0.101199       NaN
                                     gsp                   3.967003       NaN   6.923849       NaN  0.109235       NaN
                                     historical_tod_mean   4.061485       NaN   7.101474       NaN  0.108696       NaN
                                     neighbor_average      7.614258       NaN  11.702947       NaN  0.215588       NaN
       scenario_cvar_a_trace         gls_map               3.627333       NaN   6.257072       NaN  0.098281       NaN
                                     gsp                   3.963770       NaN   6.899462       NaN  0.107687       NaN
                                     historical_tod_mean   4.041090       NaN   7.078210       NaN  0.108207       NaN
                                     neighbor_average      7.842876       NaN  11.897345       NaN  0.218730       NaN
       swap_from_best_random_trace   gls_map               3.544463       NaN   6.102097       NaN  0.095371       NaN
                                     gsp                   4.007917       NaN   6.931465       NaN  0.108167       NaN
                                     historical_tod_mean   4.076318       NaN   7.111949       NaN  0.108698       NaN
                                     neighbor_average      7.166046       NaN  11.245300       NaN  0.204768       NaN
       swap_from_greedy_a_trace      gls_map               3.470103       NaN   5.916168       NaN  0.087688       NaN
                                     gsp                   3.966746       NaN   6.825537       NaN  0.101266       NaN
                                     historical_tod_mean   4.048343       NaN   7.008221       NaN  0.102956       NaN
                                     neighbor_average      7.290975       NaN  11.466001       NaN  0.205672       NaN
       swap_from_scenario_average    gls_map               3.540594       NaN   6.127038       NaN  0.097812       NaN
                                     gsp                   3.947862       NaN   6.889516       NaN  0.109379       NaN
                                     historical_tod_mean   4.051122       NaN   7.078484       NaN  0.108402       NaN
                                     neighbor_average      7.281323       NaN  11.342567       NaN  0.211240       NaN
       swap_from_scenario_cvar       gls_map               3.517085       NaN   6.045581       NaN  0.094956       NaN
                                     gsp                   3.934000       NaN   6.858525       NaN  0.107494       NaN
                                     historical_tod_mean   4.022152       NaN   7.045435       NaN  0.107614       NaN
                                     neighbor_average      7.418406       NaN  11.471081       NaN  0.212238       NaN
       top_variance                  gls_map               3.681501       NaN   6.254685       NaN  0.089436       NaN
                                     gsp                   3.790969       NaN   6.527948       NaN  0.093574       NaN
                                     historical_tod_mean   3.844754       NaN   6.678785       NaN  0.094514       NaN
                                     neighbor_average     10.458391       NaN  15.985692       NaN  0.209124       NaN
       validation_swap_selected      gls_map               3.495393       NaN   5.868087       NaN  0.086450       NaN
                                     gsp                   3.932553       NaN   6.753021       NaN  0.099792       NaN
                                     historical_tod_mean   4.006922       NaN   6.939344       NaN  0.101355       NaN
                                     neighbor_average      7.354591       NaN  11.175144       NaN  0.196353       NaN
0.2    best_random_by_trace          gls_map               3.358886       NaN   5.781822       NaN  0.090037       NaN
                                     gsp                   3.952612       NaN   6.852588       NaN  0.107518       NaN
                                     historical_tod_mean   4.046415       NaN   7.072702       NaN  0.108373       NaN
                                     neighbor_average      7.233558       NaN  11.213176       NaN  0.199198       NaN
       best_random_by_validation     gls_map               3.333722       NaN   5.777427       NaN  0.090529       NaN
                                     gsp                   3.942419       NaN   6.886548       NaN  0.108445       NaN
                                     historical_tod_mean   4.055749       NaN   7.106823       NaN  0.108997       NaN
                                     neighbor_average      7.136238       NaN  11.211130       NaN  0.189604       NaN
       coverage                      gls_map               3.376561       NaN   5.830758       NaN  0.087976       NaN
                                     gsp                   4.029199       NaN   6.958980       NaN  0.105509       NaN
                                     historical_tod_mean   4.096752       NaN   7.152763       NaN  0.107543       NaN
                                     neighbor_average      7.131532       NaN  11.066231       NaN  0.187745       NaN
       degree                        gls_map               3.949338       NaN   6.717254       NaN  0.101461       NaN
                                     gsp                   3.904348       NaN   6.852158       NaN  0.101818       NaN
                                     historical_tod_mean   3.993015       NaN   6.999271       NaN  0.103191       NaN
                                     neighbor_average      9.048431       NaN  13.059466       NaN  0.212748       NaN
       graph_sampling_laplacian      gls_map               4.216318       NaN   7.078452       NaN  0.105648       NaN
                                     gsp                   4.164711       NaN   7.076990       NaN  0.107021       NaN
                                     historical_tod_mean   4.188916       NaN   7.227967       NaN  0.107871       NaN
                                     neighbor_average      8.230925       NaN  12.219933       NaN  0.215582       NaN
       greedy_a_trace                gls_map               3.096064       NaN   5.128633       NaN  0.075519       NaN
                                     gsp                   3.858271       NaN   6.629446       NaN  0.095393       NaN
                                     historical_tod_mean   3.935199       NaN   6.836476       NaN  0.096962       NaN
                                     neighbor_average      7.198095       NaN  11.053375       NaN  0.191817       NaN
       greedy_d_logdet               gls_map               3.549136       NaN   5.825721       NaN  0.088676       NaN
                                     gsp                   3.860964       NaN   6.682750       NaN  0.097236       NaN
                                     historical_tod_mean   3.928252       NaN   6.854709       NaN  0.098057       NaN
                                     neighbor_average      7.721720       NaN  12.207015       NaN  0.221015       NaN
       multistart_swap_by_validation gls_map               3.236017       NaN   5.478568       NaN  0.083176       NaN
                                     gsp                   3.924824       NaN   6.760708       NaN  0.102516       NaN
                                     historical_tod_mean   4.020935       NaN   6.982204       NaN  0.103770       NaN
                                     neighbor_average      7.056082       NaN  10.979531       NaN  0.184547       NaN
       observability_proxy           gls_map               3.916508       NaN   6.681647       NaN  0.101352       NaN
                                     gsp                   3.887723       NaN   6.839659       NaN  0.102154       NaN
                                     historical_tod_mean   3.977232       NaN   6.990547       NaN  0.103433       NaN
                                     neighbor_average      9.699214       NaN  14.048460       NaN  0.227149       NaN
       qr_pod_modes                  gls_map               3.291321       NaN   5.407810       NaN  0.082632       NaN
                                     gsp                   3.828300       NaN   6.616839       NaN  0.097084       NaN
                                     historical_tod_mean   3.926039       NaN   6.824930       NaN  0.098050       NaN
                                     neighbor_average      7.299851       NaN  11.365927       NaN  0.206634       NaN
       random                        gls_map               3.398435  0.047043   5.875598  0.086333  0.090170  0.002243
                                     gsp                   3.988951  0.035382   6.913719  0.060604  0.107658  0.002289
                                     historical_tod_mean   4.093282  0.034499   7.127666  0.060851  0.108443  0.002112
                                     neighbor_average      7.184329  0.112991  11.316618  0.163950  0.192969  0.004071
       rcss_selected                 gls_map               3.114628       NaN   5.171031       NaN  0.075868       NaN
                                     gsp                   3.873941       NaN   6.648945       NaN  0.095858       NaN
                                     historical_tod_mean   3.946492       NaN   6.853549       NaN  0.097414       NaN
                                     neighbor_average      7.109498       NaN  11.001684       NaN  0.192608       NaN
       robust_coverage_cvar          gls_map               3.444679       NaN   5.997834       NaN  0.090940       NaN
                                     gsp                   3.956504       NaN   6.910870       NaN  0.105071       NaN
                                     historical_tod_mean   4.043392       NaN   7.106638       NaN  0.106467       NaN
                                     neighbor_average      7.444362       NaN  11.652001       NaN  0.203918       NaN
       scenario_average_a_trace      gls_map               3.429673       NaN   5.906262       NaN  0.092018       NaN
                                     gsp                   3.951751       NaN   6.942702       NaN  0.107335       NaN
                                     historical_tod_mean   4.062863       NaN   7.131326       NaN  0.107933       NaN
                                     neighbor_average      7.277937       NaN  11.414075       NaN  0.207900       NaN
       scenario_cvar_a_trace         gls_map               3.386868       NaN   5.874948       NaN  0.089101       NaN
                                     gsp                   3.908446       NaN   6.848460       NaN  0.104990       NaN
                                     historical_tod_mean   4.003529       NaN   7.062236       NaN  0.106093       NaN
                                     neighbor_average      7.481934       NaN  11.581654       NaN  0.203904       NaN
       swap_from_best_random_trace   gls_map               3.283657       NaN   5.576538       NaN  0.084835       NaN
                                     gsp                   3.959268       NaN   6.802732       NaN  0.103851       NaN
                                     historical_tod_mean   4.029509       NaN   7.016978       NaN  0.104972       NaN
                                     neighbor_average      7.030981       NaN  10.950145       NaN  0.193395       NaN
       swap_from_greedy_a_trace      gls_map               3.114628       NaN   5.171031       NaN  0.075868       NaN
                                     gsp                   3.873941       NaN   6.648945       NaN  0.095858       NaN
                                     historical_tod_mean   3.946492       NaN   6.853549       NaN  0.097414       NaN
                                     neighbor_average      7.109498       NaN  11.001684       NaN  0.192608       NaN
       swap_from_scenario_average    gls_map               3.305609       NaN   5.556298       NaN  0.084220       NaN
                                     gsp                   3.892204       NaN   6.760068       NaN  0.101301       NaN
                                     historical_tod_mean   3.990549       NaN   6.958524       NaN  0.102153       NaN
                                     neighbor_average      7.264831       NaN  11.360799       NaN  0.203378       NaN
       swap_from_scenario_cvar       gls_map               3.282620       NaN   5.581868       NaN  0.083042       NaN
                                     gsp                   3.869236       NaN   6.741361       NaN  0.100422       NaN
                                     historical_tod_mean   3.970660       NaN   6.958786       NaN  0.101783       NaN
                                     neighbor_average      7.284990       NaN  11.292118       NaN  0.198405       NaN
       top_variance                  gls_map               3.416601       NaN   5.822737       NaN  0.081442       NaN
                                     gsp                   3.621107       NaN   6.258989       NaN  0.088006       NaN
                                     historical_tod_mean   3.665293       NaN   6.400528       NaN  0.088738       NaN
                                     neighbor_average      9.637216       NaN  14.794679       NaN  0.191560       NaN
       validation_swap_selected      gls_map               3.118839       NaN   5.168783       NaN  0.075973       NaN
                                     gsp                   3.863675       NaN   6.637777       NaN  0.095619       NaN
                                     historical_tod_mean   3.930275       NaN   6.840922       NaN  0.097120       NaN
                                     neighbor_average      7.117883       NaN  10.986117       NaN  0.192856       NaN
0.3    best_random_by_trace          gls_map               3.104939       NaN   5.392358       NaN  0.083356       NaN
                                     gsp                   3.968508       NaN   6.877922       NaN  0.107871       NaN
                                     historical_tod_mean   4.053317       NaN   7.102738       NaN  0.109133       NaN
                                     neighbor_average      6.945502       NaN  10.895942       NaN  0.184854       NaN
       best_random_by_validation     gls_map               3.133155       NaN   5.421485       NaN  0.082173       NaN
                                     gsp                   3.910481       NaN   6.807928       NaN  0.105659       NaN
                                     historical_tod_mean   4.014107       NaN   7.034537       NaN  0.106612       NaN
                                     neighbor_average      7.081786       NaN  11.132472       NaN  0.188536       NaN
       coverage                      gls_map               3.252758       NaN   5.589823       NaN  0.085103       NaN
                                     gsp                   4.055254       NaN   6.993203       NaN  0.107558       NaN
                                     historical_tod_mean   4.154518       NaN   7.219883       NaN  0.109397       NaN
                                     neighbor_average      7.009072       NaN  11.110402       NaN  0.188776       NaN
       degree                        gls_map               3.852368       NaN   6.552915       NaN  0.097594       NaN
                                     gsp                   3.805330       NaN   6.716527       NaN  0.099807       NaN
                                     historical_tod_mean   3.901863       NaN   6.911240       NaN  0.101267       NaN
                                     neighbor_average      7.890555       NaN  12.253604       NaN  0.200073       NaN
       graph_sampling_laplacian      gls_map               4.132462       NaN   6.959664       NaN  0.105731       NaN
                                     gsp                   4.108194       NaN   7.054863       NaN  0.107025       NaN
                                     historical_tod_mean   4.190372       NaN   7.253793       NaN  0.108306       NaN
                                     neighbor_average      8.118812       NaN  12.670825       NaN  0.235534       NaN
       greedy_a_trace                gls_map               2.895219       NaN   4.767339       NaN  0.071492       NaN
                                     gsp                   3.821932       NaN   6.604671       NaN  0.096434       NaN
                                     historical_tod_mean   3.921338       NaN   6.840553       NaN  0.097876       NaN
                                     neighbor_average      6.953975       NaN  10.837604       NaN  0.192236       NaN
       greedy_d_logdet               gls_map               3.164935       NaN   5.245323       NaN  0.080338       NaN
                                     gsp                   3.762041       NaN   6.562925       NaN  0.096708       NaN
                                     historical_tod_mean   3.860793       NaN   6.783364       NaN  0.097640       NaN
                                     neighbor_average      7.401893       NaN  11.721287       NaN  0.211608       NaN
       multistart_swap_by_validation gls_map               3.010528       NaN   5.066031       NaN  0.073756       NaN
                                     gsp                   3.833385       NaN   6.607454       NaN  0.098363       NaN
                                     historical_tod_mean   3.934693       NaN   6.840122       NaN  0.099489       NaN
                                     neighbor_average      6.991700       NaN  10.944214       NaN  0.182704       NaN
       observability_proxy           gls_map               3.816424       NaN   6.501176       NaN  0.097045       NaN
                                     gsp                   3.798631       NaN   6.713911       NaN  0.099766       NaN
                                     historical_tod_mean   3.898141       NaN   6.909425       NaN  0.101261       NaN
                                     neighbor_average      7.889209       NaN  12.252949       NaN  0.200009       NaN
       qr_pod_modes                  gls_map               2.959854       NaN   4.838618       NaN  0.073796       NaN
                                     gsp                   3.775983       NaN   6.583082       NaN  0.097182       NaN
                                     historical_tod_mean   3.881976       NaN   6.814943       NaN  0.098118       NaN
                                     neighbor_average      6.957473       NaN  10.959908       NaN  0.197683       NaN
       random                        gls_map               3.220101  0.046258   5.579605  0.112028  0.085249  0.003019
                                     gsp                   3.983791  0.040493   6.911771  0.073501  0.107733  0.003211
                                     historical_tod_mean   4.093300  0.044092   7.135060  0.072476  0.108531  0.002977
                                     neighbor_average      7.044754  0.092645  11.172967  0.159038  0.189904  0.005058
       rcss_selected                 gls_map               2.885175       NaN   4.779565       NaN  0.071155       NaN
                                     gsp                   3.801211       NaN   6.602288       NaN  0.096369       NaN
                                     historical_tod_mean   3.903544       NaN   6.829964       NaN  0.097717       NaN
                                     neighbor_average      6.955655       NaN  10.825597       NaN  0.192963       NaN
       robust_coverage_cvar          gls_map               3.228788       NaN   5.625424       NaN  0.085529       NaN
                                     gsp                   3.940751       NaN   6.936636       NaN  0.106179       NaN
                                     historical_tod_mean   4.040168       NaN   7.158149       NaN  0.107627       NaN
                                     neighbor_average      7.371659       NaN  11.593306       NaN  0.201474       NaN
       scenario_average_a_trace      gls_map               3.170662       NaN   5.418284       NaN  0.082753       NaN
                                     gsp                   3.887441       NaN   6.824372       NaN  0.103101       NaN
                                     historical_tod_mean   3.985577       NaN   7.037777       NaN  0.104205       NaN
                                     neighbor_average      7.203248       NaN  11.423844       NaN  0.201338       NaN
       scenario_cvar_a_trace         gls_map               3.208406       NaN   5.559136       NaN  0.084645       NaN
                                     gsp                   3.877354       NaN   6.827427       NaN  0.103931       NaN
                                     historical_tod_mean   3.977900       NaN   7.053421       NaN  0.105456       NaN
                                     neighbor_average      7.388483       NaN  11.541173       NaN  0.198612       NaN
       swap_from_best_random_trace   gls_map               3.011810       NaN   5.098120       NaN  0.074968       NaN
                                     gsp                   3.888675       NaN   6.702126       NaN  0.099899       NaN
                                     historical_tod_mean   3.977265       NaN   6.938187       NaN  0.101409       NaN
                                     neighbor_average      6.903772       NaN  10.720477       NaN  0.179700       NaN
       swap_from_greedy_a_trace      gls_map               2.885175       NaN   4.779565       NaN  0.071155       NaN
                                     gsp                   3.801211       NaN   6.602288       NaN  0.096369       NaN
                                     historical_tod_mean   3.903544       NaN   6.829964       NaN  0.097717       NaN
                                     neighbor_average      6.955655       NaN  10.825597       NaN  0.192963       NaN
       swap_from_scenario_average    gls_map               3.030278       NaN   5.066973       NaN  0.074782       NaN
                                     gsp                   3.839280       NaN   6.690590       NaN  0.097889       NaN
                                     historical_tod_mean   3.938565       NaN   6.910753       NaN  0.099213       NaN
                                     neighbor_average      7.125360       NaN  11.207989       NaN  0.195794       NaN
       swap_from_scenario_cvar       gls_map               3.064398       NaN   5.192431       NaN  0.076159       NaN
                                     gsp                   3.816171       NaN   6.663130       NaN  0.097650       NaN
                                     historical_tod_mean   3.921665       NaN   6.898411       NaN  0.099159       NaN
                                     neighbor_average      7.202793       NaN  11.221221       NaN  0.191728       NaN
       top_variance                  gls_map               3.160406       NaN   5.409930       NaN  0.072537       NaN
                                     gsp                   3.455037       NaN   6.006130       NaN  0.081521       NaN
                                     historical_tod_mean   3.490764       NaN   6.129774       NaN  0.082145       NaN
                                     neighbor_average      9.067659       NaN  13.937095       NaN  0.174959       NaN
       validation_swap_selected      gls_map               2.870196       NaN   4.798639       NaN  0.073191       NaN
                                     gsp                   3.792100       NaN   6.624936       NaN  0.099070       NaN
                                     historical_tod_mean   3.897008       NaN   6.854832       NaN  0.100194       NaN
                                     neighbor_average      6.964867       NaN  10.850271       NaN  0.195498       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1           greedy_a_trace gls_map 3.454787 5.922480
    0.2           greedy_a_trace gls_map 3.096064 5.128633
    0.3 validation_swap_selected gls_map 2.870196 4.798639
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.221195      0.228335 360
    gsp   condition_number     0.221315      0.193871 360
    gsp information_logdet    -0.199961     -0.236286 360
gls_map    posterior_trace     0.923432      0.931237 360
gls_map   condition_number     0.782034      0.889250 360
gls_map information_logdet    -0.863547     -0.886699 360
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv