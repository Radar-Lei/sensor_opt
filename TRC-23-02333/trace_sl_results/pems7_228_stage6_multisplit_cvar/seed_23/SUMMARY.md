---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-30, 2012-06-05
Test days: 2012-05-23, 2012-05-31
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.336160       NaN   5.766470       NaN  0.084233       NaN
                                     gsp                   3.465743       NaN   6.030425       NaN  0.090991       NaN
                                     historical_tod_mean   3.440807       NaN   6.094910       NaN  0.093466       NaN
                                     neighbor_average      7.951682       NaN  11.988635       NaN  0.203592       NaN
       best_random_by_validation     gls_map               3.344214       NaN   5.756070       NaN  0.083778       NaN
                                     gsp                   3.432909       NaN   6.007243       NaN  0.089743       NaN
                                     historical_tod_mean   3.416949       NaN   6.074159       NaN  0.092700       NaN
                                     neighbor_average      7.882738       NaN  11.717679       NaN  0.199281       NaN
       coverage                      gls_map               3.617199       NaN   6.114329       NaN  0.090125       NaN
                                     gsp                   3.545839       NaN   6.122734       NaN  0.092859       NaN
                                     historical_tod_mean   3.465676       NaN   6.163915       NaN  0.095593       NaN
                                     neighbor_average      8.293413       NaN  12.667693       NaN  0.224808       NaN
       degree                        gls_map               3.827168       NaN   6.549605       NaN  0.100531       NaN
                                     gsp                   3.590605       NaN   6.167595       NaN  0.093317       NaN
                                     historical_tod_mean   3.488723       NaN   6.160549       NaN  0.095548       NaN
                                     neighbor_average      8.992371       NaN  13.934392       NaN  0.249525       NaN
       greedy_a_trace                gls_map               3.324124       NaN   5.821368       NaN  0.086581       NaN
                                     gsp                   3.536710       NaN   6.138972       NaN  0.095107       NaN
                                     historical_tod_mean   3.502231       NaN   6.166403       NaN  0.096072       NaN
                                     neighbor_average      7.993990       NaN  12.180657       NaN  0.230218       NaN
       greedy_d_logdet               gls_map               4.042355       NaN   6.479569       NaN  0.099304       NaN
                                     gsp                   3.563896       NaN   6.077928       NaN  0.093959       NaN
                                     historical_tod_mean   3.455003       NaN   6.095914       NaN  0.095330       NaN
                                     neighbor_average      8.405508       NaN  13.600856       NaN  0.262099       NaN
       multistart_swap_by_validation gls_map               3.236611       NaN   5.602956       NaN  0.082243       NaN
                                     gsp                   3.506962       NaN   6.095111       NaN  0.093399       NaN
                                     historical_tod_mean   3.484010       NaN   6.162905       NaN  0.095770       NaN
                                     neighbor_average      7.769184       NaN  11.903214       NaN  0.219003       NaN
       random                        gls_map               3.473523  0.070109   5.976519  0.118585  0.088810  0.002821
                                     gsp                   3.510215  0.041408   6.103007  0.060822  0.092760  0.002053
                                     historical_tod_mean   3.463522  0.034435   6.140741  0.056023  0.094678  0.001455
                                     neighbor_average      8.095600  0.289486  12.334194  0.445259  0.214474  0.010345
       scenario_average_a_trace      gls_map               3.352319       NaN   5.869517       NaN  0.086349       NaN
                                     gsp                   3.522605       NaN   6.135316       NaN  0.094940       NaN
                                     historical_tod_mean   3.479790       NaN   6.153288       NaN  0.095385       NaN
                                     neighbor_average      8.253725       NaN  12.343324       NaN  0.228530       NaN
       scenario_cvar_a_trace         gls_map               3.319539       NaN   5.658896       NaN  0.082216       NaN
                                     gsp                   3.455147       NaN   5.961995       NaN  0.090819       NaN
                                     historical_tod_mean   3.379623       NaN   6.001472       NaN  0.092248       NaN
                                     neighbor_average      8.107499       NaN  12.060481       NaN  0.214817       NaN
       swap_from_best_random_trace   gls_map               3.262794       NaN   5.728334       NaN  0.085396       NaN
                                     gsp                   3.518816       NaN   6.118402       NaN  0.095316       NaN
                                     historical_tod_mean   3.487798       NaN   6.150618       NaN  0.095915       NaN
                                     neighbor_average      7.763036       NaN  11.898472       NaN  0.225868       NaN
       swap_from_greedy_a_trace      gls_map               3.233555       NaN   5.551065       NaN  0.080996       NaN
                                     gsp                   3.504165       NaN   6.049157       NaN  0.092958       NaN
                                     historical_tod_mean   3.457446       NaN   6.086370       NaN  0.093858       NaN
                                     neighbor_average      7.826616       NaN  11.815461       NaN  0.217096       NaN
       swap_from_scenario_average    gls_map               3.342801       NaN   5.795056       NaN  0.086433       NaN
                                     gsp                   3.532171       NaN   6.141449       NaN  0.094611       NaN
                                     historical_tod_mean   3.499956       NaN   6.197079       NaN  0.096673       NaN
                                     neighbor_average      7.778397       NaN  11.961844       NaN  0.224504       NaN
       swap_from_scenario_cvar       gls_map               3.338083       NaN   5.812128       NaN  0.086880       NaN
                                     gsp                   3.541547       NaN   6.134562       NaN  0.095433       NaN
                                     historical_tod_mean   3.492530       NaN   6.172378       NaN  0.096414       NaN
                                     neighbor_average      7.750463       NaN  11.885937       NaN  0.228247       NaN
       top_variance                  gls_map               3.455124       NaN   5.744759       NaN  0.081827       NaN
                                     gsp                   3.331382       NaN   5.699156       NaN  0.081902       NaN
                                     historical_tod_mean   3.225791       NaN   5.721267       NaN  0.083134       NaN
                                     neighbor_average     11.903845       NaN  18.173733       NaN  0.229595       NaN
0.2    best_random_by_trace          gls_map               3.334240       NaN   5.779349       NaN  0.086166       NaN
                                     gsp                   3.475616       NaN   6.033497       NaN  0.091825       NaN
                                     historical_tod_mean   3.446815       NaN   6.094475       NaN  0.094819       NaN
                                     neighbor_average      7.728178       NaN  12.142673       NaN  0.225827       NaN
       best_random_by_validation     gls_map               3.114057       NaN   5.428207       NaN  0.076061       NaN
                                     gsp                   3.375460       NaN   5.907046       NaN  0.085820       NaN
                                     historical_tod_mean   3.349669       NaN   5.991280       NaN  0.089321       NaN
                                     neighbor_average      8.012324       NaN  11.936514       NaN  0.200123       NaN
       coverage                      gls_map               3.315227       NaN   5.699103       NaN  0.085516       NaN
                                     gsp                   3.479926       NaN   6.107178       NaN  0.094284       NaN
                                     historical_tod_mean   3.468285       NaN   6.200950       NaN  0.097504       NaN
                                     neighbor_average      7.644255       NaN  11.555043       NaN  0.210175       NaN
       degree                        gls_map               3.757907       NaN   6.299723       NaN  0.095590       NaN
                                     gsp                   3.565723       NaN   6.042180       NaN  0.091034       NaN
                                     historical_tod_mean   3.467330       NaN   6.005765       NaN  0.093121       NaN
                                     neighbor_average      8.474899       NaN  12.868417       NaN  0.222774       NaN
       greedy_a_trace                gls_map               3.123888       NaN   5.406783       NaN  0.078631       NaN
                                     gsp                   3.518097       NaN   6.040645       NaN  0.092693       NaN
                                     historical_tod_mean   3.492949       NaN   6.128738       NaN  0.096267       NaN
                                     neighbor_average      7.520082       NaN  11.499290       NaN  0.216573       NaN
       greedy_d_logdet               gls_map               3.853699       NaN   6.199329       NaN  0.096827       NaN
                                     gsp                   3.524727       NaN   6.013521       NaN  0.093670       NaN
                                     historical_tod_mean   3.440325       NaN   6.061414       NaN  0.096418       NaN
                                     neighbor_average      8.294002       NaN  13.240822       NaN  0.260715       NaN
       multistart_swap_by_validation gls_map               3.138906       NaN   5.323912       NaN  0.078177       NaN
                                     gsp                   3.473025       NaN   5.989291       NaN  0.091500       NaN
                                     historical_tod_mean   3.434078       NaN   6.061783       NaN  0.094098       NaN
                                     neighbor_average      7.382230       NaN  11.261571       NaN  0.207579       NaN
       random                        gls_map               3.289913  0.073380   5.693800  0.160199  0.083513  0.003453
                                     gsp                   3.497059  0.059710   6.081003  0.104775  0.092135  0.002901
                                     historical_tod_mean   3.470790  0.060754   6.147431  0.103131  0.094961  0.002619
                                     neighbor_average      7.835694  0.192625  12.026766  0.330411  0.207075  0.009768
       scenario_average_a_trace      gls_map               3.148881       NaN   5.483276       NaN  0.080687       NaN
                                     gsp                   3.520344       NaN   6.105858       NaN  0.095227       NaN
                                     historical_tod_mean   3.489606       NaN   6.165276       NaN  0.096988       NaN
                                     neighbor_average      7.545754       NaN  11.346721       NaN  0.210592       NaN
       scenario_cvar_a_trace         gls_map               3.137825       NaN   5.401714       NaN  0.078362       NaN
                                     gsp                   3.380128       NaN   5.855441       NaN  0.089519       NaN
                                     historical_tod_mean   3.333452       NaN   5.908051       NaN  0.091480       NaN
                                     neighbor_average      8.013555       NaN  12.223145       NaN  0.212014       NaN
       swap_from_best_random_trace   gls_map               3.120282       NaN   5.314084       NaN  0.078085       NaN
                                     gsp                   3.434557       NaN   5.929492       NaN  0.090364       NaN
                                     historical_tod_mean   3.441117       NaN   6.020057       NaN  0.093875       NaN
                                     neighbor_average      7.578837       NaN  11.591881       NaN  0.214729       NaN
       swap_from_greedy_a_trace      gls_map               3.150746       NaN   5.419437       NaN  0.080130       NaN
                                     gsp                   3.523934       NaN   6.034329       NaN  0.092818       NaN
                                     historical_tod_mean   3.473270       NaN   6.105015       NaN  0.095917       NaN
                                     neighbor_average      7.566335       NaN  11.761470       NaN  0.219572       NaN
       swap_from_scenario_average    gls_map               3.219586       NaN   5.518881       NaN  0.081929       NaN
                                     gsp                   3.553291       NaN   6.087693       NaN  0.094167       NaN
                                     historical_tod_mean   3.497360       NaN   6.156491       NaN  0.097043       NaN
                                     neighbor_average      7.639517       NaN  11.768472       NaN  0.224691       NaN
       swap_from_scenario_cvar       gls_map               3.149573       NaN   5.402893       NaN  0.079929       NaN
                                     gsp                   3.495868       NaN   6.004441       NaN  0.092746       NaN
                                     historical_tod_mean   3.458248       NaN   6.077705       NaN  0.095641       NaN
                                     neighbor_average      7.658882       NaN  11.958805       NaN  0.224217       NaN
       top_variance                  gls_map               3.148320       NaN   5.434796       NaN  0.074591       NaN
                                     gsp                   3.140354       NaN   5.528920       NaN  0.076701       NaN
                                     historical_tod_mean   3.091276       NaN   5.589430       NaN  0.078283       NaN
                                     neighbor_average     10.332909       NaN  16.091002       NaN  0.197494       NaN
0.3    best_random_by_trace          gls_map               3.226924       NaN   5.603577       NaN  0.084031       NaN
                                     gsp                   3.530636       NaN   6.138803       NaN  0.095109       NaN
                                     historical_tod_mean   3.523074       NaN   6.230945       NaN  0.098550       NaN
                                     neighbor_average      7.576510       NaN  11.737896       NaN  0.219843       NaN
       best_random_by_validation     gls_map               3.004464       NaN   5.217015       NaN  0.074276       NaN
                                     gsp                   3.344047       NaN   5.844873       NaN  0.086666       NaN
                                     historical_tod_mean   3.315824       NaN   5.918436       NaN  0.089723       NaN
                                     neighbor_average      7.479094       NaN  11.359836       NaN  0.182859       NaN
       coverage                      gls_map               3.160714       NaN   5.515498       NaN  0.082675       NaN
                                     gsp                   3.447747       NaN   6.107766       NaN  0.094343       NaN
                                     historical_tod_mean   3.431030       NaN   6.211554       NaN  0.097856       NaN
                                     neighbor_average      7.502027       NaN  11.227494       NaN  0.202078       NaN
       degree                        gls_map               3.600181       NaN   6.177647       NaN  0.092989       NaN
                                     gsp                   3.465531       NaN   5.972494       NaN  0.090224       NaN
                                     historical_tod_mean   3.436291       NaN   6.011031       NaN  0.092882       NaN
                                     neighbor_average      8.707627       NaN  13.675747       NaN  0.248937       NaN
       greedy_a_trace                gls_map               3.001526       NaN   5.168146       NaN  0.076742       NaN
                                     gsp                   3.460668       NaN   5.975508       NaN  0.092432       NaN
                                     historical_tod_mean   3.461522       NaN   6.085653       NaN  0.097002       NaN
                                     neighbor_average      7.352871       NaN  11.343105       NaN  0.217389       NaN
       greedy_d_logdet               gls_map               3.486325       NaN   5.841225       NaN  0.090256       NaN
                                     gsp                   3.368903       NaN   5.865760       NaN  0.091107       NaN
                                     historical_tod_mean   3.339646       NaN   5.964084       NaN  0.094973       NaN
                                     neighbor_average      8.337478       NaN  13.163838       NaN  0.260834       NaN
       multistart_swap_by_validation gls_map               2.992514       NaN   5.181149       NaN  0.075996       NaN
                                     gsp                   3.402115       NaN   5.948755       NaN  0.090343       NaN
                                     historical_tod_mean   3.387050       NaN   6.043350       NaN  0.094250       NaN
                                     neighbor_average      7.439912       NaN  11.378615       NaN  0.211318       NaN
       random                        gls_map               3.167251  0.087571   5.501057  0.169840  0.079976  0.003693
                                     gsp                   3.479127  0.071972   6.065266  0.117384  0.091625  0.003196
                                     historical_tod_mean   3.463424  0.074376   6.145598  0.116529  0.094825  0.003071
                                     neighbor_average      7.691154  0.206492  11.854722  0.380078  0.200241  0.010010
       scenario_average_a_trace      gls_map               3.089001       NaN   5.409733       NaN  0.079688       NaN
                                     gsp                   3.520709       NaN   6.153374       NaN  0.096704       NaN
                                     historical_tod_mean   3.493094       NaN   6.216890       NaN  0.098792       NaN
                                     neighbor_average      7.831013       NaN  11.972275       NaN  0.217023       NaN
       scenario_cvar_a_trace         gls_map               3.001452       NaN   5.203771       NaN  0.075194       NaN
                                     gsp                   3.400358       NaN   5.944042       NaN  0.091763       NaN
                                     historical_tod_mean   3.379689       NaN   6.022681       NaN  0.094511       NaN
                                     neighbor_average      7.487195       NaN  11.417109       NaN  0.198900       NaN
       swap_from_best_random_trace   gls_map               2.964513       NaN   5.058100       NaN  0.074218       NaN
                                     gsp                   3.415316       NaN   5.891961       NaN  0.089561       NaN
                                     historical_tod_mean   3.381797       NaN   5.977267       NaN  0.093302       NaN
                                     neighbor_average      7.273714       NaN  11.189670       NaN  0.206127       NaN
       swap_from_greedy_a_trace      gls_map               3.001141       NaN   5.134134       NaN  0.076250       NaN
                                     gsp                   3.429649       NaN   5.927846       NaN  0.091570       NaN
                                     historical_tod_mean   3.425186       NaN   6.035757       NaN  0.095906       NaN
                                     neighbor_average      7.387941       NaN  11.335347       NaN  0.217129       NaN
       swap_from_scenario_average    gls_map               3.003837       NaN   5.098537       NaN  0.076620       NaN
                                     gsp                   3.415375       NaN   5.890884       NaN  0.091213       NaN
                                     historical_tod_mean   3.394994       NaN   5.993398       NaN  0.095211       NaN
                                     neighbor_average      7.411734       NaN  11.502202       NaN  0.218907       NaN
       swap_from_scenario_cvar       gls_map               2.973778       NaN   5.044526       NaN  0.073801       NaN
                                     gsp                   3.345443       NaN   5.813837       NaN  0.088321       NaN
                                     historical_tod_mean   3.342803       NaN   5.918922       NaN  0.092376       NaN
                                     neighbor_average      7.374544       NaN  11.283365       NaN  0.209087       NaN
       top_variance                  gls_map               3.032999       NaN   5.319769       NaN  0.070718       NaN
                                     gsp                   3.042282       NaN   5.433133       NaN  0.073296       NaN
                                     historical_tod_mean   2.986669       NaN   5.478421       NaN  0.074108       NaN
                                     neighbor_average     10.001781       NaN  15.365468       NaN  0.187877       NaN
```

## Best method per budget-layout row

```
 budget                 layout_type              method      mae     rmse
    0.1                top_variance historical_tod_mean 3.225791 5.721267
    0.2                top_variance historical_tod_mean 3.091276 5.589430
    0.3 swap_from_best_random_trace             gls_map 2.964513 5.058100
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.215398      0.255209 642
    gsp   condition_number     0.215992      0.215636 642
    gsp information_logdet    -0.229834     -0.247508 642
gls_map    posterior_trace     0.838982      0.851050 642
gls_map   condition_number     0.818577      0.845721 642
gls_map information_logdet    -0.795012     -0.795786 642
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- certificate_correlations.csv