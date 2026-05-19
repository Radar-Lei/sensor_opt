# Experiment Plan

**项目**: TRACE-SL  
**日期**: 2026-05-04  
**目标**: 验证非黑箱 full-network state estimation 下，OR/RL sensor layout 是否能提升全网状态重构质量并提供可解释部署证据。  
**Supersedes**: `refine-logs/EXPERIMENT_PLAN_20260504_122115.md`

## Claim Matrix

| Claim | Evidence | Required? |
|---|---|---|
| C1: Transparent estimators can reconstruct full-network state from sparse sensors | GSP/GLS/Kalman hidden MAE/RMSE vs baselines | 必须 |
| C2: OR layout improves reconstruction vs random/topology-only | Budget sweep and paired tests | 必须 |
| C3: Certificates explain layout quality | correlation between trace/logdet/coherence/condition and hidden error | 必须 |
| C4: RL is useful only if it amortizes search | solve time/quality across budgets/networks | 条件必须 |
| C5: Regime-aware layouts reveal TS insight | free-flow vs congestion layouts and budget marginal value | 强烈建议 |

## Datasets

1. PeMS7_228: first non-DL pilot。
2. Seattle: external validation and spatial heterogeneity。
3. PeMS7_1026: scaling after estimator harness is stable。
4. CDSTE results: optional upper-bound comparison only, not main method。

## Estimator Baselines

- Historical time-of-day mean。
- kNN / spatial interpolation。
- Linear interpolation / neighbor average from existing `Average.py` idea。
- Graph signal reconstruction。
- Flow-constrained GLS/MAP。
- Kalman filter / RTS smoother。
- Compressed sensing / LASSO sparse basis。

## Layout Baselines

- Random, 20 seeds。
- Degree / betweenness / closeness。
- k-medoids on coordinates/distance。
- Top variance / top flow。
- Coverage/facility-location MIP。
- A-optimal / D-optimal posterior design。
- Coherence minimization。
- Greedy marginal uncertainty reduction。
- Local search / swap。
- RL add/swap policy only after OR baselines are strong。

## Experimental Blocks

### Block A: Non-DL Estimator Harness

Goal: 不做 sensor optimization，先确认透明 estimator 能从 sparse observations 重构全网。

Runs:

1. PeMS7_228, random 20% sensors, compare historical mean / kNN / GSP / GLS。
2. Seattle, random 20% sensors, same estimators。
3. If dynamic model feasible, add Kalman/RTS smoother。

Decision gate: 至少一个透明 estimator 明显优于 historical mean 和 neighbor average。

### Block B: Certificate Validation

Goal: 证明 uncertainty/certificate 能预测 hidden reconstruction error。

Runs:

1. Sample 200 random layouts per budget。
2. Compute trace/logdet/condition/coherence/smoothing energy。
3. Compute hidden MAE/RMSE。
4. Report Spearman/Pearson correlation and calibration plots。

Decision gate: 至少一个 certificate 与 error 有稳定 monotonic relation。

### Block C: OR Layout Optimization

Goal: 用 AMPL/OR models 选择 sensor layout。

Runs:

1. A-optimal and D-optimal design for GLS/Kalman posterior。
2. Coverage/correlation/facility-location MIP。
3. Coherence minimization for CS estimator。
4. Greedy and local search baselines。

Decision gate: OR layout beats random/topology-only across budgets。

### Block D: RL Search Amortization

Goal: 判断 RL 是否真的需要。

Runs:

1. Use exact/greedy/local-search trajectories as behavior cloning data。
2. Train add/swap policy using certificate reduction reward。
3. Evaluate cross-budget and cross-dataset warm start。

Decision gate: RL must reduce solve time or improve large-scale layout quality. If not, remove RL from main paper and keep it as negative result/appendix。

### Block E: TS-Oriented Insight

Outputs:

- Budget marginal value curves。
- Free-flow vs congestion regime-specific layouts。
- Which links/nodes are consistently selected and why。
- Tradeoff between reconstruction error and observability/uncertainty。
- Sensor failure robustness。

## First Three Runs

1. Implement `transparent_estimator_eval.py` for GSP and GLS on PeMS7_228。
2. Generate 200 random layouts at budgets 10%, 20%, 30%; compute certificates and hidden MAE。
3. Build first AMPL A-optimal / D-optimal layout model and compare against random/topology baselines。

## Pilot Budget

无需 GPU。首轮应在 CPU 上完成：

- PeMS7_228 only。
- Budgets: 10%, 20%, 30%。
- Estimators: historical mean, neighbor average, GSP, GLS。
- Time horizon: selected days or all test days depending runtime。

## Stop / Pivot Criteria

- 如果透明 estimator 不能超过简单 neighbor average，先改 estimator，不做 RL。
- 如果 certificates 与 hidden error 无关，改 objective 或只做 empirical greedy。
- 如果 OR layouts 不超过 random/topology，布局问题定义不成立，需要回到观测协议和状态变量定义。
- 如果 RL 不优于 local search/warm start，主文改为 OR-only transparent sensor layout。

