---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-08, 2012-05-25
Test days: 2012-06-27, 2012-06-29
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.769035       NaN   6.429452       NaN  0.097096       NaN
                                     gsp                   4.078016       NaN   7.035324       NaN  0.108556       NaN
                                     historical_tod_mean   4.094554       NaN   7.409089       NaN  0.113363       NaN
                                     neighbor_average      8.215528       NaN  12.327673       NaN  0.213858       NaN
       best_random_by_validation     gls_map               3.803250       NaN   6.437041       NaN  0.097577       NaN
                                     gsp                   4.065556       NaN   6.946864       NaN  0.107762       NaN
                                     historical_tod_mean   4.070901       NaN   7.365870       NaN  0.112878       NaN
                                     neighbor_average      8.373059       NaN  12.273424       NaN  0.216626       NaN
       coverage                      gls_map               4.192948       NaN   6.821798       NaN  0.105548       NaN
                                     gsp                   4.367544       NaN   7.262669       NaN  0.112518       NaN
                                     historical_tod_mean   4.129847       NaN   7.448044       NaN  0.113424       NaN
                                     neighbor_average      8.664771       NaN  12.906054       NaN  0.234110       NaN
       degree                        gls_map               4.318048       NaN   7.309279       NaN  0.115108       NaN
                                     gsp                   4.257013       NaN   7.343585       NaN  0.117241       NaN
                                     historical_tod_mean   4.185642       NaN   7.547855       NaN  0.118260       NaN
                                     neighbor_average      9.154087       NaN  13.681185       NaN  0.258396       NaN
       greedy_a_trace                gls_map               3.957969       NaN   6.592644       NaN  0.097314       NaN
                                     gsp                   4.249256       NaN   7.089050       NaN  0.110328       NaN
                                     historical_tod_mean   4.145910       NaN   7.423162       NaN  0.113771       NaN
                                     neighbor_average      8.269507       NaN  12.426874       NaN  0.235585       NaN
       greedy_d_logdet               gls_map               5.184435       NaN   8.051261       NaN  0.137363       NaN
                                     gsp                   4.343389       NaN   7.298073       NaN  0.118884       NaN
                                     historical_tod_mean   4.136067       NaN   7.446983       NaN  0.115277       NaN
                                     neighbor_average      9.082271       NaN  14.541335       NaN  0.283635       NaN
       multistart_swap_by_validation gls_map               3.815105       NaN   6.310277       NaN  0.093270       NaN
                                     gsp                   4.208990       NaN   7.024703       NaN  0.108088       NaN
                                     historical_tod_mean   4.103061       NaN   7.376333       NaN  0.112565       NaN
                                     neighbor_average      8.322225       NaN  12.391819       NaN  0.228831       NaN
       random                        gls_map               4.019688  0.097304   6.718350  0.147143  0.103396  0.003736
                                     gsp                   4.151013  0.056156   7.079201  0.088785  0.110300  0.002580
                                     historical_tod_mean   4.103843  0.041648   7.418460  0.064589  0.114442  0.001731
                                     neighbor_average      8.552372  0.326929  12.719992  0.424639  0.227289  0.010031
       rcss_selected                 gls_map               3.881612       NaN   6.525464       NaN  0.098659       NaN
                                     gsp                   4.030413       NaN   6.888330       NaN  0.105234       NaN
                                     historical_tod_mean   4.012817       NaN   7.263093       NaN  0.109879       NaN
                                     neighbor_average      9.001512       NaN  13.207507       NaN  0.213539       NaN
       robust_coverage_cvar          gls_map               3.872183       NaN   6.388374       NaN  0.098493       NaN
                                     gsp                   4.175686       NaN   7.047962       NaN  0.110916       NaN
                                     historical_tod_mean   4.103632       NaN   7.414498       NaN  0.115367       NaN
                                     neighbor_average      8.313569       NaN  12.388115       NaN  0.229808       NaN
       scenario_average_a_trace      gls_map               3.887327       NaN   6.527906       NaN  0.099847       NaN
                                     gsp                   4.189669       NaN   7.021599       NaN  0.110445       NaN
                                     historical_tod_mean   4.069722       NaN   7.374790       NaN  0.114099       NaN
                                     neighbor_average      8.942757       NaN  13.024501       NaN  0.237322       NaN
       scenario_cvar_a_trace         gls_map               3.762639       NaN   6.210450       NaN  0.094226       NaN
                                     gsp                   4.181006       NaN   6.941400       NaN  0.108321       NaN
                                     historical_tod_mean   4.059826       NaN   7.323100       NaN  0.113062       NaN
                                     neighbor_average      8.167739       NaN  12.168567       NaN  0.222292       NaN
       swap_from_best_random_trace   gls_map               3.774585       NaN   6.305102       NaN  0.094743       NaN
                                     gsp                   4.217830       NaN   7.072294       NaN  0.109894       NaN
                                     historical_tod_mean   4.123664       NaN   7.394895       NaN  0.113476       NaN
                                     neighbor_average      8.274294       NaN  12.384573       NaN  0.235504       NaN
       swap_from_greedy_a_trace      gls_map               3.828300       NaN   6.319488       NaN  0.093615       NaN
                                     gsp                   4.219632       NaN   7.057425       NaN  0.108624       NaN
                                     historical_tod_mean   4.121484       NaN   7.410491       NaN  0.113357       NaN
                                     neighbor_average      8.281461       NaN  12.434543       NaN  0.231642       NaN
       swap_from_scenario_average    gls_map               3.856824       NaN   6.294437       NaN  0.095114       NaN
                                     gsp                   4.224109       NaN   7.070653       NaN  0.109141       NaN
                                     historical_tod_mean   4.124738       NaN   7.421463       NaN  0.113728       NaN
                                     neighbor_average      8.135136       NaN  12.285032       NaN  0.231696       NaN
       swap_from_scenario_cvar       gls_map               3.800548       NaN   6.358673       NaN  0.093889       NaN
                                     gsp                   4.218999       NaN   7.111240       NaN  0.110129       NaN
                                     historical_tod_mean   4.130415       NaN   7.435795       NaN  0.114166       NaN
                                     neighbor_average      8.293230       NaN  12.426033       NaN  0.238098       NaN
       top_variance                  gls_map               3.919561       NaN   6.705885       NaN  0.097532       NaN
                                     gsp                   3.937447       NaN   6.872174       NaN  0.101352       NaN
                                     historical_tod_mean   3.918025       NaN   7.167072       NaN  0.104506       NaN
                                     neighbor_average     12.753115       NaN  18.857490       NaN  0.250722       NaN
       validation_swap_selected      gls_map               3.844917       NaN   6.509570       NaN  0.098429       NaN
                                     gsp                   3.997337       NaN   6.871685       NaN  0.105201       NaN
                                     historical_tod_mean   3.978045       NaN   7.229330       NaN  0.109551       NaN
                                     neighbor_average      8.699595       NaN  12.848509       NaN  0.207591       NaN
0.2    best_random_by_trace          gls_map               3.771468       NaN   6.280869       NaN  0.094653       NaN
                                     gsp                   4.157802       NaN   6.999515       NaN  0.109383       NaN
                                     historical_tod_mean   4.103800       NaN   7.374539       NaN  0.114230       NaN
                                     neighbor_average      8.029375       NaN  12.101887       NaN  0.226483       NaN
       best_random_by_validation     gls_map               3.615881       NaN   6.094752       NaN  0.091252       NaN
                                     gsp                   4.030859       NaN   6.773072       NaN  0.103261       NaN
                                     historical_tod_mean   3.960658       NaN   7.207470       NaN  0.109433       NaN
                                     neighbor_average      8.523464       NaN  12.421693       NaN  0.215197       NaN
       coverage                      gls_map               3.937599       NaN   6.393685       NaN  0.098598       NaN
                                     gsp                   4.352678       NaN   7.146895       NaN  0.112886       NaN
                                     historical_tod_mean   4.139534       NaN   7.515295       NaN  0.115751       NaN
                                     neighbor_average      8.129188       NaN  12.037892       NaN  0.219860       NaN
       degree                        gls_map               4.269667       NaN   7.280472       NaN  0.113074       NaN
                                     gsp                   4.295653       NaN   7.377592       NaN  0.116710       NaN
                                     historical_tod_mean   4.291232       NaN   7.651220       NaN  0.120378       NaN
                                     neighbor_average      8.724800       NaN  13.193290       NaN  0.236597       NaN
       greedy_a_trace                gls_map               3.685447       NaN   6.094227       NaN  0.091578       NaN
                                     gsp                   4.226933       NaN   7.034376       NaN  0.112384       NaN
                                     historical_tod_mean   4.155522       NaN   7.415855       NaN  0.115481       NaN
                                     neighbor_average      8.069421       NaN  12.242143       NaN  0.237898       NaN
       greedy_d_logdet               gls_map               4.551699       NaN   7.179123       NaN  0.113873       NaN
                                     gsp                   4.300840       NaN   7.167979       NaN  0.114579       NaN
                                     historical_tod_mean   4.139385       NaN   7.448721       NaN  0.115982       NaN
                                     neighbor_average      8.957784       NaN  13.794664       NaN  0.273463       NaN
       multistart_swap_by_validation gls_map               3.575932       NaN   5.928257       NaN  0.089149       NaN
                                     gsp                   4.153060       NaN   6.986330       NaN  0.109863       NaN
                                     historical_tod_mean   4.095659       NaN   7.397631       NaN  0.114246       NaN
                                     neighbor_average      7.810426       NaN  11.744953       NaN  0.222543       NaN
       random                        gls_map               3.753041  0.086359   6.313339  0.162453  0.095748  0.003524
                                     gsp                   4.161230  0.071404   7.011767  0.112712  0.109363  0.002865
                                     historical_tod_mean   4.102650  0.068885   7.414175  0.109404  0.114317  0.002709
                                     neighbor_average      8.288358  0.224420  12.447616  0.359257  0.218889  0.009554
       rcss_selected                 gls_map               3.508528       NaN   5.946002       NaN  0.090556       NaN
                                     gsp                   4.021376       NaN   6.905130       NaN  0.107738       NaN
                                     historical_tod_mean   3.982960       NaN   7.294964       NaN  0.112244       NaN
                                     neighbor_average      7.993204       NaN  11.882816       NaN  0.207503       NaN
       robust_coverage_cvar          gls_map               3.670033       NaN   6.141420       NaN  0.095460       NaN
                                     gsp                   4.226562       NaN   7.098888       NaN  0.114308       NaN
                                     historical_tod_mean   4.159835       NaN   7.515956       NaN  0.119345       NaN
                                     neighbor_average      8.122176       NaN  12.447748       NaN  0.238533       NaN
       scenario_average_a_trace      gls_map               3.692202       NaN   6.112248       NaN  0.093827       NaN
                                     gsp                   4.170296       NaN   6.942966       NaN  0.109750       NaN
                                     historical_tod_mean   4.074142       NaN   7.360970       NaN  0.114587       NaN
                                     neighbor_average      7.998235       NaN  11.806728       NaN  0.217187       NaN
       scenario_cvar_a_trace         gls_map               3.765051       NaN   6.229674       NaN  0.096190       NaN
                                     gsp                   4.240773       NaN   7.076140       NaN  0.113214       NaN
                                     historical_tod_mean   4.172999       NaN   7.514960       NaN  0.118984       NaN
                                     neighbor_average      8.222192       NaN  12.369025       NaN  0.241112       NaN
       swap_from_best_random_trace   gls_map               3.684125       NaN   6.080088       NaN  0.091268       NaN
                                     gsp                   4.251870       NaN   7.015197       NaN  0.111226       NaN
                                     historical_tod_mean   4.141837       NaN   7.400463       NaN  0.114819       NaN
                                     neighbor_average      8.248010       NaN  12.486249       NaN  0.241773       NaN
       swap_from_greedy_a_trace      gls_map               3.606860       NaN   5.966879       NaN  0.090569       NaN
                                     gsp                   4.186807       NaN   6.990692       NaN  0.110730       NaN
                                     historical_tod_mean   4.130511       NaN   7.388169       NaN  0.114381       NaN
                                     neighbor_average      8.097650       NaN  12.433070       NaN  0.238450       NaN
       swap_from_scenario_average    gls_map               3.691277       NaN   6.098847       NaN  0.094962       NaN
                                     gsp                   4.180692       NaN   7.014377       NaN  0.112935       NaN
                                     historical_tod_mean   4.134762       NaN   7.427550       NaN  0.117229       NaN
                                     neighbor_average      7.979300       NaN  12.199478       NaN  0.236567       NaN
       swap_from_scenario_cvar       gls_map               3.685267       NaN   6.064319       NaN  0.092274       NaN
                                     gsp                   4.222609       NaN   7.016285       NaN  0.112562       NaN
                                     historical_tod_mean   4.142479       NaN   7.437349       NaN  0.117136       NaN
                                     neighbor_average      8.100479       NaN  12.371865       NaN  0.238610       NaN
       top_variance                  gls_map               3.740442       NaN   6.318046       NaN  0.088389       NaN
                                     gsp                   3.850711       NaN   6.555691       NaN  0.093113       NaN
                                     historical_tod_mean   3.712599       NaN   6.837595       NaN  0.094687       NaN
                                     neighbor_average     11.492723       NaN  17.204753       NaN  0.222096       NaN
       validation_swap_selected      gls_map               3.484125       NaN   5.784692       NaN  0.086618       NaN
                                     gsp                   4.080809       NaN   6.756034       NaN  0.105179       NaN
                                     historical_tod_mean   3.958378       NaN   7.181787       NaN  0.109745       NaN
                                     neighbor_average      8.059963       NaN  11.753024       NaN  0.205027       NaN
0.3    best_random_by_trace          gls_map               3.593941       NaN   5.990452       NaN  0.086009       NaN
                                     gsp                   4.202383       NaN   6.952895       NaN  0.104808       NaN
                                     historical_tod_mean   4.076704       NaN   7.358372       NaN  0.110571       NaN
                                     neighbor_average      7.953602       NaN  11.932308       NaN  0.219917       NaN
       best_random_by_validation     gls_map               3.325782       NaN   5.538727       NaN  0.081543       NaN
                                     gsp                   4.039185       NaN   6.796660       NaN  0.103409       NaN
                                     historical_tod_mean   3.997868       NaN   7.254991       NaN  0.108349       NaN
                                     neighbor_average      8.030187       NaN  12.012679       NaN  0.198729       NaN
       coverage                      gls_map               3.602290       NaN   5.987225       NaN  0.090380       NaN
                                     gsp                   4.210506       NaN   7.053425       NaN  0.109896       NaN
                                     historical_tod_mean   4.064899       NaN   7.477770       NaN  0.113916       NaN
                                     neighbor_average      7.971239       NaN  11.635899       NaN  0.211057       NaN
       degree                        gls_map               4.177777       NaN   6.897534       NaN  0.102550       NaN
                                     gsp                   4.324098       NaN   7.175696       NaN  0.111066       NaN
                                     historical_tod_mean   4.218119       NaN   7.512833       NaN  0.115205       NaN
                                     neighbor_average      9.856776       NaN  14.950815       NaN  0.269568       NaN
       greedy_a_trace                gls_map               3.586871       NaN   5.924244       NaN  0.089258       NaN
                                     gsp                   4.277998       NaN   7.071632       NaN  0.113594       NaN
                                     historical_tod_mean   4.182086       NaN   7.469033       NaN  0.117269       NaN
                                     neighbor_average      7.901741       NaN  12.099127       NaN  0.236394       NaN
       greedy_d_logdet               gls_map               4.171004       NaN   6.765673       NaN  0.107218       NaN
                                     gsp                   4.266866       NaN   7.136815       NaN  0.115594       NaN
                                     historical_tod_mean   4.135997       NaN   7.508482       NaN  0.118189       NaN
                                     neighbor_average      8.796478       NaN  13.453899       NaN  0.271147       NaN
       multistart_swap_by_validation gls_map               3.424012       NaN   5.725723       NaN  0.086923       NaN
                                     gsp                   4.173289       NaN   6.987554       NaN  0.111435       NaN
                                     historical_tod_mean   4.100771       NaN   7.400947       NaN  0.115240       NaN
                                     neighbor_average      7.890938       NaN  12.085400       NaN  0.230355       NaN
       random                        gls_map               3.597457  0.106346   6.065021  0.191826  0.091332  0.004085
                                     gsp                   4.170477  0.080856   6.994906  0.128394  0.109340  0.003324
                                     historical_tod_mean   4.106811  0.083629   7.418314  0.126664  0.114554  0.003287
                                     neighbor_average      8.112377  0.211439  12.238877  0.354707  0.213781  0.010485
       rcss_selected                 gls_map               3.332390       NaN   5.601416       NaN  0.083057       NaN
                                     gsp                   3.974666       NaN   6.715984       NaN  0.102987       NaN
                                     historical_tod_mean   3.945286       NaN   7.157060       NaN  0.108785       NaN
                                     neighbor_average      8.077638       NaN  12.161810       NaN  0.203862       NaN
       robust_coverage_cvar          gls_map               3.567540       NaN   5.883702       NaN  0.090624       NaN
                                     gsp                   4.228478       NaN   6.972765       NaN  0.112955       NaN
                                     historical_tod_mean   4.122082       NaN   7.424393       NaN  0.118366       NaN
                                     neighbor_average      8.093539       NaN  12.157318       NaN  0.234383       NaN
       scenario_average_a_trace      gls_map               3.500294       NaN   5.842584       NaN  0.088823       NaN
                                     gsp                   4.259442       NaN   7.034414       NaN  0.111969       NaN
                                     historical_tod_mean   4.115551       NaN   7.445432       NaN  0.115751       NaN
                                     neighbor_average      8.033888       NaN  11.928739       NaN  0.225836       NaN
       scenario_cvar_a_trace         gls_map               3.548663       NaN   5.884018       NaN  0.090725       NaN
                                     gsp                   4.214789       NaN   6.997714       NaN  0.113434       NaN
                                     historical_tod_mean   4.096192       NaN   7.433138       NaN  0.118503       NaN
                                     neighbor_average      8.167038       NaN  12.251482       NaN  0.237241       NaN
       swap_from_best_random_trace   gls_map               3.438434       NaN   5.664215       NaN  0.085823       NaN
                                     gsp                   4.229433       NaN   7.002547       NaN  0.110689       NaN
                                     historical_tod_mean   4.089430       NaN   7.411457       NaN  0.114295       NaN
                                     neighbor_average      7.908265       NaN  11.934505       NaN  0.232296       NaN
       swap_from_greedy_a_trace      gls_map               3.541613       NaN   5.807863       NaN  0.088394       NaN
                                     gsp                   4.229348       NaN   7.007503       NaN  0.112891       NaN
                                     historical_tod_mean   4.116704       NaN   7.398837       NaN  0.115931       NaN
                                     neighbor_average      7.924320       NaN  12.083293       NaN  0.235417       NaN
       swap_from_scenario_average    gls_map               3.528432       NaN   5.801032       NaN  0.087741       NaN
                                     gsp                   4.211732       NaN   6.977199       NaN  0.111256       NaN
                                     historical_tod_mean   4.117215       NaN   7.362368       NaN  0.114554       NaN
                                     neighbor_average      7.876758       NaN  11.996905       NaN  0.229732       NaN
       swap_from_scenario_cvar       gls_map               3.581323       NaN   5.796394       NaN  0.089536       NaN
                                     gsp                   4.269743       NaN   7.010157       NaN  0.113982       NaN
                                     historical_tod_mean   4.122017       NaN   7.406138       NaN  0.116867       NaN
                                     neighbor_average      8.096828       NaN  12.387734       NaN  0.244908       NaN
       top_variance                  gls_map               3.395089       NaN   5.769595       NaN  0.078965       NaN
                                     gsp                   3.626434       NaN   6.210204       NaN  0.085971       NaN
                                     historical_tod_mean   3.490963       NaN   6.478793       NaN  0.087115       NaN
                                     neighbor_average     10.739767       NaN  15.845692       NaN  0.204957       NaN
       validation_swap_selected      gls_map               3.302528       NaN   5.541334       NaN  0.082607       NaN
                                     gsp                   3.895375       NaN   6.622652       NaN  0.101803       NaN
                                     historical_tod_mean   3.867201       NaN   7.063988       NaN  0.107255       NaN
                                     neighbor_average      7.952291       NaN  12.036670       NaN  0.200905       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1    scenario_cvar_a_trace gls_map 3.762639 6.210450
    0.2 validation_swap_selected gls_map 3.484125 5.784692
    0.3 validation_swap_selected gls_map 3.302528 5.541334
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.084953     -0.103610 651
    gsp   condition_number    -0.082123     -0.099675 651
    gsp information_logdet     0.075160      0.063015 651
gls_map    posterior_trace     0.839762      0.842730 651
gls_map   condition_number     0.830719      0.843165 651
gls_map information_logdet    -0.786533     -0.796675 651
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv