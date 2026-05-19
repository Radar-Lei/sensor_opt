---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-28, 2012-06-01
Test days: 2012-05-16, 2012-06-12
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.467682       NaN   5.986621       NaN  0.085285       NaN
                                     gsp                   3.670843       NaN   6.437119       NaN  0.094012       NaN
                                     historical_tod_mean   3.627392       NaN   6.486976       NaN  0.094972       NaN
                                     neighbor_average      7.789423       NaN  11.860303       NaN  0.195569       NaN
       best_random_by_validation     gls_map               3.467682       NaN   5.986621       NaN  0.085285       NaN
                                     gsp                   3.670843       NaN   6.437119       NaN  0.094012       NaN
                                     historical_tod_mean   3.627392       NaN   6.486976       NaN  0.094972       NaN
                                     neighbor_average      7.789423       NaN  11.860303       NaN  0.195569       NaN
       coverage                      gls_map               3.794073       NaN   6.414597       NaN  0.099899       NaN
                                     gsp                   3.764725       NaN   6.554338       NaN  0.100375       NaN
                                     historical_tod_mean   3.668583       NaN   6.559577       NaN  0.098901       NaN
                                     neighbor_average      8.119145       NaN  12.345702       NaN  0.228397       NaN
       degree                        gls_map               4.129135       NaN   7.001249       NaN  0.113789       NaN
                                     gsp                   3.867487       NaN   6.632783       NaN  0.105363       NaN
                                     historical_tod_mean   3.677833       NaN   6.562486       NaN  0.100045       NaN
                                     neighbor_average      8.680494       NaN  13.247710       NaN  0.247102       NaN
       greedy_a_trace                gls_map               3.497389       NaN   6.156952       NaN  0.092360       NaN
                                     gsp                   3.718676       NaN   6.501453       NaN  0.098512       NaN
                                     historical_tod_mean   3.672091       NaN   6.513687       NaN  0.097191       NaN
                                     neighbor_average      7.639352       NaN  11.844720       NaN  0.222435       NaN
       greedy_d_logdet               gls_map               4.312828       NaN   6.797901       NaN  0.113607       NaN
                                     gsp                   3.744506       NaN   6.381280       NaN  0.099778       NaN
                                     historical_tod_mean   3.607926       NaN   6.372650       NaN  0.097134       NaN
                                     neighbor_average      8.320606       NaN  13.495104       NaN  0.264764       NaN
       multistart_swap_by_validation gls_map               3.411490       NaN   5.887082       NaN  0.088338       NaN
                                     gsp                   3.668580       NaN   6.438549       NaN  0.097243       NaN
                                     historical_tod_mean   3.645974       NaN   6.456068       NaN  0.096363       NaN
                                     neighbor_average      7.685940       NaN  11.878067       NaN  0.216483       NaN
       random                        gls_map               3.658188  0.078069   6.373390  0.134895  0.096774  0.003905
                                     gsp                   3.687189  0.049881   6.505268  0.066201  0.099015  0.002404
                                     historical_tod_mean   3.649587  0.037043   6.517214  0.063745  0.097614  0.001621
                                     neighbor_average      7.910603  0.287697  12.106361  0.413400  0.214767  0.010819
       rcss_selected                 gls_map               3.411490       NaN   5.887082       NaN  0.088338       NaN
                                     gsp                   3.668580       NaN   6.438549       NaN  0.097243       NaN
                                     historical_tod_mean   3.645974       NaN   6.456068       NaN  0.096363       NaN
                                     neighbor_average      7.685940       NaN  11.878067       NaN  0.216483       NaN
       robust_coverage_cvar          gls_map               3.567662       NaN   6.328575       NaN  0.099657       NaN
                                     gsp                   3.595104       NaN   6.429337       NaN  0.098960       NaN
                                     historical_tod_mean   3.618489       NaN   6.474440       NaN  0.098198       NaN
                                     neighbor_average      7.940416       NaN  11.988709       NaN  0.225531       NaN
       scenario_average_a_trace      gls_map               3.580038       NaN   6.261748       NaN  0.094622       NaN
                                     gsp                   3.764342       NaN   6.517818       NaN  0.099180       NaN
                                     historical_tod_mean   3.667433       NaN   6.524613       NaN  0.097929       NaN
                                     neighbor_average      7.574074       NaN  11.607324       NaN  0.212586       NaN
       scenario_cvar_a_trace         gls_map               3.513849       NaN   6.125606       NaN  0.091457       NaN
                                     gsp                   3.648814       NaN   6.409116       NaN  0.096126       NaN
                                     historical_tod_mean   3.626881       NaN   6.463990       NaN  0.097126       NaN
                                     neighbor_average      7.810712       NaN  11.613851       NaN  0.214966       NaN
       swap_from_best_random_trace   gls_map               3.411490       NaN   5.887082       NaN  0.088338       NaN
                                     gsp                   3.668580       NaN   6.438549       NaN  0.097243       NaN
                                     historical_tod_mean   3.645974       NaN   6.456068       NaN  0.096363       NaN
                                     neighbor_average      7.685940       NaN  11.878067       NaN  0.216483       NaN
       swap_from_greedy_a_trace      gls_map               3.459893       NaN   6.064229       NaN  0.094581       NaN
                                     gsp                   3.710777       NaN   6.505417       NaN  0.100606       NaN
                                     historical_tod_mean   3.670478       NaN   6.526205       NaN  0.098902       NaN
                                     neighbor_average      7.700207       NaN  12.008909       NaN  0.227606       NaN
       swap_from_scenario_average    gls_map               3.438599       NaN   6.048302       NaN  0.093896       NaN
                                     gsp                   3.680755       NaN   6.488359       NaN  0.100139       NaN
                                     historical_tod_mean   3.669258       NaN   6.517424       NaN  0.098520       NaN
                                     neighbor_average      7.612097       NaN  11.858494       NaN  0.225877       NaN
       swap_from_scenario_cvar       gls_map               3.357446       NaN   5.844062       NaN  0.088391       NaN
                                     gsp                   3.634672       NaN   6.402122       NaN  0.096986       NaN
                                     historical_tod_mean   3.625234       NaN   6.418626       NaN  0.095929       NaN
                                     neighbor_average      7.783204       NaN  11.935370       NaN  0.217416       NaN
       top_variance                  gls_map               3.504969       NaN   6.018650       NaN  0.082904       NaN
                                     gsp                   3.488406       NaN   6.147729       NaN  0.084886       NaN
                                     historical_tod_mean   3.435596       NaN   6.131453       NaN  0.085540       NaN
                                     neighbor_average     12.021153       NaN  18.264936       NaN  0.231730       NaN
0.2    best_random_by_trace          gls_map               3.509130       NaN   6.164045       NaN  0.095843       NaN
                                     gsp                   3.710791       NaN   6.468767       NaN  0.101528       NaN
                                     historical_tod_mean   3.636533       NaN   6.485070       NaN  0.098721       NaN
                                     neighbor_average      7.694027       NaN  12.062436       NaN  0.231481       NaN
       best_random_by_validation     gls_map               3.325748       NaN   5.891860       NaN  0.086348       NaN
                                     gsp                   3.631454       NaN   6.440087       NaN  0.097157       NaN
                                     historical_tod_mean   3.630638       NaN   6.501688       NaN  0.097083       NaN
                                     neighbor_average      7.761151       NaN  12.046822       NaN  0.203900       NaN
       coverage                      gls_map               3.488185       NaN   6.019266       NaN  0.093178       NaN
                                     gsp                   3.731243       NaN   6.549897       NaN  0.102053       NaN
                                     historical_tod_mean   3.672806       NaN   6.589737       NaN  0.100692       NaN
                                     neighbor_average      7.463653       NaN  11.411583       NaN  0.210047       NaN
       degree                        gls_map               4.013840       NaN   6.864790       NaN  0.109613       NaN
                                     gsp                   3.910046       NaN   6.795327       NaN  0.109328       NaN
                                     historical_tod_mean   3.756424       NaN   6.665887       NaN  0.102065       NaN
                                     neighbor_average      8.227975       NaN  12.512998       NaN  0.224743       NaN
       greedy_a_trace                gls_map               3.290958       NaN   5.713577       NaN  0.086106       NaN
                                     gsp                   3.721981       NaN   6.495480       NaN  0.100239       NaN
                                     historical_tod_mean   3.687277       NaN   6.521286       NaN  0.098663       NaN
                                     neighbor_average      7.544113       NaN  11.680839       NaN  0.224666       NaN
       greedy_d_logdet               gls_map               4.020446       NaN   6.501299       NaN  0.111299       NaN
                                     gsp                   3.753522       NaN   6.462312       NaN  0.104339       NaN
                                     historical_tod_mean   3.636377       NaN   6.440203       NaN  0.100119       NaN
                                     neighbor_average      8.292285       NaN  13.346503       NaN  0.270537       NaN
       multistart_swap_by_validation gls_map               3.247229       NaN   5.615468       NaN  0.087492       NaN
                                     gsp                   3.663039       NaN   6.450316       NaN  0.100109       NaN
                                     historical_tod_mean   3.612664       NaN   6.466677       NaN  0.098415       NaN
                                     neighbor_average      7.333847       NaN  11.364481       NaN  0.213111       NaN
       random                        gls_map               3.431527  0.084884   6.008433  0.180444  0.089982  0.004173
                                     gsp                   3.670854  0.062575   6.486514  0.108055  0.098684  0.003205
                                     historical_tod_mean   3.656360  0.062007   6.524012  0.105511  0.097862  0.002644
                                     neighbor_average      7.642239  0.188610  11.809195  0.311429  0.207022  0.010358
       rcss_selected                 gls_map               3.266726       NaN   5.489707       NaN  0.083624       NaN
                                     gsp                   3.609893       NaN   6.234084       NaN  0.095221       NaN
                                     historical_tod_mean   3.583206       NaN   6.299670       NaN  0.095111       NaN
                                     neighbor_average      7.463882       NaN  11.546228       NaN  0.215215       NaN
       robust_coverage_cvar          gls_map               3.302993       NaN   5.655124       NaN  0.086586       NaN
                                     gsp                   3.639417       NaN   6.396536       NaN  0.098094       NaN
                                     historical_tod_mean   3.576643       NaN   6.434099       NaN  0.097314       NaN
                                     neighbor_average      7.531555       NaN  11.517469       NaN  0.211812       NaN
       scenario_average_a_trace      gls_map               3.402379       NaN   5.944685       NaN  0.089608       NaN
                                     gsp                   3.746692       NaN   6.482193       NaN  0.099919       NaN
                                     historical_tod_mean   3.671027       NaN   6.517460       NaN  0.098773       NaN
                                     neighbor_average      7.587803       NaN  11.579289       NaN  0.219353       NaN
       scenario_cvar_a_trace         gls_map               3.298398       NaN   5.699540       NaN  0.086946       NaN
                                     gsp                   3.685827       NaN   6.453600       NaN  0.099518       NaN
                                     historical_tod_mean   3.638625       NaN   6.508353       NaN  0.099156       NaN
                                     neighbor_average      7.387043       NaN  11.322502       NaN  0.213365       NaN
       swap_from_best_random_trace   gls_map               3.266726       NaN   5.489707       NaN  0.083624       NaN
                                     gsp                   3.609893       NaN   6.234084       NaN  0.095221       NaN
                                     historical_tod_mean   3.583206       NaN   6.299670       NaN  0.095111       NaN
                                     neighbor_average      7.463882       NaN  11.546228       NaN  0.215215       NaN
       swap_from_greedy_a_trace      gls_map               3.302576       NaN   5.619917       NaN  0.086698       NaN
                                     gsp                   3.699303       NaN   6.416685       NaN  0.099506       NaN
                                     historical_tod_mean   3.649076       NaN   6.441845       NaN  0.098150       NaN
                                     neighbor_average      7.475976       NaN  11.722581       NaN  0.220957       NaN
       swap_from_scenario_average    gls_map               3.314994       NaN   5.666522       NaN  0.086021       NaN
                                     gsp                   3.702822       NaN   6.442205       NaN  0.099465       NaN
                                     historical_tod_mean   3.663373       NaN   6.474935       NaN  0.098065       NaN
                                     neighbor_average      7.544181       NaN  11.860455       NaN  0.222915       NaN
       swap_from_scenario_cvar       gls_map               3.337268       NaN   5.675383       NaN  0.087778       NaN
                                     gsp                   3.723933       NaN   6.480338       NaN  0.100706       NaN
                                     historical_tod_mean   3.658309       NaN   6.487302       NaN  0.099199       NaN
                                     neighbor_average      7.508782       NaN  11.764316       NaN  0.221931       NaN
       top_variance                  gls_map               3.222778       NaN   5.744870       NaN  0.076553       NaN
                                     gsp                   3.329831       NaN   5.949920       NaN  0.080250       NaN
                                     historical_tod_mean   3.304167       NaN   5.963864       NaN  0.080670       NaN
                                     neighbor_average     10.365048       NaN  16.098801       NaN  0.196916       NaN
0.3    best_random_by_trace          gls_map               3.346084       NaN   5.824610       NaN  0.091905       NaN
                                     gsp                   3.696867       NaN   6.519385       NaN  0.104158       NaN
                                     historical_tod_mean   3.722398       NaN   6.571897       NaN  0.103276       NaN
                                     neighbor_average      7.325417       NaN  11.528120       NaN  0.224608       NaN
       best_random_by_validation     gls_map               3.101024       NaN   5.494531       NaN  0.078111       NaN
                                     gsp                   3.555062       NaN   6.379859       NaN  0.093215       NaN
                                     historical_tod_mean   3.545040       NaN   6.441409       NaN  0.093616       NaN
                                     neighbor_average      7.708330       NaN  11.533220       NaN  0.190221       NaN
       coverage                      gls_map               3.209285       NaN   5.717023       NaN  0.087150       NaN
                                     gsp                   3.627900       NaN   6.534372       NaN  0.101340       NaN
                                     historical_tod_mean   3.624308       NaN   6.597324       NaN  0.100910       NaN
                                     neighbor_average      7.376397       NaN  11.091865       NaN  0.204519       NaN
       degree                        gls_map               3.873460       NaN   6.802313       NaN  0.107500       NaN
                                     gsp                   3.836524       NaN   6.776813       NaN  0.108224       NaN
                                     historical_tod_mean   3.771243       NaN   6.743182       NaN  0.103874       NaN
                                     neighbor_average      8.688428       NaN  13.441681       NaN  0.253763       NaN
       greedy_a_trace                gls_map               3.183851       NaN   5.397634       NaN  0.085245       NaN
                                     gsp                   3.685984       NaN   6.388179       NaN  0.101084       NaN
                                     historical_tod_mean   3.657037       NaN   6.425021       NaN  0.099114       NaN
                                     neighbor_average      7.302326       NaN  11.268032       NaN  0.220826       NaN
       greedy_d_logdet               gls_map               3.749847       NaN   6.128317       NaN  0.103714       NaN
                                     gsp                   3.631950       NaN   6.364205       NaN  0.103171       NaN
                                     historical_tod_mean   3.556069       NaN   6.379597       NaN  0.100486       NaN
                                     neighbor_average      8.236951       NaN  12.949166       NaN  0.268080       NaN
       multistart_swap_by_validation gls_map               3.008224       NaN   5.210543       NaN  0.079042       NaN
                                     gsp                   3.529663       NaN   6.248699       NaN  0.096405       NaN
                                     historical_tod_mean   3.508884       NaN   6.295542       NaN  0.095422       NaN
                                     neighbor_average      7.236606       NaN  11.177351       NaN  0.207926       NaN
       random                        gls_map               3.291501  0.093513   5.777713  0.204083  0.085902  0.004649
                                     gsp                   3.653816  0.075197   6.479918  0.128898  0.098540  0.003784
                                     historical_tod_mean   3.648974  0.075329   6.524364  0.123434  0.097827  0.003240
                                     neighbor_average      7.514753  0.207425  11.671806  0.378329  0.201077  0.011274
       rcss_selected                 gls_map               3.008224       NaN   5.210543       NaN  0.079042       NaN
                                     gsp                   3.529663       NaN   6.248699       NaN  0.096405       NaN
                                     historical_tod_mean   3.508884       NaN   6.295542       NaN  0.095422       NaN
                                     neighbor_average      7.236606       NaN  11.177351       NaN  0.207926       NaN
       robust_coverage_cvar          gls_map               3.179822       NaN   5.395858       NaN  0.084307       NaN
                                     gsp                   3.621159       NaN   6.384542       NaN  0.100093       NaN
                                     historical_tod_mean   3.559887       NaN   6.426027       NaN  0.098880       NaN
                                     neighbor_average      7.452010       NaN  11.558974       NaN  0.211692       NaN
       scenario_average_a_trace      gls_map               3.176529       NaN   5.513034       NaN  0.085359       NaN
                                     gsp                   3.667904       NaN   6.416684       NaN  0.100878       NaN
                                     historical_tod_mean   3.637745       NaN   6.470710       NaN  0.099406       NaN
                                     neighbor_average      7.176332       NaN  10.949226       NaN  0.211199       NaN
       scenario_cvar_a_trace         gls_map               3.160542       NaN   5.416820       NaN  0.083223       NaN
                                     gsp                   3.655451       NaN   6.372387       NaN  0.099861       NaN
                                     historical_tod_mean   3.565985       NaN   6.404898       NaN  0.098126       NaN
                                     neighbor_average      7.519939       NaN  11.514142       NaN  0.222668       NaN
       swap_from_best_random_trace   gls_map               3.169075       NaN   5.314099       NaN  0.083618       NaN
                                     gsp                   3.617284       NaN   6.276936       NaN  0.099854       NaN
                                     historical_tod_mean   3.590513       NaN   6.326044       NaN  0.098255       NaN
                                     neighbor_average      7.394453       NaN  11.523690       NaN  0.224801       NaN
       swap_from_greedy_a_trace      gls_map               3.170483       NaN   5.341554       NaN  0.083321       NaN
                                     gsp                   3.658061       NaN   6.333397       NaN  0.099547       NaN
                                     historical_tod_mean   3.611753       NaN   6.379602       NaN  0.098112       NaN
                                     neighbor_average      7.302039       NaN  11.355347       NaN  0.220263       NaN
       swap_from_scenario_average    gls_map               3.181791       NaN   5.363856       NaN  0.085024       NaN
                                     gsp                   3.647894       NaN   6.329412       NaN  0.100021       NaN
                                     historical_tod_mean   3.603444       NaN   6.371841       NaN  0.098132       NaN
                                     neighbor_average      7.289452       NaN  11.289508       NaN  0.221067       NaN
       swap_from_scenario_cvar       gls_map               3.157277       NaN   5.359868       NaN  0.086695       NaN
                                     gsp                   3.618682       NaN   6.344295       NaN  0.101911       NaN
                                     historical_tod_mean   3.573189       NaN   6.380129       NaN  0.099733       NaN
                                     neighbor_average      7.252581       NaN  11.169956       NaN  0.220208       NaN
       top_variance                  gls_map               3.052263       NaN   5.380595       NaN  0.071374       NaN
                                     gsp                   3.147714       NaN   5.664101       NaN  0.075494       NaN
                                     historical_tod_mean   3.168165       NaN   5.703691       NaN  0.076298       NaN
                                     neighbor_average      9.852168       NaN  15.064610       NaN  0.187682       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1       swap_from_scenario_cvar gls_map 3.357446 5.844062
    0.2                  top_variance gls_map 3.222778 5.744870
    0.3 multistart_swap_by_validation gls_map 3.008224 5.210543
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.204320      0.257372 648
    gsp   condition_number     0.205293      0.196789 648
    gsp information_logdet    -0.224969     -0.260611 648
gls_map    posterior_trace     0.844871      0.849144 648
gls_map   condition_number     0.816346      0.845090 648
gls_map information_logdet    -0.802324     -0.801921 648
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv