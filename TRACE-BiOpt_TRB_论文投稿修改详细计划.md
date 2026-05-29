# TRACE-BiOpt / TR-B 投稿前论文修改详细计划

**文件用途**：这是一份可直接作为 GitHub issue、project checklist、co-author handoff、或投稿前硬化清单使用的 Markdown 修改计划。  
**当前判断**：研究主线与核心 evidence 已经具备冲击 *Transportation Research Part B: Methodological* 的基础；投稿前重点不是重新发明方法，而是完成 **submission hardening**：删表、降噪、同步、封口、补材料、跑最终验收。  
**当前日期基准**：2026-05-29。  
**适用仓库**：`Radar-Lei/sensor_opt`。  
**主方法名称**：TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting。  
**核心原则**：一个方法、一个目标、一个透明 lower-level estimator、一个确定性 solver、一套严格 scoped evidence claim。

---

## 0. 一句话总任务

把当前论文从“研究过程痕迹很完整的 evidence-heavy draft”整理成“TR-B reviewer 第一遍就能读懂、claim 清楚、理论边界清楚、表格分层清楚、复现入口清楚、投稿材料齐全”的正式投稿包。

投稿前不建议继续盲目加新实验。优先级是：

1. **清理论文表达**：减少 audit/contract/posture 语言，强化交通网络设计叙事。
2. **压缩表格层级**：主文只保留 reviewer-facing 核心图表，appendix 放防质疑表，repo/supplement 放 audit artifacts。
3. **统一 claim language**：所有强结论都限定在 tested regimes + 21 pre-registered non-BiOpt baselines + held-out GLS/MAP MAE + Holm-corrected paired tests。
4. **修补 theory-to-evidence 边界**：理论支撑 formulation 和 algorithm，不证明 universal empirical dominance。
5. **封闭 reproducibility chain**：README、evidence index、pipeline report、paper tables、source CSV/JSON、refresh command 必须一致。
6. **补齐 Elsevier/TR-B 投稿文件**：author metadata、affiliations、declarations、highlights、cover letter、AI declaration、data statement 等。

---

## 1. 当前状态判断与修改目标

### 1.1 当前强项

当前仓库已经完成了几个关键升级：

- README 已经将当前 paper-facing 方法改为 TRACE-BiOpt，并明确它不是 candidate-pool selector 或 AutoML-style chooser。
- `TRACE_BIOPT_SPEC.md` 已经把方法定义为：
  - 一个 recoverability-driven bilevel objective；
  - 一个 transparent GLS/MAP lower-level inverse problem；
  - 一个 CVaR tail-risk epigraph；
  - 一个 deterministic initialization-and-exchange solver；
  - 21 个 pre-registered non-BiOpt baselines 只作为 evaluation rows。
- current-best evidence 已经支持：
  - 三个网络：PeMS7_228、PeMS7_1026、Seattle；
  - 三个预算：10%、20%、30%；
  - 十个 split seeds；
  - 21 个 pre-registered non-BiOpt baselines；
  - 9/9 dataset-budget rows 上 TRACE-BiOpt mean MAE 最低；
  - 189/189 Holm-corrected paired comparisons 中没有 tied 或 better challenger。
- theory package 已经具备 TR-B 方法论文所需的基本厚度：
  - MAP closed form and stability；
  - posterior trace as Bayes squared reconstruction risk；
  - all-layout validation generalization；
  - exchange certificate；
  - continuous relaxation consistency；
  - CVaR epigraph interpretation。

### 1.2 当前最大剩余风险

这些风险不是“方法不够强”，而是“投稿形态还需要压实”：

| 风险 | 具体表现 | 投稿影响 | 优先级 |
|---|---|---:|---:|
| 表达过度审计化 | `audit / contract / posture / intended reading` 语言偏多 | reviewer 觉得文章像内部审计报告，不像自然学术论文 | P0 |
| 表格过载 | 主文、appendix、repo 表格边界不清 | 读者被 evidence artifacts 淹没，主贡献反而变弱 | P0 |
| 引用 moved-to-supplement 表格 | Section 6 中多处注释“moved to supplementary”，但正文仍 `Table~\ref{...}` | 可能出现 undefined refs，或读者找不到表 | P0 |
| claim 容易过界 | “beats all baselines / robust / deployable / global” 等词容易被误读 | 审稿人会攻击过度声明 | P0 |
| 理论与实验指标不完全对齐 | posterior trace 是 Gaussian squared-error risk，主指标是 MAE | 需要显式 boundary，否则会被抓 | P0 |
| `trace_biopt.py` 定位仍有不一致 | README 说 wrapper，某些 report 还称 solver implementation | 复现入口叙事不干净 | P1 |
| 投稿材料未齐 | author metadata、affiliations、declarations、AI declaration、cover letter | portal-ready 不完整 | P0 |
| robustness 容易抢主线 | stress tests 中 frontier winner 不总是 TRACE-BiOpt | 不能暗示 universal robustness | P0 |

### 1.3 修改完成后的目标状态

最终应达到以下状态：

- 读者在 **Abstract + Introduction + Method + Main Results + Limitations** 中即可理解：
  - 问题：sparse traffic sensing 是 recoverability-driven transportation network design。
  - 方法：TRACE-BiOpt 是单一 bilevel reconstruction-aware sensor layout optimization 方法。
  - 理论：透明 MAP/GLS lower level + posterior risk + all-layout generalization + exchange certificate。
  - 结果：在当前 tested regimes 下，对 21 个 pre-registered non-BiOpt baselines 实现 lowest held-out GLS/MAP MAE，并通过 Holm-corrected paired tests。
  - 边界：不 claim global optimality、不 claim universal robustness、不 claim untested baseline dominance。
- 主文图表减少到真正支撑 narrative 的 4–6 个核心对象。
- Appendix 和 supplement 有明确分工。
- 所有 evidence artifact 可追溯到 CSV/JSON/source script。
- LaTeX 编译无 undefined references / stale labels / overclaim language。
- Elsevier portal 所需文件齐全。

---

## 2. 总体执行顺序

不要随机改。建议严格按下面顺序执行，因为前面的修改会影响后面的表格、引用和 claim wording。

### Phase A — 冻结事实源

- [ ] 建立或确认一个干净的投稿分支，例如 `trb-submission-v1`。
- [ ] 运行 current-best evidence refresh pipeline。
- [ ] 记录当前 commit hash。
- [ ] 确认 `SUBMISSION_EVIDENCE_INDEX.md` 是唯一 evidence entry point。
- [ ] 确认 current-best evidence 目录中所有核心 CSV/JSON/MD 都已进入 repo 或 supplement。

### Phase B — 先修 P0 语言与引用

- [ ] 全文替换过强 claim。
- [ ] 修所有 moved-to-supplement table refs。
- [ ] 把 robustness 降级成 bounded stress discussion。
- [ ] 把 Conclusion 里的 “deployable” 改成 scoped phrasing。
- [ ] 在 theory section 加 “What the theory does and does not imply”。

### Phase C — 重排主文、附录、supplement 表格

- [ ] 主文保留最少核心图表。
- [ ] Appendix 放防 reviewer 质疑的证据表。
- [ ] Supplement/repo 放 audit posture/detail 表。
- [ ] 所有表格在正文中都要被引用；所有被引用的表格都必须在 manuscript 或 supplement index 中能找到。

### Phase D — 清理仓库叙事和复现入口

- [ ] 修 `RESEARCH_PIPELINE_REPORT.md` 中 `trace_biopt.py` 的定位。
- [ ] 检查 `MANIFEST.md`、`NARRATIVE_REPORT.md`、`PAPER_PLAN.md` 与 current method 是否一致。
- [ ] 检查 `TRC-23-02333/trace_sl_results/README.md` 是否把 Stage12/TRACE-SL 明确标为 historical。
- [ ] 确认 smoke test、full refresh、LaTeX compile、pytest 命令可运行。

### Phase E — 准备投稿材料

- [ ] author metadata / affiliations。
- [ ] CRediT statement。
- [ ] declaration of competing interests。
- [ ] funding statement。
- [ ] data availability statement。
- [ ] generative AI declaration。
- [ ] separate highlights file。
- [ ] cover letter。
- [ ] clean manuscript PDF。
- [ ] source archive / supplementary files。

### Phase F — 最终验收

- [ ] 跑 LaTeX clean compile。
- [ ] 跑 test suite。
- [ ] 跑 claim/evidence audit。
- [ ] 跑 grep overclaim audit。
- [ ] 用 PDF 视觉检查表格、图、caption、appendix。
- [ ] 从 reviewer 视角做 10 分钟读稿 gate。

---

## 3. P0 必须修改项

这一节是投稿前必须处理的问题。

---

### P0-1. 统一主 claim，避免任何 universal claim

#### 允许使用的主 claim

全文统一使用下面这一句或其轻微变体：

> Across PeMS7_228, PeMS7_1026, and Seattle at 10%, 20%, and 30% sensor budgets, under the stated ten-seed GLS/MAP protocol, TRACE-BiOpt achieves the lowest mean held-out hidden-state MAE against 21 pre-registered non-BiOpt baselines; Holm-corrected one-sided paired tests over the 189 row-baseline comparisons leave no statistically tied or significantly better pre-registered challenger.

#### 中文理解

这句话的强度已经足够大，但边界非常清楚：

- 只针对三个 tested networks；
- 只针对 10/20/30% budgets；
- 只针对 stated ten-seed GLS/MAP protocol；
- 只针对 21 个 pre-registered non-BiOpt baselines；
- 只针对 held-out hidden-state MAE；
- 只针对 Holm-corrected paired test family；
- 不暗示 all possible baselines；
- 不暗示 global optimality；
- 不暗示 universal robustness；
- 不暗示所有未来 network 都会赢。

#### 禁止或慎用表达

| 不要写 | 替换为 |
|---|---|
| beats all baselines | beats all 21 pre-registered non-BiOpt baselines in the tested regimes |
| universally outperforms | outperforms under the stated ten-seed GLS/MAP protocol |
| global optimum | searched-neighborhood exchange certificate / deterministic solver output |
| robust under perturbations | bounded deployment-stress evidence / stress-test screening |
| deployable routes | supported current-best routes / promoted evidence routes |
| proves MAE improvement | supports / is consistent with / gives a squared-risk certificate |
| no challenger exists | no pre-registered challenger remains tied or better after Holm correction |
| all networks | PeMS7_228, PeMS7_1026, and Seattle |
| all budgets | 10%, 20%, and 30% tested budgets |
| exact solver | deterministic solver with exact lower-level MAP solve and exchange search |

#### 操作

全文搜索：

```bash
rg -n "all baselines|universally|global|globally|robust under|deployable|proves.*MAE|exact solver|all networks|all budgets|no challenger" paper
```

每个命中都必须判断是否过界。保留数学上正确的 `exact lower-level solve`，但不要把 full layout optimization 说成 exact global solve。

---

### P0-2. Abstract 控制在 250 words 以内，并进一步自然化

当前 abstract 已经基本合格，但仍要做两件事：

1. 实际数词数，保证 ≤250 words。
2. 避免把所有 audit boundary 全塞进 abstract，保持 concise and factual。

#### 建议 abstract 版本

```text
We study sparse traffic sensor siting as a recoverability-driven network design problem. Given a fixed sensor budget, the goal is to choose a long-lived layout that minimizes hidden-state reconstruction error under a transparent generalized-least-squares/maximum-a-posteriori estimator. We formulate TRACE-BiOpt, a bilevel stochastic design method whose lower level reconstructs the full traffic state and whose upper level combines hidden-state Huber reconstruction loss, posterior uncertainty, conditional-value-at-risk tail risk, and spatial redundancy regularization. A deterministic solver uses scale-adaptive initialization and one-exchange refinement under the same objective; pre-registered baselines are not used as method candidates. We prove lower-level stability, a posterior-risk identity, an all-layout validation generalization bound, and an exchange-stationarity certificate. Across PeMS7_228, PeMS7_1026, and Seattle at 10%, 20%, and 30% budgets over ten split seeds, TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered non-BiOpt baselines on all nine dataset-budget rows. Holm-corrected paired tests leave no statistically tied or better pre-registered challenger. The claims are scoped to the tested regimes and do not assert global layout optimality, universal robustness, or dominance over untested methods.
```

#### 操作

在本地运行：

```bash
python - <<'PY'
import re, pathlib
tex = pathlib.Path("paper/main.tex").read_text()
m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
txt = re.sub(r"\\[a-zA-Z]+\{[^}]*\}", "", m.group(1))
txt = re.sub(r"\\[%_&]", " ", txt)
words = re.findall(r"[A-Za-z0-9_/-]+", txt)
print(len(words))
PY
```

验收标准：

- [ ] abstract ≤250 words。
- [ ] 第一处出现 GLS/MAP 时有完整展开或清楚定义。
- [ ] 没有 “all baselines” 的无边界表达。
- [ ] 最后一两句明确 scope，不冗长。

---

### P0-3. Highlights 单独文件，3–5 条，每条 ≤85 characters

TR-B/Elsevier 要求 highlights 是单独 editable file，3–5 bullets，每条最多 85 characters including spaces。

#### 建议文件

新建：

```text
paper/highlights.txt
```

内容：

```text
• Sparse traffic sensing is cast as bilevel network design.
• TRACE-BiOpt optimizes one reconstruction-aware layout objective.
• GLS/MAP reconstruction gives a transparent lower-level inverse problem.
• Ten-seed tests beat 21 pre-registered baselines on nine regimes.
• Theory gives stability, risk, generalization, and exchange certificates.
```

#### 字符数检查

运行：

```bash
python - <<'PY'
from pathlib import Path
for line in Path("paper/highlights.txt").read_text().splitlines():
    line=line.strip()
    if line:
        print(len(line), line)
PY
```

验收标准：

- [ ] 3–5 条。
- [ ] 每条 ≤85 characters including spaces。
- [ ] 文件名含 `highlights`。
- [ ] 不写过界 claim。
- [ ] 不出现 unsupported robustness/global optimality wording。

---

### P0-4. Introduction 降噪，减少 audit/contract 语言

当前 Introduction 的主线是对的，但第 6–12 行附近有较多 “intended reading / auditable design argument / comparison-class contract” 式语言。应保留一次边界声明，但不要让它成为 introduction 的主叙事。

#### Introduction 目标结构

Introduction 建议按以下 6 段组织：

1. 交通机构的 sparse sensor siting 是 fixed-infrastructure network design。
2. 传统 coverage / observability / OED / graph sampling 只部分匹配 recoverability 目标。
3. TRACE-BiOpt 的 bilevel framing：lower-level GLS/MAP reconstruction，upper-level recoverability objective。
4. Algorithm：scale-adaptive deterministic initialization + exchange refinement。
5. Theory：MAP stability、posterior risk、generalization、exchange certificate。
6. Evidence：three networks, three budgets, ten seeds, 21 baselines, Holm correction。

#### 建议删除或压缩的句子类型

| 当前句式类型 | 处理 |
|---|---|
| The intended reading is deliberately narrow... | 删除或移到 limitations/discussion |
| one auditable design argument tested against... | 改成一句普通 evidence summary |
| contribution stack that this paper asks a TR-B reader to evaluate... | 放到 appendix/supplement |
| reviewer-facing compression... | 删除，避免 meta-review 语气 |
| judged by whether it achieves row-wise strongest-baseline dominance... | 改为 Results preview |

#### 可替换段落草案

```text
TRACE-BiOpt treats sparse traffic sensor siting as a recoverability-driven network design problem. The lower level is a transparent GLS/MAP inverse problem that reconstructs the full traffic state from a selected sensor set. The upper level chooses the fixed layout by minimizing a single objective that combines hidden-state reconstruction loss, posterior uncertainty, CVaR tail risk, and spatial redundancy. Thus, the method optimizes a reconstruction-aware design criterion directly, rather than selecting among coverage, variance, graph-sampling, or historical TRACE-SL layouts.
```

```text
The empirical comparison is deliberately external to the solver. Random, variance, degree, coverage, graph-sampling, QR/POD, greedy A-trace, D-logdet, RCSS, validation-swap TRACE-SL, and multistart swap layouts are pre-registered baselines used only for evaluation. They are not candidates in the TRACE-BiOpt optimization procedure.
```

```text
Across three traffic networks and three budget levels, TRACE-BiOpt is compared against the row-wise strongest pre-registered non-BiOpt challenger and against the full 21-baseline registry using the same ten split seeds. This design separates the method definition from the comparison class and supports a scoped dominance claim under the stated GLS/MAP evaluation protocol.
```

#### 操作

```bash
rg -n "intended reading|auditable|contract|posture|reviewer-facing|asks a TR-B reader|one auditable" paper/sections/1_introduction.tex
```

每个命中执行以下判断：

- 是否是必要边界声明？
- 是否可以改成普通学术语气？
- 是否更适合放到 `SUBMISSION_EVIDENCE_INDEX.md` 或 appendix？

验收标准：

- [ ] Introduction 中 `audit/auditable/contract/posture` 合计出现不超过 1–2 次。
- [ ] 第一页读起来像 transport network design paper，而不是 audit report。
- [ ] Baseline 不进入 solver 这一点仍然清楚。
- [ ] 主 contribution 五点清楚。

---

### P0-5. Method section 保持“单一方法”，不要回到 pool narrative

Method section 必须继续守住：

```text
TRACE-BiOpt = one objective + one lower-level GLS/MAP inverse problem + one deterministic solver
```

#### Method section 必须包含

- Problem definition:
  \[
  \min_{S \subseteq V, |S|=k} J(S)
  \]
- Unified objective:
  \[
  J(S)=
  \text{hidden Huber reconstruction loss}
  +\beta \text{ posterior trace}/n
  +\gamma \text{ scenario CVaR}/n
  +\eta \text{ spatial penalty}.
  \]
- Lower-level reconstruction:
  \[
  \hat z_t(S)=A(S)^{-1}b_t(S).
  \]
- Deterministic solver:
  - scale-adaptive initialization；
  - objective-forward construction or posterior warm start；
  - one-exchange refinement；
  - same `J(S)` throughout。
- Explicit non-pool statement:
  - baselines are evaluation rows only；
  - no baseline layout is selected as method candidate；
  - validation is used for objective estimation/evaluation, not for selecting the best historical method.

#### 必须避免

| 避免表述 | 原因 |
|---|---|
| candidate generators are part of TRACE-BiOpt | 会回到 pool selector 风险 |
| choose the best among candidate layouts | reviewer 会认为是 AutoML/portfolio |
| validation-selected winner | 与单一优化方法冲突 |
| TRACE-SL is our main method | 与 current paper-facing method 冲突 |
| baselines enter the solver | 破坏方法身份 |

#### 操作

```bash
rg -n "candidate|pool|selector|selects among|winner|validation-selected|TRACE-SL" paper/sections/3_problem_formulation.tex paper/sections/4_method_theory.tex paper/sections/5_experiments.tex
```

每个命中分类：

- “historical baseline” 可保留；
- “method component” 必须修改；
- “not a candidate pool” 可保留但不要过度重复。

---

### P0-6. Theory section 增加 “does / does not imply” 边界框

当前理论厚度足够，但必须避免被审稿人抓“theory 与 empirical claim 不完全同构”。

#### 建议新增 subsection 或 remark

放在 theory theorem package 之后，标题：

```latex
\paragraph{Scope of the theoretical statements.}
```

或：

```latex
\begin{remark}[What the theory does and does not imply]
...
\end{remark}
```

#### 建议正文

```latex
The preceding statements support TRACE-BiOpt as a transparent and analyzable network-design procedure, but they do not by themselves prove empirical dominance on arbitrary traffic networks. The posterior-trace identity is a Gaussian squared-error Bayes-risk statement; the paper's main empirical metric is held-out hidden-state MAE under real traffic data. The all-layout generalization bound quantifies the statistical burden of validating size-$k$ layouts and should be read with independent validation blocks or an effective sample size for temporally dependent traffic. The exchange result certifies stationarity only over the searched one-exchange neighborhood, and becomes a full one-exchange certificate only when the full neighborhood is enumerated and the exchange gap is zero. These boundaries are why the empirical claim is stated only for the tested networks, budgets, seeds, estimator, and pre-registered comparison family.
```

#### 理论逐项边界

| 理论结果 | 支撑什么 | 不支撑什么 |
|---|---|---|
| MAP closed form/stability | lower-level estimator is transparent, unique, stable under assumptions | 所有 traffic data 上一定低 MAE |
| posterior trace identity | Gaussian squared-error Bayes risk certificate | non-Gaussian MAE 必然下降 |
| all-layout generalization | validation burden over all size-k layouts | current run 一定赢所有方法 |
| exchange certificate | searched-neighborhood stationarity | global optimum |
| CVaR epigraph | coherent tail-risk formulation | universal robustness under all perturbations |
| continuous relaxation | solver consistency intuition | relaxed-rounding evidence without multi-seed runs |

#### 操作

```bash
rg -n "posterior trace|Bayes|generalization|exchange|global|optimal|CVaR|robust" paper/sections/4_method_theory.tex
```

验收标准：

- [ ] 每个 theorem 后或 theory section 后有清楚边界。
- [ ] 不出现 “therefore TRACE-BiOpt must improve MAE”。
- [ ] 不出现 “global optimum”。
- [ ] temporal dependence 通过 block/effective sample size 说明。
- [ ] exchange certificate 只说 searched neighborhood。

---

### P0-7. Section 6 修 moved-to-supplement references

当前 Section 6 中有多处类似：

```latex
% MAP stability posture table moved to supplementary material (SUBMISSION_EVIDENCE_INDEX.md)
Table~\ref{tab:trace-biopt-map-stability} gives ...
```

这类写法有两个风险：

1. 如果 table 没有在 manuscript 中 `\input`，可能 undefined reference。
2. 如果 table 只在 repo/supplement，正文中写 `Table~\ref{...}` 会让读者在 PDF 中找不到。

#### 处理方式

对每一个 moved-to-supplement 表，二选一：

**方案 A：保留在 manuscript appendix**

- 在 appendix 中 `\input{tables/...}`。
- 正文引用改成 `Appendix Table~\ref{...}`。
- 表号仍可解析。

**方案 B：移到 supplement/repo**

- 正文不要用 `Table~\ref{...}`。
- 改成文字引用，例如：
  - `The corresponding supplementary stability summary is listed in the evidence index.`
  - `Supplementary Table Sx reports the detailed posture.`
  - `The source CSV and generated table are indexed in SUBMISSION_EVIDENCE_INDEX.md.`
- 在 `SUBMISSION_EVIDENCE_INDEX.md` 列明 supplement table ID。

#### 需要检查的可能表格

根据当前 Section 6，至少检查：

```text
tab:trace-biopt-map-stability
tab:trace-biopt-spatial-posture
tab:trace-biopt-layout-consensus-posture
tab:trace-biopt-initializer-posture
tab:trace-biopt-compute-posture
tab:trace-biopt-certificate-removal-probe
tab:trace-biopt-posterior-risk
tab:trace-biopt-weight-sensitivity
tab:trace-biopt-tail-risk-posture
```

#### 自动检查命令

```bash
# 找出所有“moved to supplementary”旁边仍在正文 ref 的地方
rg -n "moved to supplementary|Table~\\ref|Supplementary Table|SUBMISSION_EVIDENCE_INDEX" paper/sections paper/tables

# 编译后查 undefined references
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
rg -n "undefined|Undefined|Reference.*undefined|There were undefined references|Rerun" main.log
```

#### 推荐修改模式

原文：

```latex
% Posterior risk posture table moved to supplementary material (SUBMISSION_EVIDENCE_INDEX.md)
Table~\ref{tab:trace-biopt-posterior-risk} is the bounded theorem-to-evidence bridge...
```

改为：

```latex
The posterior-risk posture is treated as supplementary mechanism evidence and indexed in the repository evidence file. Its role is bounded: posterior trace is used as a squared-risk certificate within matched TRACE-BiOpt route comparisons, not as a universal MAE-ranking theorem.
```

如果要保留表：

```latex
Appendix Table~\ref{tab:trace-biopt-posterior-risk} reports the bounded posterior-risk posture.
```

验收标准：

- [ ] 编译无 undefined references。
- [ ] 正文所有 `Table~\ref{}` 都对应 PDF 中实际可见表。
- [ ] supplement/repo 表不再被当成主文表引用。
- [ ] Section 6 字数和表格数量明显下降。

---

### P0-8. Robustness 降级成 bounded deployment stress

Robustness section 不能在 abstract、conclusion、main claim 中暗示 TRACE-BiOpt is robust winner under all perturbations。

#### 推荐主表述

```text
The robustness analysis is a bounded deployment-stress screen, not a replacement for the main current-best dominance evidence. It tests how selected layouts behave under sensor failure, observation noise, missingness, cost proxies, and temporal shift. The results identify practical deployment vulnerabilities and motivate robust extensions; they do not establish universal robustness dominance for TRACE-BiOpt.
```

#### 不要写

- `TRACE-BiOpt is robust under perturbations.`
- `TRACE-BiOpt dominates all stress tests.`
- `Robustness experiments confirm universal deployment reliability.`
- `TRACE-BiOpt is deployable in Seattle 20/30%.`

#### 可写

- `bounded stress evidence`
- `deployment-screening evidence`
- `nominal recoverability design`
- `stress-test routing`
- `robust extension motivation`
- `conservative staged rollout interpretation`

#### Conclusion 中的具体修改

当前 conclusion 中类似：

```latex
Seattle as a conservative staged-rollout case whose 20/30\% promoted routes are deployable while the 10\% row remains intentionally fail-closed on promotion evidence.
```

建议改为：

```latex
Seattle is best read as a conservative staged-rollout case: the 20/30\% rows are supported by promoted current-best evidence, while the 10\% row remains intentionally retained on the audited Stage15 lane after the Stage16 promotion gate failed closed.
```

或更简洁：

```latex
Seattle illustrates conservative evidence routing: promoted current-best evidence supports the 20/30\% rows, while the 10\% row remains on the audited Stage15 lane after the Stage16 promotion gate failed closed.
```

验收标准：

- [ ] Abstract 不提 robustness dominance。
- [ ] Main result claim 不把 stress tests 混入 189 paired tests。
- [ ] Robustness section 明确 “not globally robust”。
- [ ] Conclusion 不用 “deployable” 作为未限定部署结论。

---

### P0-9. 投稿材料补齐

即使 manuscript scientifically ready，portal-ready 仍需要材料齐全。

#### 必备文件

建议在 `paper/submission_package/` 下准备：

```text
cover_letter_TRB.txt
highlights.txt
declaration_of_competing_interest.txt
credit_author_statement.txt
funding_statement.txt
data_availability_statement.txt
generative_ai_declaration.txt
author_metadata.txt
suggested_reviewers_optional.txt
source_file_manifest.txt
supplementary_file_manifest.txt
```

#### author metadata

`paper/main.tex` 目前匿名占位：

```latex
\shortauthors{Anonymous Authors}
\author[1]{Anonymous Author}
\affiliation[1]{organization={Anonymous Institution}, city={Anonymous City}, country={Anonymous Country}}
```

投稿前要根据是否双盲要求处理：

- 如果 journal submission 要求匿名审稿：主稿保持匿名，但 portal 填作者信息。
- 如果不匿名：替换为真实作者和 affiliation。
- 无论哪种，cover letter 与 portal metadata 不能留 placeholder。

#### Declaration of competing interest

模板：

```text
Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
```

如果有利益冲突，必须改成真实情况。

#### Funding statement

无 funding 时：

```text
Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.
```

有 funding 时填真实项目号。

#### Generative AI declaration

如果使用过 ChatGPT/Claude/GPT 辅助写作、代码审查、语言润色或计划制定，建议透明声明：

```text
Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work, the authors used ChatGPT and related AI-assisted tools to support manuscript organization, language editing, code-review planning, and consistency checks. After using these tools, the authors reviewed, verified, edited, and adapted the content as needed and take full responsibility for the content of the submitted manuscript.
```

如果没有使用生成式 AI，则按 journal policy 不需要添加；但本项目实际已使用 AI 辅助计划和审查时，建议声明。

#### Data availability statement

可用模板：

```text
Data availability

The TRACE-BiOpt code, scripts, generated tables, and paper-facing evidence artifacts are available in the project repository. Raw PeMS and Seattle traffic datasets are not redistributed with the repository; the repository documents the expected local data paths and provides scripts to regenerate the reported evidence when the datasets are available.
```

#### CRediT author statement

如果单作者：

```text
[Author Name]: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization.
```

如果多作者，逐个列贡献。

---

## 4. 表格与图件重排计划

### 4.1 核心原则

主文不应承担完整 evidence archive 的功能。主文只回答 reviewer 第一遍阅读时最重要的问题：

1. 方法是什么？
2. 不是 pool/selector 的证据在哪里？
3. 理论支撑是什么？
4. 结果是否真的打败 strongest baseline？
5. 是否只是 cherry-pick？
6. 边界是什么？

其他 audit 证据放 appendix/supplement/repo。

---

### 4.2 主文建议保留的图表

主文建议保留 4–6 个核心图表。

| 位置 | 图表 | 作用 | 建议 |
|---|---|---|---|
| Introduction or Method | workflow / formulation figure | 一眼说明 bilevel design + GLS/MAP reconstruction | 保留 |
| Results | `table_trace_biopt_dominance` | 主结果：row-wise strongest challenger dominance | 保留 |
| Results | `table_trace_biopt_significance_posture` | 证明不是只赢 best challenger，而是 189/189 corrected comparisons | 保留，但可压缩 |
| Theory/Method | theory summary table or theorem bridge | 把 theorem 与 claim boundary 对齐 | 保留或改成短文字 |
| Mechanism | 一个机制/solver diagnostic summary | 解释为什么不是 renaming baseline | 保留一个即可 |
| Robustness | bounded robustness routing table | 明确 robustness 是 stress screen，不是主 claim | 保留一个简版 |

---

### 4.3 Appendix 建议保留的表

Appendix 的任务是防 reviewer 质疑：

| Appendix 表 | 保留理由 |
|---|---|
| full baseline matrix | 防止 cherry-picking；显示全部 21 baselines |
| baseline registry | 证明 baselines pre-registered / comparison class 清楚 |
| current-best provenance | 解释 Stage15 / Stage16 / Seattle 10% retention |
| claim boundary matrix | 防 overclaim |
| exact subnetwork benchmark | 支撑 bounded exactness / solver correctness |
| exchange certificate | 支撑 theory-to-algorithm boundary |
| solver scale | 解释 compute burden and search-budget sensitivity |
| generalization burden | 支撑 validation sample/combinatorial burden |
| weight sensitivity | 如果缩短后仍必要，可放 appendix |

---

### 4.4 Supplement / repo 建议存放的表

这些不应打断主文叙事，更适合 `SUBMISSION_EVIDENCE_INDEX.md` 或 supplement：

| 表/材料 | 推荐位置 |
|---|---|
| reader guide | supplement/repo |
| comparison ladder | supplement/repo |
| method contract table | supplement/repo；主文用文字说明 |
| problem contract table | supplement/repo |
| planning takeaways | supplement/repo；Conclusion 用 1 段文字 |
| posterior-risk posture | supplement/repo，或 appendix 精简 |
| tail-risk posture | supplement/repo，或 appendix 精简 |
| spatial posture | supplement/repo |
| layout consensus posture | supplement/repo |
| initializer posture | supplement/repo |
| compute posture | supplement/repo |
| MAP stability posture | supplement/repo，除非 theory reviewers 需要 |
| certificate removal probe | supplement/repo |
| all detail CSVs | repo/evidence index |

---

### 4.5 表格重排操作清单

执行：

```bash
# 1. 列出主文 input 的所有 tables
rg -n "\\input\{tables/" paper/main.tex paper/sections paper/appendix.tex

# 2. 列出所有 labels
rg -n "\\label\{tab:" paper/tables paper/sections paper/main.tex

# 3. 列出所有正文 table refs
rg -n "Table~\\ref\{tab:" paper/sections paper/main.tex

# 4. 找 moved-to-supplement 但仍 ref 的地方
rg -n "moved to supplementary|Table~\\ref" paper/sections/6_ablation_robustness.tex
```

然后建立一个表格地图：

```text
paper/TABLE_ROUTING_AUDIT.md
```

内容：

```markdown
| Label | File | Current location | New location | Ref text status | Decision |
|---|---|---|---|---|---|
| tab:trace-biopt-dominance | paper/tables/table_trace_biopt_dominance.tex | main | main | OK | keep |
| tab:trace-biopt-full-baseline-matrix | ... | appendix | appendix | OK | keep |
| tab:trace-biopt-posterior-risk | ... | section 6 ref only | supplement | rewrite ref | move |
```

验收标准：

- [ ] 主文表格数量明显下降。
- [ ] Appendix 表格都有防质疑功能。
- [ ] Supplement/repo 表格都有 evidence index entry。
- [ ] 所有 table refs 可解析。
- [ ] 没有“注释说 moved，但正文仍 Table ref”的情况。

---

## 5. 按论文 section 的详细修改计划

---

### 5.1 `paper/main.tex`

#### 必须修改

- [ ] 填真实 author/affiliation，或确认匿名审稿版本。
- [ ] Abstract ≤250 words。
- [ ] Highlights 移到单独 `highlights.txt`。
- [ ] 检查 keywords 1–7 个。
- [ ] 检查 declaration sections 是否存在并准确。
- [ ] 如果使用 AI 辅助，新增 AI declaration section before references。
- [ ] 检查 data availability statement 不承诺 raw datasets 已分发。

#### 建议 keywords

```text
Traffic sensor siting
Network design
Bilevel optimization
Traffic state reconstruction
Sensor placement
GLS/MAP estimation
Transportation networks
```

如果必须 1–7 个，保留 6–7 个即可。

#### AI declaration 插入位置

放在 references 前：

```latex
\section*{Declaration of generative AI and AI-assisted technologies in the manuscript preparation process}
During the preparation of this work, the authors used ChatGPT and related AI-assisted tools to support manuscript organization, language editing, code-review planning, and consistency checks. After using these tools, the authors reviewed, verified, edited, and adapted the content as needed and take full responsibility for the content of the submitted manuscript.
```

如果 journal/portal 要求单独文件，也在 `submission_package/generative_ai_declaration.txt` 中放同样内容。

---

### 5.2 `paper/sections/1_introduction.tex`

#### 当前问题

- 交通问题 framing 是对的。
- 但 “intended reading / auditable / reviewer-facing / contract” 语言较多。
- `\input{tables/table_trace_biopt_dominance}` 放在 Introduction 末尾可能过早，让 Introduction 变成结果表驱动。

#### 建议修改

- [ ] 保留第 0–5 行的交通网络设计 framing。
- [ ] 删减第 6–12 行的 meta-review 语气。
- [ ] 把 dominance table 移到 Results section，或保留但需保证 Introduction 不被表格打断。
- [ ] Contributions 改成自然段或普通 numbered list。
- [ ] 不要在 Introduction 中放太多 evidence audit 语言。

#### 建议 contribution wording

```latex
This paper makes five contributions. First, it formulates sparse traffic sensor siting as a recoverability-driven bilevel stochastic network design problem. Second, it defines a transparent GLS/MAP lower-level reconstruction model and an upper-level objective that combines hidden-state reconstruction loss, posterior uncertainty, tail risk, and spatial redundancy. Third, it develops TRACE-BiOpt as a deterministic single-objective solver with scale-adaptive initialization and one-exchange refinement. Fourth, it establishes stability, posterior-risk, validation-generalization, and exchange-stationarity statements that clarify what the method can certify. Fifth, it evaluates TRACE-BiOpt against 21 pre-registered non-BiOpt baselines over three networks, three budgets, and ten split seeds.
```

---

### 5.3 `paper/sections/2_related_work.tex`

#### 目标

Related Work 应把 TRACE-BiOpt 放在交通网络设计和 sensor siting 文献中，而不是过早讲 comparison contract。

#### 建议结构

1. Traffic count location and OD estimation。
2. Link-flow observability and sensor reliability。
3. Traffic state estimation under partial observation。
4. Sensor selection, OED, graph sampling, POD/QR。
5. Bilevel/stochastic/robust network design。
6. Positioning paragraph: TRACE-BiOpt differs by optimizing recoverability under explicit lower-level reconstruction.

#### 需要减少

- `comparison contract`
- `audit`
- `posture`
- `reader guide`
- `winner`

#### Positioning paragraph 草案

```latex
TRACE-BiOpt differs from these lines of work in the object it optimizes. The design variable is a fixed sparse sensor layout, but the performance criterion is hidden-network recoverability under an explicit transparent reconstruction model. This couples sensor siting and downstream state reconstruction in a bilevel design problem. The comparison baselines are therefore used externally, to test whether the bilevel design improves held-out reconstruction error relative to standard coverage, variance, observability, graph-sampling, and predecessor TRACE-SL/RCSS layouts.
```

---

### 5.4 `paper/sections/3_problem_formulation.tex`

#### 必须确认

- [ ] Problem 是 sparse sensor siting / fixed-infrastructure network design。
- [ ] Layout \(S\) 是固定预算 \(k\)。
- [ ] Hidden complement 是 evaluation target。
- [ ] lower-level estimator 与 method/theory/experiment 同一个 GLS/MAP。
- [ ] validation/test split 定义清楚。
- [ ] 不把 estimator improvement 与 siting problem 混淆。

#### 建议添加

一个 definition：

```latex
\begin{definition}[Recoverability-driven sensor siting]
Given a traffic network, a candidate set of sensing locations, and a budget \(k\), recoverability-driven sensor siting chooses a fixed set \(S\) with \(|S|=k\) before held-out traffic states are observed. The quality of \(S\) is measured by the error with which a declared reconstruction model recovers the hidden complement \(V\setminus S\).
\end{definition}
```

#### 验收标准

- [ ] 读完 Section 3，reviewer 能说出 decision variable、objective target、evaluation metric。
- [ ] 没有 candidate-pool 主方法叙事。
- [ ] Baselines 尚未进入 method definition。

---

### 5.5 `paper/sections/4_method_theory.tex`

#### 必须保留

- Lower-level MAP/GLS problem。
- Closed form \(A(S)^{-1}b_t(S)\)。
- Unified upper-level objective。
- Solver pseudocode。
- Theory package。
- Theory scope remark。

#### 建议添加 algorithm block

```latex
\begin{algorithm}[t]
\caption{TRACE-BiOpt deterministic layout solver}
\begin{algorithmic}[1]
\State Input network, budget \(k\), validation states, objective weights \((\beta,\gamma,\eta)\)
\State Build GLS/MAP lower-level matrices and traffic priors
\State Initialize \(S_0\) by scale-adaptive objective-forward construction or posterior warm start
\For{exchange iteration \(m=0,1,\ldots\)}
  \State Evaluate searched one-exchange moves \(S_m\setminus\{i\}\cup\{j\}\) under the same objective \(J\)
  \If{best strict improvement exceeds tolerance}
    \State Accept the best improving move
  \Else
    \State Stop with searched-neighborhood certificate
  \EndIf
\EndFor
\State Return final fixed layout \(\hat S\)
\end{algorithmic}
\end{algorithm}
```

#### Theory scope remark

使用 P0-6 的文字。

#### 验收标准

- [ ] Method 是 single objective throughout。
- [ ] Algorithm 没有选择 baseline。
- [ ] 任何 active-set acceleration 都被定义为 solver acceleration, not a second method。
- [ ] Theory statements 不 overclaim。

---

### 5.6 `paper/sections/5_experiments.tex`

#### 必须写清楚

- Datasets:
  - PeMS7_228；
  - PeMS7_1026；
  - Seattle。
- Budgets:
  - 10%、20%、30%。
- Splits:
  - ten split seeds。
- Estimator:
  - GLS/MAP。
- Main metric:
  - held-out hidden-state MAE。
- Baseline registry:
  - 21 pre-registered non-BiOpt baselines；
  - 不进入 TRACE-BiOpt solver。
- Multiple testing:
  - one-sided paired tests；
  - Holm correction over 189 row-baseline comparisons。
- Evidence lane:
  - current-best hybrid chain；
  - 8/9 Stage16 promoted；
  - Seattle 10% retained Stage15 fail-closed。

#### 必须避免

- 不要说 “we selected best baseline after seeing test results”。
- 不要让 Stage15/Stage16 看起来是 post-hoc cherry-picking。
- 不要用 “directional” 描述 current-best main evidence。
- 不要让 Seattle 10% 看起来未完成。

#### Stage15/Stage16 provenance 推荐文字

```latex
The current-best evidence chain is hybrid by design. Complete Stage16 calibrated reruns are promoted when the predefined replacement gate is satisfied; otherwise the row remains on the audited Stage15 lane. Eight of the nine dataset-budget rows are promoted Stage16 rows. Seattle 10\% remains intentionally retained on the Stage15 lane because its Stage16 candidate did not pass the replacement gate. This fail-closed rule prevents weaker reruns from replacing audited ten-seed evidence and preserves the same external comparison protocol.
```

#### 验收标准

- [ ] `current-best` 的定义清楚。
- [ ] Seattle 10% 不被描述为 incomplete。
- [ ] 21 baselines 的 pre-registered 性质清楚。
- [ ] Holm family size 189 清楚。
- [ ] 不暗示 untested comparisons。

---

### 5.7 Results section

#### 主结果表建议

保留 strongest-challenger table，但 caption 可以更自然。

当前 caption 很长，建议压缩：

```latex
\caption{Current-best ten-seed dominance against the row-wise strongest pre-registered non-BiOpt challenger. Lower MAE is better. Paired tests use the same ten split seeds. Stage16 calibrated rows are promoted only when the predefined replacement gate is satisfied; Seattle 10\% remains on the audited Stage15 lane.}
```

#### Significance posture table

保留或压缩。它的作用是防止 reviewer 说 “只赢 best baseline table”。

建议正文解释：

```latex
Table~\ref{tab:trace-biopt-significance-posture} checks the full comparison family rather than only the strongest-challenger summary. In all nine rows, all 21 pre-registered non-BiOpt baselines remain significantly worse after Holm correction over the 189 row-baseline paired tests.
```

#### 结果段落不要写

- `dominates all methods`
- `wins universally`
- `all baselines`
- `full robustness`
- `global optimality`

#### 验收标准

- [ ] Main result table and all-baseline table互补。
- [ ] 强 claim 与 spec 一致。
- [ ] 不使用未限定 “all baselines”。
- [ ] p-values 不被过度解释为 practical significance；同时报告 MAE delta/win count。

---

### 5.8 `paper/sections/6_ablation_robustness.tex`

当前这个 section 实际包含 mechanism analysis、calibration diagnostics、optimization diagnostics、大量姿态表。它应该减重。

#### 建议拆分或重命名

当前 section 标题：

```latex
\section{Mechanism analysis and calibration diagnostics}
```

可以保留，但内容要更有层级。

建议内部结构：

1. Why the main result is not a selector artifact。
2. Calibration and search-budget sensitivity。
3. Layout mechanism: maps/fingerprints/hidden error heatmaps。
4. Optimization diagnostics: objective descent and exchange certificate。
5. Supplementary posture evidence is indexed in evidence index。

#### 要减少的内容

- 一表一段的 audit narrative。
- 对 moved-to-supplement 表的详细正文描述。
- 过多 “posture” 词。
- 太多 exact numeric mechanism slices，保留最有解释力的。

#### 保留的机制点

| 机制点 | 保留理由 |
|---|---|
| strongest comparator gating | 说明不是 straw man baseline |
| calibration-sensitive low-budget rows | 解释 PeMS7_228 10% |
| search-budget-sensitive large network | 解释 PeMS7_1026 |
| layout maps/fingerprints | 说明不是同一 sensor set 改名 |
| hidden error heatmaps | 说明收益不是极少数节点驱动 |
| objective descent/exchange | 说明 solver 确实优化同一 J(S) |

#### 验收标准

- [ ] Section 6 不像 artifact catalog。
- [ ] 不再逐个讲所有 supplementary posture tables。
- [ ] 仍能回答 “为什么不是 pool/selector/cherry-pick？”
- [ ] 所有引用表/图可见或正确指向 supplement。

---

### 5.9 Robustness section

详见 P0-8。

#### 建议结尾

```latex
These stress tests should be read as deployment screens rather than as an extension of the main dominance claim. They identify where a nominal recoverability-driven layout remains stable and where additional reliability or cost constraints should be built into future design objectives.
```

---

### 5.10 Discussion section

Discussion 应主动说边界。建议包含：

1. Tested regimes only。
2. Pre-registered non-BiOpt baselines only。
3. No global optimum claim。
4. Posterior trace is squared-risk certificate, not MAE theorem。
5. Temporal dependence requires block/effective-sample interpretation。
6. Robustness tests are bounded screens。
7. Raw datasets not redistributed; reproducibility requires local placement。
8. Compute burden grows with network and budget。

#### 推荐 wording

```latex
The empirical claim is intentionally scoped. It concerns three traffic networks, three budget levels, ten split seeds, the declared GLS/MAP reconstruction protocol, and the 21 pre-registered non-BiOpt baselines in the current-best evidence chain. It does not imply dominance over untested layout families or universal cross-network generalization.
```

---

### 5.11 Conclusion section

#### 当前要改的地方

- 避免 “deployable”。
- 减少 meta-review language。
- 结尾要强调 transport planning insight，而不是继续谈 contract。

#### 建议 conclusion 末段

```latex
For transportation agencies, the practical implication is that sparse sensor siting should be treated as an infrastructure design problem tied to downstream recoverability. A layout is valuable not only because it observes high-flow or high-variance locations, but because it improves reconstruction of the hidden network under a declared estimator. TRACE-BiOpt provides one way to make that design logic explicit, auditable, and statistically testable against strong pre-registered alternatives.
```

如果不想用 `auditable`，更自然版本：

```latex
TRACE-BiOpt provides one way to make that design logic explicit, reproducible, and statistically testable against strong pre-registered alternatives.
```

---

## 6. 仓库与复现入口修改计划

---

### 6.1 Root `README.md`

当前 README 已基本修正，前几行已经说明 current paper-facing method is TRACE-BiOpt，不是 candidate-pool selector。只需最终检查：

- [ ] 前 20 行是否清楚写 current method。
- [ ] Legacy TRACE-SL / RCSS 是否明确是 historical baseline / diagnostic comparator。
- [ ] `trace_biopt.py` 是否被称为 CLI wrapper，而不是 core solver implementation。
- [ ] `current_best_trace_biopt_evidence/` 是否是 authoritative evidence source。
- [ ] smoke test 命令是否可复制。
- [ ] raw datasets 不随 repo 分发这点清楚。

#### README 验收 grep

```bash
sed -n '1,120p' README.md
rg -n "candidate-pool|AutoML|TRACE-SL|RCSS|trace_biopt.py|current_best_trace_biopt_evidence" README.md
```

如果出现：

```text
trace_biopt.py: solver implementation
```

改成：

```text
trace_biopt.py: CLI wrapper that invokes transparent_estimator_eval.py with --include-biopt; solver logic is implemented in the TRACE-BiOpt routines inside transparent_estimator_eval.py.
```

如果决定重构代码，则改成：

```text
trace_biopt.py: CLI entry point for TRACE-BiOpt; core objective and solver routines live in trace_biopt_core.py.
```

---

### 6.2 `RESEARCH_PIPELINE_REPORT.md`

当前这个 report 仍可能存在一个重要措辞问题：它把 `TRC-23-02333/trace_biopt.py` 叫做 solver implementation。若实际文件仍是 thin wrapper，则必须改。

#### 建议修改

原：

```text
TRC-23-02333/trace_biopt.py: TRACE-BiOpt solver implementation with bilevel objective...
```

改：

```text
TRC-23-02333/trace_biopt.py: TRACE-BiOpt CLI wrapper that calls transparent_estimator_eval.py with --include-biopt. The current solver routines for the bilevel objective, deterministic initialization, and exchange refinement are implemented in transparent_estimator_eval.py. A future cleanup may factor these routines into trace_biopt_core.py, but the paper-facing CLI entry point is trace_biopt.py.
```

如果做推荐重构，则写：

```text
TRC-23-02333/trace_biopt.py: CLI entry point.
TRC-23-02333/trace_biopt_core.py: TRACE-BiOpt objective, initialization, and exchange-refinement solver routines.
TRC-23-02333/transparent_estimator_eval.py: evaluation driver and baseline comparison pipeline.
```

#### 验收标准

- [ ] `README.md`、`TRACE_BIOPT_SPEC.md`、`RESEARCH_PIPELINE_REPORT.md` 对 entry point 的描述一致。
- [ ] 不误导 reviewer 以为 wrapper 文件里实现了所有 solver logic。
- [ ] 如果不重构，也要诚实说明。

---

### 6.3 `SUBMISSION_EVIDENCE_INDEX.md`

当前这个文件定位很好，应作为 reviewer/co-author 的 single evidence entry point。投稿前要确保它包含：

| 字段 | 必须有 |
|---|---|
| claim | paper 中对应 claim |
| table/figure | manuscript table/figure |
| source artifact | CSV/JSON/MD |
| generation script | script path |
| input stage | Stage15/Stage16/source |
| status | committed / supplement / generated |
| row provenance | Stage15 retained or Stage16 promoted |
| replacement rule | promoted / fail-closed |
| date refreshed | 2026-05-28 or later |
| commit hash | final submission commit hash |

#### 建议新增 commit hash

在文件顶部加：

```markdown
Repository commit used for submission package: `<commit_hash>`
```

提交前自动填：

```bash
git rev-parse HEAD
```

#### current-best evidence 目录检查

确保目录包含：

```text
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
  trace_biopt_claim_contract.json
  trace_biopt_claim_contract.csv
  trace_biopt_best_baseline_delta.csv
  trace_biopt_full_baseline_matrix.csv
  trace_biopt_current_best_provenance.csv
  trace_biopt_significance_posture_detail.csv
  trace_biopt_exact_subnetwork_summary.csv
  trace_biopt_exact_subnetwork_detail.csv
  TRACE_BIOPT_DOMINANCE.md
```

检查命令：

```bash
ls -lah TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence
```

如果有些 raw output 因体积不提交，必须在 index 中说明：

```markdown
Raw per-run history JSON files are not all committed because of size. The committed summary CSV/JSON files used by manuscript tables are listed below, and the full regeneration path is ...
```

---

### 6.4 `TRACE_BIOPT_SPEC.md`

该文件应作为 method contract，不需要大改。最终确认：

- [ ] Method Identity 清楚：not candidate pool。
- [ ] Objective 清楚。
- [ ] Lower-level reconstruction 清楚。
- [ ] Solver stopping rule 清楚。
- [ ] Evidence state 清楚。
- [ ] Claim boundary 清楚。
- [ ] Relationship to manuscript 清楚。

#### 必须检查禁止 claim

Spec 中已有 forbidden claims。确保 manuscript 完全遵守：

```bash
rg -n "global optimality|untested baseline|universal|robustness outside|relaxed-rounding" TRACE_BIOPT_SPEC.md paper
```

---

### 6.5 `TRACE_BIOPT_THEORY.md`

确认其 theorem statements 与 manuscript 一致。

#### 检查点

- [ ] theorem numbering / naming 与 paper 对齐。
- [ ] posterior trace theorem 是 squared-error / Gaussian。
- [ ] generalization theorem 说明 bounded independent or blocks/effective sample size。
- [ ] exchange theorem 说明 searched neighborhood。
- [ ] CVaR epigraph 不被写成 universal robustness。
- [ ] continuous relaxation 不支撑未跑 multi-seed 的 relaxed-rounding performance claim。

---

### 6.6 `TRC-23-02333/trace_sl_results/README.md`

该 README 应避免让 reviewer 以为 Stage12/TRACE-SL 是当前主 evidence。

建议开头：

```markdown
# TRACE result artifacts

Current paper-facing evidence for the TR-B TRACE-BiOpt manuscript is:

`current_best_trace_biopt_evidence/`

Legacy TRACE-SL/RCSS Stage6--Stage14 artifacts are preserved for historical baseline and diagnostic purposes. They are not the authoritative evidence source for the current TRACE-BiOpt manuscript claims.
```

---

### 6.7 Code refactor：推荐版与最小版

#### 推荐版

新建：

```text
TRC-23-02333/trace_biopt_core.py
```

迁移：

- `trace_biopt_objective`
- relaxed objective routines
- initializer
- `trace_biopt_layout`
- exchange refinement
- history logging helpers

保留：

```text
transparent_estimator_eval.py
```

作为 evaluator / CLI / baseline driver。

`trace_biopt.py` 作为 clean CLI entry point。

优点：

- reviewer 容易定位主方法。
- README 和 code architecture 一致。
- transparent evaluator 不再过于臃肿。

#### 最小可接受版

不重构代码，但必须：

- README 明确 `trace_biopt.py` 是 wrapper。
- `TRACE_BIOPT_SPEC.md` 明确 main implementation path。
- `RESEARCH_PIPELINE_REPORT.md` 不把 wrapper 称作 core solver。
- tests 明确包含 BiOpt-specific tests。
- smoke test 命令可复制。

#### 最小命令

```bash
python TRC-23-02333/trace_biopt.py \
  --data-root TRC-23-02333/dataset/PeMS7_228 \
  --budgets "0.10" \
  --seeds 25 \
  --include-baseline-portfolio \
  --output-dir TRC-23-02333/trace_sl_results/example_trace_biopt
```

---

### 6.8 Tests

#### 必须运行

```bash
pytest -q \
  TRC-23-02333/test_transparent_estimator_eval.py \
  TRC-23-02333/test_summarize_trace_sl_rcss.py \
  scripts/test_generate_trace_biopt_dominance.py \
  scripts/test_generate_trace_biopt_claim_contract.py \
  tests/test_stage12_runtime_fast_paths.py \
  tests/test_stage12_runtime_trace_cache.py
```

如果仍保留脚本式 test runner：

```bash
python TRC-23-02333/test_transparent_estimator_eval.py
```

必须确认 `run_all()` 包含所有 BiOpt-specific tests。搜索：

```bash
rg -n "test_trace_biopt|run_all|def test_" TRC-23-02333/test_transparent_estimator_eval.py
```

验收标准：

- [ ] pytest 发现并运行 BiOpt objective tests。
- [ ] deterministic-and-not-pool-selected test 存在。
- [ ] relaxed objective test 存在。
- [ ] posterior warm-start / auto initializer threshold test 存在。
- [ ] 如果 `run_all()` 保留，则不跳过 BiOpt tests。
- [ ] 如果 `run_all()` 删除，则 README 只要求 pytest。

---

## 7. Claim wording 全文替换表

### 7.1 推荐替换表

| 原风险表达 | 替换表达 |
|---|---|
| all baselines | all 21 pre-registered non-BiOpt baselines in the tested regimes |
| benchmark winner | lowest mean held-out GLS/MAP MAE under the stated protocol |
| robust dominance | bounded deployment-stress behavior |
| deployable | supported by promoted current-best evidence |
| exact optimality | exact lower-level MAP solution; deterministic upper-level exchange search |
| global optimum | searched-neighborhood stationarity certificate |
| proves effectiveness | supports the method under the stated assumptions and evidence contract |
| universal generalization | evidence across the three tested networks and budgets |
| all future traffic states | held-out test windows under the stated splits |
| no competitor | no pre-registered challenger remains tied or better after Holm correction |

### 7.2 Grep audit

```bash
rg -n "all baselines|benchmark winner|robust dominance|deployable|exact optimal|global optimum|proves effectiveness|universal|all future|no competitor" paper README.md TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md RESEARCH_PIPELINE_REPORT.md
```

---

## 8. Stage15 / Stage16 provenance 写法

### 8.1 正确叙事

当前 current-best chain 是 hybrid，但这不是弱点，只要解释清楚：

- Stage16 calibrated rows are promoted only when replacement gate is satisfied。
- 8/9 rows promoted。
- Seattle 10% retained on audited Stage15 lane because Stage16 did not pass promotion gate。
- fail-closed policy prevents weaker evidence from replacing audited main evidence。
- all nine current-best rows satisfy current claim contract。

### 8.2 推荐主文一句话

```latex
The current-best evidence chain promotes complete Stage16 calibrated reruns when the predefined replacement gate is satisfied; otherwise it fails closed to the audited Stage15 ten-seed lane. Eight of nine rows are Stage16-promoted, while Seattle 10\% is intentionally retained on Stage15 evidence.
```

### 8.3 Appendix 解释

在 appendix provenance table 旁边写：

```latex
Seattle 10\% is not an unfinished row. Its Stage16 candidate did not satisfy the replacement gate, so the current-best chain retains the audited Stage15 ten-seed row. This fail-closed policy protects the main claim from opportunistic replacement and keeps the comparison family fixed.
```

### 8.4 不要写

- `Seattle 10% still awaits promotion`
- `remaining unfinished row`
- `directional Stage16 evidence`
- `temporary retention`
- `incomplete current-best row`

---

## 9. Cover letter 草案

建议新建：

```text
paper/submission_package/cover_letter_TRB.txt
```

草案：

```text
Dear Editors,

We are pleased to submit our manuscript, "TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting," for consideration in Transportation Research Part B: Methodological.

The paper studies sparse traffic sensor siting as a fixed-infrastructure transportation network design problem. Given a sensor budget, the goal is to choose a long-lived sensor layout that improves reconstruction of the hidden traffic network state under a transparent GLS/MAP estimator. We propose TRACE-BiOpt, a bilevel stochastic optimization method whose lower level is a transparent inverse problem and whose upper level combines hidden-state reconstruction loss, posterior uncertainty, CVaR tail risk, and spatial redundancy regularization. The solver uses deterministic initialization and one-exchange refinement under the same objective; pre-registered baselines are not used as method candidates.

The manuscript contributes a methodological formulation, a deterministic solver, and a scoped theory package covering MAP stability, posterior-risk interpretation, all-layout validation generalization, CVaR interpretation, and exchange-stationarity certification. Empirically, we evaluate TRACE-BiOpt on PeMS7_228, PeMS7_1026, and Seattle networks at 10%, 20%, and 30% sensor budgets over ten split seeds. Under the stated GLS/MAP protocol, TRACE-BiOpt achieves the lowest mean held-out hidden-state MAE against 21 pre-registered non-BiOpt baselines in all nine dataset-budget regimes, and Holm-corrected paired tests over the 189 row-baseline comparisons leave no statistically tied or significantly better pre-registered challenger.

We believe the paper fits Transportation Research Part B because it develops a mathematical and algorithmic method for transportation network design under partial observation, with transparent reconstruction, risk-aware optimization, and reproducible statistical evaluation.

All authors have approved the manuscript and agree with its submission. The manuscript is not under consideration elsewhere.

Sincerely,
[Corresponding Author Name]
[Affiliation]
[Email]
```

根据真实情况修改：

- 是否双盲；
- 作者名单；
- 是否有 preprint；
- 是否有相关投稿；
- 是否有 conflict of interest；
- suggested reviewers 是否另附。

---

## 10. Final validation commands

投稿前从仓库根目录执行：

```bash
# 0. 记录提交
git status --short
git rev-parse HEAD

# 1. 刷新 current-best paper chain
bash scripts/refresh_current_best_trace_biopt_paper_chain.sh

# 2. 单元测试
pytest -q \
  TRC-23-02333/test_transparent_estimator_eval.py \
  TRC-23-02333/test_summarize_trace_sl_rcss.py \
  scripts/test_generate_trace_biopt_dominance.py \
  scripts/test_generate_trace_biopt_claim_contract.py \
  tests/test_stage12_runtime_fast_paths.py \
  tests/test_stage12_runtime_trace_cache.py

# 3. 编译 manuscript
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# 4. 查 LaTeX warnings
rg -n "undefined|Undefined|Warning|Overfull|Underfull|Rerun|multiply|badness|empty anchor" main.log main.blg || true

# 5. 查 overclaim
cd ..
rg -n "all baselines|universally|global optimum|robust under|deployable|dominates all|proves.*MAE|untested|all networks|all budgets" paper README.md TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md RESEARCH_PIPELINE_REPORT.md || true

# 6. 查 moved-to-supplement refs
rg -n "moved to supplementary|Table~\\ref" paper/sections/6_ablation_robustness.tex

# 7. 查 metadata 占位符
rg -n "Anonymous|TODO|TBD|placeholder|fill|Insert|Your Name|Institution" paper paper/submission_package README.md RESEARCH_PIPELINE_REPORT.md || true

# 8. git diff whitespace
git diff --check
```

验收标准：

- [ ] `git status` 只显示预期修改。
- [ ] refresh script 成功。
- [ ] pytest 通过。
- [ ] LaTeX 编译成功。
- [ ] 无 undefined references。
- [ ] overclaim grep 无未处理命中。
- [ ] metadata grep 无投稿版本中不应出现的占位符。
- [ ] `git diff --check` 无 whitespace error。

---

## 11. Reviewer risk matrix

| Reviewer concern | 可能问题 | 修改策略 | 放置位置 |
|---|---|---|---|
| Is this just a portfolio selector? | 旧 TRACE-SL 叙事残留 | Method/Intro 明确 baselines evaluation only | Intro, Method, README |
| Did you cherry-pick baselines? | 只显示 strongest table | 保留 full baseline matrix + baseline registry | Appendix |
| Did you overclaim all baselines? | “all baselines” 无限定 | 统一 “21 pre-registered non-BiOpt baselines” | 全文 |
| Does theory prove empirical MAE dominance? | posterior trace vs MAE | theory scope remark | Theory, Discussion |
| Is the solver globally optimal? | exchange certificate 被误读 | searched-neighborhood only | Method, Theory, Optimization diagnostics |
| Is robustness really shown? | stress frontier 不总是 TRACE-BiOpt | bounded deployment-stress framing | Robustness |
| Is Stage16 hybrid cherry-picking? | 8/9 promoted, Seattle retained | predefined replacement gate + fail-closed explanation | Experiments, Appendix |
| Can I reproduce the numbers? | artifact path unclear | evidence index + source CSV + script + command | README, Evidence Index |
| Why only 18 pages? | TR-B method paper可能略短 | appendix/supplement 补足 evidence，主文叙事集中 | Paper structure |
| Is code entry clean? | wrapper vs solver mismatch | README/report 诚实说明，或重构 core | Repo docs |

---

## 12. 最终投稿前 checklist

### Scientific claim

- [ ] TRACE-BiOpt 是唯一主方法。
- [ ] Baselines 不进入 solver。
- [ ] Main claim scoped。
- [ ] 21 baselines registry 清楚。
- [ ] 189 Holm-corrected comparisons 清楚。
- [ ] No tied or better challenger 的含义清楚。
- [ ] No universal dominance claim。

### Theory

- [ ] MAP closed form/stability theorem 清楚。
- [ ] Posterior trace risk identity 边界清楚。
- [ ] Generalization theorem 的 independent/block/effective sample size 边界清楚。
- [ ] Exchange certificate 的 searched-neighborhood 边界清楚。
- [ ] CVaR 不被解释成 universal robustness。
- [ ] Theory-to-evidence remark 已添加。

### Results

- [ ] Dominance table 正确。
- [ ] Significance posture table 正确。
- [ ] Full baseline matrix 在 appendix。
- [ ] Provenance table 解释 Stage15/16。
- [ ] Seattle 10% fail-closed 解释清楚。
- [ ] No overclaim in captions。

### Tables/Figures

- [ ] 主文只保留核心表图。
- [ ] Appendix 表格必要且有引用。
- [ ] Supplement 表格在 evidence index 中。
- [ ] 无 undefined labels。
- [ ] 无 moved-to-supplement dead refs。
- [ ] 所有 figure caption 足够自解释。

### Repository

- [ ] README current method 正确。
- [ ] `trace_biopt.py` 定位正确。
- [ ] `RESEARCH_PIPELINE_REPORT.md` 与 README 一致。
- [ ] `SUBMISSION_EVIDENCE_INDEX.md` 最新。
- [ ] current-best evidence artifacts 可见。
- [ ] raw dataset placement 说明清楚。
- [ ] smoke test 命令清楚。
- [ ] refresh command 清楚。

### Submission package

- [ ] main PDF。
- [ ] source files。
- [ ] highlights file。
- [ ] cover letter。
- [ ] declarations。
- [ ] AI declaration。
- [ ] CRediT statement。
- [ ] data availability。
- [ ] author metadata。
- [ ] supplementary file captions。
- [ ] suggested reviewers if needed。

---

## 13. 推荐 issue 分解

可以把这份计划拆成 GitHub issues：

### Issue 1 — Manuscript claim hardening

- 全文替换过强 claim。
- 添加 theory scope remark。
- Robustness 降级成 bounded stress。
- Conclusion 删除 deployable。

### Issue 2 — Table routing cleanup

- 创建 `paper/TABLE_ROUTING_AUDIT.md`。
- 主文、appendix、supplement 三层重排。
- 修 moved-to-supplement refs。
- 编译无 undefined references。

### Issue 3 — Introduction and prose naturalization

- Introduction 删除 meta-review 语气。
- Related Work 减少 contract language。
- Conclusion 改成 transport planning takeaway。

### Issue 4 — Evidence and repository synchronization

- 检查 `SUBMISSION_EVIDENCE_INDEX.md`。
- 修 `RESEARCH_PIPELINE_REPORT.md` wrapper/core 描述。
- 检查 result README。
- 确认 current-best artifacts。

### Issue 5 — Submission package assembly

- highlights。
- cover letter。
- declarations。
- AI statement。
- author metadata。
- data availability。
- source/supplement manifests。

### Issue 6 — Final validation

- run refresh。
- run pytest。
- compile。
- grep overclaim。
- visual PDF check。
- final commit hash in evidence index。

---

## 14. 最终版本应呈现出的论文形态

修改完成后，论文读起来应该是：

1. **一个交通问题**：固定基础设施 sensor siting，目标是 hidden-network recoverability。
2. **一个方法**：TRACE-BiOpt，bilevel reconstruction-aware design。
3. **一个 estimator**：transparent GLS/MAP lower-level inverse problem。
4. **一个 objective**：hidden Huber loss + posterior uncertainty + CVaR tail risk + spatial regularization。
5. **一个 solver**：deterministic scale-adaptive initialization + exchange refinement。
6. **一组理论**：stability、risk identity、generalization、exchange certificate、CVaR interpretation。
7. **一套 evidence**：3 networks × 3 budgets × 10 seeds × 21 baselines。
8. **一个 scoped claim**：189/189 Holm-corrected comparisons，没有 tied/better pre-registered challenger。
9. **明确边界**：非 global optimum、非 universal robustness、非 untested dominance。
10. **清楚复现入口**：current-best evidence index + scripts + data placement + tests。

---

## 15. 最后建议

现在最重要的是“收敛”，不是继续扩张。

不要再新增大量 tables，除非它们直接回答 reviewer 会问的核心问题。不要再新增新 claim，除非 current-best evidence chain、paper table、theory statement、repo index 四处都同步更新。不要把 robustness 或 mechanism probes 抢成主结果。不要让旧 TRACE-SL/RCSS candidate-pool 叙事回到主方法定义里。

最终投稿版本的气质应当是：

> TRACE-BiOpt is a principled, transparent, bilevel transportation network design method for sparse sensor siting, supported by scoped theory and strong multi-network evidence against a pre-registered comparison family.

而不是：

> 我们有很多 audit artifacts，所以请相信这个 winner。

前者更像 TR-B 论文；后者更像内部技术报告。
