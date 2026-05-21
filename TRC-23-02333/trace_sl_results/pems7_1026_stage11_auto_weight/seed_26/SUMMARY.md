---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-05-08, 2012-05-25
Test days: 2012-06-27, 2012-06-29
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               4.026536       NaN   6.647295       NaN  0.103512       NaN
                                     gsp                   4.600065       NaN   7.792913       NaN  0.124187       NaN
                                     historical_tod_mean   4.561499       NaN   8.149418       NaN  0.129409       NaN
                                     neighbor_average      8.224094       NaN  12.398879       NaN  0.224977       NaN
       best_random_by_validation     gls_map               3.909333       NaN   6.437238       NaN  0.100443       NaN
                                     gsp                   4.550728       NaN   7.758896       NaN  0.123675       NaN
                                     historical_tod_mean   4.548623       NaN   8.106274       NaN  0.127878       NaN
                                     neighbor_average      8.169728       NaN  12.195730       NaN  0.215621       NaN
       coverage                      gls_map               4.103946       NaN   6.814641       NaN  0.107115       NaN
                                     gsp                   4.579187       NaN   7.933073       NaN  0.127176       NaN
                                     historical_tod_mean   4.602606       NaN   8.211146       NaN  0.130476       NaN
                                     neighbor_average      8.353873       NaN  12.263988       NaN  0.221063       NaN
       degree                        gls_map               4.573029       NaN   7.529143       NaN  0.120381       NaN
                                     gsp                   4.611726       NaN   7.888025       NaN  0.127166       NaN
                                     historical_tod_mean   4.532128       NaN   8.146124       NaN  0.128537       NaN
                                     neighbor_average      9.275982       NaN  13.175478       NaN  0.245234       NaN
       greedy_a_trace                gls_map               3.864055       NaN   6.379034       NaN  0.100367       NaN
                                     gsp                   4.551948       NaN   7.805541       NaN  0.125203       NaN
                                     historical_tod_mean   4.554466       NaN   8.136055       NaN  0.129105       NaN
                                     neighbor_average      7.916228       NaN  11.942272       NaN  0.226184       NaN
       greedy_d_logdet               gls_map               4.647382       NaN   7.298841       NaN  0.118926       NaN
                                     gsp                   4.531845       NaN   7.937226       NaN  0.128874       NaN
                                     historical_tod_mean   4.525505       NaN   8.136218       NaN  0.129760       NaN
                                     neighbor_average      8.736616       NaN  13.619168       NaN  0.270389       NaN
       multistart_swap_by_validation gls_map               3.882442       NaN   6.507305       NaN  0.100179       NaN
                                     gsp                   4.540767       NaN   7.799794       NaN  0.124822       NaN
                                     historical_tod_mean   4.550385       NaN   8.129713       NaN  0.128620       NaN
                                     neighbor_average      8.179723       NaN  12.066411       NaN  0.219290       NaN
       random                        gls_map               4.080866  0.058042   6.813949  0.110816  0.105914  0.002205
                                     gsp                   4.605777  0.027569   7.856618  0.045432  0.125635  0.001291
                                     historical_tod_mean   4.583455  0.022490   8.189197  0.038707  0.129898  0.001088
                                     neighbor_average      8.313674  0.152794  12.559267  0.208097  0.223947  0.004889
       rcss_selected                 gls_map               3.856431       NaN   6.390681       NaN  0.100203       NaN
                                     gsp                   4.540457       NaN   7.801322       NaN  0.124555       NaN
                                     historical_tod_mean   4.549012       NaN   8.128001       NaN  0.128715       NaN
                                     neighbor_average      7.973548       NaN  12.082948       NaN  0.228133       NaN
       robust_coverage_cvar          gls_map               4.043202       NaN   6.684134       NaN  0.102784       NaN
                                     gsp                   4.575386       NaN   7.790667       NaN  0.122892       NaN
                                     historical_tod_mean   4.530540       NaN   8.112323       NaN  0.127319       NaN
                                     neighbor_average      8.460715       NaN  12.585093       NaN  0.225119       NaN
       scenario_average_a_trace      gls_map               4.118541       NaN   6.699977       NaN  0.103974       NaN
                                     gsp                   4.578471       NaN   7.783203       NaN  0.123002       NaN
                                     historical_tod_mean   4.535321       NaN   8.108995       NaN  0.127373       NaN
                                     neighbor_average      8.486039       NaN  12.559504       NaN  0.233487       NaN
       scenario_cvar_a_trace         gls_map               4.037741       NaN   6.651647       NaN  0.101430       NaN
                                     gsp                   4.552639       NaN   7.735243       NaN  0.121738       NaN
                                     historical_tod_mean   4.506683       NaN   8.074481       NaN  0.126792       NaN
                                     neighbor_average      8.586264       NaN  12.824827       NaN  0.232112       NaN
       swap_from_best_random_trace   gls_map               3.965316       NaN   6.501624       NaN  0.102200       NaN
                                     gsp                   4.559453       NaN   7.761204       NaN  0.123709       NaN
                                     historical_tod_mean   4.532212       NaN   8.103249       NaN  0.128528       NaN
                                     neighbor_average      8.120939       NaN  12.130196       NaN  0.227754       NaN
       swap_from_greedy_a_trace      gls_map               3.856431       NaN   6.390681       NaN  0.100203       NaN
                                     gsp                   4.540457       NaN   7.801322       NaN  0.124555       NaN
                                     historical_tod_mean   4.549012       NaN   8.128001       NaN  0.128715       NaN
                                     neighbor_average      7.973548       NaN  12.082948       NaN  0.228133       NaN
       swap_from_scenario_average    gls_map               3.960218       NaN   6.459789       NaN  0.099817       NaN
                                     gsp                   4.521817       NaN   7.725976       NaN  0.121488       NaN
                                     historical_tod_mean   4.505966       NaN   8.056769       NaN  0.126352       NaN
                                     neighbor_average      8.214401       NaN  12.214990       NaN  0.226804       NaN
       swap_from_scenario_cvar       gls_map               3.911669       NaN   6.465637       NaN  0.099517       NaN
                                     gsp                   4.500921       NaN   7.735174       NaN  0.122544       NaN
                                     historical_tod_mean   4.497756       NaN   8.056274       NaN  0.126982       NaN
                                     neighbor_average      8.165547       NaN  12.371221       NaN  0.228551       NaN
       top_variance                  gls_map               4.207524       NaN   6.920166       NaN  0.103708       NaN
                                     gsp                   4.430517       NaN   7.465634       NaN  0.113164       NaN
                                     historical_tod_mean   4.322996       NaN   7.744657       NaN  0.115006       NaN
                                     neighbor_average     11.943961       NaN  17.725192       NaN  0.240866       NaN
       validation_swap_selected      gls_map               3.883657       NaN   6.483186       NaN  0.099421       NaN
                                     gsp                   4.514823       NaN   7.774154       NaN  0.123761       NaN
                                     historical_tod_mean   4.528933       NaN   8.100486       NaN  0.127378       NaN
                                     neighbor_average      8.314156       NaN  12.216547       NaN  0.219985       NaN
0.2    best_random_by_trace          gls_map               3.757680       NaN   6.208420       NaN  0.096613       NaN
                                     gsp                   4.666097       NaN   7.892045       NaN  0.127117       NaN
                                     historical_tod_mean   4.634115       NaN   8.266031       NaN  0.132566       NaN
                                     neighbor_average      7.770897       NaN  11.801153       NaN  0.216400       NaN
       best_random_by_validation     gls_map               3.635693       NaN   6.113743       NaN  0.094274       NaN
                                     gsp                   4.601431       NaN   7.756365       NaN  0.124570       NaN
                                     historical_tod_mean   4.522930       NaN   8.127453       NaN  0.128708       NaN
                                     neighbor_average      7.936507       NaN  12.029037       NaN  0.214597       NaN
       coverage                      gls_map               3.757410       NaN   6.238326       NaN  0.097205       NaN
                                     gsp                   4.627081       NaN   7.900839       NaN  0.128299       NaN
                                     historical_tod_mean   4.628587       NaN   8.245276       NaN  0.132108       NaN
                                     neighbor_average      7.842325       NaN  11.889486       NaN  0.214176       NaN
       degree                        gls_map               4.447353       NaN   7.283529       NaN  0.115731       NaN
                                     gsp                   4.622283       NaN   7.804894       NaN  0.126369       NaN
                                     historical_tod_mean   4.476778       NaN   8.112012       NaN  0.127406       NaN
                                     neighbor_average     10.431679       NaN  14.074178       NaN  0.240854       NaN
       greedy_a_trace                gls_map               3.454185       NaN   5.605368       NaN  0.087071       NaN
                                     gsp                   4.465978       NaN   7.609267       NaN  0.120981       NaN
                                     historical_tod_mean   4.452064       NaN   7.981377       NaN  0.125061       NaN
                                     neighbor_average      7.712095       NaN  11.700765       NaN  0.219675       NaN
       greedy_d_logdet               gls_map               4.047327       NaN   6.513364       NaN  0.104959       NaN
                                     gsp                   4.483656       NaN   7.755396       NaN  0.126193       NaN
                                     historical_tod_mean   4.486543       NaN   8.099992       NaN  0.129844       NaN
                                     neighbor_average      8.565287       NaN  13.300538       NaN  0.260526       NaN
       multistart_swap_by_validation gls_map               3.508624       NaN   5.826479       NaN  0.088227       NaN
                                     gsp                   4.501303       NaN   7.642078       NaN  0.121242       NaN
                                     historical_tod_mean   4.477541       NaN   8.015461       NaN  0.125900       NaN
                                     neighbor_average      7.727587       NaN  11.589023       NaN  0.203251       NaN
       random                        gls_map               3.748675  0.049544   6.278714  0.109204  0.096360  0.002175
                                     gsp                   4.637174  0.032149   7.828605  0.064882  0.125662  0.001887
                                     historical_tod_mean   4.586001  0.036337   8.195645  0.063417  0.130170  0.001823
                                     neighbor_average      7.994843  0.118876  12.228173  0.201117  0.215241  0.004937
       rcss_selected                 gls_map               3.427908       NaN   5.598153       NaN  0.086454       NaN
                                     gsp                   4.455406       NaN   7.600786       NaN  0.120431       NaN
                                     historical_tod_mean   4.446833       NaN   7.967396       NaN  0.124712       NaN
                                     neighbor_average      7.733653       NaN  11.729799       NaN  0.218963       NaN
       robust_coverage_cvar          gls_map               3.641176       NaN   5.976769       NaN  0.090713       NaN
                                     gsp                   4.520863       NaN   7.623208       NaN  0.120139       NaN
                                     historical_tod_mean   4.445853       NaN   7.987616       NaN  0.124325       NaN
                                     neighbor_average      8.083075       NaN  12.283232       NaN  0.218298       NaN
       scenario_average_a_trace      gls_map               3.686554       NaN   6.023641       NaN  0.091966       NaN
                                     gsp                   4.558368       NaN   7.641854       NaN  0.120700       NaN
                                     historical_tod_mean   4.484634       NaN   8.004286       NaN  0.124223       NaN
                                     neighbor_average      8.224410       NaN  12.510118       NaN  0.231180       NaN
       scenario_cvar_a_trace         gls_map               3.723817       NaN   6.117210       NaN  0.091974       NaN
                                     gsp                   4.543576       NaN   7.622298       NaN  0.119966       NaN
                                     historical_tod_mean   4.437225       NaN   7.987792       NaN  0.124684       NaN
                                     neighbor_average      8.182224       NaN  12.400831       NaN  0.221706       NaN
       swap_from_best_random_trace   gls_map               3.634497       NaN   5.943162       NaN  0.091870       NaN
                                     gsp                   4.603622       NaN   7.801291       NaN  0.124991       NaN
                                     historical_tod_mean   4.573203       NaN   8.179891       NaN  0.129993       NaN
                                     neighbor_average      7.665767       NaN  11.634069       NaN  0.215166       NaN
       swap_from_greedy_a_trace      gls_map               3.427908       NaN   5.598153       NaN  0.086454       NaN
                                     gsp                   4.455406       NaN   7.600786       NaN  0.120431       NaN
                                     historical_tod_mean   4.446833       NaN   7.967396       NaN  0.124712       NaN
                                     neighbor_average      7.733653       NaN  11.729799       NaN  0.218963       NaN
       swap_from_scenario_average    gls_map               3.562811       NaN   5.812914       NaN  0.088905       NaN
                                     gsp                   4.500337       NaN   7.624395       NaN  0.120436       NaN
                                     historical_tod_mean   4.467583       NaN   7.997722       NaN  0.125044       NaN
                                     neighbor_average      8.036589       NaN  12.210655       NaN  0.227208       NaN
       swap_from_scenario_cvar       gls_map               3.597956       NaN   5.901887       NaN  0.089300       NaN
                                     gsp                   4.493912       NaN   7.610529       NaN  0.120185       NaN
                                     historical_tod_mean   4.430055       NaN   7.983429       NaN  0.125067       NaN
                                     neighbor_average      7.966002       NaN  12.116914       NaN  0.221209       NaN
       top_variance                  gls_map               3.846636       NaN   6.274809       NaN  0.090829       NaN
                                     gsp                   4.319784       NaN   7.179010       NaN  0.105664       NaN
                                     historical_tod_mean   4.125706       NaN   7.424661       NaN  0.106025       NaN
                                     neighbor_average     10.164890       NaN  15.522920       NaN  0.205908       NaN
       validation_swap_selected      gls_map               3.434403       NaN   5.591754       NaN  0.086467       NaN
                                     gsp                   4.443933       NaN   7.577151       NaN  0.119951       NaN
                                     historical_tod_mean   4.429839       NaN   7.948243       NaN  0.124233       NaN
                                     neighbor_average      7.741436       NaN  11.743307       NaN  0.218416       NaN
0.3    best_random_by_trace          gls_map               3.518589       NaN   5.847277       NaN  0.090333       NaN
                                     gsp                   4.684418       NaN   7.872488       NaN  0.127391       NaN
                                     historical_tod_mean   4.647876       NaN   8.260159       NaN  0.131957       NaN
                                     neighbor_average      7.845094       NaN  12.009918       NaN  0.210244       NaN
       best_random_by_validation     gls_map               3.382548       NaN   5.751207       NaN  0.086152       NaN
                                     gsp                   4.624649       NaN   7.782817       NaN  0.124186       NaN
                                     historical_tod_mean   4.564967       NaN   8.147526       NaN  0.128790       NaN
                                     neighbor_average      7.616057       NaN  11.670480       NaN  0.203368       NaN
       coverage                      gls_map               3.581899       NaN   5.962773       NaN  0.092486       NaN
                                     gsp                   4.697390       NaN   7.940320       NaN  0.129906       NaN
                                     historical_tod_mean   4.685435       NaN   8.323926       NaN  0.134530       NaN
                                     neighbor_average      7.725128       NaN  11.995107       NaN  0.215791       NaN
       degree                        gls_map               4.272156       NaN   7.066685       NaN  0.110048       NaN
                                     gsp                   4.556202       NaN   7.669429       NaN  0.122366       NaN
                                     historical_tod_mean   4.371473       NaN   7.997985       NaN  0.124283       NaN
                                     neighbor_average      9.254605       NaN  13.486272       NaN  0.230778       NaN
       greedy_a_trace                gls_map               3.187133       NaN   5.186296       NaN  0.080790       NaN
                                     gsp                   4.479682       NaN   7.633084       NaN  0.122416       NaN
                                     historical_tod_mean   4.474244       NaN   8.031835       NaN  0.126811       NaN
                                     neighbor_average      7.590937       NaN  11.654535       NaN  0.219853       NaN
       greedy_d_logdet               gls_map               3.570761       NaN   5.789753       NaN  0.092731       NaN
                                     gsp                   4.483249       NaN   7.697842       NaN  0.126353       NaN
                                     historical_tod_mean   4.454067       NaN   8.096211       NaN  0.130450       NaN
                                     neighbor_average      8.314306       NaN  12.830192       NaN  0.253724       NaN
       multistart_swap_by_validation gls_map               3.263810       NaN   5.437895       NaN  0.080290       NaN
                                     gsp                   4.504947       NaN   7.547939       NaN  0.118260       NaN
                                     historical_tod_mean   4.438524       NaN   7.943818       NaN  0.122660       NaN
                                     neighbor_average      7.704262       NaN  11.735152       NaN  0.199337       NaN
       random                        gls_map               3.514672  0.048852   5.879164  0.105237  0.089195  0.002124
                                     gsp                   4.650779  0.043740   7.799123  0.079011  0.124916  0.002186
                                     historical_tod_mean   4.578338  0.045975   8.177891  0.080156  0.129519  0.002293
                                     neighbor_average      7.778632  0.101839  11.979824  0.184075  0.207755  0.004584
       rcss_selected                 gls_map               3.187133       NaN   5.186296       NaN  0.080790       NaN
                                     gsp                   4.479682       NaN   7.633084       NaN  0.122416       NaN
                                     historical_tod_mean   4.474244       NaN   8.031835       NaN  0.126811       NaN
                                     neighbor_average      7.590937       NaN  11.654535       NaN  0.219853       NaN
       robust_coverage_cvar          gls_map               3.445417       NaN   5.641830       NaN  0.084857       NaN
                                     gsp                   4.533597       NaN   7.572489       NaN  0.118994       NaN
                                     historical_tod_mean   4.416655       NaN   7.947949       NaN  0.123114       NaN
                                     neighbor_average      7.998200       NaN  12.357568       NaN  0.220375       NaN
       scenario_average_a_trace      gls_map               3.488723       NaN   5.681213       NaN  0.087107       NaN
                                     gsp                   4.546027       NaN   7.604714       NaN  0.120831       NaN
                                     historical_tod_mean   4.448625       NaN   7.994883       NaN  0.124595       NaN
                                     neighbor_average      8.113042       NaN  12.409334       NaN  0.229965       NaN
       scenario_cvar_a_trace         gls_map               3.556322       NaN   5.936181       NaN  0.088824       NaN
                                     gsp                   4.552258       NaN   7.619170       NaN  0.120667       NaN
                                     historical_tod_mean   4.424498       NaN   7.991403       NaN  0.124897       NaN
                                     neighbor_average      8.170245       NaN  12.619245       NaN  0.225930       NaN
       swap_from_best_random_trace   gls_map               3.397186       NaN   5.615341       NaN  0.086107       NaN
                                     gsp                   4.586769       NaN   7.736180       NaN  0.124411       NaN
                                     historical_tod_mean   4.557459       NaN   8.133449       NaN  0.128816       NaN
                                     neighbor_average      7.696048       NaN  11.728972       NaN  0.207540       NaN
       swap_from_greedy_a_trace      gls_map               3.172602       NaN   5.167603       NaN  0.080445       NaN
                                     gsp                   4.455055       NaN   7.593476       NaN  0.121554       NaN
                                     historical_tod_mean   4.447745       NaN   7.997806       NaN  0.126210       NaN
                                     neighbor_average      7.555034       NaN  11.604404       NaN  0.218573       NaN
       swap_from_scenario_average    gls_map               3.326494       NaN   5.427544       NaN  0.083432       NaN
                                     gsp                   4.449116       NaN   7.541525       NaN  0.119611       NaN
                                     historical_tod_mean   4.410032       NaN   7.945261       NaN  0.124064       NaN
                                     neighbor_average      7.899179       NaN  12.080464       NaN  0.222991       NaN
       swap_from_scenario_cvar       gls_map               3.405348       NaN   5.696437       NaN  0.085530       NaN
                                     gsp                   4.517545       NaN   7.654780       NaN  0.122135       NaN
                                     historical_tod_mean   4.439584       NaN   8.043054       NaN  0.126659       NaN
                                     neighbor_average      7.903062       NaN  12.142522       NaN  0.224761       NaN
       top_variance                  gls_map               3.474549       NaN   5.796131       NaN  0.080555       NaN
                                     gsp                   4.089134       NaN   6.836416       NaN  0.097134       NaN
                                     historical_tod_mean   3.893713       NaN   7.056415       NaN  0.096770       NaN
                                     neighbor_average      9.671214       NaN  14.791051       NaN  0.190287       NaN
       validation_swap_selected      gls_map               3.168168       NaN   5.166429       NaN  0.081048       NaN
                                     gsp                   4.437913       NaN   7.578181       NaN  0.122082       NaN
                                     historical_tod_mean   4.431407       NaN   7.980702       NaN  0.126560       NaN
                                     neighbor_average      7.581957       NaN  11.641933       NaN  0.219289       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 3.856431 6.390681
    0.2 swap_from_greedy_a_trace gls_map 3.427908 5.598153
    0.3 validation_swap_selected gls_map 3.168168 5.166429
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.220942     -0.322829 351
    gsp   condition_number    -0.221081     -0.397974 351
    gsp information_logdet     0.208560      0.312728 351
gls_map    posterior_trace     0.954265      0.930366 351
gls_map   condition_number     0.847249      0.888442 351
gls_map information_logdet    -0.928442     -0.899689 351
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv