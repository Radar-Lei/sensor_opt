---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-13, 2012-06-04
Test days: 2012-05-22, 2012-06-21
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.454356       NaN   5.905307       NaN  0.086370       NaN
                                     gsp                   3.731621       NaN   6.434294       NaN  0.098152       NaN
                                     historical_tod_mean   3.683146       NaN   6.541629       NaN  0.100265       NaN
                                     neighbor_average      8.052573       NaN  12.191950       NaN  0.206319       NaN
       best_random_by_validation     gls_map               3.454356       NaN   5.905307       NaN  0.086370       NaN
                                     gsp                   3.731621       NaN   6.434294       NaN  0.098152       NaN
                                     historical_tod_mean   3.683146       NaN   6.541629       NaN  0.100265       NaN
                                     neighbor_average      8.052573       NaN  12.191950       NaN  0.206319       NaN
       coverage                      gls_map               3.591871       NaN   6.247931       NaN  0.096702       NaN
                                     gsp                   3.709346       NaN   6.543637       NaN  0.102608       NaN
                                     historical_tod_mean   3.730957       NaN   6.648445       NaN  0.105073       NaN
                                     neighbor_average      8.316941       NaN  12.759592       NaN  0.238144       NaN
       degree                        gls_map               3.837879       NaN   6.578034       NaN  0.103180       NaN
                                     gsp                   3.876998       NaN   6.655362       NaN  0.107062       NaN
                                     historical_tod_mean   3.747767       NaN   6.668615       NaN  0.105772       NaN
                                     neighbor_average      9.046440       NaN  13.827927       NaN  0.258995       NaN
       greedy_a_trace                gls_map               3.372048       NaN   5.715903       NaN  0.085057       NaN
                                     gsp                   3.737611       NaN   6.417645       NaN  0.100689       NaN
                                     historical_tod_mean   3.703912       NaN   6.537871       NaN  0.102540       NaN
                                     neighbor_average      8.018880       NaN  12.052376       NaN  0.230723       NaN
       greedy_d_logdet               gls_map               4.039826       NaN   6.634955       NaN  0.105050       NaN
                                     gsp                   3.893550       NaN   6.660342       NaN  0.107347       NaN
                                     historical_tod_mean   3.732749       NaN   6.590158       NaN  0.104343       NaN
                                     neighbor_average      8.570097       NaN  13.727796       NaN  0.273474       NaN
       multistart_swap_by_validation gls_map               3.312116       NaN   5.641950       NaN  0.084464       NaN
                                     gsp                   3.691148       NaN   6.391428       NaN  0.100295       NaN
                                     historical_tod_mean   3.699534       NaN   6.520867       NaN  0.102626       NaN
                                     neighbor_average      7.908484       NaN  12.215172       NaN  0.231704       NaN
       random                        gls_map               3.600235  0.078829   6.148169  0.112727  0.092871  0.002605
                                     gsp                   3.743181  0.052104   6.447138  0.061245  0.100272  0.001894
                                     historical_tod_mean   3.695429  0.034101   6.552153  0.051554  0.102372  0.001385
                                     neighbor_average      8.174584  0.292915  12.427752  0.427283  0.221571  0.010822
       rcss_selected                 gls_map               3.372048       NaN   5.715903       NaN  0.085057       NaN
                                     gsp                   3.737611       NaN   6.417645       NaN  0.100689       NaN
                                     historical_tod_mean   3.703912       NaN   6.537871       NaN  0.102540       NaN
                                     neighbor_average      8.018880       NaN  12.052376       NaN  0.230723       NaN
       robust_coverage_cvar          gls_map               3.409311       NaN   5.758304       NaN  0.087782       NaN
                                     gsp                   3.695429       NaN   6.399115       NaN  0.100616       NaN
                                     historical_tod_mean   3.669786       NaN   6.511323       NaN  0.101775       NaN
                                     neighbor_average      7.944804       NaN  11.939610       NaN  0.217897       NaN
       scenario_average_a_trace      gls_map               3.386402       NaN   5.803421       NaN  0.086481       NaN
                                     gsp                   3.698014       NaN   6.433348       NaN  0.100448       NaN
                                     historical_tod_mean   3.703206       NaN   6.548714       NaN  0.102481       NaN
                                     neighbor_average      7.897002       NaN  12.036821       NaN  0.217914       NaN
       scenario_cvar_a_trace         gls_map               3.341230       NaN   5.818439       NaN  0.089382       NaN
                                     gsp                   3.618324       NaN   6.351958       NaN  0.099628       NaN
                                     historical_tod_mean   3.636959       NaN   6.490622       NaN  0.101905       NaN
                                     neighbor_average      7.811567       NaN  11.874360       NaN  0.214325       NaN
       swap_from_best_random_trace   gls_map               3.353206       NaN   5.699783       NaN  0.084670       NaN
                                     gsp                   3.735039       NaN   6.439054       NaN  0.100925       NaN
                                     historical_tod_mean   3.722147       NaN   6.562594       NaN  0.103369       NaN
                                     neighbor_average      7.838054       NaN  12.098058       NaN  0.236105       NaN
       swap_from_greedy_a_trace      gls_map               3.313482       NaN   5.628704       NaN  0.083703       NaN
                                     gsp                   3.690614       NaN   6.386352       NaN  0.100367       NaN
                                     historical_tod_mean   3.706393       NaN   6.530112       NaN  0.102714       NaN
                                     neighbor_average      7.889146       NaN  12.142231       NaN  0.231436       NaN
       swap_from_scenario_average    gls_map               3.313482       NaN   5.628704       NaN  0.083703       NaN
                                     gsp                   3.690614       NaN   6.386352       NaN  0.100367       NaN
                                     historical_tod_mean   3.706393       NaN   6.530112       NaN  0.102714       NaN
                                     neighbor_average      7.889146       NaN  12.142231       NaN  0.231436       NaN
       swap_from_scenario_cvar       gls_map               3.381461       NaN   5.712870       NaN  0.085279       NaN
                                     gsp                   3.737283       NaN   6.440331       NaN  0.100920       NaN
                                     historical_tod_mean   3.727571       NaN   6.569307       NaN  0.103193       NaN
                                     neighbor_average      7.752612       NaN  12.011563       NaN  0.230054       NaN
       top_variance                  gls_map               3.470139       NaN   6.030046       NaN  0.088578       NaN
                                     gsp                   3.487188       NaN   6.163814       NaN  0.091530       NaN
                                     historical_tod_mean   3.513384       NaN   6.276406       NaN  0.093965       NaN
                                     neighbor_average     11.606882       NaN  17.824036       NaN  0.227971       NaN
       validation_swap_selected      gls_map               3.353064       NaN   5.777630       NaN  0.087806       NaN
                                     gsp                   3.689655       NaN   6.413504       NaN  0.101405       NaN
                                     historical_tod_mean   3.676165       NaN   6.530145       NaN  0.103178       NaN
                                     neighbor_average      8.078970       NaN  12.448028       NaN  0.237418       NaN
0.2    best_random_by_trace          gls_map               3.319871       NaN   5.668689       NaN  0.085301       NaN
                                     gsp                   3.686841       NaN   6.405100       NaN  0.100995       NaN
                                     historical_tod_mean   3.685598       NaN   6.541539       NaN  0.102608       NaN
                                     neighbor_average      7.686524       NaN  11.806984       NaN  0.224379       NaN
       best_random_by_validation     gls_map               3.219863       NaN   5.553728       NaN  0.082067       NaN
                                     gsp                   3.602925       NaN   6.204430       NaN  0.094943       NaN
                                     historical_tod_mean   3.601991       NaN   6.396835       NaN  0.098482       NaN
                                     neighbor_average      8.438061       NaN  12.659977       NaN  0.209153       NaN
       coverage                      gls_map               3.438834       NaN   6.047056       NaN  0.091886       NaN
                                     gsp                   3.748169       NaN   6.602642       NaN  0.104414       NaN
                                     historical_tod_mean   3.774634       NaN   6.767031       NaN  0.108279       NaN
                                     neighbor_average      7.766037       NaN  11.891089       NaN  0.221236       NaN
       degree                        gls_map               3.886744       NaN   6.499446       NaN  0.095955       NaN
                                     gsp                   4.046459       NaN   6.725089       NaN  0.101868       NaN
                                     historical_tod_mean   3.783454       NaN   6.581944       NaN  0.100365       NaN
                                     neighbor_average      8.617375       NaN  12.935042       NaN  0.222040       NaN
       greedy_a_trace                gls_map               3.231206       NaN   5.500374       NaN  0.081682       NaN
                                     gsp                   3.803536       NaN   6.501572       NaN  0.103219       NaN
                                     historical_tod_mean   3.764963       NaN   6.621874       NaN  0.105286       NaN
                                     neighbor_average      7.598942       NaN  11.785714       NaN  0.232256       NaN
       greedy_d_logdet               gls_map               3.894728       NaN   6.262705       NaN  0.100735       NaN
                                     gsp                   3.856600       NaN   6.547795       NaN  0.105051       NaN
                                     historical_tod_mean   3.757955       NaN   6.590120       NaN  0.105810       NaN
                                     neighbor_average      8.545895       NaN  13.447130       NaN  0.272383       NaN
       multistart_swap_by_validation gls_map               3.129994       NaN   5.322180       NaN  0.080836       NaN
                                     gsp                   3.600684       NaN   6.219526       NaN  0.096274       NaN
                                     historical_tod_mean   3.594131       NaN   6.357608       NaN  0.099781       NaN
                                     neighbor_average      7.471588       NaN  11.508238       NaN  0.213816       NaN
       random                        gls_map               3.373438  0.074078   5.805465  0.137060  0.086503  0.002766
                                     gsp                   3.731334  0.063051   6.422355  0.094568  0.099744  0.002483
                                     historical_tod_mean   3.700816  0.061265   6.563082  0.095711  0.102593  0.002438
                                     neighbor_average      7.925321  0.207682  12.153632  0.337694  0.213125  0.010203
       rcss_selected                 gls_map               3.129994       NaN   5.322180       NaN  0.080836       NaN
                                     gsp                   3.600684       NaN   6.219526       NaN  0.096274       NaN
                                     historical_tod_mean   3.594131       NaN   6.357608       NaN  0.099781       NaN
                                     neighbor_average      7.471588       NaN  11.508238       NaN  0.213816       NaN
       robust_coverage_cvar          gls_map               3.231813       NaN   5.457590       NaN  0.081945       NaN
                                     gsp                   3.670927       NaN   6.370557       NaN  0.098745       NaN
                                     historical_tod_mean   3.648556       NaN   6.498402       NaN  0.100985       NaN
                                     neighbor_average      7.751566       NaN  11.710094       NaN  0.213788       NaN
       scenario_average_a_trace      gls_map               3.216565       NaN   5.449039       NaN  0.082598       NaN
                                     gsp                   3.689753       NaN   6.366855       NaN  0.100347       NaN
                                     historical_tod_mean   3.674507       NaN   6.495105       NaN  0.102459       NaN
                                     neighbor_average      7.716569       NaN  11.745689       NaN  0.222205       NaN
       scenario_cvar_a_trace         gls_map               3.224088       NaN   5.485906       NaN  0.083218       NaN
                                     gsp                   3.636399       NaN   6.301289       NaN  0.099190       NaN
                                     historical_tod_mean   3.612447       NaN   6.438738       NaN  0.100947       NaN
                                     neighbor_average      7.537681       NaN  11.456507       NaN  0.211489       NaN
       swap_from_best_random_trace   gls_map               3.213098       NaN   5.433228       NaN  0.081237       NaN
                                     gsp                   3.749122       NaN   6.429814       NaN  0.101857       NaN
                                     historical_tod_mean   3.702079       NaN   6.541384       NaN  0.103299       NaN
                                     neighbor_average      7.715662       NaN  12.062102       NaN  0.233365       NaN
       swap_from_greedy_a_trace      gls_map               3.205859       NaN   5.431192       NaN  0.081745       NaN
                                     gsp                   3.799127       NaN   6.486156       NaN  0.103298       NaN
                                     historical_tod_mean   3.739321       NaN   6.567778       NaN  0.104300       NaN
                                     neighbor_average      7.709894       NaN  12.139728       NaN  0.237451       NaN
       swap_from_scenario_average    gls_map               3.181605       NaN   5.377919       NaN  0.080036       NaN
                                     gsp                   3.769787       NaN   6.406378       NaN  0.100780       NaN
                                     historical_tod_mean   3.703673       NaN   6.514418       NaN  0.102661       NaN
                                     neighbor_average      7.503827       NaN  11.714032       NaN  0.225331       NaN
       swap_from_scenario_cvar       gls_map               3.167537       NaN   5.353802       NaN  0.080121       NaN
                                     gsp                   3.738551       NaN   6.400255       NaN  0.101305       NaN
                                     historical_tod_mean   3.705412       NaN   6.504736       NaN  0.102769       NaN
                                     neighbor_average      7.558635       NaN  11.715470       NaN  0.229055       NaN
       top_variance                  gls_map               3.236412       NaN   5.678647       NaN  0.082405       NaN
                                     gsp                   3.359640       NaN   5.937570       NaN  0.087475       NaN
                                     historical_tod_mean   3.353395       NaN   6.065400       NaN  0.088990       NaN
                                     neighbor_average     10.367169       NaN  15.969309       NaN  0.200571       NaN
       validation_swap_selected      gls_map               3.216700       NaN   5.661441       NaN  0.085031       NaN
                                     gsp                   3.615826       NaN   6.333920       NaN  0.098408       NaN
                                     historical_tod_mean   3.597421       NaN   6.502332       NaN  0.101333       NaN
                                     neighbor_average      8.061088       NaN  12.081212       NaN  0.205813       NaN
0.3    best_random_by_trace          gls_map               3.142456       NaN   5.416221       NaN  0.081353       NaN
                                     gsp                   3.654103       NaN   6.316053       NaN  0.099861       NaN
                                     historical_tod_mean   3.644467       NaN   6.505037       NaN  0.103425       NaN
                                     neighbor_average      7.496034       NaN  11.619342       NaN  0.219081       NaN
       best_random_by_validation     gls_map               3.028920       NaN   5.040356       NaN  0.072657       NaN
                                     gsp                   3.573381       NaN   6.024552       NaN  0.091009       NaN
                                     historical_tod_mean   3.526982       NaN   6.203262       NaN  0.094536       NaN
                                     neighbor_average      7.486503       NaN  11.244877       NaN  0.190011       NaN
       coverage                      gls_map               3.231435       NaN   5.698507       NaN  0.085455       NaN
                                     gsp                   3.711922       NaN   6.541097       NaN  0.103730       NaN
                                     historical_tod_mean   3.721946       NaN   6.730619       NaN  0.107397       NaN
                                     neighbor_average      7.588183       NaN  11.332182       NaN  0.211598       NaN
       degree                        gls_map               3.687048       NaN   6.232270       NaN  0.090785       NaN
                                     gsp                   3.843047       NaN   6.484987       NaN  0.098026       NaN
                                     historical_tod_mean   3.708546       NaN   6.505850       NaN  0.098455       NaN
                                     neighbor_average      8.912137       NaN  13.698442       NaN  0.247297       NaN
       greedy_a_trace                gls_map               3.168768       NaN   5.406226       NaN  0.082812       NaN
                                     gsp                   3.861041       NaN   6.579193       NaN  0.106326       NaN
                                     historical_tod_mean   3.813855       NaN   6.715071       NaN  0.109035       NaN
                                     neighbor_average      7.558576       NaN  11.837308       NaN  0.238225       NaN
       greedy_d_logdet               gls_map               3.655170       NaN   5.944931       NaN  0.094609       NaN
                                     gsp                   3.762463       NaN   6.421246       NaN  0.102813       NaN
                                     historical_tod_mean   3.646992       NaN   6.488548       NaN  0.103966       NaN
                                     neighbor_average      8.566943       NaN  13.272104       NaN  0.269741       NaN
       multistart_swap_by_validation gls_map               3.032325       NaN   5.186710       NaN  0.078489       NaN
                                     gsp                   3.639376       NaN   6.358355       NaN  0.100234       NaN
                                     historical_tod_mean   3.621550       NaN   6.516378       NaN  0.103043       NaN
                                     neighbor_average      7.751172       NaN  11.814012       NaN  0.223402       NaN
       random                        gls_map               3.236469  0.085838   5.565406  0.167835  0.081977  0.003255
                                     gsp                   3.723726  0.067557   6.395213  0.102629  0.099110  0.002654
                                     historical_tod_mean   3.696532  0.065505   6.552740  0.103171  0.102425  0.002708
                                     neighbor_average      7.739109  0.201595  11.932779  0.365441  0.207318  0.011037
       rcss_selected                 gls_map               3.033699       NaN   5.406959       NaN  0.078897       NaN
                                     gsp                   3.550854       NaN   6.306396       NaN  0.095518       NaN
                                     historical_tod_mean   3.565978       NaN   6.490768       NaN  0.099278       NaN
                                     neighbor_average      7.640926       NaN  11.575025       NaN  0.185332       NaN
       robust_coverage_cvar          gls_map               3.064729       NaN   5.243976       NaN  0.078562       NaN
                                     gsp                   3.651661       NaN   6.360214       NaN  0.099799       NaN
                                     historical_tod_mean   3.634047       NaN   6.521075       NaN  0.102380       NaN
                                     neighbor_average      7.623702       NaN  11.641268       NaN  0.210944       NaN
       scenario_average_a_trace      gls_map               3.097300       NaN   5.240252       NaN  0.079191       NaN
                                     gsp                   3.676804       NaN   6.366462       NaN  0.101243       NaN
                                     historical_tod_mean   3.640275       NaN   6.491641       NaN  0.102914       NaN
                                     neighbor_average      7.547435       NaN  11.581133       NaN  0.215759       NaN
       scenario_cvar_a_trace         gls_map               3.065649       NaN   5.194576       NaN  0.079864       NaN
                                     gsp                   3.649499       NaN   6.308874       NaN  0.099984       NaN
                                     historical_tod_mean   3.605533       NaN   6.434519       NaN  0.101841       NaN
                                     neighbor_average      7.683385       NaN  11.988310       NaN  0.228229       NaN
       swap_from_best_random_trace   gls_map               3.110857       NaN   5.299810       NaN  0.080281       NaN
                                     gsp                   3.720503       NaN   6.410271       NaN  0.102136       NaN
                                     historical_tod_mean   3.695486       NaN   6.568914       NaN  0.105184       NaN
                                     neighbor_average      7.582736       NaN  11.657281       NaN  0.234142       NaN
       swap_from_greedy_a_trace      gls_map               3.153386       NaN   5.323971       NaN  0.081762       NaN
                                     gsp                   3.774376       NaN   6.452460       NaN  0.103768       NaN
                                     historical_tod_mean   3.745379       NaN   6.590923       NaN  0.106330       NaN
                                     neighbor_average      7.590945       NaN  11.904518       NaN  0.236849       NaN
       swap_from_scenario_average    gls_map               3.150215       NaN   5.302781       NaN  0.080462       NaN
                                     gsp                   3.755074       NaN   6.417890       NaN  0.101811       NaN
                                     historical_tod_mean   3.728664       NaN   6.557133       NaN  0.104816       NaN
                                     neighbor_average      7.613712       NaN  11.845650       NaN  0.229192       NaN
       swap_from_scenario_cvar       gls_map               3.149971       NaN   5.301161       NaN  0.081487       NaN
                                     gsp                   3.764645       NaN   6.438787       NaN  0.102297       NaN
                                     historical_tod_mean   3.728045       NaN   6.584350       NaN  0.105295       NaN
                                     neighbor_average      7.547527       NaN  11.712496       NaN  0.232468       NaN
       top_variance                  gls_map               3.089943       NaN   5.441067       NaN  0.076291       NaN
                                     gsp                   3.250183       NaN   5.753743       NaN  0.081934       NaN
                                     historical_tod_mean   3.233050       NaN   5.890857       NaN  0.083539       NaN
                                     neighbor_average      9.893732       NaN  15.233306       NaN  0.190282       NaN
       validation_swap_selected      gls_map               2.940980       NaN   5.073967       NaN  0.072344       NaN
                                     gsp                   3.510581       NaN   6.160668       NaN  0.092203       NaN
                                     historical_tod_mean   3.484226       NaN   6.333696       NaN  0.095398       NaN
                                     neighbor_average      7.556452       NaN  11.371169       NaN  0.180183       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1 multistart_swap_by_validation gls_map 3.312116 5.641950
    0.2 multistart_swap_by_validation gls_map 3.129994 5.322180
    0.3      validation_swap_selected gls_map 2.940980 5.073967
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.125736      0.153460 651
    gsp   condition_number     0.128036      0.138408 651
    gsp information_logdet    -0.140143     -0.173530 651
gls_map    posterior_trace     0.860539      0.853439 651
gls_map   condition_number     0.831080      0.851678 651
gls_map information_logdet    -0.817072     -0.807390 651
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv