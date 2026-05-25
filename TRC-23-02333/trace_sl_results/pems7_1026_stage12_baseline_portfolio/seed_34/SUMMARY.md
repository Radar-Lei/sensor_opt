---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-05-14, 2012-06-15
Test days: 2012-05-11, 2012-06-22
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               4.110106       NaN   6.824498       NaN  0.106216       NaN
                                     gsp                   5.006257       NaN   8.373988       NaN  0.132884       NaN
                                     historical_tod_mean   5.108215       NaN   8.984073       NaN  0.142486       NaN
                                     neighbor_average      7.778926       NaN  11.952070       NaN  0.206468       NaN
       best_random_by_validation     gls_map               4.196596       NaN   6.881931       NaN  0.107350       NaN
                                     gsp                   5.042463       NaN   8.361813       NaN  0.133074       NaN
                                     historical_tod_mean   5.085887       NaN   8.948399       NaN  0.141132       NaN
                                     neighbor_average      8.184213       NaN  12.182894       NaN  0.209987       NaN
       coverage                      gls_map               4.247051       NaN   6.927392       NaN  0.108396       NaN
                                     gsp                   5.011332       NaN   8.423511       NaN  0.131849       NaN
                                     historical_tod_mean   5.117554       NaN   8.994267       NaN  0.141353       NaN
                                     neighbor_average      8.091990       NaN  12.092256       NaN  0.206692       NaN
       degree                        gls_map               5.083538       NaN   8.067171       NaN  0.125872       NaN
                                     gsp                   5.223387       NaN   8.529999       NaN  0.133043       NaN
                                     historical_tod_mean   5.035297       NaN   8.891466       NaN  0.139081       NaN
                                     neighbor_average      9.175010       NaN  13.113728       NaN  0.229715       NaN
       graph_sampling_laplacian      gls_map               5.202911       NaN   8.364573       NaN  0.133688       NaN
                                     gsp                   5.245928       NaN   8.757302       NaN  0.134837       NaN
                                     historical_tod_mean   5.191493       NaN   9.081316       NaN  0.143897       NaN
                                     neighbor_average      8.723410       NaN  14.096823       NaN  0.262864       NaN
       greedy_a_trace                gls_map               3.992700       NaN   6.591209       NaN  0.104961       NaN
                                     gsp                   4.994589       NaN   8.408185       NaN  0.134001       NaN
                                     historical_tod_mean   5.100213       NaN   8.987953       NaN  0.142835       NaN
                                     neighbor_average      7.516867       NaN  11.695797       NaN  0.220813       NaN
       greedy_d_logdet               gls_map               4.894065       NaN   7.686404       NaN  0.123582       NaN
                                     gsp                   4.998246       NaN   8.520969       NaN  0.135066       NaN
                                     historical_tod_mean   5.094429       NaN   9.014021       NaN  0.142812       NaN
                                     neighbor_average      8.423820       NaN  12.990127       NaN  0.255616       NaN
       multistart_swap_by_validation gls_map               4.026424       NaN   6.634390       NaN  0.105816       NaN
                                     gsp                   4.999736       NaN   8.383172       NaN  0.134665       NaN
                                     historical_tod_mean   5.090924       NaN   8.977185       NaN  0.142771       NaN
                                     neighbor_average      7.678572       NaN  11.662156       NaN  0.215922       NaN
       observability_proxy           gls_map               5.118351       NaN   8.078106       NaN  0.126003       NaN
                                     gsp                   5.258594       NaN   8.550322       NaN  0.133586       NaN
                                     historical_tod_mean   5.038673       NaN   8.898395       NaN  0.138853       NaN
                                     neighbor_average     12.434042       NaN  18.051775       NaN  0.260113       NaN
       qr_pod_modes                  gls_map               4.357588       NaN   6.945669       NaN  0.112897       NaN
                                     gsp                   4.978986       NaN   8.443591       NaN  0.134633       NaN
                                     historical_tod_mean   5.082646       NaN   8.988791       NaN  0.142719       NaN
                                     neighbor_average      7.897055       NaN  12.302220       NaN  0.239349       NaN
       random                        gls_map               4.238443  0.059975   6.987236  0.106863  0.110308  0.002494
                                     gsp                   5.032857  0.026504   8.417955  0.048843  0.134255  0.001593
                                     historical_tod_mean   5.118771  0.023816   9.009293  0.038178  0.142878  0.001171
                                     neighbor_average      7.879027  0.135553  12.071103  0.184836  0.212949  0.004862
       rcss_selected                 gls_map               4.026424       NaN   6.634390       NaN  0.105816       NaN
                                     gsp                   4.999736       NaN   8.383172       NaN  0.134665       NaN
                                     historical_tod_mean   5.090924       NaN   8.977185       NaN  0.142771       NaN
                                     neighbor_average      7.678572       NaN  11.662156       NaN  0.215922       NaN
       robust_coverage_cvar          gls_map               4.258261       NaN   6.925020       NaN  0.107780       NaN
                                     gsp                   4.986120       NaN   8.364549       NaN  0.130773       NaN
                                     historical_tod_mean   5.053208       NaN   8.938428       NaN  0.140500       NaN
                                     neighbor_average      8.234653       NaN  12.215170       NaN  0.223976       NaN
       scenario_average_a_trace      gls_map               4.423140       NaN   7.082826       NaN  0.108558       NaN
                                     gsp                   5.018489       NaN   8.386597       NaN  0.130340       NaN
                                     historical_tod_mean   5.071652       NaN   8.959856       NaN  0.140475       NaN
                                     neighbor_average      8.417896       NaN  12.391901       NaN  0.229087       NaN
       scenario_cvar_a_trace         gls_map               4.353849       NaN   7.025595       NaN  0.109605       NaN
                                     gsp                   4.965465       NaN   8.334909       NaN  0.130429       NaN
                                     historical_tod_mean   5.042663       NaN   8.914500       NaN  0.139967       NaN
                                     neighbor_average      8.224227       NaN  12.231810       NaN  0.225742       NaN
       swap_from_best_random_trace   gls_map               3.983631       NaN   6.551166       NaN  0.101995       NaN
                                     gsp                   4.970710       NaN   8.326060       NaN  0.131465       NaN
                                     historical_tod_mean   5.066135       NaN   8.926090       NaN  0.140975       NaN
                                     neighbor_average      7.584786       NaN  11.578296       NaN  0.206927       NaN
       swap_from_greedy_a_trace      gls_map               3.988419       NaN   6.499640       NaN  0.102665       NaN
                                     gsp                   4.983600       NaN   8.365395       NaN  0.132625       NaN
                                     historical_tod_mean   5.082849       NaN   8.946638       NaN  0.141386       NaN
                                     neighbor_average      7.602361       NaN  11.677843       NaN  0.217417       NaN
       swap_from_scenario_average    gls_map               4.146571       NaN   6.702836       NaN  0.104519       NaN
                                     gsp                   4.993179       NaN   8.395607       NaN  0.131772       NaN
                                     historical_tod_mean   5.071808       NaN   8.957495       NaN  0.140992       NaN
                                     neighbor_average      8.061753       NaN  12.029243       NaN  0.227816       NaN
       swap_from_scenario_cvar       gls_map               4.132158       NaN   6.717383       NaN  0.106462       NaN
                                     gsp                   4.933674       NaN   8.354984       NaN  0.131804       NaN
                                     historical_tod_mean   5.030254       NaN   8.919264       NaN  0.140805       NaN
                                     neighbor_average      7.967101       NaN  11.938927       NaN  0.226035       NaN
       top_variance                  gls_map               4.336463       NaN   7.068282       NaN  0.107479       NaN
                                     gsp                   4.908452       NaN   7.962323       NaN  0.122678       NaN
                                     historical_tod_mean   4.806389       NaN   8.472813       NaN  0.126857       NaN
                                     neighbor_average     10.813403       NaN  16.326799       NaN  0.220456       NaN
       validation_swap_selected      gls_map               4.015217       NaN   6.607325       NaN  0.105474       NaN
                                     gsp                   4.969048       NaN   8.362686       NaN  0.134163       NaN
                                     historical_tod_mean   5.061493       NaN   8.952170       NaN  0.142176       NaN
                                     neighbor_average      7.859944       NaN  11.810136       NaN  0.218874       NaN
0.2    best_random_by_trace          gls_map               3.901129       NaN   6.408816       NaN  0.101076       NaN
                                     gsp                   5.085998       NaN   8.342115       NaN  0.134755       NaN
                                     historical_tod_mean   5.118954       NaN   9.000329       NaN  0.144201       NaN
                                     neighbor_average      7.756633       NaN  11.841307       NaN  0.215017       NaN
       best_random_by_validation     gls_map               3.761111       NaN   6.225009       NaN  0.097791       NaN
                                     gsp                   5.012767       NaN   8.272622       NaN  0.134369       NaN
                                     historical_tod_mean   5.053108       NaN   8.919238       NaN  0.141978       NaN
                                     neighbor_average      7.734546       NaN  12.011524       NaN  0.208070       NaN
       coverage                      gls_map               3.855581       NaN   6.349744       NaN  0.098040       NaN
                                     gsp                   5.036323       NaN   8.376009       NaN  0.132479       NaN
                                     historical_tod_mean   5.141158       NaN   9.028460       NaN  0.142411       NaN
                                     neighbor_average      7.448665       NaN  11.460197       NaN  0.199018       NaN
       degree                        gls_map               4.826338       NaN   7.717194       NaN  0.121196       NaN
                                     gsp                   5.168047       NaN   8.356347       NaN  0.131422       NaN
                                     historical_tod_mean   4.998665       NaN   8.877389       NaN  0.137725       NaN
                                     neighbor_average      9.861244       NaN  13.808189       NaN  0.227127       NaN
       graph_sampling_laplacian      gls_map               4.918342       NaN   7.955754       NaN  0.132187       NaN
                                     gsp                   5.233335       NaN   8.546614       NaN  0.139213       NaN
                                     historical_tod_mean   5.241158       NaN   9.110076       NaN  0.148115       NaN
                                     neighbor_average      8.763015       NaN  12.925992       NaN  0.243682       NaN
       greedy_a_trace                gls_map               3.610413       NaN   5.920345       NaN  0.093276       NaN
                                     gsp                   4.955411       NaN   8.301839       NaN  0.132640       NaN
                                     historical_tod_mean   5.042250       NaN   8.942383       NaN  0.141600       NaN
                                     neighbor_average      7.256367       NaN  11.286165       NaN  0.213480       NaN
       greedy_d_logdet               gls_map               4.174800       NaN   6.743893       NaN  0.107551       NaN
                                     gsp                   4.961857       NaN   8.393714       NaN  0.133123       NaN
                                     historical_tod_mean   5.081822       NaN   9.034855       NaN  0.143553       NaN
                                     neighbor_average      8.001826       NaN  12.449400       NaN  0.244751       NaN
       multistart_swap_by_validation gls_map               3.668680       NaN   5.941485       NaN  0.092955       NaN
                                     gsp                   5.009509       NaN   8.252703       NaN  0.131655       NaN
                                     historical_tod_mean   5.051236       NaN   8.908999       NaN  0.140696       NaN
                                     neighbor_average      7.407127       NaN  11.379638       NaN  0.203452       NaN
       observability_proxy           gls_map               4.784087       NaN   7.651799       NaN  0.121534       NaN
                                     gsp                   5.151616       NaN   8.346314       NaN  0.131935       NaN
                                     historical_tod_mean   4.989360       NaN   8.877008       NaN  0.138410       NaN
                                     neighbor_average     10.378464       NaN  14.633200       NaN  0.246548       NaN
       qr_pod_modes                  gls_map               3.740858       NaN   6.048944       NaN  0.096343       NaN
                                     gsp                   4.928274       NaN   8.323434       NaN  0.132949       NaN
                                     historical_tod_mean   5.043489       NaN   8.958240       NaN  0.142316       NaN
                                     neighbor_average      7.596055       NaN  11.716812       NaN  0.226903       NaN
       random                        gls_map               3.864783  0.046598   6.385636  0.094574  0.099438  0.001997
                                     gsp                   5.065052  0.031582   8.345907  0.053547  0.133560  0.001719
                                     historical_tod_mean   5.112832  0.033226   9.000223  0.051524  0.142655  0.001689
                                     neighbor_average      7.581944  0.099735  11.737582  0.171543  0.203297  0.005359
       rcss_selected                 gls_map               3.576713       NaN   5.893343       NaN  0.092922       NaN
                                     gsp                   4.936263       NaN   8.274191       NaN  0.132327       NaN
                                     historical_tod_mean   5.028395       NaN   8.913324       NaN  0.141232       NaN
                                     neighbor_average      7.250705       NaN  11.251354       NaN  0.213651       NaN
       robust_coverage_cvar          gls_map               3.853578       NaN   6.312463       NaN  0.098148       NaN
                                     gsp                   4.981751       NaN   8.281355       NaN  0.130833       NaN
                                     historical_tod_mean   5.029878       NaN   8.936654       NaN  0.140893       NaN
                                     neighbor_average      7.767086       NaN  11.855296       NaN  0.212187       NaN
       scenario_average_a_trace      gls_map               3.944421       NaN   6.422046       NaN  0.098379       NaN
                                     gsp                   5.043905       NaN   8.367673       NaN  0.131596       NaN
                                     historical_tod_mean   5.086053       NaN   9.023473       NaN  0.142167       NaN
                                     neighbor_average      7.836105       NaN  11.918522       NaN  0.223444       NaN
       scenario_cvar_a_trace         gls_map               3.960172       NaN   6.464823       NaN  0.101172       NaN
                                     gsp                   4.977499       NaN   8.270641       NaN  0.130351       NaN
                                     historical_tod_mean   5.009428       NaN   8.925545       NaN  0.140041       NaN
                                     neighbor_average      8.048585       NaN  12.209332       NaN  0.222051       NaN
       swap_from_best_random_trace   gls_map               3.731042       NaN   6.098508       NaN  0.095703       NaN
                                     gsp                   5.038102       NaN   8.275094       NaN  0.132620       NaN
                                     historical_tod_mean   5.068832       NaN   8.938329       NaN  0.141987       NaN
                                     neighbor_average      7.528307       NaN  11.445278       NaN  0.210574       NaN
       swap_from_greedy_a_trace      gls_map               3.576713       NaN   5.893343       NaN  0.092922       NaN
                                     gsp                   4.936263       NaN   8.274191       NaN  0.132327       NaN
                                     historical_tod_mean   5.028395       NaN   8.913324       NaN  0.141232       NaN
                                     neighbor_average      7.250705       NaN  11.251354       NaN  0.213651       NaN
       swap_from_scenario_average    gls_map               3.764488       NaN   6.146462       NaN  0.095678       NaN
                                     gsp                   4.991069       NaN   8.336724       NaN  0.131627       NaN
                                     historical_tod_mean   5.055873       NaN   8.994711       NaN  0.141439       NaN
                                     neighbor_average      7.531006       NaN  11.516660       NaN  0.215679       NaN
       swap_from_scenario_cvar       gls_map               3.795909       NaN   6.207479       NaN  0.097726       NaN
                                     gsp                   4.969532       NaN   8.295954       NaN  0.131650       NaN
                                     historical_tod_mean   5.017791       NaN   8.948069       NaN  0.141266       NaN
                                     neighbor_average      7.689353       NaN  11.793994       NaN  0.219330       NaN
       top_variance                  gls_map               3.991030       NaN   6.570228       NaN  0.097283       NaN
                                     gsp                   4.744588       NaN   7.692239       NaN  0.116288       NaN
                                     historical_tod_mean   4.604192       NaN   8.170098       NaN  0.119096       NaN
                                     neighbor_average      9.343099       NaN  14.661128       NaN  0.191335       NaN
       validation_swap_selected      gls_map               3.569545       NaN   5.885204       NaN  0.092801       NaN
                                     gsp                   4.932884       NaN   8.273275       NaN  0.132321       NaN
                                     historical_tod_mean   5.025342       NaN   8.912344       NaN  0.141184       NaN
                                     neighbor_average      7.259167       NaN  11.293975       NaN  0.214686       NaN
0.3    best_random_by_trace          gls_map               3.524113       NaN   5.859309       NaN  0.089711       NaN
                                     gsp                   5.038709       NaN   8.326272       NaN  0.131360       NaN
                                     historical_tod_mean   5.084998       NaN   9.001358       NaN  0.141010       NaN
                                     neighbor_average      7.209823       NaN  11.175518       NaN  0.193251       NaN
       best_random_by_validation     gls_map               3.524113       NaN   5.859309       NaN  0.089711       NaN
                                     gsp                   5.038709       NaN   8.326272       NaN  0.131360       NaN
                                     historical_tod_mean   5.084998       NaN   9.001358       NaN  0.141010       NaN
                                     neighbor_average      7.209823       NaN  11.175518       NaN  0.193251       NaN
       coverage                      gls_map               3.671717       NaN   6.036724       NaN  0.093257       NaN
                                     gsp                   5.095811       NaN   8.376565       NaN  0.133838       NaN
                                     historical_tod_mean   5.191281       NaN   9.070338       NaN  0.144399       NaN
                                     neighbor_average      7.328332       NaN  11.454752       NaN  0.199969       NaN
       degree                        gls_map               4.565888       NaN   7.414748       NaN  0.116134       NaN
                                     gsp                   5.057161       NaN   8.273614       NaN  0.131076       NaN
                                     historical_tod_mean   4.952124       NaN   8.867337       NaN  0.138091       NaN
                                     neighbor_average      8.784852       NaN  13.368152       NaN  0.223960       NaN
       graph_sampling_laplacian      gls_map               4.869652       NaN   7.897750       NaN  0.128880       NaN
                                     gsp                   5.167263       NaN   8.333528       NaN  0.137245       NaN
                                     historical_tod_mean   5.152817       NaN   8.956659       NaN  0.146282       NaN
                                     neighbor_average      9.100760       NaN  13.952136       NaN  0.281302       NaN
       greedy_a_trace                gls_map               3.320121       NaN   5.448606       NaN  0.086329       NaN
                                     gsp                   4.947975       NaN   8.280572       NaN  0.132826       NaN
                                     historical_tod_mean   5.042767       NaN   8.977755       NaN  0.143090       NaN
                                     neighbor_average      7.146278       NaN  11.233998       NaN  0.214372       NaN
       greedy_d_logdet               gls_map               3.731886       NaN   6.052871       NaN  0.097003       NaN
                                     gsp                   4.972269       NaN   8.343531       NaN  0.133486       NaN
                                     historical_tod_mean   5.063022       NaN   9.054453       NaN  0.144657       NaN
                                     neighbor_average      7.822902       NaN  12.262528       NaN  0.240997       NaN
       multistart_swap_by_validation gls_map               3.449350       NaN   5.653845       NaN  0.085341       NaN
                                     gsp                   4.985558       NaN   8.164545       NaN  0.127044       NaN
                                     historical_tod_mean   5.003463       NaN   8.836924       NaN  0.136618       NaN
                                     neighbor_average      7.224231       NaN  11.321300       NaN  0.186601       NaN
       observability_proxy           gls_map               4.536384       NaN   7.347297       NaN  0.115256       NaN
                                     gsp                   5.050121       NaN   8.253526       NaN  0.130466       NaN
                                     historical_tod_mean   4.936056       NaN   8.847045       NaN  0.137458       NaN
                                     neighbor_average      8.775849       NaN  13.345510       NaN  0.219665       NaN
       qr_pod_modes                  gls_map               3.375452       NaN   5.468679       NaN  0.086762       NaN
                                     gsp                   4.918939       NaN   8.248349       NaN  0.131455       NaN
                                     historical_tod_mean   5.012018       NaN   8.956115       NaN  0.142233       NaN
                                     neighbor_average      7.242844       NaN  11.214981       NaN  0.214458       NaN
       random                        gls_map               3.626844  0.051585   5.990344  0.103574  0.092653  0.002353
                                     gsp                   5.078173  0.041043   8.326588  0.071500  0.133576  0.002529
                                     historical_tod_mean   5.110434  0.048429   9.001010  0.074588  0.142724  0.002498
                                     neighbor_average      7.380967  0.093876  11.525115  0.179112  0.198644  0.005651
       rcss_selected                 gls_map               3.310566       NaN   5.422561       NaN  0.085868       NaN
                                     gsp                   4.925547       NaN   8.235517       NaN  0.131577       NaN
                                     historical_tod_mean   5.006409       NaN   8.930247       NaN  0.141673       NaN
                                     neighbor_average      7.211066       NaN  11.307572       NaN  0.215168       NaN
       robust_coverage_cvar          gls_map               3.600107       NaN   5.847972       NaN  0.090953       NaN
                                     gsp                   4.979025       NaN   8.222095       NaN  0.130825       NaN
                                     historical_tod_mean   4.969648       NaN   8.903681       NaN  0.140606       NaN
                                     neighbor_average      7.690545       NaN  11.961568       NaN  0.210864       NaN
       scenario_average_a_trace      gls_map               3.646868       NaN   5.995224       NaN  0.092436       NaN
                                     gsp                   4.993644       NaN   8.299699       NaN  0.130520       NaN
                                     historical_tod_mean   5.033511       NaN   8.992262       NaN  0.141647       NaN
                                     neighbor_average      7.742655       NaN  11.976728       NaN  0.222382       NaN
       scenario_cvar_a_trace         gls_map               3.690844       NaN   6.004845       NaN  0.093789       NaN
                                     gsp                   4.977983       NaN   8.255189       NaN  0.131223       NaN
                                     historical_tod_mean   4.988696       NaN   8.935777       NaN  0.140872       NaN
                                     neighbor_average      7.685051       NaN  11.960822       NaN  0.216916       NaN
       swap_from_best_random_trace   gls_map               3.444966       NaN   5.710090       NaN  0.087385       NaN
                                     gsp                   5.005668       NaN   8.316588       NaN  0.131053       NaN
                                     historical_tod_mean   5.076414       NaN   9.012330       NaN  0.140983       NaN
                                     neighbor_average      7.056570       NaN  10.870635       NaN  0.191111       NaN
       swap_from_greedy_a_trace      gls_map               3.310566       NaN   5.422561       NaN  0.085868       NaN
                                     gsp                   4.925547       NaN   8.235517       NaN  0.131577       NaN
                                     historical_tod_mean   5.006409       NaN   8.930247       NaN  0.141673       NaN
                                     neighbor_average      7.211066       NaN  11.307572       NaN  0.215168       NaN
       swap_from_scenario_average    gls_map               3.506669       NaN   5.755724       NaN  0.089301       NaN
                                     gsp                   4.970750       NaN   8.285910       NaN  0.130473       NaN
                                     historical_tod_mean   5.026878       NaN   8.983892       NaN  0.141254       NaN
                                     neighbor_average      7.450927       NaN  11.598639       NaN  0.214955       NaN
       swap_from_scenario_cvar       gls_map               3.523228       NaN   5.739258       NaN  0.089996       NaN
                                     gsp                   4.958556       NaN   8.255746       NaN  0.131530       NaN
                                     historical_tod_mean   5.002933       NaN   8.952524       NaN  0.141555       NaN
                                     neighbor_average      7.438527       NaN  11.546232       NaN  0.214045       NaN
       top_variance                  gls_map               3.676018       NaN   6.104444       NaN  0.086995       NaN
                                     gsp                   4.528490       NaN   7.362301       NaN  0.108308       NaN
                                     historical_tod_mean   4.367520       NaN   7.799902       NaN  0.110172       NaN
                                     neighbor_average      8.987244       NaN  14.047640       NaN  0.179357       NaN
       validation_swap_selected      gls_map               3.298548       NaN   5.418166       NaN  0.086030       NaN
                                     gsp                   4.908006       NaN   8.207079       NaN  0.131187       NaN
                                     historical_tod_mean   4.985742       NaN   8.901725       NaN  0.141228       NaN
                                     neighbor_average      7.217537       NaN  11.320923       NaN  0.215204       NaN
```

## Best method per budget-layout row

```
 budget                 layout_type  method      mae     rmse
    0.1 swap_from_best_random_trace gls_map 3.983631 6.551166
    0.2    validation_swap_selected gls_map 3.569545 5.885204
    0.3    validation_swap_selected gls_map 3.298548 5.418166
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.206812     -0.291309 360
    gsp   condition_number    -0.207162     -0.349245 360
    gsp information_logdet     0.199286      0.281457 360
gls_map    posterior_trace     0.920938      0.928613 360
gls_map   condition_number     0.804153      0.904442 360
gls_map information_logdet    -0.844875     -0.879202 360
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv