---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-06-27, 2012-06-22
Test days: 2012-05-02, 2012-05-09
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.872029       NaN   6.492689       NaN  0.099340       NaN
                                     gsp                   4.418378       NaN   7.527603       NaN  0.117097       NaN
                                     historical_tod_mean   4.600335       NaN   7.856657       NaN  0.119401       NaN
                                     neighbor_average      7.580502       NaN  11.653377       NaN  0.202923       NaN
       best_random_by_validation     gls_map               3.872029       NaN   6.492689       NaN  0.099340       NaN
                                     gsp                   4.418378       NaN   7.527603       NaN  0.117097       NaN
                                     historical_tod_mean   4.600335       NaN   7.856657       NaN  0.119401       NaN
                                     neighbor_average      7.580502       NaN  11.653377       NaN  0.202923       NaN
       coverage                      gls_map               3.979615       NaN   6.706360       NaN  0.105182       NaN
                                     gsp                   4.426940       NaN   7.544034       NaN  0.117720       NaN
                                     historical_tod_mean   4.613215       NaN   7.839352       NaN  0.119727       NaN
                                     neighbor_average      7.503578       NaN  11.536393       NaN  0.202913       NaN
       degree                        gls_map               4.452375       NaN   7.426871       NaN  0.116876       NaN
                                     gsp                   4.426487       NaN   7.603335       NaN  0.116510       NaN
                                     historical_tod_mean   4.581948       NaN   7.806275       NaN  0.118974       NaN
                                     neighbor_average      8.960849       NaN  13.535008       NaN  0.226004       NaN
       graph_sampling_laplacian      gls_map               4.762678       NaN   7.777358       NaN  0.130442       NaN
                                     gsp                   4.584961       NaN   7.719918       NaN  0.123471       NaN
                                     historical_tod_mean   4.703625       NaN   7.952087       NaN  0.122489       NaN
                                     neighbor_average      8.330781       NaN  13.461833       NaN  0.258969       NaN
       greedy_a_trace                gls_map               3.772403       NaN   6.300136       NaN  0.097748       NaN
                                     gsp                   4.418889       NaN   7.492835       NaN  0.116753       NaN
                                     historical_tod_mean   4.604111       NaN   7.822897       NaN  0.119159       NaN
                                     neighbor_average      7.253001       NaN  11.383623       NaN  0.206196       NaN
       greedy_d_logdet               gls_map               4.464620       NaN   7.148359       NaN  0.109460       NaN
                                     gsp                   4.547043       NaN   7.574693       NaN  0.110254       NaN
                                     historical_tod_mean   4.539560       NaN   7.743096       NaN  0.112490       NaN
                                     neighbor_average      8.193036       NaN  12.467456       NaN  0.224946       NaN
       multistart_swap_by_validation gls_map               3.820891       NaN   6.385795       NaN  0.100290       NaN
                                     gsp                   4.452562       NaN   7.525078       NaN  0.117258       NaN
                                     historical_tod_mean   4.608978       NaN   7.848172       NaN  0.119325       NaN
                                     neighbor_average      7.305447       NaN  11.177039       NaN  0.200223       NaN
       observability_proxy           gls_map               4.384245       NaN   7.341598       NaN  0.115406       NaN
                                     gsp                   4.411550       NaN   7.587898       NaN  0.116406       NaN
                                     historical_tod_mean   4.586784       NaN   7.818393       NaN  0.119199       NaN
                                     neighbor_average     10.716237       NaN  16.041940       NaN  0.239247       NaN
       qr_pod_modes                  gls_map               4.097644       NaN   6.654337       NaN  0.103111       NaN
                                     gsp                   4.455855       NaN   7.545948       NaN  0.115509       NaN
                                     historical_tod_mean   4.579685       NaN   7.813883       NaN  0.118395       NaN
                                     neighbor_average      7.479918       NaN  11.717785       NaN  0.218515       NaN
       random                        gls_map               3.963559  0.047636   6.647118  0.093543  0.101585  0.002981
                                     gsp                   4.455914  0.030557   7.549880  0.035160  0.116197  0.002239
                                     historical_tod_mean   4.622675  0.021651   7.851427  0.033621  0.118950  0.001978
                                     neighbor_average      7.577542  0.149440  11.746800  0.208045  0.201028  0.004172
       rcss_selected                 gls_map               3.820891       NaN   6.385795       NaN  0.100290       NaN
                                     gsp                   4.452562       NaN   7.525078       NaN  0.117258       NaN
                                     historical_tod_mean   4.608978       NaN   7.848172       NaN  0.119325       NaN
                                     neighbor_average      7.305447       NaN  11.177039       NaN  0.200223       NaN
       robust_coverage_cvar          gls_map               3.956547       NaN   6.587178       NaN  0.100563       NaN
                                     gsp                   4.435199       NaN   7.527238       NaN  0.116014       NaN
                                     historical_tod_mean   4.599591       NaN   7.827320       NaN  0.118915       NaN
                                     neighbor_average      7.600480       NaN  11.663041       NaN  0.209124       NaN
       scenario_average_a_trace      gls_map               4.108742       NaN   6.791006       NaN  0.105247       NaN
                                     gsp                   4.508735       NaN   7.564894       NaN  0.116434       NaN
                                     historical_tod_mean   4.600665       NaN   7.812471       NaN  0.118803       NaN
                                     neighbor_average      7.613985       NaN  11.545157       NaN  0.212145       NaN
       scenario_cvar_a_trace         gls_map               3.994284       NaN   6.611167       NaN  0.101038       NaN
                                     gsp                   4.424680       NaN   7.502512       NaN  0.115533       NaN
                                     historical_tod_mean   4.570061       NaN   7.788432       NaN  0.118221       NaN
                                     neighbor_average      7.691496       NaN  11.675793       NaN  0.211344       NaN
       swap_from_best_random_trace   gls_map               3.777473       NaN   6.362122       NaN  0.097464       NaN
                                     gsp                   4.426528       NaN   7.529222       NaN  0.117219       NaN
                                     historical_tod_mean   4.597613       NaN   7.854485       NaN  0.119427       NaN
                                     neighbor_average      7.369125       NaN  11.571906       NaN  0.203683       NaN
       swap_from_greedy_a_trace      gls_map               3.738933       NaN   6.254096       NaN  0.096680       NaN
                                     gsp                   4.415358       NaN   7.482524       NaN  0.115572       NaN
                                     historical_tod_mean   4.586356       NaN   7.799816       NaN  0.118335       NaN
                                     neighbor_average      7.245939       NaN  11.379813       NaN  0.205785       NaN
       swap_from_scenario_average    gls_map               3.926374       NaN   6.545656       NaN  0.100301       NaN
                                     gsp                   4.492912       NaN   7.554970       NaN  0.115173       NaN
                                     historical_tod_mean   4.598092       NaN   7.818956       NaN  0.118053       NaN
                                     neighbor_average      7.502770       NaN  11.478497       NaN  0.208523       NaN
       swap_from_scenario_cvar       gls_map               3.864271       NaN   6.414632       NaN  0.098609       NaN
                                     gsp                   4.402066       NaN   7.474936       NaN  0.114564       NaN
                                     historical_tod_mean   4.551299       NaN   7.780481       NaN  0.117347       NaN
                                     neighbor_average      7.538760       NaN  11.469892       NaN  0.209091       NaN
       top_variance                  gls_map               4.002194       NaN   6.721980       NaN  0.096303       NaN
                                     gsp                   4.222459       NaN   7.184345       NaN  0.102447       NaN
                                     historical_tod_mean   4.378998       NaN   7.441364       NaN  0.105547       NaN
                                     neighbor_average     10.237627       NaN  15.888055       NaN  0.209067       NaN
       validation_swap_selected      gls_map               3.815041       NaN   6.326741       NaN  0.098856       NaN
                                     gsp                   4.436846       NaN   7.480582       NaN  0.115520       NaN
                                     historical_tod_mean   4.573042       NaN   7.793247       NaN  0.117893       NaN
                                     neighbor_average      7.489030       NaN  11.262513       NaN  0.200141       NaN
0.2    best_random_by_trace          gls_map               3.630355       NaN   6.055537       NaN  0.089120       NaN
                                     gsp                   4.435649       NaN   7.470693       NaN  0.112852       NaN
                                     historical_tod_mean   4.615945       NaN   7.815577       NaN  0.114801       NaN
                                     neighbor_average      7.375538       NaN  11.552047       NaN  0.196359       NaN
       best_random_by_validation     gls_map               3.602572       NaN   6.039904       NaN  0.086987       NaN
                                     gsp                   4.363479       NaN   7.423334       NaN  0.110444       NaN
                                     historical_tod_mean   4.569474       NaN   7.775270       NaN  0.113132       NaN
                                     neighbor_average      7.328453       NaN  11.459925       NaN  0.187136       NaN
       coverage                      gls_map               3.665604       NaN   6.151037       NaN  0.095706       NaN
                                     gsp                   4.437530       NaN   7.552179       NaN  0.118466       NaN
                                     historical_tod_mean   4.630134       NaN   7.891889       NaN  0.121704       NaN
                                     neighbor_average      7.230056       NaN  11.310453       NaN  0.195149       NaN
       degree                        gls_map               4.304258       NaN   7.201920       NaN  0.104614       NaN
                                     gsp                   4.355889       NaN   7.434991       NaN  0.107624       NaN
                                     historical_tod_mean   4.508976       NaN   7.679689       NaN  0.110838       NaN
                                     neighbor_average      8.989247       NaN  13.294042       NaN  0.207744       NaN
       graph_sampling_laplacian      gls_map               4.576458       NaN   7.589171       NaN  0.123109       NaN
                                     gsp                   4.683905       NaN   7.768185       NaN  0.124384       NaN
                                     historical_tod_mean   4.786284       NaN   8.052224       NaN  0.125633       NaN
                                     neighbor_average      8.985066       NaN  12.791075       NaN  0.236822       NaN
       greedy_a_trace                gls_map               3.385433       NaN   5.590564       NaN  0.080576       NaN
                                     gsp                   4.393743       NaN   7.374396       NaN  0.107394       NaN
                                     historical_tod_mean   4.519369       NaN   7.697653       NaN  0.110779       NaN
                                     neighbor_average      7.172965       NaN  11.045075       NaN  0.189765       NaN
       greedy_d_logdet               gls_map               3.857609       NaN   6.301924       NaN  0.094099       NaN
                                     gsp                   4.454003       NaN   7.468670       NaN  0.110496       NaN
                                     historical_tod_mean   4.539136       NaN   7.763226       NaN  0.113418       NaN
                                     neighbor_average      7.774301       NaN  12.167699       NaN  0.218651       NaN
       multistart_swap_by_validation gls_map               3.494740       NaN   5.849015       NaN  0.083849       NaN
                                     gsp                   4.377022       NaN   7.406922       NaN  0.110158       NaN
                                     historical_tod_mean   4.574032       NaN   7.766597       NaN  0.112939       NaN
                                     neighbor_average      7.093304       NaN  11.126744       NaN  0.184108       NaN
       observability_proxy           gls_map               4.326339       NaN   7.214913       NaN  0.105684       NaN
                                     gsp                   4.352520       NaN   7.437319       NaN  0.108010       NaN
                                     historical_tod_mean   4.505039       NaN   7.693637       NaN  0.111194       NaN
                                     neighbor_average     10.214637       NaN  14.516230       NaN  0.226349       NaN
       qr_pod_modes                  gls_map               3.534621       NaN   5.788089       NaN  0.084852       NaN
                                     gsp                   4.393323       NaN   7.413215       NaN  0.109057       NaN
                                     historical_tod_mean   4.512618       NaN   7.732509       NaN  0.112320       NaN
                                     neighbor_average      7.376289       NaN  11.358667       NaN  0.200062       NaN
       random                        gls_map               3.659537  0.045348   6.134437  0.086643  0.093052  0.002695
                                     gsp                   4.444168  0.035354   7.517154  0.051962  0.116525  0.002770
                                     historical_tod_mean   4.624234  0.033530   7.854772  0.050520  0.119263  0.002664
                                     neighbor_average      7.301343  0.113302  11.453061  0.177941  0.193724  0.004412
       rcss_selected                 gls_map               3.376837       NaN   5.576258       NaN  0.081039       NaN
                                     gsp                   4.375889       NaN   7.358662       NaN  0.107455       NaN
                                     historical_tod_mean   4.503074       NaN   7.689784       NaN  0.110653       NaN
                                     neighbor_average      7.158733       NaN  11.083871       NaN  0.192019       NaN
       robust_coverage_cvar          gls_map               3.646599       NaN   5.958720       NaN  0.086235       NaN
                                     gsp                   4.413034       NaN   7.417540       NaN  0.108775       NaN
                                     historical_tod_mean   4.522104       NaN   7.731548       NaN  0.111996       NaN
                                     neighbor_average      7.603090       NaN  11.514209       NaN  0.197888       NaN
       scenario_average_a_trace      gls_map               3.699662       NaN   6.108163       NaN  0.093199       NaN
                                     gsp                   4.471880       NaN   7.520622       NaN  0.115804       NaN
                                     historical_tod_mean   4.573718       NaN   7.815607       NaN  0.119338       NaN
                                     neighbor_average      7.322588       NaN  11.257504       NaN  0.203768       NaN
       scenario_cvar_a_trace         gls_map               3.657738       NaN   6.051079       NaN  0.092109       NaN
                                     gsp                   4.394530       NaN   7.462849       NaN  0.115954       NaN
                                     historical_tod_mean   4.540003       NaN   7.790611       NaN  0.118809       NaN
                                     neighbor_average      7.443394       NaN  11.517340       NaN  0.208297       NaN
       swap_from_best_random_trace   gls_map               3.530460       NaN   5.849873       NaN  0.085732       NaN
                                     gsp                   4.403551       NaN   7.424395       NaN  0.111372       NaN
                                     historical_tod_mean   4.586528       NaN   7.778879       NaN  0.113587       NaN
                                     neighbor_average      7.298934       NaN  11.314974       NaN  0.194110       NaN
       swap_from_greedy_a_trace      gls_map               3.376837       NaN   5.576258       NaN  0.081039       NaN
                                     gsp                   4.375889       NaN   7.358662       NaN  0.107455       NaN
                                     historical_tod_mean   4.503074       NaN   7.689784       NaN  0.110653       NaN
                                     neighbor_average      7.158733       NaN  11.083871       NaN  0.192019       NaN
       swap_from_scenario_average    gls_map               3.558459       NaN   5.896991       NaN  0.089400       NaN
                                     gsp                   4.420406       NaN   7.478905       NaN  0.114916       NaN
                                     historical_tod_mean   4.540565       NaN   7.785129       NaN  0.118395       NaN
                                     neighbor_average      7.222259       NaN  11.186319       NaN  0.204166       NaN
       swap_from_scenario_cvar       gls_map               3.541618       NaN   5.891488       NaN  0.090438       NaN
                                     gsp                   4.394566       NaN   7.445669       NaN  0.116037       NaN
                                     historical_tod_mean   4.532623       NaN   7.775890       NaN  0.118474       NaN
                                     neighbor_average      7.286755       NaN  11.320726       NaN  0.206298       NaN
       top_variance                  gls_map               3.681665       NaN   6.201399       NaN  0.087587       NaN
                                     gsp                   4.049622       NaN   6.894932       NaN  0.097650       NaN
                                     historical_tod_mean   4.193363       NaN   7.138137       NaN  0.100017       NaN
                                     neighbor_average      8.891096       NaN  14.047401       NaN  0.185567       NaN
       validation_swap_selected      gls_map               3.381139       NaN   5.585596       NaN  0.081211       NaN
                                     gsp                   4.371742       NaN   7.353874       NaN  0.107450       NaN
                                     historical_tod_mean   4.501680       NaN   7.686666       NaN  0.110627       NaN
                                     neighbor_average      7.191429       NaN  11.119649       NaN  0.192036       NaN
0.3    best_random_by_trace          gls_map               3.342565       NaN   5.575614       NaN  0.084361       NaN
                                     gsp                   4.437410       NaN   7.493894       NaN  0.118023       NaN
                                     historical_tod_mean   4.620271       NaN   7.850864       NaN  0.120955       NaN
                                     neighbor_average      6.994982       NaN  11.016305       NaN  0.187993       NaN
       best_random_by_validation     gls_map               3.345667       NaN   5.575283       NaN  0.080401       NaN
                                     gsp                   4.310988       NaN   7.315892       NaN  0.110611       NaN
                                     historical_tod_mean   4.504901       NaN   7.665192       NaN  0.113103       NaN
                                     neighbor_average      7.101864       NaN  11.065544       NaN  0.177129       NaN
       coverage                      gls_map               3.511310       NaN   5.911108       NaN  0.093089       NaN
                                     gsp                   4.492861       NaN   7.590948       NaN  0.121995       NaN
                                     historical_tod_mean   4.690493       NaN   7.949900       NaN  0.124612       NaN
                                     neighbor_average      7.080683       NaN  11.284987       NaN  0.197274       NaN
       degree                        gls_map               4.210556       NaN   7.053118       NaN  0.101427       NaN
                                     gsp                   4.263420       NaN   7.314391       NaN  0.104875       NaN
                                     historical_tod_mean   4.428157       NaN   7.594939       NaN  0.108336       NaN
                                     neighbor_average      8.062367       NaN  12.399264       NaN  0.196463       NaN
       graph_sampling_laplacian      gls_map               4.505887       NaN   7.493495       NaN  0.120286       NaN
                                     gsp                   4.669226       NaN   7.709095       NaN  0.122765       NaN
                                     historical_tod_mean   4.760617       NaN   8.004563       NaN  0.123898       NaN
                                     neighbor_average      8.570042       NaN  13.090536       NaN  0.244974       NaN
       greedy_a_trace                gls_map               3.131593       NaN   5.132191       NaN  0.075188       NaN
                                     gsp                   4.327037       NaN   7.299817       NaN  0.107933       NaN
                                     historical_tod_mean   4.490490       NaN   7.674283       NaN  0.111041       NaN
                                     neighbor_average      6.993404       NaN  10.831485       NaN  0.189258       NaN
       greedy_d_logdet               gls_map               3.461667       NaN   5.732807       NaN  0.086044       NaN
                                     gsp                   4.371404       NaN   7.419422       NaN  0.110982       NaN
                                     historical_tod_mean   4.513023       NaN   7.785300       NaN  0.114029       NaN
                                     neighbor_average      7.476095       NaN  11.805986       NaN  0.213174       NaN
       multistart_swap_by_validation gls_map               3.254853       NaN   5.452384       NaN  0.083211       NaN
                                     gsp                   4.352683       NaN   7.409902       NaN  0.116376       NaN
                                     historical_tod_mean   4.529405       NaN   7.772839       NaN  0.118888       NaN
                                     neighbor_average      6.972552       NaN  10.859546       NaN  0.189411       NaN
       observability_proxy           gls_map               4.168584       NaN   7.001162       NaN  0.100633       NaN
                                     gsp                   4.253991       NaN   7.295962       NaN  0.104911       NaN
                                     historical_tod_mean   4.422213       NaN   7.578756       NaN  0.108331       NaN
                                     neighbor_average      8.089458       NaN  12.472220       NaN  0.197271       NaN
       qr_pod_modes                  gls_map               3.210255       NaN   5.259760       NaN  0.077930       NaN
                                     gsp                   4.320203       NaN   7.321612       NaN  0.109100       NaN
                                     historical_tod_mean   4.468921       NaN   7.686952       NaN  0.112345       NaN
                                     neighbor_average      7.052309       NaN  10.905872       NaN  0.192158       NaN
       random                        gls_map               3.444274  0.052654   5.754917  0.096873  0.086030  0.003284
                                     gsp                   4.438625  0.045276   7.487794  0.066274  0.115767  0.003599
                                     historical_tod_mean   4.616144  0.043555   7.838516  0.066792  0.118389  0.003469
                                     neighbor_average      7.156506  0.094209  11.297421  0.178960  0.189061  0.006305
       rcss_selected                 gls_map               3.128678       NaN   5.146332       NaN  0.075542       NaN
                                     gsp                   4.317563       NaN   7.294849       NaN  0.108005       NaN
                                     historical_tod_mean   4.472904       NaN   7.671478       NaN  0.110883       NaN
                                     neighbor_average      7.004472       NaN  10.839387       NaN  0.190101       NaN
       robust_coverage_cvar          gls_map               3.417965       NaN   5.582345       NaN  0.080429       NaN
                                     gsp                   4.339626       NaN   7.316223       NaN  0.107218       NaN
                                     historical_tod_mean   4.466651       NaN   7.656540       NaN  0.110927       NaN
                                     neighbor_average      7.476187       NaN  11.709649       NaN  0.199001       NaN
       scenario_average_a_trace      gls_map               3.504607       NaN   5.752851       NaN  0.084189       NaN
                                     gsp                   4.385475       NaN   7.419554       NaN  0.111192       NaN
                                     historical_tod_mean   4.533559       NaN   7.777699       NaN  0.114223       NaN
                                     neighbor_average      7.433726       NaN  11.529356       NaN  0.203716       NaN
       scenario_cvar_a_trace         gls_map               3.468544       NaN   5.683959       NaN  0.082635       NaN
                                     gsp                   4.334495       NaN   7.314722       NaN  0.107452       NaN
                                     historical_tod_mean   4.456746       NaN   7.649869       NaN  0.110766       NaN
                                     neighbor_average      7.585526       NaN  11.871553       NaN  0.204400       NaN
       swap_from_best_random_trace   gls_map               3.248939       NaN   5.393429       NaN  0.082032       NaN
                                     gsp                   4.392103       NaN   7.414455       NaN  0.116260       NaN
                                     historical_tod_mean   4.558854       NaN   7.777982       NaN  0.119319       NaN
                                     neighbor_average      6.911158       NaN  10.854786       NaN  0.188801       NaN
       swap_from_greedy_a_trace      gls_map               3.128678       NaN   5.146332       NaN  0.075542       NaN
                                     gsp                   4.317563       NaN   7.294849       NaN  0.108005       NaN
                                     historical_tod_mean   4.472904       NaN   7.671478       NaN  0.110883       NaN
                                     neighbor_average      7.004472       NaN  10.839387       NaN  0.190101       NaN
       swap_from_scenario_average    gls_map               3.340247       NaN   5.484223       NaN  0.080013       NaN
                                     gsp                   4.366059       NaN   7.390076       NaN  0.110232       NaN
                                     historical_tod_mean   4.516218       NaN   7.752548       NaN  0.113449       NaN
                                     neighbor_average      7.216358       NaN  11.277637       NaN  0.199198       NaN
       swap_from_scenario_cvar       gls_map               3.316543       NaN   5.457330       NaN  0.079535       NaN
                                     gsp                   4.339436       NaN   7.312400       NaN  0.107693       NaN
                                     historical_tod_mean   4.464634       NaN   7.652523       NaN  0.110911       NaN
                                     neighbor_average      7.349990       NaN  11.509799       NaN  0.199072       NaN
       top_variance                  gls_map               3.419902       NaN   5.730997       NaN  0.078031       NaN
                                     gsp                   3.876286       NaN   6.654204       NaN  0.091990       NaN
                                     historical_tod_mean   4.009053       NaN   6.875243       NaN  0.094131       NaN
                                     neighbor_average      8.625286       NaN  13.476221       NaN  0.174141       NaN
       validation_swap_selected      gls_map               3.123523       NaN   5.135572       NaN  0.075421       NaN
                                     gsp                   4.307445       NaN   7.281270       NaN  0.107787       NaN
                                     historical_tod_mean   4.460924       NaN   7.658186       NaN  0.110580       NaN
                                     neighbor_average      7.002871       NaN  10.839240       NaN  0.189753       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 3.738933 6.254096
    0.2 swap_from_greedy_a_trace gls_map 3.376837 5.576258
    0.3 validation_swap_selected gls_map 3.123523 5.135572
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.201080      0.201398 360
    gsp   condition_number     0.201989      0.206936 360
    gsp information_logdet    -0.154771     -0.186746 360
gls_map    posterior_trace     0.924015      0.921694 360
gls_map   condition_number     0.791097      0.893611 360
gls_map information_logdet    -0.861332     -0.876578 360
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv