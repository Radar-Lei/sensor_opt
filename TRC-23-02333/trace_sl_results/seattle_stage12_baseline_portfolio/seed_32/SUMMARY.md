---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-03, 2015-01-13
Test days: 2015-01-02, 2015-01-15
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.528901       NaN   5.854552       NaN  0.119704       NaN
                                     gsp                  4.395646       NaN   7.223081       NaN  0.158897       NaN
                                     historical_tod_mean  5.468702       NaN   9.321449       NaN  0.217809       NaN
                                     neighbor_average     6.037485       NaN   9.757207       NaN  0.193138       NaN
       best_random_by_validation     gls_map              3.442599       NaN   5.481369       NaN  0.108739       NaN
                                     gsp                  4.258245       NaN   6.882240       NaN  0.148581       NaN
                                     historical_tod_mean  5.351393       NaN   9.132345       NaN  0.212067       NaN
                                     neighbor_average     6.040459       NaN   9.366000       NaN  0.177044       NaN
       coverage                      gls_map              3.495461       NaN   5.689593       NaN  0.116258       NaN
                                     gsp                  4.397751       NaN   7.278967       NaN  0.162630       NaN
                                     historical_tod_mean  5.480652       NaN   9.347231       NaN  0.222680       NaN
                                     neighbor_average     5.741886       NaN   8.851417       NaN  0.193924       NaN
       degree                        gls_map              3.823868       NaN   6.155016       NaN  0.129156       NaN
                                     gsp                  4.325974       NaN   6.994818       NaN  0.155005       NaN
                                     historical_tod_mean  5.404338       NaN   9.231074       NaN  0.219601       NaN
                                     neighbor_average     6.753030       NaN  10.698104       NaN  0.235070       NaN
       graph_sampling_laplacian      gls_map              4.256492       NaN   6.884697       NaN  0.152844       NaN
                                     gsp                  4.665803       NaN   7.728556       NaN  0.177975       NaN
                                     historical_tod_mean  5.562399       NaN   9.498055       NaN  0.232258       NaN
                                     neighbor_average     6.543973       NaN  10.740119       NaN  0.247874       NaN
       greedy_a_trace                gls_map              3.321831       NaN   5.435730       NaN  0.110143       NaN
                                     gsp                  4.338912       NaN   7.115313       NaN  0.157834       NaN
                                     historical_tod_mean  5.428018       NaN   9.268649       NaN  0.220311       NaN
                                     neighbor_average     5.549950       NaN   8.644225       NaN  0.184435       NaN
       greedy_d_logdet               gls_map              4.179845       NaN   6.588136       NaN  0.126368       NaN
                                     gsp                  4.568910       NaN   7.350765       NaN  0.155654       NaN
                                     historical_tod_mean  5.581892       NaN   9.416966       NaN  0.221519       NaN
                                     neighbor_average     6.487868       NaN  10.585783       NaN  0.249481       NaN
       multistart_swap_by_validation gls_map              3.269264       NaN   5.309776       NaN  0.106470       NaN
                                     gsp                  4.332744       NaN   7.104120       NaN  0.157315       NaN
                                     historical_tod_mean  5.433402       NaN   9.260464       NaN  0.220814       NaN
                                     neighbor_average     5.889974       NaN   9.130559       NaN  0.189602       NaN
       observability_proxy           gls_map              3.768574       NaN   6.164082       NaN  0.129529       NaN
                                     gsp                  4.347613       NaN   7.027850       NaN  0.155995       NaN
                                     historical_tod_mean  5.408165       NaN   9.228502       NaN  0.220357       NaN
                                     neighbor_average     6.784997       NaN  10.912373       NaN  0.217358       NaN
       qr_pod_modes                  gls_map              3.930123       NaN   6.309381       NaN  0.125647       NaN
                                     gsp                  4.504327       NaN   7.264328       NaN  0.156050       NaN
                                     historical_tod_mean  5.539792       NaN   9.378895       NaN  0.224211       NaN
                                     neighbor_average     6.256421       NaN  10.177292       NaN  0.231446       NaN
       random                        gls_map              3.554325  0.077268   5.813097  0.150255  0.120393  0.005228
                                     gsp                  4.371680  0.040218   7.177672  0.113506  0.159650  0.004816
                                     historical_tod_mean  5.446981  0.039211   9.303406  0.064372  0.221461  0.003869
                                     neighbor_average     6.016807  0.241882   9.602320  0.370146  0.198932  0.012349
       rcss_selected                 gls_map              3.285274       NaN   5.319040       NaN  0.105551       NaN
                                     gsp                  4.340881       NaN   7.105088       NaN  0.157039       NaN
                                     historical_tod_mean  5.438274       NaN   9.264845       NaN  0.219546       NaN
                                     neighbor_average     5.882546       NaN   9.040784       NaN  0.187600       NaN
       robust_coverage_cvar          gls_map              3.487892       NaN   5.671099       NaN  0.116432       NaN
                                     gsp                  4.375082       NaN   7.156412       NaN  0.157074       NaN
                                     historical_tod_mean  5.488557       NaN   9.343478       NaN  0.222219       NaN
                                     neighbor_average     5.669512       NaN   9.022063       NaN  0.203174       NaN
       scenario_average_a_trace      gls_map              3.536236       NaN   5.723842       NaN  0.116465       NaN
                                     gsp                  4.409611       NaN   7.179453       NaN  0.156626       NaN
                                     historical_tod_mean  5.493925       NaN   9.319122       NaN  0.221705       NaN
                                     neighbor_average     6.061223       NaN   9.695859       NaN  0.220103       NaN
       scenario_cvar_a_trace         gls_map              3.501799       NaN   5.795707       NaN  0.118357       NaN
                                     gsp                  4.388097       NaN   7.176250       NaN  0.157220       NaN
                                     historical_tod_mean  5.479643       NaN   9.320911       NaN  0.220621       NaN
                                     neighbor_average     5.674108       NaN   9.253619       NaN  0.198863       NaN
       swap_from_best_random_trace   gls_map              3.302262       NaN   5.412298       NaN  0.109008       NaN
                                     gsp                  4.363730       NaN   7.176321       NaN  0.159823       NaN
                                     historical_tod_mean  5.454691       NaN   9.297795       NaN  0.220154       NaN
                                     neighbor_average     5.855886       NaN   9.237508       NaN  0.191347       NaN
       swap_from_greedy_a_trace      gls_map              3.321268       NaN   5.445279       NaN  0.110493       NaN
                                     gsp                  4.340802       NaN   7.124697       NaN  0.158432       NaN
                                     historical_tod_mean  5.447205       NaN   9.280941       NaN  0.220798       NaN
                                     neighbor_average     5.829215       NaN   9.060399       NaN  0.192476       NaN
       swap_from_scenario_average    gls_map              3.285274       NaN   5.319040       NaN  0.105551       NaN
                                     gsp                  4.340881       NaN   7.105088       NaN  0.157039       NaN
                                     historical_tod_mean  5.438274       NaN   9.264845       NaN  0.219546       NaN
                                     neighbor_average     5.882546       NaN   9.040784       NaN  0.187600       NaN
       swap_from_scenario_cvar       gls_map              3.342461       NaN   5.447093       NaN  0.111028       NaN
                                     gsp                  4.330459       NaN   7.097089       NaN  0.155756       NaN
                                     historical_tod_mean  5.438578       NaN   9.247500       NaN  0.218259       NaN
                                     neighbor_average     5.848872       NaN   9.320402       NaN  0.192334       NaN
       top_variance                  gls_map              3.751095       NaN   6.024907       NaN  0.123539       NaN
                                     gsp                  4.176776       NaN   6.876827       NaN  0.146853       NaN
                                     historical_tod_mean  5.051654       NaN   8.692966       NaN  0.188246       NaN
                                     neighbor_average     9.472950       NaN  15.240876       NaN  0.197715       NaN
       validation_swap_selected      gls_map              3.273620       NaN   5.312751       NaN  0.107252       NaN
                                     gsp                  4.315162       NaN   7.095446       NaN  0.157847       NaN
                                     historical_tod_mean  5.419135       NaN   9.250543       NaN  0.220673       NaN
                                     neighbor_average     5.934546       NaN   9.195355       NaN  0.191071       NaN
0.2    best_random_by_trace          gls_map              3.168510       NaN   5.199150       NaN  0.103615       NaN
                                     gsp                  4.377583       NaN   7.026370       NaN  0.154221       NaN
                                     historical_tod_mean  5.476262       NaN   9.358219       NaN  0.222210       NaN
                                     neighbor_average     5.423166       NaN   8.419055       NaN  0.157424       NaN
       best_random_by_validation     gls_map              3.073188       NaN   5.020528       NaN  0.099588       NaN
                                     gsp                  4.218092       NaN   6.791292       NaN  0.145193       NaN
                                     historical_tod_mean  5.299810       NaN   9.095101       NaN  0.209533       NaN
                                     neighbor_average     5.298506       NaN   8.471610       NaN  0.149128       NaN
       coverage                      gls_map              3.047894       NaN   4.933680       NaN  0.098534       NaN
                                     gsp                  4.311157       NaN   6.937230       NaN  0.152325       NaN
                                     historical_tod_mean  5.474931       NaN   9.322004       NaN  0.223474       NaN
                                     neighbor_average     4.792041       NaN   7.474378       NaN  0.153501       NaN
       degree                        gls_map              3.827392       NaN   6.141033       NaN  0.124658       NaN
                                     gsp                  4.381760       NaN   6.816857       NaN  0.148581       NaN
                                     historical_tod_mean  5.398768       NaN   9.150235       NaN  0.219045       NaN
                                     neighbor_average     6.867684       NaN  11.015506       NaN  0.231686       NaN
       graph_sampling_laplacian      gls_map              4.023005       NaN   6.625150       NaN  0.150663       NaN
                                     gsp                  4.603427       NaN   7.563178       NaN  0.174869       NaN
                                     historical_tod_mean  5.646097       NaN   9.676585       NaN  0.242228       NaN
                                     neighbor_average     6.793260       NaN  11.018779       NaN  0.266796       NaN
       greedy_a_trace                gls_map              3.070368       NaN   4.929271       NaN  0.094972       NaN
                                     gsp                  4.410700       NaN   7.009741       NaN  0.150029       NaN
                                     historical_tod_mean  5.540633       NaN   9.370170       NaN  0.221037       NaN
                                     neighbor_average     4.992334       NaN   7.878698       NaN  0.168572       NaN
       greedy_d_logdet               gls_map              3.840463       NaN   5.919796       NaN  0.118131       NaN
                                     gsp                  4.604671       NaN   7.185077       NaN  0.150105       NaN
                                     historical_tod_mean  5.693626       NaN   9.511079       NaN  0.225170       NaN
                                     neighbor_average     5.873061       NaN   9.683934       NaN  0.229989       NaN
       multistart_swap_by_validation gls_map              3.077808       NaN   4.986037       NaN  0.100017       NaN
                                     gsp                  4.346615       NaN   6.947698       NaN  0.150606       NaN
                                     historical_tod_mean  5.465537       NaN   9.304391       NaN  0.219506       NaN
                                     neighbor_average     4.966212       NaN   7.942690       NaN  0.168011       NaN
       observability_proxy           gls_map              3.651868       NaN   5.845474       NaN  0.117861       NaN
                                     gsp                  4.357082       NaN   6.835079       NaN  0.148994       NaN
                                     historical_tod_mean  5.384398       NaN   9.149144       NaN  0.218140       NaN
                                     neighbor_average     6.933831       NaN  11.050929       NaN  0.214915       NaN
       qr_pod_modes                  gls_map              3.403375       NaN   5.280237       NaN  0.099670       NaN
                                     gsp                  4.496146       NaN   7.029251       NaN  0.147296       NaN
                                     historical_tod_mean  5.605878       NaN   9.375873       NaN  0.220243       NaN
                                     neighbor_average     5.431633       NaN   8.717771       NaN  0.190186       NaN
       random                        gls_map              3.211251  0.064748   5.254110  0.144008  0.106238  0.005505
                                     gsp                  4.332018  0.041587   6.952394  0.095211  0.152384  0.005632
                                     historical_tod_mean  5.446929  0.054218   9.311118  0.090142  0.221894  0.005804
                                     neighbor_average     5.363834  0.169412   8.552529  0.303914  0.169901  0.010905
       rcss_selected                 gls_map              3.077808       NaN   4.986037       NaN  0.100017       NaN
                                     gsp                  4.346615       NaN   6.947698       NaN  0.150606       NaN
                                     historical_tod_mean  5.465537       NaN   9.304391       NaN  0.219506       NaN
                                     neighbor_average     4.966212       NaN   7.942690       NaN  0.168011       NaN
       robust_coverage_cvar          gls_map              3.187546       NaN   5.153738       NaN  0.104159       NaN
                                     gsp                  4.413842       NaN   7.029796       NaN  0.152980       NaN
                                     historical_tod_mean  5.559339       NaN   9.420146       NaN  0.225894       NaN
                                     neighbor_average     5.095064       NaN   8.063863       NaN  0.171065       NaN
       scenario_average_a_trace      gls_map              3.325677       NaN   5.310218       NaN  0.107226       NaN
                                     gsp                  4.480927       NaN   7.153595       NaN  0.154818       NaN
                                     historical_tod_mean  5.627518       NaN   9.487807       NaN  0.227020       NaN
                                     neighbor_average     5.497186       NaN   8.819641       NaN  0.203774       NaN
       scenario_cvar_a_trace         gls_map              3.308730       NaN   5.414436       NaN  0.108886       NaN
                                     gsp                  4.460072       NaN   7.095528       NaN  0.154237       NaN
                                     historical_tod_mean  5.618546       NaN   9.478024       NaN  0.226927       NaN
                                     neighbor_average     5.344763       NaN   8.593097       NaN  0.181729       NaN
       swap_from_best_random_trace   gls_map              3.123765       NaN   4.967353       NaN  0.097318       NaN
                                     gsp                  4.421077       NaN   6.983050       NaN  0.148757       NaN
                                     historical_tod_mean  5.537257       NaN   9.356755       NaN  0.221465       NaN
                                     neighbor_average     5.381818       NaN   8.569522       NaN  0.166428       NaN
       swap_from_greedy_a_trace      gls_map              3.088231       NaN   4.821125       NaN  0.093213       NaN
                                     gsp                  4.378772       NaN   6.908285       NaN  0.146136       NaN
                                     historical_tod_mean  5.514322       NaN   9.276682       NaN  0.216576       NaN
                                     neighbor_average     4.950006       NaN   7.893869       NaN  0.162176       NaN
       swap_from_scenario_average    gls_map              3.157334       NaN   5.045034       NaN  0.100072       NaN
                                     gsp                  4.435804       NaN   7.053456       NaN  0.152467       NaN
                                     historical_tod_mean  5.591583       NaN   9.421760       NaN  0.224480       NaN
                                     neighbor_average     5.178369       NaN   8.425451       NaN  0.183137       NaN
       swap_from_scenario_cvar       gls_map              3.196741       NaN   5.052859       NaN  0.101375       NaN
                                     gsp                  4.433043       NaN   6.986122       NaN  0.152539       NaN
                                     historical_tod_mean  5.581471       NaN   9.391883       NaN  0.226450       NaN
                                     neighbor_average     5.230775       NaN   8.334869       NaN  0.178541       NaN
       top_variance                  gls_map              3.282739       NaN   5.447836       NaN  0.105972       NaN
                                     gsp                  3.968551       NaN   6.411134       NaN  0.130330       NaN
                                     historical_tod_mean  4.766479       NaN   8.226300       NaN  0.168693       NaN
                                     neighbor_average     7.470420       NaN  12.184163       NaN  0.162612       NaN
       validation_swap_selected      gls_map              3.033305       NaN   4.941951       NaN  0.098707       NaN
                                     gsp                  4.284960       NaN   6.867063       NaN  0.147747       NaN
                                     historical_tod_mean  5.395780       NaN   9.222244       NaN  0.215884       NaN
                                     neighbor_average     5.018345       NaN   7.908065       NaN  0.164491       NaN
0.3    best_random_by_trace          gls_map              3.024189       NaN   5.019163       NaN  0.100229       NaN
                                     gsp                  4.348636       NaN   6.971598       NaN  0.154683       NaN
                                     historical_tod_mean  5.508526       NaN   9.408684       NaN  0.225549       NaN
                                     neighbor_average     4.995198       NaN   7.996491       NaN  0.154321       NaN
       best_random_by_validation     gls_map              2.901490       NaN   4.719638       NaN  0.091761       NaN
                                     gsp                  4.215093       NaN   6.682541       NaN  0.143496       NaN
                                     historical_tod_mean  5.302685       NaN   9.047227       NaN  0.212742       NaN
                                     neighbor_average     4.713862       NaN   7.641569       NaN  0.136276       NaN
       coverage                      gls_map              2.811494       NaN   4.519077       NaN  0.088225       NaN
                                     gsp                  4.318334       NaN   6.828060       NaN  0.147001       NaN
                                     historical_tod_mean  5.433064       NaN   9.264196       NaN  0.221004       NaN
                                     neighbor_average     4.680356       NaN   7.175166       NaN  0.134934       NaN
       degree                        gls_map              3.636172       NaN   5.727888       NaN  0.107418       NaN
                                     gsp                  4.376420       NaN   6.679935       NaN  0.134215       NaN
                                     historical_tod_mean  5.337623       NaN   8.911523       NaN  0.196515       NaN
                                     neighbor_average     7.720801       NaN  12.323910       NaN  0.209017       NaN
       graph_sampling_laplacian      gls_map              3.828792       NaN   6.422942       NaN  0.146439       NaN
                                     gsp                  4.560338       NaN   7.500356       NaN  0.175273       NaN
                                     historical_tod_mean  5.664863       NaN   9.764554       NaN  0.249335       NaN
                                     neighbor_average     6.910560       NaN  11.217518       NaN  0.266254       NaN
       greedy_a_trace                gls_map              2.913811       NaN   4.546836       NaN  0.085185       NaN
                                     gsp                  4.476759       NaN   6.970705       NaN  0.144824       NaN
                                     historical_tod_mean  5.637822       NaN   9.430328       NaN  0.220924       NaN
                                     neighbor_average     4.602926       NaN   7.224722       NaN  0.153475       NaN
       greedy_d_logdet               gls_map              3.550037       NaN   5.463465       NaN  0.108912       NaN
                                     gsp                  4.687090       NaN   7.240357       NaN  0.153772       NaN
                                     historical_tod_mean  5.805225       NaN   9.633512       NaN  0.232306       NaN
                                     neighbor_average     5.630545       NaN   9.391171       NaN  0.217713       NaN
       multistart_swap_by_validation gls_map              2.886547       NaN   4.617140       NaN  0.088271       NaN
                                     gsp                  4.350222       NaN   6.828133       NaN  0.145609       NaN
                                     historical_tod_mean  5.467993       NaN   9.287310       NaN  0.220300       NaN
                                     neighbor_average     4.546644       NaN   7.165186       NaN  0.143219       NaN
       observability_proxy           gls_map              3.617746       NaN   5.697858       NaN  0.107376       NaN
                                     gsp                  4.371172       NaN   6.695495       NaN  0.135207       NaN
                                     historical_tod_mean  5.333916       NaN   8.923871       NaN  0.197495       NaN
                                     neighbor_average     7.567816       NaN  12.142617       NaN  0.207191       NaN
       qr_pod_modes                  gls_map              2.999193       NaN   4.634857       NaN  0.088929       NaN
                                     gsp                  4.492936       NaN   6.976125       NaN  0.143363       NaN
                                     historical_tod_mean  5.636042       NaN   9.400247       NaN  0.217962       NaN
                                     neighbor_average     4.727475       NaN   7.511042       NaN  0.158132       NaN
       random                        gls_map              3.025443  0.067591   4.978731  0.165858  0.099461  0.005634
                                     gsp                  4.329047  0.061483   6.888001  0.106909  0.150755  0.005453
                                     historical_tod_mean  5.437116  0.065564   9.300899  0.111333  0.222433  0.006778
                                     neighbor_average     4.986021  0.128138   7.974097  0.254912  0.152201  0.009811
       rcss_selected                 gls_map              2.804950       NaN   4.516406       NaN  0.086998       NaN
                                     gsp                  4.187552       NaN   6.683633       NaN  0.141471       NaN
                                     historical_tod_mean  5.262925       NaN   9.077198       NaN  0.207140       NaN
                                     neighbor_average     5.039137       NaN   7.817484       NaN  0.133159       NaN
       robust_coverage_cvar          gls_map              3.018358       NaN   4.906731       NaN  0.095559       NaN
                                     gsp                  4.495190       NaN   7.084465       NaN  0.151591       NaN
                                     historical_tod_mean  5.674015       NaN   9.554267       NaN  0.227233       NaN
                                     neighbor_average     4.702939       NaN   7.580480       NaN  0.162434       NaN
       scenario_average_a_trace      gls_map              3.137955       NaN   4.968189       NaN  0.098560       NaN
                                     gsp                  4.583889       NaN   7.171902       NaN  0.153690       NaN
                                     historical_tod_mean  5.744972       NaN   9.623356       NaN  0.231893       NaN
                                     neighbor_average     5.032867       NaN   8.224516       NaN  0.186299       NaN
       scenario_cvar_a_trace         gls_map              3.103281       NaN   4.987887       NaN  0.097256       NaN
                                     gsp                  4.553795       NaN   7.143109       NaN  0.151384       NaN
                                     historical_tod_mean  5.717814       NaN   9.571916       NaN  0.226213       NaN
                                     neighbor_average     4.837561       NaN   7.916140       NaN  0.170629       NaN
       swap_from_best_random_trace   gls_map              2.919328       NaN   4.663445       NaN  0.089228       NaN
                                     gsp                  4.449717       NaN   6.984056       NaN  0.148142       NaN
                                     historical_tod_mean  5.636196       NaN   9.498970       NaN  0.223632       NaN
                                     neighbor_average     4.727445       NaN   7.435718       NaN  0.153060       NaN
       swap_from_greedy_a_trace      gls_map              2.903776       NaN   4.523516       NaN  0.086706       NaN
                                     gsp                  4.456342       NaN   6.936469       NaN  0.144845       NaN
                                     historical_tod_mean  5.633539       NaN   9.417192       NaN  0.221087       NaN
                                     neighbor_average     4.647231       NaN   7.355528       NaN  0.156725       NaN
       swap_from_scenario_average    gls_map              2.876726       NaN   4.467067       NaN  0.085830       NaN
                                     gsp                  4.425437       NaN   6.902269       NaN  0.144106       NaN
                                     historical_tod_mean  5.577733       NaN   9.360080       NaN  0.218863       NaN
                                     neighbor_average     4.664360       NaN   7.371047       NaN  0.154728       NaN
       swap_from_scenario_cvar       gls_map              2.895364       NaN   4.482391       NaN  0.086303       NaN
                                     gsp                  4.443330       NaN   6.910448       NaN  0.144725       NaN
                                     historical_tod_mean  5.592857       NaN   9.365325       NaN  0.219919       NaN
                                     neighbor_average     4.657271       NaN   7.266810       NaN  0.153352       NaN
       top_variance                  gls_map              3.013735       NaN   5.047932       NaN  0.094095       NaN
                                     gsp                  3.766895       NaN   6.074734       NaN  0.115956       NaN
                                     historical_tod_mean  4.553772       NaN   7.834174       NaN  0.149265       NaN
                                     neighbor_average     6.434045       NaN  10.555988       NaN  0.134830       NaN
       validation_swap_selected      gls_map              2.722363       NaN   4.364278       NaN  0.083625       NaN
                                     gsp                  4.093063       NaN   6.488772       NaN  0.136928       NaN
                                     historical_tod_mean  5.168426       NaN   8.849410       NaN  0.201247       NaN
                                     neighbor_average     4.666433       NaN   7.176356       NaN  0.123221       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1 multistart_swap_by_validation gls_map 3.269264 5.309776
    0.2      validation_swap_selected gls_map 3.033305 4.941951
    0.3      validation_swap_selected gls_map 2.722363 4.364278
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.133164      0.156471 210
    gsp   condition_number     0.135146      0.173291 210
    gsp information_logdet    -0.084198     -0.110241 210
gls_map    posterior_trace     0.859474      0.862192 210
gls_map   condition_number     0.882262      0.892173 210
gls_map information_logdet    -0.764178     -0.806283 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv