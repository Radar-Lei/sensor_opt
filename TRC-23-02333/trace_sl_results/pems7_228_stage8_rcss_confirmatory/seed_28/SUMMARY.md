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
0.2    best_random_by_trace          gls_map               3.266825       NaN   5.730930       NaN  0.079613       NaN
                                     gsp                   3.628772       NaN   6.342022       NaN  0.088574       NaN
                                     historical_tod_mean   3.878061       NaN   6.858790       NaN  0.090849       NaN
                                     neighbor_average      6.855741       NaN  10.994538       NaN  0.186923       NaN
       best_random_by_validation     gls_map               3.070085       NaN   5.339692       NaN  0.071376       NaN
                                     gsp                   3.552530       NaN   6.101671       NaN  0.083605       NaN
                                     historical_tod_mean   3.728797       NaN   6.598145       NaN  0.086163       NaN
                                     neighbor_average      7.090051       NaN  10.991738       NaN  0.174995       NaN
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
       multistart_swap_by_validation gls_map               3.071592       NaN   5.244224       NaN  0.071758       NaN
                                     gsp                   3.633837       NaN   6.154207       NaN  0.086808       NaN
                                     historical_tod_mean   3.819077       NaN   6.660651       NaN  0.089070       NaN
                                     neighbor_average      6.829760       NaN  10.730791       NaN  0.185600       NaN
       random                        gls_map               3.232663  0.072212   5.626786  0.132948  0.076562  0.002184
                                     gsp                   3.636909  0.063836   6.281672  0.098381  0.087155  0.001959
                                     historical_tod_mean   3.855609  0.058596   6.783069  0.096634  0.090155  0.001759
                                     neighbor_average      7.159788  0.164448  11.288977  0.278802  0.183063  0.007021
       rcss_selected                 gls_map               3.137363       NaN   5.359891       NaN  0.076313       NaN
                                     gsp                   3.638064       NaN   6.265831       NaN  0.088769       NaN
                                     historical_tod_mean   3.866261       NaN   6.755598       NaN  0.091341       NaN
                                     neighbor_average      6.982295       NaN  11.087731       NaN  0.195234       NaN
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
       swap_from_best_random_trace   gls_map               3.137363       NaN   5.359891       NaN  0.076313       NaN
                                     gsp                   3.638064       NaN   6.265831       NaN  0.088769       NaN
                                     historical_tod_mean   3.866261       NaN   6.755598       NaN  0.091341       NaN
                                     neighbor_average      6.982295       NaN  11.087731       NaN  0.195234       NaN
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
0.3    best_random_by_trace          gls_map               3.161359       NaN   5.573854       NaN  0.074275       NaN
                                     gsp                   3.772038       NaN   6.473118       NaN  0.090354       NaN
                                     historical_tod_mean   3.980332       NaN   7.024104       NaN  0.093922       NaN
                                     neighbor_average      6.851510       NaN  10.938315       NaN  0.187753       NaN
       best_random_by_validation     gls_map               2.954024       NaN   5.283983       NaN  0.071190       NaN
                                     gsp                   3.526449       NaN   6.198134       NaN  0.085344       NaN
                                     historical_tod_mean   3.763348       NaN   6.735704       NaN  0.088004       NaN
                                     neighbor_average      7.151406       NaN  10.895146       NaN  0.170278       NaN
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
       multistart_swap_by_validation gls_map               2.952752       NaN   5.090286       NaN  0.071685       NaN
                                     gsp                   3.594575       NaN   6.188889       NaN  0.086828       NaN
                                     historical_tod_mean   3.793573       NaN   6.718231       NaN  0.089098       NaN
                                     neighbor_average      6.907139       NaN  10.811724       NaN  0.185286       NaN
       random                        gls_map               3.090843  0.083088   5.402497  0.163544  0.072745  0.002625
                                     gsp                   3.616865  0.078501   6.248085  0.118550  0.086705  0.002664
                                     historical_tod_mean   3.847169  0.077100   6.781336  0.122628  0.089852  0.002440
                                     neighbor_average      7.050404  0.179730  11.151302  0.335603  0.177897  0.008082
       rcss_selected                 gls_map               2.954024       NaN   5.283983       NaN  0.071190       NaN
                                     gsp                   3.526449       NaN   6.198134       NaN  0.085344       NaN
                                     historical_tod_mean   3.763348       NaN   6.735704       NaN  0.088004       NaN
                                     neighbor_average      7.151406       NaN  10.895146       NaN  0.170278       NaN
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
       swap_from_best_random_trace   gls_map               2.963020       NaN   5.140825       NaN  0.072392       NaN
                                     gsp                   3.627996       NaN   6.294740       NaN  0.089068       NaN
                                     historical_tod_mean   3.878063       NaN   6.854307       NaN  0.092147       NaN
                                     neighbor_average      6.836581       NaN  10.850421       NaN  0.189647       NaN
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
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 3.252684 5.613618
    0.2             top_variance gls_map 3.015254 5.380285
    0.3             top_variance gls_map 2.890031 5.119386
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.225700      0.235405 648
    gsp   condition_number     0.227824      0.221408 648
    gsp information_logdet    -0.239529     -0.249837 648
gls_map    posterior_trace     0.870187      0.866461 648
gls_map   condition_number     0.836250      0.867182 648
gls_map information_logdet    -0.837066     -0.824135 648
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv