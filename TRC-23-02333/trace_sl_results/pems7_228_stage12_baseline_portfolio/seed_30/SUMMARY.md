---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-22, 2012-06-25
Test days: 2012-06-04, 2012-06-05
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.555334       NaN   5.928249       NaN  0.087488       NaN
                                     gsp                   3.919730       NaN   6.561769       NaN  0.093934       NaN
                                     historical_tod_mean   3.931655       NaN   6.735093       NaN  0.094932       NaN
                                     neighbor_average      7.297414       NaN  11.292102       NaN  0.191915       NaN
       best_random_by_validation     gls_map               3.495910       NaN   5.851951       NaN  0.083151       NaN
                                     gsp                   3.879394       NaN   6.500429       NaN  0.092901       NaN
                                     historical_tod_mean   3.922132       NaN   6.700253       NaN  0.094150       NaN
                                     neighbor_average      7.056369       NaN  10.654110       NaN  0.176172       NaN
       coverage                      gls_map               3.658524       NaN   6.134107       NaN  0.085131       NaN
                                     gsp                   3.999839       NaN   6.681445       NaN  0.092373       NaN
                                     historical_tod_mean   3.971537       NaN   6.784835       NaN  0.094852       NaN
                                     neighbor_average      7.642072       NaN  11.634513       NaN  0.197310       NaN
       degree                        gls_map               4.035201       NaN   6.671667       NaN  0.093899       NaN
                                     gsp                   4.145749       NaN   6.809001       NaN  0.096252       NaN
                                     historical_tod_mean   3.996279       NaN   6.866260       NaN  0.096430       NaN
                                     neighbor_average      8.251889       NaN  12.592109       NaN  0.213404       NaN
       graph_sampling_laplacian      gls_map               3.950499       NaN   6.490860       NaN  0.097951       NaN
                                     gsp                   3.925793       NaN   6.479706       NaN  0.096795       NaN
                                     historical_tod_mean   3.901073       NaN   6.569007       NaN  0.094323       NaN
                                     neighbor_average      8.174196       NaN  12.799907       NaN  0.208167       NaN
       greedy_a_trace                gls_map               3.548410       NaN   5.911916       NaN  0.084586       NaN
                                     gsp                   3.985253       NaN   6.603816       NaN  0.094829       NaN
                                     historical_tod_mean   3.958325       NaN   6.773580       NaN  0.095090       NaN
                                     neighbor_average      7.131102       NaN  10.794072       NaN  0.190390       NaN
       greedy_d_logdet               gls_map               4.476128       NaN   7.012534       NaN  0.117544       NaN
                                     gsp                   4.109212       NaN   6.747513       NaN  0.101612       NaN
                                     historical_tod_mean   3.999136       NaN   6.783819       NaN  0.097616       NaN
                                     neighbor_average      7.902405       NaN  13.101259       NaN  0.240228       NaN
       multistart_swap_by_validation gls_map               3.421318       NaN   5.658422       NaN  0.083862       NaN
                                     gsp                   4.007321       NaN   6.537033       NaN  0.095544       NaN
                                     historical_tod_mean   3.960193       NaN   6.728649       NaN  0.095403       NaN
                                     neighbor_average      7.300634       NaN  11.309227       NaN  0.198807       NaN
       observability_proxy           gls_map               3.826495       NaN   6.447102       NaN  0.090311       NaN
                                     gsp                   4.038831       NaN   6.708400       NaN  0.096810       NaN
                                     historical_tod_mean   3.995820       NaN   6.842469       NaN  0.096421       NaN
                                     neighbor_average      7.757621       NaN  12.134581       NaN  0.206717       NaN
       qr_pod_modes                  gls_map               3.887989       NaN   6.412856       NaN  0.097318       NaN
                                     gsp                   4.023583       NaN   6.588863       NaN  0.095365       NaN
                                     historical_tod_mean   3.988160       NaN   6.772083       NaN  0.095102       NaN
                                     neighbor_average      7.350613       NaN  11.926200       NaN  0.214501       NaN
       random                        gls_map               3.662481  0.098611   6.071064  0.157886  0.086740  0.002524
                                     gsp                   3.972005  0.046765   6.562745  0.071423  0.093435  0.001515
                                     historical_tod_mean   3.950495  0.038786   6.740867  0.060790  0.094571  0.001240
                                     neighbor_average      7.408663  0.295680  11.349468  0.420782  0.188946  0.008095
       rcss_selected                 gls_map               3.407556       NaN   5.633682       NaN  0.083598       NaN
                                     gsp                   3.964400       NaN   6.511431       NaN  0.095418       NaN
                                     historical_tod_mean   3.950765       NaN   6.715167       NaN  0.095240       NaN
                                     neighbor_average      7.165764       NaN  11.069966       NaN  0.195107       NaN
       robust_coverage_cvar          gls_map               3.600293       NaN   5.914708       NaN  0.086613       NaN
                                     gsp                   3.976932       NaN   6.517139       NaN  0.096432       NaN
                                     historical_tod_mean   3.927489       NaN   6.676333       NaN  0.093191       NaN
                                     neighbor_average      7.288563       NaN  11.082180       NaN  0.191567       NaN
       scenario_average_a_trace      gls_map               3.504590       NaN   5.799498       NaN  0.082306       NaN
                                     gsp                   4.042629       NaN   6.593124       NaN  0.093067       NaN
                                     historical_tod_mean   3.960202       NaN   6.721941       NaN  0.094440       NaN
                                     neighbor_average      7.417456       NaN  11.180666       NaN  0.187360       NaN
       scenario_cvar_a_trace         gls_map               3.528379       NaN   5.797223       NaN  0.084270       NaN
                                     gsp                   3.963617       NaN   6.548257       NaN  0.096127       NaN
                                     historical_tod_mean   3.957150       NaN   6.757021       NaN  0.094995       NaN
                                     neighbor_average      7.261291       NaN  11.133464       NaN  0.189648       NaN
       swap_from_best_random_trace   gls_map               3.492736       NaN   5.764288       NaN  0.086339       NaN
                                     gsp                   3.980825       NaN   6.540906       NaN  0.096623       NaN
                                     historical_tod_mean   3.971811       NaN   6.745389       NaN  0.095885       NaN
                                     neighbor_average      7.155422       NaN  11.092177       NaN  0.197255       NaN
       swap_from_greedy_a_trace      gls_map               3.467481       NaN   5.693843       NaN  0.085475       NaN
                                     gsp                   3.985788       NaN   6.538218       NaN  0.096377       NaN
                                     historical_tod_mean   3.963873       NaN   6.735576       NaN  0.095786       NaN
                                     neighbor_average      7.177755       NaN  11.176576       NaN  0.198967       NaN
       swap_from_scenario_average    gls_map               3.407556       NaN   5.633682       NaN  0.083598       NaN
                                     gsp                   3.964400       NaN   6.511431       NaN  0.095418       NaN
                                     historical_tod_mean   3.950765       NaN   6.715167       NaN  0.095240       NaN
                                     neighbor_average      7.165764       NaN  11.069966       NaN  0.195107       NaN
       swap_from_scenario_cvar       gls_map               3.541860       NaN   5.773794       NaN  0.086244       NaN
                                     gsp                   3.978090       NaN   6.511461       NaN  0.095213       NaN
                                     historical_tod_mean   3.959115       NaN   6.722304       NaN  0.095434       NaN
                                     neighbor_average      7.051704       NaN  11.043856       NaN  0.195845       NaN
       top_variance                  gls_map               3.575306       NaN   5.858932       NaN  0.082372       NaN
                                     gsp                   3.756450       NaN   6.120673       NaN  0.086895       NaN
                                     historical_tod_mean   3.700846       NaN   6.265312       NaN  0.086591       NaN
                                     neighbor_average     10.738321       NaN  16.845589       NaN  0.210797       NaN
       validation_swap_selected      gls_map               3.431011       NaN   5.629494       NaN  0.084743       NaN
                                     gsp                   3.928736       NaN   6.500914       NaN  0.097183       NaN
                                     historical_tod_mean   3.902774       NaN   6.653453       NaN  0.094397       NaN
                                     neighbor_average      7.012368       NaN  10.965981       NaN  0.196378       NaN
0.2    best_random_by_trace          gls_map               3.349053       NaN   5.540046       NaN  0.077220       NaN
                                     gsp                   3.972946       NaN   6.488500       NaN  0.091813       NaN
                                     historical_tod_mean   3.926451       NaN   6.707913       NaN  0.093280       NaN
                                     neighbor_average      6.903352       NaN  10.779343       NaN  0.183970       NaN
       best_random_by_validation     gls_map               3.213605       NaN   5.248293       NaN  0.072475       NaN
                                     gsp                   3.923261       NaN   6.309036       NaN  0.088024       NaN
                                     historical_tod_mean   3.815133       NaN   6.488712       NaN  0.089298       NaN
                                     neighbor_average      7.729272       NaN  11.635687       NaN  0.178159       NaN
       coverage                      gls_map               3.409776       NaN   5.648922       NaN  0.079031       NaN
                                     gsp                   4.003878       NaN   6.592647       NaN  0.092910       NaN
                                     historical_tod_mean   3.961888       NaN   6.797502       NaN  0.095445       NaN
                                     neighbor_average      7.018171       NaN  10.596203       NaN  0.181815       NaN
       degree                        gls_map               3.955541       NaN   6.627662       NaN  0.095449       NaN
                                     gsp                   4.149076       NaN   6.800985       NaN  0.099878       NaN
                                     historical_tod_mean   4.080157       NaN   6.943533       NaN  0.099686       NaN
                                     neighbor_average      7.748382       NaN  12.012552       NaN  0.206368       NaN
       graph_sampling_laplacian      gls_map               3.730968       NaN   6.058928       NaN  0.087805       NaN
                                     gsp                   3.806077       NaN   6.210965       NaN  0.088866       NaN
                                     historical_tod_mean   3.768481       NaN   6.375081       NaN  0.089471       NaN
                                     neighbor_average      7.616933       NaN  11.337685       NaN  0.191746       NaN
       greedy_a_trace                gls_map               3.211526       NaN   5.270375       NaN  0.077413       NaN
                                     gsp                   3.959625       NaN   6.544558       NaN  0.094295       NaN
                                     historical_tod_mean   3.955928       NaN   6.744064       NaN  0.096194       NaN
                                     neighbor_average      6.873888       NaN  10.785966       NaN  0.193458       NaN
       greedy_d_logdet               gls_map               3.944738       NaN   6.287328       NaN  0.104245       NaN
                                     gsp                   4.057829       NaN   6.724800       NaN  0.100406       NaN
                                     historical_tod_mean   4.032336       NaN   6.855006       NaN  0.099282       NaN
                                     neighbor_average      7.738699       NaN  12.552924       NaN  0.233787       NaN
       multistart_swap_by_validation gls_map               3.159688       NaN   5.108113       NaN  0.073858       NaN
                                     gsp                   3.942961       NaN   6.436327       NaN  0.091771       NaN
                                     historical_tod_mean   3.911002       NaN   6.665108       NaN  0.093672       NaN
                                     neighbor_average      6.764327       NaN  10.534855       NaN  0.183798       NaN
       observability_proxy           gls_map               3.754858       NaN   6.377632       NaN  0.090868       NaN
                                     gsp                   4.124544       NaN   6.843841       NaN  0.098851       NaN
                                     historical_tod_mean   4.095381       NaN   7.021087       NaN  0.100027       NaN
                                     neighbor_average      7.804220       NaN  11.957097       NaN  0.207050       NaN
       qr_pod_modes                  gls_map               3.506893       NaN   5.741598       NaN  0.087731       NaN
                                     gsp                   3.948891       NaN   6.530752       NaN  0.094177       NaN
                                     historical_tod_mean   3.944703       NaN   6.703136       NaN  0.095666       NaN
                                     neighbor_average      7.360989       NaN  11.617936       NaN  0.208535       NaN
       random                        gls_map               3.375438  0.088319   5.639978  0.174647  0.079205  0.002954
                                     gsp                   3.970797  0.064465   6.518722  0.095770  0.092659  0.002061
                                     historical_tod_mean   3.946525  0.056765   6.726998  0.087859  0.094188  0.001865
                                     neighbor_average      7.223584  0.216847  11.130585  0.309329  0.184122  0.006793
       rcss_selected                 gls_map               3.159688       NaN   5.108113       NaN  0.073858       NaN
                                     gsp                   3.942961       NaN   6.436327       NaN  0.091771       NaN
                                     historical_tod_mean   3.911002       NaN   6.665108       NaN  0.093672       NaN
                                     neighbor_average      6.764327       NaN  10.534855       NaN  0.183798       NaN
       robust_coverage_cvar          gls_map               3.292189       NaN   5.542970       NaN  0.078716       NaN
                                     gsp                   3.964034       NaN   6.541007       NaN  0.094486       NaN
                                     historical_tod_mean   3.932536       NaN   6.737541       NaN  0.094367       NaN
                                     neighbor_average      7.092238       NaN  10.913124       NaN  0.187951       NaN
       scenario_average_a_trace      gls_map               3.259428       NaN   5.416783       NaN  0.077492       NaN
                                     gsp                   3.957144       NaN   6.527067       NaN  0.093163       NaN
                                     historical_tod_mean   3.936004       NaN   6.704327       NaN  0.094171       NaN
                                     neighbor_average      7.124774       NaN  10.859704       NaN  0.185422       NaN
       scenario_cvar_a_trace         gls_map               3.213186       NaN   5.278575       NaN  0.076370       NaN
                                     gsp                   3.899477       NaN   6.405575       NaN  0.092005       NaN
                                     historical_tod_mean   3.851901       NaN   6.612211       NaN  0.092755       NaN
                                     neighbor_average      7.173021       NaN  10.866992       NaN  0.187464       NaN
       swap_from_best_random_trace   gls_map               3.171403       NaN   5.101261       NaN  0.074052       NaN
                                     gsp                   3.945327       NaN   6.454474       NaN  0.091950       NaN
                                     historical_tod_mean   3.901836       NaN   6.643351       NaN  0.093653       NaN
                                     neighbor_average      6.835312       NaN  10.587943       NaN  0.188011       NaN
       swap_from_greedy_a_trace      gls_map               3.232408       NaN   5.316846       NaN  0.079186       NaN
                                     gsp                   3.994516       NaN   6.586204       NaN  0.095824       NaN
                                     historical_tod_mean   3.994126       NaN   6.788887       NaN  0.097521       NaN
                                     neighbor_average      7.021344       NaN  11.043804       NaN  0.200489       NaN
       swap_from_scenario_average    gls_map               3.223010       NaN   5.263693       NaN  0.077336       NaN
                                     gsp                   3.986293       NaN   6.563214       NaN  0.094059       NaN
                                     historical_tod_mean   3.970305       NaN   6.737083       NaN  0.096171       NaN
                                     neighbor_average      6.950292       NaN  10.905921       NaN  0.195882       NaN
       swap_from_scenario_cvar       gls_map               3.273874       NaN   5.318252       NaN  0.077906       NaN
                                     gsp                   4.013816       NaN   6.581052       NaN  0.095559       NaN
                                     historical_tod_mean   3.985741       NaN   6.759502       NaN  0.096994       NaN
                                     neighbor_average      7.082201       NaN  11.060738       NaN  0.201745       NaN
       top_variance                  gls_map               3.234069       NaN   5.320767       NaN  0.071192       NaN
                                     gsp                   3.592740       NaN   5.824637       NaN  0.079383       NaN
                                     historical_tod_mean   3.518612       NaN   5.968278       NaN  0.079335       NaN
                                     neighbor_average      9.463374       NaN  14.810485       NaN  0.182154       NaN
       validation_swap_selected      gls_map               3.117630       NaN   5.052723       NaN  0.074068       NaN
                                     gsp                   3.859319       NaN   6.337882       NaN  0.092152       NaN
                                     historical_tod_mean   3.828536       NaN   6.571342       NaN  0.092195       NaN
                                     neighbor_average      6.933448       NaN  10.667117       NaN  0.183798       NaN
0.3    best_random_by_trace          gls_map               3.207844       NaN   5.382324       NaN  0.075033       NaN
                                     gsp                   4.053326       NaN   6.578920       NaN  0.096164       NaN
                                     historical_tod_mean   4.018823       NaN   6.803465       NaN  0.096499       NaN
                                     neighbor_average      6.751916       NaN  10.434345       NaN  0.171086       NaN
       best_random_by_validation     gls_map               3.038648       NaN   5.078135       NaN  0.071084       NaN
                                     gsp                   3.883547       NaN   6.389784       NaN  0.091020       NaN
                                     historical_tod_mean   3.879244       NaN   6.637608       NaN  0.092297       NaN
                                     neighbor_average      7.171027       NaN  10.839407       NaN  0.177492       NaN
       coverage                      gls_map               3.175856       NaN   5.349172       NaN  0.072553       NaN
                                     gsp                   4.030111       NaN   6.614779       NaN  0.092117       NaN
                                     historical_tod_mean   3.921234       NaN   6.778256       NaN  0.094238       NaN
                                     neighbor_average      6.898687       NaN  10.459013       NaN  0.175159       NaN
       degree                        gls_map               3.848043       NaN   6.463682       NaN  0.091615       NaN
                                     gsp                   4.127225       NaN   6.770536       NaN  0.097178       NaN
                                     historical_tod_mean   4.029023       NaN   6.908308       NaN  0.097576       NaN
                                     neighbor_average      8.391448       NaN  12.890442       NaN  0.221134       NaN
       graph_sampling_laplacian      gls_map               3.464487       NaN   5.629419       NaN  0.080197       NaN
                                     gsp                   3.821787       NaN   6.180670       NaN  0.089278       NaN
                                     historical_tod_mean   3.815028       NaN   6.403204       NaN  0.091108       NaN
                                     neighbor_average      7.145743       NaN  11.227948       NaN  0.186308       NaN
       greedy_a_trace                gls_map               3.104842       NaN   5.014211       NaN  0.074273       NaN
                                     gsp                   3.961278       NaN   6.547953       NaN  0.094298       NaN
                                     historical_tod_mean   3.933289       NaN   6.741738       NaN  0.095964       NaN
                                     neighbor_average      6.709608       NaN  10.421560       NaN  0.190695       NaN
       greedy_d_logdet               gls_map               3.656832       NaN   5.695454       NaN  0.090228       NaN
                                     gsp                   4.036142       NaN   6.636696       NaN  0.097077       NaN
                                     historical_tod_mean   3.982939       NaN   6.806609       NaN  0.097823       NaN
                                     neighbor_average      7.734319       NaN  12.329174       NaN  0.230423       NaN
       multistart_swap_by_validation gls_map               3.046236       NaN   4.988567       NaN  0.073424       NaN
                                     gsp                   4.042272       NaN   6.646044       NaN  0.095295       NaN
                                     historical_tod_mean   3.970060       NaN   6.829861       NaN  0.096909       NaN
                                     neighbor_average      6.895515       NaN  10.603110       NaN  0.189086       NaN
       observability_proxy           gls_map               3.698603       NaN   6.289426       NaN  0.088987       NaN
                                     gsp                   4.109880       NaN   6.795704       NaN  0.098031       NaN
                                     historical_tod_mean   4.066167       NaN   6.975035       NaN  0.098808       NaN
                                     neighbor_average      7.941886       NaN  11.830523       NaN  0.199667       NaN
       qr_pod_modes                  gls_map               3.237718       NaN   5.220280       NaN  0.079501       NaN
                                     gsp                   4.015525       NaN   6.605573       NaN  0.098143       NaN
                                     historical_tod_mean   3.981556       NaN   6.801706       NaN  0.097769       NaN
                                     neighbor_average      7.151565       NaN  11.046691       NaN  0.203545       NaN
       random                        gls_map               3.185018  0.088979   5.328505  0.188949  0.074584  0.002882
                                     gsp                   3.951605  0.069089   6.479156  0.115201  0.092544  0.002625
                                     historical_tod_mean   3.925832  0.063684   6.707631  0.109934  0.093934  0.002297
                                     neighbor_average      7.022426  0.179004  10.922373  0.325465  0.178265  0.007308
       rcss_selected                 gls_map               2.956068       NaN   4.923936       NaN  0.068221       NaN
                                     gsp                   3.799963       NaN   6.175816       NaN  0.086817       NaN
                                     historical_tod_mean   3.720149       NaN   6.404498       NaN  0.087774       NaN
                                     neighbor_average      7.020006       NaN  10.758323       NaN  0.163231       NaN
       robust_coverage_cvar          gls_map               2.955376       NaN   4.873557       NaN  0.069394       NaN
                                     gsp                   3.792001       NaN   6.251004       NaN  0.088638       NaN
                                     historical_tod_mean   3.786585       NaN   6.490079       NaN  0.089709       NaN
                                     neighbor_average      7.003630       NaN  10.788026       NaN  0.169425       NaN
       scenario_average_a_trace      gls_map               3.012463       NaN   5.006171       NaN  0.070256       NaN
                                     gsp                   3.936378       NaN   6.511588       NaN  0.090722       NaN
                                     historical_tod_mean   3.877339       NaN   6.681842       NaN  0.092517       NaN
                                     neighbor_average      6.946049       NaN  10.388884       NaN  0.176861       NaN
       scenario_cvar_a_trace         gls_map               2.913693       NaN   4.849462       NaN  0.067166       NaN
                                     gsp                   3.848773       NaN   6.317425       NaN  0.087975       NaN
                                     historical_tod_mean   3.775547       NaN   6.516641       NaN  0.089375       NaN
                                     neighbor_average      6.806600       NaN  10.258579       NaN  0.170471       NaN
       swap_from_best_random_trace   gls_map               3.096890       NaN   5.113292       NaN  0.074407       NaN
                                     gsp                   4.049829       NaN   6.631842       NaN  0.096845       NaN
                                     historical_tod_mean   4.029067       NaN   6.833826       NaN  0.098009       NaN
                                     neighbor_average      6.801057       NaN  10.462410       NaN  0.184008       NaN
       swap_from_greedy_a_trace      gls_map               3.185772       NaN   5.078301       NaN  0.076452       NaN
                                     gsp                   4.006005       NaN   6.553542       NaN  0.095289       NaN
                                     historical_tod_mean   3.958192       NaN   6.743578       NaN  0.096175       NaN
                                     neighbor_average      6.915766       NaN  10.727749       NaN  0.197121       NaN
       swap_from_scenario_average    gls_map               3.133249       NaN   5.114160       NaN  0.077182       NaN
                                     gsp                   4.038729       NaN   6.622892       NaN  0.096473       NaN
                                     historical_tod_mean   4.011584       NaN   6.818689       NaN  0.097992       NaN
                                     neighbor_average      6.892643       NaN  10.743855       NaN  0.195285       NaN
       swap_from_scenario_cvar       gls_map               3.067919       NaN   5.054564       NaN  0.074511       NaN
                                     gsp                   4.029064       NaN   6.596994       NaN  0.097069       NaN
                                     historical_tod_mean   3.990234       NaN   6.802570       NaN  0.098093       NaN
                                     neighbor_average      7.003339       NaN  10.942113       NaN  0.201132       NaN
       top_variance                  gls_map               3.041913       NaN   5.080790       NaN  0.066482       NaN
                                     gsp                   3.486651       NaN   5.684535       NaN  0.076446       NaN
                                     historical_tod_mean   3.424293       NaN   5.800459       NaN  0.076297       NaN
                                     neighbor_average      9.055374       NaN  13.928185       NaN  0.172756       NaN
       validation_swap_selected      gls_map               2.900052       NaN   4.789879       NaN  0.067228       NaN
                                     gsp                   3.710455       NaN   6.061232       NaN  0.085867       NaN
                                     historical_tod_mean   3.678324       NaN   6.312705       NaN  0.086972       NaN
                                     neighbor_average      7.014612       NaN  10.640396       NaN  0.164474       NaN
```

## Best method per budget-layout row

```
 budget                layout_type  method      mae     rmse
    0.1 swap_from_scenario_average gls_map 3.407556 5.633682
    0.2   validation_swap_selected gls_map 3.117630 5.052723
    0.3   validation_swap_selected gls_map 2.900052 4.789879
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.121003      0.123636 210
    gsp   condition_number     0.123481      0.155195 210
    gsp information_logdet    -0.156388     -0.140005 210
gls_map    posterior_trace     0.834510      0.837974 210
gls_map   condition_number     0.823303      0.868118 210
gls_map information_logdet    -0.746158     -0.800563 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv