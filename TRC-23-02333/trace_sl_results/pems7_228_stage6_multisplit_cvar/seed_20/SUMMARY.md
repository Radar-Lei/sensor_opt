---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-01, 2012-06-05
Test days: 2012-06-04, 2012-06-28
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.528060       NaN   5.889086       NaN  0.082247       NaN
                                     gsp                   3.889070       NaN   6.470752       NaN  0.090665       NaN
                                     historical_tod_mean   3.880096       NaN   6.680173       NaN  0.093184       NaN
                                     neighbor_average      7.447236       NaN  11.195451       NaN  0.184391       NaN
       best_random_by_validation     gls_map               3.689362       NaN   6.123718       NaN  0.082670       NaN
                                     gsp                   3.889595       NaN   6.387044       NaN  0.088751       NaN
                                     historical_tod_mean   3.833837       NaN   6.580875       NaN  0.090527       NaN
                                     neighbor_average      8.155565       NaN  12.338945       NaN  0.191378       NaN
       coverage                      gls_map               3.738463       NaN   6.212276       NaN  0.089662       NaN
                                     gsp                   3.971381       NaN   6.677010       NaN  0.093334       NaN
                                     historical_tod_mean   3.921396       NaN   6.763861       NaN  0.094895       NaN
                                     neighbor_average      7.629438       NaN  11.508932       NaN  0.197146       NaN
       degree                        gls_map               4.026956       NaN   6.705187       NaN  0.095110       NaN
                                     gsp                   4.067065       NaN   6.789086       NaN  0.095469       NaN
                                     historical_tod_mean   3.952599       NaN   6.837055       NaN  0.096146       NaN
                                     neighbor_average      8.386175       NaN  12.776689       NaN  0.219147       NaN
       greedy_a_trace                gls_map               3.524430       NaN   5.971056       NaN  0.085940       NaN
                                     gsp                   3.946869       NaN   6.581870       NaN  0.093717       NaN
                                     historical_tod_mean   3.927912       NaN   6.770962       NaN  0.095123       NaN
                                     neighbor_average      7.317017       NaN  11.099822       NaN  0.196714       NaN
       greedy_d_logdet               gls_map               4.564674       NaN   6.948678       NaN  0.109889       NaN
                                     gsp                   4.104432       NaN   6.625658       NaN  0.098142       NaN
                                     historical_tod_mean   3.918629       NaN   6.680124       NaN  0.095304       NaN
                                     neighbor_average      8.249328       NaN  13.188565       NaN  0.238120       NaN
       multistart_swap_by_validation gls_map               3.418499       NaN   5.632313       NaN  0.081769       NaN
                                     gsp                   3.935066       NaN   6.431053       NaN  0.092506       NaN
                                     historical_tod_mean   3.884815       NaN   6.647988       NaN  0.093694       NaN
                                     neighbor_average      7.410761       NaN  11.116920       NaN  0.194609       NaN
       random                        gls_map               3.682397  0.075803   6.100976  0.126588  0.087156  0.002733
                                     gsp                   3.928204  0.045809   6.524842  0.081892  0.092406  0.001873
                                     historical_tod_mean   3.897065  0.035784   6.701660  0.058370  0.093798  0.001307
                                     neighbor_average      7.634913  0.286977  11.505820  0.383588  0.192227  0.006594
       scenario_average_a_trace      gls_map               3.579476       NaN   6.007093       NaN  0.083711       NaN
                                     gsp                   3.957670       NaN   6.612591       NaN  0.091379       NaN
                                     historical_tod_mean   3.915086       NaN   6.726878       NaN  0.094339       NaN
                                     neighbor_average      7.008871       NaN  10.713703       NaN  0.186745       NaN
       scenario_cvar_a_trace         gls_map               3.536614       NaN   5.823477       NaN  0.081060       NaN
                                     gsp                   3.876047       NaN   6.358107       NaN  0.088159       NaN
                                     historical_tod_mean   3.787207       NaN   6.479573       NaN  0.089976       NaN
                                     neighbor_average      7.791193       NaN  11.378577       NaN  0.186628       NaN
       swap_from_best_random_trace   gls_map               3.446575       NaN   5.727050       NaN  0.083017       NaN
                                     gsp                   3.977406       NaN   6.517472       NaN  0.093736       NaN
                                     historical_tod_mean   3.925141       NaN   6.709967       NaN  0.094923       NaN
                                     neighbor_average      7.431873       NaN  11.498282       NaN  0.202314       NaN
       swap_from_greedy_a_trace      gls_map               3.513339       NaN   5.806687       NaN  0.083046       NaN
                                     gsp                   3.971074       NaN   6.521164       NaN  0.092752       NaN
                                     historical_tod_mean   3.921555       NaN   6.723586       NaN  0.094634       NaN
                                     neighbor_average      7.433723       NaN  11.297091       NaN  0.199151       NaN
       swap_from_scenario_average    gls_map               3.521817       NaN   5.859016       NaN  0.084365       NaN
                                     gsp                   3.945203       NaN   6.542545       NaN  0.093062       NaN
                                     historical_tod_mean   3.921548       NaN   6.750100       NaN  0.094896       NaN
                                     neighbor_average      7.340072       NaN  11.203470       NaN  0.196533       NaN
       swap_from_scenario_cvar       gls_map               3.401103       NaN   5.630545       NaN  0.081607       NaN
                                     gsp                   3.923737       NaN   6.437734       NaN  0.092640       NaN
                                     historical_tod_mean   3.887199       NaN   6.657551       NaN  0.093880       NaN
                                     neighbor_average      7.600554       NaN  11.475233       NaN  0.198435       NaN
       top_variance                  gls_map               3.592668       NaN   5.932208       NaN  0.081930       NaN
                                     gsp                   3.727151       NaN   6.187151       NaN  0.086176       NaN
                                     historical_tod_mean   3.687853       NaN   6.335663       NaN  0.086226       NaN
                                     neighbor_average     11.263644       NaN  17.041635       NaN  0.218906       NaN
0.2    best_random_by_trace          gls_map               3.507922       NaN   5.855756       NaN  0.082086       NaN
                                     gsp                   4.015811       NaN   6.643765       NaN  0.092645       NaN
                                     historical_tod_mean   3.938005       NaN   6.789867       NaN  0.094089       NaN
                                     neighbor_average      7.044806       NaN  11.045806       NaN  0.190438       NaN
       best_random_by_validation     gls_map               3.244815       NaN   5.360160       NaN  0.077312       NaN
                                     gsp                   3.842023       NaN   6.359864       NaN  0.091436       NaN
                                     historical_tod_mean   3.836052       NaN   6.602764       NaN  0.092426       NaN
                                     neighbor_average      7.101561       NaN  10.858344       NaN  0.181060       NaN
       coverage                      gls_map               3.468242       NaN   5.814238       NaN  0.084618       NaN
                                     gsp                   3.986704       NaN   6.645613       NaN  0.095315       NaN
                                     historical_tod_mean   3.932178       NaN   6.843299       NaN  0.096874       NaN
                                     neighbor_average      7.110961       NaN  10.766119       NaN  0.186243       NaN
       degree                        gls_map               3.962015       NaN   6.555207       NaN  0.094611       NaN
                                     gsp                   4.098776       NaN   6.690743       NaN  0.096339       NaN
                                     historical_tod_mean   4.004043       NaN   6.829498       NaN  0.097156       NaN
                                     neighbor_average      7.894469       NaN  11.876019       NaN  0.205391       NaN
       greedy_a_trace                gls_map               3.298418       NaN   5.498318       NaN  0.080502       NaN
                                     gsp                   3.969034       NaN   6.582760       NaN  0.095062       NaN
                                     historical_tod_mean   3.925472       NaN   6.757855       NaN  0.096225       NaN
                                     neighbor_average      7.384625       NaN  11.394161       NaN  0.205197       NaN
       greedy_d_logdet               gls_map               4.062814       NaN   6.338672       NaN  0.099373       NaN
                                     gsp                   4.061645       NaN   6.624665       NaN  0.096722       NaN
                                     historical_tod_mean   3.955593       NaN   6.749804       NaN  0.096997       NaN
                                     neighbor_average      8.104127       NaN  12.774640       NaN  0.235903       NaN
       multistart_swap_by_validation gls_map               3.287978       NaN   5.492904       NaN  0.079867       NaN
                                     gsp                   3.957569       NaN   6.582818       NaN  0.093833       NaN
                                     historical_tod_mean   3.921983       NaN   6.770993       NaN  0.095818       NaN
                                     neighbor_average      7.078509       NaN  10.874269       NaN  0.192729       NaN
       random                        gls_map               3.435841  0.090442   5.744509  0.162452  0.081684  0.002946
                                     gsp                   3.936449  0.058629   6.494936  0.098460  0.092541  0.002261
                                     historical_tod_mean   3.905513  0.057628   6.713082  0.094364  0.094123  0.002071
                                     neighbor_average      7.371001  0.181863  11.246700  0.278827  0.186876  0.007048
       scenario_average_a_trace      gls_map               3.412509       NaN   5.658837       NaN  0.081237       NaN
                                     gsp                   4.019377       NaN   6.595457       NaN  0.093212       NaN
                                     historical_tod_mean   3.919349       NaN   6.723545       NaN  0.094990       NaN
                                     neighbor_average      7.293084       NaN  10.846300       NaN  0.193937       NaN
       scenario_cvar_a_trace         gls_map               3.353416       NaN   5.526367       NaN  0.077814       NaN
                                     gsp                   3.953468       NaN   6.472185       NaN  0.090271       NaN
                                     historical_tod_mean   3.885245       NaN   6.610952       NaN  0.092796       NaN
                                     neighbor_average      7.217184       NaN  10.961311       NaN  0.190312       NaN
       swap_from_best_random_trace   gls_map               3.284637       NaN   5.407805       NaN  0.079169       NaN
                                     gsp                   3.927633       NaN   6.489961       NaN  0.093174       NaN
                                     historical_tod_mean   3.895835       NaN   6.679283       NaN  0.094538       NaN
                                     neighbor_average      7.094862       NaN  10.898592       NaN  0.193952       NaN
       swap_from_greedy_a_trace      gls_map               3.274904       NaN   5.399184       NaN  0.079218       NaN
                                     gsp                   3.964083       NaN   6.527371       NaN  0.094442       NaN
                                     historical_tod_mean   3.925519       NaN   6.718539       NaN  0.095908       NaN
                                     neighbor_average      7.313510       NaN  11.360669       NaN  0.202440       NaN
       swap_from_scenario_average    gls_map               3.342589       NaN   5.501268       NaN  0.082609       NaN
                                     gsp                   3.959435       NaN   6.527239       NaN  0.095236       NaN
                                     historical_tod_mean   3.919425       NaN   6.702025       NaN  0.096228       NaN
                                     neighbor_average      7.313894       NaN  11.284109       NaN  0.206864       NaN
       swap_from_scenario_cvar       gls_map               3.312492       NaN   5.449501       NaN  0.081426       NaN
                                     gsp                   3.964283       NaN   6.493368       NaN  0.095053       NaN
                                     historical_tod_mean   3.933108       NaN   6.698165       NaN  0.095854       NaN
                                     neighbor_average      7.156313       NaN  11.084637       NaN  0.200678       NaN
       top_variance                  gls_map               3.391367       NaN   5.608158       NaN  0.073543       NaN
                                     gsp                   3.564396       NaN   5.936546       NaN  0.078676       NaN
                                     historical_tod_mean   3.520664       NaN   6.093642       NaN  0.079162       NaN
                                     neighbor_average     10.141909       NaN  15.433136       NaN  0.192038       NaN
0.3    best_random_by_trace          gls_map               3.442088       NaN   5.771211       NaN  0.083098       NaN
                                     gsp                   4.083698       NaN   6.701339       NaN  0.096696       NaN
                                     historical_tod_mean   4.019074       NaN   6.902694       NaN  0.098444       NaN
                                     neighbor_average      7.040662       NaN  10.835645       NaN  0.192676       NaN
       best_random_by_validation     gls_map               2.981833       NaN   4.931183       NaN  0.067407       NaN
                                     gsp                   3.752742       NaN   6.184472       NaN  0.084215       NaN
                                     historical_tod_mean   3.713251       NaN   6.411997       NaN  0.086389       NaN
                                     neighbor_average      7.577799       NaN  11.212505       NaN  0.173052       NaN
       coverage                      gls_map               3.227218       NaN   5.550948       NaN  0.079178       NaN
                                     gsp                   3.939991       NaN   6.666006       NaN  0.093953       NaN
                                     historical_tod_mean   3.894619       NaN   6.854068       NaN  0.095838       NaN
                                     neighbor_average      7.102305       NaN  10.649903       NaN  0.182772       NaN
       degree                        gls_map               3.857871       NaN   6.400700       NaN  0.091131       NaN
                                     gsp                   4.115652       NaN   6.689905       NaN  0.094609       NaN
                                     historical_tod_mean   3.954342       NaN   6.818976       NaN  0.095345       NaN
                                     neighbor_average      8.477198       NaN  12.795142       NaN  0.219415       NaN
       greedy_a_trace                gls_map               3.185568       NaN   5.245391       NaN  0.076677       NaN
                                     gsp                   3.961213       NaN   6.508470       NaN  0.093012       NaN
                                     historical_tod_mean   3.891741       NaN   6.687350       NaN  0.094846       NaN
                                     neighbor_average      7.055391       NaN  10.860690       NaN  0.197774       NaN
       greedy_d_logdet               gls_map               3.668357       NaN   5.738115       NaN  0.090071       NaN
                                     gsp                   3.973490       NaN   6.503390       NaN  0.093910       NaN
                                     historical_tod_mean   3.866757       NaN   6.653512       NaN  0.094942       NaN
                                     neighbor_average      7.796845       NaN  12.053690       NaN  0.223268       NaN
       multistart_swap_by_validation gls_map               3.078138       NaN   5.039750       NaN  0.072476       NaN
                                     gsp                   3.849336       NaN   6.314481       NaN  0.089157       NaN
                                     historical_tod_mean   3.807545       NaN   6.522679       NaN  0.091334       NaN
                                     neighbor_average      6.927731       NaN  10.600934       NaN  0.182254       NaN
       random                        gls_map               3.277799  0.096828   5.508479  0.184878  0.077435  0.003475
                                     gsp                   3.926993  0.074033   6.475650  0.121177  0.091868  0.003001
                                     historical_tod_mean   3.896604  0.078813   6.712070  0.121436  0.093774  0.002938
                                     neighbor_average      7.242372  0.195364  11.101677  0.324127  0.181493  0.008127
       scenario_average_a_trace      gls_map               3.169081       NaN   5.203196       NaN  0.075012       NaN
                                     gsp                   3.989712       NaN   6.495495       NaN  0.092555       NaN
                                     historical_tod_mean   3.889263       NaN   6.659837       NaN  0.094364       NaN
                                     neighbor_average      7.171925       NaN  10.781782       NaN  0.191345       NaN
       scenario_cvar_a_trace         gls_map               3.070920       NaN   5.056598       NaN  0.070742       NaN
                                     gsp                   3.880656       NaN   6.356483       NaN  0.087515       NaN
                                     historical_tod_mean   3.797921       NaN   6.502966       NaN  0.089970       NaN
                                     neighbor_average      7.101722       NaN  10.685450       NaN  0.177757       NaN
       swap_from_best_random_trace   gls_map               3.190087       NaN   5.214705       NaN  0.078016       NaN
                                     gsp                   3.989019       NaN   6.515940       NaN  0.094590       NaN
                                     historical_tod_mean   3.896992       NaN   6.706318       NaN  0.095846       NaN
                                     neighbor_average      7.128024       NaN  10.951565       NaN  0.195152       NaN
       swap_from_greedy_a_trace      gls_map               3.221960       NaN   5.258776       NaN  0.078229       NaN
                                     gsp                   3.991422       NaN   6.509854       NaN  0.093848       NaN
                                     historical_tod_mean   3.913191       NaN   6.695292       NaN  0.095421       NaN
                                     neighbor_average      7.102695       NaN  10.924808       NaN  0.197817       NaN
       swap_from_scenario_average    gls_map               3.205154       NaN   5.215177       NaN  0.078316       NaN
                                     gsp                   3.934344       NaN   6.434444       NaN  0.092885       NaN
                                     historical_tod_mean   3.871127       NaN   6.630230       NaN  0.094404       NaN
                                     neighbor_average      7.135674       NaN  10.977513       NaN  0.199734       NaN
       swap_from_scenario_cvar       gls_map               3.200117       NaN   5.190024       NaN  0.078081       NaN
                                     gsp                   3.945231       NaN   6.452921       NaN  0.092926       NaN
                                     historical_tod_mean   3.910219       NaN   6.656655       NaN  0.095125       NaN
                                     neighbor_average      7.134808       NaN  10.916650       NaN  0.197529       NaN
       top_variance                  gls_map               3.187424       NaN   5.244793       NaN  0.067743       NaN
                                     gsp                   3.428512       NaN   5.649305       NaN  0.073924       NaN
                                     historical_tod_mean   3.362967       NaN   5.789433       NaN  0.073882       NaN
                                     neighbor_average      9.987751       NaN  14.951865       NaN  0.185529       NaN
```

## Best method per budget-layout row

```
 budget             layout_type  method      mae     rmse
    0.1 swap_from_scenario_cvar gls_map 3.401103 5.630545
    0.2                  random gls_map 3.236700 5.396222
    0.3                  random gls_map 2.981833 4.931183
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.002182      0.046066 642
    gsp   condition_number     0.004510      0.004247 642
    gsp information_logdet    -0.028954     -0.072928 642
gls_map    posterior_trace     0.865568      0.860531 642
gls_map   condition_number     0.829938      0.860923 642
gls_map information_logdet    -0.820969     -0.815625 642
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- certificate_correlations.csv