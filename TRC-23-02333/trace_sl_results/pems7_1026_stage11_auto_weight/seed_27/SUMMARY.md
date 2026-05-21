---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-06-13, 2012-06-04
Test days: 2012-05-22, 2012-06-21
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.614211       NaN   6.038732       NaN  0.091375       NaN
                                     gsp                   4.054626       NaN   6.854608       NaN  0.107225       NaN
                                     historical_tod_mean   4.053362       NaN   6.968145       NaN  0.108911       NaN
                                     neighbor_average      7.719568       NaN  11.900380       NaN  0.208032       NaN
       best_random_by_validation     gls_map               3.598236       NaN   6.058712       NaN  0.089030       NaN
                                     gsp                   4.022388       NaN   6.820063       NaN  0.105534       NaN
                                     historical_tod_mean   4.035778       NaN   6.949227       NaN  0.107888       NaN
                                     neighbor_average      7.791728       NaN  11.815436       NaN  0.201847       NaN
       coverage                      gls_map               3.673549       NaN   6.178446       NaN  0.092955       NaN
                                     gsp                   4.034739       NaN   6.905380       NaN  0.107273       NaN
                                     historical_tod_mean   4.082774       NaN   7.009908       NaN  0.109177       NaN
                                     neighbor_average      7.999741       NaN  11.897894       NaN  0.208966       NaN
       degree                        gls_map               4.141659       NaN   6.773876       NaN  0.099384       NaN
                                     gsp                   4.166702       NaN   6.908902       NaN  0.104169       NaN
                                     historical_tod_mean   4.001833       NaN   6.892578       NaN  0.105547       NaN
                                     neighbor_average      9.600909       NaN  13.796349       NaN  0.236609       NaN
       greedy_a_trace                gls_map               3.485319       NaN   5.770720       NaN  0.087045       NaN
                                     gsp                   4.015598       NaN   6.793748       NaN  0.106393       NaN
                                     historical_tod_mean   4.027016       NaN   6.914202       NaN  0.108203       NaN
                                     neighbor_average      7.795661       NaN  11.900217       NaN  0.219344       NaN
       greedy_d_logdet               gls_map               4.119203       NaN   6.531779       NaN  0.102754       NaN
                                     gsp                   4.019085       NaN   6.812693       NaN  0.107636       NaN
                                     historical_tod_mean   3.978958       NaN   6.874025       NaN  0.107326       NaN
                                     neighbor_average      8.572367       NaN  13.113435       NaN  0.254726       NaN
       multistart_swap_by_validation gls_map               3.482280       NaN   5.837555       NaN  0.087889       NaN
                                     gsp                   4.040190       NaN   6.828900       NaN  0.106565       NaN
                                     historical_tod_mean   4.052499       NaN   6.951962       NaN  0.108531       NaN
                                     neighbor_average      7.764586       NaN  11.658580       NaN  0.209143       NaN
       random                        gls_map               3.654839  0.038945   6.140407  0.070529  0.090835  0.001376
                                     gsp                   4.060709  0.023361   6.864577  0.032887  0.105887  0.000975
                                     historical_tod_mean   4.069852  0.020785   6.986879  0.032173  0.108482  0.000772
                                     neighbor_average      7.924710  0.140724  12.139456  0.186896  0.208619  0.004512
       rcss_selected                 gls_map               3.485319       NaN   5.770720       NaN  0.087045       NaN
                                     gsp                   4.015598       NaN   6.793748       NaN  0.106393       NaN
                                     historical_tod_mean   4.027016       NaN   6.914202       NaN  0.108203       NaN
                                     neighbor_average      7.795661       NaN  11.900217       NaN  0.219344       NaN
       robust_coverage_cvar          gls_map               3.629149       NaN   6.025369       NaN  0.090612       NaN
                                     gsp                   4.020134       NaN   6.838268       NaN  0.106243       NaN
                                     historical_tod_mean   4.031503       NaN   6.946196       NaN  0.107685       NaN
                                     neighbor_average      8.114416       NaN  12.151186       NaN  0.218122       NaN
       scenario_average_a_trace      gls_map               3.671848       NaN   6.056807       NaN  0.091260       NaN
                                     gsp                   4.026475       NaN   6.808913       NaN  0.106127       NaN
                                     historical_tod_mean   4.021654       NaN   6.904755       NaN  0.106854       NaN
                                     neighbor_average      8.221907       NaN  12.113064       NaN  0.222198       NaN
       scenario_cvar_a_trace         gls_map               3.656219       NaN   6.100342       NaN  0.090894       NaN
                                     gsp                   4.013632       NaN   6.816229       NaN  0.104927       NaN
                                     historical_tod_mean   4.025659       NaN   6.922844       NaN  0.107057       NaN
                                     neighbor_average      8.230516       NaN  12.225964       NaN  0.216391       NaN
       swap_from_best_random_trace   gls_map               3.486371       NaN   5.849782       NaN  0.087071       NaN
                                     gsp                   4.033929       NaN   6.814182       NaN  0.106178       NaN
                                     historical_tod_mean   4.036838       NaN   6.936513       NaN  0.108235       NaN
                                     neighbor_average      7.618427       NaN  11.714015       NaN  0.211406       NaN
       swap_from_greedy_a_trace      gls_map               3.457469       NaN   5.724474       NaN  0.085960       NaN
                                     gsp                   4.000215       NaN   6.760678       NaN  0.105822       NaN
                                     historical_tod_mean   4.005757       NaN   6.878625       NaN  0.107542       NaN
                                     neighbor_average      7.743612       NaN  11.869063       NaN  0.218268       NaN
       swap_from_scenario_average    gls_map               3.527182       NaN   5.813729       NaN  0.086065       NaN
                                     gsp                   4.023254       NaN   6.741046       NaN  0.104376       NaN
                                     historical_tod_mean   3.998642       NaN   6.851451       NaN  0.105832       NaN
                                     neighbor_average      8.089070       NaN  12.000836       NaN  0.218816       NaN
       swap_from_scenario_cvar       gls_map               3.521787       NaN   5.841942       NaN  0.086813       NaN
                                     gsp                   3.988474       NaN   6.747230       NaN  0.103546       NaN
                                     historical_tod_mean   3.993940       NaN   6.860303       NaN  0.105878       NaN
                                     neighbor_average      7.983745       NaN  11.980157       NaN  0.214621       NaN
       top_variance                  gls_map               3.646532       NaN   6.206181       NaN  0.088772       NaN
                                     gsp                   3.863384       NaN   6.611236       NaN  0.097506       NaN
                                     historical_tod_mean   3.874968       NaN   6.714410       NaN  0.099165       NaN
                                     neighbor_average     10.680808       NaN  16.064565       NaN  0.215063       NaN
       validation_swap_selected      gls_map               3.512877       NaN   5.878017       NaN  0.088550       NaN
                                     gsp                   3.980438       NaN   6.788921       NaN  0.105963       NaN
                                     historical_tod_mean   4.004282       NaN   6.892722       NaN  0.107137       NaN
                                     neighbor_average      7.913016       NaN  11.809133       NaN  0.210039       NaN
0.2    best_random_by_trace          gls_map               3.395908       NaN   5.709578       NaN  0.083153       NaN
                                     gsp                   4.061806       NaN   6.850563       NaN  0.106135       NaN
                                     historical_tod_mean   4.075023       NaN   6.995308       NaN  0.108754       NaN
                                     neighbor_average      7.602948       NaN  11.869285       NaN  0.203979       NaN
       best_random_by_validation     gls_map               3.325597       NaN   5.531244       NaN  0.080803       NaN
                                     gsp                   4.031902       NaN   6.766982       NaN  0.103512       NaN
                                     historical_tod_mean   4.029330       NaN   6.901293       NaN  0.106049       NaN
                                     neighbor_average      7.402100       NaN  11.471202       NaN  0.187994       NaN
       coverage                      gls_map               3.394153       NaN   5.700633       NaN  0.084673       NaN
                                     gsp                   4.071313       NaN   6.922656       NaN  0.107639       NaN
                                     historical_tod_mean   4.096530       NaN   7.052829       NaN  0.110316       NaN
                                     neighbor_average      7.508604       NaN  11.507105       NaN  0.198939       NaN
       degree                        gls_map               4.031832       NaN   6.608369       NaN  0.096114       NaN
                                     gsp                   4.092702       NaN   6.805807       NaN  0.101709       NaN
                                     historical_tod_mean   3.969811       NaN   6.849343       NaN  0.103725       NaN
                                     neighbor_average      9.758473       NaN  13.926108       NaN  0.223103       NaN
       greedy_a_trace                gls_map               3.104683       NaN   5.085995       NaN  0.075976       NaN
                                     gsp                   3.933699       NaN   6.660171       NaN  0.103722       NaN
                                     historical_tod_mean   3.936620       NaN   6.788186       NaN  0.105851       NaN
                                     neighbor_average      7.520967       NaN  11.475915       NaN  0.212283       NaN
       greedy_d_logdet               gls_map               3.590908       NaN   5.805773       NaN  0.090511       NaN
                                     gsp                   3.960823       NaN   6.708127       NaN  0.105742       NaN
                                     historical_tod_mean   3.942149       NaN   6.831844       NaN  0.107430       NaN
                                     neighbor_average      8.096938       NaN  12.619253       NaN  0.241185       NaN
       multistart_swap_by_validation gls_map               3.191836       NaN   5.341094       NaN  0.078625       NaN
                                     gsp                   3.979312       NaN   6.754565       NaN  0.104450       NaN
                                     historical_tod_mean   3.971153       NaN   6.882323       NaN  0.106841       NaN
                                     neighbor_average      7.469080       NaN  11.404390       NaN  0.199150       NaN
       random                        gls_map               3.388325  0.039350   5.694247  0.082623  0.083151  0.001586
                                     gsp                   4.065685  0.028621   6.849904  0.046986  0.105506  0.001249
                                     historical_tod_mean   4.069489  0.028447   6.986322  0.046368  0.108408  0.001253
                                     neighbor_average      7.585639  0.106165  11.758866  0.166166  0.198525  0.004546
       rcss_selected                 gls_map               3.089166       NaN   5.065123       NaN  0.075877       NaN
                                     gsp                   3.921527       NaN   6.641931       NaN  0.103647       NaN
                                     historical_tod_mean   3.923240       NaN   6.770558       NaN  0.105600       NaN
                                     neighbor_average      7.554004       NaN  11.614586       NaN  0.214971       NaN
       robust_coverage_cvar          gls_map               3.365383       NaN   5.619557       NaN  0.083885       NaN
                                     gsp                   3.961952       NaN   6.776492       NaN  0.104893       NaN
                                     historical_tod_mean   3.979107       NaN   6.909786       NaN  0.107363       NaN
                                     neighbor_average      7.823990       NaN  12.026530       NaN  0.210675       NaN
       scenario_average_a_trace      gls_map               3.384984       NaN   5.596527       NaN  0.084430       NaN
                                     gsp                   3.986423       NaN   6.758318       NaN  0.105714       NaN
                                     historical_tod_mean   3.991140       NaN   6.885178       NaN  0.107322       NaN
                                     neighbor_average      7.940410       NaN  12.079880       NaN  0.221384       NaN
       scenario_cvar_a_trace         gls_map               3.325389       NaN   5.536298       NaN  0.082342       NaN
                                     gsp                   3.935237       NaN   6.714566       NaN  0.103778       NaN
                                     historical_tod_mean   3.951899       NaN   6.846881       NaN  0.106249       NaN
                                     neighbor_average      7.820033       NaN  11.931148       NaN  0.210116       NaN
       swap_from_best_random_trace   gls_map               3.285323       NaN   5.516745       NaN  0.079745       NaN
                                     gsp                   4.046720       NaN   6.828283       NaN  0.106051       NaN
                                     historical_tod_mean   4.059666       NaN   6.971714       NaN  0.108383       NaN
                                     neighbor_average      7.483742       NaN  11.597246       NaN  0.202889       NaN
       swap_from_greedy_a_trace      gls_map               3.089166       NaN   5.065123       NaN  0.075877       NaN
                                     gsp                   3.921527       NaN   6.641931       NaN  0.103647       NaN
                                     historical_tod_mean   3.923240       NaN   6.770558       NaN  0.105600       NaN
                                     neighbor_average      7.554004       NaN  11.614586       NaN  0.214971       NaN
       swap_from_scenario_average    gls_map               3.257650       NaN   5.348181       NaN  0.079891       NaN
                                     gsp                   3.957430       NaN   6.686146       NaN  0.103935       NaN
                                     historical_tod_mean   3.958867       NaN   6.823798       NaN  0.106063       NaN
                                     neighbor_average      7.666698       NaN  11.706213       NaN  0.213928       NaN
       swap_from_scenario_cvar       gls_map               3.217972       NaN   5.311010       NaN  0.078869       NaN
                                     gsp                   3.914582       NaN   6.642933       NaN  0.102614       NaN
                                     historical_tod_mean   3.923326       NaN   6.775070       NaN  0.104994       NaN
                                     neighbor_average      7.583903       NaN  11.492156       NaN  0.205753       NaN
       top_variance                  gls_map               3.449596       NaN   5.821693       NaN  0.080386       NaN
                                     gsp                   3.745932       NaN   6.405933       NaN  0.091639       NaN
                                     historical_tod_mean   3.736777       NaN   6.517782       NaN  0.093374       NaN
                                     neighbor_average      9.627209       NaN  14.865798       NaN  0.192441       NaN
       validation_swap_selected      gls_map               3.093312       NaN   5.069548       NaN  0.075854       NaN
                                     gsp                   3.915711       NaN   6.635339       NaN  0.103343       NaN
                                     historical_tod_mean   3.912483       NaN   6.764522       NaN  0.105382       NaN
                                     neighbor_average      7.572423       NaN  11.623808       NaN  0.214469       NaN
0.3    best_random_by_trace          gls_map               3.253162       NaN   5.529634       NaN  0.081331       NaN
                                     gsp                   4.082354       NaN   6.894443       NaN  0.108459       NaN
                                     historical_tod_mean   4.091914       NaN   7.038713       NaN  0.110922       NaN
                                     neighbor_average      7.540767       NaN  11.658727       NaN  0.206348       NaN
       best_random_by_validation     gls_map               3.150500       NaN   5.340188       NaN  0.076578       NaN
                                     gsp                   4.016084       NaN   6.804795       NaN  0.104150       NaN
                                     historical_tod_mean   4.007359       NaN   6.940402       NaN  0.106766       NaN
                                     neighbor_average      7.366450       NaN  11.406020       NaN  0.192158       NaN
       coverage                      gls_map               3.274867       NaN   5.490679       NaN  0.081420       NaN
                                     gsp                   4.118693       NaN   6.980982       NaN  0.109174       NaN
                                     historical_tod_mean   4.153380       NaN   7.124434       NaN  0.112093       NaN
                                     neighbor_average      7.426511       NaN  11.596784       NaN  0.199862       NaN
       degree                        gls_map               3.892893       NaN   6.461603       NaN  0.093233       NaN
                                     gsp                   3.948434       NaN   6.662595       NaN  0.099018       NaN
                                     historical_tod_mean   3.864458       NaN   6.742313       NaN  0.101031       NaN
                                     neighbor_average      8.204882       NaN  12.688563       NaN  0.212609       NaN
       greedy_a_trace                gls_map               2.867515       NaN   4.679955       NaN  0.070419       NaN
                                     gsp                   3.898276       NaN   6.615338       NaN  0.103481       NaN
                                     historical_tod_mean   3.906666       NaN   6.763980       NaN  0.106052       NaN
                                     neighbor_average      7.269369       NaN  11.186768       NaN  0.208239       NaN
       greedy_d_logdet               gls_map               3.169713       NaN   5.170459       NaN  0.079393       NaN
                                     gsp                   3.887952       NaN   6.616537       NaN  0.104394       NaN
                                     historical_tod_mean   3.883573       NaN   6.764815       NaN  0.107012       NaN
                                     neighbor_average      7.836559       NaN  12.246880       NaN  0.232473       NaN
       multistart_swap_by_validation gls_map               3.020806       NaN   5.070304       NaN  0.072561       NaN
                                     gsp                   3.956567       NaN   6.685020       NaN  0.102233       NaN
                                     historical_tod_mean   3.943002       NaN   6.826523       NaN  0.104687       NaN
                                     neighbor_average      7.266334       NaN  11.156369       NaN  0.191015       NaN
       random                        gls_map               3.197008  0.038726   5.386519  0.077739  0.077984  0.001386
                                     gsp                   4.064018  0.033390   6.849895  0.053658  0.105519  0.001409
                                     historical_tod_mean   4.068982  0.034428   6.992862  0.052871  0.108557  0.001330
                                     neighbor_average      7.412873  0.091025  11.574004  0.158683  0.194076  0.004433
       rcss_selected                 gls_map               2.844299       NaN   4.639340       NaN  0.069959       NaN
                                     gsp                   3.876173       NaN   6.588691       NaN  0.103056       NaN
                                     historical_tod_mean   3.882756       NaN   6.737557       NaN  0.105535       NaN
                                     neighbor_average      7.282821       NaN  11.254824       NaN  0.208891       NaN
       robust_coverage_cvar          gls_map               3.217619       NaN   5.379445       NaN  0.080404       NaN
                                     gsp                   3.938182       NaN   6.739809       NaN  0.105470       NaN
                                     historical_tod_mean   3.952225       NaN   6.879000       NaN  0.107914       NaN
                                     neighbor_average      7.753476       NaN  12.143885       NaN  0.212323       NaN
       scenario_average_a_trace      gls_map               3.155809       NaN   5.291807       NaN  0.079021       NaN
                                     gsp                   3.937868       NaN   6.730406       NaN  0.105589       NaN
                                     historical_tod_mean   3.954823       NaN   6.871211       NaN  0.107693       NaN
                                     neighbor_average      7.637084       NaN  11.857221       NaN  0.216386       NaN
       scenario_cvar_a_trace         gls_map               3.199838       NaN   5.386388       NaN  0.080265       NaN
                                     gsp                   3.922716       NaN   6.707693       NaN  0.105186       NaN
                                     historical_tod_mean   3.939597       NaN   6.851285       NaN  0.107654       NaN
                                     neighbor_average      7.873105       NaN  12.327177       NaN  0.217527       NaN
       swap_from_best_random_trace   gls_map               3.114160       NaN   5.260944       NaN  0.077411       NaN
                                     gsp                   4.010080       NaN   6.782786       NaN  0.106674       NaN
                                     historical_tod_mean   4.016278       NaN   6.926648       NaN  0.108896       NaN
                                     neighbor_average      7.427543       NaN  11.368757       NaN  0.204375       NaN
       swap_from_greedy_a_trace      gls_map               2.844299       NaN   4.639340       NaN  0.069959       NaN
                                     gsp                   3.876173       NaN   6.588691       NaN  0.103056       NaN
                                     historical_tod_mean   3.882756       NaN   6.737557       NaN  0.105535       NaN
                                     neighbor_average      7.282821       NaN  11.254824       NaN  0.208891       NaN
       swap_from_scenario_average    gls_map               3.026857       NaN   4.999622       NaN  0.075034       NaN
                                     gsp                   3.905793       NaN   6.661569       NaN  0.104753       NaN
                                     historical_tod_mean   3.925135       NaN   6.804073       NaN  0.106873       NaN
                                     neighbor_average      7.499782       NaN  11.614118       NaN  0.213334       NaN
       swap_from_scenario_cvar       gls_map               3.068363       NaN   5.137935       NaN  0.076135       NaN
                                     gsp                   3.904041       NaN   6.644773       NaN  0.103848       NaN
                                     historical_tod_mean   3.918589       NaN   6.790606       NaN  0.106500       NaN
                                     neighbor_average      7.593978       NaN  11.883777       NaN  0.213538       NaN
       top_variance                  gls_map               3.220360       NaN   5.435891       NaN  0.072416       NaN
                                     gsp                   3.592830       NaN   6.164236       NaN  0.084783       NaN
                                     historical_tod_mean   3.564883       NaN   6.266571       NaN  0.086098       NaN
                                     neighbor_average      9.280550       NaN  14.413128       NaN  0.181046       NaN
       validation_swap_selected      gls_map               2.838366       NaN   4.643751       NaN  0.070160       NaN
                                     gsp                   3.865237       NaN   6.590751       NaN  0.103262       NaN
                                     historical_tod_mean   3.874489       NaN   6.738752       NaN  0.105681       NaN
                                     neighbor_average      7.276644       NaN  11.234500       NaN  0.208410       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 3.457469 5.724474
    0.2 swap_from_greedy_a_trace gls_map 3.089166 5.065123
    0.3 validation_swap_selected gls_map 2.838366 4.643751
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.073928      0.025470 351
    gsp   condition_number     0.073563     -0.023857 351
    gsp information_logdet    -0.088728     -0.024061 351
gls_map    posterior_trace     0.952016      0.939221 351
gls_map   condition_number     0.831970      0.900099 351
gls_map information_logdet    -0.924207     -0.900554 351
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv