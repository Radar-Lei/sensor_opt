---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-27, 2012-06-22
Test days: 2012-05-02, 2012-05-09
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.625114       NaN   6.304510       NaN  0.086113       NaN
                                     gsp                   3.861336       NaN   6.655836       NaN  0.091305       NaN
                                     historical_tod_mean   4.049959       NaN   6.963353       NaN  0.093740       NaN
                                     neighbor_average      7.329355       NaN  11.240254       NaN  0.186148       NaN
       best_random_by_validation     gls_map               3.544665       NaN   6.216368       NaN  0.083001       NaN
                                     gsp                   3.793588       NaN   6.530912       NaN  0.088377       NaN
                                     historical_tod_mean   3.980071       NaN   6.831869       NaN  0.091061       NaN
                                     neighbor_average      7.435524       NaN  11.157530       NaN  0.176168       NaN
       coverage                      gls_map               3.717870       NaN   6.398277       NaN  0.089677       NaN
                                     gsp                   3.798060       NaN   6.624576       NaN  0.092064       NaN
                                     historical_tod_mean   3.996823       NaN   6.901022       NaN  0.093158       NaN
                                     neighbor_average      7.401059       NaN  11.521711       NaN  0.192852       NaN
       degree                        gls_map               3.919825       NaN   6.640431       NaN  0.095385       NaN
                                     gsp                   3.868824       NaN   6.670298       NaN  0.092512       NaN
                                     historical_tod_mean   3.997742       NaN   6.899259       NaN  0.092711       NaN
                                     neighbor_average      8.100538       NaN  12.477806       NaN  0.204960       NaN
       graph_sampling_laplacian      gls_map               4.036367       NaN   6.654326       NaN  0.088154       NaN
                                     gsp                   3.844847       NaN   6.547003       NaN  0.086162       NaN
                                     historical_tod_mean   3.938270       NaN   6.770899       NaN  0.088315       NaN
                                     neighbor_average      8.983674       NaN  14.288313       NaN  0.199576       NaN
       greedy_a_trace                gls_map               3.504054       NaN   5.979966       NaN  0.082325       NaN
                                     gsp                   3.750866       NaN   6.557646       NaN  0.088961       NaN
                                     historical_tod_mean   3.987291       NaN   6.884962       NaN  0.092436       NaN
                                     neighbor_average      7.034844       NaN  10.808849       NaN  0.185523       NaN
       greedy_d_logdet               gls_map               4.113993       NaN   6.721203       NaN  0.099371       NaN
                                     gsp                   3.869355       NaN   6.629632       NaN  0.091905       NaN
                                     historical_tod_mean   4.018094       NaN   6.914821       NaN  0.093581       NaN
                                     neighbor_average      7.663346       NaN  12.615666       NaN  0.218599       NaN
       multistart_swap_by_validation gls_map               3.367999       NaN   5.900623       NaN  0.078462       NaN
                                     gsp                   3.741824       NaN   6.566239       NaN  0.088025       NaN
                                     historical_tod_mean   3.995141       NaN   6.894184       NaN  0.092026       NaN
                                     neighbor_average      7.104561       NaN  10.919281       NaN  0.180216       NaN
       observability_proxy           gls_map               3.769256       NaN   6.382033       NaN  0.089458       NaN
                                     gsp                   3.773949       NaN   6.606574       NaN  0.088592       NaN
                                     historical_tod_mean   3.961508       NaN   6.848712       NaN  0.091123       NaN
                                     neighbor_average      7.683043       NaN  12.240264       NaN  0.193051       NaN
       qr_pod_modes                  gls_map               3.688270       NaN   6.270789       NaN  0.087681       NaN
                                     gsp                   3.843571       NaN   6.567868       NaN  0.089085       NaN
                                     historical_tod_mean   4.029229       NaN   6.882593       NaN  0.092222       NaN
                                     neighbor_average      7.280688       NaN  11.776764       NaN  0.201745       NaN
       random                        gls_map               3.650868  0.086933   6.260681  0.139438  0.087421  0.003863
                                     gsp                   3.773160  0.047740   6.540100  0.065879  0.090140  0.002026
                                     historical_tod_mean   3.978831  0.037388   6.856816  0.060514  0.092128  0.001283
                                     neighbor_average      7.389403  0.219669  11.417838  0.355877  0.185250  0.008230
       rcss_selected                 gls_map               3.466328       NaN   5.908188       NaN  0.078764       NaN
                                     gsp                   3.791935       NaN   6.569304       NaN  0.087726       NaN
                                     historical_tod_mean   3.989401       NaN   6.862222       NaN  0.091233       NaN
                                     neighbor_average      7.220087       NaN  11.093330       NaN  0.182584       NaN
       robust_coverage_cvar          gls_map               3.646302       NaN   6.133644       NaN  0.086538       NaN
                                     gsp                   3.800406       NaN   6.548960       NaN  0.090011       NaN
                                     historical_tod_mean   3.996244       NaN   6.885248       NaN  0.092455       NaN
                                     neighbor_average      7.438878       NaN  11.401664       NaN  0.185855       NaN
       scenario_average_a_trace      gls_map               3.584080       NaN   6.228275       NaN  0.085734       NaN
                                     gsp                   3.841418       NaN   6.636812       NaN  0.090482       NaN
                                     historical_tod_mean   4.047961       NaN   6.949152       NaN  0.093546       NaN
                                     neighbor_average      7.387475       NaN  11.396065       NaN  0.186241       NaN
       scenario_cvar_a_trace         gls_map               3.772847       NaN   6.364463       NaN  0.093666       NaN
                                     gsp                   3.818948       NaN   6.573939       NaN  0.091700       NaN
                                     historical_tod_mean   3.994624       NaN   6.881240       NaN  0.092914       NaN
                                     neighbor_average      7.369396       NaN  11.296206       NaN  0.193597       NaN
       swap_from_best_random_trace   gls_map               3.451050       NaN   6.006730       NaN  0.082987       NaN
                                     gsp                   3.785800       NaN   6.613244       NaN  0.090717       NaN
                                     historical_tod_mean   4.031076       NaN   6.953984       NaN  0.094042       NaN
                                     neighbor_average      7.075430       NaN  10.990237       NaN  0.191054       NaN
       swap_from_greedy_a_trace      gls_map               3.466328       NaN   5.908188       NaN  0.078764       NaN
                                     gsp                   3.791935       NaN   6.569304       NaN  0.087726       NaN
                                     historical_tod_mean   3.989401       NaN   6.862222       NaN  0.091233       NaN
                                     neighbor_average      7.220087       NaN  11.093330       NaN  0.182584       NaN
       swap_from_scenario_average    gls_map               3.464859       NaN   5.901438       NaN  0.079160       NaN
                                     gsp                   3.783359       NaN   6.560076       NaN  0.087852       NaN
                                     historical_tod_mean   3.990450       NaN   6.865164       NaN  0.091549       NaN
                                     neighbor_average      7.205743       NaN  11.060764       NaN  0.183041       NaN
       swap_from_scenario_cvar       gls_map               3.457599       NaN   5.899694       NaN  0.079056       NaN
                                     gsp                   3.776098       NaN   6.550121       NaN  0.087823       NaN
                                     historical_tod_mean   3.981925       NaN   6.853871       NaN  0.091109       NaN
                                     neighbor_average      7.158160       NaN  11.025632       NaN  0.182356       NaN
       top_variance                  gls_map               3.477628       NaN   5.871177       NaN  0.077208       NaN
                                     gsp                   3.539028       NaN   6.140511       NaN  0.080191       NaN
                                     historical_tod_mean   3.727966       NaN   6.393421       NaN  0.083274       NaN
                                     neighbor_average     10.693407       NaN  16.493436       NaN  0.208298       NaN
       validation_swap_selected      gls_map               3.471783       NaN   5.898702       NaN  0.078260       NaN
                                     gsp                   3.801921       NaN   6.541221       NaN  0.086348       NaN
                                     historical_tod_mean   3.963043       NaN   6.819628       NaN  0.090122       NaN
                                     neighbor_average      7.083227       NaN  10.868284       NaN  0.178130       NaN
0.2    best_random_by_trace          gls_map               3.378962       NaN   5.727232       NaN  0.076763       NaN
                                     gsp                   3.807985       NaN   6.519097       NaN  0.088129       NaN
                                     historical_tod_mean   3.997321       NaN   6.893310       NaN  0.091537       NaN
                                     neighbor_average      7.363143       NaN  11.279323       NaN  0.183558       NaN
       best_random_by_validation     gls_map               3.280705       NaN   5.716554       NaN  0.077883       NaN
                                     gsp                   3.675400       NaN   6.398739       NaN  0.088301       NaN
                                     historical_tod_mean   3.918048       NaN   6.783090       NaN  0.090678       NaN
                                     neighbor_average      7.119908       NaN  10.965998       NaN  0.162793       NaN
       coverage                      gls_map               3.416141       NaN   5.936227       NaN  0.080959       NaN
                                     gsp                   3.768132       NaN   6.558833       NaN  0.090245       NaN
                                     historical_tod_mean   4.006775       NaN   6.934378       NaN  0.093819       NaN
                                     neighbor_average      7.014621       NaN  10.818484       NaN  0.179913       NaN
       degree                        gls_map               3.829607       NaN   6.524394       NaN  0.092461       NaN
                                     gsp                   3.841701       NaN   6.601869       NaN  0.090955       NaN
                                     historical_tod_mean   4.047049       NaN   6.917114       NaN  0.093250       NaN
                                     neighbor_average      7.597361       NaN  11.785041       NaN  0.191120       NaN
       graph_sampling_laplacian      gls_map               3.837904       NaN   6.328592       NaN  0.084355       NaN
                                     gsp                   3.664972       NaN   6.384413       NaN  0.082505       NaN
                                     historical_tod_mean   3.851269       NaN   6.719948       NaN  0.085899       NaN
                                     neighbor_average      7.469545       NaN  11.370326       NaN  0.183580       NaN
       greedy_a_trace                gls_map               3.336125       NaN   5.719964       NaN  0.078814       NaN
                                     gsp                   3.804803       NaN   6.600650       NaN  0.090442       NaN
                                     historical_tod_mean   4.038315       NaN   6.992463       NaN  0.094062       NaN
                                     neighbor_average      6.905161       NaN  10.655900       NaN  0.182962       NaN
       greedy_d_logdet               gls_map               3.913042       NaN   6.440231       NaN  0.093888       NaN
                                     gsp                   3.906417       NaN   6.679908       NaN  0.093461       NaN
                                     historical_tod_mean   4.105858       NaN   7.033330       NaN  0.095811       NaN
                                     neighbor_average      7.614150       NaN  12.291049       NaN  0.217743       NaN
       multistart_swap_by_validation gls_map               3.258294       NaN   5.580690       NaN  0.076053       NaN
                                     gsp                   3.749088       NaN   6.489545       NaN  0.088402       NaN
                                     historical_tod_mean   3.986870       NaN   6.871923       NaN  0.091993       NaN
                                     neighbor_average      6.894338       NaN  10.814149       NaN  0.182597       NaN
       observability_proxy           gls_map               3.738805       NaN   6.380649       NaN  0.090052       NaN
                                     gsp                   3.856290       NaN   6.648375       NaN  0.091793       NaN
                                     historical_tod_mean   4.056292       NaN   6.985349       NaN  0.094069       NaN
                                     neighbor_average      7.784139       NaN  11.831098       NaN  0.200314       NaN
       qr_pod_modes                  gls_map               3.454691       NaN   5.859225       NaN  0.084848       NaN
                                     gsp                   3.803882       NaN   6.526684       NaN  0.092846       NaN
                                     historical_tod_mean   4.008284       NaN   6.895515       NaN  0.093803       NaN
                                     neighbor_average      7.335123       NaN  11.727779       NaN  0.204015       NaN
       random                        gls_map               3.435229  0.081360   5.930299  0.145142  0.081739  0.003268
                                     gsp                   3.755452  0.068153   6.511122  0.094284  0.090054  0.002461
                                     historical_tod_mean   3.987086  0.059627   6.876951  0.094336  0.092402  0.001971
                                     neighbor_average      7.208649  0.173902  11.163469  0.282313  0.180030  0.006923
       rcss_selected                 gls_map               3.258294       NaN   5.580690       NaN  0.076053       NaN
                                     gsp                   3.749088       NaN   6.489545       NaN  0.088402       NaN
                                     historical_tod_mean   3.986870       NaN   6.871923       NaN  0.091993       NaN
                                     neighbor_average      6.894338       NaN  10.814149       NaN  0.182597       NaN
       robust_coverage_cvar          gls_map               3.423059       NaN   5.887356       NaN  0.082975       NaN
                                     gsp                   3.797176       NaN   6.625258       NaN  0.092924       NaN
                                     historical_tod_mean   4.064233       NaN   7.031883       NaN  0.095167       NaN
                                     neighbor_average      7.004043       NaN  10.852815       NaN  0.184803       NaN
       scenario_average_a_trace      gls_map               3.508072       NaN   6.034653       NaN  0.082557       NaN
                                     gsp                   3.888385       NaN   6.677262       NaN  0.091717       NaN
                                     historical_tod_mean   4.090243       NaN   7.016650       NaN  0.094717       NaN
                                     neighbor_average      7.283535       NaN  11.229529       NaN  0.188550       NaN
       scenario_cvar_a_trace         gls_map               3.527221       NaN   6.069053       NaN  0.088217       NaN
                                     gsp                   3.839048       NaN   6.628053       NaN  0.094634       NaN
                                     historical_tod_mean   4.061698       NaN   6.992734       NaN  0.095420       NaN
                                     neighbor_average      7.347151       NaN  11.364138       NaN  0.194621       NaN
       swap_from_best_random_trace   gls_map               3.355421       NaN   5.797275       NaN  0.078324       NaN
                                     gsp                   3.869667       NaN   6.624775       NaN  0.090403       NaN
                                     historical_tod_mean   4.075696       NaN   6.999533       NaN  0.094112       NaN
                                     neighbor_average      6.858941       NaN  10.656275       NaN  0.182306       NaN
       swap_from_greedy_a_trace      gls_map               3.334105       NaN   5.772766       NaN  0.079024       NaN
                                     gsp                   3.791231       NaN   6.575399       NaN  0.089550       NaN
                                     historical_tod_mean   4.037070       NaN   6.977200       NaN  0.093336       NaN
                                     neighbor_average      6.952404       NaN  10.808307       NaN  0.185205       NaN
       swap_from_scenario_average    gls_map               3.330990       NaN   5.789079       NaN  0.078716       NaN
                                     gsp                   3.866015       NaN   6.640245       NaN  0.090669       NaN
                                     historical_tod_mean   4.067442       NaN   6.997129       NaN  0.094049       NaN
                                     neighbor_average      7.020744       NaN  10.912791       NaN  0.185909       NaN
       swap_from_scenario_cvar       gls_map               3.353092       NaN   5.665275       NaN  0.076932       NaN
                                     gsp                   3.778631       NaN   6.515956       NaN  0.088080       NaN
                                     historical_tod_mean   4.006747       NaN   6.909506       NaN  0.091864       NaN
                                     neighbor_average      6.939383       NaN  10.848473       NaN  0.179784       NaN
       top_variance                  gls_map               3.208909       NaN   5.455355       NaN  0.068936       NaN
                                     gsp                   3.310899       NaN   5.744711       NaN  0.073048       NaN
                                     historical_tod_mean   3.535287       NaN   6.035016       NaN  0.076835       NaN
                                     neighbor_average      9.188633       NaN  14.474583       NaN  0.176437       NaN
       validation_swap_selected      gls_map               3.230820       NaN   5.545943       NaN  0.075301       NaN
                                     gsp                   3.686215       NaN   6.432631       NaN  0.087443       NaN
                                     historical_tod_mean   3.934626       NaN   6.815886       NaN  0.090867       NaN
                                     neighbor_average      6.902471       NaN  10.716531       NaN  0.179152       NaN
0.3    best_random_by_trace          gls_map               3.352928       NaN   5.771264       NaN  0.080277       NaN
                                     gsp                   3.822800       NaN   6.611005       NaN  0.092249       NaN
                                     historical_tod_mean   4.068553       NaN   7.004146       NaN  0.094361       NaN
                                     neighbor_average      7.179310       NaN  11.017620       NaN  0.178682       NaN
       best_random_by_validation     gls_map               3.192816       NaN   5.544994       NaN  0.075542       NaN
                                     gsp                   3.685079       NaN   6.408750       NaN  0.088234       NaN
                                     historical_tod_mean   3.942715       NaN   6.806886       NaN  0.091373       NaN
                                     neighbor_average      6.890190       NaN  10.761952       NaN  0.173096       NaN
       coverage                      gls_map               3.212743       NaN   5.543801       NaN  0.074978       NaN
                                     gsp                   3.661792       NaN   6.428370       NaN  0.087686       NaN
                                     historical_tod_mean   3.912786       NaN   6.839756       NaN  0.091477       NaN
                                     neighbor_average      6.986421       NaN  10.611217       NaN  0.173175       NaN
       degree                        gls_map               3.702839       NaN   6.318883       NaN  0.089955       NaN
                                     gsp                   3.823401       NaN   6.558043       NaN  0.090832       NaN
                                     historical_tod_mean   4.042521       NaN   6.913841       NaN  0.093169       NaN
                                     neighbor_average      7.975106       NaN  12.504204       NaN  0.208534       NaN
       graph_sampling_laplacian      gls_map               3.608084       NaN   6.108028       NaN  0.082287       NaN
                                     gsp                   3.663012       NaN   6.363912       NaN  0.084099       NaN
                                     historical_tod_mean   3.898903       NaN   6.778178       NaN  0.087362       NaN
                                     neighbor_average      6.899375       NaN  11.185565       NaN  0.178959       NaN
       greedy_a_trace                gls_map               3.243975       NaN   5.516758       NaN  0.078893       NaN
                                     gsp                   3.824652       NaN   6.607085       NaN  0.093360       NaN
                                     historical_tod_mean   4.072738       NaN   7.027525       NaN  0.096480       NaN
                                     neighbor_average      6.852214       NaN  10.727310       NaN  0.187546       NaN
       greedy_d_logdet               gls_map               3.603602       NaN   5.905574       NaN  0.089377       NaN
                                     gsp                   3.767851       NaN   6.463781       NaN  0.091878       NaN
                                     historical_tod_mean   3.990709       NaN   6.863755       NaN  0.094500       NaN
                                     neighbor_average      7.603228       NaN  12.154858       NaN  0.218500       NaN
       multistart_swap_by_validation gls_map               3.092208       NaN   5.249450       NaN  0.073371       NaN
                                     gsp                   3.701866       NaN   6.365601       NaN  0.088858       NaN
                                     historical_tod_mean   3.955829       NaN   6.791924       NaN  0.091566       NaN
                                     neighbor_average      6.845325       NaN  10.622372       NaN  0.179256       NaN
       observability_proxy           gls_map               3.641100       NaN   6.249856       NaN  0.088787       NaN
                                     gsp                   3.808466       NaN   6.530577       NaN  0.090792       NaN
                                     historical_tod_mean   4.032019       NaN   6.894729       NaN  0.093290       NaN
                                     neighbor_average      7.842263       NaN  11.777865       NaN  0.194744       NaN
       qr_pod_modes                  gls_map               3.371121       NaN   5.652189       NaN  0.080462       NaN
                                     gsp                   3.744373       NaN   6.450968       NaN  0.090757       NaN
                                     historical_tod_mean   3.980398       NaN   6.865816       NaN  0.093596       NaN
                                     neighbor_average      7.029282       NaN  11.079325       NaN  0.191987       NaN
       random                        gls_map               3.282363  0.078989   5.659007  0.143857  0.077283  0.003016
                                     gsp                   3.725232  0.067168   6.459368  0.105543  0.089224  0.002480
                                     historical_tod_mean   3.975738  0.061226   6.848559  0.106402  0.091782  0.001996
                                     neighbor_average      7.112492  0.196773  11.071769  0.314097  0.173638  0.006147
       rcss_selected                 gls_map               3.080531       NaN   5.324010       NaN  0.071984       NaN
                                     gsp                   3.559609       NaN   6.269143       NaN  0.086148       NaN
                                     historical_tod_mean   3.841713       NaN   6.651934       NaN  0.088671       NaN
                                     neighbor_average      7.238905       NaN  11.081625       NaN  0.163636       NaN
       robust_coverage_cvar          gls_map               3.239349       NaN   5.604847       NaN  0.076759       NaN
                                     gsp                   3.777148       NaN   6.609820       NaN  0.092278       NaN
                                     historical_tod_mean   4.050498       NaN   7.042872       NaN  0.095019       NaN
                                     neighbor_average      6.787975       NaN  10.518271       NaN  0.179544       NaN
       scenario_average_a_trace      gls_map               3.342203       NaN   5.723097       NaN  0.081080       NaN
                                     gsp                   3.809212       NaN   6.549950       NaN  0.093321       NaN
                                     historical_tod_mean   4.054468       NaN   6.956298       NaN  0.095883       NaN
                                     neighbor_average      7.294305       NaN  11.350766       NaN  0.189947       NaN
       scenario_cvar_a_trace         gls_map               3.365149       NaN   5.798223       NaN  0.084523       NaN
                                     gsp                   3.768286       NaN   6.565975       NaN  0.094676       NaN
                                     historical_tod_mean   4.026901       NaN   6.963463       NaN  0.095766       NaN
                                     neighbor_average      7.344273       NaN  11.491951       NaN  0.198339       NaN
       swap_from_best_random_trace   gls_map               3.163329       NaN   5.476432       NaN  0.076139       NaN
                                     gsp                   3.779994       NaN   6.521791       NaN  0.090608       NaN
                                     historical_tod_mean   3.991398       NaN   6.931795       NaN  0.092526       NaN
                                     neighbor_average      6.885525       NaN  10.960438       NaN  0.181770       NaN
       swap_from_greedy_a_trace      gls_map               3.281997       NaN   5.534948       NaN  0.077888       NaN
                                     gsp                   3.814598       NaN   6.533108       NaN  0.091311       NaN
                                     historical_tod_mean   4.065952       NaN   6.956592       NaN  0.094663       NaN
                                     neighbor_average      6.825515       NaN  10.684722       NaN  0.184980       NaN
       swap_from_scenario_average    gls_map               3.228187       NaN   5.496794       NaN  0.076599       NaN
                                     gsp                   3.813853       NaN   6.536497       NaN  0.090102       NaN
                                     historical_tod_mean   4.026310       NaN   6.924496       NaN  0.093151       NaN
                                     neighbor_average      6.876404       NaN  10.821909       NaN  0.181629       NaN
       swap_from_scenario_cvar       gls_map               3.156318       NaN   5.368228       NaN  0.075432       NaN
                                     gsp                   3.719831       NaN   6.447015       NaN  0.090440       NaN
                                     historical_tod_mean   3.959954       NaN   6.883374       NaN  0.093050       NaN
                                     neighbor_average      6.806670       NaN  10.629502       NaN  0.179544       NaN
       top_variance                  gls_map               2.924422       NaN   4.996497       NaN  0.062127       NaN
                                     gsp                   3.083082       NaN   5.406193       NaN  0.067752       NaN
                                     historical_tod_mean   3.310999       NaN   5.668794       NaN  0.071288       NaN
                                     neighbor_average      8.573407       NaN  13.322415       NaN  0.160981       NaN
       validation_swap_selected      gls_map               3.012669       NaN   5.167005       NaN  0.069770       NaN
                                     gsp                   3.509107       NaN   6.187778       NaN  0.084321       NaN
                                     historical_tod_mean   3.796376       NaN   6.581485       NaN  0.087188       NaN
                                     neighbor_average      7.180312       NaN  10.936276       NaN  0.161046       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1 multistart_swap_by_validation gls_map 3.367999 5.900623
    0.2                  top_variance gls_map 3.208909 5.455355
    0.3                  top_variance gls_map 2.924422 4.996497
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.251866      0.308362 210
    gsp   condition_number     0.251661      0.292899 210
    gsp information_logdet    -0.285590     -0.322281 210
gls_map    posterior_trace     0.792148      0.806587 210
gls_map   condition_number     0.801777      0.848518 210
gls_map information_logdet    -0.710889     -0.759708 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv