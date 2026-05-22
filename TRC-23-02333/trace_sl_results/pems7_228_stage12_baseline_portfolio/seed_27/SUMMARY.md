---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-13, 2012-06-04
Test days: 2012-05-22, 2012-06-21
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.626481       NaN   6.141267       NaN  0.092666       NaN
                                     gsp                   3.848279       NaN   6.528267       NaN  0.101993       NaN
                                     historical_tod_mean   3.747767       NaN   6.591458       NaN  0.103411       NaN
                                     neighbor_average      8.212733       NaN  12.593139       NaN  0.232709       NaN
       best_random_by_validation     gls_map               3.486229       NaN   5.869603       NaN  0.088743       NaN
                                     gsp                   3.707631       NaN   6.384178       NaN  0.100492       NaN
                                     historical_tod_mean   3.657054       NaN   6.495405       NaN  0.101392       NaN
                                     neighbor_average      8.361963       NaN  12.642944       NaN  0.226639       NaN
       coverage                      gls_map               3.591871       NaN   6.247931       NaN  0.096702       NaN
                                     gsp                   3.709346       NaN   6.543637       NaN  0.102608       NaN
                                     historical_tod_mean   3.730957       NaN   6.648445       NaN  0.105073       NaN
                                     neighbor_average      8.316941       NaN  12.759592       NaN  0.238144       NaN
       degree                        gls_map               3.837879       NaN   6.578034       NaN  0.103180       NaN
                                     gsp                   3.876998       NaN   6.655362       NaN  0.107062       NaN
                                     historical_tod_mean   3.747767       NaN   6.668615       NaN  0.105772       NaN
                                     neighbor_average      9.046440       NaN  13.827927       NaN  0.258995       NaN
       graph_sampling_laplacian      gls_map               3.678344       NaN   6.363560       NaN  0.098584       NaN
                                     gsp                   3.666707       NaN   6.399376       NaN  0.098492       NaN
                                     historical_tod_mean   3.658716       NaN   6.456977       NaN  0.100924       NaN
                                     neighbor_average      9.084355       NaN  14.349934       NaN  0.235356       NaN
       greedy_a_trace                gls_map               3.372048       NaN   5.715903       NaN  0.085057       NaN
                                     gsp                   3.737611       NaN   6.417645       NaN  0.100689       NaN
                                     historical_tod_mean   3.703912       NaN   6.537871       NaN  0.102540       NaN
                                     neighbor_average      8.018880       NaN  12.052376       NaN  0.230723       NaN
       greedy_d_logdet               gls_map               4.039826       NaN   6.634955       NaN  0.105050       NaN
                                     gsp                   3.893550       NaN   6.660342       NaN  0.107347       NaN
                                     historical_tod_mean   3.732749       NaN   6.590158       NaN  0.104343       NaN
                                     neighbor_average      8.570097       NaN  13.727796       NaN  0.273474       NaN
       multistart_swap_by_validation gls_map               3.313733       NaN   5.640757       NaN  0.084896       NaN
                                     gsp                   3.665914       NaN   6.358102       NaN  0.099402       NaN
                                     historical_tod_mean   3.679080       NaN   6.494337       NaN  0.101908       NaN
                                     neighbor_average      7.901051       NaN  12.028318       NaN  0.225064       NaN
       observability_proxy           gls_map               3.687872       NaN   6.315517       NaN  0.096141       NaN
                                     gsp                   3.803690       NaN   6.555681       NaN  0.103156       NaN
                                     historical_tod_mean   3.712278       NaN   6.596278       NaN  0.103984       NaN
                                     neighbor_average      8.622824       NaN  13.291562       NaN  0.243409       NaN
       qr_pod_modes                  gls_map               3.810697       NaN   6.264652       NaN  0.098918       NaN
                                     gsp                   3.790788       NaN   6.517637       NaN  0.103802       NaN
                                     historical_tod_mean   3.740272       NaN   6.568812       NaN  0.104349       NaN
                                     neighbor_average      8.007645       NaN  12.898463       NaN  0.260556       NaN
       random                        gls_map               3.583503  0.079001   6.145545  0.112970  0.092869  0.002729
                                     gsp                   3.732348  0.046038   6.448004  0.052553  0.100306  0.001614
                                     historical_tod_mean   3.694828  0.028932   6.556055  0.045165  0.102466  0.001196
                                     neighbor_average      8.132260  0.220832  12.345079  0.336559  0.221224  0.010734
       rcss_selected                 gls_map               3.372048       NaN   5.715903       NaN  0.085057       NaN
                                     gsp                   3.737611       NaN   6.417645       NaN  0.100689       NaN
                                     historical_tod_mean   3.703912       NaN   6.537871       NaN  0.102540       NaN
                                     neighbor_average      8.018880       NaN  12.052376       NaN  0.230723       NaN
       robust_coverage_cvar          gls_map               3.537060       NaN   5.974156       NaN  0.092391       NaN
                                     gsp                   3.706047       NaN   6.338296       NaN  0.099913       NaN
                                     historical_tod_mean   3.662166       NaN   6.478952       NaN  0.101667       NaN
                                     neighbor_average      8.489890       NaN  13.095892       NaN  0.237417       NaN
       scenario_average_a_trace      gls_map               3.498682       NaN   5.963420       NaN  0.087431       NaN
                                     gsp                   3.761569       NaN   6.437546       NaN  0.099598       NaN
                                     historical_tod_mean   3.715883       NaN   6.547739       NaN  0.102096       NaN
                                     neighbor_average      8.314303       NaN  12.435242       NaN  0.225365       NaN
       scenario_cvar_a_trace         gls_map               3.552106       NaN   6.198320       NaN  0.095044       NaN
                                     gsp                   3.746086       NaN   6.492446       NaN  0.102352       NaN
                                     historical_tod_mean   3.732490       NaN   6.623155       NaN  0.104189       NaN
                                     neighbor_average      8.899234       NaN  13.514828       NaN  0.250343       NaN
       swap_from_best_random_trace   gls_map               3.332126       NaN   5.673932       NaN  0.085090       NaN
                                     gsp                   3.689327       NaN   6.384230       NaN  0.100189       NaN
                                     historical_tod_mean   3.702547       NaN   6.522643       NaN  0.102684       NaN
                                     neighbor_average      7.915431       NaN  12.161522       NaN  0.231269       NaN
       swap_from_greedy_a_trace      gls_map               3.313482       NaN   5.628704       NaN  0.083703       NaN
                                     gsp                   3.690614       NaN   6.386352       NaN  0.100367       NaN
                                     historical_tod_mean   3.706393       NaN   6.530112       NaN  0.102714       NaN
                                     neighbor_average      7.889146       NaN  12.142231       NaN  0.231436       NaN
       swap_from_scenario_average    gls_map               3.330953       NaN   5.665619       NaN  0.084597       NaN
                                     gsp                   3.696135       NaN   6.384467       NaN  0.099816       NaN
                                     historical_tod_mean   3.698265       NaN   6.519193       NaN  0.102555       NaN
                                     neighbor_average      7.948482       NaN  12.161249       NaN  0.231354       NaN
       swap_from_scenario_cvar       gls_map               3.363190       NaN   5.705409       NaN  0.085550       NaN
                                     gsp                   3.729424       NaN   6.407676       NaN  0.100995       NaN
                                     historical_tod_mean   3.714229       NaN   6.538079       NaN  0.102867       NaN
                                     neighbor_average      7.893399       NaN  12.063152       NaN  0.235776       NaN
       top_variance                  gls_map               3.470139       NaN   6.030046       NaN  0.088578       NaN
                                     gsp                   3.487188       NaN   6.163814       NaN  0.091530       NaN
                                     historical_tod_mean   3.513384       NaN   6.276406       NaN  0.093965       NaN
                                     neighbor_average     11.606882       NaN  17.824036       NaN  0.227971       NaN
       validation_swap_selected      gls_map               3.362339       NaN   5.834383       NaN  0.087448       NaN
                                     gsp                   3.646342       NaN   6.367137       NaN  0.099131       NaN
                                     historical_tod_mean   3.631499       NaN   6.491417       NaN  0.101139       NaN
                                     neighbor_average      8.080261       NaN  12.140370       NaN  0.207166       NaN
0.2    best_random_by_trace          gls_map               3.304902       NaN   5.585309       NaN  0.082932       NaN
                                     gsp                   3.726062       NaN   6.366258       NaN  0.098533       NaN
                                     historical_tod_mean   3.674539       NaN   6.480200       NaN  0.099641       NaN
                                     neighbor_average      7.864816       NaN  12.293252       NaN  0.204047       NaN
       best_random_by_validation     gls_map               3.276127       NaN   5.647785       NaN  0.079060       NaN
                                     gsp                   3.625223       NaN   6.267673       NaN  0.092742       NaN
                                     historical_tod_mean   3.593108       NaN   6.420935       NaN  0.095832       NaN
                                     neighbor_average      7.887200       NaN  12.037055       NaN  0.184173       NaN
       coverage                      gls_map               3.438834       NaN   6.047056       NaN  0.091886       NaN
                                     gsp                   3.748169       NaN   6.602642       NaN  0.104414       NaN
                                     historical_tod_mean   3.774634       NaN   6.767031       NaN  0.108279       NaN
                                     neighbor_average      7.766037       NaN  11.891089       NaN  0.221236       NaN
       degree                        gls_map               3.886744       NaN   6.499446       NaN  0.095955       NaN
                                     gsp                   4.046459       NaN   6.725089       NaN  0.101868       NaN
                                     historical_tod_mean   3.783454       NaN   6.581944       NaN  0.100365       NaN
                                     neighbor_average      8.617375       NaN  12.935042       NaN  0.222040       NaN
       graph_sampling_laplacian      gls_map               3.612631       NaN   6.100974       NaN  0.094173       NaN
                                     gsp                   3.606816       NaN   6.251552       NaN  0.098040       NaN
                                     historical_tod_mean   3.562251       NaN   6.321580       NaN  0.098676       NaN
                                     neighbor_average      8.349700       NaN  12.407417       NaN  0.231654       NaN
       greedy_a_trace                gls_map               3.231206       NaN   5.500374       NaN  0.081682       NaN
                                     gsp                   3.803536       NaN   6.501572       NaN  0.103219       NaN
                                     historical_tod_mean   3.764963       NaN   6.621874       NaN  0.105286       NaN
                                     neighbor_average      7.598942       NaN  11.785714       NaN  0.232256       NaN
       greedy_d_logdet               gls_map               3.894728       NaN   6.262705       NaN  0.100735       NaN
                                     gsp                   3.856600       NaN   6.547795       NaN  0.105051       NaN
                                     historical_tod_mean   3.757955       NaN   6.590120       NaN  0.105810       NaN
                                     neighbor_average      8.545895       NaN  13.447130       NaN  0.272383       NaN
       multistart_swap_by_validation gls_map               3.142043       NaN   5.325259       NaN  0.080177       NaN
                                     gsp                   3.650895       NaN   6.380685       NaN  0.100331       NaN
                                     historical_tod_mean   3.681448       NaN   6.531194       NaN  0.103103       NaN
                                     neighbor_average      7.554296       NaN  11.473131       NaN  0.218111       NaN
       observability_proxy           gls_map               3.692426       NaN   6.275674       NaN  0.093104       NaN
                                     gsp                   3.950441       NaN   6.674286       NaN  0.103553       NaN
                                     historical_tod_mean   3.782961       NaN   6.644504       NaN  0.103487       NaN
                                     neighbor_average      8.816107       NaN  13.223229       NaN  0.241324       NaN
       qr_pod_modes                  gls_map               3.482276       NaN   5.741579       NaN  0.089275       NaN
                                     gsp                   3.797483       NaN   6.462688       NaN  0.103087       NaN
                                     historical_tod_mean   3.727727       NaN   6.561340       NaN  0.104379       NaN
                                     neighbor_average      8.069820       NaN  12.625846       NaN  0.250484       NaN
       random                        gls_map               3.369436  0.077112   5.799285  0.141300  0.086535  0.002815
                                     gsp                   3.732311  0.060217   6.431402  0.081937  0.100137  0.002233
                                     historical_tod_mean   3.704825  0.045923   6.576151  0.077592  0.102943  0.002070
                                     neighbor_average      7.922731  0.195698  12.094656  0.311088  0.214151  0.010298
       rcss_selected                 gls_map               3.157184       NaN   5.416909       NaN  0.079287       NaN
                                     gsp                   3.574889       NaN   6.207824       NaN  0.095806       NaN
                                     historical_tod_mean   3.604703       NaN   6.379158       NaN  0.098985       NaN
                                     neighbor_average      7.768002       NaN  11.982304       NaN  0.201198       NaN
       robust_coverage_cvar          gls_map               3.319959       NaN   5.719879       NaN  0.085178       NaN
                                     gsp                   3.673576       NaN   6.330884       NaN  0.098383       NaN
                                     historical_tod_mean   3.632251       NaN   6.467750       NaN  0.100288       NaN
                                     neighbor_average      8.270122       NaN  12.533423       NaN  0.215267       NaN
       scenario_average_a_trace      gls_map               3.429162       NaN   5.858956       NaN  0.088325       NaN
                                     gsp                   3.829227       NaN   6.554653       NaN  0.105057       NaN
                                     historical_tod_mean   3.739674       NaN   6.625218       NaN  0.104960       NaN
                                     neighbor_average      8.115105       NaN  12.391822       NaN  0.235260       NaN
       scenario_cvar_a_trace         gls_map               3.506495       NaN   6.072744       NaN  0.091240       NaN
                                     gsp                   3.814361       NaN   6.556773       NaN  0.102627       NaN
                                     historical_tod_mean   3.734338       NaN   6.647375       NaN  0.103487       NaN
                                     neighbor_average      8.448874       NaN  12.910270       NaN  0.236076       NaN
       swap_from_best_random_trace   gls_map               3.225554       NaN   5.456990       NaN  0.082493       NaN
                                     gsp                   3.776290       NaN   6.488641       NaN  0.103624       NaN
                                     historical_tod_mean   3.744515       NaN   6.598120       NaN  0.104893       NaN
                                     neighbor_average      7.745211       NaN  12.101256       NaN  0.232420       NaN
       swap_from_greedy_a_trace      gls_map               3.205859       NaN   5.431192       NaN  0.081745       NaN
                                     gsp                   3.799127       NaN   6.486156       NaN  0.103298       NaN
                                     historical_tod_mean   3.739321       NaN   6.567778       NaN  0.104300       NaN
                                     neighbor_average      7.709894       NaN  12.139728       NaN  0.237451       NaN
       swap_from_scenario_average    gls_map               3.226555       NaN   5.469671       NaN  0.081150       NaN
                                     gsp                   3.777909       NaN   6.464104       NaN  0.101678       NaN
                                     historical_tod_mean   3.740913       NaN   6.571723       NaN  0.104020       NaN
                                     neighbor_average      7.682145       NaN  11.853620       NaN  0.229973       NaN
       swap_from_scenario_cvar       gls_map               3.222068       NaN   5.491854       NaN  0.082539       NaN
                                     gsp                   3.731360       NaN   6.418032       NaN  0.100854       NaN
                                     historical_tod_mean   3.701482       NaN   6.524469       NaN  0.102748       NaN
                                     neighbor_average      7.735896       NaN  12.087609       NaN  0.233447       NaN
       top_variance                  gls_map               3.236412       NaN   5.678647       NaN  0.082405       NaN
                                     gsp                   3.359640       NaN   5.937570       NaN  0.087475       NaN
                                     historical_tod_mean   3.353395       NaN   6.065400       NaN  0.088990       NaN
                                     neighbor_average     10.367169       NaN  15.969309       NaN  0.200571       NaN
       validation_swap_selected      gls_map               3.203058       NaN   5.512470       NaN  0.080271       NaN
                                     gsp                   3.593711       NaN   6.203818       NaN  0.093269       NaN
                                     historical_tod_mean   3.546137       NaN   6.346495       NaN  0.097889       NaN
                                     neighbor_average      7.902029       NaN  11.926706       NaN  0.201571       NaN
0.3    best_random_by_trace          gls_map               3.201122       NaN   5.433155       NaN  0.079431       NaN
                                     gsp                   3.676452       NaN   6.238913       NaN  0.095727       NaN
                                     historical_tod_mean   3.611941       NaN   6.394715       NaN  0.099475       NaN
                                     neighbor_average      7.896615       NaN  12.110923       NaN  0.221764       NaN
       best_random_by_validation     gls_map               3.168063       NaN   5.559993       NaN  0.081540       NaN
                                     gsp                   3.664378       NaN   6.333898       NaN  0.096886       NaN
                                     historical_tod_mean   3.628489       NaN   6.486146       NaN  0.101316       NaN
                                     neighbor_average      7.551467       NaN  11.539036       NaN  0.196106       NaN
       coverage                      gls_map               3.231435       NaN   5.698507       NaN  0.085455       NaN
                                     gsp                   3.711922       NaN   6.541097       NaN  0.103730       NaN
                                     historical_tod_mean   3.721946       NaN   6.730619       NaN  0.107397       NaN
                                     neighbor_average      7.588183       NaN  11.332182       NaN  0.211598       NaN
       degree                        gls_map               3.687048       NaN   6.232270       NaN  0.090785       NaN
                                     gsp                   3.843047       NaN   6.484987       NaN  0.098026       NaN
                                     historical_tod_mean   3.708546       NaN   6.505850       NaN  0.098455       NaN
                                     neighbor_average      8.912137       NaN  13.698442       NaN  0.247297       NaN
       graph_sampling_laplacian      gls_map               3.527445       NaN   5.981192       NaN  0.091175       NaN
                                     gsp                   3.636238       NaN   6.215013       NaN  0.097134       NaN
                                     historical_tod_mean   3.605653       NaN   6.341524       NaN  0.099388       NaN
                                     neighbor_average      7.927479       NaN  12.433957       NaN  0.213703       NaN
       greedy_a_trace                gls_map               3.168768       NaN   5.406226       NaN  0.082812       NaN
                                     gsp                   3.861041       NaN   6.579193       NaN  0.106326       NaN
                                     historical_tod_mean   3.813855       NaN   6.715071       NaN  0.109035       NaN
                                     neighbor_average      7.558576       NaN  11.837308       NaN  0.238225       NaN
       greedy_d_logdet               gls_map               3.655170       NaN   5.944931       NaN  0.094609       NaN
                                     gsp                   3.762463       NaN   6.421246       NaN  0.102813       NaN
                                     historical_tod_mean   3.646992       NaN   6.488548       NaN  0.103966       NaN
                                     neighbor_average      8.566943       NaN  13.272104       NaN  0.269741       NaN
       multistart_swap_by_validation gls_map               3.047304       NaN   5.178473       NaN  0.076144       NaN
                                     gsp                   3.673272       NaN   6.338739       NaN  0.098076       NaN
                                     historical_tod_mean   3.659256       NaN   6.485540       NaN  0.100830       NaN
                                     neighbor_average      7.371962       NaN  11.286302       NaN  0.202419       NaN
       observability_proxy           gls_map               3.626722       NaN   6.186978       NaN  0.089185       NaN
                                     gsp                   3.871767       NaN   6.519901       NaN  0.097937       NaN
                                     historical_tod_mean   3.736224       NaN   6.537501       NaN  0.098697       NaN
                                     neighbor_average      8.776333       NaN  12.894821       NaN  0.226357       NaN
       qr_pod_modes                  gls_map               3.233260       NaN   5.348217       NaN  0.082517       NaN
                                     gsp                   3.722856       NaN   6.363970       NaN  0.101762       NaN
                                     historical_tod_mean   3.667950       NaN   6.500225       NaN  0.104328       NaN
                                     neighbor_average      7.791830       NaN  11.975484       NaN  0.238359       NaN
       random                        gls_map               3.259470  0.079560   5.613969  0.143395  0.082293  0.002874
                                     gsp                   3.738795  0.065487   6.418631  0.094225  0.099187  0.002636
                                     historical_tod_mean   3.706649  0.061715   6.569614  0.095477  0.102500  0.002668
                                     neighbor_average      7.773498  0.205618  11.982304  0.361350  0.207093  0.010187
       rcss_selected                 gls_map               3.052299       NaN   5.213106       NaN  0.076249       NaN
                                     gsp                   3.572955       NaN   6.198906       NaN  0.094607       NaN
                                     historical_tod_mean   3.580065       NaN   6.374620       NaN  0.098644       NaN
                                     neighbor_average      7.614381       NaN  11.491025       NaN  0.187041       NaN
       robust_coverage_cvar          gls_map               3.163057       NaN   5.425888       NaN  0.079787       NaN
                                     gsp                   3.678278       NaN   6.348950       NaN  0.099831       NaN
                                     historical_tod_mean   3.615825       NaN   6.480393       NaN  0.101032       NaN
                                     neighbor_average      7.815264       NaN  11.923399       NaN  0.209080       NaN
       scenario_average_a_trace      gls_map               3.246176       NaN   5.534731       NaN  0.082595       NaN
                                     gsp                   3.790055       NaN   6.461852       NaN  0.103460       NaN
                                     historical_tod_mean   3.730981       NaN   6.574984       NaN  0.104853       NaN
                                     neighbor_average      7.728830       NaN  11.953092       NaN  0.225023       NaN
       scenario_cvar_a_trace         gls_map               3.368436       NaN   5.918448       NaN  0.088255       NaN
                                     gsp                   3.775364       NaN   6.546059       NaN  0.103024       NaN
                                     historical_tod_mean   3.697958       NaN   6.648646       NaN  0.104040       NaN
                                     neighbor_average      8.259246       NaN  12.561004       NaN  0.227034       NaN
       swap_from_best_random_trace   gls_map               3.139758       NaN   5.237392       NaN  0.079654       NaN
                                     gsp                   3.735202       NaN   6.327654       NaN  0.100377       NaN
                                     historical_tod_mean   3.694837       NaN   6.501141       NaN  0.103829       NaN
                                     neighbor_average      7.527963       NaN  11.555976       NaN  0.229734       NaN
       swap_from_greedy_a_trace      gls_map               3.153386       NaN   5.323971       NaN  0.081762       NaN
                                     gsp                   3.774376       NaN   6.452460       NaN  0.103768       NaN
                                     historical_tod_mean   3.745379       NaN   6.590923       NaN  0.106330       NaN
                                     neighbor_average      7.590945       NaN  11.904518       NaN  0.236849       NaN
       swap_from_scenario_average    gls_map               3.148123       NaN   5.330423       NaN  0.081444       NaN
                                     gsp                   3.748657       NaN   6.438051       NaN  0.102410       NaN
                                     historical_tod_mean   3.726746       NaN   6.568753       NaN  0.104994       NaN
                                     neighbor_average      7.560482       NaN  11.680868       NaN  0.224004       NaN
       swap_from_scenario_cvar       gls_map               3.088808       NaN   5.304480       NaN  0.078100       NaN
                                     gsp                   3.709524       NaN   6.411265       NaN  0.099734       NaN
                                     historical_tod_mean   3.664259       NaN   6.534085       NaN  0.101980       NaN
                                     neighbor_average      7.652445       NaN  11.804081       NaN  0.214620       NaN
       top_variance                  gls_map               3.089943       NaN   5.441067       NaN  0.076291       NaN
                                     gsp                   3.250183       NaN   5.753743       NaN  0.081934       NaN
                                     historical_tod_mean   3.233050       NaN   5.890857       NaN  0.083539       NaN
                                     neighbor_average      9.893732       NaN  15.233306       NaN  0.190282       NaN
       validation_swap_selected      gls_map               3.004867       NaN   5.173522       NaN  0.076962       NaN
                                     gsp                   3.517217       NaN   6.131350       NaN  0.093759       NaN
                                     historical_tod_mean   3.504400       NaN   6.320733       NaN  0.097045       NaN
                                     neighbor_average      7.708261       NaN  11.542530       NaN  0.185319       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1      swap_from_greedy_a_trace gls_map 3.313482 5.628704
    0.2 multistart_swap_by_validation gls_map 3.142043 5.325259
    0.3      validation_swap_selected gls_map 3.004867 5.173522
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.016227      0.033067 210
    gsp   condition_number     0.020647      0.051841 210
    gsp information_logdet    -0.054477     -0.116843 210
gls_map    posterior_trace     0.769890      0.772722 210
gls_map   condition_number     0.787863      0.811085 210
gls_map information_logdet    -0.672866     -0.709932 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv