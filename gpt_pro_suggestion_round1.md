根据 2026-05-28 的仓库文档、论文源码和 current-best evidence，我的判断是：**研究核心已经够冲 Transportation Research Part B，但投稿包还需要一次“删表、同步、降噪、封口”的 submission hardening。** 我没有重新跑原始实验；下面判断基于仓库里已经提交的 evidence/artifact、论文源码和官方期刊要求。

## 1. 总体判断

**可以冲 TR-B。** 现在的 TRACE-BiOpt 叙事已经从旧的 TRACE-SL/RCSS candidate-pool selector 转成了一个单一的 recoverability-driven bilevel transportation network design 方法。README 现在明确写了：当前稿件方法是 TRACE-BiOpt，不是 candidate-pool selector 或 AutoML-style portfolio chooser；旧 TRACE-SL/RCSS 只是 historical baseline / diagnostic comparator。 这一点非常关键，因为 TR-B 官方 scope 强调 methodological aspects，特别是需要数学分析、服务于 transportation system design/analysis 的问题；其覆盖范围也包括 transportation networks 的 design/analysis、optimization、statistical/econometric/mathematical models。([ScienceDirect][1])

**强 claim 基本能站住，但必须严格限定。** current-best evidence 已经支持：3 个网络、3 个预算、10 个 split seed、21 个 pre-registered non-BiOpt baselines；9/9 dataset-budget rows 上 TRACE-BiOpt 都低于 row-wise strongest challenger，而且每行都是 10/10 paired wins。 all-baseline significance posture 进一步显示 189/189 Holm-corrected comparisons 中，21/21 baselines 在每个 row 都显著 worse，aggregate 行也是 189/189、0 non-worse、0 better。

**但还不建议直接 submit。** 不是因为方法不够，而是因为论文和仓库还有几处“版本同步”和“表格过载”问题。现在最容易被 reviewer 抓的不是实验结果，而是：某些 section 还残留旧 Stage15/Stage16 叙事，paper pipeline report 和 research pipeline report 对 submission-ready 状态不一致，`trace_biopt.py` 的文档定位和实际代码入口不完全一致，以及正文/附录/仓库之间的 audit tables 太多。

## 2. 附录大量表格有没有必要？

**有一部分必要，但现在数量过多，尤其不应该都进入 manuscript。**

现在 `paper/tables/` 里有大量 TRACE-BiOpt 表，从 dominance、significance、full baseline matrix，到 comparison ladder、reader guide、method contract、problem contract、planning takeaways、weight sensitivity、tail-risk posture、solver-scale 等等，目录本身已经非常像一个 audit artifact library。([GitHub][2]) Elsevier guide 明确建议 tables 要 sparingly 使用，避免重复正文已经描述的结果。([ScienceDirect][1]) 所以问题不是“附录有表格就不好”，而是**这些表格承担的角色没有分层**。

我建议分成三层：

**主文只保留 4–6 个真正 reviewer-facing 的表/图。**
最核心应是：dominance table、all-baseline significance posture、theory summary 或 theory bridge、一个机制/solver diagnostic 汇总、一个 bounded robustness routing。Introduction 现在同时引入 contribution stack、reader guide、dominance table，Related Work 又很早放 comparison class contract，这会让文章前几页像审计报告而不是论文。 

**附录保留“防 reviewer 质疑”的表。**
这些是必要的：full baseline matrix、baseline registry、current-best provenance、claim boundary matrix、exact subnetwork benchmark、exchange certificate、solver scale、weight sensitivity。当前 appendix 已经包含 claim boundary、provenance、baseline registry、full baseline matrix，这个方向是对的。 full baseline matrix 尤其应该保留，因为它能证明 main dominance table 不是挑了一个方便 comparator，而是整个 22-method matrix 中 TRACE-BiOpt rank 1。

**仓库/补充材料放 audit-contract 表。**
例如 reader guide、comparison ladder、method contract、problem contract、planning takeaways、discussion boundary、tail-risk posture、posterior-risk posture、layout-consensus posture 等，更适合作为 reproducibility/evidence index，而不是全放论文主体。仓库已经有 `SUBMISSION_EVIDENCE_INDEX.md`，它的定位就是把 paper claim 映射到 artifact、script、input stage 和 status。 这类东西留在 repo/supplement 比塞进正文更好。

一句话：**附录表格不是没必要；必要的是 evidence tables，不必要的是把每个 audit posture 都变成论文表格。**

## 3. TR-B 够不够？

**研究贡献够。写作形态还需要更像 TR-B 论文。**

现在的方法定义已经对了。TRACE-BiOpt spec 写得很清楚：它不是 candidate pool、portfolio selector 或 AutoML chooser；random、top variance、degree、coverage、graph sampling、QR/POD、greedy A-trace、D-logdet、RCSS、validation-swap TRACE-SL 都只是 evaluation rows，不进入 solver。 目标函数也已经是统一的：
[
J(S)=\text{hidden Huber reconstruction loss}
+\beta\text{ posterior trace}
+\gamma\text{ scenario CVaR}
+\eta\text{ spatial penalty}.
]
spec 明确说明四项共同优化，不是 coverage-only、observability-only 或 posterior-certificate-only criterion。 lower-level GLS/MAP reconstruction 也有闭式解 (A(S)^{-1}b_t(S))，并且和 theory、dominance tables、current-best evidence chain 使用同一个 estimator。

理论包也足够支撑 TR-B 方法论文：MAP closed form/stability、posterior trace Bayes risk、uniform generalization over all size-(k) layouts、exchange certificate、continuous relaxation consistency、CVaR epigraph。  这比旧的“candidate pool + validation selector”更像 Part B 会接受的 methodological contribution。

但文章语气还要再调整。现在很多地方反复说 “external audited comparison-class contract / one auditable design argument / claim contract”。这些话本身是对的，但过多会让 reviewer 感觉你在“证明自己不是作弊”，而不是自然地展开一个交通网络设计方法。Related Work 和 Introduction 应该更多讲 transportation sensor location、observability、network design、inverse problem、bilevel optimization，少讲 contract 语言。

## 4. 强 claim 能不能站住？

**能，但只能用 scoped claim。**

我建议主 claim 精确写成：

> Across PeMS7_228, PeMS7_1026, and Seattle at 10%, 20%, and 30% sensor budgets, under the stated ten-seed GLS/MAP protocol, TRACE-BiOpt achieves the lowest mean held-out hidden-state MAE against 21 pre-registered non-BiOpt baselines; Holm-corrected one-sided paired tests over the 189 row-baseline comparisons leave no statistically tied or significantly better pre-registered challenger.

这个 claim 和仓库 contract 一致。spec 允许说：TRACE-BiOpt 是 recoverability-driven bilevel transportation network-design method；它在 current-best contract 记录的 tested regimes 上，对 pre-registered non-BiOpt registry achieves lowest mean held-out GLS/MAP MAE；Holm correction 后没有 tied 或 better challenger。

不能写这些：

> beats all baselines
> globally optimal
> robust under all perturbations
> generalizes to all networks
> proves MAE improvement theoretically
> exact solver on full networks

这些都已经在 spec 里明确列为 forbidden upgrades：不能 claim global optimality、untested baseline dominance、universal cross-network generalization、untested robustness、或没有 matching multi-seed evidence 的 relaxed-rounding performance claim。

理论也要保持这个边界。uniform generalization theorem 是 bounded independent validation samples 下的 layout-class bound，traffic time series 要解释成 independent blocks 或 effective sample size。 exchange certificate 只保证 searched one-exchange neighborhood；如果 active sets 是 strict subsets 或 exchange cap exhausted，就不能说 full local optimum，更不能说 global optimum。 posterior trace 是 Gaussian squared-error Bayes-risk certificate，不是非 Gaussian traffic MAE 一定下降的 theorem；discussion 已经正确写了这个 caveat。

## 5. 当前必须修的几个具体问题

第一，**Section 6 里有一个明显过时句子。** 当前 evidence index 和 dominance table 都说 PeMS7_228 的 10/20/30 rows 已经 Stage16 promoted。 dominance table note 也说 PeMS7_1026 全部、PeMS7_228 全部、Seattle 20/30 都来自 complete replaceable Stage16 reruns。 但 `6_ablation_robustness.tex` 末尾仍写着 “only PeMS7_228 20/30 still awaits…”。这必须删掉或改成 current-best 状态，否则 reviewer 会怀疑证据链没冻结。

第二，**pipeline report 之间状态冲突。** `RESEARCH_PIPELINE_REPORT.md` 写 current method TRACE-BiOpt、target TR-B、pipeline stage “evidence complete, manuscript compiled, submission-ready”，aggregate status `supported_submission_ready`。 但 `paper/PAPER_WRITING_PIPELINE_REPORT.md` 仍写 “Submission-ready: no”，日期是 2026-05-27，remaining issues 还包括 author metadata、affiliations、declarations、portal-specific files、manuscript only 18 pages 等。  这不是科学问题，但投稿前必须同步：要么刷新 paper report，要么标记旧 report superseded。

第三，**`trace_biopt.py` 的定位需要修正。** README 说 `trace_biopt.py` 是 TRACE-BiOpt solver implementation。 但文件本身写得很清楚：它只是 thin wrapper，调用 `transparent_estimator_eval.main()` 并自动 append `--include-biopt`。 这不致命，因为 wrapper 可以用；但 reproducibility 叙事应改成“CLI wrapper”，或者把 BiOpt core 函数拆成 `trace_biopt_core.py`。

第四，**robustness 不能抢主 claim。** 当前 robustness section 处理得比较诚实：它说 stress tests 不支持 globally robust，也不替代 main evidence。 更重要的是 stress frontier 里 `graph_sampling_laplacian` 赢了 8/9 perturbation slices，而不是 TRACE-BiOpt。 所以 robustness 最多作为 bounded deployment-stress discussion，不能在 abstract 或 conclusion 暗示 TRACE-BiOpt robust dominance。

第五，**current evidence index 的 metadata 也要检查。** 它写 aggregate evidence status 是 `supported_submission_ready`，但 “Last refreshed” 是 2025-05-28。 如果这是笔误，应改成 2026-05-28；如果不是笔误，需要解释。这个小地方很容易让人觉得 artifact 不是最新的。

## 6. 我对“附录表格”的具体裁剪建议

我会这样重排：

| 位置      | 保留内容                                                                                                                                                | 理由                                                   |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| 主文      | workflow figure、dominance table、significance posture、theory summary、1 个 mechanism/solver diagnostic、1 个 bounded robustness routing                  | reviewer 第一遍读完就能明白方法、证据、边界                           |
| 附录      | full baseline matrix、baseline registry、current-best provenance、claim boundary、exact subnetwork、exchange certificate、solver scale、weight sensitivity | 防止 cherry-picking、解释 Stage15/Stage16、支撑 scoped claim |
| 仓库/补充材料 | reader guide、comparison ladder、method/problem contract、planning takeaways、posterior/tail/spatial posture、所有 probe/detail CSV                        | 这些是审计材料，不应打断论文叙事                                     |

特别是 full baseline matrix 要留。它的 caption 已经把作用说清楚：TRACE-BiOpt ranks first on every dataset-budget row，因此 best-baseline table 不是 selective comparison。 但 comparison ladder、reader guide、contribution stack、problem contract、method contract 这类表，如果全部在主文，会显得过度自证。

## 7. 下一步应该怎么做

我建议不要继续盲目加实验。下一步按这个顺序做：

1. **做一次全文/全仓库同步清理。** 搜索并修掉这些词附近的旧句子：`awaits`, `Stage15 main evidence`, `directional`, `PeMS7_228 20/30`, `Submission-ready: no`, `TRACE-SL main method`, `candidate pool`. 最优先修 Section 6 的 PeMS7_228 20/30 旧句子。

2. **重排表格。** 主文删掉一半以上的 contract/audit tables，把 full matrix 和 provenance 放 appendix，把大多数 posture/contract/detail 表移到 supplement 或 `SUBMISSION_EVIDENCE_INDEX.md`。这样更符合 Elsevier 对表格 sparingly 使用的要求。([ScienceDirect][1])

3. **把 paper report 刷新成唯一状态。** `RESEARCH_PIPELINE_REPORT.md` 和 `paper/PAPER_WRITING_PIPELINE_REPORT.md` 不能一个说 submission-ready，一个说 no。保留一个 authoritative report，另一个标记 superseded。

4. **固定 claim language。** 全文统一只说 “21 pre-registered non-BiOpt baselines / tested dataset-budget regimes / held-out GLS/MAP MAE / Holm-corrected one-sided paired tests”。不要写 “all baselines” 除非前面加 tested/pre-registered/non-BiOpt。

5. **整理 reproducibility 入口。** README 已经给了 data placement、smoke test、refresh command；这很好。  但 `trace_biopt.py` 是 wrapper 这件事要说明清楚，或者拆出 core module。测试方面已经比之前好，`run_all()` 现在包含 TRACE-BiOpt objective、relaxed objective、deterministic layout、relaxed rounding、posterior warm start、auto initializer tests。

6. **补齐投稿文件。** 当前 abstract/highlights 看起来已经接近 Elsevier 要求：official guide 要求 abstract concise/factual 且不超过 250 words，highlights 3–5 bullets、每条最多 85 characters。([ScienceDirect][1]) 但 submission package 还需要 author metadata、affiliations、declarations、portal-specific files；paper pipeline report 也列了这些 remaining issues。 如果使用了生成式 AI 辅助写作，Elsevier 还要求 submission 时声明，并说明作者审核和负责。([ScienceDirect][1])

## 8. 最终判断

我的结论很明确：

**研究主线已经够 TR-B。** TRACE-BiOpt 现在是一个真正的 transportation network design / bilevel stochastic optimization / transparent inverse problem 论文，不再是 candidate-pool selector。理论包和实验包都比之前扎实很多。

**强 claim 可以站住，但必须 scoped。** 现在 evidence 支持的是 tested regimes + pre-registered non-BiOpt baseline registry + held-out GLS/MAP MAE + Holm-corrected paired tests；不支持 universal dominance、global optimality 或 robust-everywhere。

**附录表格不是没必要，而是要分层。** full baseline matrix、provenance、baseline registry、claim boundary、exact benchmark、exchange certificate 是必要防线；大量 audit/contract/posture tables 应该移到 supplement/repo，不要全部进入论文主叙事。

**下一步不是再发明方法，而是投稿硬化。** 修版本冲突，删冗余表，统一 claim wording，清理 code/reproducibility 入口，更新 submission reports，然后让一个交通/OR 方向读者只看 abstract、intro、method、main result table 和 limitations，确认 10 分钟内能说清楚贡献。现在最大的风险不是“结果不强”，而是“强结果被过度审计化表达和残留旧叙事稀释”。

[1]: https://www.sciencedirect.com/journal/transportation-research-part-b-methodological/publish/guide-for-authors "Guide for authors - Transportation Research Part B: Methodological - ISSN 0191-2615 | ScienceDirect.com by Elsevier"
[2]: https://github.com/Radar-Lei/sensor_opt/tree/main/paper/tables "sensor_opt/paper/tables at main · Radar-Lei/sensor_opt · GitHub"
