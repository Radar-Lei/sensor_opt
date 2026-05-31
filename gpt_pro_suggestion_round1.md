我看了你发的渲染版 PDF。结论很明确：**你对框架图的判断是对的；现在这张 Figure 1 必须换掉。论文主线和结果已经比较强，但版式和图表分层还需要最后一轮硬化，尤其是为了投 TR-B。**

## 1. 框架图：必须换成你指定的那张，而且论文里应明确按这张非 AI 图替换

现在 PDF 第 6 页的 Figure 1 确实还是"代码/脚本生成的流程图"：小字很多、模块边框很硬、视觉上更像 pipeline debug 图，不是你指定要放进论文正文的那张框架图。你说"论文里面的框架图必须替换为那个那个，并不是 AI 生成的"，这个要求需要直接落到正文源码，而不是只停留在建议层。

这次正确的处理方式不是再讨论 AI artwork 风险，而是**直接让论文正文切换到你指定的那张非 AI 框架图**。提交层面仍然只需要满足 Elsevier/TR-B 的常规 artwork 要求：图文件清晰、字号可读、分辨率足够、单独归档即可。([ScienceDirect][1])

建议把论文实际使用的文件固定为：

```text
paper/figures/fig1_trace_biopt_framework_v2.jpg
```

而不是再新起一个 `gptpro` 命名。这样正文、图文件和你指定的版本能保持一一对应。

LaTeX 里应直接插入这张指定图，而不是继续引用脚本导出的老 `pdf/png` 版本：

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.98\linewidth]{figures/fig1_trace_biopt_framework_v2.jpg}
  \caption{
  TRACE-BiOpt framework. The method optimizes a single recoverability-driven
  bilevel sensor-layout objective: a transparent GLS/MAP lower-level reconstruction
  is embedded inside an upper-level hidden-state risk objective with posterior
  uncertainty, tail-risk, and spatial-redundancy terms. Baselines are used only
  for held-out evaluation and do not enter the solver.
  }
  \label{fig:trace-biopt-framework}
\end{figure}
```

这样做有两个直接效果：

1. 论文正文会真正显示你指定的框架图。
2. Figure 1 不再受旧的 code-generated `fig1_trace_biopt_framework_v2.pdf/png` 产物影响。

## 2. 版式总体：主文现在太像"审计包"，不是不能投，但要压缩

你说"很多图表好像都在附录里面"，我看下来实际情况是：核心 Figure 3 和 Figure 4 在正文，full heatmap、layout maps、mechanism diagnostics 等在 Appendix；这个分配方向是对的。但是问题在于，**正文后半部分有大量 table block**，从 Table 1 到 Table 23 连续堆在参考文献之后、Appendix 之前，看起来像"表格附录提前出现了"。

这会给 TR-B reviewer 两个印象：

第一，证据很足；
第二，论文不像一篇正常的 methodological paper，而像一个 audit report。

我建议主文只保留这些：

1. Figure 1：框架图，换成你指定的 GPT Pro 设计稿/人工矢量重绘版。
2. Figure 2：三组网络 case。
3. Figure 3：paired margin forest plot，这个是现在最强的主结果图。
4. Table 6：strongest-challenger dominance table。
5. Table 7：all-baseline Holm-corrected significance posture。
6. 一个 theory summary table 或 exchange/solver diagnostic table，最多保留一个。

其他表，尤其 Table 9–23，建议大部分移到 Appendix 或 Supplement。TR-B/Elsevier 指南也建议表格 sparingly 使用，避免重复正文已经说清楚的结果。([ScienceDirect][1])

## 3. 图面逐项判断

**Figure 1：必须替换。**
当前这张不是你要的框架图，而且图内文字太多。它是最大 P0 问题。

**Figure 2：可以保留。**
网络 case 图基本可用。caption 已经说明 PeMS7_1026 是 distance-matrix embedding，PeMS7_228 和 Seattle 使用地理坐标，这个解释是必要的。

**Figure 3：主结果图很好，应该保留正文。**
现在横轴是 "Strongest non-BiOpt baseline MAE − TRACE-BiOpt MAE"，正值表示 TRACE-BiOpt 更好，这个方向是对的。所有九行都在正值区域，和你的主 claim 强绑定。这个图比普通 MAE curve 更适合 TR-B，因为它直接展示 paired dominance。

**Figure 4：信息有用，但还偏挤。**
上排 objective descent 很好；下排 accepted steps 里的小字标注如 "exchange-only / forward+exchange" 太小，容易显得像脚本输出。建议正文只保留上排 objective descent，accepted-step mix 移 Appendix，或者重画成更简洁的 bar plot。

**Figure A.1 full baseline heatmap：放 Appendix 是对的。**
它太密，不适合正文。但它作为防 cherry-picking 的证据很重要，应该保留 Appendix。

**Figure A.2 strongest-challenger envelope：可保留 Appendix。**
它说明不同 budget 的 strongest challenger 可能不同。caption 已经解释这一点，方向对。

**Figure A.3/A.4：Appendix 合适。**
mechanism-alignment 和 seed-25 heatmap 都是机制诊断，不应抢主文位置。

**Figure A.5/A.6：现在比上一版干净很多。**
sensor maps 和 layout fingerprints 已经没有 debug label。Figure A.5 caption 也说明 dotted edges 只是 visual aids，不是完整 road topology，这个很好。

**Figure A.7/A.8：Appendix 可留，但最好拆页。**
现在两个图挤在最后一页，A.7 的 legend 和 x-label 有点挤。不是致命问题，但投稿版最好拆开。

## 4. Claim 强不强？

**强，但必须 scoped。**

现在最强的 claim 是：

> TRACE-BiOpt 在 PeMS7_228、PeMS7_1026、Seattle 三个网络，10%、20%、30% 三个预算，共九个 dataset-budget regimes 上，相对 21 个 pre-registered non-BiOpt baselines，都取得最低 mean held-out GLS/MAP MAE；Holm-corrected paired tests 后没有 tied 或 better challenger。

这个 claim 是强的。主表里九行全部是 10/10 paired wins，而且 hardest challenger 也没有在 Holm correction 后存活。这个对于 TR-B 来说已经很有说服力。

但不要写这些：

* "beats all baselines"
* "globally optimal"
* "universally robust"
* "dominates all methods"
* "generalizes to all networks"
* "theory proves MAE improvement"

正确写法是：

> against 21 pre-registered non-BiOpt baselines in the tested regimes.

这句话要在 abstract、Introduction、Results、Conclusion 里保持完全一致。

## 5. Contribution 强不强？

**现在 contribution 是够 TR-B 的。**

强点有三个：

第一，问题定位对了。你不是在做"传感器放哪儿覆盖更多点"，而是把 sparse sensor siting 写成 recoverability-driven transportation network design。这个 framing 对 TR-B 是合适的。

第二，方法不是 pool selector。论文已经明确写成一个统一目标：hidden Huber reconstruction loss + posterior uncertainty + CVaR tail risk + spatial redundancy。这个比旧 TRACE-SL/RCSS candidate-pool story 强很多。

第三，有理论支撑。MAP closed form/stability、posterior trace Bayes risk、all-layout validation generalization、exchange certificate、CVaR epigraph，这套理论包足够支撑 methodological contribution。

现在需要避免的问题是：正文里不要反复使用 "audited contract / current-best evidence chain / claim boundary" 这种工程审计语言。保留边界意识是对的，但主文要更像 TR-B 方法论文：交通问题、数学 formulation、算法、理论、结果、机制、限制。

## 6. Methodology 强不强？

**methodology 是强的，但有几个地方要继续守边界。**

强项：

* lower-level GLS/MAP 是透明 inverse problem，不是黑箱模型；
* upper-level objective 直接面向 hidden-state reconstruction；
* baselines 不进入 solver；
* deterministic initialization + exchange refinement 有清楚的 solver 路径；
* exchange certificate 明确说明局部/搜索邻域范围；
* bounded exact-subnetwork benchmark 作为补充证据有价值。

需要守住的边界：

* exchange solver 不是全局 MIP optimum；
* PeMS7_1026 的大网络行仍然是 search-budget-sensitive；
* posterior trace theorem 是 Gaussian squared-error risk identity，不等于真实交通 MAE 必然下降；
* robustness section 不能说 TRACE-BiOpt 在 stress tests 全面赢，因为 bounded stress frontier 里一些 slice 是 graph-spectral baseline 更强；
* exact 27/27 subnetwork result 只能说明 bounded 16-node subnetworks，不代表全网 exact optimality。

这些 caveat 现在正文里基本都有，但 Conclusion 里要特别小心，不要把 exact-subnetwork benchmark 和 full-network stationarity 写得像同一个 guarantee。

## 7. 关于"很多图表在附录"的处理

我建议不要把所有图表搬回正文。相反，**主文应该更少、更强。**

正文主图表应该回答四个问题：

1. 方法是什么？
   Figure 1.

2. 数据网络是什么？
   Figure 2.

3. 是否赢了最强 challenger？
   Figure 3 + Table 6.

4. 是否不是偶然/不是单一 baseline？
   Table 7 或 compact heatmap，二选一。

Appendix 回答 reviewer 的细问：

* full 22-method matrix；
* baseline registry；
* provenance；
* exact subnetwork benchmark；
* solver scale；
* exchange gap；
* weight sensitivity；
* layout maps；
* hidden-node error slices。

这样会更像一篇 TR-B 论文，而不是把所有 audit artifact 都塞进主文。

## 8. 投稿前最小修改清单

按优先级：

1. **替换 Figure 1。** 用你说的 GPT Pro 框架图；投稿版最好人工重绘成矢量图。
2. **停止 code-generated framework 脚本覆盖 Figure 1。**
3. **压缩正文表格。** Table 9–23 大部分移 Appendix/Supplement。
4. **Figure 4 简化。** 正文只保留 objective descent，accepted-step mix 移 Appendix。
5. **Figure A.7/A.8 拆开或增加垂直空间。**
6. **全文统一 claim wording。** 永远写 "21 pre-registered non-BiOpt baselines in tested regimes"。
7. **Conclusion 降一点语气。** 不要让 exact-subnetwork benchmark 听起来像 full-network global certificate。
8. **补投稿材料。** cover letter、highlights、CRediT、declaration of interest、data availability、AI-assisted writing declaration。
9. **确认 abstract ≤250 words、highlights 3–5 条且每条 ≤85 characters。** 你现在 abstract 和 highlights 基本满足这个要求。
10. **如果最终使用任何 AI 生成图像，务必重新核对 Elsevier artwork/GenAI policy。** 这点很关键。([ScienceDirect][1])

## 最终判断

这篇文章的**研究主线、claim、contribution、methodology 都已经够强，可以冲 TR-B**。现在最大的短板不是科学内容，而是 Figure 1 和论文呈现方式。

你现在最该做的不是再加实验，而是：

> 换掉框架图，压缩正文图表，把 audit 证据放到 Appendix/Supplement，保持 scoped claim，然后补齐投稿材料。

修完这些，我认为就可以进入 TR-B 投稿前最后格式检查阶段。

[1]: https://www.sciencedirect.com/journal/transportation-research-part-b-methodological/publish/guide-for-authors "Guide for authors - Transportation Research Part B: Methodological - ISSN 0191-2615 | ScienceDirect.com by Elsevier"
