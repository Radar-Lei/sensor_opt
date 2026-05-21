---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-06-13, 2012-06-08
Test days: 2012-05-07, 2012-05-30
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.583949       NaN   5.928744       NaN  0.086197       NaN
                                     gsp                   3.993785       NaN   6.750924       NaN  0.098377       NaN
                                     historical_tod_mean   4.134479       NaN   7.111634       NaN  0.101600       NaN
                                     neighbor_average      7.533483       NaN  11.625412       NaN  0.187903       NaN
       best_random_by_validation     gls_map               3.540267       NaN   6.058907       NaN  0.088883       NaN
                                     gsp                   3.998174       NaN   6.837588       NaN  0.103192       NaN
                                     historical_tod_mean   4.201091       NaN   7.228840       NaN  0.106652       NaN
                                     neighbor_average      7.396327       NaN  11.690275       NaN  0.195732       NaN
       coverage                      gls_map               3.539621       NaN   6.005661       NaN  0.089529       NaN
                                     gsp                   3.965352       NaN   6.859200       NaN  0.101790       NaN
                                     historical_tod_mean   4.192145       NaN   7.206059       NaN  0.105199       NaN
                                     neighbor_average      7.399845       NaN  11.333740       NaN  0.193726       NaN
       degree                        gls_map               3.896825       NaN   6.588615       NaN  0.100206       NaN
                                     gsp                   3.966018       NaN   6.897849       NaN  0.104877       NaN
                                     historical_tod_mean   4.158843       NaN   7.196543       NaN  0.105886       NaN
                                     neighbor_average      8.395338       NaN  12.700683       NaN  0.214555       NaN
       greedy_a_trace                gls_map               3.333794       NaN   5.631386       NaN  0.082493       NaN
                                     gsp                   3.962436       NaN   6.769915       NaN  0.100763       NaN
                                     historical_tod_mean   4.167319       NaN   7.149416       NaN  0.103768       NaN
                                     neighbor_average      7.093980       NaN  11.387956       NaN  0.196919       NaN
       greedy_d_logdet               gls_map               4.021232       NaN   6.423135       NaN  0.094333       NaN
                                     gsp                   4.051273       NaN   6.868465       NaN  0.095665       NaN
                                     historical_tod_mean   4.100332       NaN   7.052769       NaN  0.097820       NaN
                                     neighbor_average      8.167562       NaN  12.590189       NaN  0.222931       NaN
       multistart_swap_by_validation gls_map               3.407130       NaN   5.847354       NaN  0.086280       NaN
                                     gsp                   3.978674       NaN   6.818292       NaN  0.102963       NaN
                                     historical_tod_mean   4.183987       NaN   7.215364       NaN  0.106215       NaN
                                     neighbor_average      7.075532       NaN  11.116115       NaN  0.190072       NaN
       random                        gls_map               3.534131  0.038167   6.004503  0.070985  0.088757  0.001585
                                     gsp                   4.005448  0.022196   6.855195  0.040579  0.102618  0.001349
                                     historical_tod_mean   4.202133  0.020884   7.225056  0.036078  0.105931  0.001275
                                     neighbor_average      7.400593  0.140509  11.628928  0.190298  0.194153  0.003527
       rcss_selected                 gls_map               3.333794       NaN   5.631386       NaN  0.082493       NaN
                                     gsp                   3.962436       NaN   6.769915       NaN  0.100763       NaN
                                     historical_tod_mean   4.167319       NaN   7.149416       NaN  0.103768       NaN
                                     neighbor_average      7.093980       NaN  11.387956       NaN  0.196919       NaN
       robust_coverage_cvar          gls_map               3.479812       NaN   5.983367       NaN  0.089447       NaN
                                     gsp                   3.974618       NaN   6.865564       NaN  0.103510       NaN
                                     historical_tod_mean   4.180673       NaN   7.224209       NaN  0.106339       NaN
                                     neighbor_average      7.466114       NaN  11.551628       NaN  0.198785       NaN
       scenario_average_a_trace      gls_map               3.547280       NaN   6.004371       NaN  0.090126       NaN
                                     gsp                   4.008008       NaN   6.906042       NaN  0.103984       NaN
                                     historical_tod_mean   4.189416       NaN   7.231216       NaN  0.106508       NaN
                                     neighbor_average      7.422751       NaN  11.335912       NaN  0.202850       NaN
       scenario_cvar_a_trace         gls_map               3.534041       NaN   6.004909       NaN  0.090768       NaN
                                     gsp                   3.998924       NaN   6.871179       NaN  0.104297       NaN
                                     historical_tod_mean   4.183879       NaN   7.225544       NaN  0.106713       NaN
                                     neighbor_average      7.452667       NaN  11.424745       NaN  0.204946       NaN
       swap_from_best_random_trace   gls_map               3.476372       NaN   5.758497       NaN  0.082678       NaN
                                     gsp                   3.974783       NaN   6.733517       NaN  0.097093       NaN
                                     historical_tod_mean   4.133940       NaN   7.110913       NaN  0.100584       NaN
                                     neighbor_average      7.185526       NaN  11.022964       NaN  0.183800       NaN
       swap_from_greedy_a_trace      gls_map               3.355193       NaN   5.632465       NaN  0.080279       NaN
                                     gsp                   3.956337       NaN   6.733753       NaN  0.097416       NaN
                                     historical_tod_mean   4.151626       NaN   7.104173       NaN  0.100823       NaN
                                     neighbor_average      7.098772       NaN  11.187178       NaN  0.192375       NaN
       swap_from_scenario_average    gls_map               3.424654       NaN   5.801547       NaN  0.087299       NaN
                                     gsp                   3.960237       NaN   6.824000       NaN  0.102982       NaN
                                     historical_tod_mean   4.163298       NaN   7.192510       NaN  0.105817       NaN
                                     neighbor_average      7.255791       NaN  11.266364       NaN  0.201042       NaN
       swap_from_scenario_cvar       gls_map               3.413819       NaN   5.794642       NaN  0.086984       NaN
                                     gsp                   3.970424       NaN   6.816439       NaN  0.103209       NaN
                                     historical_tod_mean   4.156183       NaN   7.192545       NaN  0.105872       NaN
                                     neighbor_average      7.276716       NaN  11.367186       NaN  0.203222       NaN
       top_variance                  gls_map               3.518574       NaN   5.886455       NaN  0.083856       NaN
                                     gsp                   3.769744       NaN   6.390689       NaN  0.092265       NaN
                                     historical_tod_mean   3.930617       NaN   6.719283       NaN  0.094425       NaN
                                     neighbor_average     10.344290       NaN  15.799403       NaN  0.202290       NaN
       validation_swap_selected      gls_map               3.372910       NaN   5.713084       NaN  0.080819       NaN
                                     gsp                   3.940360       NaN   6.687631       NaN  0.097059       NaN
                                     historical_tod_mean   4.121441       NaN   7.084992       NaN  0.100346       NaN
                                     neighbor_average      7.390712       NaN  11.242182       NaN  0.186628       NaN
0.2    best_random_by_trace          gls_map               3.270514       NaN   5.560312       NaN  0.079671       NaN
                                     gsp                   4.006464       NaN   6.827016       NaN  0.101014       NaN
                                     historical_tod_mean   4.199057       NaN   7.225354       NaN  0.104514       NaN
                                     neighbor_average      7.127519       NaN  11.217508       NaN  0.188672       NaN
       best_random_by_validation     gls_map               3.293044       NaN   5.512300       NaN  0.080207       NaN
                                     gsp                   3.931935       NaN   6.639156       NaN  0.098566       NaN
                                     historical_tod_mean   4.076413       NaN   7.039671       NaN  0.101678       NaN
                                     neighbor_average      7.190101       NaN  11.300192       NaN  0.179100       NaN
       coverage                      gls_map               3.265367       NaN   5.572784       NaN  0.082868       NaN
                                     gsp                   3.989586       NaN   6.843375       NaN  0.103056       NaN
                                     historical_tod_mean   4.212155       NaN   7.260773       NaN  0.106862       NaN
                                     neighbor_average      6.989244       NaN  11.056970       NaN  0.185866       NaN
       degree                        gls_map               3.819013       NaN   6.416146       NaN  0.095200       NaN
                                     gsp                   3.930039       NaN   6.813244       NaN  0.101009       NaN
                                     historical_tod_mean   4.130645       NaN   7.183512       NaN  0.103180       NaN
                                     neighbor_average      8.718455       NaN  12.795151       NaN  0.203895       NaN
       greedy_a_trace                gls_map               3.032592       NaN   4.970184       NaN  0.070761       NaN
                                     gsp                   3.892491       NaN   6.592652       NaN  0.094182       NaN
                                     historical_tod_mean   4.074939       NaN   7.005364       NaN  0.097168       NaN
                                     neighbor_average      6.970503       NaN  10.959983       NaN  0.186933       NaN
       greedy_d_logdet               gls_map               3.512579       NaN   5.698620       NaN  0.082784       NaN
                                     gsp                   3.930349       NaN   6.692313       NaN  0.095041       NaN
                                     historical_tod_mean   4.086913       NaN   7.059702       NaN  0.097854       NaN
                                     neighbor_average      7.585861       NaN  11.912502       NaN  0.210555       NaN
       multistart_swap_by_validation gls_map               3.125124       NaN   5.237976       NaN  0.073488       NaN
                                     gsp                   3.944247       NaN   6.694035       NaN  0.096382       NaN
                                     historical_tod_mean   4.149862       NaN   7.108468       NaN  0.099743       NaN
                                     neighbor_average      6.862328       NaN  10.802617       NaN  0.173662       NaN
       random                        gls_map               3.281160  0.037151   5.573474  0.065539  0.081337  0.001853
                                     gsp                   3.996202  0.029934   6.804528  0.050386  0.102304  0.002081
                                     historical_tod_mean   4.195946  0.029985   7.212940  0.051114  0.105610  0.001905
                                     neighbor_average      7.076985  0.110389  11.247994  0.182451  0.184960  0.004030
       rcss_selected                 gls_map               3.032592       NaN   4.970184       NaN  0.070761       NaN
                                     gsp                   3.892491       NaN   6.592652       NaN  0.094182       NaN
                                     historical_tod_mean   4.074939       NaN   7.005364       NaN  0.097168       NaN
                                     neighbor_average      6.970503       NaN  10.959983       NaN  0.186933       NaN
       robust_coverage_cvar          gls_map               3.172937       NaN   5.414226       NaN  0.078494       NaN
                                     gsp                   3.927289       NaN   6.793178       NaN  0.100337       NaN
                                     historical_tod_mean   4.145509       NaN   7.188233       NaN  0.103481       NaN
                                     neighbor_average      7.177296       NaN  11.259619       NaN  0.191612       NaN
       scenario_average_a_trace      gls_map               3.252278       NaN   5.410586       NaN  0.077007       NaN
                                     gsp                   3.971266       NaN   6.778251       NaN  0.097978       NaN
                                     historical_tod_mean   4.137643       NaN   7.145228       NaN  0.101349       NaN
                                     neighbor_average      7.318012       NaN  11.469161       NaN  0.198806       NaN
       scenario_cvar_a_trace         gls_map               3.224598       NaN   5.523963       NaN  0.082353       NaN
                                     gsp                   3.942534       NaN   6.825156       NaN  0.103860       NaN
                                     historical_tod_mean   4.143066       NaN   7.222299       NaN  0.106843       NaN
                                     neighbor_average      7.079944       NaN  11.213114       NaN  0.196738       NaN
       swap_from_best_random_trace   gls_map               3.222672       NaN   5.383874       NaN  0.075052       NaN
                                     gsp                   3.963990       NaN   6.773618       NaN  0.096713       NaN
                                     historical_tod_mean   4.161579       NaN   7.166474       NaN  0.100384       NaN
                                     neighbor_average      7.048424       NaN  11.018979       NaN  0.185257       NaN
       swap_from_greedy_a_trace      gls_map               3.040861       NaN   4.970022       NaN  0.070683       NaN
                                     gsp                   3.869563       NaN   6.574326       NaN  0.093051       NaN
                                     historical_tod_mean   4.055076       NaN   6.980868       NaN  0.096385       NaN
                                     neighbor_average      6.983238       NaN  10.972330       NaN  0.187795       NaN
       swap_from_scenario_average    gls_map               3.124968       NaN   5.101205       NaN  0.072821       NaN
                                     gsp                   3.895265       NaN   6.611229       NaN  0.094009       NaN
                                     historical_tod_mean   4.058545       NaN   7.002600       NaN  0.097362       NaN
                                     neighbor_average      7.140793       NaN  11.127008       NaN  0.192235       NaN
       swap_from_scenario_cvar       gls_map               3.132816       NaN   5.227855       NaN  0.075934       NaN
                                     gsp                   3.897567       NaN   6.686415       NaN  0.098592       NaN
                                     historical_tod_mean   4.089789       NaN   7.093495       NaN  0.101792       NaN
                                     neighbor_average      7.017612       NaN  11.072261       NaN  0.191131       NaN
       top_variance                  gls_map               3.282760       NaN   5.531094       NaN  0.074989       NaN
                                     gsp                   3.634414       NaN   6.187476       NaN  0.085878       NaN
                                     historical_tod_mean   3.785421       NaN   6.500464       NaN  0.088372       NaN
                                     neighbor_average      9.051789       NaN  14.339681       NaN  0.178764       NaN
       validation_swap_selected      gls_map               3.026727       NaN   4.976749       NaN  0.070653       NaN
                                     gsp                   3.882603       NaN   6.580341       NaN  0.093893       NaN
                                     historical_tod_mean   4.063919       NaN   6.995822       NaN  0.096881       NaN
                                     neighbor_average      6.992330       NaN  10.960398       NaN  0.186754       NaN
0.3    best_random_by_trace          gls_map               3.128248       NaN   5.297101       NaN  0.077707       NaN
                                     gsp                   3.999514       NaN   6.761912       NaN  0.102317       NaN
                                     historical_tod_mean   4.177700       NaN   7.180960       NaN  0.105470       NaN
                                     neighbor_average      6.937526       NaN  11.072486       NaN  0.184018       NaN
       best_random_by_validation     gls_map               3.069999       NaN   5.288760       NaN  0.076089       NaN
                                     gsp                   3.994782       NaN   6.828409       NaN  0.102447       NaN
                                     historical_tod_mean   4.210988       NaN   7.269912       NaN  0.106609       NaN
                                     neighbor_average      6.909494       NaN  10.935627       NaN  0.179073       NaN
       coverage                      gls_map               3.148324       NaN   5.378043       NaN  0.080209       NaN
                                     gsp                   4.048842       NaN   6.897691       NaN  0.105685       NaN
                                     historical_tod_mean   4.276525       NaN   7.341274       NaN  0.109513       NaN
                                     neighbor_average      6.926688       NaN  11.164131       NaN  0.189654       NaN
       degree                        gls_map               3.728241       NaN   6.306720       NaN  0.093241       NaN
                                     gsp                   3.863400       NaN   6.712419       NaN  0.100787       NaN
                                     historical_tod_mean   4.036676       NaN   7.092881       NaN  0.102135       NaN
                                     neighbor_average      7.711382       NaN  12.427724       NaN  0.201672       NaN
       greedy_a_trace                gls_map               2.812423       NaN   4.604018       NaN  0.065612       NaN
                                     gsp                   3.844495       NaN   6.522747       NaN  0.093204       NaN
                                     historical_tod_mean   4.035205       NaN   6.969699       NaN  0.096366       NaN
                                     neighbor_average      6.843058       NaN  10.847066       NaN  0.185882       NaN
       greedy_d_logdet               gls_map               3.117048       NaN   5.078018       NaN  0.072827       NaN
                                     gsp                   3.882669       NaN   6.633559       NaN  0.094689       NaN
                                     historical_tod_mean   4.070323       NaN   7.072058       NaN  0.097963       NaN
                                     neighbor_average      7.266009       NaN  11.511173       NaN  0.202185       NaN
       multistart_swap_by_validation gls_map               2.958086       NaN   4.956814       NaN  0.070044       NaN
                                     gsp                   3.930049       NaN   6.669053       NaN  0.098474       NaN
                                     historical_tod_mean   4.115015       NaN   7.099471       NaN  0.101939       NaN
                                     neighbor_average      6.698662       NaN  10.574400       NaN  0.175642       NaN
       random                        gls_map               3.120896  0.042224   5.312211  0.090999  0.077069  0.002611
                                     gsp                   3.996879  0.040147   6.795365  0.073404  0.102583  0.002836
                                     historical_tod_mean   4.196041  0.041043   7.219264  0.073106  0.105772  0.002691
                                     neighbor_average      6.948910  0.097468  11.123915  0.168202  0.182005  0.004207
       rcss_selected                 gls_map               2.820174       NaN   4.610234       NaN  0.065742       NaN
                                     gsp                   3.830375       NaN   6.509705       NaN  0.092871       NaN
                                     historical_tod_mean   4.015468       NaN   6.952037       NaN  0.095954       NaN
                                     neighbor_average      6.886867       NaN  10.909688       NaN  0.187343       NaN
       robust_coverage_cvar          gls_map               3.041290       NaN   5.172122       NaN  0.075490       NaN
                                     gsp                   3.904909       NaN   6.762613       NaN  0.100964       NaN
                                     historical_tod_mean   4.110993       NaN   7.187731       NaN  0.104249       NaN
                                     neighbor_average      7.270900       NaN  11.644071       NaN  0.198766       NaN
       scenario_average_a_trace      gls_map               3.117440       NaN   5.159538       NaN  0.075008       NaN
                                     gsp                   3.925984       NaN   6.713304       NaN  0.098965       NaN
                                     historical_tod_mean   4.117706       NaN   7.136699       NaN  0.102154       NaN
                                     neighbor_average      7.191399       NaN  11.410565       NaN  0.200857       NaN
       scenario_cvar_a_trace         gls_map               3.129943       NaN   5.359080       NaN  0.080970       NaN
                                     gsp                   3.929945       NaN   6.830369       NaN  0.105474       NaN
                                     historical_tod_mean   4.131449       NaN   7.259551       NaN  0.108541       NaN
                                     neighbor_average      7.179721       NaN  11.500438       NaN  0.204065       NaN
       swap_from_best_random_trace   gls_map               3.016730       NaN   5.012343       NaN  0.071158       NaN
                                     gsp                   3.927777       NaN   6.609564       NaN  0.097041       NaN
                                     historical_tod_mean   4.102835       NaN   7.043273       NaN  0.100205       NaN
                                     neighbor_average      6.879860       NaN  10.874128       NaN  0.179967       NaN
       swap_from_greedy_a_trace      gls_map               2.820174       NaN   4.610234       NaN  0.065742       NaN
                                     gsp                   3.830375       NaN   6.509705       NaN  0.092871       NaN
                                     historical_tod_mean   4.015468       NaN   6.952037       NaN  0.095954       NaN
                                     neighbor_average      6.886867       NaN  10.909688       NaN  0.187343       NaN
       swap_from_scenario_average    gls_map               2.973703       NaN   4.843873       NaN  0.069744       NaN
                                     gsp                   3.877330       NaN   6.577816       NaN  0.094805       NaN
                                     historical_tod_mean   4.058266       NaN   7.006438       NaN  0.098035       NaN
                                     neighbor_average      6.965445       NaN  11.017569       NaN  0.191643       NaN
       swap_from_scenario_cvar       gls_map               3.002226       NaN   5.032775       NaN  0.072404       NaN
                                     gsp                   3.894478       NaN   6.704047       NaN  0.098831       NaN
                                     historical_tod_mean   4.095806       NaN   7.142615       NaN  0.102301       NaN
                                     neighbor_average      7.051259       NaN  11.245856       NaN  0.197500       NaN
       top_variance                  gls_map               3.098383       NaN   5.258225       NaN  0.070393       NaN
                                     gsp                   3.483373       NaN   5.974936       NaN  0.081717       NaN
                                     historical_tod_mean   3.602077       NaN   6.246296       NaN  0.083626       NaN
                                     neighbor_average      8.618899       NaN  13.561999       NaN  0.166476       NaN
       validation_swap_selected      gls_map               2.814508       NaN   4.651525       NaN  0.068312       NaN
                                     gsp                   3.835766       NaN   6.535361       NaN  0.095788       NaN
                                     historical_tod_mean   4.009684       NaN   6.972113       NaN  0.098480       NaN
                                     neighbor_average      6.895531       NaN  10.927590       NaN  0.189723       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1           greedy_a_trace gls_map 3.333794 5.631386
    0.2 validation_swap_selected gls_map 3.026727 4.976749
    0.3           greedy_a_trace gls_map 2.812423 4.604018
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.155422      0.106846 351
    gsp   condition_number     0.155566      0.089538 351
    gsp information_logdet    -0.143846     -0.110228 351
gls_map    posterior_trace     0.946221      0.929594 351
gls_map   condition_number     0.832416      0.884834 351
gls_map information_logdet    -0.919687     -0.899563 351
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv