---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-22, 2012-05-01
Test days: 2012-06-13, 2012-06-19
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.463892       NaN   5.913904       NaN  0.087528       NaN
                                     gsp                   3.686064       NaN   6.431563       NaN  0.097705       NaN
                                     historical_tod_mean   3.689073       NaN   6.611431       NaN  0.102921       NaN
                                     neighbor_average      7.994400       NaN  12.237571       NaN  0.206619       NaN
       best_random_by_validation     gls_map               3.467120       NaN   5.943677       NaN  0.088011       NaN
                                     gsp                   3.660492       NaN   6.392597       NaN  0.097705       NaN
                                     historical_tod_mean   3.670447       NaN   6.592956       NaN  0.104249       NaN
                                     neighbor_average      7.856310       NaN  11.676853       NaN  0.207287       NaN
       coverage                      gls_map               3.870601       NaN   6.559691       NaN  0.101140       NaN
                                     gsp                   3.836435       NaN   6.629246       NaN  0.104037       NaN
                                     historical_tod_mean   3.747774       NaN   6.747121       NaN  0.107596       NaN
                                     neighbor_average      8.329350       NaN  12.656879       NaN  0.238602       NaN
       degree                        gls_map               4.058845       NaN   6.938565       NaN  0.112816       NaN
                                     gsp                   3.946477       NaN   6.879501       NaN  0.114265       NaN
                                     historical_tod_mean   3.764954       NaN   6.736468       NaN  0.108790       NaN
                                     neighbor_average      8.869116       NaN  13.627190       NaN  0.265364       NaN
       greedy_a_trace                gls_map               3.530191       NaN   6.132555       NaN  0.093311       NaN
                                     gsp                   3.859499       NaN   6.612466       NaN  0.106823       NaN
                                     historical_tod_mean   3.728998       NaN   6.668059       NaN  0.107092       NaN
                                     neighbor_average      8.294585       NaN  12.549220       NaN  0.250026       NaN
       greedy_d_logdet               gls_map               4.802491       NaN   7.390248       NaN  0.132573       NaN
                                     gsp                   3.958131       NaN   6.719335       NaN  0.114827       NaN
                                     historical_tod_mean   3.704535       NaN   6.596553       NaN  0.107866       NaN
                                     neighbor_average      8.781978       NaN  14.475692       NaN  0.298447       NaN
       multistart_swap_by_validation gls_map               3.483150       NaN   5.903356       NaN  0.088889       NaN
                                     gsp                   3.779722       NaN   6.490370       NaN  0.102606       NaN
                                     historical_tod_mean   3.716674       NaN   6.630903       NaN  0.105654       NaN
                                     neighbor_average      7.803542       NaN  12.009827       NaN  0.228025       NaN
       random                        gls_map               3.686661  0.089224   6.277134  0.129131  0.095145  0.003459
                                     gsp                   3.772391  0.054209   6.538117  0.077382  0.102047  0.002878
                                     historical_tod_mean   3.718168  0.036803   6.658117  0.060968  0.105604  0.001640
                                     neighbor_average      8.199528  0.307647  12.418493  0.436477  0.223380  0.013810
       rcss_selected                 gls_map               3.483150       NaN   5.903356       NaN  0.088889       NaN
                                     gsp                   3.779722       NaN   6.490370       NaN  0.102606       NaN
                                     historical_tod_mean   3.716674       NaN   6.630903       NaN  0.105654       NaN
                                     neighbor_average      7.803542       NaN  12.009827       NaN  0.228025       NaN
       robust_coverage_cvar          gls_map               3.502637       NaN   5.940721       NaN  0.091300       NaN
                                     gsp                   3.841877       NaN   6.548550       NaN  0.106279       NaN
                                     historical_tod_mean   3.686880       NaN   6.587343       NaN  0.105505       NaN
                                     neighbor_average      8.392029       NaN  12.658064       NaN  0.245881       NaN
       scenario_average_a_trace      gls_map               3.612447       NaN   6.069751       NaN  0.097559       NaN
                                     gsp                   3.913943       NaN   6.597949       NaN  0.108537       NaN
                                     historical_tod_mean   3.672430       NaN   6.577780       NaN  0.105088       NaN
                                     neighbor_average      8.640480       NaN  12.774786       NaN  0.240404       NaN
       scenario_cvar_a_trace         gls_map               3.477059       NaN   5.989854       NaN  0.091442       NaN
                                     gsp                   3.799939       NaN   6.579678       NaN  0.105169       NaN
                                     historical_tod_mean   3.723412       NaN   6.664012       NaN  0.106214       NaN
                                     neighbor_average      8.037054       NaN  12.277058       NaN  0.234488       NaN
       swap_from_best_random_trace   gls_map               3.538724       NaN   6.000079       NaN  0.090176       NaN
                                     gsp                   3.818730       NaN   6.528719       NaN  0.104119       NaN
                                     historical_tod_mean   3.724795       NaN   6.657611       NaN  0.106678       NaN
                                     neighbor_average      7.886048       NaN  12.022161       NaN  0.236570       NaN
       swap_from_greedy_a_trace      gls_map               3.538724       NaN   6.000079       NaN  0.090176       NaN
                                     gsp                   3.818730       NaN   6.528719       NaN  0.104119       NaN
                                     historical_tod_mean   3.724795       NaN   6.657611       NaN  0.106678       NaN
                                     neighbor_average      7.886048       NaN  12.022161       NaN  0.236570       NaN
       swap_from_scenario_average    gls_map               3.542772       NaN   6.040368       NaN  0.090565       NaN
                                     gsp                   3.820459       NaN   6.560788       NaN  0.104808       NaN
                                     historical_tod_mean   3.738321       NaN   6.685997       NaN  0.107203       NaN
                                     neighbor_average      7.780198       NaN  11.897684       NaN  0.233899       NaN
       swap_from_scenario_cvar       gls_map               3.431051       NaN   5.958430       NaN  0.089710       NaN
                                     gsp                   3.788320       NaN   6.567357       NaN  0.104698       NaN
                                     historical_tod_mean   3.735141       NaN   6.688026       NaN  0.107186       NaN
                                     neighbor_average      7.928491       NaN  12.179093       NaN  0.238066       NaN
       top_variance                  gls_map               3.566144       NaN   6.113872       NaN  0.087864       NaN
                                     gsp                   3.555089       NaN   6.193709       NaN  0.090004       NaN
                                     historical_tod_mean   3.500420       NaN   6.316944       NaN  0.093102       NaN
                                     neighbor_average     12.118653       NaN  18.505255       NaN  0.235542       NaN
0.2    best_random_by_trace          gls_map               3.579509       NaN   6.098548       NaN  0.094512       NaN
                                     gsp                   3.802882       NaN   6.579440       NaN  0.106480       NaN
                                     historical_tod_mean   3.722318       NaN   6.682861       NaN  0.108806       NaN
                                     neighbor_average      8.064821       NaN  12.486748       NaN  0.248103       NaN
       best_random_by_validation     gls_map               3.312888       NaN   5.558027       NaN  0.083881       NaN
                                     gsp                   3.651245       NaN   6.327904       NaN  0.100330       NaN
                                     historical_tod_mean   3.587723       NaN   6.444051       NaN  0.102109       NaN
                                     neighbor_average      7.967789       NaN  11.719992       NaN  0.200407       NaN
       coverage                      gls_map               3.572267       NaN   6.201344       NaN  0.093899       NaN
                                     gsp                   3.845443       NaN   6.675443       NaN  0.105452       NaN
                                     historical_tod_mean   3.779825       NaN   6.832719       NaN  0.110314       NaN
                                     neighbor_average      7.760493       NaN  11.758350       NaN  0.218955       NaN
       degree                        gls_map               3.985491       NaN   6.842466       NaN  0.109127       NaN
                                     gsp                   3.941190       NaN   6.784815       NaN  0.110450       NaN
                                     historical_tod_mean   3.810485       NaN   6.774895       NaN  0.109839       NaN
                                     neighbor_average      8.213894       NaN  12.615446       NaN  0.228069       NaN
       greedy_a_trace                gls_map               3.287049       NaN   5.536901       NaN  0.086159       NaN
                                     gsp                   3.810898       NaN   6.481036       NaN  0.106375       NaN
                                     historical_tod_mean   3.719108       NaN   6.605134       NaN  0.108492       NaN
                                     neighbor_average      8.014979       NaN  12.214289       NaN  0.246212       NaN
       greedy_d_logdet               gls_map               4.497865       NaN   6.914332       NaN  0.124734       NaN
                                     gsp                   3.970788       NaN   6.714189       NaN  0.115843       NaN
                                     historical_tod_mean   3.745076       NaN   6.660967       NaN  0.111526       NaN
                                     neighbor_average      8.684093       NaN  13.856008       NaN  0.293193       NaN
       multistart_swap_by_validation gls_map               3.312990       NaN   5.542580       NaN  0.087165       NaN
                                     gsp                   3.707200       NaN   6.465683       NaN  0.105181       NaN
                                     historical_tod_mean   3.695204       NaN   6.615560       NaN  0.108082       NaN
                                     neighbor_average      7.773115       NaN  12.004633       NaN  0.243501       NaN
       random                        gls_map               3.457342  0.085520   5.930593  0.155423  0.088379  0.003399
                                     gsp                   3.768447  0.064664   6.505564  0.104651  0.100991  0.003349
                                     historical_tod_mean   3.723490  0.058904   6.662289  0.100707  0.105736  0.002854
                                     neighbor_average      7.881373  0.185571  12.051401  0.318629  0.214068  0.012125
       rcss_selected                 gls_map               3.312990       NaN   5.542580       NaN  0.087165       NaN
                                     gsp                   3.707200       NaN   6.465683       NaN  0.105181       NaN
                                     historical_tod_mean   3.695204       NaN   6.615560       NaN  0.108082       NaN
                                     neighbor_average      7.773115       NaN  12.004633       NaN  0.243501       NaN
       robust_coverage_cvar          gls_map               3.294873       NaN   5.644127       NaN  0.084686       NaN
                                     gsp                   3.780614       NaN   6.448258       NaN  0.102770       NaN
                                     historical_tod_mean   3.684432       NaN   6.580828       NaN  0.105639       NaN
                                     neighbor_average      7.938196       NaN  12.237355       NaN  0.228713       NaN
       scenario_average_a_trace      gls_map               3.354427       NaN   5.746569       NaN  0.088841       NaN
                                     gsp                   3.803937       NaN   6.560833       NaN  0.105786       NaN
                                     historical_tod_mean   3.732332       NaN   6.661319       NaN  0.107600       NaN
                                     neighbor_average      7.547402       NaN  11.612380       NaN  0.224250       NaN
       scenario_cvar_a_trace         gls_map               3.283775       NaN   5.643793       NaN  0.084786       NaN
                                     gsp                   3.781398       NaN   6.454541       NaN  0.102468       NaN
                                     historical_tod_mean   3.699611       NaN   6.602652       NaN  0.106391       NaN
                                     neighbor_average      7.703762       NaN  11.879124       NaN  0.226588       NaN
       swap_from_best_random_trace   gls_map               3.371649       NaN   5.509603       NaN  0.085443       NaN
                                     gsp                   3.764950       NaN   6.369999       NaN  0.103696       NaN
                                     historical_tod_mean   3.677084       NaN   6.516993       NaN  0.106567       NaN
                                     neighbor_average      7.832817       NaN  11.932416       NaN  0.238015       NaN
       swap_from_greedy_a_trace      gls_map               3.338652       NaN   5.480060       NaN  0.085452       NaN
                                     gsp                   3.766737       NaN   6.387748       NaN  0.104805       NaN
                                     historical_tod_mean   3.704915       NaN   6.527787       NaN  0.106996       NaN
                                     neighbor_average      7.797705       NaN  12.051850       NaN  0.239818       NaN
       swap_from_scenario_average    gls_map               3.332432       NaN   5.536239       NaN  0.085107       NaN
                                     gsp                   3.760984       NaN   6.458432       NaN  0.104238       NaN
                                     historical_tod_mean   3.722901       NaN   6.601347       NaN  0.107061       NaN
                                     neighbor_average      7.612990       NaN  11.851051       NaN  0.236024       NaN
       swap_from_scenario_cvar       gls_map               3.294124       NaN   5.551064       NaN  0.086424       NaN
                                     gsp                   3.774516       NaN   6.466412       NaN  0.104766       NaN
                                     historical_tod_mean   3.735588       NaN   6.617880       NaN  0.108116       NaN
                                     neighbor_average      7.808849       NaN  12.241041       NaN  0.246645       NaN
       top_variance                  gls_map               3.342097       NaN   5.780595       NaN  0.078151       NaN
                                     gsp                   3.457924       NaN   6.030479       NaN  0.082914       NaN
                                     historical_tod_mean   3.371221       NaN   6.136962       NaN  0.085791       NaN
                                     neighbor_average     10.641600       NaN  16.614858       NaN  0.201928       NaN
0.3    best_random_by_trace          gls_map               3.385613       NaN   5.778878       NaN  0.088143       NaN
                                     gsp                   3.847818       NaN   6.603862       NaN  0.105442       NaN
                                     historical_tod_mean   3.812369       NaN   6.769217       NaN  0.111275       NaN
                                     neighbor_average      7.525113       NaN  11.558051       NaN  0.227291       NaN
       best_random_by_validation     gls_map               3.065784       NaN   5.264431       NaN  0.073679       NaN
                                     gsp                   3.599622       NaN   6.233700       NaN  0.091816       NaN
                                     historical_tod_mean   3.576923       NaN   6.431941       NaN  0.097634       NaN
                                     neighbor_average      7.936715       NaN  11.779321       NaN  0.192876       NaN
       coverage                      gls_map               3.297751       NaN   5.794088       NaN  0.086789       NaN
                                     gsp                   3.758100       NaN   6.611331       NaN  0.103130       NaN
                                     historical_tod_mean   3.727096       NaN   6.802686       NaN  0.109582       NaN
                                     neighbor_average      7.706647       NaN  11.502882       NaN  0.212847       NaN
       degree                        gls_map               3.857218       NaN   6.614667       NaN  0.103433       NaN
                                     gsp                   3.873994       NaN   6.691558       NaN  0.107702       NaN
                                     historical_tod_mean   3.769260       NaN   6.757507       NaN  0.109774       NaN
                                     neighbor_average      9.216723       NaN  14.013494       NaN  0.269832       NaN
       greedy_a_trace                gls_map               3.180404       NaN   5.168195       NaN  0.082198       NaN
                                     gsp                   3.797785       NaN   6.371114       NaN  0.105930       NaN
                                     historical_tod_mean   3.694407       NaN   6.509121       NaN  0.108769       NaN
                                     neighbor_average      7.548713       NaN  11.392503       NaN  0.230698       NaN
       greedy_d_logdet               gls_map               3.814191       NaN   6.102293       NaN  0.105160       NaN
                                     gsp                   3.816256       NaN   6.572760       NaN  0.111987       NaN
                                     historical_tod_mean   3.678299       NaN   6.617146       NaN  0.111814       NaN
                                     neighbor_average      8.686176       NaN  13.674623       NaN  0.292755       NaN
       multistart_swap_by_validation gls_map               3.139969       NaN   5.235420       NaN  0.082358       NaN
                                     gsp                   3.655787       NaN   6.364897       NaN  0.104020       NaN
                                     historical_tod_mean   3.643973       NaN   6.541231       NaN  0.108054       NaN
                                     neighbor_average      7.604242       NaN  11.527666       NaN  0.232494       NaN
       random                        gls_map               3.309265  0.094197   5.702911  0.175821  0.084107  0.003605
                                     gsp                   3.746462  0.080248   6.487011  0.118841  0.100220  0.003363
                                     historical_tod_mean   3.718992  0.076095   6.667603  0.116878  0.105726  0.003360
                                     neighbor_average      7.747547  0.206830  11.904018  0.367361  0.207340  0.012350
       rcss_selected                 gls_map               3.139969       NaN   5.235420       NaN  0.082358       NaN
                                     gsp                   3.655787       NaN   6.364897       NaN  0.104020       NaN
                                     historical_tod_mean   3.643973       NaN   6.541231       NaN  0.108054       NaN
                                     neighbor_average      7.604242       NaN  11.527666       NaN  0.232494       NaN
       robust_coverage_cvar          gls_map               3.190348       NaN   5.470888       NaN  0.082714       NaN
                                     gsp                   3.787279       NaN   6.492390       NaN  0.103710       NaN
                                     historical_tod_mean   3.736763       NaN   6.661651       NaN  0.109342       NaN
                                     neighbor_average      7.698326       NaN  11.844632       NaN  0.231496       NaN
       scenario_average_a_trace      gls_map               3.246977       NaN   5.623460       NaN  0.085805       NaN
                                     gsp                   3.821117       NaN   6.592965       NaN  0.106024       NaN
                                     historical_tod_mean   3.735381       NaN   6.707829       NaN  0.109507       NaN
                                     neighbor_average      7.646869       NaN  11.668815       NaN  0.228648       NaN
       scenario_cvar_a_trace         gls_map               3.185571       NaN   5.433664       NaN  0.081711       NaN
                                     gsp                   3.767646       NaN   6.451097       NaN  0.102754       NaN
                                     historical_tod_mean   3.702795       NaN   6.619958       NaN  0.107932       NaN
                                     neighbor_average      7.812953       NaN  12.260536       NaN  0.236635       NaN
       swap_from_best_random_trace   gls_map               3.218961       NaN   5.249039       NaN  0.083054       NaN
                                     gsp                   3.785685       NaN   6.419931       NaN  0.106176       NaN
                                     historical_tod_mean   3.694025       NaN   6.554955       NaN  0.109164       NaN
                                     neighbor_average      7.730328       NaN  11.858754       NaN  0.240572       NaN
       swap_from_greedy_a_trace      gls_map               3.280024       NaN   5.331959       NaN  0.084904       NaN
                                     gsp                   3.797842       NaN   6.452862       NaN  0.106782       NaN
                                     historical_tod_mean   3.716670       NaN   6.590972       NaN  0.109494       NaN
                                     neighbor_average      7.561723       NaN  11.616240       NaN  0.237175       NaN
       swap_from_scenario_average    gls_map               3.253141       NaN   5.276978       NaN  0.083714       NaN
                                     gsp                   3.740164       NaN   6.358690       NaN  0.103838       NaN
                                     historical_tod_mean   3.663457       NaN   6.502336       NaN  0.107042       NaN
                                     neighbor_average      7.539485       NaN  11.494051       NaN  0.233766       NaN
       swap_from_scenario_cvar       gls_map               3.221731       NaN   5.205153       NaN  0.081277       NaN
                                     gsp                   3.767917       NaN   6.309543       NaN  0.102805       NaN
                                     historical_tod_mean   3.649774       NaN   6.447953       NaN  0.106201       NaN
                                     neighbor_average      7.576196       NaN  11.637573       NaN  0.232609       NaN
       top_variance                  gls_map               3.135040       NaN   5.532687       NaN  0.071701       NaN
                                     gsp                   3.360399       NaN   5.919157       NaN  0.078863       NaN
                                     historical_tod_mean   3.252722       NaN   5.986999       NaN  0.080464       NaN
                                     neighbor_average     10.110842       NaN  15.552207       NaN  0.191230       NaN
```

## Best method per budget-layout row

```
 budget             layout_type  method      mae     rmse
    0.1 swap_from_scenario_cvar gls_map 3.431051 5.958430
    0.2                  random gls_map 3.259542 5.652803
    0.3                  random gls_map 3.065784 5.264431
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.146465      0.164237 648
    gsp   condition_number     0.148362      0.151898 648
    gsp information_logdet    -0.170643     -0.211241 648
gls_map    posterior_trace     0.821020      0.859291 648
gls_map   condition_number     0.829252      0.862335 648
gls_map information_logdet    -0.772033     -0.806039 648
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv