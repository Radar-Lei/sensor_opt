---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-21, 2012-05-16
Test days: 2012-05-11, 2012-05-14
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape          
                                                               mean       std       mean       std      mean       std
budget layout_type                   method                                                                           
0.1    best_random_by_trace          gls_map               3.848272       NaN   6.502257       NaN  0.095276       NaN
                                     gsp                   4.113534       NaN   6.964206       NaN  0.101447       NaN
                                     historical_tod_mean   4.206141       NaN   7.441423       NaN  0.107015       NaN
                                     neighbor_average      7.229047       NaN  11.062485       NaN  0.191388       NaN
       best_random_by_validation     gls_map               3.716631       NaN   6.346588       NaN  0.094654       NaN
                                     gsp                   3.917248       NaN   6.804509       NaN  0.099424       NaN
                                     historical_tod_mean   4.087275       NaN   7.282126       NaN  0.103897       NaN
                                     neighbor_average      7.392417       NaN  11.514083       NaN  0.186148       NaN
       coverage                      gls_map               3.962150       NaN   6.691198       NaN  0.098815       NaN
                                     gsp                   4.047868       NaN   7.015191       NaN  0.102471       NaN
                                     historical_tod_mean   4.179729       NaN   7.441585       NaN  0.107101       NaN
                                     neighbor_average      7.609647       NaN  11.700131       NaN  0.204800       NaN
       degree                        gls_map               4.144662       NaN   7.050771       NaN  0.107697       NaN
                                     gsp                   4.168706       NaN   7.091238       NaN  0.103669       NaN
                                     historical_tod_mean   4.206654       NaN   7.440047       NaN  0.107678       NaN
                                     neighbor_average      8.270752       NaN  12.674822       NaN  0.222807       NaN
       graph_sampling_laplacian      gls_map               4.099444       NaN   6.986571       NaN  0.100366       NaN
                                     gsp                   4.002989       NaN   6.846756       NaN  0.099486       NaN
                                     historical_tod_mean   4.091371       NaN   7.232421       NaN  0.102119       NaN
                                     neighbor_average      9.083617       NaN  14.415610       NaN  0.220937       NaN
       greedy_a_trace                gls_map               3.568196       NaN   6.098406       NaN  0.089937       NaN
                                     gsp                   4.079055       NaN   6.934218       NaN  0.100550       NaN
                                     historical_tod_mean   4.188650       NaN   7.376992       NaN  0.106329       NaN
                                     neighbor_average      7.130705       NaN  10.978255       NaN  0.197354       NaN
       greedy_d_logdet               gls_map               4.258759       NaN   6.963611       NaN  0.104708       NaN
                                     gsp                   4.164994       NaN   7.083275       NaN  0.100957       NaN
                                     historical_tod_mean   4.176906       NaN   7.377455       NaN  0.106235       NaN
                                     neighbor_average      7.743199       NaN  12.560200       NaN  0.230898       NaN
       multistart_swap_by_validation gls_map               3.561644       NaN   6.051308       NaN  0.091016       NaN
                                     gsp                   4.052146       NaN   6.895209       NaN  0.101046       NaN
                                     historical_tod_mean   4.183551       NaN   7.389896       NaN  0.106539       NaN
                                     neighbor_average      7.204685       NaN  11.210069       NaN  0.195815       NaN
       observability_proxy           gls_map               4.048982       NaN   6.806204       NaN  0.102484       NaN
                                     gsp                   4.149754       NaN   7.030878       NaN  0.101152       NaN
                                     historical_tod_mean   4.163678       NaN   7.337833       NaN  0.105149       NaN
                                     neighbor_average      7.979914       NaN  12.433245       NaN  0.208455       NaN
       qr_pod_modes                  gls_map               3.824492       NaN   6.356143       NaN  0.097490       NaN
                                     gsp                   4.092699       NaN   6.917217       NaN  0.100253       NaN
                                     historical_tod_mean   4.171536       NaN   7.326290       NaN  0.105075       NaN
                                     neighbor_average      7.190045       NaN  11.664496       NaN  0.212238       NaN
       random                        gls_map               3.805220  0.093282   6.481082  0.141190  0.096250  0.002837
                                     gsp                   4.019650  0.061973   6.931526  0.091929  0.101396  0.001949
                                     historical_tod_mean   4.164984  0.040219   7.393653  0.060287  0.106263  0.001450
                                     neighbor_average      7.526301  0.236417  11.644317  0.327760  0.196652  0.008576
       rcss_selected                 gls_map               3.561644       NaN   6.051308       NaN  0.091016       NaN
                                     gsp                   4.052146       NaN   6.895209       NaN  0.101046       NaN
                                     historical_tod_mean   4.183551       NaN   7.389896       NaN  0.106539       NaN
                                     neighbor_average      7.204685       NaN  11.210069       NaN  0.195815       NaN
       robust_coverage_cvar          gls_map               3.624428       NaN   6.180547       NaN  0.090521       NaN
                                     gsp                   3.987325       NaN   6.841203       NaN  0.098698       NaN
                                     historical_tod_mean   4.136229       NaN   7.354607       NaN  0.105169       NaN
                                     neighbor_average      7.952674       NaN  11.808036       NaN  0.198220       NaN
       scenario_average_a_trace      gls_map               3.871433       NaN   6.487164       NaN  0.096540       NaN
                                     gsp                   4.013646       NaN   6.944985       NaN  0.102922       NaN
                                     historical_tod_mean   4.178971       NaN   7.405282       NaN  0.106328       NaN
                                     neighbor_average      7.603957       NaN  11.423572       NaN  0.204986       NaN
       scenario_cvar_a_trace         gls_map               3.706348       NaN   6.389492       NaN  0.095231       NaN
                                     gsp                   4.051606       NaN   6.945328       NaN  0.101496       NaN
                                     historical_tod_mean   4.182924       NaN   7.420732       NaN  0.107294       NaN
                                     neighbor_average      7.324098       NaN  11.520773       NaN  0.203315       NaN
       swap_from_best_random_trace   gls_map               3.534005       NaN   6.074593       NaN  0.089626       NaN
                                     gsp                   4.071740       NaN   6.904487       NaN  0.101039       NaN
                                     historical_tod_mean   4.178210       NaN   7.341989       NaN  0.105588       NaN
                                     neighbor_average      7.182699       NaN  11.275080       NaN  0.199279       NaN
       swap_from_greedy_a_trace      gls_map               3.534005       NaN   6.074593       NaN  0.089626       NaN
                                     gsp                   4.071740       NaN   6.904487       NaN  0.101039       NaN
                                     historical_tod_mean   4.178210       NaN   7.341989       NaN  0.105588       NaN
                                     neighbor_average      7.182699       NaN  11.275080       NaN  0.199279       NaN
       swap_from_scenario_average    gls_map               3.530578       NaN   6.019097       NaN  0.087979       NaN
                                     gsp                   4.055935       NaN   6.857788       NaN  0.100123       NaN
                                     historical_tod_mean   4.162788       NaN   7.308877       NaN  0.104460       NaN
                                     neighbor_average      7.327033       NaN  11.449141       NaN  0.200025       NaN
       swap_from_scenario_cvar       gls_map               3.619742       NaN   6.131884       NaN  0.091000       NaN
                                     gsp                   4.078260       NaN   6.934111       NaN  0.100884       NaN
                                     historical_tod_mean   4.195723       NaN   7.388140       NaN  0.106338       NaN
                                     neighbor_average      7.272583       NaN  11.343422       NaN  0.202555       NaN
       top_variance                  gls_map               3.719811       NaN   6.466041       NaN  0.088628       NaN
                                     gsp                   3.845896       NaN   6.644353       NaN  0.092170       NaN
                                     historical_tod_mean   3.927284       NaN   7.013532       NaN  0.095451       NaN
                                     neighbor_average     11.166549       NaN  16.926798       NaN  0.213926       NaN
       validation_swap_selected      gls_map               3.517308       NaN   5.966180       NaN  0.088605       NaN
                                     gsp                   4.002609       NaN   6.814332       NaN  0.096779       NaN
                                     historical_tod_mean   4.117929       NaN   7.269708       NaN  0.103553       NaN
                                     neighbor_average      7.281292       NaN  11.231874       NaN  0.189529       NaN
0.2    best_random_by_trace          gls_map               3.461721       NaN   5.996225       NaN  0.086892       NaN
                                     gsp                   4.011870       NaN   6.925378       NaN  0.099860       NaN
                                     historical_tod_mean   4.221772       NaN   7.451502       NaN  0.106956       NaN
                                     neighbor_average      6.991910       NaN  11.022404       NaN  0.183580       NaN
       best_random_by_validation     gls_map               3.347817       NaN   5.661988       NaN  0.083474       NaN
                                     gsp                   3.939111       NaN   6.674547       NaN  0.098935       NaN
                                     historical_tod_mean   4.092338       NaN   7.263425       NaN  0.104071       NaN
                                     neighbor_average      7.036768       NaN  10.851533       NaN  0.185318       NaN
       coverage                      gls_map               3.587637       NaN   6.190443       NaN  0.091069       NaN
                                     gsp                   4.042309       NaN   6.951600       NaN  0.100973       NaN
                                     historical_tod_mean   4.195469       NaN   7.484669       NaN  0.108007       NaN
                                     neighbor_average      7.185229       NaN  11.118703       NaN  0.189546       NaN
       degree                        gls_map               4.124089       NaN   6.861998       NaN  0.103806       NaN
                                     gsp                   4.195651       NaN   7.039640       NaN  0.102689       NaN
                                     historical_tod_mean   4.260572       NaN   7.436251       NaN  0.106774       NaN
                                     neighbor_average      7.738505       NaN  11.981518       NaN  0.198947       NaN
       graph_sampling_laplacian      gls_map               4.013381       NaN   6.789950       NaN  0.098268       NaN
                                     gsp                   3.933265       NaN   6.738401       NaN  0.098093       NaN
                                     historical_tod_mean   3.971994       NaN   7.118017       NaN  0.099446       NaN
                                     neighbor_average      7.552642       NaN  11.501134       NaN  0.200907       NaN
       greedy_a_trace                gls_map               3.392229       NaN   5.748424       NaN  0.085635       NaN
                                     gsp                   4.090688       NaN   6.898899       NaN  0.101011       NaN
                                     historical_tod_mean   4.192863       NaN   7.366677       NaN  0.106837       NaN
                                     neighbor_average      6.999872       NaN  10.989497       NaN  0.198890       NaN
       greedy_d_logdet               gls_map               3.995784       NaN   6.582279       NaN  0.099900       NaN
                                     gsp                   4.113867       NaN   7.098467       NaN  0.103351       NaN
                                     historical_tod_mean   4.273197       NaN   7.559900       NaN  0.110324       NaN
                                     neighbor_average      7.761705       NaN  12.464407       NaN  0.238732       NaN
       multistart_swap_by_validation gls_map               3.344330       NaN   5.607898       NaN  0.085161       NaN
                                     gsp                   3.957529       NaN   6.759918       NaN  0.100068       NaN
                                     historical_tod_mean   4.109557       NaN   7.268362       NaN  0.105267       NaN
                                     neighbor_average      6.943756       NaN  10.809947       NaN  0.196567       NaN
       observability_proxy           gls_map               3.892990       NaN   6.532897       NaN  0.097730       NaN
                                     gsp                   4.139732       NaN   7.014009       NaN  0.101871       NaN
                                     historical_tod_mean   4.266813       NaN   7.506792       NaN  0.108618       NaN
                                     neighbor_average      8.108327       NaN  12.363365       NaN  0.216024       NaN
       qr_pod_modes                  gls_map               3.862567       NaN   6.284478       NaN  0.102250       NaN
                                     gsp                   4.060793       NaN   6.924310       NaN  0.104668       NaN
                                     historical_tod_mean   4.174672       NaN   7.406851       NaN  0.108923       NaN
                                     neighbor_average      7.382307       NaN  11.879086       NaN  0.223026       NaN
       random                        gls_map               3.542131  0.086308   6.073922  0.165949  0.089304  0.003434
                                     gsp                   4.015004  0.055911   6.861435  0.090266  0.101090  0.002364
                                     historical_tod_mean   4.178206  0.058642   7.403343  0.098396  0.106580  0.002265
                                     neighbor_average      7.234796  0.176199  11.265244  0.265507  0.190012  0.006940
       rcss_selected                 gls_map               3.393100       NaN   5.947266       NaN  0.080323       NaN
                                     gsp                   3.670511       NaN   6.361354       NaN  0.086194       NaN
                                     historical_tod_mean   3.707253       NaN   6.698247       NaN  0.088881       NaN
                                     neighbor_average      9.567448       NaN  14.985342       NaN  0.180688       NaN
       robust_coverage_cvar          gls_map               3.362661       NaN   5.768095       NaN  0.086792       NaN
                                     gsp                   3.959554       NaN   6.794587       NaN  0.100855       NaN
                                     historical_tod_mean   4.108000       NaN   7.330173       NaN  0.106116       NaN
                                     neighbor_average      7.167072       NaN  10.798344       NaN  0.188078       NaN
       scenario_average_a_trace      gls_map               3.513893       NaN   5.880907       NaN  0.087301       NaN
                                     gsp                   3.878832       NaN   6.728800       NaN  0.098349       NaN
                                     historical_tod_mean   4.059925       NaN   7.293062       NaN  0.104119       NaN
                                     neighbor_average      7.521271       NaN  11.624022       NaN  0.200629       NaN
       scenario_cvar_a_trace         gls_map               3.448672       NaN   5.899691       NaN  0.087526       NaN
                                     gsp                   3.960604       NaN   6.786431       NaN  0.098614       NaN
                                     historical_tod_mean   4.127908       NaN   7.344943       NaN  0.105508       NaN
                                     neighbor_average      7.078374       NaN  10.997669       NaN  0.191358       NaN
       swap_from_best_random_trace   gls_map               3.379640       NaN   5.778706       NaN  0.085925       NaN
                                     gsp                   4.072289       NaN   6.951425       NaN  0.101068       NaN
                                     historical_tod_mean   4.212018       NaN   7.413202       NaN  0.107093       NaN
                                     neighbor_average      7.029271       NaN  11.108671       NaN  0.196709       NaN
       swap_from_greedy_a_trace      gls_map               3.378227       NaN   5.719261       NaN  0.086418       NaN
                                     gsp                   4.040064       NaN   6.875489       NaN  0.101398       NaN
                                     historical_tod_mean   4.195516       NaN   7.361001       NaN  0.107224       NaN
                                     neighbor_average      7.082418       NaN  11.272623       NaN  0.204776       NaN
       swap_from_scenario_average    gls_map               3.441693       NaN   5.753740       NaN  0.087543       NaN
                                     gsp                   4.045110       NaN   6.830029       NaN  0.100087       NaN
                                     historical_tod_mean   4.170860       NaN   7.311617       NaN  0.105454       NaN
                                     neighbor_average      7.046625       NaN  11.191294       NaN  0.199659       NaN
       swap_from_scenario_cvar       gls_map               3.424926       NaN   5.715263       NaN  0.087678       NaN
                                     gsp                   4.033518       NaN   6.841285       NaN  0.100483       NaN
                                     historical_tod_mean   4.170506       NaN   7.311819       NaN  0.106213       NaN
                                     neighbor_average      7.019954       NaN  11.061869       NaN  0.200933       NaN
       top_variance                  gls_map               3.393100       NaN   5.947266       NaN  0.080323       NaN
                                     gsp                   3.670511       NaN   6.361354       NaN  0.086194       NaN
                                     historical_tod_mean   3.707253       NaN   6.698247       NaN  0.088881       NaN
                                     neighbor_average      9.567448       NaN  14.985342       NaN  0.180688       NaN
       validation_swap_selected      gls_map               3.385778       NaN   5.808115       NaN  0.077256       NaN
                                     gsp                   3.698473       NaN   6.325693       NaN  0.084289       NaN
                                     historical_tod_mean   3.723104       NaN   6.676883       NaN  0.087874       NaN
                                     neighbor_average      8.866327       NaN  13.966658       NaN  0.173466       NaN
0.3    best_random_by_trace          gls_map               3.268459       NaN   5.622831       NaN  0.082315       NaN
                                     gsp                   4.038054       NaN   6.916368       NaN  0.102457       NaN
                                     historical_tod_mean   4.254017       NaN   7.515263       NaN  0.109993       NaN
                                     neighbor_average      7.087917       NaN  10.904205       NaN  0.187348       NaN
       best_random_by_validation     gls_map               3.076744       NaN   5.409677       NaN  0.076250       NaN
                                     gsp                   3.813546       NaN   6.618758       NaN  0.095456       NaN
                                     historical_tod_mean   3.971147       NaN   7.194669       NaN  0.100794       NaN
                                     neighbor_average      7.275662       NaN  11.313449       NaN  0.168924       NaN
       coverage                      gls_map               3.259044       NaN   5.695562       NaN  0.083979       NaN
                                     gsp                   3.924950       NaN   6.819475       NaN  0.099949       NaN
                                     historical_tod_mean   4.095408       NaN   7.417774       NaN  0.106548       NaN
                                     neighbor_average      6.983158       NaN  10.623019       NaN  0.183577       NaN
       degree                        gls_map               3.943622       NaN   6.569502       NaN  0.096813       NaN
                                     gsp                   4.139711       NaN   6.951354       NaN  0.100511       NaN
                                     historical_tod_mean   4.271779       NaN   7.470650       NaN  0.106880       NaN
                                     neighbor_average      8.162899       NaN  12.898153       NaN  0.227361       NaN
       graph_sampling_laplacian      gls_map               3.882856       NaN   6.574608       NaN  0.096596       NaN
                                     gsp                   3.947686       NaN   6.764690       NaN  0.099345       NaN
                                     historical_tod_mean   3.988041       NaN   7.139889       NaN  0.100340       NaN
                                     neighbor_average      7.271890       NaN  11.582960       NaN  0.192874       NaN
       greedy_a_trace                gls_map               3.244113       NaN   5.465965       NaN  0.084468       NaN
                                     gsp                   4.048497       NaN   6.891195       NaN  0.103051       NaN
                                     historical_tod_mean   4.209736       NaN   7.440507       NaN  0.109587       NaN
                                     neighbor_average      6.861848       NaN  10.764816       NaN  0.200491       NaN
       greedy_d_logdet               gls_map               3.731639       NaN   6.223316       NaN  0.099280       NaN
                                     gsp                   4.059033       NaN   7.000575       NaN  0.105018       NaN
                                     historical_tod_mean   4.215482       NaN   7.566991       NaN  0.111547       NaN
                                     neighbor_average      7.792356       NaN  12.343924       NaN  0.240728       NaN
       multistart_swap_by_validation gls_map               3.103696       NaN   5.263764       NaN  0.077690       NaN
                                     gsp                   3.899682       NaN   6.719977       NaN  0.098051       NaN
                                     historical_tod_mean   4.093850       NaN   7.304678       NaN  0.104781       NaN
                                     neighbor_average      6.875018       NaN  10.641134       NaN  0.183860       NaN
       observability_proxy           gls_map               3.854184       NaN   6.494387       NaN  0.095198       NaN
                                     gsp                   4.136185       NaN   6.969919       NaN  0.100366       NaN
                                     historical_tod_mean   4.285541       NaN   7.499021       NaN  0.107095       NaN
                                     neighbor_average      7.917883       NaN  11.879113       NaN  0.203871       NaN
       qr_pod_modes                  gls_map               3.447667       NaN   5.651064       NaN  0.090819       NaN
                                     gsp                   3.968754       NaN   6.795893       NaN  0.102039       NaN
                                     historical_tod_mean   4.124507       NaN   7.355861       NaN  0.107936       NaN
                                     neighbor_average      7.030147       NaN  11.056411       NaN  0.207567       NaN
       random                        gls_map               3.352822  0.091693   5.763377  0.149145  0.083697  0.002968
                                     gsp                   3.987406  0.067426   6.813628  0.109944  0.100140  0.002715
                                     historical_tod_mean   4.159013  0.080458   7.380235  0.117391  0.105950  0.002921
                                     neighbor_average      7.114007  0.185104  11.112967  0.366007  0.182983  0.009505
       rcss_selected                 gls_map               3.076744       NaN   5.409677       NaN  0.076250       NaN
                                     gsp                   3.813546       NaN   6.618758       NaN  0.095456       NaN
                                     historical_tod_mean   3.971147       NaN   7.194669       NaN  0.100794       NaN
                                     neighbor_average      7.275662       NaN  11.313449       NaN  0.168924       NaN
       robust_coverage_cvar          gls_map               3.182403       NaN   5.379553       NaN  0.080363       NaN
                                     gsp                   3.901723       NaN   6.727911       NaN  0.098029       NaN
                                     historical_tod_mean   4.086146       NaN   7.304545       NaN  0.104986       NaN
                                     neighbor_average      7.100289       NaN  10.924639       NaN  0.186456       NaN
       scenario_average_a_trace      gls_map               3.243887       NaN   5.521367       NaN  0.081535       NaN
                                     gsp                   3.873480       NaN   6.704646       NaN  0.098817       NaN
                                     historical_tod_mean   4.027034       NaN   7.288504       NaN  0.104452       NaN
                                     neighbor_average      7.166202       NaN  11.192564       NaN  0.194137       NaN
       scenario_cvar_a_trace         gls_map               3.337481       NaN   5.732906       NaN  0.084383       NaN
                                     gsp                   3.992025       NaN   6.887056       NaN  0.100744       NaN
                                     historical_tod_mean   4.177421       NaN   7.463445       NaN  0.107967       NaN
                                     neighbor_average      7.226318       NaN  11.391084       NaN  0.199380       NaN
       swap_from_best_random_trace   gls_map               3.295523       NaN   5.589465       NaN  0.084616       NaN
                                     gsp                   4.067682       NaN   6.914381       NaN  0.102426       NaN
                                     historical_tod_mean   4.233220       NaN   7.478134       NaN  0.108956       NaN
                                     neighbor_average      6.971563       NaN  10.941364       NaN  0.199523       NaN
       swap_from_greedy_a_trace      gls_map               3.339167       NaN   5.557869       NaN  0.087194       NaN
                                     gsp                   3.996419       NaN   6.817692       NaN  0.102377       NaN
                                     historical_tod_mean   4.167773       NaN   7.379536       NaN  0.108644       NaN
                                     neighbor_average      6.904405       NaN  10.962234       NaN  0.201548       NaN
       swap_from_scenario_average    gls_map               3.351288       NaN   5.632914       NaN  0.087921       NaN
                                     gsp                   3.986816       NaN   6.818924       NaN  0.101574       NaN
                                     historical_tod_mean   4.153847       NaN   7.373478       NaN  0.107195       NaN
                                     neighbor_average      7.025975       NaN  11.086248       NaN  0.201222       NaN
       swap_from_scenario_cvar       gls_map               3.300489       NaN   5.537202       NaN  0.085563       NaN
                                     gsp                   3.966255       NaN   6.812848       NaN  0.101183       NaN
                                     historical_tod_mean   4.151580       NaN   7.378463       NaN  0.107873       NaN
                                     neighbor_average      6.981611       NaN  11.069657       NaN  0.201134       NaN
       top_variance                  gls_map               3.191580       NaN   5.670191       NaN  0.075966       NaN
                                     gsp                   3.523769       NaN   6.175850       NaN  0.083282       NaN
                                     historical_tod_mean   3.569160       NaN   6.459254       NaN  0.085273       NaN
                                     neighbor_average      8.928557       NaN  13.931098       NaN  0.172033       NaN
       validation_swap_selected      gls_map               3.127307       NaN   5.429318       NaN  0.071202       NaN
                                     gsp                   3.557126       NaN   6.116844       NaN  0.080553       NaN
                                     historical_tod_mean   3.566586       NaN   6.381628       NaN  0.082630       NaN
                                     neighbor_average      8.512736       NaN  13.432267       NaN  0.164250       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 validation_swap_selected gls_map 3.517308 5.966180
    0.2                   random gls_map 3.339824 5.740808
    0.3                   random gls_map 3.076744 5.409677
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.242057      0.257164 210
    gsp   condition_number     0.244874      0.301675 210
    gsp information_logdet    -0.278101     -0.311808 210
gls_map    posterior_trace     0.794060      0.796149 210
gls_map   condition_number     0.796037      0.849204 210
gls_map information_logdet    -0.719081     -0.761844 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv