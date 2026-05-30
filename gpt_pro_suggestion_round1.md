你这个担心是对的。**框架图现在应该优先重画；Numerical Experiments 也应该补一张“三个网络案例 + sensor-budget 示意”的图。** 当前仓库里已经有 `fig1_workflow.pdf` 和 `fig_trace_biopt_sensor_maps.pdf`，但现有 sensor map 更像 10% low-budget 的结果/对比图，不是实验设置图。仓库 figures 目录现在确实已有 workflow、sensor maps、paired margins、heatmap 等图。([GitHub][1]) 现有 `generate_trace_biopt_sensor_map_figure.py` 也是 “current-best low-budget sensor layout maps”，并且只取 10% low-budget rows。([GitHub][2])

我建议这样处理：

**框架图不要用 GPT Image 作为最终稿。** 可以用 GPT Image 做视觉草图，但最终论文图最好用可复现的矢量图，因为图中文字、公式、箭头关系必须准确；图生成模型很容易把公式、labels、箭头方向弄错。尤其你的核心叙事是：TRACE-BiOpt 是单一 bilevel objective + deterministic solver，不是 baseline pool selector，这个必须在框架图里非常清楚。这个方向也和前面已经定下来的“不要再写成 pool”的主线一致。

我已经直接给你做了两份可落地文件。

## 1. 新框架图：我建议替换现在的 Figure 1

预览图和脚本在这里：

[下载框架图 PDF](sandbox:/mnt/data/paper/figures/fig1_trace_biopt_framework_v2.pdf)
[下载框架图 PNG](sandbox:/mnt/data/paper/figures/fig1_trace_biopt_framework_v2.png)
[下载生成脚本](sandbox:/mnt/data/generate_trace_biopt_framework_figure_v2.py)

这张图的结构是：

左侧：traffic network data + deployment decision
中间：TRACE-BiOpt 的唯一目标和 solver
右侧：selected sensor layout + held-out evaluation + scoped claim
底部：baseline registry，只用虚线接到 evaluation，不接到 solver

这个设计的好处是，它直接消除了 “是不是从 baseline pool 里挑最优” 的误解。

放进仓库后运行：

```bash
cp /mnt/data/generate_trace_biopt_framework_figure_v2.py scripts/

python scripts/generate_trace_biopt_framework_figure_v2.py --root .
```

LaTeX 可以这样替换原 Figure 1：

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig1_trace_biopt_framework_v2.pdf}
  \caption{
  TRACE-BiOpt framework. The method optimizes a single recoverability-driven
  bilevel sensor-layout objective: a transparent GLS/MAP lower-level
  reconstruction is embedded inside an upper-level hidden-state risk objective
  with posterior-uncertainty, tail-risk, and spatial-redundancy terms. Baselines
  are used only for held-out evaluation and do not enter the solver.
  }
  \label{fig:trace-biopt-framework}
\end{figure}
```

## 2. Numerical Experiments 应该补一张网络案例图

这里我建议补两张，主文至少放第一张，第二张可主文也可 appendix。

第一张是 **Experiment network cases**：一行三个网络，PeMS7_1026、PeMS7_228、Seattle。它回答 reviewer 的直观问题：你到底在哪些网络上做实验？

第二张是 **Sensor-budget illustration**：3 个网络 × 3 个 budget，10%、20%、30%。灰色点是候选节点，绿色点是安装 sensor 的节点。这里要注意一个表达问题：**10% budget 通常表示 10% 节点有 sensors，不是 10% 节点没有 sensors；没有 sensors 的节点其实是 90%。** 所以图注里建议写 “10% sensors installed; remaining nodes are hidden/uninstrumented”。

我也给你写了脚本：

[下载网络与 budget 图脚本](sandbox:/mnt/data/generate_trace_biopt_network_budget_panels.py)

放到仓库：

```bash
cp /mnt/data/generate_trace_biopt_network_budget_panels.py scripts/
```

如果你只是想在 Numerical Experiments 里解释 sensor budget，不想把它说成 TRACE-BiOpt 的结果，运行这个：

```bash
python scripts/generate_trace_biopt_network_budget_panels.py \
  --root . \
  --mask-source random \
  --highlight sensors
```

它会生成：

```text
paper/figures/fig_network_case_overview.pdf
paper/figures/fig_network_case_overview.png
paper/figures/fig_sensor_budget_panels.pdf
paper/figures/fig_sensor_budget_panels.png
```

如果你想画 actual TRACE-BiOpt representative layouts，用这个：

```bash
python scripts/generate_trace_biopt_network_budget_panels.py \
  --root . \
  --mask-source trace \
  --layout-seed 25 \
  --highlight sensors
```

如果你确实想强调“哪些节点没有 sensor”，用这个：

```bash
python scripts/generate_trace_biopt_network_budget_panels.py \
  --root . \
  --mask-source random \
  --highlight hidden
```

不过我更建议主文默认高亮 **installed sensors**，不要高亮 “no sensor nodes”，因为 10% budget 下无 sensor 节点太多，视觉上会变成一大片红点，反而不清楚。

## 3. 这两张网络图的论文放置建议

我建议 Numerical Experiments 里这样安排：

**Figure 2 或 Figure 3：Experiment network cases**

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig_network_case_overview.pdf}
  \caption{
  Network cases used in the numerical experiments. PeMS7\_228 and Seattle are
  shown using available geographic station/cabinet coordinates, while
  PeMS7\_1026 is shown using a spectral embedding of its distance matrix for
  visualization. Each point is a candidate sensor location.
  }
  \label{fig:network-cases}
\end{figure}
```

**Appendix 或主文小图：Sensor budget illustration**

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig_sensor_budget_panels.pdf}
  \caption{
  Sensor-budget illustration for the three experiment networks. Highlighted
  nodes denote installed sensors under 10\%, 20\%, and 30\% budgets; grey nodes
  denote candidate locations that remain hidden/uninstrumented. The random-mask
  version is illustrative only and is not used as a performance result.
  }
  \label{fig:sensor-budget-illustration}
\end{figure}
```

如果你用 `--mask-source trace`，caption 最后一半改成：

```latex
The displayed layouts are representative TRACE-BiOpt selections for split seed 25.
```

## 4. 主文里怎么取舍

我建议最终主文图顺序改成：

1. **Framework figure**：用我给的 `fig1_trace_biopt_framework_v2.pdf` 替换原框架图。
2. **Network cases figure**：三个实验网络一行三图。
3. **Main result figure/table**：paired margin forest 或 dominance table。
4. **Solver/mechanism figure**：objective descent 或 exchange gap。

Sensor-budget 3×3 图如果版面紧，可以放 appendix；但 Numerical Experiments 里至少要有三网络 overview 图。这样 reviewer 读到实验设置时不会觉得 PeMS/Seattle 都只是名字，没有空间直觉。

总体上：**框架图用可复现矢量图，不用最终 AI 图；网络/预算图用代码从真实数据和布局文件生成。** 这两处修完，论文视觉质量会明显更像正式 TR-B manuscript，而不是内部 evidence report。

[1]: https://github.com/Radar-Lei/sensor_opt/tree/main/paper/figures "https://github.com/Radar-Lei/sensor_opt/tree/main/paper/figures"
[2]: https://github.com/Radar-Lei/sensor_opt/blob/main/scripts/generate_trace_biopt_sensor_map_figure.py "https://github.com/Radar-Lei/sensor_opt/blob/main/scripts/generate_trace_biopt_sensor_map_figure.py"


According to a document from 2026-05-29，我的判断是：**现在这个版本基本“差不多了”，研究主线、证据链和仓库叙事已经接近可投；剩下主要不是再发明方法或补大实验，而是最后的 submission hardening，以及把图做得更像 TR-B 主文图。** 最新审查文件也明确说，目前重点已经转为“投稿硬化、删冗余表、统一 claim wording、清理复现入口和补齐投稿材料”，而不是继续改方法。

## 1. 目前版本是否差不多了？

**结论：可以进入投稿前最后封口阶段。**

我看下来，现在最关键的几个旧问题已经明显改善：

第一，仓库主叙事已经对齐。README 现在把项目直接定义为 **TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design**，并明确当前 TR-B 稿件的方法是 TRACE-BiOpt，而不是 TRACE-SL/RCSS candidate-pool selector；旧 TRACE-SL/RCSS 被定位成 historical baseline / diagnostic comparator。这个很重要，因为它消除了之前“论文说 BiOpt、仓库像旧 TRACE-SL”的最大不一致。([GitHub][1])

第二，current-best evidence 目录现在是可见且成体系的。`current_best_trace_biopt_evidence/` 下已经包含 dominance、best-baseline delta、claim contract、provenance、significance、exact subnetwork、exchange gap、full baseline matrix、paired margin、performance curves 等 artifact；`SUBMISSION_EVIDENCE_INDEX.md` 也已经把 figure/table、source CSV、generation script、input stage 和 status 映射起来。([GitHub][2])

第三，主结果 claim 现在可以站住，但要保持 scoped。当前证据支持的是：PeMS7_228、PeMS7_1026、Seattle，10%/20%/30% budgets，十个 split seeds，21 个 pre-registered non-BiOpt baselines；9/9 dataset-budget rows 上 TRACE-BiOpt 都是 lowest mean held-out GLS/MAP MAE，并且 paired status 是 10/10。Seattle 10% 仍是 Stage15 retained row，但 evidence index 已经解释它是 fail-closed retained，并给出完整 ten-seed 和显著性证据。([GitHub][3])

第四，paper pipeline report 也已经从之前的 “Submission-ready: no” 更新到 **Submission-ready: yes, post-hardening draft**，并且 proof audit、claim audit、citation audit、kill-argument audit、verifier、LaTeX 编译、pytest、py_compile 都是通过状态。剩下的问题主要是作者信息、affiliations、declarations、portal-specific files，以及可能还需要独立读者读一遍。([GitHub][4])

所以我会这样定性：

> **方法和主结果已经够；论文/仓库已经基本同步；现在不建议再大改方法或继续盲目加实验。最后要做的是：删噪、控 claim、补投稿材料、把主图换成更 reviewer-facing 的表达。**

主文 claim 建议固定为这一版，不要再扩大：

> TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered non-BiOpt baselines across all nine tested dataset-budget regimes, and no pre-registered challenger remains tied or better after Holm-corrected paired tests over the current-best comparison family.

不要写 “beats all baselines” 或 “globally optimal”；也不要暗示 robust stress tests 里 TRACE-BiOpt 全面支配，因为 robustness 只能作为 bounded deployment-stress discussion。

## 2. 投稿前还要最后检查什么？

我建议只做 5 个小封口：

1. **全文搜索 claim 词。**
   搜索 `all baselines`, `globally`, `robust`, `Stage15`, `directional`, `awaits`, `candidate pool`, `TRACE-SL main`。凡是没有 scoped qualifier 的都改掉。

2. **主文减少 audit-contract 语言。**
   现在仓库 evidence 很强，但论文主文不要显得像审计报告。Introduction / Related Work / Conclusion 中 “contract / audited / evidence chain” 这类词保留一次即可。你之前的审查意见也建议把 evidence tables 分层：主文只留 4–6 个 reviewer-facing 图表，appendix 留 full matrix/provenance/baseline registry/claim boundary/exact/exchange/solver scale/weight sensitivity，repo/supplement 放大量 audit posture 表。

3. **保留 Seattle 10% provenance，但不要在主文展开太多。**
   主文一句话：current-best evidence combines Stage16 promoted rows with fail-closed retained Seattle 10% Stage15 evidence. 详细解释放 appendix/evidence index。

4. **投稿材料补齐。**
   cover letter、highlights、declaration of interest、CRediT author statement、data availability statement、generative AI declaration。Elsevier/TR-B 对 abstract、highlights、tables/figures 都有格式要求，尤其 abstract ≤250 words、highlights 3–5 条且每条 ≤85 characters。([ScienceDirect][5])

5. **让一个交通/OR 方向读者快速读。**
   只给他 abstract、intro、method、main result figure/table、limitations。目标是 10 分钟内能说清楚：这是一个 sparse traffic sensor siting 的 bilevel network design 方法，而不是 benchmark selector。

## 3. 作图方面：现在已有图够多，但主图可以更好

仓库现在已经有很多图：workflow、main MAE、current-best curves、calibration alignment、exchange gap curves、full baseline heatmap、hidden error heatmaps、layout fingerprints、objective descent、objective mix、paired margins、sensor maps 等；scripts 目录也已经有对应的生成脚本。([GitHub][6])

但我建议不要“继续加很多图”，而是把主文图换成更直击 claim 的图。现在最适合 TR-B 主文的是：

### 主文 Figure 1：Method workflow

保留。它解释 bilevel upper/lower level、GLS/MAP estimator、objective terms、exchange refinement。这个是方法论文必须有的。

### 主文 Figure 2：Paired margin forest / lollipop plot

这是我最建议新增或替换的主结果图。不要只画 TRACE-BiOpt 和 best baseline 的 MAE 曲线，而是直接画：

[
\Delta = \text{MAE}*{\text{strongest challenger}}-\text{MAE}*{\text{TRACE-BiOpt}}
]

每个 dataset-budget 一行，点是 mean paired margin，横线是 95% CI，右侧标注 strongest challenger 和 10/10 wins。这样 reviewer 一眼能看出：所有 margin 都在 0 右侧，claim 是 paired dominance，不是肉眼看均值。

### 主文 Figure 3：Compact baseline heatmap

不要把 22 个方法的 full matrix 全塞主文。主文只放 TRACE-BiOpt + top 6–8 strongest challengers，按 average rank 排列；full 22-method matrix 放 appendix。这样能防 cherry-picking，又不会让主文像审计表格库。

### 主文 Figure 4：Solver diagnostic

用 objective descent 或 exchange-gap curve。这个图服务于“这是一个 deterministic solver under one objective”，不是 pool selector。它比 sensor map 更能支撑方法贡献。

### Appendix figures

Seed-level paired margin strip plot、full baseline matrix、sensor maps、hidden error heatmaps、layout fingerprints、robustness routing、weight sensitivity。Sensor maps 如果视觉质量很高可以进主文；否则 appendix 更稳。

## 4. 我给你写了一个可直接放进仓库的作图脚本

完整脚本在这里：

[generate_trace_biopt_submission_figures_v2.py](sandbox:/mnt/data/generate_trace_biopt_submission_figures_v2.py)

建议放到仓库：

```bash
cp /mnt/data/generate_trace_biopt_submission_figures_v2.py scripts/

python scripts/generate_trace_biopt_submission_figures_v2.py
```

如果你从其他目录运行：

```bash
python scripts/generate_trace_biopt_submission_figures_v2.py --root .
```

它默认读取：

```text
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
```

并输出到：

```text
paper/figures/
```

会生成这四组 PDF/PNG：

```text
fig_trace_biopt_margin_forest_v2.pdf
fig_trace_biopt_seed_margins_v2.pdf
fig_trace_biopt_compact_baseline_heatmap_v2.pdf
fig_trace_biopt_submission_panel_v2.pdf
```

其中我最建议进主文的是：

```text
fig_trace_biopt_margin_forest_v2.pdf
```

它比普通 bar plot 更适合你的 claim，因为它直接展示 “TRACE-BiOpt vs strongest challenger” 的 paired margin 和不确定性。

LaTeX 可以这样插：

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig_trace_biopt_margin_forest_v2.pdf}
  \caption{
  Paired held-out GLS/MAP MAE margins between the strongest pre-registered
  non-BiOpt challenger and TRACE-BiOpt. Positive values indicate that
  TRACE-BiOpt has lower error. Error bars show approximate 95\% confidence
  intervals over the ten split seeds. All nine tested dataset--budget regimes
  favor TRACE-BiOpt under the current-best evidence chain.
  }
  \label{fig:trace-biopt-margin-forest}
\end{figure}
```

Appendix 可以插：

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig_trace_biopt_seed_margins_v2.pdf}
  \caption{
  Seed-level paired MAE margins against the row-wise strongest challenger.
  Each marker is one split seed. Positive values indicate lower held-out
  GLS/MAP MAE for TRACE-BiOpt.
  }
  \label{fig:trace-biopt-seed-margins}
\end{figure}
```

## 5. 最终建议

**现在不要再把精力放在“方法还要不要更强”上。** 方法身份已经清楚：TRACE-BiOpt 是单一 bilevel reconstruction-aware network design 方法，不是 candidate pool；证据也已经足够支撑 scoped TR-B claim。更早的设计建议里就强调过，核心是保持 “Bilevel MAP reconstruction + Huber hidden-state risk + posterior uncertainty + CVaR tail risk + deterministic exchange refinement” 这个唯一方法，而不是回到 pool 叙事。

接下来最值钱的是两件事：

**第一，把主文压成“方法论文”的气质。** 少一些 audit-contract 语言，多一些 transportation network design、inverse problem、bilevel optimization、solver certificate。

**第二，把主结果图换成 paired margin forest plot。** 这张图会比大表、全 baseline heatmap、普通 MAE 曲线更直接地说服 reviewer：你的 claim 是有十个 split seed支撑的、row-wise strongest challenger comparison，而不是挑了几个好看的 baseline。

[1]: https://github.com/Radar-Lei/sensor_opt "https://github.com/Radar-Lei/sensor_opt"
[2]: https://github.com/Radar-Lei/sensor_opt/tree/main/TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence "https://github.com/Radar-Lei/sensor_opt/tree/main/TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence"
[3]: https://github.com/Radar-Lei/sensor_opt/blob/main/SUBMISSION_EVIDENCE_INDEX.md "https://github.com/Radar-Lei/sensor_opt/blob/main/SUBMISSION_EVIDENCE_INDEX.md"
[4]: https://github.com/Radar-Lei/sensor_opt/blob/main/paper/PAPER_WRITING_PIPELINE_REPORT.md "https://github.com/Radar-Lei/sensor_opt/blob/main/paper/PAPER_WRITING_PIPELINE_REPORT.md"
[5]: https://www.sciencedirect.com/journal/transportation-research-part-b-methodological/publish/guide-for-authors "https://www.sciencedirect.com/journal/transportation-research-part-b-methodological/publish/guide-for-authors"
[6]: https://github.com/Radar-Lei/sensor_opt/tree/main/paper/figures "https://github.com/Radar-Lei/sensor_opt/tree/main/paper/figures"
