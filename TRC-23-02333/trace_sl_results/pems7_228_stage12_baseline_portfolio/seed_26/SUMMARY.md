---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-08, 2012-05-25
Test days: 2012-06-27, 2012-06-29
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.744975       NaN   6.404066       NaN  0.096209       NaN
                                     gsp                   4.061280       NaN   6.907910       NaN  0.107095       NaN
                                     historical_tod_mean   4.034160       NaN   7.309035       NaN  0.112294       NaN
                                     neighbor_average      8.540218       NaN  12.278785       NaN  0.226934       NaN
       best_random_by_validation     gls_map               3.892819       NaN   6.533841       NaN  0.096509       NaN
                                     gsp                   4.125232       NaN   7.062578       NaN  0.106671       NaN
                                     historical_tod_mean   4.101669       NaN   7.425457       NaN  0.113908       NaN
                                     neighbor_average      8.674841       NaN  12.793646       NaN  0.216495       NaN
       coverage                      gls_map               4.192948       NaN   6.821798       NaN  0.105548       NaN
                                     gsp                   4.367544       NaN   7.262669       NaN  0.112518       NaN
                                     historical_tod_mean   4.129847       NaN   7.448044       NaN  0.113424       NaN
                                     neighbor_average      8.664771       NaN  12.906054       NaN  0.234110       NaN
       degree                        gls_map               4.318048       NaN   7.309279       NaN  0.115108       NaN
                                     gsp                   4.257013       NaN   7.343585       NaN  0.117241       NaN
                                     historical_tod_mean   4.185642       NaN   7.547855       NaN  0.118260       NaN
                                     neighbor_average      9.154087       NaN  13.681185       NaN  0.258396       NaN
       graph_sampling_laplacian      gls_map               4.190363       NaN   7.217025       NaN  0.111260       NaN
                                     gsp                   4.107243       NaN   7.300112       NaN  0.112758       NaN
                                     historical_tod_mean   4.106673       NaN   7.439492       NaN  0.114003       NaN
                                     neighbor_average      9.770082       NaN  15.141168       NaN  0.249309       NaN
       greedy_a_trace                gls_map               3.957969       NaN   6.592644       NaN  0.097314       NaN
                                     gsp                   4.249256       NaN   7.089050       NaN  0.110328       NaN
                                     historical_tod_mean   4.145910       NaN   7.423162       NaN  0.113771       NaN
                                     neighbor_average      8.269507       NaN  12.426874       NaN  0.235585       NaN
       greedy_d_logdet               gls_map               5.184435       NaN   8.051261       NaN  0.137363       NaN
                                     gsp                   4.343389       NaN   7.298073       NaN  0.118884       NaN
                                     historical_tod_mean   4.136067       NaN   7.446983       NaN  0.115277       NaN
                                     neighbor_average      9.082271       NaN  14.541335       NaN  0.283635       NaN
       multistart_swap_by_validation gls_map               3.767334       NaN   6.266005       NaN  0.091840       NaN
                                     gsp                   4.198871       NaN   7.052131       NaN  0.109089       NaN
                                     historical_tod_mean   4.122050       NaN   7.398492       NaN  0.113201       NaN
                                     neighbor_average      8.375687       NaN  12.581527       NaN  0.234657       NaN
       observability_proxy           gls_map               4.170985       NaN   7.151778       NaN  0.109089       NaN
                                     gsp                   4.188700       NaN   7.275293       NaN  0.114719       NaN
                                     historical_tod_mean   4.158097       NaN   7.513569       NaN  0.117146       NaN
                                     neighbor_average      8.927210       NaN  13.735218       NaN  0.258043       NaN
       qr_pod_modes                  gls_map               4.161826       NaN   6.800115       NaN  0.105527       NaN
                                     gsp                   4.248131       NaN   7.167141       NaN  0.112198       NaN
                                     historical_tod_mean   4.151516       NaN   7.439906       NaN  0.114434       NaN
                                     neighbor_average      8.233947       NaN  12.996698       NaN  0.252524       NaN
       random                        gls_map               4.029328  0.109456   6.740416  0.176002  0.104485  0.005104
                                     gsp                   4.158059  0.067682   7.098836  0.097115  0.110897  0.002905
                                     historical_tod_mean   4.108936  0.044844   7.424735  0.068362  0.114585  0.001900
                                     neighbor_average      8.576537  0.311247  12.756198  0.405017  0.228965  0.009064
       rcss_selected                 gls_map               3.749997       NaN   6.256048       NaN  0.092836       NaN
                                     gsp                   4.200468       NaN   7.075477       NaN  0.109869       NaN
                                     historical_tod_mean   4.123112       NaN   7.417593       NaN  0.113645       NaN
                                     neighbor_average      8.372275       NaN  12.557691       NaN  0.233595       NaN
       robust_coverage_cvar          gls_map               3.874045       NaN   6.376335       NaN  0.097106       NaN
                                     gsp                   4.208990       NaN   7.031572       NaN  0.108269       NaN
                                     historical_tod_mean   4.090676       NaN   7.366672       NaN  0.112137       NaN
                                     neighbor_average      8.889931       NaN  13.551824       NaN  0.245085       NaN
       scenario_average_a_trace      gls_map               4.076601       NaN   6.728415       NaN  0.101260       NaN
                                     gsp                   4.326630       NaN   7.142701       NaN  0.111503       NaN
                                     historical_tod_mean   4.153204       NaN   7.455554       NaN  0.115648       NaN
                                     neighbor_average      8.393131       NaN  12.515253       NaN  0.238026       NaN
       scenario_cvar_a_trace         gls_map               4.025722       NaN   6.611125       NaN  0.099634       NaN
                                     gsp                   4.307409       NaN   7.111604       NaN  0.109601       NaN
                                     historical_tod_mean   4.121649       NaN   7.437764       NaN  0.114442       NaN
                                     neighbor_average      8.862995       NaN  13.301238       NaN  0.254486       NaN
       swap_from_best_random_trace   gls_map               3.749997       NaN   6.256048       NaN  0.092836       NaN
                                     gsp                   4.200468       NaN   7.075477       NaN  0.109869       NaN
                                     historical_tod_mean   4.123112       NaN   7.417593       NaN  0.113645       NaN
                                     neighbor_average      8.372275       NaN  12.557691       NaN  0.233595       NaN
       swap_from_greedy_a_trace      gls_map               3.828300       NaN   6.319488       NaN  0.093615       NaN
                                     gsp                   4.219632       NaN   7.057425       NaN  0.108624       NaN
                                     historical_tod_mean   4.121484       NaN   7.410491       NaN  0.113357       NaN
                                     neighbor_average      8.281461       NaN  12.434543       NaN  0.231642       NaN
       swap_from_scenario_average    gls_map               3.867184       NaN   6.438022       NaN  0.094714       NaN
                                     gsp                   4.222411       NaN   7.108886       NaN  0.109921       NaN
                                     historical_tod_mean   4.145698       NaN   7.457418       NaN  0.114201       NaN
                                     neighbor_average      8.236743       NaN  12.180374       NaN  0.232054       NaN
       swap_from_scenario_cvar       gls_map               3.828496       NaN   6.325059       NaN  0.093940       NaN
                                     gsp                   4.226601       NaN   7.045800       NaN  0.109057       NaN
                                     historical_tod_mean   4.121605       NaN   7.408084       NaN  0.113648       NaN
                                     neighbor_average      8.278954       NaN  12.388817       NaN  0.232668       NaN
       top_variance                  gls_map               3.919561       NaN   6.705885       NaN  0.097532       NaN
                                     gsp                   3.937447       NaN   6.872174       NaN  0.101352       NaN
                                     historical_tod_mean   3.918025       NaN   7.167072       NaN  0.104506       NaN
                                     neighbor_average     12.753115       NaN  18.857490       NaN  0.250722       NaN
       validation_swap_selected      gls_map               3.704001       NaN   6.122452       NaN  0.090201       NaN
                                     gsp                   4.167039       NaN   6.895536       NaN  0.105826       NaN
                                     historical_tod_mean   4.041364       NaN   7.288048       NaN  0.111155       NaN
                                     neighbor_average      8.549101       NaN  12.549204       NaN  0.231998       NaN
0.2    best_random_by_trace          gls_map               3.683615       NaN   6.322105       NaN  0.098930       NaN
                                     gsp                   4.149393       NaN   7.090292       NaN  0.113997       NaN
                                     historical_tod_mean   4.129480       NaN   7.459122       NaN  0.116302       NaN
                                     neighbor_average      7.766001       NaN  11.873323       NaN  0.218078       NaN
       best_random_by_validation     gls_map               3.604148       NaN   6.112823       NaN  0.090930       NaN
                                     gsp                   4.041339       NaN   6.903774       NaN  0.105879       NaN
                                     historical_tod_mean   3.988847       NaN   7.301657       NaN  0.109780       NaN
                                     neighbor_average      8.187574       NaN  12.239104       NaN  0.202594       NaN
       coverage                      gls_map               3.937599       NaN   6.393685       NaN  0.098598       NaN
                                     gsp                   4.352678       NaN   7.146895       NaN  0.112886       NaN
                                     historical_tod_mean   4.139534       NaN   7.515295       NaN  0.115751       NaN
                                     neighbor_average      8.129188       NaN  12.037892       NaN  0.219860       NaN
       degree                        gls_map               4.269667       NaN   7.280472       NaN  0.113074       NaN
                                     gsp                   4.295653       NaN   7.377592       NaN  0.116710       NaN
                                     historical_tod_mean   4.291232       NaN   7.651220       NaN  0.120378       NaN
                                     neighbor_average      8.724800       NaN  13.193290       NaN  0.236597       NaN
       graph_sampling_laplacian      gls_map               4.096448       NaN   6.927766       NaN  0.105777       NaN
                                     gsp                   4.040042       NaN   7.081088       NaN  0.108571       NaN
                                     historical_tod_mean   4.034454       NaN   7.384833       NaN  0.112072       NaN
                                     neighbor_average      8.399974       NaN  12.262366       NaN  0.227741       NaN
       greedy_a_trace                gls_map               3.685447       NaN   6.094227       NaN  0.091578       NaN
                                     gsp                   4.226933       NaN   7.034376       NaN  0.112384       NaN
                                     historical_tod_mean   4.155522       NaN   7.415855       NaN  0.115481       NaN
                                     neighbor_average      8.069421       NaN  12.242143       NaN  0.237898       NaN
       greedy_d_logdet               gls_map               4.551699       NaN   7.179123       NaN  0.113873       NaN
                                     gsp                   4.300840       NaN   7.167979       NaN  0.114579       NaN
                                     historical_tod_mean   4.139385       NaN   7.448721       NaN  0.115982       NaN
                                     neighbor_average      8.957784       NaN  13.794664       NaN  0.273463       NaN
       multistart_swap_by_validation gls_map               3.542361       NaN   5.812463       NaN  0.087150       NaN
                                     gsp                   4.169817       NaN   6.936597       NaN  0.107632       NaN
                                     historical_tod_mean   4.092960       NaN   7.375878       NaN  0.112936       NaN
                                     neighbor_average      7.882034       NaN  11.765248       NaN  0.219555       NaN
       observability_proxy           gls_map               4.089698       NaN   6.821236       NaN  0.104959       NaN
                                     gsp                   4.268458       NaN   7.306302       NaN  0.117114       NaN
                                     historical_tod_mean   4.259199       NaN   7.668067       NaN  0.121540       NaN
                                     neighbor_average      9.405769       NaN  13.684798       NaN  0.260648       NaN
       qr_pod_modes                  gls_map               3.955328       NaN   6.429593       NaN  0.100530       NaN
                                     gsp                   4.237213       NaN   7.047997       NaN  0.113037       NaN
                                     historical_tod_mean   4.108526       NaN   7.389218       NaN  0.114715       NaN
                                     neighbor_average      8.219903       NaN  12.446767       NaN  0.245180       NaN
       random                        gls_map               3.759468  0.089545   6.335525  0.162656  0.096044  0.003627
                                     gsp                   4.161553  0.067717   7.025689  0.112241  0.109670  0.003110
                                     historical_tod_mean   4.107801  0.064803   7.426828  0.104535  0.114647  0.002747
                                     neighbor_average      8.269464  0.237147  12.439048  0.346167  0.219824  0.010421
       rcss_selected                 gls_map               3.575158       NaN   6.012163       NaN  0.092384       NaN
                                     gsp                   4.168624       NaN   7.042613       NaN  0.112579       NaN
                                     historical_tod_mean   4.125821       NaN   7.435536       NaN  0.115875       NaN
                                     neighbor_average      7.746376       NaN  11.883006       NaN  0.227245       NaN
       robust_coverage_cvar          gls_map               3.779437       NaN   6.250069       NaN  0.094554       NaN
                                     gsp                   4.260102       NaN   7.024068       NaN  0.109704       NaN
                                     historical_tod_mean   4.111361       NaN   7.408067       NaN  0.113722       NaN
                                     neighbor_average      8.348081       NaN  12.766930       NaN  0.238839       NaN
       scenario_average_a_trace      gls_map               3.844733       NaN   6.301194       NaN  0.095347       NaN
                                     gsp                   4.353071       NaN   7.086278       NaN  0.110725       NaN
                                     historical_tod_mean   4.158385       NaN   7.413078       NaN  0.114954       NaN
                                     neighbor_average      8.634027       NaN  13.401295       NaN  0.259307       NaN
       scenario_cvar_a_trace         gls_map               3.772909       NaN   6.252257       NaN  0.093533       NaN
                                     gsp                   4.292173       NaN   7.071738       NaN  0.109293       NaN
                                     historical_tod_mean   4.119740       NaN   7.454039       NaN  0.115160       NaN
                                     neighbor_average      8.329673       NaN  12.477772       NaN  0.245210       NaN
       swap_from_best_random_trace   gls_map               3.575158       NaN   6.012163       NaN  0.092384       NaN
                                     gsp                   4.168624       NaN   7.042613       NaN  0.112579       NaN
                                     historical_tod_mean   4.125821       NaN   7.435536       NaN  0.115875       NaN
                                     neighbor_average      7.746376       NaN  11.883006       NaN  0.227245       NaN
       swap_from_greedy_a_trace      gls_map               3.606860       NaN   5.966879       NaN  0.090569       NaN
                                     gsp                   4.186807       NaN   6.990692       NaN  0.110730       NaN
                                     historical_tod_mean   4.130511       NaN   7.388169       NaN  0.114381       NaN
                                     neighbor_average      8.097650       NaN  12.433070       NaN  0.238450       NaN
       swap_from_scenario_average    gls_map               3.660780       NaN   6.023961       NaN  0.091868       NaN
                                     gsp                   4.227285       NaN   7.039059       NaN  0.112157       NaN
                                     historical_tod_mean   4.142026       NaN   7.399210       NaN  0.114966       NaN
                                     neighbor_average      8.125936       NaN  12.612623       NaN  0.243499       NaN
       swap_from_scenario_cvar       gls_map               3.589058       NaN   5.974170       NaN  0.090863       NaN
                                     gsp                   4.191057       NaN   7.014171       NaN  0.110845       NaN
                                     historical_tod_mean   4.122476       NaN   7.418025       NaN  0.115110       NaN
                                     neighbor_average      7.949953       NaN  12.272751       NaN  0.236189       NaN
       top_variance                  gls_map               3.740442       NaN   6.318046       NaN  0.088389       NaN
                                     gsp                   3.850711       NaN   6.555691       NaN  0.093113       NaN
                                     historical_tod_mean   3.712599       NaN   6.837595       NaN  0.094687       NaN
                                     neighbor_average     11.492723       NaN  17.204753       NaN  0.222096       NaN
       validation_swap_selected      gls_map               3.574419       NaN   6.024149       NaN  0.089793       NaN
                                     gsp                   3.974697       NaN   6.844620       NaN  0.104780       NaN
                                     historical_tod_mean   3.922887       NaN   7.233415       NaN  0.108530       NaN
                                     neighbor_average      8.426091       NaN  12.445402       NaN  0.202962       NaN
0.3    best_random_by_trace          gls_map               3.633642       NaN   5.978012       NaN  0.091331       NaN
                                     gsp                   4.322565       NaN   7.081667       NaN  0.110959       NaN
                                     historical_tod_mean   4.159371       NaN   7.485702       NaN  0.114129       NaN
                                     neighbor_average      7.969355       NaN  12.038300       NaN  0.212646       NaN
       best_random_by_validation     gls_map               3.459331       NaN   5.844415       NaN  0.087592       NaN
                                     gsp                   4.035639       NaN   6.834201       NaN  0.105651       NaN
                                     historical_tod_mean   3.995315       NaN   7.235998       NaN  0.110983       NaN
                                     neighbor_average      8.199807       NaN  12.567896       NaN  0.210850       NaN
       coverage                      gls_map               3.602290       NaN   5.987225       NaN  0.090380       NaN
                                     gsp                   4.210506       NaN   7.053425       NaN  0.109896       NaN
                                     historical_tod_mean   4.064899       NaN   7.477770       NaN  0.113916       NaN
                                     neighbor_average      7.971239       NaN  11.635899       NaN  0.211057       NaN
       degree                        gls_map               4.177777       NaN   6.897534       NaN  0.102550       NaN
                                     gsp                   4.324098       NaN   7.175696       NaN  0.111066       NaN
                                     historical_tod_mean   4.218119       NaN   7.512833       NaN  0.115205       NaN
                                     neighbor_average      9.856776       NaN  14.950815       NaN  0.269568       NaN
       graph_sampling_laplacian      gls_map               3.998972       NaN   6.698069       NaN  0.102124       NaN
                                     gsp                   4.059296       NaN   7.031977       NaN  0.108471       NaN
                                     historical_tod_mean   4.060729       NaN   7.424877       NaN  0.113354       NaN
                                     neighbor_average      8.308958       NaN  12.622960       NaN  0.223679       NaN
       greedy_a_trace                gls_map               3.586871       NaN   5.924244       NaN  0.089258       NaN
                                     gsp                   4.277998       NaN   7.071632       NaN  0.113594       NaN
                                     historical_tod_mean   4.182086       NaN   7.469033       NaN  0.117269       NaN
                                     neighbor_average      7.901741       NaN  12.099127       NaN  0.236394       NaN
       greedy_d_logdet               gls_map               4.171004       NaN   6.765673       NaN  0.107218       NaN
                                     gsp                   4.266866       NaN   7.136815       NaN  0.115594       NaN
                                     historical_tod_mean   4.135997       NaN   7.508482       NaN  0.118189       NaN
                                     neighbor_average      8.796478       NaN  13.453899       NaN  0.271147       NaN
       multistart_swap_by_validation gls_map               3.469173       NaN   5.657362       NaN  0.085842       NaN
                                     gsp                   4.134663       NaN   6.861154       NaN  0.108160       NaN
                                     historical_tod_mean   4.061539       NaN   7.263980       NaN  0.111913       NaN
                                     neighbor_average      7.895688       NaN  12.001688       NaN  0.222979       NaN
       observability_proxy           gls_map               4.084820       NaN   6.801511       NaN  0.102208       NaN
                                     gsp                   4.287555       NaN   7.237758       NaN  0.113507       NaN
                                     historical_tod_mean   4.252863       NaN   7.613224       NaN  0.119040       NaN
                                     neighbor_average      9.622852       NaN  13.681952       NaN  0.249083       NaN
       qr_pod_modes                  gls_map               3.615829       NaN   5.741831       NaN  0.089253       NaN
                                     gsp                   4.163019       NaN   6.923868       NaN  0.110246       NaN
                                     historical_tod_mean   4.079755       NaN   7.371993       NaN  0.114751       NaN
                                     neighbor_average      8.042386       NaN  11.979830       NaN  0.233022       NaN
       random                        gls_map               3.582841  0.100356   6.007292  0.164889  0.090359  0.003641
                                     gsp                   4.163870  0.092727   6.964302  0.121275  0.108609  0.003285
                                     historical_tod_mean   4.094615  0.086530   7.389403  0.122257  0.113810  0.003477
                                     neighbor_average      8.132613  0.200050  12.282294  0.342390  0.214793  0.008377
       rcss_selected                 gls_map               3.469173       NaN   5.657362       NaN  0.085842       NaN
                                     gsp                   4.134663       NaN   6.861154       NaN  0.108160       NaN
                                     historical_tod_mean   4.061539       NaN   7.263980       NaN  0.111913       NaN
                                     neighbor_average      7.895688       NaN  12.001688       NaN  0.222979       NaN
       robust_coverage_cvar          gls_map               3.729252       NaN   6.131925       NaN  0.093392       NaN
                                     gsp                   4.281334       NaN   7.021215       NaN  0.111030       NaN
                                     historical_tod_mean   4.129556       NaN   7.445379       NaN  0.115579       NaN
                                     neighbor_average      8.135246       NaN  12.282004       NaN  0.228426       NaN
       scenario_average_a_trace      gls_map               3.657511       NaN   5.907808       NaN  0.089092       NaN
                                     gsp                   4.295450       NaN   6.991558       NaN  0.109931       NaN
                                     historical_tod_mean   4.098462       NaN   7.353895       NaN  0.114303       NaN
                                     neighbor_average      8.669450       NaN  13.238883       NaN  0.249253       NaN
       scenario_cvar_a_trace         gls_map               3.685051       NaN   6.077497       NaN  0.090715       NaN
                                     gsp                   4.317207       NaN   7.078287       NaN  0.111552       NaN
                                     historical_tod_mean   4.133554       NaN   7.489440       NaN  0.117168       NaN
                                     neighbor_average      8.368833       NaN  12.494672       NaN  0.246962       NaN
       swap_from_best_random_trace   gls_map               3.520962       NaN   5.772931       NaN  0.089582       NaN
                                     gsp                   4.303832       NaN   7.135878       NaN  0.116133       NaN
                                     historical_tod_mean   4.199858       NaN   7.516096       NaN  0.118398       NaN
                                     neighbor_average      7.951318       NaN  12.063908       NaN  0.234276       NaN
       swap_from_greedy_a_trace      gls_map               3.541613       NaN   5.807863       NaN  0.088394       NaN
                                     gsp                   4.229348       NaN   7.007503       NaN  0.112891       NaN
                                     historical_tod_mean   4.116704       NaN   7.398837       NaN  0.115931       NaN
                                     neighbor_average      7.924320       NaN  12.083293       NaN  0.235417       NaN
       swap_from_scenario_average    gls_map               3.499416       NaN   5.725920       NaN  0.085626       NaN
                                     gsp                   4.230436       NaN   6.997837       NaN  0.110338       NaN
                                     historical_tod_mean   4.140059       NaN   7.394227       NaN  0.114564       NaN
                                     neighbor_average      7.730091       NaN  11.849291       NaN  0.226422       NaN
       swap_from_scenario_cvar       gls_map               3.473891       NaN   5.681360       NaN  0.087391       NaN
                                     gsp                   4.221284       NaN   7.038531       NaN  0.112864       NaN
                                     historical_tod_mean   4.107609       NaN   7.454180       NaN  0.116549       NaN
                                     neighbor_average      7.914825       NaN  11.939926       NaN  0.233665       NaN
       top_variance                  gls_map               3.395089       NaN   5.769595       NaN  0.078965       NaN
                                     gsp                   3.626434       NaN   6.210204       NaN  0.085971       NaN
                                     historical_tod_mean   3.490963       NaN   6.478793       NaN  0.087115       NaN
                                     neighbor_average     10.739767       NaN  15.845692       NaN  0.204957       NaN
       validation_swap_selected      gls_map               3.240575       NaN   5.555034       NaN  0.079842       NaN
                                     gsp                   3.929792       NaN   6.724882       NaN  0.101365       NaN
                                     historical_tod_mean   3.912135       NaN   7.172717       NaN  0.106924       NaN
                                     neighbor_average      8.075170       NaN  12.079601       NaN  0.193837       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1      validation_swap_selected gls_map 3.704001 6.122452
    0.2 multistart_swap_by_validation gls_map 3.542361 5.812463
    0.3      validation_swap_selected gls_map 3.240575 5.555034
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.016002      0.001266 210
    gsp   condition_number     0.020170      0.039900 210
    gsp information_logdet    -0.038182     -0.040098 210
gls_map    posterior_trace     0.771330      0.787448 210
gls_map   condition_number     0.834514      0.843090 210
gls_map information_logdet    -0.660949     -0.747552 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv