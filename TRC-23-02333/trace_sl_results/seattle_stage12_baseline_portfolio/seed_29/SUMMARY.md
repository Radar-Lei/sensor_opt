---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/Seattle
Validation days: 2015-01-09, 2015-01-12
Test days: 2015-01-10, 2015-01-15
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 50
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                               mae                 rmse                mape
                                                              mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map              3.411958       NaN   5.745795       NaN  0.119734       NaN
                                     gsp                  4.565493       NaN   7.556511       NaN  0.171012       NaN
                                     historical_tod_mean  6.164879       NaN  10.080162       NaN  0.241516       NaN
                                     neighbor_average     5.925444       NaN   9.740831       NaN  0.205419       NaN
       best_random_by_validation     gls_map              3.411958       NaN   5.745795       NaN  0.119734       NaN
                                     gsp                  4.565493       NaN   7.556511       NaN  0.171012       NaN
                                     historical_tod_mean  6.164879       NaN  10.080162       NaN  0.241516       NaN
                                     neighbor_average     5.925444       NaN   9.740831       NaN  0.205419       NaN
       coverage                      gls_map              3.578187       NaN   5.924960       NaN  0.120431       NaN
                                     gsp                  4.617659       NaN   7.626246       NaN  0.173209       NaN
                                     historical_tod_mean  6.182657       NaN  10.104126       NaN  0.241580       NaN
                                     neighbor_average     5.794004       NaN   9.006297       NaN  0.198581       NaN
       degree                        gls_map              4.000777       NaN   6.468138       NaN  0.137108       NaN
                                     gsp                  4.585972       NaN   7.442830       NaN  0.165937       NaN
                                     historical_tod_mean  6.120811       NaN  10.023845       NaN  0.239799       NaN
                                     neighbor_average     6.793453       NaN  10.925977       NaN  0.241600       NaN
       graph_sampling_laplacian      gls_map              4.381012       NaN   7.250937       NaN  0.159697       NaN
                                     gsp                  4.867732       NaN   8.075893       NaN  0.189820       NaN
                                     historical_tod_mean  6.270917       NaN  10.269262       NaN  0.252019       NaN
                                     neighbor_average     6.722630       NaN  11.435509       NaN  0.258515       NaN
       greedy_a_trace                gls_map              3.349309       NaN   5.662971       NaN  0.116492       NaN
                                     gsp                  4.562104       NaN   7.514937       NaN  0.170386       NaN
                                     historical_tod_mean  6.134479       NaN  10.036674       NaN  0.240565       NaN
                                     neighbor_average     5.552664       NaN   8.795629       NaN  0.193434       NaN
       greedy_d_logdet               gls_map              4.342039       NaN   6.997887       NaN  0.137873       NaN
                                     gsp                  4.832631       NaN   7.824947       NaN  0.169282       NaN
                                     historical_tod_mean  6.334711       NaN  10.238270       NaN  0.242548       NaN
                                     neighbor_average     6.569540       NaN  10.902436       NaN  0.248974       NaN
       multistart_swap_by_validation gls_map              3.349540       NaN   5.614174       NaN  0.112928       NaN
                                     gsp                  4.586754       NaN   7.564783       NaN  0.170293       NaN
                                     historical_tod_mean  6.150900       NaN  10.032385       NaN  0.238738       NaN
                                     neighbor_average     5.700413       NaN   9.147840       NaN  0.192374       NaN
       observability_proxy           gls_map              3.936807       NaN   6.472674       NaN  0.137173       NaN
                                     gsp                  4.601288       NaN   7.461658       NaN  0.167165       NaN
                                     historical_tod_mean  6.127162       NaN  10.018850       NaN  0.240829       NaN
                                     neighbor_average     6.835499       NaN  11.120039       NaN  0.224257       NaN
       qr_pod_modes                  gls_map              3.661640       NaN   6.026042       NaN  0.119297       NaN
                                     gsp                  4.663939       NaN   7.612551       NaN  0.167698       NaN
                                     historical_tod_mean  6.225251       NaN  10.115257       NaN  0.241506       NaN
                                     neighbor_average     5.904956       NaN   9.612138       NaN  0.214318       NaN
       random                        gls_map              3.589043  0.068911   5.993547  0.121880  0.125012  0.004712
                                     gsp                  4.578802  0.032647   7.526434  0.085902  0.170146  0.004961
                                     historical_tod_mean  6.133171  0.043211  10.044735  0.066896  0.240342  0.004159
                                     neighbor_average     6.038052  0.277282   9.792370  0.509389  0.202038  0.013032
       rcss_selected                 gls_map              3.304063       NaN   5.614423       NaN  0.112872       NaN
                                     gsp                  4.578996       NaN   7.554086       NaN  0.171364       NaN
                                     historical_tod_mean  6.162045       NaN  10.065698       NaN  0.241146       NaN
                                     neighbor_average     5.872652       NaN   9.406013       NaN  0.203654       NaN
       robust_coverage_cvar          gls_map              3.576107       NaN   6.020914       NaN  0.125697       NaN
                                     gsp                  4.605825       NaN   7.610109       NaN  0.173989       NaN
                                     historical_tod_mean  6.188708       NaN  10.102068       NaN  0.243549       NaN
                                     neighbor_average     5.694763       NaN   9.084362       NaN  0.203170       NaN
       scenario_average_a_trace      gls_map              3.509967       NaN   6.028813       NaN  0.127206       NaN
                                     gsp                  4.663211       NaN   7.686989       NaN  0.176724       NaN
                                     historical_tod_mean  6.205490       NaN  10.128498       NaN  0.245194       NaN
                                     neighbor_average     6.140345       NaN  10.033952       NaN  0.220333       NaN
       scenario_cvar_a_trace         gls_map              3.623621       NaN   6.089242       NaN  0.124732       NaN
                                     gsp                  4.639511       NaN   7.608025       NaN  0.170490       NaN
                                     historical_tod_mean  6.225816       NaN  10.146831       NaN  0.243964       NaN
                                     neighbor_average     5.744701       NaN   9.565091       NaN  0.223958       NaN
       swap_from_best_random_trace   gls_map              3.349070       NaN   5.627982       NaN  0.115404       NaN
                                     gsp                  4.557240       NaN   7.504289       NaN  0.170129       NaN
                                     historical_tod_mean  6.150614       NaN  10.036507       NaN  0.240468       NaN
                                     neighbor_average     5.829074       NaN   9.250054       NaN  0.207946       NaN
       swap_from_greedy_a_trace      gls_map              3.321098       NaN   5.554283       NaN  0.111431       NaN
                                     gsp                  4.563155       NaN   7.504201       NaN  0.168956       NaN
                                     historical_tod_mean  6.142275       NaN  10.017272       NaN  0.238522       NaN
                                     neighbor_average     6.040942       NaN   9.493170       NaN  0.198166       NaN
       swap_from_scenario_average    gls_map              3.323598       NaN   5.546832       NaN  0.111157       NaN
                                     gsp                  4.566870       NaN   7.504857       NaN  0.168012       NaN
                                     historical_tod_mean  6.138462       NaN  10.007862       NaN  0.236713       NaN
                                     neighbor_average     5.916692       NaN   9.466095       NaN  0.192643       NaN
       swap_from_scenario_cvar       gls_map              3.304063       NaN   5.614423       NaN  0.112872       NaN
                                     gsp                  4.578996       NaN   7.554086       NaN  0.171364       NaN
                                     historical_tod_mean  6.162045       NaN  10.065698       NaN  0.241146       NaN
                                     neighbor_average     5.872652       NaN   9.406013       NaN  0.203654       NaN
       top_variance                  gls_map              3.901365       NaN   6.235661       NaN  0.126010       NaN
                                     gsp                  4.401733       NaN   7.160912       NaN  0.152015       NaN
                                     historical_tod_mean  5.691122       NaN   9.329947       NaN  0.201632       NaN
                                     neighbor_average     9.314718       NaN  15.128898       NaN  0.195994       NaN
       validation_swap_selected      gls_map              3.336293       NaN   5.584412       NaN  0.112835       NaN
                                     gsp                  4.550737       NaN   7.511967       NaN  0.170152       NaN
                                     historical_tod_mean  6.113610       NaN   9.998690       NaN  0.237975       NaN
                                     neighbor_average     6.189658       NaN   9.644072       NaN  0.200090       NaN
0.2    best_random_by_trace          gls_map              3.233416       NaN   5.416743       NaN  0.106902       NaN
                                     gsp                  4.531345       NaN   7.301956       NaN  0.160726       NaN
                                     historical_tod_mean  6.160512       NaN  10.068142       NaN  0.241197       NaN
                                     neighbor_average     5.306157       NaN   8.555624       NaN  0.163263       NaN
       best_random_by_validation     gls_map              3.121082       NaN   5.261043       NaN  0.103644       NaN
                                     gsp                  4.413242       NaN   7.155100       NaN  0.159103       NaN
                                     historical_tod_mean  6.028554       NaN   9.888706       NaN  0.233152       NaN
                                     neighbor_average     5.092787       NaN   8.158845       NaN  0.148736       NaN
       coverage                      gls_map              3.113689       NaN   5.133364       NaN  0.102986       NaN
                                     gsp                  4.493059       NaN   7.279219       NaN  0.162232       NaN
                                     historical_tod_mean  6.193641       NaN  10.100459       NaN  0.243196       NaN
                                     neighbor_average     4.797228       NaN   7.560420       NaN  0.157094       NaN
       degree                        gls_map              3.948606       NaN   6.477797       NaN  0.133208       NaN
                                     gsp                  4.576800       NaN   7.223048       NaN  0.159652       NaN
                                     historical_tod_mean  6.120026       NaN   9.966457       NaN  0.240302       NaN
                                     neighbor_average     6.887478       NaN  11.182028       NaN  0.238748       NaN
       graph_sampling_laplacian      gls_map              4.130034       NaN   6.933346       NaN  0.157925       NaN
                                     gsp                  4.794493       NaN   7.904959       NaN  0.186978       NaN
                                     historical_tod_mean  6.357477       NaN  10.444417       NaN  0.262373       NaN
                                     neighbor_average     6.847839       NaN  11.331469       NaN  0.274206       NaN
       greedy_a_trace                gls_map              3.113786       NaN   5.181254       NaN  0.102075       NaN
                                     gsp                  4.607537       NaN   7.390538       NaN  0.163004       NaN
                                     historical_tod_mean  6.289349       NaN  10.217019       NaN  0.246500       NaN
                                     neighbor_average     5.011006       NaN   8.099184       NaN  0.176174       NaN
       greedy_d_logdet               gls_map              3.992532       NaN   6.349853       NaN  0.128134       NaN
                                     gsp                  4.834204       NaN   7.598140       NaN  0.161726       NaN
                                     historical_tod_mean  6.471321       NaN  10.351684       NaN  0.246940       NaN
                                     neighbor_average     5.868016       NaN   9.823713       NaN  0.227900       NaN
       multistart_swap_by_validation gls_map              3.140818       NaN   5.221069       NaN  0.103097       NaN
                                     gsp                  4.617351       NaN   7.359286       NaN  0.159326       NaN
                                     historical_tod_mean  6.285966       NaN  10.196703       NaN  0.242856       NaN
                                     neighbor_average     4.946065       NaN   8.076530       NaN  0.174984       NaN
       observability_proxy           gls_map              3.765904       NaN   6.153064       NaN  0.125754       NaN
                                     gsp                  4.563646       NaN   7.241610       NaN  0.160023       NaN
                                     historical_tod_mean  6.101599       NaN   9.961827       NaN  0.239288       NaN
                                     neighbor_average     6.950224       NaN  11.198578       NaN  0.222239       NaN
       qr_pod_modes                  gls_map              3.313354       NaN   5.250854       NaN  0.101726       NaN
                                     gsp                  4.656105       NaN   7.352408       NaN  0.158325       NaN
                                     historical_tod_mean  6.335863       NaN  10.197042       NaN  0.243713       NaN
                                     neighbor_average     5.226134       NaN   8.487367       NaN  0.191533       NaN
       random                        gls_map              3.253493  0.064299   5.442729  0.141766  0.110304  0.005252
                                     gsp                  4.507840  0.042783   7.266284  0.087153  0.161485  0.005108
                                     historical_tod_mean  6.132220  0.055306  10.041317  0.083992  0.239886  0.005567
                                     neighbor_average     5.310720  0.194889   8.647295  0.369187  0.168776  0.009370
       rcss_selected                 gls_map              3.036377       NaN   5.088728       NaN  0.101187       NaN
                                     gsp                  4.407702       NaN   7.141740       NaN  0.159415       NaN
                                     historical_tod_mean  6.068525       NaN   9.927615       NaN  0.234300       NaN
                                     neighbor_average     5.109030       NaN   8.241076       NaN  0.149199       NaN
       robust_coverage_cvar          gls_map              3.281029       NaN   5.380013       NaN  0.105635       NaN
                                     gsp                  4.633689       NaN   7.389627       NaN  0.161783       NaN
                                     historical_tod_mean  6.292239       NaN  10.190914       NaN  0.245186       NaN
                                     neighbor_average     5.073331       NaN   8.102248       NaN  0.171817       NaN
       scenario_average_a_trace      gls_map              3.417133       NaN   5.705938       NaN  0.114678       NaN
                                     gsp                  4.694694       NaN   7.484914       NaN  0.166233       NaN
                                     historical_tod_mean  6.361411       NaN  10.296362       NaN  0.250898       NaN
                                     neighbor_average     5.302150       NaN   8.757856       NaN  0.202377       NaN
       scenario_cvar_a_trace         gls_map              3.395877       NaN   5.663991       NaN  0.114178       NaN
                                     gsp                  4.692214       NaN   7.513365       NaN  0.167341       NaN
                                     historical_tod_mean  6.376447       NaN  10.310299       NaN  0.251598       NaN
                                     neighbor_average     5.449319       NaN   8.994211       NaN  0.201471       NaN
       swap_from_best_random_trace   gls_map              3.098763       NaN   4.979087       NaN  0.096441       NaN
                                     gsp                  4.560901       NaN   7.261326       NaN  0.157607       NaN
                                     historical_tod_mean  6.223941       NaN  10.099652       NaN  0.240657       NaN
                                     neighbor_average     5.061988       NaN   7.954717       NaN  0.163769       NaN
       swap_from_greedy_a_trace      gls_map              3.142547       NaN   5.126565       NaN  0.099002       NaN
                                     gsp                  4.603907       NaN   7.310976       NaN  0.159066       NaN
                                     historical_tod_mean  6.294183       NaN  10.137324       NaN  0.241491       NaN
                                     neighbor_average     4.997982       NaN   8.211013       NaN  0.177553       NaN
       swap_from_scenario_average    gls_map              3.196955       NaN   5.241947       NaN  0.100536       NaN
                                     gsp                  4.623004       NaN   7.350952       NaN  0.155816       NaN
                                     historical_tod_mean  6.297428       NaN  10.145664       NaN  0.238824       NaN
                                     neighbor_average     4.993437       NaN   8.191014       NaN  0.176599       NaN
       swap_from_scenario_cvar       gls_map              3.205948       NaN   5.178818       NaN  0.099753       NaN
                                     gsp                  4.674217       NaN   7.399327       NaN  0.161362       NaN
                                     historical_tod_mean  6.360438       NaN  10.250660       NaN  0.246710       NaN
                                     neighbor_average     5.142862       NaN   8.345218       NaN  0.183333       NaN
       top_variance                  gls_map              3.411297       NaN   5.659175       NaN  0.106418       NaN
                                     gsp                  4.140421       NaN   6.644699       NaN  0.131917       NaN
                                     historical_tod_mean  5.393568       NaN   8.831047       NaN  0.177480       NaN
                                     neighbor_average     7.373557       NaN  12.321572       NaN  0.159432       NaN
       validation_swap_selected      gls_map              3.027948       NaN   5.043143       NaN  0.099994       NaN
                                     gsp                  4.403898       NaN   7.136331       NaN  0.159096       NaN
                                     historical_tod_mean  6.063883       NaN   9.911057       NaN  0.233625       NaN
                                     neighbor_average     5.160092       NaN   8.319207       NaN  0.157359       NaN
0.3    best_random_by_trace          gls_map              3.078488       NaN   5.068746       NaN  0.103309       NaN
                                     gsp                  4.533036       NaN   7.193095       NaN  0.161931       NaN
                                     historical_tod_mean  6.169592       NaN  10.057070       NaN  0.243956       NaN
                                     neighbor_average     4.874003       NaN   7.876349       NaN  0.155463       NaN
       best_random_by_validation     gls_map              2.872638       NaN   4.852858       NaN  0.097635       NaN
                                     gsp                  4.398154       NaN   7.123612       NaN  0.158823       NaN
                                     historical_tod_mean  5.995353       NaN   9.923283       NaN  0.236040       NaN
                                     neighbor_average     4.764040       NaN   7.500844       NaN  0.135698       NaN
       coverage                      gls_map              2.874020       NaN   4.728883       NaN  0.093422       NaN
                                     gsp                  4.483765       NaN   7.171101       NaN  0.157631       NaN
                                     historical_tod_mean  6.143512       NaN  10.053207       NaN  0.241747       NaN
                                     neighbor_average     4.655714       NaN   7.268426       NaN  0.139673       NaN
       degree                        gls_map              3.759610       NaN   6.073679       NaN  0.115710       NaN
                                     gsp                  4.599491       NaN   7.163556       NaN  0.147600       NaN
                                     historical_tod_mean  6.086668       NaN   9.784144       NaN  0.219659       NaN
                                     neighbor_average     7.463410       NaN  12.181525       NaN  0.212256       NaN
       graph_sampling_laplacian      gls_map              3.912137       NaN   6.686462       NaN  0.152159       NaN
                                     gsp                  4.737150       NaN   7.795153       NaN  0.186138       NaN
                                     historical_tod_mean  6.350489       NaN  10.489230       NaN  0.268408       NaN
                                     neighbor_average     6.882254       NaN  11.457993       NaN  0.270829       NaN
       greedy_a_trace                gls_map              2.985921       NaN   4.851446       NaN  0.093613       NaN
                                     gsp                  4.683817       NaN   7.374728       NaN  0.160360       NaN
                                     historical_tod_mean  6.414642       NaN  10.303127       NaN  0.247734       NaN
                                     neighbor_average     4.650907       NaN   7.500843       NaN  0.160271       NaN
       greedy_d_logdet               gls_map              3.508621       NaN   5.605419       NaN  0.112567       NaN
                                     gsp                  4.859824       NaN   7.595290       NaN  0.164754       NaN
                                     historical_tod_mean  6.578401       NaN  10.485382       NaN  0.254366       NaN
                                     neighbor_average     5.511545       NaN   9.295894       NaN  0.210482       NaN
       multistart_swap_by_validation gls_map              2.869626       NaN   4.718697       NaN  0.093462       NaN
                                     gsp                  4.548357       NaN   7.257171       NaN  0.159524       NaN
                                     historical_tod_mean  6.249288       NaN  10.189295       NaN  0.243686       NaN
                                     neighbor_average     4.568030       NaN   7.226715       NaN  0.147566       NaN
       observability_proxy           gls_map              3.747267       NaN   6.046296       NaN  0.115758       NaN
                                     gsp                  4.598437       NaN   7.177594       NaN  0.148473       NaN
                                     historical_tod_mean  6.083602       NaN   9.791836       NaN  0.220454       NaN
                                     neighbor_average     7.338808       NaN  12.035135       NaN  0.210759       NaN
       qr_pod_modes                  gls_map              2.997949       NaN   4.779868       NaN  0.092331       NaN
                                     gsp                  4.640008       NaN   7.290818       NaN  0.153724       NaN
                                     historical_tod_mean  6.391017       NaN  10.243658       NaN  0.238790       NaN
                                     neighbor_average     4.637268       NaN   7.366144       NaN  0.157475       NaN
       random                        gls_map              3.050017  0.050044   5.127761  0.140621  0.103070  0.005373
                                     gsp                  4.495498  0.049169   7.208624  0.110325  0.160355  0.006519
                                     historical_tod_mean  6.130366  0.072586  10.056837  0.128876  0.241359  0.008460
                                     neighbor_average     4.911741  0.129561   7.959115  0.298543  0.151659  0.010885
       rcss_selected                 gls_map              2.843140       NaN   4.803573       NaN  0.096366       NaN
                                     gsp                  4.349321       NaN   7.048026       NaN  0.157048       NaN
                                     historical_tod_mean  5.947346       NaN   9.857730       NaN  0.234263       NaN
                                     neighbor_average     4.819889       NaN   7.612170       NaN  0.130348       NaN
       robust_coverage_cvar          gls_map              3.151454       NaN   5.115334       NaN  0.101699       NaN
                                     gsp                  4.773001       NaN   7.495369       NaN  0.165979       NaN
                                     historical_tod_mean  6.507083       NaN  10.441474       NaN  0.256542       NaN
                                     neighbor_average     4.834779       NaN   7.820749       NaN  0.172971       NaN
       scenario_average_a_trace      gls_map              3.294029       NaN   5.482799       NaN  0.109061       NaN
                                     gsp                  4.767920       NaN   7.510766       NaN  0.165417       NaN
                                     historical_tod_mean  6.506387       NaN  10.461730       NaN  0.252636       NaN
                                     neighbor_average     5.099440       NaN   8.495221       NaN  0.197293       NaN
       scenario_cvar_a_trace         gls_map              3.266538       NaN   5.434202       NaN  0.107690       NaN
                                     gsp                  4.807710       NaN   7.585586       NaN  0.164868       NaN
                                     historical_tod_mean  6.556469       NaN  10.497713       NaN  0.253514       NaN
                                     neighbor_average     5.058807       NaN   8.426982       NaN  0.193253       NaN
       swap_from_best_random_trace   gls_map              3.025778       NaN   4.797018       NaN  0.094068       NaN
                                     gsp                  4.668173       NaN   7.290562       NaN  0.157904       NaN
                                     historical_tod_mean  6.363156       NaN  10.239398       NaN  0.245474       NaN
                                     neighbor_average     4.734108       NaN   7.519125       NaN  0.155705       NaN
       swap_from_greedy_a_trace      gls_map              2.950017       NaN   4.728060       NaN  0.091637       NaN
                                     gsp                  4.665152       NaN   7.314750       NaN  0.157411       NaN
                                     historical_tod_mean  6.409307       NaN  10.259138       NaN  0.244920       NaN
                                     neighbor_average     4.638499       NaN   7.479016       NaN  0.164596       NaN
       swap_from_scenario_average    gls_map              3.028445       NaN   4.865022       NaN  0.093166       NaN
                                     gsp                  4.683490       NaN   7.339288       NaN  0.157131       NaN
                                     historical_tod_mean  6.424681       NaN  10.281660       NaN  0.242848       NaN
                                     neighbor_average     4.745464       NaN   7.753295       NaN  0.170192       NaN
       swap_from_scenario_cvar       gls_map              3.013516       NaN   4.892408       NaN  0.093316       NaN
                                     gsp                  4.706465       NaN   7.374897       NaN  0.158694       NaN
                                     historical_tod_mean  6.444873       NaN  10.316729       NaN  0.246431       NaN
                                     neighbor_average     4.851807       NaN   7.876193       NaN  0.172097       NaN
       top_variance                  gls_map              3.048459       NaN   5.141037       NaN  0.093822       NaN
                                     gsp                  3.898874       NaN   6.256304       NaN  0.117041       NaN
                                     historical_tod_mean  5.129393       NaN   8.376470       NaN  0.157477       NaN
                                     neighbor_average     6.310997       NaN  10.598781       NaN  0.133053       NaN
       validation_swap_selected      gls_map              2.821069       NaN   4.800174       NaN  0.097044       NaN
                                     gsp                  4.327573       NaN   7.060498       NaN  0.158209       NaN
                                     historical_tod_mean  5.931630       NaN   9.854736       NaN  0.234234       NaN
                                     neighbor_average     4.798898       NaN   7.539293       NaN  0.132813       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1  swap_from_scenario_cvar gls_map 3.304063 5.614423
    0.2 validation_swap_selected gls_map 3.027948 5.043143
    0.3 validation_swap_selected gls_map 2.821069 4.800174
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.282042      0.332003 210
    gsp   condition_number     0.283340      0.361853 210
    gsp information_logdet    -0.229929     -0.343576 210
gls_map    posterior_trace     0.853516      0.860763 210
gls_map   condition_number     0.861345      0.889521 210
gls_map information_logdet    -0.739020     -0.810171 210
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv