---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-06-18, 2012-06-19
Test days: 2012-05-25, 2012-06-29
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               4.146838       NaN   7.066268       NaN  0.115654       NaN
                                     gsp                   4.617138       NaN   7.965192       NaN  0.129886       NaN
                                     historical_tod_mean   4.686416       NaN   8.479259       NaN  0.136097       NaN
                                     neighbor_average      7.913032       NaN  12.014864       NaN  0.231506       NaN
       best_random_by_validation     gls_map               4.258243       NaN   7.241566       NaN  0.114424       NaN
                                     gsp                   4.560921       NaN   7.928877       NaN  0.124104       NaN
                                     historical_tod_mean   4.671628       NaN   8.479129       NaN  0.134066       NaN
                                     neighbor_average      8.083614       NaN  11.780576       NaN  0.209302       NaN
       coverage                      gls_map               4.456309       NaN   7.384309       NaN  0.117597       NaN
                                     gsp                   4.791092       NaN   8.110627       NaN  0.128694       NaN
                                     historical_tod_mean   4.712857       NaN   8.507181       NaN  0.133781       NaN
                                     neighbor_average      8.261009       NaN  12.450881       NaN  0.223445       NaN
       degree                        gls_map               4.624159       NaN   7.879874       NaN  0.128464       NaN
                                     gsp                   4.758754       NaN   8.235271       NaN  0.135381       NaN
                                     historical_tod_mean   4.770138       NaN   8.603220       NaN  0.139208       NaN
                                     neighbor_average      8.701711       NaN  13.299455       NaN  0.256088       NaN
       graph_sampling_laplacian      gls_map               4.505955       NaN   7.753685       NaN  0.122237       NaN
                                     gsp                   4.551299       NaN   7.951216       NaN  0.123733       NaN
                                     historical_tod_mean   4.630241       NaN   8.372287       NaN  0.130751       NaN
                                     neighbor_average      9.507364       NaN  14.882331       NaN  0.241793       NaN
       greedy_a_trace                gls_map               4.263794       NaN   7.081383       NaN  0.109610       NaN
                                     gsp                   4.707268       NaN   8.021518       NaN  0.126427       NaN
                                     historical_tod_mean   4.708900       NaN   8.472371       NaN  0.132981       NaN
                                     neighbor_average      8.034824       NaN  12.093551       NaN  0.232113       NaN
       greedy_d_logdet               gls_map               5.697575       NaN   8.798607       NaN  0.148169       NaN
                                     gsp                   4.796704       NaN   8.143494       NaN  0.130277       NaN
                                     historical_tod_mean   4.707177       NaN   8.433918       NaN  0.133426       NaN
                                     neighbor_average      8.580112       NaN  13.734243       NaN  0.266174       NaN
       multistart_swap_by_validation gls_map               4.167916       NaN   6.858906       NaN  0.106430       NaN
                                     gsp                   4.693651       NaN   7.968217       NaN  0.125309       NaN
                                     historical_tod_mean   4.680549       NaN   8.422216       NaN  0.131678       NaN
                                     neighbor_average      7.930572       NaN  12.149713       NaN  0.222262       NaN
       observability_proxy           gls_map               4.488292       NaN   7.726194       NaN  0.125247       NaN
                                     gsp                   4.740021       NaN   8.231872       NaN  0.135213       NaN
                                     historical_tod_mean   4.734874       NaN   8.557478       NaN  0.137972       NaN
                                     neighbor_average      8.481364       NaN  13.145137       NaN  0.252264       NaN
       qr_pod_modes                  gls_map               4.429435       NaN   7.232148       NaN  0.117868       NaN
                                     gsp                   4.726063       NaN   7.996594       NaN  0.128800       NaN
                                     historical_tod_mean   4.744505       NaN   8.473867       NaN  0.134582       NaN
                                     neighbor_average      7.971994       NaN  12.882099       NaN  0.253942       NaN
       random                        gls_map               4.307527  0.097998   7.228162  0.151099  0.115492  0.004434
                                     gsp                   4.608969  0.066251   7.922125  0.096448  0.125884  0.003231
                                     historical_tod_mean   4.672492  0.045580   8.430387  0.072481  0.133463  0.002443
                                     neighbor_average      8.011787  0.320821  12.059054  0.390521  0.218467  0.010117
       rcss_selected                 gls_map               4.111615       NaN   6.836586       NaN  0.103708       NaN
                                     gsp                   4.696850       NaN   7.963106       NaN  0.124631       NaN
                                     historical_tod_mean   4.705955       NaN   8.438156       NaN  0.131616       NaN
                                     neighbor_average      7.823396       NaN  12.081322       NaN  0.222638       NaN
       robust_coverage_cvar          gls_map               4.066760       NaN   6.997856       NaN  0.115384       NaN
                                     gsp                   4.570062       NaN   7.971882       NaN  0.128740       NaN
                                     historical_tod_mean   4.685970       NaN   8.431944       NaN  0.135687       NaN
                                     neighbor_average      8.019823       NaN  12.214201       NaN  0.234538       NaN
       scenario_average_a_trace      gls_map               4.194318       NaN   7.055545       NaN  0.108588       NaN
                                     gsp                   4.711832       NaN   7.957176       NaN  0.124970       NaN
                                     historical_tod_mean   4.662488       NaN   8.403481       NaN  0.131676       NaN
                                     neighbor_average      7.770495       NaN  11.630174       NaN  0.217037       NaN
       scenario_cvar_a_trace         gls_map               4.325269       NaN   7.117532       NaN  0.108060       NaN
                                     gsp                   4.707738       NaN   7.987757       NaN  0.122502       NaN
                                     historical_tod_mean   4.709499       NaN   8.436180       NaN  0.130933       NaN
                                     neighbor_average      8.004027       NaN  12.240272       NaN  0.225950       NaN
       swap_from_best_random_trace   gls_map               4.106249       NaN   6.853138       NaN  0.105353       NaN
                                     gsp                   4.616194       NaN   7.988451       NaN  0.125020       NaN
                                     historical_tod_mean   4.704776       NaN   8.474040       NaN  0.133473       NaN
                                     neighbor_average      7.707192       NaN  11.892157       NaN  0.220495       NaN
       swap_from_greedy_a_trace      gls_map               4.111615       NaN   6.836586       NaN  0.103708       NaN
                                     gsp                   4.696850       NaN   7.963106       NaN  0.124631       NaN
                                     historical_tod_mean   4.705955       NaN   8.438156       NaN  0.131616       NaN
                                     neighbor_average      7.823396       NaN  12.081322       NaN  0.222638       NaN
       swap_from_scenario_average    gls_map               4.107133       NaN   6.747504       NaN  0.101608       NaN
                                     gsp                   4.676728       NaN   7.870570       NaN  0.122575       NaN
                                     historical_tod_mean   4.657673       NaN   8.354706       NaN  0.129901       NaN
                                     neighbor_average      7.972026       NaN  12.042452       NaN  0.220967       NaN
       swap_from_scenario_cvar       gls_map               4.105271       NaN   6.845943       NaN  0.104952       NaN
                                     gsp                   4.692067       NaN   8.008707       NaN  0.126540       NaN
                                     historical_tod_mean   4.684346       NaN   8.429267       NaN  0.132394       NaN
                                     neighbor_average      7.716691       NaN  11.785244       NaN  0.223615       NaN
       top_variance                  gls_map               4.205793       NaN   7.171621       NaN  0.110906       NaN
                                     gsp                   4.325964       NaN   7.553655       NaN  0.114925       NaN
                                     historical_tod_mean   4.414966       NaN   8.019319       NaN  0.120884       NaN
                                     neighbor_average     11.966483       NaN  17.788367       NaN  0.233538       NaN
       validation_swap_selected      gls_map               4.097072       NaN   6.798302       NaN  0.102524       NaN
                                     gsp                   4.650948       NaN   7.904158       NaN  0.123126       NaN
                                     historical_tod_mean   4.685435       NaN   8.403042       NaN  0.130771       NaN
                                     neighbor_average      8.050928       NaN  12.383428       NaN  0.227636       NaN
