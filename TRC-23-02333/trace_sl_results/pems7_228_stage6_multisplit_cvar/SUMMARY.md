---
status: complete
completed: 2026-05-18
---

# TRACE-SL Stage 6 Multi-Split Scenario-CVaR Summary

Goal: test whether `scenario_cvar_a_trace` and its posterior-trace swap refinement are stable across multiple validation/test splits, rather than relying on one split.

## Setup

- Dataset: PeMS7_228
- Split seeds: 20, 21, 22, 23, 24
- Budgets: 10%, 20%, 30%
- Random layouts: 200 per budget per split
- Scenario-CVaR parameters: scenario_count=8, cvar_tail_fraction=0.25
- Estimator used for selection comparison: GLS/MAP
- Compared layouts: random mean, best random by validation, greedy A-trace, scenario average A-trace, scenario CVaR A-trace, swap from scenario CVaR, multistart validation swap, and simple baselines.

## Mean GLS/MAP test MAE across splits

```
 budget                   layout_type   mean    std  count
    0.1          best_random_by_trace 3.4631 0.0767      5
    0.1     best_random_by_validation 3.4976 0.1251      5
    0.1                      coverage 3.7152 0.1284      5
    0.1                greedy_a_trace 3.4407 0.1056      5
    0.1 multistart_swap_by_validation 3.3731 0.0991      5
    0.1                        random 3.6039 0.1184   1000
    0.1      scenario_average_a_trace 3.5122 0.1123      5
    0.1         scenario_cvar_a_trace 3.4591 0.0850      5
    0.1       swap_from_scenario_cvar 3.3725 0.0421      5
    0.1                  top_variance 3.4930 0.0980      5
    0.2          best_random_by_trace 3.4420 0.1284      5
    0.2     best_random_by_validation 3.2303 0.0942      5
    0.2                      coverage 3.4328 0.1121      5
    0.2                greedy_a_trace 3.2373 0.0784      5
    0.2 multistart_swap_by_validation 3.2151 0.0903      5
    0.2                        random 3.3827 0.1101   1000
    0.2      scenario_average_a_trace 3.2988 0.1269      5
    0.2         scenario_cvar_a_trace 3.2579 0.0831      5
    0.2       swap_from_scenario_cvar 3.2568 0.0819      5
    0.2                  top_variance 3.2298 0.1412      5
    0.3          best_random_by_trace 3.3335 0.0873      5
    0.3     best_random_by_validation 3.0356 0.0479      5
    0.3                      coverage 3.2106 0.0573      5
    0.3                greedy_a_trace 3.1315 0.0800      5
    0.3 multistart_swap_by_validation 3.0563 0.0523      5
    0.3                        random 3.2419 0.1121   1000
    0.3      scenario_average_a_trace 3.1542 0.0667      5
    0.3         scenario_cvar_a_trace 3.0970 0.0752      5
    0.3       swap_from_scenario_cvar 3.1175 0.1082      5
    0.3                  top_variance 3.0534 0.1252      5
```

## Per-budget winner counts

```
 budget                   best_layout  wins
    0.1 multistart_swap_by_validation     2
    0.1       swap_from_scenario_cvar     3
    0.2     best_random_by_validation     2
    0.2         scenario_cvar_a_trace     1
    0.2                  top_variance     2
    0.3     best_random_by_validation     2
    0.3 multistart_swap_by_validation     1
    0.3       swap_from_scenario_cvar     1
    0.3                  top_variance     1
```

## Scenario-CVaR deltas, negative is better

```
 budget  cvar_minus_random_mean  cvar_minus_best_val_random  cvar_minus_greedy_a  swap_cvar_minus_random_mean  swap_cvar_minus_best_val_random  swap_cvar_minus_greedy_a
    0.1                 -0.1448                     -0.0385               0.0184                      -0.2315                          -0.1251                   -0.0683
    0.2                 -0.1248                      0.0275               0.0206                      -0.1259                           0.0265                    0.0195
    0.3                 -0.1449                      0.0615              -0.0344                      -0.1245                           0.0819                   -0.0140
```

## Certificate stability

```
 method        certificate pearson_mae                              spearman_mae
                                  mean      std       min       max         mean      std       min       max
gls_map   condition_number    0.820830 0.008316  0.810515  0.829938     0.851263 0.009318  0.843258  0.861913
gls_map information_logdet   -0.802581 0.021475 -0.824277 -0.771324    -0.804372 0.007534 -0.815625 -0.795786
gls_map    posterior_trace    0.844199 0.017119  0.819646  0.865568     0.852450 0.006571  0.845321  0.860531
```

## Interpretation

- `scenario_cvar_a_trace` is consistently a principled candidate generator, but its average advantage is budget-dependent rather than uniformly dominant.
- Mean `scenario_cvar_a_trace - random` MAE deltas by budget: 0.1: -0.1448, 0.2: -0.1248, 0.3: -0.1449.
- Mean `swap_from_scenario_cvar - random` MAE deltas by budget: 0.1: -0.2315, 0.2: -0.1259, 0.3: -0.1245.
- Against `best_random_by_validation`, raw CVaR deltas are: 0.1: -0.0385, 0.2: 0.0275, 0.3: 0.0615; swap-CVaR deltas are: 0.1: -0.1251, 0.2: 0.0265, 0.3: 0.0819.
- This means the method should not be claimed as a universal test-MAE winner yet. The stronger claim is that CVaR optimal design gives an interpretable, robust OR candidate whose quality is competitive and whose uncertainty certificate is stable.
- The methodology contribution still needs either a stronger calibrated robust-search rule or another OR baseline/failure-robust variant before paper-level claims.

## Output files

- combined_metrics.csv
- gls_map_layout_summary.csv
- gls_map_per_split_comparison.csv
- gls_map_win_counts.csv
- gls_map_delta_summary.csv
- combined_certificate_correlations.csv
- certificate_correlation_summary.csv