---
status: complete
completed: 2026-05-18
---

# TRACE-SL CPU Pilot Stage 3 Summary

第三阶段将 GLS posterior A-trace greedy 扩展为 swap local search，检验简单局部搜索是否能超过 random 与 greedy baselines。

## 代码更新

- 更新 `TRC-23-02333/transparent_estimator_eval.py`
  - 新增 `--include-swap`。
  - 新增 `--swap-max-iter`。
  - 新增 posterior trace swap local search。
  - 新增 `swap_from_greedy_a_trace` baseline。
  - 新增 `swap_from_best_random_trace` baseline。
  - 新增 `swap_history.json` 保存每次 swap 的 remove/add 和 posterior trace。

## 实验设置

- Dataset: PeMS7_228
- Test days: 2012-06-04, 2012-06-28
- Budgets: 10%, 20%, 30%
- Random layouts: 200 per budget
- Greedy baselines: A-trace, D-logdet
- Swap max iterations: 20
- Output directory: `TRC-23-02333/trace_sl_results/pems7_228_stage3_swap/`

## GLS/MAP MAE 对比

| Budget | Random mean | Best random | Greedy A-trace | Swap from greedy | Swap from best-random-trace |
|---:|---:|---:|---:|---:|---:|
| 10% | 3.6824 | 3.4704 | 3.5244 | 3.5133 | **3.4466** |
| 20% | 3.4358 | **3.2367** | 3.2984 | 3.2749 | 3.2846 |
| 30% | 3.2778 | **2.9818** | 3.1856 | 3.2220 | 3.1901 |

## 结论

- Swap local search 在 10% budget 上超过 best random，并且优于 greedy A-trace。
- 20% budget 上 swap 改善 greedy A-trace，但仍未超过 best random。
- 30% budget 上 swap 降低 posterior trace，却没有改善 empirical hidden MAE，说明 certificate 与 MAE 虽强相关，但不是逐布局单调等价。
- D-logdet 仍然不适合作为主布局目标。
- 当前最稳主线：GLS/MAP + A-trace certificate + random/multistart local search，而不是立刻引入 RL。

## Certificate 信号

GLS/MAP certificate 与 hidden MAE 仍强相关：

- posterior_trace: Pearson 0.8761, Spearman 0.8656
- condition_number: Pearson 0.8376, Spearman 0.8634
- information_logdet: Pearson -0.8342, Spearman -0.8163

GSP certificate 继续无效，GSP 不应作为当前主优化目标。

## 验证

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py` 通过。
- sanity stage3 run 通过。
- full stage3 run 通过。

## 下一步

1. 加入 topology / simple empirical baselines：degree、k-medoids、top variance、coverage。
2. 做 multistart swap：从 top-K random by empirical validation 或 by certificate 启动，而不是只选一个 best-random-by-trace。
3. 增加 validation/test split：layout 只用 validation/certificate 选择，test 只做最终评价，避免 best random 看 test 的问题。
4. 扩展到 Seattle，检验 TRACE-SL 的跨网络稳定性。
