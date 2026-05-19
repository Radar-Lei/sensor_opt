---
status: complete
completed: 2026-05-18
---

# TRACE-SL CPU Pilot Stage 4 Summary

第四阶段把前一轮的 test-set 观察推进为更可信的 validation/test 流程，并补齐简单布局基线与 multistart swap。

## 代码更新

- 更新 `TRC-23-02333/transparent_estimator_eval.py`
  - `load_pems7_228` 现在返回 train/validation/test 三段数据。
  - 新增 `--include-simple-baselines`。
  - 新增 `--multistart-count`。
  - 新增 `--selection-method`，默认用 `gls_map` validation MAE 选择布局。
  - 新增 `best_random_by_validation`，只用 validation 选随机候选。
  - 新增 `best_random_by_trace`，保留 certificate-only random baseline。
  - 新增 `degree`、`coverage`、`top_variance` 三个简单布局基线。
  - 新增 `multistart_swap_by_validation`，从 validation 表现最好的 top-K random layouts 出发做 posterior-trace swap，再用 validation 选最终布局。
  - 输出中保存 `validation_selected_mae`，用于区分 layout selection 与 test evaluation。

## 实验设置

- Dataset: PeMS7_228
- Validation days: 2012-06-01, 2012-06-05
- Test days: 2012-06-04, 2012-06-28
- Budgets: 10%, 20%, 30%
- Random layouts: 200 per budget
- Multistart count: 10
- Selection method: GLS/MAP validation MAE
- Output directory: `TRC-23-02333/trace_sl_results/pems7_228_stage4_validation_multistart/`

## GLS/MAP test MAE 对比

| Budget | Random mean | Best random by validation | Greedy A-trace | Greedy D-logdet | Top variance | Coverage | Multistart swap by validation | Best test result |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 10% | 3.6824 | 3.6894 | 3.5244 | 4.5647 | 3.5927 | 3.7385 | **3.4185** | multistart swap |
| 20% | 3.4358 | **3.2448** | 3.2984 | 4.0628 | 3.3914 | 3.4682 | 3.2880 | best random by validation |
| 30% | 3.2778 | **2.9818** | 3.1856 | 3.6684 | 3.1874 | 3.2272 | 3.0781 | best random by validation |

## 主要结论

1. validation-selected random 是当前最强且最干净的 baseline：20% 和 30% budget 都显著优于 random mean、greedy A-trace 和 simple topology baselines。
2. multistart swap 在 10% budget 最强，且 30% budget 也明显优于 greedy A-trace；20% budget 接近但略弱于 best_random_by_validation。
3. greedy D-logdet 继续系统性较差，不适合作为主优化目标，应保留为 negative baseline。
4. top-variance 在 20%/30% budget 接近 greedy A-trace，说明强经验基线必须进入论文，否则 OR 方法的增益会被质疑。
5. GLS/MAP certificate 仍强相关：posterior_trace Pearson 0.8645 / Spearman 0.8578；GSP certificate 仍基本无效。

## 当前推荐主线

论文方法不应表述为“RL 主导”。更稳的主线是：

> TRACE-SL uses a transparent GLS/MAP reconstruction model and separates layout search from final evaluation through validation-selected randomized search and local posterior-trace improvement.

可作为主方法的候选：

- Primary: `best_random_by_validation`，简单、无 test leakage、20%/30% 最强。
- Enhancement: `multistart_swap_by_validation`，10% 最强，30% 次强，可作为 local-search refinement。
- Certificate story: posterior trace 是可靠 surrogate，但不能保证逐布局单调最优，因此需要 validation selection。

## 验证

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py` 通过。
- Stage 4 sanity run 通过。
- Full Stage 4 run 通过。

## 下一步

1. 把 Stage 4 跑成 multi-split seeds，至少 5 个 split seeds，报告 mean/std。
2. 加 Seattle 或 Chengdu/SUMO 小网络，检验跨网络稳定性。
3. 为论文准备 Figure 1：transparent pipeline；Figure 2：certificate-vs-error scatter；Table 1：layout baselines。
4. 如果继续做 RL，只应作为 amortized optimizer/warm start，不作为当前核心贡献。
