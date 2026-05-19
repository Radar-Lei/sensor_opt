---
status: complete
completed: 2026-05-18
---

# TRACE-SL CPU Pilot Stage 2 Summary

第二阶段将 TRACE-SL pilot 从随机布局评估推进到 GLS posterior OR baseline。

## 代码更新

- 更新 `TRC-23-02333/transparent_estimator_eval.py`
  - 新增 `--include-greedy`。
  - 新增 `greedy_a_trace`：基于 GLS posterior trace reduction 的 greedy A-optimal layout。
  - 新增 `greedy_d_logdet`：基于 GLS information logdet gain 的 greedy D-optimal layout。
  - 新增 `layout_type` 字段区分 random / greedy baselines。
  - 新增 `layouts.json` 保存每个 layout 的 sensor set。

## 实验设置

- Dataset: PeMS7_228
- Test days: 2012-06-04, 2012-06-28
- Budgets: 10%, 20%, 30%
- Random layouts: 200 per budget
- OR baselines: greedy A-trace and greedy D-logdet, one layout per budget
- Output directory: `TRC-23-02333/trace_sl_results/pems7_228_stage2_or/`

## 关键结果：GLS/MAP MAE

| Budget | Random mean | Greedy A-trace | Greedy D-logdet |
|---:|---:|---:|---:|
| 10% | 3.6824 | **3.5244** | 4.5647 |
| 20% | 3.4358 | **3.2984** | 4.0628 |
| 30% | 3.2778 | **3.1856** | 3.6684 |

Greedy A-trace 相对 random mean 改善：

- 10% budget: 4.3%
- 20% budget: 4.0%
- 30% budget: 2.8%

但 200 个 random layouts 中存在更好的个体：

| Budget | Best random GLS/MAP MAE |
|---:|---:|
| 10% | 3.4704 |
| 20% | 3.2367 |
| 30% | 2.9818 |

解释：A-trace certificate 是有效方向，但单步 greedy 还不是最优布局搜索器；下一步应做 multi-start swap/local search 或 stochastic greedy，而不是立刻上 RL。

## Certificate 信号

在 606 个 layout-method rows 上，GLS/MAP certificate 与 hidden MAE 仍然强相关：

- posterior_trace: Pearson 0.8755, Spearman 0.8640
- condition_number: Pearson 0.8374, Spearman 0.8634
- information_logdet: Pearson -0.8347, Spearman -0.8140

GSP certificate 仍基本无信号，说明当前主线应围绕 GLS/MAP posterior design。

## 验证

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py` 通过。
- sanity stage2 run 通过。
- full stage2 run 通过。

## 下一步

1. 实现基于 A-trace 的 swap local search：以 greedy A-trace 和 top random layouts 为 warm start。
2. 加入 topology baselines：degree / k-medoids / top variance。
3. 将结果扩到 Seattle 或 PeMS7_1026，验证 certificate 是否跨数据集稳定。
4. 在 local search 明确遇到规模/时间瓶颈前，不启动 RL。