0.2    best_random_by_trace          gls_map               3.933960       NaN   6.801427       NaN  0.111005       NaN
                                     gsp                   4.615328       NaN   8.007065       NaN  0.130366       NaN
                                     historical_tod_mean   4.720163       NaN   8.587725       NaN  0.139299       NaN
                                     neighbor_average      7.632252       NaN  11.794089       NaN  0.228024       NaN
       best_random_by_validation     gls_map               3.893249       NaN   6.470389       NaN  0.102259       NaN
                                     gsp                   4.542648       NaN   7.760608       NaN  0.121634       NaN
                                     historical_tod_mean   4.619267       NaN   8.381119       NaN  0.132632       NaN
                                     neighbor_average      7.565971       NaN  11.493945       NaN  0.204622       NaN
       coverage                      gls_map               4.201577       NaN   6.838985       NaN  0.109401       NaN
                                     gsp                   4.747114       NaN   7.938764       NaN  0.126853       NaN
                                     historical_tod_mean   4.712184       NaN   8.544455       NaN  0.135429       NaN
                                     neighbor_average      7.677987       NaN  11.440182       NaN  0.206727       NaN
       degree                        gls_map               4.657375       NaN   7.890898       NaN  0.125085       NaN
                                     gsp                   4.902242       NaN   8.351113       NaN  0.134679       NaN
                                     historical_tod_mean   4.871136       NaN   8.640349       NaN  0.136987       NaN
                                     neighbor_average      8.342003       NaN  12.745249       NaN  0.228609       NaN
       graph_sampling_laplacian      gls_map               4.404453       NaN   7.502931       NaN  0.117494       NaN
                                     gsp                   4.524794       NaN   7.886588       NaN  0.122717       NaN
                                     historical_tod_mean   4.576175       NaN   8.368809       NaN  0.129868       NaN
                                     neighbor_average      8.019585       NaN  11.888831       NaN  0.218426       NaN
       greedy_a_trace                gls_map               3.865812       NaN   6.379643       NaN  0.100693       NaN
                                     gsp                   4.673961       NaN   7.928503       NaN  0.127854       NaN
                                     historical_tod_mean   4.746911       NaN   8.502795       NaN  0.135910       NaN
                                     neighbor_average      7.554245       NaN  11.578185       NaN  0.226578       NaN
       greedy_d_logdet               gls_map               4.918198       NaN   7.720535       NaN  0.123633       NaN
                                     gsp                   4.773176       NaN   8.068813       NaN  0.127671       NaN
                                     historical_tod_mean   4.776122       NaN   8.544652       NaN  0.136225       NaN
                                     neighbor_average      8.428296       NaN  13.118376       NaN  0.258894       NaN
       multistart_swap_by_validation gls_map               3.842670       NaN   6.277646       NaN  0.095405       NaN
                                     gsp                   4.561221       NaN   7.750807       NaN  0.120016       NaN
                                     historical_tod_mean   4.637148       NaN   8.333651       NaN  0.128744       NaN
                                     neighbor_average      7.474721       NaN  11.327964       NaN  0.202352       NaN
       observability_proxy           gls_map               4.384102       NaN   7.337254       NaN  0.117566       NaN
                                     gsp                   4.816673       NaN   8.240655       NaN  0.135151       NaN
                                     historical_tod_mean   4.847710       NaN   8.696150       NaN  0.140492       NaN
                                     neighbor_average      9.081579       NaN  13.376111       NaN  0.254431       NaN
       qr_pod_modes                  gls_map               4.287982       NaN   6.881484       NaN  0.114437       NaN
                                     gsp                   4.692004       NaN   7.976872       NaN  0.128527       NaN
                                     historical_tod_mean   4.743009       NaN   8.523035       NaN  0.136666       NaN
                                     neighbor_average      7.836593       NaN  12.366740       NaN  0.242250       NaN
       random                        gls_map               4.016263  0.090035   6.764207  0.157388  0.106811  0.004316
                                     gsp                   4.607951  0.060740   7.835838  0.103776  0.124785  0.003666
                                     historical_tod_mean   4.682163  0.057527   8.441944  0.093508  0.133816  0.003235
                                     neighbor_average      7.740690  0.192925  11.806990  0.355951  0.207879  0.009658
       rcss_selected                 gls_map               3.723789       NaN   6.157506       NaN  0.097343       NaN
                                     gsp                   4.417775       NaN   7.448055       NaN  0.117182       NaN
                                     historical_tod_mean   4.441318       NaN   8.104303       NaN  0.125876       NaN
                                     neighbor_average      7.719105       NaN  11.637057       NaN  0.185673       NaN
       robust_coverage_cvar          gls_map               3.794974       NaN   6.450884       NaN  0.105129       NaN
                                     gsp                   4.621687       NaN   7.826931       NaN  0.128469       NaN
                                     historical_tod_mean   4.718019       NaN   8.418312       NaN  0.137529       NaN
                                     neighbor_average      7.669424       NaN  11.978899       NaN  0.227479       NaN
       scenario_average_a_trace      gls_map               3.829590       NaN   6.410132       NaN  0.099023       NaN
                                     gsp                   4.655330       NaN   7.829982       NaN  0.124310       NaN
                                     historical_tod_mean   4.668865       NaN   8.378971       NaN  0.132777       NaN
                                     neighbor_average      7.466454       NaN  11.441499       NaN  0.218319       NaN
       scenario_cvar_a_trace         gls_map               4.132168       NaN   6.827380       NaN  0.103126       NaN
                                     gsp                   4.670781       NaN   7.859208       NaN  0.120300       NaN
                                     historical_tod_mean   4.727618       NaN   8.411231       NaN  0.130151       NaN
                                     neighbor_average      7.856931       NaN  12.530843       NaN  0.224423       NaN
       swap_from_best_random_trace   gls_map               3.755688       NaN   6.178864       NaN  0.094006       NaN
                                     gsp                   4.594169       NaN   7.798343       NaN  0.122410       NaN
                                     historical_tod_mean   4.655723       NaN   8.381966       NaN  0.131272       NaN
                                     neighbor_average      7.292885       NaN  11.212352       NaN  0.211172       NaN
       swap_from_greedy_a_trace      gls_map               3.870240       NaN   6.384192       NaN  0.100145       NaN
                                     gsp                   4.664970       NaN   7.911197       NaN  0.126721       NaN
                                     historical_tod_mean   4.750212       NaN   8.495343       NaN  0.135320       NaN
                                     neighbor_average      7.635484       NaN  11.919022       NaN  0.228732       NaN
       swap_from_scenario_average    gls_map               3.930131       NaN   6.447951       NaN  0.100833       NaN
                                     gsp                   4.684827       NaN   7.897701       NaN  0.126614       NaN
                                     historical_tod_mean   4.730169       NaN   8.471473       NaN  0.134780       NaN
                                     neighbor_average      7.532030       NaN  11.744859       NaN  0.224377       NaN
       swap_from_scenario_cvar       gls_map               3.800574       NaN   6.317024       NaN  0.097153       NaN
                                     gsp                   4.617911       NaN   7.827246       NaN  0.123909       NaN
                                     historical_tod_mean   4.707159       NaN   8.429974       NaN  0.133335       NaN
                                     neighbor_average      7.521867       NaN  11.497487       NaN  0.218849       NaN
       top_variance                  gls_map               3.816933       NaN   6.530741       NaN  0.098531       NaN
                                     gsp                   4.159334       NaN   7.150742       NaN  0.106332       NaN
                                     historical_tod_mean   4.158381       NaN   7.611365       NaN  0.110939       NaN
                                     neighbor_average     10.042670       NaN  15.203198       NaN  0.196542       NaN
       validation_swap_selected      gls_map               3.700011       NaN   6.107908       NaN  0.096908       NaN
                                     gsp                   4.381276       NaN   7.422919       NaN  0.116377       NaN
                                     historical_tod_mean   4.417978       NaN   8.082028       NaN  0.125273       NaN
                                     neighbor_average      7.860796       NaN  11.729340       NaN  0.186961       NaN
0.3    best_random_by_trace          gls_map               3.706170       NaN   6.186582       NaN  0.095670       NaN
                                     gsp                   4.502774       NaN   7.787929       NaN  0.122502       NaN
                                     historical_tod_mean   4.701839       NaN   8.449399       NaN  0.132943       NaN
                                     neighbor_average      7.275094       NaN  11.269110       NaN  0.186780       NaN
       best_random_by_validation     gls_map               3.552695       NaN   6.047804       NaN  0.091298       NaN
                                     gsp                   4.446093       NaN   7.609377       NaN  0.115788       NaN
                                     historical_tod_mean   4.529721       NaN   8.269398       NaN  0.125667       NaN
                                     neighbor_average      7.366393       NaN  11.541855       NaN  0.190763       NaN
       coverage                      gls_map               3.806704       NaN   6.411484       NaN  0.103862       NaN
                                     gsp                   4.644217       NaN   7.905038       NaN  0.127701       NaN
                                     historical_tod_mean   4.674158       NaN   8.578350       NaN  0.136621       NaN
                                     neighbor_average      7.463980       NaN  11.075168       NaN  0.203315       NaN
       degree                        gls_map               4.521138       NaN   7.503551       NaN  0.115946       NaN
                                     gsp                   4.869665       NaN   8.177030       NaN  0.130078       NaN
                                     historical_tod_mean   4.852692       NaN   8.627510       NaN  0.134667       NaN
                                     neighbor_average      9.365191       NaN  14.389403       NaN  0.260815       NaN
       graph_sampling_laplacian      gls_map               4.286786       NaN   7.332501       NaN  0.115417       NaN
                                     gsp                   4.578388       NaN   7.952507       NaN  0.125019       NaN
                                     historical_tod_mean   4.638451       NaN   8.474486       NaN  0.132980       NaN
                                     neighbor_average      7.783628       NaN  12.118265       NaN  0.213492       NaN
       greedy_a_trace                gls_map               3.719473       NaN   6.152408       NaN  0.095422       NaN
                                     gsp                   4.714421       NaN   7.927271       NaN  0.126201       NaN
                                     historical_tod_mean   4.796933       NaN   8.557272       NaN  0.136774       NaN
                                     neighbor_average      7.346101       NaN  11.475415       NaN  0.222421       NaN
       greedy_d_logdet               gls_map               4.450373       NaN   6.997698       NaN  0.112164       NaN
                                     gsp                   4.752883       NaN   8.038446       NaN  0.127558       NaN
                                     historical_tod_mean   4.808596       NaN   8.617856       NaN  0.137644       NaN
                                     neighbor_average      8.225374       NaN  12.700045       NaN  0.252925       NaN
       multistart_swap_by_validation gls_map               3.627480       NaN   5.983590       NaN  0.096038       NaN
                                     gsp                   4.582864       NaN   7.867190       NaN  0.127238       NaN
                                     historical_tod_mean   4.701553       NaN   8.522227       NaN  0.137324       NaN
                                     neighbor_average      7.097226       NaN  10.909529       NaN  0.207951       NaN
       observability_proxy           gls_map               4.440117       NaN   7.389589       NaN  0.115847       NaN
                                     gsp                   4.811830       NaN   8.159087       NaN  0.131388       NaN
                                     historical_tod_mean   4.856947       NaN   8.657823       NaN  0.137402       NaN
                                     neighbor_average      8.980400       NaN  13.005362       NaN  0.240507       NaN
       qr_pod_modes                  gls_map               3.852801       NaN   6.355566       NaN  0.103024       NaN
                                     gsp                   4.640953       NaN   7.930943       NaN  0.127076       NaN
                                     historical_tod_mean   4.739558       NaN   8.571360       NaN  0.138093       NaN
                                     neighbor_average      7.470558       NaN  11.549354       NaN  0.227832       NaN
       random                        gls_map               3.799972  0.110718   6.430439  0.206477  0.101162  0.005351
                                     gsp                   4.589854  0.091139   7.794210  0.134905  0.124240  0.004790
                                     historical_tod_mean   4.675355  0.092416   8.436038  0.135921  0.133831  0.004601
                                     neighbor_average      7.565974  0.172225  11.662933  0.278643  0.203194  0.011596
       rcss_selected                 gls_map               3.627480       NaN   5.983590       NaN  0.096038       NaN
                                     gsp                   4.582864       NaN   7.867190       NaN  0.127238       NaN
                                     historical_tod_mean   4.701553       NaN   8.522227       NaN  0.137324       NaN
                                     neighbor_average      7.097226       NaN  10.909529       NaN  0.207951       NaN
       robust_coverage_cvar          gls_map               3.683123       NaN   6.017513       NaN  0.095159       NaN
                                     gsp                   4.591491       NaN   7.641065       NaN  0.123507       NaN
                                     historical_tod_mean   4.674129       NaN   8.304291       NaN  0.133600       NaN
                                     neighbor_average      7.758675       NaN  12.165626       NaN  0.230335       NaN
       scenario_average_a_trace      gls_map               3.688932       NaN   6.159756       NaN  0.095857       NaN
                                     gsp                   4.673063       NaN   7.838974       NaN  0.125442       NaN
                                     historical_tod_mean   4.721499       NaN   8.469501       NaN  0.135520       NaN
                                     neighbor_average      7.527835       NaN  11.691760       NaN  0.222070       NaN
       scenario_cvar_a_trace         gls_map               3.802329       NaN   6.319530       NaN  0.095587       NaN
                                     gsp                   4.575317       NaN   7.629323       NaN  0.117375       NaN
                                     historical_tod_mean   4.630581       NaN   8.258415       NaN  0.127430       NaN
                                     neighbor_average      7.842551       NaN  12.265670       NaN  0.224161       NaN
       swap_from_best_random_trace   gls_map               3.703412       NaN   6.079184       NaN  0.095528       NaN
                                     gsp                   4.667745       NaN   7.959029       NaN  0.126409       NaN
                                     historical_tod_mean   4.796205       NaN   8.590223       NaN  0.136421       NaN
                                     neighbor_average      7.318363       NaN  11.474071       NaN  0.210090       NaN
       swap_from_greedy_a_trace      gls_map               3.714051       NaN   5.948893       NaN  0.093133       NaN
                                     gsp                   4.636919       NaN   7.747360       NaN  0.122749       NaN
                                     historical_tod_mean   4.716807       NaN   8.383907       NaN  0.133122       NaN
                                     neighbor_average      7.255391       NaN  11.336513       NaN  0.215551       NaN
       swap_from_scenario_average    gls_map               3.644080       NaN   6.000182       NaN  0.092807       NaN
                                     gsp                   4.648627       NaN   7.841561       NaN  0.123820       NaN
                                     historical_tod_mean   4.738051       NaN   8.481682       NaN  0.135022       NaN
                                     neighbor_average      7.304241       NaN  11.440733       NaN  0.217810       NaN
       swap_from_scenario_cvar       gls_map               3.689482       NaN   6.131773       NaN  0.095369       NaN
                                     gsp                   4.632916       NaN   7.832285       NaN  0.124346       NaN
                                     historical_tod_mean   4.748102       NaN   8.497987       NaN  0.135519       NaN
                                     neighbor_average      7.487755       NaN  11.505058       NaN  0.218642       NaN
       top_variance                  gls_map               3.549512       NaN   6.163670       NaN  0.090183       NaN
                                     gsp                   4.003619       NaN   6.940504       NaN  0.100843       NaN
                                     historical_tod_mean   3.984544       NaN   7.334492       NaN  0.104303       NaN
                                     neighbor_average      9.637074       NaN  14.608080       NaN  0.190437       NaN
       validation_swap_selected      gls_map               3.404525       NaN   5.736074       NaN  0.088994       NaN
                                     gsp                   4.287147       NaN   7.280698       NaN  0.115930       NaN
                                     historical_tod_mean   4.388486       NaN   7.938903       NaN  0.124949       NaN
                                     neighbor_average      7.332951       NaN  11.045903       NaN  0.187108       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1     robust_coverage_cvar gls_map 4.066760 6.997856
    0.2 validation_swap_selected gls_map 3.700011 6.107908
    0.3 validation_swap_selected gls_map 3.404525 5.736074
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.129931      0.129198 210
    gsp   condition_number     0.136027      0.229137 210
    gsp information_logdet    -0.163022     -0.220235 210
gls_map    posterior_trace     0.784109      0.814988 210
gls_map   condition_number     0.837528      0.861453 210
gls_map information_logdet    -0.679517     -0.762944 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv