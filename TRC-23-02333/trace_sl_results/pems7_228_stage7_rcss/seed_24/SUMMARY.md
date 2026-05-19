---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-14, 2012-06-13
Test days: 2012-05-03, 2012-05-07
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.519628       NaN   5.905641       NaN  0.082553       NaN
                                     gsp                  3.570923       NaN   6.165681       NaN  0.081812       NaN
                                     historical_tod_mean  3.978987       NaN   6.752063       NaN  0.084557       NaN
                                     neighbor_average     6.907801       NaN  10.811808       NaN  0.168475       NaN
       best_random_by_validation     gls_map              3.519628       NaN   5.905641       NaN  0.082553       NaN
                                     gsp                  3.570923       NaN   6.165681       NaN  0.081812       NaN
                                     historical_tod_mean  3.978987       NaN   6.752063       NaN  0.084557       NaN
                                     neighbor_average     6.907801       NaN  10.811808       NaN  0.168475       NaN
       coverage                      gls_map              3.555880       NaN   6.172894       NaN  0.081201       NaN
                                     gsp                  3.725183       NaN   6.439831       NaN  0.084095       NaN
                                     historical_tod_mean  4.055143       NaN   6.958300       NaN  0.086072       NaN
                                     neighbor_average     6.958924       NaN  10.845491       NaN  0.171074       NaN
       degree                        gls_map              3.754568       NaN   6.494497       NaN  0.080771       NaN
                                     gsp                  3.897852       NaN   6.740784       NaN  0.081940       NaN
                                     historical_tod_mean  4.051247       NaN   6.932850       NaN  0.083820       NaN
                                     neighbor_average     7.647089       NaN  11.973096       NaN  0.176858       NaN
       greedy_a_trace                gls_map              3.327478       NaN   5.723513       NaN  0.074308       NaN
                                     gsp                  3.733269       NaN   6.350744       NaN  0.081163       NaN
                                     historical_tod_mean  4.054458       NaN   6.874504       NaN  0.084255       NaN
                                     neighbor_average     6.705703       NaN  10.414775       NaN  0.162367       NaN
       greedy_d_logdet               gls_map              3.978347       NaN   6.429631       NaN  0.089625       NaN
                                     gsp                  3.828860       NaN   6.506335       NaN  0.084167       NaN
                                     historical_tod_mean  4.074370       NaN   6.968183       NaN  0.085597       NaN
                                     neighbor_average     7.181221       NaN  11.766166       NaN  0.191743       NaN
       multistart_swap_by_validation gls_map              3.310509       NaN   5.683847       NaN  0.074414       NaN
                                     gsp                  3.731078       NaN   6.346679       NaN  0.081240       NaN
                                     historical_tod_mean  4.055034       NaN   6.865120       NaN  0.084262       NaN
                                     neighbor_average     6.766649       NaN  10.443707       NaN  0.164863       NaN
       random                        gls_map              3.518933  0.072825   6.065833  0.119915  0.080121  0.002635
                                     gsp                  3.679913  0.053753   6.360346  0.090001  0.081577  0.001500
                                     historical_tod_mean  4.032194  0.039899   6.890608  0.071452  0.084803  0.001025
                                     neighbor_average     6.981458  0.234013  10.925010  0.356759  0.166252  0.005172
       rcss_selected                 gls_map              3.310509       NaN   5.683847       NaN  0.074414       NaN
                                     gsp                  3.731078       NaN   6.346679       NaN  0.081240       NaN
                                     historical_tod_mean  4.055034       NaN   6.865120       NaN  0.084262       NaN
                                     neighbor_average     6.766649       NaN  10.443707       NaN  0.164863       NaN
       robust_coverage_cvar          gls_map              3.408786       NaN   5.869405       NaN  0.078193       NaN
                                     gsp                  3.624886       NaN   6.280761       NaN  0.081828       NaN
                                     historical_tod_mean  4.028946       NaN   6.894992       NaN  0.085206       NaN
                                     neighbor_average     7.106866       NaN  11.010756       NaN  0.168543       NaN
       scenario_average_a_trace      gls_map              3.436608       NaN   5.952770       NaN  0.078502       NaN
                                     gsp                  3.662078       NaN   6.344990       NaN  0.081339       NaN
                                     historical_tod_mean  4.031361       NaN   6.887630       NaN  0.084567       NaN
                                     neighbor_average     7.016572       NaN  10.407524       NaN  0.162776       NaN
       scenario_cvar_a_trace         gls_map              3.448648       NaN   5.892663       NaN  0.077475       NaN
                                     gsp                  3.671663       NaN   6.314983       NaN  0.081000       NaN
                                     historical_tod_mean  4.013008       NaN   6.854389       NaN  0.084185       NaN
                                     neighbor_average     7.061577       NaN  10.983461       NaN  0.171374       NaN
       swap_from_best_random_trace   gls_map              3.334660       NaN   5.835825       NaN  0.074047       NaN
                                     gsp                  3.770614       NaN   6.451792       NaN  0.081455       NaN
                                     historical_tod_mean  4.073892       NaN   6.928843       NaN  0.084500       NaN
                                     neighbor_average     6.539062       NaN  10.364545       NaN  0.163703       NaN
       swap_from_greedy_a_trace      gls_map              3.318620       NaN   5.676874       NaN  0.073862       NaN
                                     gsp                  3.757590       NaN   6.378103       NaN  0.081559       NaN
                                     historical_tod_mean  4.055279       NaN   6.862798       NaN  0.084150       NaN
                                     neighbor_average     6.717933       NaN  10.424900       NaN  0.164200       NaN
       swap_from_scenario_average    gls_map              3.367313       NaN   5.718022       NaN  0.076508       NaN
                                     gsp                  3.763712       NaN   6.375585       NaN  0.081974       NaN
                                     historical_tod_mean  4.045808       NaN   6.851739       NaN  0.083880       NaN
                                     neighbor_average     6.749432       NaN  10.477972       NaN  0.165429       NaN
       swap_from_scenario_cvar       gls_map              3.334660       NaN   5.835825       NaN  0.074047       NaN
                                     gsp                  3.770614       NaN   6.451792       NaN  0.081455       NaN
                                     historical_tod_mean  4.073892       NaN   6.928843       NaN  0.084500       NaN
                                     neighbor_average     6.539062       NaN  10.364545       NaN  0.163703       NaN
       top_variance                  gls_map              3.346310       NaN   5.681493       NaN  0.074107       NaN
                                     gsp                  3.388689       NaN   5.823878       NaN  0.075308       NaN
                                     historical_tod_mean  3.770668       NaN   6.321245       NaN  0.078916       NaN
                                     neighbor_average     9.817996       NaN  15.242815       NaN  0.187812       NaN
0.2    best_random_by_trace          gls_map              3.278961       NaN   5.775069       NaN  0.072158       NaN
                                     gsp                  3.670285       NaN   6.291807       NaN  0.078432       NaN
                                     historical_tod_mean  4.043992       NaN   6.896831       NaN  0.082801       NaN
                                     neighbor_average     6.508298       NaN  10.389951       NaN  0.160588       NaN
       best_random_by_validation     gls_map              3.154080       NaN   5.584392       NaN  0.072145       NaN
                                     gsp                  3.550029       NaN   6.149424       NaN  0.079814       NaN
                                     historical_tod_mean  3.926126       NaN   6.753317       NaN  0.082694       NaN
                                     neighbor_average     6.688034       NaN  10.425749       NaN  0.154588       NaN
       coverage                      gls_map              3.320083       NaN   5.880557       NaN  0.075034       NaN
                                     gsp                  3.658573       NaN   6.386733       NaN  0.082238       NaN
                                     historical_tod_mean  4.043562       NaN   7.001362       NaN  0.085972       NaN
                                     neighbor_average     6.633894       NaN  10.349405       NaN  0.161454       NaN
       degree                        gls_map              3.625712       NaN   6.139710       NaN  0.079044       NaN
                                     gsp                  3.755994       NaN   6.351800       NaN  0.078448       NaN
                                     historical_tod_mean  4.052359       NaN   6.809500       NaN  0.082247       NaN
                                     neighbor_average     7.136321       NaN  11.355729       NaN  0.170014       NaN
       greedy_a_trace                gls_map              3.186229       NaN   5.561580       NaN  0.072732       NaN
                                     gsp                  3.758432       NaN   6.427878       NaN  0.082899       NaN
                                     historical_tod_mean  4.143624       NaN   7.031955       NaN  0.086325       NaN
                                     neighbor_average     6.637890       NaN  10.482701       NaN  0.170658       NaN
       greedy_d_logdet               gls_map              3.760596       NaN   6.230473       NaN  0.081706       NaN
                                     gsp                  3.810502       NaN   6.522556       NaN  0.082267       NaN
                                     historical_tod_mean  4.137698       NaN   7.046533       NaN  0.085763       NaN
                                     neighbor_average     7.099751       NaN  11.446602       NaN  0.187930       NaN
       multistart_swap_by_validation gls_map              3.132645       NaN   5.448963       NaN  0.072159       NaN
                                     gsp                  3.649382       NaN   6.261981       NaN  0.082699       NaN
                                     historical_tod_mean  4.044346       NaN   6.899252       NaN  0.085467       NaN
                                     neighbor_average     6.514541       NaN  10.351741       NaN  0.165901       NaN
       random                        gls_map              3.298779  0.079092   5.758740  0.164562  0.074946  0.002552
                                     gsp                  3.635049  0.066695   6.279125  0.127687  0.081362  0.002120
                                     historical_tod_mean  4.036408  0.070168   6.893495  0.129497  0.084896  0.001855
                                     neighbor_average     6.782880  0.160771  10.706544  0.271699  0.162321  0.005272
       rcss_selected                 gls_map              3.132645       NaN   5.448963       NaN  0.072159       NaN
                                     gsp                  3.649382       NaN   6.261981       NaN  0.082699       NaN
                                     historical_tod_mean  4.044346       NaN   6.899252       NaN  0.085467       NaN
                                     neighbor_average     6.514541       NaN  10.351741       NaN  0.165901       NaN
       robust_coverage_cvar          gls_map              3.166203       NaN   5.496227       NaN  0.072081       NaN
                                     gsp                  3.640816       NaN   6.292491       NaN  0.081900       NaN
                                     historical_tod_mean  4.029598       NaN   6.921620       NaN  0.085337       NaN
                                     neighbor_average     6.740549       NaN  10.489964       NaN  0.164577       NaN
       scenario_average_a_trace      gls_map              3.175690       NaN   5.513911       NaN  0.073049       NaN
                                     gsp                  3.632191       NaN   6.311709       NaN  0.081418       NaN
                                     historical_tod_mean  4.023946       NaN   6.931861       NaN  0.085003       NaN
                                     neighbor_average     6.595171       NaN  10.002796       NaN  0.159795       NaN
       scenario_cvar_a_trace         gls_map              3.215912       NaN   5.531218       NaN  0.072928       NaN
                                     gsp                  3.639456       NaN   6.269371       NaN  0.082105       NaN
                                     historical_tod_mean  3.992919       NaN   6.890662       NaN  0.084621       NaN
                                     neighbor_average     6.908012       NaN  10.882346       NaN  0.170274       NaN
       swap_from_best_random_trace   gls_map              3.164912       NaN   5.439272       NaN  0.070198       NaN
                                     gsp                  3.661861       NaN   6.257123       NaN  0.079066       NaN
                                     historical_tod_mean  4.051161       NaN   6.850902       NaN  0.083215       NaN
                                     neighbor_average     6.548606       NaN  10.419056       NaN  0.167290       NaN
       swap_from_greedy_a_trace      gls_map              3.161370       NaN   5.473194       NaN  0.070608       NaN
                                     gsp                  3.739509       NaN   6.386595       NaN  0.081245       NaN
                                     historical_tod_mean  4.127729       NaN   6.992548       NaN  0.085026       NaN
                                     neighbor_average     6.566993       NaN  10.510085       NaN  0.168721       NaN
       swap_from_scenario_average    gls_map              3.177332       NaN   5.489757       NaN  0.072812       NaN
                                     gsp                  3.752013       NaN   6.387545       NaN  0.082693       NaN
                                     historical_tod_mean  4.132194       NaN   7.006113       NaN  0.085951       NaN
                                     neighbor_average     6.516646       NaN  10.369818       NaN  0.167845       NaN
       swap_from_scenario_cvar       gls_map              3.190566       NaN   5.505093       NaN  0.070267       NaN
                                     gsp                  3.744335       NaN   6.387830       NaN  0.081084       NaN
                                     historical_tod_mean  4.121546       NaN   6.979633       NaN  0.085036       NaN
                                     neighbor_average     6.449705       NaN  10.416616       NaN  0.167275       NaN
       top_variance                  gls_map              3.044578       NaN   5.330119       NaN  0.067958       NaN
                                     gsp                  3.229068       NaN   5.579453       NaN  0.071446       NaN
                                     historical_tod_mean  3.606451       NaN   6.059092       NaN  0.075535       NaN
                                     neighbor_average     8.594588       NaN  13.712685       NaN  0.160248       NaN
0.3    best_random_by_trace          gls_map              3.266762       NaN   5.785190       NaN  0.071823       NaN
                                     gsp                  3.753110       NaN   6.485351       NaN  0.082540       NaN
                                     historical_tod_mean  4.163053       NaN   7.164104       NaN  0.086787       NaN
                                     neighbor_average     6.490022       NaN  10.409475       NaN  0.163862       NaN
       best_random_by_validation     gls_map              3.024750       NaN   5.280656       NaN  0.069907       NaN
                                     gsp                  3.507482       NaN   6.049055       NaN  0.080097       NaN
                                     historical_tod_mean  3.886231       NaN   6.670798       NaN  0.082499       NaN
                                     neighbor_average     6.674274       NaN  10.179769       NaN  0.153606       NaN
       coverage                      gls_map              3.158002       NaN   5.677453       NaN  0.072167       NaN
                                     gsp                  3.585054       NaN   6.317944       NaN  0.082202       NaN
                                     historical_tod_mean  3.962124       NaN   6.963512       NaN  0.084981       NaN
                                     neighbor_average     6.626463       NaN  10.170049       NaN  0.157755       NaN
       degree                        gls_map              3.524280       NaN   5.972035       NaN  0.077324       NaN
                                     gsp                  3.688251       NaN   6.215613       NaN  0.077126       NaN
                                     historical_tod_mean  4.039770       NaN   6.783943       NaN  0.081433       NaN
                                     neighbor_average     7.404026       NaN  11.647211       NaN  0.179467       NaN
       greedy_a_trace                gls_map              3.106055       NaN   5.408112       NaN  0.070778       NaN
                                     gsp                  3.723240       NaN   6.392019       NaN  0.082921       NaN
                                     historical_tod_mean  4.154953       NaN   7.063110       NaN  0.086751       NaN
                                     neighbor_average     6.535998       NaN  10.358971       NaN  0.171409       NaN
       greedy_d_logdet               gls_map              3.467228       NaN   5.858695       NaN  0.077781       NaN
                                     gsp                  3.663348       NaN   6.308957       NaN  0.080393       NaN
                                     historical_tod_mean  4.034135       NaN   6.953812       NaN  0.083959       NaN
                                     neighbor_average     7.218602       NaN  11.514184       NaN  0.191587       NaN
       multistart_swap_by_validation gls_map              3.097593       NaN   5.357347       NaN  0.068494       NaN
                                     gsp                  3.651639       NaN   6.259074       NaN  0.078316       NaN
                                     historical_tod_mean  4.041058       NaN   6.910819       NaN  0.082412       NaN
                                     neighbor_average     6.565286       NaN  10.287747       NaN  0.161465       NaN
       random                        gls_map              3.163845  0.091430   5.566013  0.195000  0.071557  0.002902
                                     gsp                  3.611837  0.078750   6.249019  0.142963  0.081070  0.002792
                                     historical_tod_mean  4.029212  0.087484   6.897133  0.151872  0.084657  0.002423
                                     neighbor_average     6.682648  0.171142  10.581065  0.329816  0.158053  0.006242
       rcss_selected                 gls_map              3.025311       NaN   5.307581       NaN  0.069623       NaN
                                     gsp                  3.609373       NaN   6.303818       NaN  0.082222       NaN
                                     historical_tod_mean  4.032896       NaN   6.987286       NaN  0.085985       NaN
                                     neighbor_average     6.678743       NaN  10.423982       NaN  0.166108       NaN
       robust_coverage_cvar          gls_map              3.025311       NaN   5.307581       NaN  0.069623       NaN
                                     gsp                  3.609373       NaN   6.303818       NaN  0.082222       NaN
                                     historical_tod_mean  4.032896       NaN   6.987286       NaN  0.085985       NaN
                                     neighbor_average     6.678743       NaN  10.423982       NaN  0.166108       NaN
       scenario_average_a_trace      gls_map              3.089309       NaN   5.315444       NaN  0.072576       NaN
                                     gsp                  3.597506       NaN   6.234638       NaN  0.082779       NaN
                                     historical_tod_mean  3.997559       NaN   6.892736       NaN  0.085617       NaN
                                     neighbor_average     6.467507       NaN  10.002674       NaN  0.160772       NaN
       scenario_cvar_a_trace         gls_map              3.066729       NaN   5.317862       NaN  0.070703       NaN
                                     gsp                  3.584604       NaN   6.209018       NaN  0.082217       NaN
                                     historical_tod_mean  3.954615       NaN   6.882503       NaN  0.084543       NaN
                                     neighbor_average     6.736216       NaN  10.510736       NaN  0.166517       NaN
       swap_from_best_random_trace   gls_map              3.096317       NaN   5.379200       NaN  0.069257       NaN
                                     gsp                  3.695210       NaN   6.355912       NaN  0.080375       NaN
                                     historical_tod_mean  4.081859       NaN   6.989719       NaN  0.084083       NaN
                                     neighbor_average     6.559176       NaN  10.420132       NaN  0.165537       NaN
       swap_from_greedy_a_trace      gls_map              3.134008       NaN   5.394261       NaN  0.070879       NaN
                                     gsp                  3.708787       NaN   6.364761       NaN  0.082488       NaN
                                     historical_tod_mean  4.133480       NaN   7.036763       NaN  0.086298       NaN
                                     neighbor_average     6.489202       NaN  10.377939       NaN  0.172017       NaN
       swap_from_scenario_average    gls_map              3.050628       NaN   5.309187       NaN  0.069033       NaN
                                     gsp                  3.661430       NaN   6.330077       NaN  0.080796       NaN
                                     historical_tod_mean  4.088217       NaN   6.997367       NaN  0.084774       NaN
                                     neighbor_average     6.528109       NaN  10.393430       NaN  0.166346       NaN
       swap_from_scenario_cvar       gls_map              3.034349       NaN   5.252839       NaN  0.068008       NaN
                                     gsp                  3.653363       NaN   6.258833       NaN  0.080250       NaN
                                     historical_tod_mean  4.060403       NaN   6.934592       NaN  0.084045       NaN
                                     neighbor_average     6.490709       NaN  10.197414       NaN  0.165256       NaN
       top_variance                  gls_map              2.859445       NaN   5.042031       NaN  0.063143       NaN
                                     gsp                  3.070090       NaN   5.341065       NaN  0.067956       NaN
                                     historical_tod_mean  3.406037       NaN   5.700017       NaN  0.071675       NaN
                                     neighbor_average     8.033611       NaN  12.784727       NaN  0.150097       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1 multistart_swap_by_validation gls_map 3.310509 5.683847
    0.2                  top_variance gls_map 3.044578 5.330119
    0.3                  top_variance gls_map 2.859445 5.042031
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.362063      0.355652 648
    gsp   condition_number     0.363964      0.347654 648
    gsp information_logdet    -0.367252     -0.385053 648
gls_map    posterior_trace     0.854709      0.847137 648
gls_map   condition_number     0.811175      0.843754 648
gls_map information_logdet    -0.824928     -0.808906 648
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv