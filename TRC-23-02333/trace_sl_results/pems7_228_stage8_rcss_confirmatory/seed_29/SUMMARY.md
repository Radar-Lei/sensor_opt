---
status: complete
---

# TRACE-SL CPU Pilot Summary

Dataset: /home/samuel/projects/sensor_opt/TRC-23-02333/dataset/PeMS7_228
Validation days: 2012-05-21, 2012-05-16
Test days: 2012-05-11, 2012-05-14
Budgets: [0.1, 0.2, 0.3]
Random layouts per budget: 200
Selection method: gls_map

## Mean metrics by budget and method

```
                                                                mae                 rmse                mape
                                                               mean       std       mean       std      mean       std
budget layout_type                   method
0.1    best_random_by_trace          gls_map               3.693734       NaN   6.421496       NaN  0.094806       NaN
                                     gsp                   3.992464       NaN   6.836795       NaN  0.101385       NaN
                                     historical_tod_mean   4.150978       NaN   7.356243       NaN  0.105260       NaN
                                     neighbor_average      7.241107       NaN  11.342132       NaN  0.187615       NaN
       best_random_by_validation     gls_map               3.603760       NaN   6.208999       NaN  0.092015       NaN
                                     gsp                   3.894208       NaN   6.751896       NaN  0.098414       NaN
                                     historical_tod_mean   4.068994       NaN   7.275582       NaN  0.103968       NaN
                                     neighbor_average      7.778146       NaN  11.694943       NaN  0.187658       NaN
       coverage                      gls_map               3.962150       NaN   6.691198       NaN  0.098815       NaN
                                     gsp                   4.047868       NaN   7.015191       NaN  0.102471       NaN
                                     historical_tod_mean   4.179729       NaN   7.441585       NaN  0.107101       NaN
                                     neighbor_average      7.609647       NaN  11.700131       NaN  0.204800       NaN
       degree                        gls_map               4.144662       NaN   7.050771       NaN  0.107697       NaN
                                     gsp                   4.168706       NaN   7.091238       NaN  0.103669       NaN
                                     historical_tod_mean   4.206654       NaN   7.440047       NaN  0.107678       NaN
                                     neighbor_average      8.270752       NaN  12.674822       NaN  0.222807       NaN
       greedy_a_trace                gls_map               3.568196       NaN   6.098406       NaN  0.089937       NaN
                                     gsp                   4.079055       NaN   6.934218       NaN  0.100550       NaN
                                     historical_tod_mean   4.188650       NaN   7.376992       NaN  0.106329       NaN
                                     neighbor_average      7.130705       NaN  10.978255       NaN  0.197354       NaN
       greedy_d_logdet               gls_map               4.258759       NaN   6.963611       NaN  0.104708       NaN
                                     gsp                   4.164994       NaN   7.083275       NaN  0.100957       NaN
                                     historical_tod_mean   4.176906       NaN   7.377455       NaN  0.106235       NaN
                                     neighbor_average      7.743199       NaN  12.560200       NaN  0.230898       NaN
       multistart_swap_by_validation gls_map               3.491656       NaN   5.921371       NaN  0.087406       NaN
                                     gsp                   4.058784       NaN   6.872185       NaN  0.100603       NaN
                                     historical_tod_mean   4.179986       NaN   7.342720       NaN  0.105603       NaN
                                     neighbor_average      7.097125       NaN  11.147415       NaN  0.195484       NaN
       random                        gls_map               3.804453  0.092828   6.476967  0.136703  0.096095  0.003084
                                     gsp                   4.029524  0.060761   6.936177  0.089686  0.101305  0.002250
                                     historical_tod_mean   4.164653  0.037338   7.390129  0.058315  0.106179  0.001397
                                     neighbor_average      7.509849  0.260740  11.600568  0.364082  0.196020  0.008878
       rcss_selected                 gls_map               3.510226       NaN   5.953728       NaN  0.088560       NaN
                                     gsp                   4.045243       NaN   6.845410       NaN  0.099490       NaN
                                     historical_tod_mean   4.152617       NaN   7.296229       NaN  0.104357       NaN
                                     neighbor_average      7.277066       NaN  11.303451       NaN  0.198432       NaN
       robust_coverage_cvar          gls_map               3.597616       NaN   6.236536       NaN  0.093733       NaN
                                     gsp                   3.958339       NaN   6.903698       NaN  0.102214       NaN
                                     historical_tod_mean   4.147151       NaN   7.354915       NaN  0.106022       NaN
                                     neighbor_average      7.342319       NaN  11.192417       NaN  0.192627       NaN
       scenario_average_a_trace      gls_map               3.764603       NaN   6.446531       NaN  0.098750       NaN
                                     gsp                   4.106956       NaN   6.945518       NaN  0.104403       NaN
                                     historical_tod_mean   4.178751       NaN   7.391714       NaN  0.107242       NaN
                                     neighbor_average      7.397308       NaN  11.459127       NaN  0.206394       NaN
       scenario_cvar_a_trace         gls_map               3.673163       NaN   6.313426       NaN  0.091739       NaN
                                     gsp                   4.088962       NaN   7.001300       NaN  0.102746       NaN
                                     historical_tod_mean   4.199039       NaN   7.451555       NaN  0.107363       NaN
                                     neighbor_average      7.251556       NaN  10.906625       NaN  0.194900       NaN
       swap_from_best_random_trace   gls_map               3.491656       NaN   5.921371       NaN  0.087406       NaN
                                     gsp                   4.058784       NaN   6.872185       NaN  0.100603       NaN
                                     historical_tod_mean   4.179986       NaN   7.342720       NaN  0.105603       NaN
                                     neighbor_average      7.097125       NaN  11.147415       NaN  0.195484       NaN
       swap_from_greedy_a_trace      gls_map               3.534005       NaN   6.074593       NaN  0.089626       NaN
                                     gsp                   4.071740       NaN   6.904487       NaN  0.101039       NaN
                                     historical_tod_mean   4.178210       NaN   7.341989       NaN  0.105588       NaN
                                     neighbor_average      7.182699       NaN  11.275080       NaN  0.199279       NaN
       swap_from_scenario_average    gls_map               3.510226       NaN   5.953728       NaN  0.088560       NaN
                                     gsp                   4.045243       NaN   6.845410       NaN  0.099490       NaN
                                     historical_tod_mean   4.152617       NaN   7.296229       NaN  0.104357       NaN
                                     neighbor_average      7.277066       NaN  11.303451       NaN  0.198432       NaN
       swap_from_scenario_cvar       gls_map               3.593330       NaN   6.157907       NaN  0.091888       NaN
                                     gsp                   4.080352       NaN   6.947536       NaN  0.100926       NaN
                                     historical_tod_mean   4.197470       NaN   7.399373       NaN  0.106403       NaN
                                     neighbor_average      7.181703       NaN  11.229134       NaN  0.200998       NaN
       top_variance                  gls_map               3.719811       NaN   6.466041       NaN  0.088628       NaN
                                     gsp                   3.845896       NaN   6.644353       NaN  0.092170       NaN
                                     historical_tod_mean   3.927284       NaN   7.013532       NaN  0.095451       NaN
                                     neighbor_average     11.166549       NaN  16.926798       NaN  0.213926       NaN
0.2    best_random_by_trace          gls_map               3.558638       NaN   5.994036       NaN  0.088395       NaN
                                     gsp                   4.014834       NaN   6.848913       NaN  0.099981       NaN
                                     historical_tod_mean   4.148202       NaN   7.349771       NaN  0.106100       NaN
                                     neighbor_average      7.100533       NaN  11.197818       NaN  0.202907       NaN
       best_random_by_validation     gls_map               3.403477       NaN   5.899769       NaN  0.086391       NaN
                                     gsp                   3.885390       NaN   6.744049       NaN  0.097874       NaN
                                     historical_tod_mean   4.055129       NaN   7.301950       NaN  0.103248       NaN
                                     neighbor_average      7.371259       NaN  11.123434       NaN  0.185506       NaN
       coverage                      gls_map               3.587637       NaN   6.190443       NaN  0.091069       NaN
                                     gsp                   4.042309       NaN   6.951600       NaN  0.100973       NaN
                                     historical_tod_mean   4.195469       NaN   7.484669       NaN  0.108007       NaN
                                     neighbor_average      7.185229       NaN  11.118703       NaN  0.189546       NaN
       degree                        gls_map               4.124089       NaN   6.861998       NaN  0.103806       NaN
                                     gsp                   4.195651       NaN   7.039640       NaN  0.102689       NaN
                                     historical_tod_mean   4.260572       NaN   7.436251       NaN  0.106774       NaN
                                     neighbor_average      7.738505       NaN  11.981518       NaN  0.198947       NaN
       greedy_a_trace                gls_map               3.392229       NaN   5.748424       NaN  0.085635       NaN
                                     gsp                   4.090688       NaN   6.898899       NaN  0.101011       NaN
                                     historical_tod_mean   4.192863       NaN   7.366677       NaN  0.106837       NaN
                                     neighbor_average      6.999872       NaN  10.989497       NaN  0.198890       NaN
       greedy_d_logdet               gls_map               3.995784       NaN   6.582279       NaN  0.099900       NaN
                                     gsp                   4.113867       NaN   7.098467       NaN  0.103351       NaN
                                     historical_tod_mean   4.273197       NaN   7.559900       NaN  0.110324       NaN
                                     neighbor_average      7.761705       NaN  12.464407       NaN  0.238732       NaN
       multistart_swap_by_validation gls_map               3.285058       NaN   5.549025       NaN  0.081439       NaN
                                     gsp                   3.958781       NaN   6.733419       NaN  0.097653       NaN
                                     historical_tod_mean   4.141810       NaN   7.290445       NaN  0.104421       NaN
                                     neighbor_average      7.031468       NaN  10.953243       NaN  0.190220       NaN
       random                        gls_map               3.531489  0.087146   6.043217  0.150082  0.088809  0.003157
                                     gsp                   4.012900  0.063588   6.858932  0.102506  0.100877  0.002520
                                     historical_tod_mean   4.170456  0.060901   7.393068  0.095953  0.106351  0.002283
                                     neighbor_average      7.270081  0.170350  11.326971  0.284338  0.189538  0.008373
       rcss_selected                 gls_map               3.398686       NaN   5.776535       NaN  0.087118       NaN
                                     gsp                   3.992831       NaN   6.833784       NaN  0.101329       NaN
                                     historical_tod_mean   4.156633       NaN   7.400700       NaN  0.106811       NaN
                                     neighbor_average      7.069130       NaN  10.613652       NaN  0.185933       NaN
       robust_coverage_cvar          gls_map               3.416538       NaN   5.905756       NaN  0.088240       NaN
                                     gsp                   3.983728       NaN   6.886051       NaN  0.102638       NaN
                                     historical_tod_mean   4.182980       NaN   7.413471       NaN  0.107657       NaN
                                     neighbor_average      7.016462       NaN  10.933599       NaN  0.189640       NaN
       scenario_average_a_trace      gls_map               3.431997       NaN   5.809499       NaN  0.088233       NaN
                                     gsp                   4.032506       NaN   6.891777       NaN  0.102657       NaN
                                     historical_tod_mean   4.148362       NaN   7.378680       NaN  0.107125       NaN
                                     neighbor_average      7.265030       NaN  11.214236       NaN  0.204570       NaN
       scenario_cvar_a_trace         gls_map               3.398686       NaN   5.776535       NaN  0.087118       NaN
                                     gsp                   3.992831       NaN   6.833784       NaN  0.101329       NaN
                                     historical_tod_mean   4.156633       NaN   7.400700       NaN  0.106811       NaN
                                     neighbor_average      7.069130       NaN  10.613652       NaN  0.185933       NaN
       swap_from_best_random_trace   gls_map               3.385670       NaN   5.657320       NaN  0.086088       NaN
                                     gsp                   4.026164       NaN   6.795108       NaN  0.100141       NaN
                                     historical_tod_mean   4.162951       NaN   7.299152       NaN  0.105800       NaN
                                     neighbor_average      6.947011       NaN  10.835537       NaN  0.193332       NaN
       swap_from_greedy_a_trace      gls_map               3.378227       NaN   5.719261       NaN  0.086418       NaN
                                     gsp                   4.040064       NaN   6.875489       NaN  0.101398       NaN
                                     historical_tod_mean   4.195516       NaN   7.361001       NaN  0.107224       NaN
                                     neighbor_average      7.082418       NaN  11.272623       NaN  0.204776       NaN
       swap_from_scenario_average    gls_map               3.405646       NaN   5.829879       NaN  0.088527       NaN
                                     gsp                   4.079668       NaN   6.960923       NaN  0.103465       NaN
                                     historical_tod_mean   4.222132       NaN   7.433906       NaN  0.109082       NaN
                                     neighbor_average      7.237910       NaN  11.542459       NaN  0.212782       NaN
       swap_from_scenario_cvar       gls_map               3.434456       NaN   5.864492       NaN  0.089574       NaN
                                     gsp                   4.093857       NaN   6.933083       NaN  0.102624       NaN
                                     historical_tod_mean   4.230789       NaN   7.423325       NaN  0.108219       NaN
                                     neighbor_average      7.151581       NaN  11.252676       NaN  0.203552       NaN
       top_variance                  gls_map               3.393100       NaN   5.947266       NaN  0.080323       NaN
                                     gsp                   3.670511       NaN   6.361354       NaN  0.086194       NaN
                                     historical_tod_mean   3.707253       NaN   6.698247       NaN  0.088881       NaN
                                     neighbor_average      9.567448       NaN  14.985342       NaN  0.180688       NaN
0.3    best_random_by_trace          gls_map               3.399620       NaN   5.780819       NaN  0.088074       NaN
                                     gsp                   4.038736       NaN   6.978565       NaN  0.105161       NaN
                                     historical_tod_mean   4.245542       NaN   7.553459       NaN  0.111495       NaN
                                     neighbor_average      6.989225       NaN  11.006963       NaN  0.202071       NaN
       best_random_by_validation     gls_map               3.148301       NaN   5.286449       NaN  0.074768       NaN
                                     gsp                   3.854012       NaN   6.562015       NaN  0.094001       NaN
                                     historical_tod_mean   3.988366       NaN   7.141179       NaN  0.099452       NaN
                                     neighbor_average      6.917493       NaN  10.685873       NaN  0.162080       NaN
       coverage                      gls_map               3.259044       NaN   5.695562       NaN  0.083979       NaN
                                     gsp                   3.924950       NaN   6.819475       NaN  0.099949       NaN
                                     historical_tod_mean   4.095408       NaN   7.417774       NaN  0.106548       NaN
                                     neighbor_average      6.983158       NaN  10.623019       NaN  0.183577       NaN
       degree                        gls_map               3.943622       NaN   6.569502       NaN  0.096813       NaN
                                     gsp                   4.139711       NaN   6.951354       NaN  0.100511       NaN
                                     historical_tod_mean   4.271779       NaN   7.470650       NaN  0.106880       NaN
                                     neighbor_average      8.162899       NaN  12.898153       NaN  0.227361       NaN
       greedy_a_trace                gls_map               3.244113       NaN   5.465965       NaN  0.084468       NaN
                                     gsp                   4.048497       NaN   6.891195       NaN  0.103051       NaN
                                     historical_tod_mean   4.209736       NaN   7.440507       NaN  0.109587       NaN
                                     neighbor_average      6.861848       NaN  10.764816       NaN  0.200491       NaN
       greedy_d_logdet               gls_map               3.731639       NaN   6.223316       NaN  0.099280       NaN
                                     gsp                   4.059033       NaN   7.000575       NaN  0.105018       NaN
                                     historical_tod_mean   4.215482       NaN   7.566991       NaN  0.111547       NaN
                                     neighbor_average      7.792356       NaN  12.343924       NaN  0.240728       NaN
       multistart_swap_by_validation gls_map               3.177996       NaN   5.295510       NaN  0.079317       NaN
                                     gsp                   3.971614       NaN   6.743058       NaN  0.099349       NaN
                                     historical_tod_mean   4.133948       NaN   7.313312       NaN  0.105868       NaN
                                     neighbor_average      7.016750       NaN  10.877751       NaN  0.189120       NaN
       random                        gls_map               3.354483  0.091843   5.768041  0.168778  0.083583  0.003387
                                     gsp                   3.992551  0.073992   6.823136  0.122222  0.100184  0.003095
                                     historical_tod_mean   4.161539  0.079171   7.390903  0.125208  0.106044  0.003088
                                     neighbor_average      7.137044  0.191832  11.162142  0.334483  0.183437  0.008481
       rcss_selected                 gls_map               3.177996       NaN   5.295510       NaN  0.079317       NaN
                                     gsp                   3.971614       NaN   6.743058       NaN  0.099349       NaN
                                     historical_tod_mean   4.133948       NaN   7.313312       NaN  0.105868       NaN
                                     neighbor_average      7.016750       NaN  10.877751       NaN  0.189120       NaN
       robust_coverage_cvar          gls_map               3.280269       NaN   5.701079       NaN  0.085566       NaN
                                     gsp                   3.984623       NaN   6.889396       NaN  0.103350       NaN
                                     historical_tod_mean   4.177409       NaN   7.456477       NaN  0.108425       NaN
                                     neighbor_average      6.899151       NaN  10.793083       NaN  0.190756       NaN
       scenario_average_a_trace      gls_map               3.283343       NaN   5.611340       NaN  0.086338       NaN
                                     gsp                   4.042364       NaN   6.940201       NaN  0.105443       NaN
                                     historical_tod_mean   4.175198       NaN   7.455039       NaN  0.110067       NaN
                                     neighbor_average      7.136411       NaN  11.048236       NaN  0.199773       NaN
       scenario_cvar_a_trace         gls_map               3.305550       NaN   5.690598       NaN  0.085684       NaN
                                     gsp                   4.089628       NaN   6.972485       NaN  0.105040       NaN
                                     historical_tod_mean   4.230711       NaN   7.523809       NaN  0.109655       NaN
                                     neighbor_average      6.944480       NaN  10.694867       NaN  0.189738       NaN
       swap_from_best_random_trace   gls_map               3.279287       NaN   5.530714       NaN  0.084507       NaN
                                     gsp                   3.982017       NaN   6.848395       NaN  0.100648       NaN
                                     historical_tod_mean   4.151204       NaN   7.405654       NaN  0.107831       NaN
                                     neighbor_average      6.935957       NaN  10.915055       NaN  0.199406       NaN
       swap_from_greedy_a_trace      gls_map               3.339167       NaN   5.557869       NaN  0.087194       NaN
                                     gsp                   3.996419       NaN   6.817692       NaN  0.102377       NaN
                                     historical_tod_mean   4.167773       NaN   7.379536       NaN  0.108644       NaN
                                     neighbor_average      6.904405       NaN  10.962234       NaN  0.201548       NaN
       swap_from_scenario_average    gls_map               3.291459       NaN   5.569972       NaN  0.087264       NaN
                                     gsp                   4.036100       NaN   6.882410       NaN  0.104092       NaN
                                     historical_tod_mean   4.200574       NaN   7.439627       NaN  0.109833       NaN
                                     neighbor_average      6.901426       NaN  10.825246       NaN  0.202670       NaN
       swap_from_scenario_cvar       gls_map               3.274348       NaN   5.477019       NaN  0.084961       NaN
                                     gsp                   4.044662       NaN   6.868742       NaN  0.102539       NaN
                                     historical_tod_mean   4.214388       NaN   7.446497       NaN  0.109379       NaN
                                     neighbor_average      6.974076       NaN  10.920760       NaN  0.201468       NaN
       top_variance                  gls_map               3.191580       NaN   5.670191       NaN  0.075966       NaN
                                     gsp                   3.523769       NaN   6.175850       NaN  0.083282       NaN
                                     historical_tod_mean   3.569160       NaN   6.459254       NaN  0.085273       NaN
                                     neighbor_average      8.928557       NaN  13.931098       NaN  0.172033       NaN
```

## Best method per budget-layout row

```
 budget                   layout_type  method      mae     rmse
    0.1   swap_from_best_random_trace gls_map 3.491656 5.921371
    0.2 multistart_swap_by_validation gls_map 3.285058 5.549025
    0.3                        random gls_map 3.141562 5.492614
```

## Certificate-error correlations

```
 method        certificate  pearson_mae  spearman_mae   n
    gsp    posterior_trace     0.211420      0.208988 648
    gsp   condition_number     0.214504      0.219406 648
    gsp information_logdet    -0.228631     -0.245914 648
gls_map    posterior_trace     0.882685      0.875206 648
gls_map   condition_number     0.839850      0.877012 648
gls_map information_logdet    -0.849052     -0.837900 648
```

## Output files

- metrics.csv
- metrics.json
- layouts.json
- swap_history.json
- rcss_candidates.csv
- certificate_correlations.csv