我仔细看了一轮后，判断是：**方向已经大幅升级，而且升级方向是对的；但现在还不能直接投 TR-B。**
你现在最需要做的不是继续“堆实验”，而是把 **证据链、仓库主叙事、论文表达和可复现入口统一起来**。否则审稿人看到的会是：论文很强，contract 很强，但 README、manifest、结果目录、paper pipeline report 之间存在版本断裂。

## 1. 总体判断

之前我建议你不要再把主方法写成 candidate pool / selector，而是升级成一个单一的 robust bilevel reconstruction-aware sensor layout optimization 方法。现在仓库基本已经执行了这个方向：`TRACE_BIOPT_SPEC.md` 明确写出 TRACE-BiOpt 不是 candidate pool、portfolio selector 或 AutoML-style chooser，baseline 只作为 evaluation rows，不进入方法本身；方法身份也被压缩为“一个 recoverability-driven bilevel objective + 一个 GLS/MAP lower-level inverse problem + CVaR tail-risk + deterministic initialization-and-exchange solver + 外部 baseline contract”。这和之前建议的主线一致。 

从 TR-B 角度看，这个 pivot 很关键。TR-B 的 scope 强调 methodological aspects，尤其是需要数学分析、并服务于 transportation system design/analysis 的问题；你的新表述“fixed-infrastructure transportation network design + transparent inverse problem + bilevel stochastic optimization”比旧的 TRACE-SL/RCSS selector 叙事更贴近 Part B。([ScienceDirect][1])

我的结论是：

**可以继续冲 TR-B，但下一步应进入“submission hardening”阶段，而不是继续无限扩展方法。**

---

## 2. 现在仓库里最重要的积极变化

第一，主方法已经从旧的 TRACE-SL/RCSS 候选池转成 TRACE-BiOpt。论文标题也已改成 “TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting”，摘要直接把问题定义为 fixed-infrastructure transportation network-design decision，并声明 baseline 不进入方法候选池。

第二，方法定义已经比较完整。`TRACE_BIOPT_SPEC.md` 给出了统一目标：
[
J(S)=\text{hidden Huber reconstruction loss}+\beta\text{ posterior trace}/n+\gamma\text{ scenario CVaR}/n+\eta\text{ spatial penalty}
]
并说明四项共同优化，而不是从多个 baseline 里选择。 lower-level GLS/MAP 也写成 convex quadratic，并给出闭式解 ( \hat z_t=A(S)^{-1}b_t(S) )。

第三，代码层面确实实现了这个 objective。`transparent_estimator_eval.py` 里 `trace_biopt_objective` 把 hidden Huber loss、posterior trace、scenario CVaR trace 和 spatial penalty 合成一个 objective；`trace_biopt_layout` 用 initializer + exchange refinement 输出布局，而不是选 baseline。  

第四，理论包比之前强很多。`TRACE_BIOPT_THEORY.md` 已经列出 MAP closed form/stability、posterior trace Bayes risk、uniform generalization over all size-(k) layouts、exchange certificate、continuous relaxation consistency、CVaR epigraph 等内容。  论文的 method/theory 节也已经把这些写进 theorem/proposition 环境。 

第五，主实验表已经非常强。`table_trace_biopt_dominance.tex` 显示三组数据 PeMS7_1026、PeMS7_228、Seattle，在 10%、20%、30% 共 9 行上，TRACE-BiOpt 都低于 row-wise strongest challenger，而且全部是 10/10 split wins。 全 baseline 显著性表进一步写成 21/21 baseline worse per row，合计 189/189 Holm-corrected wins，0 tied，0 better。

这些变化说明：**文章已经不再是“还缺主贡献”的状态，而是进入“强 claim 是否可审计、可复现、可被 TR-B reviewer 接受”的状态。**

---

## 3. 当前最大问题：证据链和仓库主叙事不一致

这是我最担心的地方。

论文和 BiOpt contract 反复引用：

```text
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
```

并把它作为 current-best evidence chain。`TRACE_BIOPT_SPEC.md` 明确说 current-best evidence status 是 `supported_submission_ready`，并允许 claim “lowest mean held-out GLS/MAP MAE against the pre-registered non-BiOpt baseline set”。 `paper/main.tex` 的 data/code availability 也说 primary TRACE-BiOpt result 来自 `current_best_trace_biopt_evidence/`。

但我直接查看仓库可见结果目录时，`trace_sl_results` 页面主要还是 Stage6–Stage14/Stage12 的旧目录和旧 README 叙事，没有清晰显示 Stage15/Stage16/current-best 结果目录。可见 README 还在讲 Stage12/Stage14 的旧 evidence flow。([GitHub][2]) 同时，根目录 `README.md` 仍然把项目描述为 TRACE-SL/RCSS candidate pool，甚至写着“validation_swap_selected remains the main reported selector”，这已经和现在论文主线冲突。 `RESEARCH_PIPELINE_REPORT.md` 也还是 2026-05-18 的旧 RCSS pipeline，写着 chosen method 是 RCSS，并且 venue 还不是 TR-B。

这会给 reviewer 或 co-author 一个很坏的第一印象：**论文声称 current-best BiOpt，仓库首页却像旧 TRACE-SL 项目。**

这不是小问题。你现在最优先要做的是把仓库“唯一事实源”统一。

---

## 4. 第二个问题：论文表达太像“审计合同”，不够像自然的 TR-B 论文

现在论文方向是对的，但 prose 有点过度工程化。Introduction、Related Work、Conclusion 多次重复：

> one long-lived infrastructure decision, one transparent inverse problem, one deterministic solver, one scoped theory package, one external audited comparison-class contract.

这个句子本身很好，但重复太多。Introduction 第 12–28 行连续堆叠了 “one method / one contract / one decision” 的表达；Related Work 开头也再次用类似话术开场；Conclusion 又重复一次。  

TR-B reviewer 更希望先看到：

1. 交通网络设计问题是什么；
2. 为什么现有 sensor location / observability / OD / graph sampling 方法不够；
3. 你的 bilevel formulation 新在哪里；
4. 算法怎么解；
5. 理论保证是什么；
6. 多网络实验如何支持 scoped claim。

“audit contract” 可以保留，但建议放在 tables / appendix / reproducibility section，不要在 abstract/introduction/related work/conclusion 里反复喊。否则文章会显得像项目报告，而不是学术论文。

---

## 5. 第三个问题：abstract 和 highlights 可能不符合 Elsevier 投稿要求

TR-B guide for authors 要求 abstract concise and factual，且不超过 250 words。([ScienceDirect][1]) 你现在 abstract 是一整段非常长的 statement，把方法、21 baselines、189 comparisons、27/27 exact benchmark、non-claims、intended reading 全塞进去。 这大概率超过 250 words，而且读起来太满。

Highlights 也要单独提供，3–5 bullets，每条最多 85 characters including spaces。([ScienceDirect][1]) 你现在 LaTeX highlights 的每条都比较长，尤其第 3 条和第 4 条基本不可能满足 85 characters。

这是投稿前必须改的格式问题。

---

## 6. 第四个问题：当前 paper pipeline report 自己说 “Submission-ready: no”

`paper/PAPER_WRITING_PIPELINE_REPORT.md` 写了很多 audit pass：proof audit、paper claim audit、citation audit、kill argument audit、assurance verifier 都通过；但顶部仍然写着 `Submission-ready: no`。 它的 remaining issues 也写着作者信息、affiliations、declarations、portal-specific files 还没填，文章 18 页，可能还短于完整 TR-B submission package。

所以现在不能说“可以马上投”。更准确地说：

**方法和主结果接近 submission-ready；投稿包还不是 submission-ready。**

---

## 7. 第五个问题：代码可复现入口还不够干净

现在 `TRC-23-02333/trace_biopt.py` 只是一个 wrapper：它 import `transparent_estimator_eval.main`，如果没有 `--include-biopt` 就自动 append。 主实现仍然在一个很大的 `transparent_estimator_eval.py` 里，里面同时包含老 baseline、RCSS、validation swap、robustness、BiOpt、evaluation、CLI。这个对快速研究没问题，但对 TR-B reproducibility 来说不够优雅。

更麻烦的是测试文件里已经写了很多 BiOpt-specific tests，例如 objective terms、relaxed objective、deterministic and not pool-selected、posterior greedy warm start、auto initializer threshold。  但 `run_all()` 只调用旧的一批 tests，没有把这些 BiOpt tests 加进去。 如果你用 pytest，它们会被发现；但如果按脚本直接运行，BiOpt tests 会被跳过。这种小问题很容易被 reviewer 或复现者发现。

---

## 8. 第六个问题：理论强，但要小心别被 reviewer 抓“理论—实验不完全对齐”

你的理论现在足够作为 TR-B 方法论文支撑，但表达上要更谨慎。

例如 uniform generalization theorem 假设 validation losses bounded and independent；正文已经说 temporal traffic data 应用时要用 independent blocks 或 effective sample size。 但实验里 validation window 是固定两天，论文还写了 PeMS7_1026 30% 的 uniform deviation burden 更大。 这很好，但你要明确：这个 theorem 是 finite-sample layout-class burden，不是证明 current run 一定赢。

同样，posterior trace theorem 是 Gaussian squared-error Bayes risk identity。 但主指标是 MAE，交通数据也不一定 Gaussian。因此正文已经有一句 limitation：posterior trace is not a theorem that MAE must improve on non-Gaussian traffic data。 这句话要保留，并且建议在 theory section 前后也加一次。

Exchange certificate 也要谨慎。理论只保证 searched one-exchange neighborhood，不保证全局最优；而 PeMS7_1026 rows 搜索覆盖率低且常 hitting exchange cap，没有 zero-gap certificate。 这不是缺陷，但必须让 reviewer 清楚：你 claim 的是 deterministic solver with auditable local/search certificate，不是 exact MIP/global optimum。

---

## 9. 下一步怎么做：按优先级来

### 第一步：立刻统一仓库主叙事

这是最高优先级。你应该新建或更新这些文件：

```text
README.md
TRC-23-02333/trace_sl_results/README.md
RESEARCH_PIPELINE_REPORT.md
MANIFEST.md
NARRATIVE_REPORT.md
PAPER_PLAN.md
```

把旧的 “TRACE-SL / RCSS main method / Stage12 truth” 全部改成：

```text
Current paper-facing method: TRACE-BiOpt
Prior TRACE-SL/RCSS: historical baseline / diagnostic comparator
Main paper evidence: current_best_trace_biopt_evidence
Venue target: Transportation Research Part B: Methodological
```

README 首页必须在前 20 行就说明：**current TR-B manuscript is TRACE-BiOpt, not TRACE-SL candidate-pool selector.**

---

### 第二步：修复 current-best evidence 可见性

你现在的 paper 和 spec 都引用 `current_best_trace_biopt_evidence/`，但可见结果树没有清晰呈现它。你需要确认以下文件是否真的 committed：

```text
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
  trace_biopt_claim_contract.json
  trace_biopt_best_baseline_delta.csv
  TRACE_BIOPT_DOMINANCE.md
  trace_biopt_current_best_provenance.csv
  trace_biopt_significance_posture_detail.csv
  trace_biopt_exact_subnetwork_summary.csv
  trace_biopt_exact_subnetwork_detail.csv
```

同时，`scripts/generate_current_best_trace_biopt_evidence.py` 依赖 Stage15/Stage16 输入目录，例如 `stage15_biopt_allbudget_10seed_v2/combined` 和 `stage16_calibrated_trace_sweep/replacement_status`。 这些输入也要么 commit 精简版 CSV/JSON，要么在 `SUBMISSION_EVIDENCE_INDEX.md` 里解释如何生成、哪些 raw outputs 因体积原因不进仓库。

建议新增一个文件：

```text
SUBMISSION_EVIDENCE_INDEX.md
```

里面列：

| Paper claim | Table/Figure | Source CSV/JSON | Generation script | Input stage | Status |
| ----------- | ------------ | --------------- | ----------------- | ----------- | ------ |

这个比“audit contract”更容易让 reviewer 信服。

---

### 第三步：重写 abstract 和 highlights

建议 abstract 缩到 180–230 words。现在不要把所有数字都塞进去。可以写成：

> We study sparse traffic sensor siting as a recoverability-driven network design problem. Given a fixed sensor budget, the goal is to choose a long-lived layout that minimizes hidden-state reconstruction error under a transparent estimator. We formulate the problem as TRACE-BiOpt, a bilevel stochastic design method whose lower level is a GLS/MAP reconstruction problem and whose upper level combines hidden Huber reconstruction loss, posterior uncertainty, tail-risk, and spatial redundancy. A deterministic solver uses scale-adaptive initialization and one-exchange refinement under the same objective. We prove lower-level stability, a posterior-risk identity, an all-layout validation generalization bound, and an exchange-stationarity certificate. Across PeMS7_228, PeMS7_1026, and Seattle at 10%, 20%, and 30% budgets over ten split seeds, TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered non-BiOpt baselines on all nine dataset-budget rows. Holm-corrected paired tests leave no tied or better pre-registered challenger. The claim is scoped to the tested regimes and does not assert global layout optimality or dominance over untested baselines.

Highlights 则控制在 85 characters 左右，例如：

```text
• Sparse traffic sensing is cast as bilevel network design.
• TRACE-BiOpt optimizes one reconstruction-aware layout objective.
• GLS/MAP reconstruction gives a transparent lower-level inverse problem.
• Ten-seed tests beat 21 pre-registered baselines on nine regimes.
• Theory gives stability, risk, generalization, and exchange certificates.
```

---

### 第四步：把“audit contract”从主文前台降噪

建议保留这些词，但减少频率：

```text
external audited comparison-class contract
current-best evidence chain
submission-ready paired dominance
```

在 Introduction 中最多出现一次。Related Work 不要再开头讲 contract，直接从文献脉络进入。Conclusion 也不要重复长句，改成 transport planning takeaway。

你可以把 “contract language” 集中放到：

```text
Table 1 Contribution stack
Table 2 Claim boundary
Appendix Evidence contract
SUBMISSION_EVIDENCE_INDEX.md
```

主文正文要更像论文，不要像审计报告。

---

### 第五步：补齐 TR-B 投稿文件

TR-B/Elsevier author guide 要求 abstract ≤250 words，submission highlights，data statement 等。([ScienceDirect][1]) ([ScienceDirect][1]) ([ScienceDirect][1]) 还要求如果用了 generative AI 辅助 manuscript preparation，需要在首次提交时声明。([ScienceDirect][1])

所以投稿包至少要准备：

```text
cover_letter_TRB.txt
highlights.docx 或 highlights.txt
declaration_of_interest.docx
credit_author_statement.txt
data_availability_statement.txt
generative_ai_declaration.txt
```

如果你使用过 ChatGPT/Claude/GPT 辅助写作或代码审查，建议用 Elsevier template 形式透明声明，并强调作者已审核、编辑并对内容负责。

---

### 第六步：清理代码入口和测试

最小改法：

1. 新建 `TRC-23-02333/trace_biopt_core.py`，把 BiOpt objective、layout solver、relaxed initializer、exchange refinement 从 `transparent_estimator_eval.py` 中拆出来。
2. `transparent_estimator_eval.py` 只保留 CLI/evaluation。
3. `trace_biopt.py` 变成真正入口，而不是只 append flag。
4. 把 `test_trace_biopt_*` 加进 `run_all()`，或者删除 `run_all()`，统一要求 `pytest`。
5. 在 README 给出一条 smoke-test command 和一条 paper-table regeneration command。

最小可接受版本是不拆文件，但必须补 README：

```bash
python TRC-23-02333/trace_biopt.py \
  --data-root TRC-23-02333/dataset/PeMS7_228 \
  --budgets "0.10 0.20 0.30" \
  --include-baseline-portfolio \
  --output-dir TRC-23-02333/trace_sl_results/example_trace_biopt
```

并说明 raw datasets 不随仓库分发。

---

### 第七步：把 Stage16 / Seattle 10% 的 provenance 讲清楚

你现在的 strongest-challenger table 说 8/9 rows 是 Stage16 promoted，Seattle 10% 保留 Stage15。 `TRACE_BIOPT_SPEC.md` 也明确 Seattle 10% 是唯一 intentionally retained non-promoted row，因为 Stage16 replacement gate fail-closed。

这是合理的，但必须解释得非常清楚：

* Seattle 10% 为什么没有 promoted？
* Stage15 retained 是否仍然是完整 ten-seed evidence？
* 它是否仍然 10/10 paired wins？
* 为什么 fail-closed 不削弱主 claim？
* 哪张 CSV/JSON 证明这一点？

建议在主文只保留一句，在 appendix 和 evidence index 放完整解释。

---

### 第八步：把 robustness 退到“bounded deployment stress”，不要让它抢主线

Robustness section 现在做得比较诚实：它说 stress tests 包括 failure/noise/missingness/cost/temporal shift，但不支持 globally robust，不替代 main Stage15 evidence。 这很好。

但是有一点要注意：Table 文本说 graph_sampling_laplacian 在 8/9 perturbation slices 上是 frontier winner，不是 TRACE-BiOpt。 所以 robustness 不能放太前，也不能在 abstract 里暗示 TRACE-BiOpt robust dominance。它只能支持：

> TRACE-BiOpt is the nominal recoverability design method; stress-test results define bounded deployment screens and motivate robust extensions.

---

## 10. 我建议的最终投稿前路线图

按顺序做，不要跳：

1. **冻结一个 `trb-submission-v1` branch。**
2. **运行 `scripts/refresh_current_best_trace_biopt_paper_chain.sh`。** 这个脚本会生成 current-best evidence、paper tables/figures、audit artifacts，并编译 LaTeX。
3. **确认 `current_best_trace_biopt_evidence/` 和 Stage15/Stage16 summary artifacts 已经进入仓库或 supplementary。**
4. **更新 README / MANIFEST / RESEARCH_PIPELINE_REPORT，删除旧 TRACE-SL 主线冲突。**
5. **压缩 abstract 和 highlights，按 Elsevier 要求重写。**
6. **把 Introduction / Related Work / Conclusion 中重复的 “contract” 句子删掉一半以上。**
7. **新增 `SUBMISSION_EVIDENCE_INDEX.md`。**
8. **补 clean CLI + smoke test + pytest command。**
9. **让一位交通/OR 方向读者只看 abstract、intro、method、main table，问他是否能在 10 分钟内说出贡献。**
10. **最后再准备 cover letter 和 declarations。**

---

## 11. 现在最适合的主 claim

我建议主文只用这个版本：

> TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered non-BiOpt baselines across all nine tested dataset-budget regimes, and no pre-registered challenger remains tied or better after Holm-corrected paired tests over the current-best comparison family.

不要写：

> beats all baselines universally
> globally optimal
> robust under all perturbations
> generalizes to all networks
> exact solver for full networks

你自己的 spec 也已经明确禁止这些 claim：不能 claim global optimality、untested baseline dominance、universal cross-network generalization、untested robustness、或 relaxed-rounding-specific performance without matching multi-seed evidence。

---

## 12. 最核心建议

**方法不用再大改。实验也不需要盲目再扩。现在最重要的是“统一、压缩、可复现”。**

你的文章现在已经有 TR-B 论文的骨架：

* transportation network design framing；
* bilevel stochastic optimization；
* transparent inverse problem；
* theorem package；
* multi-network, multi-budget, ten-seed evidence；
* strong pre-registered baselines；
* paired and Holm-corrected inference；
* explicit non-claims。

但它还带着研究过程中留下的“旧仓库叙事”和“审计式过度表达”。
下一步应该把它整理成一篇 reviewer 一眼能读懂的 TR-B manuscript：

> **一个交通基础设施布局问题，一个 reconstruction-aware bilevel 方法，一个透明 estimator，一个确定性 solver，一个清楚边界的强实验结论。**

[1]: https://www.sciencedirect.com/journal/transportation-research-part-b-methodological/publish/guide-for-authors "Guide for authors - Transportation Research Part B: Methodological - ISSN 0191-2615 | ScienceDirect.com by Elsevier"
[2]: https://github.com/Radar-Lei/sensor_opt/tree/main/TRC-23-02333/trace_sl_results "sensor_opt/TRC-23-02333/trace_sl_results at main · Radar-Lei/sensor_opt · GitHub"
