---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-06-18, 2012-06-19
Test days: 2012-05-25, 2012-06-29
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               4.198843       NaN   6.901159       NaN  0.109883       NaN
                                     gsp                   5.164472       NaN   8.711152       NaN  0.141347       NaN
                                     historical_tod_mean   5.254588       NaN   9.272458       NaN  0.151882       NaN
                                     neighbor_average      7.991033       NaN  12.076238       NaN  0.216951       NaN
       best_random_by_validation     gls_map               4.344372       NaN   7.199245       NaN  0.116338       NaN
                                     gsp                   5.201303       NaN   8.769607       NaN  0.144013       NaN
                                     historical_tod_mean   5.259440       NaN   9.310424       NaN  0.152475       NaN
                                     neighbor_average      8.219077       NaN  12.382317       NaN  0.224039       NaN
       coverage                      gls_map               4.330429       NaN   7.088169       NaN  0.111834       NaN
                                     gsp                   5.150882       NaN   8.746467       NaN  0.140786       NaN
                                     historical_tod_mean   5.266488       NaN   9.284464       NaN  0.151143       NaN
                                     neighbor_average      8.325975       NaN  12.169109       NaN  0.214571       NaN
       degree                        gls_map               5.032680       NaN   8.208845       NaN  0.133052       NaN
                                     gsp                   5.232598       NaN   8.812428       NaN  0.142823       NaN
                                     historical_tod_mean   5.221765       NaN   9.255857       NaN  0.149933       NaN
                                     neighbor_average      9.087710       NaN  12.885300       NaN  0.236515       NaN
       graph_sampling_laplacian      gls_map               5.438311       NaN   8.660859       NaN  0.138240       NaN
                                     gsp                   5.307733       NaN   8.868502       NaN  0.139437       NaN
                                     historical_tod_mean   5.288230       NaN   9.240623       NaN  0.149930       NaN
                                     neighbor_average      8.961532       NaN  14.276522       NaN  0.276971       NaN
       greedy_a_trace                gls_map               4.092804       NaN   6.666743       NaN  0.106717       NaN
                                     gsp                   5.103605       NaN   8.670012       NaN  0.139768       NaN
                                     historical_tod_mean   5.240348       NaN   9.234666       NaN  0.150481       NaN
                                     neighbor_average      7.748293       NaN  11.830823       NaN  0.221896       NaN
       greedy_d_logdet               gls_map               5.049239       NaN   7.709723       NaN  0.124700       NaN
                                     gsp                   5.120464       NaN   8.811672       NaN  0.141226       NaN
                                     historical_tod_mean   5.201482       NaN   9.221154       NaN  0.150069       NaN
                                     neighbor_average      8.633469       NaN  13.231136       NaN  0.260961       NaN
       multistart_swap_by_validation gls_map               4.150611       NaN   6.805575       NaN  0.109072       NaN
                                     gsp                   5.141245       NaN   8.694891       NaN  0.140937       NaN
                                     historical_tod_mean   5.227999       NaN   9.245275       NaN  0.150269       NaN
                                     neighbor_average      7.839597       NaN  11.925578       NaN  0.215783       NaN
       observability_proxy           gls_map               5.021488       NaN   8.131253       NaN  0.132979       NaN
                                     gsp                   5.260616       NaN   8.800300       NaN  0.143012       NaN
                                     historical_tod_mean   5.216939       NaN   9.249484       NaN  0.149460       NaN
                                     neighbor_average     12.325459       NaN  17.626286       NaN  0.263028       NaN
       qr_pod_modes                  gls_map               4.573802       NaN   7.172669       NaN  0.113058       NaN
                                     gsp                   5.117615       NaN   8.721146       NaN  0.138019       NaN
                                     historical_tod_mean   5.204647       NaN   9.189743       NaN  0.148074       NaN
                                     neighbor_average      8.129614       NaN  12.330504       NaN  0.236454       NaN
       random                        gls_map               4.350861  0.063097   7.182517  0.114244  0.114814  0.002620
                                     gsp                   5.172832  0.025797   8.724903  0.051201  0.141890  0.001876
                                     historical_tod_mean   5.265950  0.025991   9.288761  0.040711  0.151623  0.001490
                                     neighbor_average      8.085722  0.138552  12.265278  0.216362  0.219009  0.006113
       rcss_selected                 gls_map               4.150611       NaN   6.805575       NaN  0.109072       NaN
                                     gsp                   5.141245       NaN   8.694891       NaN  0.140937       NaN
                                     historical_tod_mean   5.227999       NaN   9.245275       NaN  0.150269       NaN
                                     neighbor_average      7.839597       NaN  11.925578       NaN  0.215783       NaN
       robust_coverage_cvar          gls_map               4.343841       NaN   7.054126       NaN  0.108493       NaN
                                     gsp                   5.133363       NaN   8.647571       NaN  0.137252       NaN
                                     historical_tod_mean   5.204418       NaN   9.191319       NaN  0.148078       NaN
                                     neighbor_average      8.126083       NaN  12.203122       NaN  0.223817       NaN
       scenario_average_a_trace      gls_map               4.430568       NaN   7.210752       NaN  0.113717       NaN
                                     gsp                   5.154620       NaN   8.697937       NaN  0.139241       NaN
                                     historical_tod_mean   5.239162       NaN   9.232858       NaN  0.148826       NaN
                                     neighbor_average      8.428372       NaN  12.614194       NaN  0.237860       NaN
       scenario_cvar_a_trace         gls_map               4.345583       NaN   7.156764       NaN  0.110384       NaN
                                     gsp                   5.125283       NaN   8.670979       NaN  0.138161       NaN
                                     historical_tod_mean   5.210068       NaN   9.218752       NaN  0.149162       NaN
                                     neighbor_average      8.436532       NaN  12.600631       NaN  0.236402       NaN
       swap_from_best_random_trace   gls_map               4.109257       NaN   6.775959       NaN  0.108682       NaN
                                     gsp                   5.153442       NaN   8.733318       NaN  0.142319       NaN
                                     historical_tod_mean   5.266960       NaN   9.284203       NaN  0.152637       NaN
                                     neighbor_average      7.698268       NaN  11.610484       NaN  0.219961       NaN
       swap_from_greedy_a_trace      gls_map               4.042323       NaN   6.584375       NaN  0.104502       NaN
                                     gsp                   5.097310       NaN   8.651529       NaN  0.139102       NaN
                                     historical_tod_mean   5.222848       NaN   9.203094       NaN  0.149679       NaN
                                     neighbor_average      7.877884       NaN  11.887697       NaN  0.222083       NaN
       swap_from_scenario_average    gls_map               4.262096       NaN   6.910900       NaN  0.109161       NaN
                                     gsp                   5.110658       NaN   8.664322       NaN  0.138194       NaN
                                     historical_tod_mean   5.214749       NaN   9.191698       NaN  0.148285       NaN
                                     neighbor_average      8.091087       NaN  12.264041       NaN  0.231079       NaN
       swap_from_scenario_cvar       gls_map               4.198766       NaN   6.892447       NaN  0.107706       NaN
                                     gsp                   5.089646       NaN   8.665879       NaN  0.138184       NaN
                                     historical_tod_mean   5.199119       NaN   9.199903       NaN  0.148933       NaN
                                     neighbor_average      8.113268       NaN  12.136325       NaN  0.230458       NaN
       top_variance                  gls_map               4.516431       NaN   7.395164       NaN  0.114142       NaN
                                     gsp                   4.971516       NaN   8.274329       NaN  0.127866       NaN
                                     historical_tod_mean   4.954388       NaN   8.769690       NaN  0.133418       NaN
                                     neighbor_average     11.611761       NaN  17.493650       NaN  0.239239       NaN
       validation_swap_selected      gls_map               4.155347       NaN   6.788472       NaN  0.108065       NaN
                                     gsp                   5.116765       NaN   8.634326       NaN  0.139111       NaN
                                     historical_tod_mean   5.192572       NaN   9.195728       NaN  0.148361       NaN
                                     neighbor_average      7.998212       NaN  12.072052       NaN  0.215180       NaN
0.2    best_random_by_trace          gls_map               3.974191       NaN   6.550158       NaN  0.104699       NaN
                                     gsp                   5.180629       NaN   8.658633       NaN  0.141760       NaN
                                     historical_tod_mean   5.276648       NaN   9.290505       NaN  0.152408       NaN
                                     neighbor_average      7.658774       NaN  11.895705       NaN  0.210945       NaN
       best_random_by_validation     gls_map               3.861014       NaN   6.499715       NaN  0.100001       NaN
                                     gsp                   5.165872       NaN   8.629029       NaN  0.139516       NaN
                                     historical_tod_mean   5.210941       NaN   9.252654       NaN  0.149933       NaN
                                     neighbor_average      7.713337       NaN  11.828921       NaN  0.202541       NaN
       coverage                      gls_map               3.908403       NaN   6.392735       NaN  0.100271       NaN
                                     gsp                   5.175454       NaN   8.669886       NaN  0.140388       NaN
                                     historical_tod_mean   5.277939       NaN   9.288634       NaN  0.151580       NaN
                                     neighbor_average      7.606637       NaN  11.580805       NaN  0.205133       NaN
       degree                        gls_map               4.842827       NaN   7.877943       NaN  0.127897       NaN
                                     gsp                   5.245629       NaN   8.745316       NaN  0.142752       NaN
                                     historical_tod_mean   5.191281       NaN   9.266496       NaN  0.149573       NaN
                                     neighbor_average     10.455451       NaN  14.231247       NaN  0.243194       NaN
       graph_sampling_laplacian      gls_map               5.024166       NaN   8.212378       NaN  0.133738       NaN
                                     gsp                   5.343726       NaN   8.755988       NaN  0.143698       NaN
                                     historical_tod_mean   5.342809       NaN   9.283475       NaN  0.153772       NaN
                                     neighbor_average      8.470989       NaN  12.790379       NaN  0.239641       NaN
       greedy_a_trace                gls_map               3.658773       NaN   5.843974       NaN  0.092453       NaN
                                     gsp                   5.073755       NaN   8.526372       NaN  0.135812       NaN
                                     historical_tod_mean   5.176166       NaN   9.142636       NaN  0.147121       NaN
                                     neighbor_average      7.488446       NaN  11.427174       NaN  0.212659       NaN
       greedy_d_logdet               gls_map               4.261925       NaN   6.717265       NaN  0.109295       NaN
                                     gsp                   5.078552       NaN   8.637658       NaN  0.138988       NaN
                                     historical_tod_mean   5.207639       NaN   9.245841       NaN  0.151240       NaN
                                     neighbor_average      8.181937       NaN  12.668391       NaN  0.247345       NaN
       multistart_swap_by_validation gls_map               3.737928       NaN   6.258687       NaN  0.097166       NaN
                                     gsp                   5.134208       NaN   8.641086       NaN  0.140629       NaN
                                     historical_tod_mean   5.218786       NaN   9.266608       NaN  0.151043       NaN
                                     neighbor_average      7.436450       NaN  11.397365       NaN  0.204284       NaN
       observability_proxy           gls_map               4.806836       NaN   7.810372       NaN  0.125635       NaN
                                     gsp                   5.248808       NaN   8.739229       NaN  0.142157       NaN
                                     historical_tod_mean   5.176673       NaN   9.258193       NaN  0.149321       NaN
                                     neighbor_average     11.100483       NaN  15.139354       NaN  0.250876       NaN
       qr_pod_modes                  gls_map               3.870665       NaN   6.185392       NaN  0.098096       NaN
                                     gsp                   5.081365       NaN   8.635596       NaN  0.138871       NaN
                                     historical_tod_mean   5.203412       NaN   9.234898       NaN  0.150557       NaN
                                     neighbor_average      7.689741       NaN  11.820353       NaN  0.228753       NaN
       random                        gls_map               3.966870  0.055815   6.557813  0.104449  0.103061  0.002778
                                     gsp                   5.203549  0.030764   8.661977  0.061238  0.141075  0.002663
                                     historical_tod_mean   5.261574  0.035811   9.283528  0.062393  0.151498  0.002480
                                     neighbor_average      7.747928  0.116493  11.909176  0.191067  0.209296  0.005843
       rcss_selected                 gls_map               3.658773       NaN   5.843974       NaN  0.092453       NaN
                                     gsp                   5.073755       NaN   8.526372       NaN  0.135812       NaN
                                     historical_tod_mean   5.176166       NaN   9.142636       NaN  0.147121       NaN
                                     neighbor_average      7.488446       NaN  11.427174       NaN  0.212659       NaN
       robust_coverage_cvar          gls_map               3.929842       NaN   6.370923       NaN  0.098302       NaN
                                     gsp                   5.127773       NaN   8.569630       NaN  0.136560       NaN
                                     historical_tod_mean   5.184377       NaN   9.187716       NaN  0.147759       NaN
                                     neighbor_average      7.912268       NaN  12.156138       NaN  0.218449       NaN
       scenario_average_a_trace      gls_map               4.017177       NaN   6.531395       NaN  0.102314       NaN
                                     gsp                   5.146421       NaN   8.643738       NaN  0.138517       NaN
                                     historical_tod_mean   5.241276       NaN   9.258484       NaN  0.149536       NaN
                                     neighbor_average      8.034436       NaN  12.334603       NaN  0.233080       NaN
       scenario_cvar_a_trace         gls_map               4.037748       NaN   6.534664       NaN  0.100138       NaN
                                     gsp                   5.120533       NaN   8.544763       NaN  0.135139       NaN
                                     historical_tod_mean   5.162232       NaN   9.155012       NaN  0.146430       NaN
                                     neighbor_average      8.093810       NaN  12.355507       NaN  0.224516       NaN
       swap_from_best_random_trace   gls_map               3.864861       NaN   6.312078       NaN  0.099952       NaN
                                     gsp                   5.145140       NaN   8.606548       NaN  0.139356       NaN
                                     historical_tod_mean   5.245486       NaN   9.247985       NaN  0.150289       NaN
                                     neighbor_average      7.467526       NaN  11.540898       NaN  0.208106       NaN
       swap_from_greedy_a_trace      gls_map               3.674671       NaN   5.866124       NaN  0.093029       NaN
                                     gsp                   5.063271       NaN   8.517418       NaN  0.135852       NaN
                                     historical_tod_mean   5.167205       NaN   9.128642       NaN  0.147022       NaN
                                     neighbor_average      7.504301       NaN  11.515452       NaN  0.215071       NaN
       swap_from_scenario_average    gls_map               3.861531       NaN   6.245084       NaN  0.098116       NaN
                                     gsp                   5.092416       NaN   8.592719       NaN  0.137053       NaN
                                     historical_tod_mean   5.210204       NaN   9.205955       NaN  0.148462       NaN
                                     neighbor_average      7.705283       NaN  11.784499       NaN  0.221924       NaN
       swap_from_scenario_cvar       gls_map               3.878750       NaN   6.237724       NaN  0.097210       NaN
                                     gsp                   5.066700       NaN   8.525255       NaN  0.134887       NaN
                                     historical_tod_mean   5.144614       NaN   9.138521       NaN  0.146529       NaN
                                     neighbor_average      7.829619       NaN  11.934696       NaN  0.219570       NaN
       top_variance                  gls_map               4.093253       NaN   6.709236       NaN  0.099470       NaN
                                     gsp                   4.840833       NaN   7.990400       NaN  0.121074       NaN
                                     historical_tod_mean   4.745576       NaN   8.453524       NaN  0.124900       NaN
                                     neighbor_average      9.869176       NaN  15.135204       NaN  0.202274       NaN
       validation_swap_selected      gls_map               3.664807       NaN   5.844592       NaN  0.092362       NaN
                                     gsp                   5.069854       NaN   8.523092       NaN  0.135966       NaN
                                     historical_tod_mean   5.170325       NaN   9.142830       NaN  0.147106       NaN
                                     neighbor_average      7.482088       NaN  11.382707       NaN  0.212596       NaN
0.3    best_random_by_trace          gls_map               3.709091       NaN   6.115064       NaN  0.095087       NaN
                                     gsp                   5.171558       NaN   8.634096       NaN  0.138876       NaN
                                     historical_tod_mean   5.210403       NaN   9.241386       NaN  0.149732       NaN
                                     neighbor_average      7.598244       NaN  11.857700       NaN  0.207130       NaN
       best_random_by_validation     gls_map               3.630701       NaN   5.940517       NaN  0.091102       NaN
                                     gsp                   5.148767       NaN   8.538329       NaN  0.137169       NaN
                                     historical_tod_mean   5.198986       NaN   9.177417       NaN  0.147821       NaN
                                     neighbor_average      7.329323       NaN  11.242612       NaN  0.195315       NaN
       coverage                      gls_map               3.743586       NaN   6.146236       NaN  0.096672       NaN
                                     gsp                   5.233007       NaN   8.681695       NaN  0.141575       NaN
                                     historical_tod_mean   5.328475       NaN   9.342680       NaN  0.153619       NaN
                                     neighbor_average      7.441634       NaN  11.616103       NaN  0.204837       NaN
       degree                        gls_map               4.701252       NaN   7.716053       NaN  0.122120       NaN
                                     gsp                   5.173067       NaN   8.618614       NaN  0.139159       NaN
                                     historical_tod_mean   5.092237       NaN   9.173425       NaN  0.146489       NaN
                                     neighbor_average      9.333698       NaN  13.688767       NaN  0.232434       NaN
       graph_sampling_laplacian      gls_map               4.949892       NaN   8.089442       NaN  0.132295       NaN
                                     gsp                   5.323028       NaN   8.743613       NaN  0.145691       NaN
                                     historical_tod_mean   5.358759       NaN   9.323862       NaN  0.156499       NaN
                                     neighbor_average      9.042502       NaN  13.984380       NaN  0.283445       NaN
       greedy_a_trace                gls_map               3.390465       NaN   5.412150       NaN  0.085388       NaN
                                     gsp                   5.065551       NaN   8.458379       NaN  0.135063       NaN
                                     historical_tod_mean   5.176883       NaN   9.136632       NaN  0.147261       NaN
                                     neighbor_average      7.266192       NaN  11.230582       NaN  0.211136       NaN
       greedy_d_logdet               gls_map               3.831264       NaN   6.066895       NaN  0.098240       NaN
                                     gsp                   5.068084       NaN   8.570571       NaN  0.138634       NaN
                                     historical_tod_mean   5.182373       NaN   9.251971       NaN  0.151938       NaN
                                     neighbor_average      7.911578       NaN  12.262813       NaN  0.240945       NaN
       multistart_swap_by_validation gls_map               3.515580       NaN   5.672624       NaN  0.086541       NaN
                                     gsp                   5.123976       NaN   8.473428       NaN  0.134689       NaN
                                     historical_tod_mean   5.162884       NaN   9.121744       NaN  0.145931       NaN
                                     neighbor_average      7.213532       NaN  10.973053       NaN  0.193204       NaN
       observability_proxy           gls_map               4.677473       NaN   7.666361       NaN  0.120945       NaN
                                     gsp                   5.169397       NaN   8.599601       NaN  0.138547       NaN
                                     historical_tod_mean   5.076556       NaN   9.149369       NaN  0.145763       NaN
                                     neighbor_average      9.259174       NaN  13.597980       NaN  0.225509       NaN
       qr_pod_modes                  gls_map               3.452154       NaN   5.498449       NaN  0.087451       NaN
                                     gsp                   5.062205       NaN   8.567263       NaN  0.137936       NaN
                                     historical_tod_mean   5.186586       NaN   9.253799       NaN  0.150640       NaN
                                     neighbor_average      7.371330       NaN  11.274815       NaN  0.214318       NaN
       random                        gls_map               3.720762  0.054765   6.152167  0.114606  0.095752  0.002766
                                     gsp                   5.220285  0.044924   8.652182  0.079881  0.141086  0.003038
                                     historical_tod_mean   5.268159  0.054904   9.292443  0.085152  0.151688  0.003188
                                     neighbor_average      7.560952  0.104522  11.714798  0.191129  0.203213  0.006095
       rcss_selected                 gls_map               3.359243       NaN   5.372931       NaN  0.084597       NaN
                                     gsp                   5.020378       NaN   8.407688       NaN  0.133930       NaN
                                     historical_tod_mean   5.140017       NaN   9.086899       NaN  0.146201       NaN
                                     neighbor_average      7.331480       NaN  11.277306       NaN  0.211230       NaN
       robust_coverage_cvar          gls_map               3.631938       NaN   5.887085       NaN  0.091212       NaN
                                     gsp                   5.131245       NaN   8.581377       NaN  0.138073       NaN
                                     historical_tod_mean   5.201754       NaN   9.242429       NaN  0.149494       NaN
                                     neighbor_average      7.772100       NaN  12.120341       NaN  0.216839       NaN
       scenario_average_a_trace      gls_map               3.789791       NaN   6.129579       NaN  0.096313       NaN
                                     gsp                   5.143567       NaN   8.560104       NaN  0.137732       NaN
                                     historical_tod_mean   5.204202       NaN   9.218473       NaN  0.149297       NaN
                                     neighbor_average      8.026539       NaN  12.500789       NaN  0.231270       NaN
       scenario_cvar_a_trace         gls_map               3.813156       NaN   6.205445       NaN  0.096310       NaN
                                     gsp                   5.111718       NaN   8.558168       NaN  0.137061       NaN
                                     historical_tod_mean   5.173075       NaN   9.204952       NaN  0.148524       NaN
                                     neighbor_average      8.010968       NaN  12.307396       NaN  0.227509       NaN
       swap_from_best_random_trace   gls_map               3.562662       NaN   5.794918       NaN  0.088604       NaN
                                     gsp                   5.117921       NaN   8.527975       NaN  0.134779       NaN
                                     historical_tod_mean   5.164816       NaN   9.150204       NaN  0.146002       NaN
                                     neighbor_average      7.397387       NaN  11.381473       NaN  0.201393       NaN
       swap_from_greedy_a_trace      gls_map               3.359243       NaN   5.372931       NaN  0.084597       NaN
                                     gsp                   5.020378       NaN   8.407688       NaN  0.133930       NaN
                                     historical_tod_mean   5.140017       NaN   9.086899       NaN  0.146201       NaN
                                     neighbor_average      7.331480       NaN  11.277306       NaN  0.211230       NaN
       swap_from_scenario_average    gls_map               3.576495       NaN   5.762387       NaN  0.091403       NaN
                                     gsp                   5.068522       NaN   8.519852       NaN  0.136505       NaN
                                     historical_tod_mean   5.174165       NaN   9.193130       NaN  0.148568       NaN
                                     neighbor_average      7.711999       NaN  11.963860       NaN  0.221242       NaN
       swap_from_scenario_cvar       gls_map               3.651677       NaN   5.879906       NaN  0.091509       NaN
                                     gsp                   5.064299       NaN   8.494681       NaN  0.135496       NaN
                                     historical_tod_mean   5.148720       NaN   9.151926       NaN  0.147416       NaN
                                     neighbor_average      7.738926       NaN  11.871894       NaN  0.220291       NaN
       top_variance                  gls_map               3.715937       NaN   6.177893       NaN  0.088813       NaN
                                     gsp                   4.607487       NaN   7.626789       NaN  0.111866       NaN
                                     historical_tod_mean   4.480048       NaN   8.044206       NaN  0.114497       NaN
                                     neighbor_average      9.451669       NaN  14.573575       NaN  0.189452       NaN
       validation_swap_selected      gls_map               3.360969       NaN   5.378717       NaN  0.085288       NaN
                                     gsp                   5.010986       NaN   8.397519       NaN  0.134471       NaN
                                     historical_tod_mean   5.130370       NaN   9.075456       NaN  0.146557       NaN
                                     neighbor_average      7.313928       NaN  11.277624       NaN  0.211911       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 4.042323 6.584375
    0.2           greedy_a_trace gls_map 3.658773 5.843974
    0.3 swap_from_greedy_a_trace gls_map 3.359243 5.372931
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.203578     -0.262289 360
    gsp   condition_number    -0.204117     -0.367879 360
    gsp information_logdet     0.200637      0.260897 360
gls_map    posterior_trace     0.923612      0.926448 360
gls_map   condition_number     0.823350      0.919026 360
gls_map information_logdet    -0.850978     -0.878742 360
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv