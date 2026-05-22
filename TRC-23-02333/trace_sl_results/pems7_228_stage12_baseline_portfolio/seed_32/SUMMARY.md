---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-18, 2012-06-27
Test days: 2012-05-17, 2012-05-21
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.415767       NaN   5.911728       NaN  0.085280       NaN
                                     gsp                   3.602768       NaN   6.246496       NaN  0.088136       NaN
                                     historical_tod_mean   3.640619       NaN   6.474388       NaN  0.088083       NaN
                                     neighbor_average      7.495882       NaN  12.065753       NaN  0.209217       NaN
       best_random_by_validation     gls_map               3.313232       NaN   5.739046       NaN  0.079736       NaN
                                     gsp                   3.520810       NaN   6.106123       NaN  0.083881       NaN
                                     historical_tod_mean   3.587860       NaN   6.391196       NaN  0.085117       NaN
                                     neighbor_average      7.503542       NaN  11.718169       NaN  0.184630       NaN
       coverage                      gls_map               3.545198       NaN   6.112684       NaN  0.086683       NaN
                                     gsp                   3.614509       NaN   6.333774       NaN  0.087869       NaN
                                     historical_tod_mean   3.665154       NaN   6.545170       NaN  0.088859       NaN
                                     neighbor_average      7.585813       NaN  11.833535       NaN  0.201476       NaN
       degree                        gls_map               3.950618       NaN   6.598333       NaN  0.093492       NaN
                                     gsp                   3.797454       NaN   6.372972       NaN  0.087659       NaN
                                     historical_tod_mean   3.622977       NaN   6.432266       NaN  0.086451       NaN
                                     neighbor_average      8.237738       NaN  12.600855       NaN  0.217286       NaN
       graph_sampling_laplacian      gls_map               3.593579       NaN   6.160672       NaN  0.088115       NaN
                                     gsp                   3.492027       NaN   6.086054       NaN  0.084744       NaN
                                     historical_tod_mean   3.584132       NaN   6.360185       NaN  0.084813       NaN
                                     neighbor_average      8.848054       NaN  14.206425       NaN  0.213854       NaN
       greedy_a_trace                gls_map               3.363420       NaN   5.864184       NaN  0.089243       NaN
                                     gsp                   3.613800       NaN   6.279505       NaN  0.090949       NaN
                                     historical_tod_mean   3.661562       NaN   6.506869       NaN  0.088512       NaN
                                     neighbor_average      7.011076       NaN  11.050829       NaN  0.199084       NaN
       greedy_d_logdet               gls_map               3.947747       NaN   6.475250       NaN  0.094567       NaN
                                     gsp                   3.681275       NaN   6.357328       NaN  0.086248       NaN
                                     historical_tod_mean   3.648436       NaN   6.462561       NaN  0.087098       NaN
                                     neighbor_average      7.562804       NaN  12.393201       NaN  0.221535       NaN
       multistart_swap_by_validation gls_map               3.276637       NaN   5.715285       NaN  0.082922       NaN
                                     gsp                   3.586470       NaN   6.241303       NaN  0.088588       NaN
                                     historical_tod_mean   3.653585       NaN   6.486705       NaN  0.087684       NaN
                                     neighbor_average      7.179294       NaN  11.234257       NaN  0.196723       NaN
       observability_proxy           gls_map               3.734259       NaN   6.221495       NaN  0.089015       NaN
                                     gsp                   3.759930       NaN   6.336405       NaN  0.086613       NaN
                                     historical_tod_mean   3.605693       NaN   6.398097       NaN  0.085748       NaN
                                     neighbor_average      7.866184       NaN  12.196209       NaN  0.207042       NaN
       qr_pod_modes                  gls_map               3.548213       NaN   6.062396       NaN  0.090245       NaN
                                     gsp                   3.622958       NaN   6.277685       NaN  0.088809       NaN
                                     historical_tod_mean   3.691369       NaN   6.498404       NaN  0.088541       NaN
                                     neighbor_average      7.238172       NaN  11.908945       NaN  0.214542       NaN
       random                        gls_map               3.451340  0.081298   5.935195  0.110873  0.084980  0.002985
                                     gsp                   3.573399  0.049006   6.215187  0.061743  0.086756  0.001935
                                     historical_tod_mean   3.630332  0.035189   6.459027  0.049897  0.086922  0.001409
                                     neighbor_average      7.384275  0.272022  11.437950  0.384596  0.187947  0.009513
       rcss_selected                 gls_map               3.305323       NaN   5.684296       NaN  0.083387       NaN
                                     gsp                   3.581634       NaN   6.248660       NaN  0.088493       NaN
                                     historical_tod_mean   3.637968       NaN   6.456757       NaN  0.087070       NaN
                                     neighbor_average      7.124229       NaN  11.239903       NaN  0.194836       NaN
       robust_coverage_cvar          gls_map               3.382396       NaN   5.861025       NaN  0.084848       NaN
                                     gsp                   3.540864       NaN   6.248374       NaN  0.087886       NaN
                                     historical_tod_mean   3.648261       NaN   6.500834       NaN  0.087931       NaN
                                     neighbor_average      7.238171       NaN  11.498354       NaN  0.201894       NaN
       scenario_average_a_trace      gls_map               3.374260       NaN   5.915493       NaN  0.083131       NaN
                                     gsp                   3.609523       NaN   6.362220       NaN  0.089184       NaN
                                     historical_tod_mean   3.688495       NaN   6.554100       NaN  0.088018       NaN
                                     neighbor_average      7.147828       NaN  11.292789       NaN  0.184461       NaN
       scenario_cvar_a_trace         gls_map               3.424516       NaN   5.954413       NaN  0.088942       NaN
                                     gsp                   3.610204       NaN   6.292244       NaN  0.091130       NaN
                                     historical_tod_mean   3.686300       NaN   6.543495       NaN  0.089224       NaN
                                     neighbor_average      7.340723       NaN  11.619972       NaN  0.208775       NaN
       swap_from_best_random_trace   gls_map               3.335541       NaN   5.864469       NaN  0.085407       NaN
                                     gsp                   3.611357       NaN   6.312767       NaN  0.090304       NaN
                                     historical_tod_mean   3.678470       NaN   6.524745       NaN  0.088829       NaN
                                     neighbor_average      6.898907       NaN  11.161764       NaN  0.199150       NaN
       swap_from_greedy_a_trace      gls_map               3.370726       NaN   5.885388       NaN  0.088597       NaN
                                     gsp                   3.618493       NaN   6.289864       NaN  0.090973       NaN
                                     historical_tod_mean   3.667658       NaN   6.512674       NaN  0.088781       NaN
                                     neighbor_average      6.918464       NaN  11.092009       NaN  0.199566       NaN
       swap_from_scenario_average    gls_map               3.305323       NaN   5.684296       NaN  0.083387       NaN
                                     gsp                   3.581634       NaN   6.248660       NaN  0.088493       NaN
                                     historical_tod_mean   3.637968       NaN   6.456757       NaN  0.087070       NaN
                                     neighbor_average      7.124229       NaN  11.239903       NaN  0.194836       NaN
       swap_from_scenario_cvar       gls_map               3.370726       NaN   5.885388       NaN  0.088597       NaN
                                     gsp                   3.618493       NaN   6.289864       NaN  0.090973       NaN
                                     historical_tod_mean   3.667658       NaN   6.512674       NaN  0.088781       NaN
                                     neighbor_average      6.918464       NaN  11.092009       NaN  0.199566       NaN
       top_variance                  gls_map               3.373488       NaN   5.784621       NaN  0.073979       NaN
                                     gsp                   3.410445       NaN   5.911372       NaN  0.076026       NaN
                                     historical_tod_mean   3.425347       NaN   6.086659       NaN  0.077101       NaN
                                     neighbor_average     11.652018       NaN  17.831995       NaN  0.219821       NaN
       validation_swap_selected      gls_map               3.277882       NaN   5.648382       NaN  0.082273       NaN
                                     gsp                   3.550093       NaN   6.228769       NaN  0.087598       NaN
                                     historical_tod_mean   3.623339       NaN   6.464506       NaN  0.087262       NaN
                                     neighbor_average      7.262661       NaN  11.487014       NaN  0.200037       NaN
0.2    best_random_by_trace          gls_map               3.135280       NaN   5.609461       NaN  0.078321       NaN
                                     gsp                   3.531216       NaN   6.172805       NaN  0.086385       NaN
                                     historical_tod_mean   3.651484       NaN   6.484968       NaN  0.086837       NaN
                                     neighbor_average      7.017937       NaN  10.966672       NaN  0.175810       NaN
       best_random_by_validation     gls_map               3.162783       NaN   5.452185       NaN  0.074538       NaN
                                     gsp                   3.515422       NaN   6.152717       NaN  0.082282       NaN
                                     historical_tod_mean   3.600130       NaN   6.404775       NaN  0.084445       NaN
                                     neighbor_average      7.291089       NaN  11.312753       NaN  0.178403       NaN
       coverage                      gls_map               3.301874       NaN   5.715035       NaN  0.081296       NaN
                                     gsp                   3.604042       NaN   6.273969       NaN  0.087512       NaN
                                     historical_tod_mean   3.653070       NaN   6.529391       NaN  0.088948       NaN
                                     neighbor_average      7.139323       NaN  11.031795       NaN  0.184069       NaN
       degree                        gls_map               3.828348       NaN   6.379412       NaN  0.087999       NaN
                                     gsp                   3.860859       NaN   6.419660       NaN  0.087763       NaN
                                     historical_tod_mean   3.698397       NaN   6.487518       NaN  0.085667       NaN
                                     neighbor_average      7.709745       NaN  11.627840       NaN  0.184614       NaN
       graph_sampling_laplacian      gls_map               3.500218       NaN   6.060484       NaN  0.087319       NaN
                                     gsp                   3.458688       NaN   6.103554       NaN  0.086773       NaN
                                     historical_tod_mean   3.520378       NaN   6.350828       NaN  0.084959       NaN
                                     neighbor_average      7.130811       NaN  10.963929       NaN  0.193463       NaN
       greedy_a_trace                gls_map               3.094866       NaN   5.334355       NaN  0.076742       NaN
                                     gsp                   3.570005       NaN   6.175086       NaN  0.086562       NaN
                                     historical_tod_mean   3.664687       NaN   6.485176       NaN  0.087380       NaN
                                     neighbor_average      6.773569       NaN  10.716591       NaN  0.190086       NaN
       greedy_d_logdet               gls_map               3.594791       NaN   5.924951       NaN  0.087726       NaN
                                     gsp                   3.648551       NaN   6.322655       NaN  0.088087       NaN
                                     historical_tod_mean   3.682873       NaN   6.528977       NaN  0.089110       NaN
                                     neighbor_average      7.527475       NaN  12.167617       NaN  0.223284       NaN
       multistart_swap_by_validation gls_map               3.087472       NaN   5.392864       NaN  0.076988       NaN
                                     gsp                   3.548184       NaN   6.174333       NaN  0.085824       NaN
                                     historical_tod_mean   3.654670       NaN   6.471464       NaN  0.087773       NaN
                                     neighbor_average      6.911246       NaN  10.857867       NaN  0.190369       NaN
       observability_proxy           gls_map               3.591907       NaN   6.117768       NaN  0.085336       NaN
                                     gsp                   3.770983       NaN   6.383751       NaN  0.087550       NaN
                                     historical_tod_mean   3.702082       NaN   6.526137       NaN  0.087646       NaN
                                     neighbor_average      7.805507       NaN  12.010873       NaN  0.203514       NaN
       qr_pod_modes                  gls_map               3.378126       NaN   5.655808       NaN  0.084310       NaN
                                     gsp                   3.582113       NaN   6.193668       NaN  0.085353       NaN
                                     historical_tod_mean   3.622464       NaN   6.413260       NaN  0.086316       NaN
                                     neighbor_average      6.957584       NaN  10.992292       NaN  0.196392       NaN
       random                        gls_map               3.234480  0.068982   5.620289  0.127263  0.079991  0.003398
                                     gsp                   3.555757  0.043234   6.188294  0.084602  0.087399  0.002867
                                     historical_tod_mean   3.640318  0.049202   6.477510  0.087326  0.087453  0.002177
                                     neighbor_average      7.105948  0.209295  11.099582  0.352958  0.182401  0.008886
       rcss_selected                 gls_map               3.041089       NaN   5.354087       NaN  0.074804       NaN
                                     gsp                   3.487272       NaN   6.099084       NaN  0.085561       NaN
                                     historical_tod_mean   3.610100       NaN   6.420240       NaN  0.086365       NaN
                                     neighbor_average      7.315153       NaN  11.487846       NaN  0.174425       NaN
       robust_coverage_cvar          gls_map               3.275666       NaN   5.684897       NaN  0.080558       NaN
                                     gsp                   3.598276       NaN   6.253337       NaN  0.088906       NaN
                                     historical_tod_mean   3.673601       NaN   6.535163       NaN  0.088503       NaN
                                     neighbor_average      6.973876       NaN  10.883253       NaN  0.189955       NaN
       scenario_average_a_trace      gls_map               3.286752       NaN   5.794686       NaN  0.081619       NaN
                                     gsp                   3.654666       NaN   6.411994       NaN  0.091073       NaN
                                     historical_tod_mean   3.749174       NaN   6.674482       NaN  0.090736       NaN
                                     neighbor_average      7.175846       NaN  11.244167       NaN  0.188352       NaN
       scenario_cvar_a_trace         gls_map               3.308350       NaN   5.816319       NaN  0.086303       NaN
                                     gsp                   3.663168       NaN   6.394438       NaN  0.093627       NaN
                                     historical_tod_mean   3.738147       NaN   6.655384       NaN  0.091679       NaN
                                     neighbor_average      7.116515       NaN  11.394407       NaN  0.208173       NaN
       swap_from_best_random_trace   gls_map               3.079062       NaN   5.335341       NaN  0.076590       NaN
                                     gsp                   3.574990       NaN   6.185943       NaN  0.085522       NaN
                                     historical_tod_mean   3.673101       NaN   6.472161       NaN  0.087526       NaN
                                     neighbor_average      6.718062       NaN  10.643499       NaN  0.184612       NaN
       swap_from_greedy_a_trace      gls_map               3.119541       NaN   5.366216       NaN  0.077332       NaN
                                     gsp                   3.596795       NaN   6.207007       NaN  0.086136       NaN
                                     historical_tod_mean   3.682526       NaN   6.480770       NaN  0.087657       NaN
                                     neighbor_average      6.787978       NaN  10.817558       NaN  0.190675       NaN
       swap_from_scenario_average    gls_map               3.151604       NaN   5.429774       NaN  0.078995       NaN
                                     gsp                   3.591763       NaN   6.200124       NaN  0.087128       NaN
                                     historical_tod_mean   3.676294       NaN   6.477641       NaN  0.088462       NaN
                                     neighbor_average      6.952075       NaN  11.066220       NaN  0.194656       NaN
       swap_from_scenario_cvar       gls_map               3.128584       NaN   5.324105       NaN  0.077186       NaN
                                     gsp                   3.586291       NaN   6.194529       NaN  0.086102       NaN
                                     historical_tod_mean   3.654424       NaN   6.470699       NaN  0.087593       NaN
                                     neighbor_average      6.708199       NaN  10.612438       NaN  0.186291       NaN
       top_variance                  gls_map               3.028992       NaN   5.317050       NaN  0.067885       NaN
                                     gsp                   3.190120       NaN   5.612796       NaN  0.071617       NaN
                                     historical_tod_mean   3.255183       NaN   5.826492       NaN  0.072673       NaN
                                     neighbor_average      9.530744       NaN  15.049753       NaN  0.178792       NaN
       validation_swap_selected      gls_map               2.968536       NaN   5.223601       NaN  0.071709       NaN
                                     gsp                   3.415368       NaN   5.995539       NaN  0.082572       NaN
                                     historical_tod_mean   3.542706       NaN   6.317235       NaN  0.083887       NaN
                                     neighbor_average      7.378006       NaN  11.449241       NaN  0.173465       NaN
0.3    best_random_by_trace          gls_map               2.907207       NaN   5.115011       NaN  0.069684       NaN
                                     gsp                   3.447303       NaN   6.035720       NaN  0.084280       NaN
                                     historical_tod_mean   3.546458       NaN   6.380680       NaN  0.085519       NaN
                                     neighbor_average      6.746192       NaN  10.530403       NaN  0.162822       NaN
       best_random_by_validation     gls_map               3.017691       NaN   5.303216       NaN  0.073165       NaN
                                     gsp                   3.531368       NaN   6.219244       NaN  0.085154       NaN
                                     historical_tod_mean   3.647415       NaN   6.533319       NaN  0.087509       NaN
                                     neighbor_average      6.835962       NaN  10.680478       NaN  0.176365       NaN
       coverage                      gls_map               3.025668       NaN   5.337080       NaN  0.075045       NaN
                                     gsp                   3.483169       NaN   6.130870       NaN  0.085501       NaN
                                     historical_tod_mean   3.592184       NaN   6.456080       NaN  0.087103       NaN
                                     neighbor_average      6.823454       NaN  10.351858       NaN  0.174345       NaN
       degree                        gls_map               3.637240       NaN   6.160066       NaN  0.084263       NaN
                                     gsp                   3.762686       NaN   6.347425       NaN  0.086157       NaN
                                     historical_tod_mean   3.690691       NaN   6.494577       NaN  0.084898       NaN
                                     neighbor_average      7.984630       NaN  12.443853       NaN  0.205113       NaN
       graph_sampling_laplacian      gls_map               3.399049       NaN   5.963695       NaN  0.086242       NaN
                                     gsp                   3.490756       NaN   6.147700       NaN  0.088067       NaN
                                     historical_tod_mean   3.552923       NaN   6.379615       NaN  0.086305       NaN
                                     neighbor_average      7.147255       NaN  11.470411       NaN  0.186247       NaN
       greedy_a_trace                gls_map               2.965570       NaN   5.082164       NaN  0.075112       NaN
                                     gsp                   3.552034       NaN   6.185207       NaN  0.087846       NaN
                                     historical_tod_mean   3.661165       NaN   6.517378       NaN  0.089130       NaN
                                     neighbor_average      6.682568       NaN  10.574697       NaN  0.192779       NaN
       greedy_d_logdet               gls_map               3.324754       NaN   5.568665       NaN  0.085161       NaN
                                     gsp                   3.519402       NaN   6.155125       NaN  0.087883       NaN
                                     historical_tod_mean   3.609653       NaN   6.458405       NaN  0.088602       NaN
                                     neighbor_average      7.429861       NaN  11.897519       NaN  0.222171       NaN
       multistart_swap_by_validation gls_map               2.778063       NaN   4.862347       NaN  0.068654       NaN
                                     gsp                   3.382718       NaN   5.964249       NaN  0.082738       NaN
                                     historical_tod_mean   3.511242       NaN   6.314990       NaN  0.084183       NaN
                                     neighbor_average      6.612927       NaN  10.635998       NaN  0.179774       NaN
       observability_proxy           gls_map               3.557752       NaN   6.069595       NaN  0.081970       NaN
                                     gsp                   3.756786       NaN   6.345875       NaN  0.085278       NaN
                                     historical_tod_mean   3.705955       NaN   6.510276       NaN  0.084811       NaN
                                     neighbor_average      7.804015       NaN  11.739716       NaN  0.189559       NaN
       qr_pod_modes                  gls_map               3.012552       NaN   5.170725       NaN  0.076088       NaN
                                     gsp                   3.498186       NaN   6.085134       NaN  0.086007       NaN
                                     historical_tod_mean   3.593331       NaN   6.387317       NaN  0.087214       NaN
                                     neighbor_average      6.738251       NaN  10.602501       NaN  0.186922       NaN
       random                        gls_map               3.060346  0.082272   5.326085  0.133789  0.074617  0.002983
                                     gsp                   3.533902  0.081725   6.136473  0.117188  0.086241  0.002837
                                     historical_tod_mean   3.633287  0.081624   6.455705  0.119963  0.086721  0.002394
                                     neighbor_average      6.929476  0.184282  10.849134  0.298213  0.174408  0.008429
       rcss_selected                 gls_map               2.778063       NaN   4.862347       NaN  0.068654       NaN
                                     gsp                   3.382718       NaN   5.964249       NaN  0.082738       NaN
                                     historical_tod_mean   3.511242       NaN   6.314990       NaN  0.084183       NaN
                                     neighbor_average      6.612927       NaN  10.635998       NaN  0.179774       NaN
       robust_coverage_cvar          gls_map               3.053239       NaN   5.248363       NaN  0.074906       NaN
                                     gsp                   3.535708       NaN   6.176387       NaN  0.089154       NaN
                                     historical_tod_mean   3.636695       NaN   6.494837       NaN  0.088351       NaN
                                     neighbor_average      7.068819       NaN  10.954742       NaN  0.188938       NaN
       scenario_average_a_trace      gls_map               3.146860       NaN   5.479253       NaN  0.077684       NaN
                                     gsp                   3.614026       NaN   6.316913       NaN  0.089714       NaN
                                     historical_tod_mean   3.707446       NaN   6.618792       NaN  0.089873       NaN
                                     neighbor_average      6.896892       NaN  10.656859       NaN  0.177680       NaN
       scenario_cvar_a_trace         gls_map               3.254545       NaN   5.794027       NaN  0.085359       NaN
                                     gsp                   3.674568       NaN   6.432268       NaN  0.094755       NaN
                                     historical_tod_mean   3.749249       NaN   6.691229       NaN  0.092455       NaN
                                     neighbor_average      7.195142       NaN  11.497676       NaN  0.201227       NaN
       swap_from_best_random_trace   gls_map               2.910773       NaN   5.071893       NaN  0.072168       NaN
                                     gsp                   3.500554       NaN   6.135893       NaN  0.085741       NaN
                                     historical_tod_mean   3.607255       NaN   6.455121       NaN  0.087201       NaN
                                     neighbor_average      6.730285       NaN  10.543290       NaN  0.186545       NaN
       swap_from_greedy_a_trace      gls_map               2.936049       NaN   5.020547       NaN  0.074545       NaN
                                     gsp                   3.517275       NaN   6.113199       NaN  0.086817       NaN
                                     historical_tod_mean   3.614866       NaN   6.428888       NaN  0.087721       NaN
                                     neighbor_average      6.651749       NaN  10.548657       NaN  0.191420       NaN
       swap_from_scenario_average    gls_map               3.001718       NaN   5.120422       NaN  0.075130       NaN
                                     gsp                   3.534525       NaN   6.104333       NaN  0.085731       NaN
                                     historical_tod_mean   3.636448       NaN   6.432238       NaN  0.087196       NaN
                                     neighbor_average      6.724540       NaN  10.552205       NaN  0.188916       NaN
       swap_from_scenario_cvar       gls_map               2.984227       NaN   5.077411       NaN  0.073256       NaN
                                     gsp                   3.494187       NaN   6.105057       NaN  0.085319       NaN
                                     historical_tod_mean   3.599095       NaN   6.433107       NaN  0.086571       NaN
                                     neighbor_average      6.754779       NaN  10.676033       NaN  0.182706       NaN
       top_variance                  gls_map               2.848375       NaN   4.979359       NaN  0.062424       NaN
                                     gsp                   3.074251       NaN   5.365938       NaN  0.067651       NaN
                                     historical_tod_mean   3.100531       NaN   5.512248       NaN  0.068009       NaN
                                     neighbor_average      8.995061       NaN  13.971489       NaN  0.166981       NaN
       validation_swap_selected      gls_map               2.691172       NaN   4.713189       NaN  0.066334       NaN
                                     gsp                   3.272473       NaN   5.809858       NaN  0.079920       NaN
                                     historical_tod_mean   3.393824       NaN   6.157517       NaN  0.081147       NaN
                                     neighbor_average      6.700044       NaN  10.619594       NaN  0.176230       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1 multistart_swap_by_validation gls_map 3.276637 5.715285
    0.2      validation_swap_selected gls_map 2.968536 5.223601
    0.3      validation_swap_selected gls_map 2.691172 4.713189
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.250426      0.313933 210
    gsp   condition_number     0.251939      0.314814 210
    gsp information_logdet    -0.293904     -0.370364 210
gls_map    posterior_trace     0.819877      0.838337 210
gls_map   condition_number     0.778407      0.869073 210
gls_map information_logdet    -0.753767     -0.799324 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv