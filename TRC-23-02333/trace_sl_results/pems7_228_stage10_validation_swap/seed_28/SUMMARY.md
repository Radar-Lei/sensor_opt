---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-13, 2012-06-08
Test days: 2012-05-07, 2012-05-30
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.377815       NaN   5.724269       NaN  0.080999       NaN
                                     gsp                   3.562097       NaN   6.197392       NaN  0.086974       NaN
                                     historical_tod_mean   3.816674       NaN   6.686189       NaN  0.089817       NaN
                                     neighbor_average      7.278081       NaN  11.337094       NaN  0.185771       NaN
       best_random_by_validation     gls_map               3.377815       NaN   5.724269       NaN  0.080999       NaN
                                     gsp                   3.562097       NaN   6.197392       NaN  0.086974       NaN
                                     historical_tod_mean   3.816674       NaN   6.686189       NaN  0.089817       NaN
                                     neighbor_average      7.278081       NaN  11.337094       NaN  0.185771       NaN
       coverage                      gls_map               3.576208       NaN   6.075505       NaN  0.085773       NaN
                                     gsp                   3.721344       NaN   6.425346       NaN  0.090033       NaN
                                     historical_tod_mean   3.872928       NaN   6.838673       NaN  0.091417       NaN
                                     neighbor_average      7.528220       NaN  11.863063       NaN  0.200456       NaN
       degree                        gls_map               3.744527       NaN   6.566654       NaN  0.087805       NaN
                                     gsp                   3.827449       NaN   6.716318       NaN  0.089400       NaN
                                     historical_tod_mean   3.908854       NaN   6.886101       NaN  0.091379       NaN
                                     neighbor_average      8.088245       NaN  12.740808       NaN  0.207836       NaN
       greedy_a_trace                gls_map               3.298545       NaN   5.784946       NaN  0.079261       NaN
                                     gsp                   3.749746       NaN   6.415077       NaN  0.088528       NaN
                                     historical_tod_mean   3.880670       NaN   6.828874       NaN  0.090855       NaN
                                     neighbor_average      7.118372       NaN  11.185999       NaN  0.193909       NaN
       greedy_d_logdet               gls_map               3.917772       NaN   6.380912       NaN  0.096769       NaN
                                     gsp                   3.770299       NaN   6.488133       NaN  0.091991       NaN
                                     historical_tod_mean   3.888358       NaN   6.859711       NaN  0.091399       NaN
                                     neighbor_average      7.513673       NaN  12.478248       NaN  0.221050       NaN
       multistart_swap_by_validation gls_map               3.286071       NaN   5.726324       NaN  0.078286       NaN
                                     gsp                   3.749929       NaN   6.392939       NaN  0.088686       NaN
                                     historical_tod_mean   3.881329       NaN   6.799288       NaN  0.090815       NaN
                                     neighbor_average      6.984767       NaN  10.977047       NaN  0.191697       NaN
       random                        gls_map               3.451137  0.075173   5.963940  0.116205  0.082365  0.002181
                                     gsp                   3.655565  0.053817   6.346337  0.075700  0.087328  0.001443
                                     historical_tod_mean   3.850787  0.035052   6.781195  0.056580  0.090036  0.000978
                                     neighbor_average      7.363486  0.245032  11.530211  0.371333  0.188035  0.006247
       rcss_selected                 gls_map               3.252684       NaN   5.613618       NaN  0.077698       NaN
                                     gsp                   3.713994       NaN   6.333119       NaN  0.088231       NaN
                                     historical_tod_mean   3.851169       NaN   6.748324       NaN  0.090162       NaN
                                     neighbor_average      7.130670       NaN  11.059027       NaN  0.190551       NaN
       robust_coverage_cvar          gls_map               3.318598       NaN   5.783446       NaN  0.079302       NaN
                                     gsp                   3.666178       NaN   6.352301       NaN  0.086921       NaN
                                     historical_tod_mean   3.868986       NaN   6.769892       NaN  0.089902       NaN
                                     neighbor_average      7.292263       NaN  11.562661       NaN  0.192143       NaN
       scenario_average_a_trace      gls_map               3.408263       NaN   5.926463       NaN  0.079881       NaN
                                     gsp                   3.689353       NaN   6.402067       NaN  0.087322       NaN
                                     historical_tod_mean   3.870766       NaN   6.816291       NaN  0.089940       NaN
                                     neighbor_average      7.392033       NaN  11.451116       NaN  0.188622       NaN
       scenario_cvar_a_trace         gls_map               3.303246       NaN   5.686310       NaN  0.079627       NaN
                                     gsp                   3.684189       NaN   6.309311       NaN  0.089488       NaN
                                     historical_tod_mean   3.856550       NaN   6.783626       NaN  0.090322       NaN
                                     neighbor_average      7.218865       NaN  11.397252       NaN  0.191698       NaN
       swap_from_best_random_trace   gls_map               3.264099       NaN   5.620789       NaN  0.077454       NaN
                                     gsp                   3.724876       NaN   6.359355       NaN  0.088540       NaN
                                     historical_tod_mean   3.866203       NaN   6.764799       NaN  0.090592       NaN
                                     neighbor_average      7.020890       NaN  10.993816       NaN  0.191090       NaN
       swap_from_greedy_a_trace      gls_map               3.252684       NaN   5.613618       NaN  0.077698       NaN
                                     gsp                   3.713994       NaN   6.333119       NaN  0.088231       NaN
                                     historical_tod_mean   3.851169       NaN   6.748324       NaN  0.090162       NaN
                                     neighbor_average      7.130670       NaN  11.059027       NaN  0.190551       NaN
       swap_from_scenario_average    gls_map               3.347275       NaN   5.782616       NaN  0.078269       NaN
                                     gsp                   3.755654       NaN   6.395204       NaN  0.089202       NaN
                                     historical_tod_mean   3.849622       NaN   6.766683       NaN  0.090321       NaN
                                     neighbor_average      7.129754       NaN  11.158820       NaN  0.190887       NaN
       swap_from_scenario_cvar       gls_map               3.268834       NaN   5.588873       NaN  0.077027       NaN
                                     gsp                   3.711608       NaN   6.303484       NaN  0.087418       NaN
                                     historical_tod_mean   3.843550       NaN   6.721024       NaN  0.089461       NaN
                                     neighbor_average      7.090329       NaN  11.150838       NaN  0.188102       NaN
       top_variance                  gls_map               3.302614       NaN   5.749662       NaN  0.077476       NaN
                                     gsp                   3.380443       NaN   5.973763       NaN  0.080096       NaN
                                     historical_tod_mean   3.636535       NaN   6.385029       NaN  0.083585       NaN
                                     neighbor_average     10.161157       NaN  15.979864       NaN  0.199835       NaN
       validation_swap_selected      gls_map               3.205678       NaN   5.505802       NaN  0.076397       NaN
                                     gsp                   3.661464       NaN   6.276604       NaN  0.087228       NaN
                                     historical_tod_mean   3.830739       NaN   6.717306       NaN  0.089603       NaN
                                     neighbor_average      7.195558       NaN  11.226071       NaN  0.192910       NaN
0.2    best_random_by_trace          gls_map               3.222655       NaN   5.567505       NaN  0.077579       NaN
                                     gsp                   3.649854       NaN   6.302090       NaN  0.089742       NaN
                                     historical_tod_mean   3.855423       NaN   6.817250       NaN  0.091047       NaN
                                     neighbor_average      6.955975       NaN  10.904916       NaN  0.190733       NaN
       best_random_by_validation     gls_map               3.124444       NaN   5.459696       NaN  0.075526       NaN
                                     gsp                   3.605982       NaN   6.297386       NaN  0.088364       NaN
                                     historical_tod_mean   3.837813       NaN   6.828826       NaN  0.090611       NaN
                                     neighbor_average      7.147788       NaN  11.055192       NaN  0.184224       NaN
       coverage                      gls_map               3.261246       NaN   5.716533       NaN  0.078723       NaN
                                     gsp                   3.637450       NaN   6.379599       NaN  0.089764       NaN
                                     historical_tod_mean   3.888532       NaN   6.915098       NaN  0.092950       NaN
                                     neighbor_average      7.028219       NaN  10.993721       NaN  0.187723       NaN
       degree                        gls_map               3.617164       NaN   6.263671       NaN  0.087069       NaN
                                     gsp                   3.721028       NaN   6.480138       NaN  0.087902       NaN
                                     historical_tod_mean   3.943139       NaN   6.875640       NaN  0.091441       NaN
                                     neighbor_average      7.515680       NaN  11.980899       NaN  0.194205       NaN
       greedy_a_trace                gls_map               3.144382       NaN   5.373038       NaN  0.075690       NaN
                                     gsp                   3.708852       NaN   6.318548       NaN  0.089531       NaN
                                     historical_tod_mean   3.905744       NaN   6.826407       NaN  0.092082       NaN
                                     neighbor_average      7.136211       NaN  11.274782       NaN  0.201610       NaN
       greedy_d_logdet               gls_map               3.645134       NaN   5.952973       NaN  0.085953       NaN
                                     gsp                   3.754206       NaN   6.446615       NaN  0.090310       NaN
                                     historical_tod_mean   3.931390       NaN   6.909515       NaN  0.092191       NaN
                                     neighbor_average      7.456650       NaN  12.145015       NaN  0.218106       NaN
       multistart_swap_by_validation gls_map               3.133162       NaN   5.253085       NaN  0.073013       NaN
                                     gsp                   3.594139       NaN   6.154475       NaN  0.085790       NaN
                                     historical_tod_mean   3.803694       NaN   6.648697       NaN  0.089325       NaN
                                     neighbor_average      6.965101       NaN  10.802475       NaN  0.188359       NaN
       random                        gls_map               3.226387  0.072069   5.619756  0.128347  0.076402  0.002208
                                     gsp                   3.627926  0.063852   6.273375  0.087999  0.086957  0.002011
                                     historical_tod_mean   3.850710  0.056545   6.780486  0.088614  0.089992  0.001647
                                     neighbor_average      7.173028  0.187681  11.304244  0.311812  0.182120  0.006680
       rcss_selected                 gls_map               3.133162       NaN   5.253085       NaN  0.073013       NaN
                                     gsp                   3.594139       NaN   6.154475       NaN  0.085790       NaN
                                     historical_tod_mean   3.803694       NaN   6.648697       NaN  0.089325       NaN
                                     neighbor_average      6.965101       NaN  10.802475       NaN  0.188359       NaN
       robust_coverage_cvar          gls_map               3.111490       NaN   5.366317       NaN  0.071720       NaN
                                     gsp                   3.677997       NaN   6.262980       NaN  0.086368       NaN
                                     historical_tod_mean   3.850012       NaN   6.721894       NaN  0.089385       NaN
                                     neighbor_average      7.193712       NaN  11.270846       NaN  0.187573       NaN
       scenario_average_a_trace      gls_map               3.180212       NaN   5.496868       NaN  0.075745       NaN
                                     gsp                   3.696678       NaN   6.283611       NaN  0.088584       NaN
                                     historical_tod_mean   3.871926       NaN   6.803508       NaN  0.090553       NaN
                                     neighbor_average      7.005985       NaN  10.840071       NaN  0.186130       NaN
       scenario_cvar_a_trace         gls_map               3.202723       NaN   5.546885       NaN  0.077717       NaN
                                     gsp                   3.678117       NaN   6.302493       NaN  0.088451       NaN
                                     historical_tod_mean   3.834538       NaN   6.767384       NaN  0.089305       NaN
                                     neighbor_average      7.300498       NaN  11.488431       NaN  0.196217       NaN
       swap_from_best_random_trace   gls_map               3.144447       NaN   5.416600       NaN  0.075193       NaN
                                     gsp                   3.690214       NaN   6.363601       NaN  0.090466       NaN
                                     historical_tod_mean   3.874679       NaN   6.851185       NaN  0.091873       NaN
                                     neighbor_average      7.006131       NaN  11.097253       NaN  0.196950       NaN
       swap_from_greedy_a_trace      gls_map               3.118137       NaN   5.380128       NaN  0.074282       NaN
                                     gsp                   3.707752       NaN   6.374036       NaN  0.089278       NaN
                                     historical_tod_mean   3.918242       NaN   6.863750       NaN  0.091986       NaN
                                     neighbor_average      7.001058       NaN  11.139033       NaN  0.196247       NaN
       swap_from_scenario_average    gls_map               3.102030       NaN   5.328365       NaN  0.075140       NaN
                                     gsp                   3.693869       NaN   6.310662       NaN  0.090227       NaN
                                     historical_tod_mean   3.906642       NaN   6.839321       NaN  0.092396       NaN
                                     neighbor_average      7.113077       NaN  11.330723       NaN  0.201590       NaN
       swap_from_scenario_cvar       gls_map               3.141859       NaN   5.403405       NaN  0.074191       NaN
                                     gsp                   3.706059       NaN   6.335012       NaN  0.088167       NaN
                                     historical_tod_mean   3.911844       NaN   6.828919       NaN  0.091603       NaN
                                     neighbor_average      7.015044       NaN  11.220074       NaN  0.195261       NaN
       top_variance                  gls_map               3.015254       NaN   5.380285       NaN  0.070011       NaN
                                     gsp                   3.240028       NaN   5.763665       NaN  0.076030       NaN
                                     historical_tod_mean   3.474279       NaN   6.164916       NaN  0.079408       NaN
                                     neighbor_average      9.315921       NaN  14.908244       NaN  0.180837       NaN
       validation_swap_selected      gls_map               3.102171       NaN   5.251637       NaN  0.072921       NaN
                                     gsp                   3.540423       NaN   6.118086       NaN  0.085348       NaN
                                     historical_tod_mean   3.754699       NaN   6.628420       NaN  0.088688       NaN
                                     neighbor_average      6.957721       NaN  10.768508       NaN  0.186779       NaN
0.3    best_random_by_trace          gls_map               3.107696       NaN   5.427286       NaN  0.072515       NaN
                                     gsp                   3.659174       NaN   6.249393       NaN  0.086962       NaN
                                     historical_tod_mean   3.819343       NaN   6.787530       NaN  0.088851       NaN
                                     neighbor_average      6.686659       NaN  10.621597       NaN  0.177811       NaN
       best_random_by_validation     gls_map               2.910954       NaN   5.010605       NaN  0.066886       NaN
                                     gsp                   3.509315       NaN   6.057488       NaN  0.081432       NaN
                                     historical_tod_mean   3.744115       NaN   6.594103       NaN  0.085029       NaN
                                     neighbor_average      6.940133       NaN  10.966800       NaN  0.166212       NaN
       coverage                      gls_map               3.084519       NaN   5.417426       NaN  0.073053       NaN
                                     gsp                   3.586717       NaN   6.304464       NaN  0.088007       NaN
                                     historical_tod_mean   3.826094       NaN   6.877436       NaN  0.091490       NaN
                                     neighbor_average      6.955843       NaN  10.686813       NaN  0.179718       NaN
       degree                        gls_map               3.522199       NaN   6.056583       NaN  0.085267       NaN
                                     gsp                   3.649239       NaN   6.338102       NaN  0.086998       NaN
                                     historical_tod_mean   3.917088       NaN   6.848187       NaN  0.090937       NaN
                                     neighbor_average      7.994215       NaN  12.672860       NaN  0.211334       NaN
       greedy_a_trace                gls_map               3.056360       NaN   5.238556       NaN  0.074811       NaN
                                     gsp                   3.692522       NaN   6.334776       NaN  0.091286       NaN
                                     historical_tod_mean   3.903668       NaN   6.882628       NaN  0.093614       NaN
                                     neighbor_average      6.817190       NaN  10.757959       NaN  0.196131       NaN
       greedy_d_logdet               gls_map               3.440676       NaN   5.640431       NaN  0.081813       NaN
                                     gsp                   3.637851       NaN   6.286756       NaN  0.088628       NaN
                                     historical_tod_mean   3.843886       NaN   6.846821       NaN  0.090747       NaN
                                     neighbor_average      7.651496       NaN  12.320914       NaN  0.220919       NaN
       multistart_swap_by_validation gls_map               2.937192       NaN   5.007121       NaN  0.069792       NaN
                                     gsp                   3.592209       NaN   6.167035       NaN  0.087305       NaN
                                     historical_tod_mean   3.802569       NaN   6.716312       NaN  0.089573       NaN
                                     neighbor_average      6.801075       NaN  10.671122       NaN  0.184664       NaN
       random                        gls_map               3.090889  0.077665   5.400282  0.147542  0.072888  0.002228
                                     gsp                   3.621737  0.072865   6.248127  0.104084  0.086974  0.002193
                                     historical_tod_mean   3.852135  0.067825   6.782372  0.105205  0.090094  0.001977
                                     neighbor_average      7.025077  0.187701  11.113526  0.344164  0.178045  0.007721
       rcss_selected                 gls_map               2.910954       NaN   5.010605       NaN  0.066886       NaN
                                     gsp                   3.509315       NaN   6.057488       NaN  0.081432       NaN
                                     historical_tod_mean   3.744115       NaN   6.594103       NaN  0.085029       NaN
                                     neighbor_average      6.940133       NaN  10.966800       NaN  0.166212       NaN
       robust_coverage_cvar          gls_map               3.031897       NaN   5.203562       NaN  0.070673       NaN
                                     gsp                   3.690059       NaN   6.234538       NaN  0.087142       NaN
                                     historical_tod_mean   3.847072       NaN   6.728215       NaN  0.089394       NaN
                                     neighbor_average      6.906909       NaN  10.795729       NaN  0.181874       NaN
       scenario_average_a_trace      gls_map               3.039921       NaN   5.267597       NaN  0.071948       NaN
                                     gsp                   3.638146       NaN   6.241724       NaN  0.087201       NaN
                                     historical_tod_mean   3.803153       NaN   6.773529       NaN  0.088770       NaN
                                     neighbor_average      7.000724       NaN  10.851226       NaN  0.185725       NaN
       scenario_cvar_a_trace         gls_map               3.046499       NaN   5.261033       NaN  0.074055       NaN
                                     gsp                   3.626709       NaN   6.187251       NaN  0.088155       NaN
                                     historical_tod_mean   3.779994       NaN   6.697057       NaN  0.088598       NaN
                                     neighbor_average      7.037183       NaN  11.125937       NaN  0.192320       NaN
       swap_from_best_random_trace   gls_map               3.004107       NaN   5.124701       NaN  0.072099       NaN
                                     gsp                   3.609310       NaN   6.202408       NaN  0.088210       NaN
                                     historical_tod_mean   3.834111       NaN   6.779315       NaN  0.090520       NaN
                                     neighbor_average      6.947249       NaN  10.973733       NaN  0.195074       NaN
       swap_from_greedy_a_trace      gls_map               3.045886       NaN   5.183429       NaN  0.073011       NaN
                                     gsp                   3.696635       NaN   6.285470       NaN  0.089362       NaN
                                     historical_tod_mean   3.908652       NaN   6.832244       NaN  0.091799       NaN
                                     neighbor_average      6.850710       NaN  10.843495       NaN  0.194911       NaN
       swap_from_scenario_average    gls_map               3.007820       NaN   5.143546       NaN  0.073016       NaN
                                     gsp                   3.672422       NaN   6.270450       NaN  0.088748       NaN
                                     historical_tod_mean   3.884114       NaN   6.816357       NaN  0.090914       NaN
                                     neighbor_average      6.837945       NaN  10.836588       NaN  0.191833       NaN
       swap_from_scenario_cvar       gls_map               3.024411       NaN   5.094426       NaN  0.074962       NaN
                                     gsp                   3.624417       NaN   6.181043       NaN  0.089225       NaN
                                     historical_tod_mean   3.815738       NaN   6.714101       NaN  0.090388       NaN
                                     neighbor_average      6.993208       NaN  10.989732       NaN  0.198297       NaN
       top_variance                  gls_map               2.890031       NaN   5.119386       NaN  0.064888       NaN
                                     gsp                   3.099940       NaN   5.504848       NaN  0.070969       NaN
                                     historical_tod_mean   3.308552       NaN   5.849745       NaN  0.074326       NaN
                                     neighbor_average      8.996992       NaN  14.234406       NaN  0.171446       NaN
       validation_swap_selected      gls_map               2.850774       NaN   5.027673       NaN  0.066267       NaN
                                     gsp                   3.451625       NaN   6.072576       NaN  0.082208       NaN
                                     historical_tod_mean   3.720041       NaN   6.639203       NaN  0.085903       NaN
                                     neighbor_average      6.929844       NaN  10.661065       NaN  0.166649       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 3.205678 5.505802
    0.2             top_variance gls_map 3.015254 5.380285
    0.3 validation_swap_selected gls_map 2.850774 5.027673
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.229790      0.249868 651
    gsp   condition_number     0.232785      0.247693 651
    gsp information_logdet    -0.232827     -0.263414 651
gls_map    posterior_trace     0.869363      0.852916 651
gls_map   condition_number     0.841362      0.863389 651
gls_map information_logdet    -0.835435     -0.817398 651
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv