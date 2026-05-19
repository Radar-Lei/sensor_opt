---
status: complete
completed: 2026-05-18
---

# TRACE-SL CPU Pilot Quick Summary

实现并运行了 TRACE-SL 首轮 CPU-only non-DL pilot。

## 代码产物

- `TRC-23-02333/transparent_estimator_eval.py`
  - 独立加载 PeMS7_228。
  - 支持 historical time-of-day mean、neighbor average、GSP、GLS/MAP。
  - 支持 budget sweep、随机 layout seeds、certificate 计算。
  - 输出 `metrics.csv`、`metrics.json`、`certificate_correlations.csv`、`config.json`、`SUMMARY.md`。

## 实验产物

- 主结果目录：`TRC-23-02333/trace_sl_results/pems7_228_cpu_pilot/`
- sanity 目录：`TRC-23-02333/trace_sl_results/sanity/`

## 首轮结果

PeMS7_228，test days: 2012-06-04 与 2012-06-28，budgets 10% / 20% / 30%，每个 budget 20 个随机 layouts。

| Budget | Historical MAE | Neighbor MAE | GSP MAE | GLS/MAP MAE |
|---:|---:|---:|---:|---:|
| 10% | 3.8921 | 7.5767 | 3.9202 | **3.6844** |
| 20% | 3.9093 | 7.3801 | 3.9389 | **3.4382** |
| 30% | 3.8761 | 7.2157 | 3.9100 | **3.2213** |

GLS/MAP 相比 historical time-of-day mean 的 MAE 改善约为：10% budget 5.3%，20% budget 12.0%，30% budget 16.9%。相比 neighbor average 的改善约为 51%–55%。

## Certificate 信号

GLS/MAP certificates 与 hidden MAE 有强相关：

- posterior_trace: Pearson 0.902, Spearman 0.889
- condition_number: Pearson 0.874, Spearman 0.886
- information_logdet: Pearson -0.889, Spearman -0.832

GSP certificates 当前基本无相关，说明首轮更应围绕 GLS/MAP posterior design 推进。

## 验证

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py` 通过。
- sanity run 通过。
- full pilot run 通过。

## 下一步

1. 基于 GLS/MAP posterior_trace / logdet 实现 A-optimal / D-optimal layout baseline。
2. 将 random layout 数量从 20 扩到 200，巩固 certificate-error 相关性。
3. 对比 greedy marginal posterior reduction、degree/betweenness/k-medoids/top variance baselines。
4. 暂缓 RL，直到 OR baseline 明确成立且存在求解时间或迁移需求。
