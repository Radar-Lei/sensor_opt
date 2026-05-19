---
status: complete
completed: 2026-05-18
---

# TRACE-SL CPU Pilot Stage 5 OR-Guided Summary

第五阶段根据 Obsidian 中的 OR 文献线索，优先尝试更强的 OR-guided layout 方法：多场景 A-trace greedy 与 robust/CVaR A-trace greedy，并与 validation-selected random、posterior-trace swap、simple baselines 同场比较。

## 文献动机

- `Li et al. 2023 Submodularity of optimal sensor placement for traffic networks`：交通传感器选址在 rank / trace covariance / coverage 等目标下可形成次模或近似次模结构，支持 greedy/lazy greedy 的 OR 叙事。
- `Zhou and List 2010 Information-Theoretic Sensor Location Model`：用 Kalman/GLS posterior covariance 的 trace/determinant 指标做 sensor information gain。
- `Zhu et al. 2018 DRO reliable information gain`：强调可靠性/最坏场景信息增益，启发 robust/CVaR objective。

## 代码更新

- 更新 `TRC-23-02333/transparent_estimator_eval.py`
  - 新增 `build_scenario_matrices`：从训练日构造多个 Ledoit-Wolf covariance / precision scenarios。
  - 新增 `scenario_greedy_layout`：支持 `average_trace` 与 `cvar_trace` 两类多场景 A-trace greedy。
  - 新增参数：
    - `--include-scenario-greedy`
    - `--scenario-count`
    - `--cvar-tail-fraction`
  - 新增布局类型：
    - `scenario_average_a_trace`
    - `scenario_cvar_a_trace`
    - `swap_from_scenario_average`
    - `swap_from_scenario_cvar`

## 实验设置

- Dataset: PeMS7_228
- Validation days: 2012-06-01, 2012-06-05
- Test days: 2012-06-04, 2012-06-28
- Budgets: 10%, 20%, 30%
- Random layouts: 200 per budget
- Scenario count: 8 training-day covariance scenarios
- CVaR tail fraction: 0.25
- Selection method: GLS/MAP validation MAE
- Output directory: `TRC-23-02333/trace_sl_results/pems7_228_stage5_or_guided/`

## GLS/MAP test MAE 对比

| Budget | Random mean | Best random by validation | Greedy A | Scenario avg A | Scenario CVaR A | Swap from scenario CVaR | Multistart swap by validation | Best |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 10% | 3.6824 | 3.6894 | 3.5244 | 3.5795 | 3.5366 | **3.4011** | 3.4185 | swap from scenario CVaR |
| 20% | 3.4358 | **3.2448** | 3.2984 | 3.4125 | 3.3534 | 3.3125 | 3.2880 | best random by validation |
| 30% | 3.2778 | **2.9818** | 3.1856 | 3.1691 | 3.0709 | 3.2001 | 3.0781 | best random by validation |

## 主要发现

1. **Robust/CVaR A-trace 有真实信号**：
   - 30% budget 下 `scenario_cvar_a_trace` = 3.0709，明显优于 greedy A = 3.1856、random mean = 3.2778、top variance = 3.1874。
   - 10% budget 下 `swap_from_scenario_cvar` = 3.4011，是当前最优。
2. **Scenario average A-trace 不如 CVaR**：平均场景目标在 20% 表现偏弱，说明“鲁棒坏场景”比“平均 covariance”更适合当前数据。
3. **OR-guided 还未完全打败强随机选择**：20%/30% 的 `best_random_by_validation` 仍是最强 test MAE。
4. **greedy D-logdet 继续失败**：10%/20%/30% 分别为 4.5647 / 4.0628 / 3.6684，仍应作为 negative baseline。
5. **GLS/MAP certificate 稳定有效**：posterior_trace 与 MAE 的 Pearson 0.8656、Spearman 0.8605；GSP certificate 仍基本无效。

## 对 methodology contribution 的影响

现在可以更清楚地说：

- OR-guided 并非只体现在事后 certificate，而是已体现在 `scenario_cvar_a_trace` 的 robust optimal-design objective 和 posterior-trace swap refinement 中。
- 但当前单 split 结果还不能声称 OR-guided 方法全面优于 validation-selected random。
- 更稳的论文表述应是：TRACE-SL 是一个 transparent, validation-calibrated OR search framework；其中 robust/CVaR A-trace 是 principled candidate generator，validation-selected random 是强 baseline 与 calibration module。

## 推荐下一步

1. **先跑 multi-split seeds**：当前最关键问题不是继续加新方法，而是验证 `scenario_cvar_a_trace` / `swap_from_scenario_cvar` 在多个 split 上是否稳定优于 greedy A 和 random mean。
2. **把 CVaR greedy 做成 validation-calibrated variant**：在多个 `scenario_count` / `tail_fraction` / swap-start 上用 validation 选配置，而不是固定 8 和 0.25。
3. **再做 small-network exact/MIP benchmark**：如果 multi-split 支撑 OR-guided 方法，再用小网络 exact result 强化 OR anchor。

## 验证

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py` 通过。
- Stage 5 OR sanity run 通过。
- Full Stage 5 OR-guided run 通过。
