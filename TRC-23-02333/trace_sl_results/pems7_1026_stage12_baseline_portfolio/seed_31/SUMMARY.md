---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: TRC-23-02333/dataset/PeMS7_1026
Validation days: 2012-06-25, 2012-06-06
Test days: 2012-06-01, 2012-06-08
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 100
Selection method: gls_map
Phase 3 baseline portfolio: observability_proxy is an observability/coverage-style proxy for TSLP-style reviewer comparison; all implemented Phase 3 rows are still judged by held-out hidden-node reconstruction metrics.

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               4.471288       NaN   7.343098       NaN  0.126508       NaN
                                     gsp                   4.825276       NaN   8.340981       NaN  0.144492       NaN
                                     historical_tod_mean   4.868632       NaN   8.691044       NaN  0.151249       NaN
                                     neighbor_average      8.255223       NaN  12.496677       NaN  0.240632       NaN
       best_random_by_validation     gls_map               4.324070       NaN   7.316825       NaN  0.124388       NaN
                                     gsp                   4.841343       NaN   8.349116       NaN  0.144442       NaN
                                     historical_tod_mean   4.878891       NaN   8.734186       NaN  0.152057       NaN
                                     neighbor_average      8.218716       NaN  12.454162       NaN  0.236696       NaN
       coverage                      gls_map               4.450238       NaN   7.375622       NaN  0.125180       NaN
                                     gsp                   4.826512       NaN   8.328659       NaN  0.143483       NaN
                                     historical_tod_mean   4.876610       NaN   8.727275       NaN  0.152395       NaN
                                     neighbor_average      8.501699       NaN  12.552618       NaN  0.233413       NaN
       degree                        gls_map               4.869172       NaN   8.340401       NaN  0.142264       NaN
                                     gsp                   4.860288       NaN   8.504058       NaN  0.149047       NaN
                                     historical_tod_mean   4.885219       NaN   8.802854       NaN  0.153565       NaN
                                     neighbor_average      9.378064       NaN  13.497800       NaN  0.265373       NaN
       graph_sampling_laplacian      gls_map               5.536745       NaN   8.769816       NaN  0.159483       NaN
                                     gsp                   4.945301       NaN   8.439913       NaN  0.146812       NaN
                                     historical_tod_mean   4.932713       NaN   8.767753       NaN  0.154865       NaN
                                     neighbor_average      9.303557       NaN  14.871729       NaN  0.317081       NaN
       greedy_a_trace                gls_map               4.148897       NaN   7.033645       NaN  0.117601       NaN
                                     gsp                   4.816457       NaN   8.342297       NaN  0.143426       NaN
                                     historical_tod_mean   4.872728       NaN   8.729320       NaN  0.152391       NaN
                                     neighbor_average      7.897733       NaN  12.042494       NaN  0.237368       NaN
       greedy_d_logdet               gls_map               4.982885       NaN   8.055333       NaN  0.139393       NaN
                                     gsp                   4.793325       NaN   8.420621       NaN  0.144547       NaN
                                     historical_tod_mean   4.840376       NaN   8.716838       NaN  0.152051       NaN
                                     neighbor_average      8.891190       NaN  13.798100       NaN  0.287906       NaN
       multistart_swap_by_validation gls_map               4.228603       NaN   7.094572       NaN  0.119395       NaN
                                     gsp                   4.804891       NaN   8.324022       NaN  0.143049       NaN
                                     historical_tod_mean   4.860731       NaN   8.709037       NaN  0.150977       NaN
                                     neighbor_average      8.200208       NaN  12.390062       NaN  0.242131       NaN
       observability_proxy           gls_map               4.864423       NaN   8.325336       NaN  0.142592       NaN
                                     gsp                   4.869282       NaN   8.503616       NaN  0.149036       NaN
                                     historical_tod_mean   4.886174       NaN   8.807030       NaN  0.153370       NaN
                                     neighbor_average     11.564757       NaN  16.822618       NaN  0.272539       NaN
       qr_pod_modes                  gls_map               4.530337       NaN   7.322053       NaN  0.126167       NaN
                                     gsp                   4.763111       NaN   8.270189       NaN  0.140309       NaN
                                     historical_tod_mean   4.811618       NaN   8.638285       NaN  0.148644       NaN
                                     neighbor_average      8.494687       NaN  12.950462       NaN  0.265506       NaN
       random                        gls_map               4.372177  0.052907   7.343275  0.101546  0.122175  0.003061
                                     gsp                   4.848517  0.022899   8.356265  0.046688  0.143591  0.001968
                                     historical_tod_mean   4.887152  0.022037   8.744970  0.037033  0.152349  0.001338
                                     neighbor_average      8.383442  0.146929  12.735494  0.216583  0.236408  0.006377
       rcss_selected                 gls_map               4.135018       NaN   6.962417       NaN  0.117068       NaN
                                     gsp                   4.800788       NaN   8.328835       NaN  0.143075       NaN
                                     historical_tod_mean   4.867335       NaN   8.721755       NaN  0.152427       NaN
                                     neighbor_average      7.976868       NaN  12.205129       NaN  0.241458       NaN
       robust_coverage_cvar          gls_map               4.311938       NaN   7.204339       NaN  0.121272       NaN
                                     gsp                   4.786076       NaN   8.320038       NaN  0.143367       NaN
                                     historical_tod_mean   4.847891       NaN   8.690544       NaN  0.151576       NaN
                                     neighbor_average      8.451334       NaN  12.783926       NaN  0.248072       NaN
       scenario_average_a_trace      gls_map               4.345408       NaN   7.260081       NaN  0.122657       NaN
                                     gsp                   4.786052       NaN   8.356058       NaN  0.144081       NaN
                                     historical_tod_mean   4.853959       NaN   8.696802       NaN  0.151445       NaN
                                     neighbor_average      8.413533       NaN  12.564411       NaN  0.247189       NaN
       scenario_cvar_a_trace         gls_map               4.353839       NaN   7.248729       NaN  0.119729       NaN
                                     gsp                   4.771192       NaN   8.287564       NaN  0.140737       NaN
                                     historical_tod_mean   4.831880       NaN   8.668489       NaN  0.150044       NaN
                                     neighbor_average      8.675938       NaN  12.860296       NaN  0.241397       NaN
       swap_from_best_random_trace   gls_map               4.293876       NaN   7.052678       NaN  0.119364       NaN
                                     gsp                   4.802876       NaN   8.308311       NaN  0.142158       NaN
                                     historical_tod_mean   4.866468       NaN   8.689331       NaN  0.150695       NaN
                                     neighbor_average      7.986208       NaN  12.206071       NaN  0.241445       NaN
       swap_from_greedy_a_trace      gls_map               4.135018       NaN   6.962417       NaN  0.117068       NaN
                                     gsp                   4.800788       NaN   8.328835       NaN  0.143075       NaN
                                     historical_tod_mean   4.867335       NaN   8.721755       NaN  0.152427       NaN
                                     neighbor_average      7.976868       NaN  12.205129       NaN  0.241458       NaN
       swap_from_scenario_average    gls_map               4.230623       NaN   7.036978       NaN  0.117438       NaN
                                     gsp                   4.760459       NaN   8.334962       NaN  0.142553       NaN
                                     historical_tod_mean   4.845727       NaN   8.684232       NaN  0.150992       NaN
                                     neighbor_average      8.261168       NaN  12.550196       NaN  0.249131       NaN
       swap_from_scenario_cvar       gls_map               4.225388       NaN   7.029551       NaN  0.115937       NaN
                                     gsp                   4.750263       NaN   8.257174       NaN  0.139691       NaN
                                     historical_tod_mean   4.814716       NaN   8.633347       NaN  0.148995       NaN
                                     neighbor_average      8.197715       NaN  12.263801       NaN  0.234088       NaN
       top_variance                  gls_map               4.579871       NaN   7.627633       NaN  0.127281       NaN
                                     gsp                   4.706603       NaN   8.109097       NaN  0.135602       NaN
                                     historical_tod_mean   4.657294       NaN   8.418271       NaN  0.139273       NaN
                                     neighbor_average     12.329420       NaN  18.142964       NaN  0.252369       NaN
       validation_swap_selected      gls_map               4.227301       NaN   7.111733       NaN  0.120048       NaN
                                     gsp                   4.797384       NaN   8.327322       NaN  0.143772       NaN
                                     historical_tod_mean   4.851942       NaN   8.705402       NaN  0.151159       NaN
                                     neighbor_average      8.231297       NaN  12.455177       NaN  0.243033       NaN
0.2    best_random_by_trace          gls_map               4.009338       NaN   6.567308       NaN  0.106762       NaN
                                     gsp                   4.810143       NaN   8.273907       NaN  0.140736       NaN
                                     historical_tod_mean   4.855823       NaN   8.708432       NaN  0.150430       NaN
                                     neighbor_average      7.952331       NaN  12.156614       NaN  0.220134       NaN
       best_random_by_validation     gls_map               3.994055       NaN   6.679739       NaN  0.108445       NaN
                                     gsp                   4.854140       NaN   8.280648       NaN  0.141378       NaN
                                     historical_tod_mean   4.866872       NaN   8.704543       NaN  0.150063       NaN
                                     neighbor_average      8.046150       NaN  12.187836       NaN  0.225593       NaN
       coverage                      gls_map               4.010915       NaN   6.670402       NaN  0.112903       NaN
                                     gsp                   4.859068       NaN   8.286756       NaN  0.143608       NaN
                                     historical_tod_mean   4.874775       NaN   8.734259       NaN  0.154041       NaN
                                     neighbor_average      7.882181       NaN  12.027021       NaN  0.223986       NaN
       degree                        gls_map               4.851757       NaN   8.352139       NaN  0.143566       NaN
                                     gsp                   4.926434       NaN   8.564068       NaN  0.152381       NaN
                                     historical_tod_mean   4.911728       NaN   8.927277       NaN  0.157256       NaN
                                     neighbor_average     10.019677       NaN  14.003128       NaN  0.253868       NaN
       graph_sampling_laplacian      gls_map               5.178149       NaN   8.429807       NaN  0.145495       NaN
                                     gsp                   5.023844       NaN   8.489377       NaN  0.150851       NaN
                                     historical_tod_mean   4.999485       NaN   8.870298       NaN  0.159224       NaN
                                     neighbor_average      8.837357       NaN  13.149934       NaN  0.265352       NaN
       greedy_a_trace                gls_map               3.682360       NaN   6.076934       NaN  0.100522       NaN
                                     gsp                   4.742492       NaN   8.202769       NaN  0.138269       NaN
                                     historical_tod_mean   4.802945       NaN   8.631577       NaN  0.148492       NaN
                                     neighbor_average      7.741282       NaN  11.829278       NaN  0.230703       NaN
       greedy_d_logdet               gls_map               4.256260       NaN   7.013153       NaN  0.120833       NaN
                                     gsp                   4.757137       NaN   8.304016       NaN  0.142328       NaN
                                     historical_tod_mean   4.831290       NaN   8.706529       NaN  0.152571       NaN
                                     neighbor_average      8.386063       NaN  13.060434       NaN  0.272036       NaN
       multistart_swap_by_validation gls_map               3.865342       NaN   6.443422       NaN  0.105178       NaN
                                     gsp                   4.828094       NaN   8.231490       NaN  0.141144       NaN
                                     historical_tod_mean   4.815369       NaN   8.669862       NaN  0.150452       NaN
                                     neighbor_average      7.863334       NaN  11.897504       NaN  0.218431       NaN
       observability_proxy           gls_map               4.845917       NaN   8.283537       NaN  0.142565       NaN
                                     gsp                   4.909843       NaN   8.547292       NaN  0.151976       NaN
                                     historical_tod_mean   4.897776       NaN   8.912728       NaN  0.157105       NaN
                                     neighbor_average     10.667591       NaN  15.032138       NaN  0.268709       NaN
       qr_pod_modes                  gls_map               3.959691       NaN   6.441256       NaN  0.107666       NaN
                                     gsp                   4.747264       NaN   8.225097       NaN  0.139286       NaN
                                     historical_tod_mean   4.802121       NaN   8.648375       NaN  0.149567       NaN
                                     neighbor_average      7.933600       NaN  12.137086       NaN  0.245212       NaN
       random                        gls_map               4.022974  0.050320   6.713052  0.129224  0.109802  0.003108
                                     gsp                   4.877725  0.033419   8.310981  0.055832  0.142441  0.002210
                                     historical_tod_mean   4.887172  0.033135   8.744286  0.055510  0.152189  0.002013
                                     neighbor_average      8.013720  0.110880  12.306500  0.204325  0.224814  0.005866
       rcss_selected                 gls_map               3.694930       NaN   6.086293       NaN  0.101003       NaN
                                     gsp                   4.733100       NaN   8.191640       NaN  0.138172       NaN
                                     historical_tod_mean   4.795279       NaN   8.620443       NaN  0.148419       NaN
                                     neighbor_average      7.778018       NaN  11.980218       NaN  0.236322       NaN
       robust_coverage_cvar          gls_map               3.976449       NaN   6.518784       NaN  0.107861       NaN
                                     gsp                   4.760697       NaN   8.176408       NaN  0.139069       NaN
                                     historical_tod_mean   4.805332       NaN   8.612056       NaN  0.148809       NaN
                                     neighbor_average      8.185698       NaN  12.650354       NaN  0.238612       NaN
       scenario_average_a_trace      gls_map               4.123708       NaN   6.809817       NaN  0.113244       NaN
                                     gsp                   4.816019       NaN   8.274149       NaN  0.141198       NaN
                                     historical_tod_mean   4.850079       NaN   8.691418       NaN  0.150961       NaN
                                     neighbor_average      8.231074       NaN  12.659415       NaN  0.250674       NaN
       scenario_cvar_a_trace         gls_map               4.003048       NaN   6.623242       NaN  0.108062       NaN
                                     gsp                   4.737927       NaN   8.147807       NaN  0.137985       NaN
                                     historical_tod_mean   4.760984       NaN   8.581881       NaN  0.147415       NaN
                                     neighbor_average      8.361224       NaN  12.924475       NaN  0.238806       NaN
       swap_from_best_random_trace   gls_map               3.843775       NaN   6.300993       NaN  0.103075       NaN
                                     gsp                   4.775827       NaN   8.246239       NaN  0.140497       NaN
                                     historical_tod_mean   4.821453       NaN   8.683118       NaN  0.150962       NaN
                                     neighbor_average      7.711065       NaN  11.689693       NaN  0.221442       NaN
       swap_from_greedy_a_trace      gls_map               3.694930       NaN   6.086293       NaN  0.101003       NaN
                                     gsp                   4.733100       NaN   8.191640       NaN  0.138172       NaN
                                     historical_tod_mean   4.795279       NaN   8.620443       NaN  0.148419       NaN
                                     neighbor_average      7.778018       NaN  11.980218       NaN  0.236322       NaN
       swap_from_scenario_average    gls_map               3.966962       NaN   6.585420       NaN  0.109855       NaN
                                     gsp                   4.794116       NaN   8.277170       NaN  0.141777       NaN
                                     historical_tod_mean   4.838202       NaN   8.696946       NaN  0.151669       NaN
                                     neighbor_average      8.090010       NaN  12.452749       NaN  0.249192       NaN
       swap_from_scenario_cvar       gls_map               3.834208       NaN   6.348466       NaN  0.103851       NaN
                                     gsp                   4.729695       NaN   8.131884       NaN  0.137246       NaN
                                     historical_tod_mean   4.748693       NaN   8.561568       NaN  0.146820       NaN
                                     neighbor_average      8.056863       NaN  12.447381       NaN  0.233050       NaN
       top_variance                  gls_map               4.276630       NaN   7.160377       NaN  0.113469       NaN
                                     gsp                   4.580944       NaN   7.858165       NaN  0.127733       NaN
                                     historical_tod_mean   4.489295       NaN   8.181928       NaN  0.131750       NaN
                                     neighbor_average     10.535935       NaN  16.087351       NaN  0.220546       NaN
       validation_swap_selected      gls_map               3.681099       NaN   6.058158       NaN  0.100270       NaN
                                     gsp                   4.730561       NaN   8.190854       NaN  0.138014       NaN
                                     historical_tod_mean   4.792899       NaN   8.621370       NaN  0.148234       NaN
                                     neighbor_average      7.733609       NaN  11.823452       NaN  0.230563       NaN
0.3    best_random_by_trace          gls_map               3.718016       NaN   6.121377       NaN  0.099158       NaN
                                     gsp                   4.882580       NaN   8.242772       NaN  0.140108       NaN
                                     historical_tod_mean   4.847772       NaN   8.664598       NaN  0.149964       NaN
                                     neighbor_average      7.832748       NaN  11.960288       NaN  0.216997       NaN
       best_random_by_validation     gls_map               3.679820       NaN   6.119588       NaN  0.097608       NaN
                                     gsp                   4.830571       NaN   8.231854       NaN  0.138771       NaN
                                     historical_tod_mean   4.852209       NaN   8.677942       NaN  0.148041       NaN
                                     neighbor_average      7.603636       NaN  11.625798       NaN  0.210341       NaN
       coverage                      gls_map               3.817880       NaN   6.379750       NaN  0.108847       NaN
                                     gsp                   4.910726       NaN   8.322135       NaN  0.146676       NaN
                                     historical_tod_mean   4.925757       NaN   8.790993       NaN  0.157570       NaN
                                     neighbor_average      7.782561       NaN  12.152409       NaN  0.228598       NaN
       degree                        gls_map               4.720778       NaN   8.097469       NaN  0.136242       NaN
                                     gsp                   4.862133       NaN   8.462534       NaN  0.147296       NaN
                                     historical_tod_mean   4.837873       NaN   8.873597       NaN  0.154467       NaN
                                     neighbor_average      9.081131       NaN  13.719819       NaN  0.250861       NaN
       graph_sampling_laplacian      gls_map               4.969432       NaN   8.179395       NaN  0.138552       NaN
                                     gsp                   4.921257       NaN   8.273190       NaN  0.144563       NaN
                                     historical_tod_mean   4.913062       NaN   8.702666       NaN  0.155498       NaN
                                     neighbor_average      9.323694       NaN  14.395513       NaN  0.299818       NaN
       greedy_a_trace                gls_map               3.399872       NaN   5.563809       NaN  0.092602       NaN
                                     gsp                   4.733620       NaN   8.157075       NaN  0.138426       NaN
                                     historical_tod_mean   4.800177       NaN   8.623538       NaN  0.149405       NaN
                                     neighbor_average      7.597128       NaN  11.717186       NaN  0.232793       NaN
       greedy_d_logdet               gls_map               3.824435       NaN   6.307969       NaN  0.106804       NaN
                                     gsp                   4.738424       NaN   8.202593       NaN  0.139818       NaN
                                     historical_tod_mean   4.794808       NaN   8.665157       NaN  0.151610       NaN
                                     neighbor_average      8.153874       NaN  12.708749       NaN  0.259926       NaN
       multistart_swap_by_validation gls_map               3.509057       NaN   5.804580       NaN  0.092581       NaN
                                     gsp                   4.775442       NaN   8.160236       NaN  0.136821       NaN
                                     historical_tod_mean   4.804108       NaN   8.615849       NaN  0.146813       NaN
                                     neighbor_average      7.502882       NaN  11.389345       NaN  0.208234       NaN
       observability_proxy           gls_map               4.692559       NaN   8.067040       NaN  0.135420       NaN
                                     gsp                   4.861685       NaN   8.472903       NaN  0.147435       NaN
                                     historical_tod_mean   4.839110       NaN   8.884517       NaN  0.154605       NaN
                                     neighbor_average      9.114553       NaN  13.739488       NaN  0.246885       NaN
       qr_pod_modes                  gls_map               3.500711       NaN   5.688583       NaN  0.096195       NaN
                                     gsp                   4.717556       NaN   8.130549       NaN  0.138579       NaN
                                     historical_tod_mean   4.773178       NaN   8.611583       NaN  0.149918       NaN
                                     neighbor_average      7.645505       NaN  11.806566       NaN  0.236757       NaN
       random                        gls_map               3.780799  0.057154   6.289144  0.120614  0.102377  0.002903
                                     gsp                   4.891113  0.039943   8.290031  0.072945  0.142114  0.002529
                                     historical_tod_mean   4.880684  0.047804   8.733161  0.078089  0.152064  0.002568
                                     neighbor_average      7.830389  0.099646  12.133300  0.186917  0.219329  0.005357
       rcss_selected                 gls_map               3.406649       NaN   5.551906       NaN  0.092557       NaN
                                     gsp                   4.702795       NaN   8.114100       NaN  0.137197       NaN
                                     historical_tod_mean   4.765364       NaN   8.580193       NaN  0.148338       NaN
                                     neighbor_average      7.675053       NaN  11.802197       NaN  0.235114       NaN
       robust_coverage_cvar          gls_map               3.825707       NaN   6.256006       NaN  0.102028       NaN
                                     gsp                   4.779178       NaN   8.143318       NaN  0.137962       NaN
                                     historical_tod_mean   4.800084       NaN   8.599266       NaN  0.147857       NaN
                                     neighbor_average      8.262778       NaN  13.053064       NaN  0.245709       NaN
       scenario_average_a_trace      gls_map               3.834281       NaN   6.289225       NaN  0.102265       NaN
                                     gsp                   4.768875       NaN   8.182188       NaN  0.138503       NaN
                                     historical_tod_mean   4.811578       NaN   8.639133       NaN  0.149496       NaN
                                     neighbor_average      8.188779       NaN  12.823593       NaN  0.245696       NaN
       scenario_cvar_a_trace         gls_map               3.852098       NaN   6.285707       NaN  0.101796       NaN
                                     gsp                   4.703304       NaN   8.071443       NaN  0.135890       NaN
                                     historical_tod_mean   4.735312       NaN   8.533683       NaN  0.146250       NaN
                                     neighbor_average      8.545189       NaN  13.365594       NaN  0.247732       NaN
       swap_from_best_random_trace   gls_map               3.572909       NaN   5.832176       NaN  0.094589       NaN
                                     gsp                   4.797868       NaN   8.140794       NaN  0.137968       NaN
                                     historical_tod_mean   4.792370       NaN   8.588287       NaN  0.148269       NaN
                                     neighbor_average      7.788573       NaN  11.791375       NaN  0.218419       NaN
       swap_from_greedy_a_trace      gls_map               3.406649       NaN   5.551906       NaN  0.092557       NaN
                                     gsp                   4.702795       NaN   8.114100       NaN  0.137197       NaN
                                     historical_tod_mean   4.765364       NaN   8.580193       NaN  0.148338       NaN
                                     neighbor_average      7.675053       NaN  11.802197       NaN  0.235114       NaN
       swap_from_scenario_average    gls_map               3.655687       NaN   6.000991       NaN  0.098634       NaN
                                     gsp                   4.749094       NaN   8.173908       NaN  0.138637       NaN
                                     historical_tod_mean   4.797026       NaN   8.644072       NaN  0.149769       NaN
                                     neighbor_average      7.952925       NaN  12.403729       NaN  0.239364       NaN
       swap_from_scenario_cvar       gls_map               3.691372       NaN   6.033979       NaN  0.097966       NaN
                                     gsp                   4.692159       NaN   8.066409       NaN  0.135573       NaN
                                     historical_tod_mean   4.735770       NaN   8.541046       NaN  0.146313       NaN
                                     neighbor_average      8.202552       NaN  12.842251       NaN  0.239734       NaN
       top_variance                  gls_map               3.928622       NaN   6.627279       NaN  0.100864       NaN
                                     gsp                   4.415930       NaN   7.582241       NaN  0.119475       NaN
                                     historical_tod_mean   4.259422       NaN   7.862509       NaN  0.121858       NaN
                                     neighbor_average     10.191074       NaN  15.573011       NaN  0.207545       NaN
       validation_swap_selected      gls_map               3.387849       NaN   5.528411       NaN  0.092434       NaN
                                     gsp                   4.692807       NaN   8.102029       NaN  0.137228       NaN
                                     historical_tod_mean   4.750232       NaN   8.565025       NaN  0.148256       NaN
                                     neighbor_average      7.660521       NaN  11.796765       NaN  0.234716       NaN
```

## Best method per budget-layout row

```
 budget              layout_type  method      mae     rmse
    0.1 swap_from_greedy_a_trace gls_map 4.135018 6.962417
    0.2 validation_swap_selected gls_map 3.681099 6.058158
    0.3 validation_swap_selected gls_map 3.387849 5.528411
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace    -0.204901     -0.273911 360
    gsp   condition_number    -0.205458     -0.381621 360
    gsp information_logdet     0.189912      0.248968 360
gls_map    posterior_trace     0.921638      0.934766 360
gls_map   condition_number     0.812287      0.907113 360
gls_map information_logdet    -0.850968     -0.888996 360
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv