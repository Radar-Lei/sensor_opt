---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-27, 2012-06-22
Test days: 2012-05-02, 2012-05-09
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.599503       NaN   6.208602       NaN  0.087361       NaN
                                     gsp                   3.720742       NaN   6.521748       NaN  0.091256       NaN
                                     historical_tod_mean   3.964659       NaN   6.830298       NaN  0.091941       NaN
                                     neighbor_average      7.225916       NaN  11.217127       NaN  0.181842       NaN
       best_random_by_validation     gls_map               3.599503       NaN   6.208602       NaN  0.087361       NaN
                                     gsp                   3.720742       NaN   6.521748       NaN  0.091256       NaN
                                     historical_tod_mean   3.964659       NaN   6.830298       NaN  0.091941       NaN
                                     neighbor_average      7.225916       NaN  11.217127       NaN  0.181842       NaN
       coverage                      gls_map               3.717870       NaN   6.398277       NaN  0.089677       NaN
                                     gsp                   3.798060       NaN   6.624576       NaN  0.092064       NaN
                                     historical_tod_mean   3.996823       NaN   6.901022       NaN  0.093158       NaN
                                     neighbor_average      7.401059       NaN  11.521711       NaN  0.192852       NaN
       degree                        gls_map               3.919825       NaN   6.640431       NaN  0.095385       NaN
                                     gsp                   3.868824       NaN   6.670298       NaN  0.092512       NaN
                                     historical_tod_mean   3.997742       NaN   6.899259       NaN  0.092711       NaN
                                     neighbor_average      8.100538       NaN  12.477806       NaN  0.204960       NaN
       greedy_a_trace                gls_map               3.504054       NaN   5.979966       NaN  0.082325       NaN
                                     gsp                   3.750866       NaN   6.557646       NaN  0.088961       NaN
                                     historical_tod_mean   3.987291       NaN   6.884962       NaN  0.092436       NaN
                                     neighbor_average      7.034844       NaN  10.808849       NaN  0.185523       NaN
       greedy_d_logdet               gls_map               4.113993       NaN   6.721203       NaN  0.099371       NaN
                                     gsp                   3.869355       NaN   6.629632       NaN  0.091905       NaN
                                     historical_tod_mean   4.018094       NaN   6.914821       NaN  0.093581       NaN
                                     neighbor_average      7.663346       NaN  12.615666       NaN  0.218599       NaN
       multistart_swap_by_validation gls_map               3.402139       NaN   5.980227       NaN  0.081088       NaN
                                     gsp                   3.757945       NaN   6.577431       NaN  0.089348       NaN
                                     historical_tod_mean   4.016568       NaN   6.910040       NaN  0.092987       NaN
                                     neighbor_average      6.929263       NaN  10.863106       NaN  0.186155       NaN
       random                        gls_map               3.658071  0.077954   6.267557  0.118936  0.087454  0.003006
                                     gsp                   3.773749  0.056384   6.543993  0.069472  0.090031  0.001772
                                     historical_tod_mean   3.976725  0.039792   6.859887  0.064767  0.092029  0.001241
                                     neighbor_average      7.463976  0.258284  11.515810  0.390102  0.186036  0.006169
       rcss_selected                 gls_map               3.466328       NaN   5.908188       NaN  0.078764       NaN
                                     gsp                   3.791935       NaN   6.569304       NaN  0.087726       NaN
                                     historical_tod_mean   3.989401       NaN   6.862222       NaN  0.091233       NaN
                                     neighbor_average      7.220087       NaN  11.093330       NaN  0.182584       NaN
       robust_coverage_cvar          gls_map               3.543945       NaN   6.273643       NaN  0.087065       NaN
                                     gsp                   3.771201       NaN   6.625004       NaN  0.091269       NaN
                                     historical_tod_mean   4.040159       NaN   6.956963       NaN  0.094173       NaN
                                     neighbor_average      7.224083       NaN  11.226326       NaN  0.191394       NaN
       scenario_average_a_trace      gls_map               3.458123       NaN   6.127416       NaN  0.084609       NaN
                                     gsp                   3.739940       NaN   6.592763       NaN  0.090918       NaN
                                     historical_tod_mean   4.015216       NaN   6.923566       NaN  0.093324       NaN
                                     neighbor_average      7.281701       NaN  11.282575       NaN  0.184927       NaN
       scenario_cvar_a_trace         gls_map               3.434776       NaN   6.051804       NaN  0.080979       NaN
                                     gsp                   3.731416       NaN   6.565614       NaN  0.088702       NaN
                                     historical_tod_mean   3.992158       NaN   6.896225       NaN  0.092321       NaN
                                     neighbor_average      7.230665       NaN  11.308587       NaN  0.181000       NaN
       swap_from_best_random_trace   gls_map               3.402139       NaN   5.980227       NaN  0.081088       NaN
                                     gsp                   3.757945       NaN   6.577431       NaN  0.089348       NaN
                                     historical_tod_mean   4.016568       NaN   6.910040       NaN  0.092987       NaN
                                     neighbor_average      6.929263       NaN  10.863106       NaN  0.186155       NaN
       swap_from_greedy_a_trace      gls_map               3.466328       NaN   5.908188       NaN  0.078764       NaN
                                     gsp                   3.791935       NaN   6.569304       NaN  0.087726       NaN
                                     historical_tod_mean   3.989401       NaN   6.862222       NaN  0.091233       NaN
                                     neighbor_average      7.220087       NaN  11.093330       NaN  0.182584       NaN
       swap_from_scenario_average    gls_map               3.398187       NaN   5.957669       NaN  0.079006       NaN
                                     gsp                   3.766015       NaN   6.564841       NaN  0.087999       NaN
                                     historical_tod_mean   4.002347       NaN   6.877809       NaN  0.091664       NaN
                                     neighbor_average      7.246730       NaN  11.234253       NaN  0.184505       NaN
       swap_from_scenario_cvar       gls_map               3.465130       NaN   5.921690       NaN  0.079744       NaN
                                     gsp                   3.778646       NaN   6.578424       NaN  0.088383       NaN
                                     historical_tod_mean   3.996383       NaN   6.883011       NaN  0.091872       NaN
                                     neighbor_average      7.174135       NaN  11.001609       NaN  0.183549       NaN
       top_variance                  gls_map               3.477628       NaN   5.871177       NaN  0.077208       NaN
                                     gsp                   3.539028       NaN   6.140511       NaN  0.080191       NaN
                                     historical_tod_mean   3.727966       NaN   6.393421       NaN  0.083274       NaN
                                     neighbor_average     10.693407       NaN  16.493436       NaN  0.208298       NaN
0.2    best_random_by_trace          gls_map               3.387730       NaN   5.869308       NaN  0.082259       NaN
                                     gsp                   3.768416       NaN   6.403915       NaN  0.089801       NaN
                                     historical_tod_mean   3.938244       NaN   6.761440       NaN  0.090918       NaN
                                     neighbor_average      7.035302       NaN  11.065733       NaN  0.187030       NaN
       best_random_by_validation     gls_map               3.270184       NaN   5.588462       NaN  0.073673       NaN
                                     gsp                   3.715723       NaN   6.401891       NaN  0.086229       NaN
                                     historical_tod_mean   3.953353       NaN   6.795985       NaN  0.089785       NaN
                                     neighbor_average      6.995281       NaN  10.658788       NaN  0.168035       NaN
       coverage                      gls_map               3.416141       NaN   5.936227       NaN  0.080959       NaN
                                     gsp                   3.768132       NaN   6.558833       NaN  0.090245       NaN
                                     historical_tod_mean   4.006775       NaN   6.934378       NaN  0.093819       NaN
                                     neighbor_average      7.014621       NaN  10.818484       NaN  0.179913       NaN
       degree                        gls_map               3.829607       NaN   6.524394       NaN  0.092461       NaN
                                     gsp                   3.841701       NaN   6.601869       NaN  0.090955       NaN
                                     historical_tod_mean   4.047049       NaN   6.917114       NaN  0.093250       NaN
                                     neighbor_average      7.597361       NaN  11.785041       NaN  0.191120       NaN
       greedy_a_trace                gls_map               3.336125       NaN   5.719964       NaN  0.078814       NaN
                                     gsp                   3.804803       NaN   6.600650       NaN  0.090442       NaN
                                     historical_tod_mean   4.038315       NaN   6.992463       NaN  0.094062       NaN
                                     neighbor_average      6.905161       NaN  10.655900       NaN  0.182962       NaN
       greedy_d_logdet               gls_map               3.913042       NaN   6.440231       NaN  0.093888       NaN
                                     gsp                   3.906417       NaN   6.679908       NaN  0.093461       NaN
                                     historical_tod_mean   4.105858       NaN   7.033330       NaN  0.095811       NaN
                                     neighbor_average      7.614150       NaN  12.291049       NaN  0.217743       NaN
       multistart_swap_by_validation gls_map               3.313649       NaN   5.739574       NaN  0.077997       NaN
                                     gsp                   3.798526       NaN   6.578951       NaN  0.088808       NaN
                                     historical_tod_mean   4.008142       NaN   6.927636       NaN  0.092352       NaN
                                     neighbor_average      7.024510       NaN  10.995909       NaN  0.183563       NaN
       random                        gls_map               3.429397  0.090383   5.913060  0.167480  0.081393  0.003551
                                     gsp                   3.744294  0.071295   6.496751  0.111270  0.089759  0.002592
                                     historical_tod_mean   3.981881  0.065739   6.861740  0.111903  0.092143  0.002111
                                     neighbor_average      7.230039  0.175320  11.231306  0.298243  0.179854  0.007226
       rcss_selected                 gls_map               3.313649       NaN   5.739574       NaN  0.077997       NaN
                                     gsp                   3.798526       NaN   6.578951       NaN  0.088808       NaN
                                     historical_tod_mean   4.008142       NaN   6.927636       NaN  0.092352       NaN
                                     neighbor_average      7.024510       NaN  10.995909       NaN  0.183563       NaN
       robust_coverage_cvar          gls_map               3.384175       NaN   5.977361       NaN  0.083472       NaN
                                     gsp                   3.744843       NaN   6.573526       NaN  0.091785       NaN
                                     historical_tod_mean   4.000539       NaN   6.940986       NaN  0.094221       NaN
                                     neighbor_average      7.038222       NaN  11.088618       NaN  0.187342       NaN
       scenario_average_a_trace      gls_map               3.390757       NaN   5.987452       NaN  0.082355       NaN
                                     gsp                   3.812589       NaN   6.683703       NaN  0.093201       NaN
                                     historical_tod_mean   4.086665       NaN   7.075249       NaN  0.096063       NaN
                                     neighbor_average      7.042124       NaN  10.973447       NaN  0.183878       NaN
       scenario_cvar_a_trace         gls_map               3.332284       NaN   5.872413       NaN  0.079094       NaN
                                     gsp                   3.750135       NaN   6.587190       NaN  0.089749       NaN
                                     historical_tod_mean   4.008922       NaN   6.972282       NaN  0.093640       NaN
                                     neighbor_average      7.020722       NaN  10.932040       NaN  0.178753       NaN
       swap_from_best_random_trace   gls_map               3.291417       NaN   5.605509       NaN  0.077261       NaN
                                     gsp                   3.758710       NaN   6.440699       NaN  0.088646       NaN
                                     historical_tod_mean   3.999889       NaN   6.832003       NaN  0.092047       NaN
                                     neighbor_average      7.002556       NaN  10.877629       NaN  0.183044       NaN
       swap_from_greedy_a_trace      gls_map               3.334105       NaN   5.772766       NaN  0.079024       NaN
                                     gsp                   3.791231       NaN   6.575399       NaN  0.089550       NaN
                                     historical_tod_mean   4.037070       NaN   6.977200       NaN  0.093336       NaN
                                     neighbor_average      6.952404       NaN  10.808307       NaN  0.185205       NaN
       swap_from_scenario_average    gls_map               3.351215       NaN   5.783062       NaN  0.079188       NaN
                                     gsp                   3.829660       NaN   6.623288       NaN  0.090062       NaN
                                     historical_tod_mean   4.075839       NaN   7.016054       NaN  0.094012       NaN
                                     neighbor_average      6.883895       NaN  10.698983       NaN  0.182132       NaN
       swap_from_scenario_cvar       gls_map               3.341411       NaN   5.825289       NaN  0.078687       NaN
                                     gsp                   3.856556       NaN   6.632199       NaN  0.090605       NaN
                                     historical_tod_mean   4.066553       NaN   7.003500       NaN  0.094181       NaN
                                     neighbor_average      6.899319       NaN  10.748979       NaN  0.182262       NaN
       top_variance                  gls_map               3.208909       NaN   5.455355       NaN  0.068936       NaN
                                     gsp                   3.310899       NaN   5.744711       NaN  0.073048       NaN
                                     historical_tod_mean   3.535287       NaN   6.035016       NaN  0.076835       NaN
                                     neighbor_average      9.188633       NaN  14.474583       NaN  0.176437       NaN
0.3    best_random_by_trace          gls_map               3.347809       NaN   5.813614       NaN  0.081404       NaN
                                     gsp                   3.820343       NaN   6.568197       NaN  0.092162       NaN
                                     historical_tod_mean   4.054282       NaN   6.975967       NaN  0.094897       NaN
                                     neighbor_average      6.900618       NaN  10.896781       NaN  0.185496       NaN
       best_random_by_validation     gls_map               3.187193       NaN   5.545524       NaN  0.074065       NaN
                                     gsp                   3.596024       NaN   6.346239       NaN  0.086890       NaN
                                     historical_tod_mean   3.859461       NaN   6.732496       NaN  0.089258       NaN
                                     neighbor_average      7.105696       NaN  11.163402       NaN  0.165917       NaN
       coverage                      gls_map               3.212743       NaN   5.543801       NaN  0.074978       NaN
                                     gsp                   3.661792       NaN   6.428370       NaN  0.087686       NaN
                                     historical_tod_mean   3.912786       NaN   6.839756       NaN  0.091477       NaN
                                     neighbor_average      6.986421       NaN  10.611217       NaN  0.173175       NaN
       degree                        gls_map               3.702839       NaN   6.318883       NaN  0.089955       NaN
                                     gsp                   3.823401       NaN   6.558043       NaN  0.090832       NaN
                                     historical_tod_mean   4.042521       NaN   6.913841       NaN  0.093169       NaN
                                     neighbor_average      7.975106       NaN  12.504204       NaN  0.208534       NaN
       greedy_a_trace                gls_map               3.243975       NaN   5.516758       NaN  0.078893       NaN
                                     gsp                   3.824652       NaN   6.607085       NaN  0.093360       NaN
                                     historical_tod_mean   4.072738       NaN   7.027525       NaN  0.096480       NaN
                                     neighbor_average      6.852214       NaN  10.727310       NaN  0.187546       NaN
       greedy_d_logdet               gls_map               3.603602       NaN   5.905574       NaN  0.089377       NaN
                                     gsp                   3.767851       NaN   6.463781       NaN  0.091878       NaN
                                     historical_tod_mean   3.990709       NaN   6.863755       NaN  0.094500       NaN
                                     neighbor_average      7.603228       NaN  12.154858       NaN  0.218500       NaN
       multistart_swap_by_validation gls_map               3.159865       NaN   5.493268       NaN  0.074441       NaN
                                     gsp                   3.649252       NaN   6.372728       NaN  0.087744       NaN
                                     historical_tod_mean   3.906712       NaN   6.813166       NaN  0.090434       NaN
                                     neighbor_average      6.760660       NaN  10.738894       NaN  0.173083       NaN
       random                        gls_map               3.281589  0.102629   5.667061  0.206248  0.077350  0.003931
                                     gsp                   3.717678  0.085156   6.461372  0.144635  0.089213  0.003397
                                     historical_tod_mean   3.971356  0.087426   6.849386  0.148717  0.091777  0.002929
                                     neighbor_average      7.126838  0.191845  11.100589  0.356763  0.174643  0.007966
       rcss_selected                 gls_map               3.110397       NaN   5.516864       NaN  0.075137       NaN
                                     gsp                   3.687188       NaN   6.513817       NaN  0.090914       NaN
                                     historical_tod_mean   3.971218       NaN   6.927132       NaN  0.093816       NaN
                                     neighbor_average      6.916852       NaN  10.730687       NaN  0.177477       NaN
       robust_coverage_cvar          gls_map               3.110397       NaN   5.516864       NaN  0.075137       NaN
                                     gsp                   3.687188       NaN   6.513817       NaN  0.090914       NaN
                                     historical_tod_mean   3.971218       NaN   6.927132       NaN  0.093816       NaN
                                     neighbor_average      6.916852       NaN  10.730687       NaN  0.177477       NaN
       scenario_average_a_trace      gls_map               3.203043       NaN   5.571248       NaN  0.078379       NaN
                                     gsp                   3.727443       NaN   6.553991       NaN  0.091869       NaN
                                     historical_tod_mean   4.004714       NaN   6.965658       NaN  0.094838       NaN
                                     neighbor_average      7.014453       NaN  10.978357       NaN  0.184298       NaN
       scenario_cvar_a_trace         gls_map               3.307667       NaN   5.829466       NaN  0.079329       NaN
                                     gsp                   3.775994       NaN   6.671479       NaN  0.093228       NaN
                                     historical_tod_mean   4.046716       NaN   7.085184       NaN  0.096207       NaN
                                     neighbor_average      6.813372       NaN  10.563894       NaN  0.178924       NaN
       swap_from_best_random_trace   gls_map               3.186978       NaN   5.529407       NaN  0.078015       NaN
                                     gsp                   3.807370       NaN   6.515651       NaN  0.091062       NaN
                                     historical_tod_mean   4.018514       NaN   6.928515       NaN  0.093765       NaN
                                     neighbor_average      6.922233       NaN  10.897706       NaN  0.183868       NaN
       swap_from_greedy_a_trace      gls_map               3.281997       NaN   5.534948       NaN  0.077888       NaN
                                     gsp                   3.814598       NaN   6.533108       NaN  0.091311       NaN
                                     historical_tod_mean   4.065952       NaN   6.956592       NaN  0.094663       NaN
                                     neighbor_average      6.825515       NaN  10.684722       NaN  0.184980       NaN
       swap_from_scenario_average    gls_map               3.256852       NaN   5.539920       NaN  0.078924       NaN
                                     gsp                   3.791830       NaN   6.566511       NaN  0.092335       NaN
                                     historical_tod_mean   4.050616       NaN   6.984556       NaN  0.095110       NaN
                                     neighbor_average      6.906940       NaN  11.015241       NaN  0.188365       NaN
       swap_from_scenario_cvar       gls_map               3.300402       NaN   5.668258       NaN  0.076831       NaN
                                     gsp                   3.812022       NaN   6.634808       NaN  0.091045       NaN
                                     historical_tod_mean   4.071134       NaN   7.059549       NaN  0.094944       NaN
                                     neighbor_average      6.837697       NaN  10.676085       NaN  0.181971       NaN
       top_variance                  gls_map               2.924422       NaN   4.996497       NaN  0.062127       NaN
                                     gsp                   3.083082       NaN   5.406193       NaN  0.067752       NaN
                                     historical_tod_mean   3.310999       NaN   5.668794       NaN  0.071288       NaN
                                     neighbor_average      8.573407       NaN  13.322415       NaN  0.160981       NaN
```

## Best method per budget-layout row

```
 budget                layout_type  method      mae     rmse
    0.1 swap_from_scenario_average gls_map 3.398187 5.957669
    0.2                     random gls_map 3.198751 5.558884
    0.3               top_variance gls_map 2.924422 4.996497
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.272371      0.293636 648
    gsp   condition_number     0.273671      0.267256 648
    gsp information_logdet    -0.287419     -0.303984 648
gls_map    posterior_trace     0.845192      0.845714 648
gls_map   condition_number     0.810769      0.844675 648
gls_map information_logdet    -0.813299     -0.809566 648
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv