#!/usr/bin/env python3
"""Generate a TR Part B CAS manuscript draft from TRACE-SL paper sources."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
TEMPLATE_DIR = ROOT / "els-cas-templates"
PAPER_DIR = ROOT / "paper"
FIG_DIR = ROOT / "figures"


METHOD_LABELS = {
    "validation_swap_selected": "TRACE-SL",
    "rcss_selected": "RCSS selected",
    "multistart_swap_by_validation": "Multistart swap",
    "best_random_by_validation": "Best random by validation",
    "random": "Random mean",
    "top_variance": "Top variance",
    "greedy_a_trace": "Greedy A-trace",
    "greedy_d_logdet": "Greedy logdet",
    "observability_proxy": "Observability proxy",
    "graph_sampling_laplacian": "Graph sampling",
    "qr_pod_modes": "QR/POD",
    "scenario_cvar_a_trace": "Scenario CVaR trace",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def fmt_num(value: str | float, digits: int = 3) -> str:
    if value in ("", None):
        return "--"
    return f"{float(value):.{digits}f}"


def fmt_p(value: str) -> str:
    if not value:
        return "--"
    x = float(value)
    if x < 1e-4:
        return f"{x:.1e}"
    return f"{x:.4f}"


def pct_budget(value: str | float) -> str:
    return f"{int(round(float(value) * 100))}\\%"


def tex_escape(text: str) -> str:
    return (
        text.replace("&", r"\&")
        .replace("%", r"\%")
        .replace("_", r"\_")
        .replace("#", r"\#")
    )


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def main_rows() -> list[dict[str, str]]:
    rows = read_csv(PAPER_SOURCES / "core_performance_table.csv")
    ablation_rows = read_csv(PAPER_SOURCES / "ablation_contract.csv")
    keep = {
        "validation_swap_selected",
        "best_random_by_validation",
        "random",
        "top_variance",
        "greedy_a_trace",
        "observability_proxy",
        "graph_sampling_laplacian",
        "qr_pod_modes",
        "multistart_swap_by_validation",
    }
    out = [r for r in rows if r["layout_type"] in keep]
    existing = {(r["budget"], r["layout_type"]) for r in out}
    for row in ablation_rows:
        key = (row["budget"], row["layout_type"])
        if row["layout_type"] in keep and key not in existing:
            out.append(
                {
                    "budget": row["budget"],
                    "layout_type": row["layout_type"],
                    "mean": row["test_mae_mean"],
                    "std": row.get("test_mae_std", ""),
                    "count": row.get("actual_split_count", ""),
                }
            )
            existing.add(key)
    return out


def pivot_main_table() -> dict[float, dict[str, dict[str, str]]]:
    out: dict[float, dict[str, dict[str, str]]] = {}
    for row in main_rows():
        out.setdefault(float(row["budget"]), {})[row["layout_type"]] = row
    return out


def external_main_rows() -> list[dict[str, str]]:
    rows = read_csv(PAPER_SOURCES / "external_evidence_contract.csv")
    return [r for r in rows if r["table_role"] == "main_method"]


def paired_vs_random_rows() -> list[dict[str, str]]:
    rows = read_csv(PAPER_SOURCES / "paired_delta_table.csv")
    return [
        r
        for r in rows
        if r["layout"] == "validation_swap_selected"
        and r["baseline"] in {"best_random_by_validation", "random", "top_variance"}
    ]


def write_plan() -> None:
    plan = """# Paper Plan

**Title**: TRACE-SL: Reconstruction-Aware Sensor Layout Design for Traffic State Estimation
**Venue**: Transportation Research Part B: Methodological (Elsevier CAS template)
**Type**: Method + empirical + scoped theory
**Date**: 2026-05-26
**Page budget**: Full journal manuscript, targeting 12-14 pages before appendix
**Section count**: 8 main sections plus appendix

## Claims-Evidence Matrix

| Claim | Evidence | Status | Section |
|-------|----------|--------|---------|
| TRACE-SL formulates sparse traffic sensing as reconstruction-aware hidden-network design rather than counting-point coverage alone. | `claim_contract.json`, `theory_statement_contract.json`, method implementation | Supported | §1, §3 |
| The posterior-trace certificate is a principled squared-error uncertainty proxy under a scoped linear-Gaussian GLS/MAP model. | `theory_statement_contract.json`, `transparent_estimator_eval.py` | Supported with assumptions | §4 |
| Validation-aware TRACE-SL improves held-out GLS/MAP reconstruction on PeMS7_228 against reviewer-facing baselines. | `core_performance_table.csv`, `paired_delta_table.csv` | Supported | §5 |
| PeMS7_1026 and Seattle provide multi-network empirical evidence but not universal generalization proof. | `external_evidence_contract.csv`, `external_evidence_gate.json` | Supported with caveat | §5 |
| Candidate generation, validation selection, and validation-aware swap each have distinct roles. | `ablation_contract.csv` | Supported | §6 |
| Robustness evidence is stress-test evidence, not global robustness certification. | `robustness_condition_table.csv`, claim contract | Bounded | §6, §7 |

## Structure

### §0 Abstract
- Problem: fixed sparse sensors are often chosen for coverage or observability, not for hidden-network reconstruction quality.
- Approach: TRACE-SL combines transparent GLS/MAP reconstruction with posterior certificates, validation selection, and local swap refinement.
- Key result: on PeMS7_228, TRACE-SL reduces held-out MAE relative to validation-selected random layouts by 0.123, 0.095, and 0.163 at 10%, 20%, and 30% budgets.
- Implication: the layout problem can be treated as transparent reconstruction-aware network design.

### §1 Introduction
- Open with the cost and permanence of traffic sensor deployments.
- Gap: classical count-location formulations do not directly optimize full-network state reconstruction.
- Contributions: formulation, TRACE-SL algorithm, scoped theory bridge, multi-network evidence, reproducible claim routing.

### §2 Related Work
- Traffic counting and detector location.
- Sensor selection and optimal experimental design.
- Graph signal sampling and sparse reconstruction.
- Traffic state estimation and black-box forecasting.

### §3 Reconstruction-Aware Layout Problem
- Define graph, candidate sensors, hidden complement, train/validation/test split, transparent reconstructors.
- Present the budgeted design objective and evidence discipline.

### §4 TRACE-SL Method
- Candidate generation, posterior/scenario certificates, validation-tuned scoring, validation-aware one-swap refinement.
- State scoped posterior trace identity, monotonicity, local optimality, and workload complexity.

### §5 Experimental Design and Main Results
- Datasets, budgets, baselines, metrics, and Stage12 protocol.
- Main PeMS7_228 table and paired tests.
- External PeMS7_1026 and Seattle evidence.

### §6 Ablations and Robustness
- Random pool, validation-selected random, certificate-only candidates, RCSS, validation-swap, multistart.
- Robustness and stress-test routing.

### §7 Discussion and Limitations
- Interpret why reconstruction-aware design helps.
- Preserve multistart and non-universal-generalization caveats.

### §8 Conclusion
- Summarize reconstruction-aware sensor layout design and scoped evidence.

## Figure Plan

| ID | Type | Description | Data Source | Priority |
|----|------|-------------|-------------|----------|
| Fig 1 | Workflow | TRACE-SL train/validation/test and candidate-to-layout pipeline | generated | HIGH |
| Fig 2 | Line plot | PeMS7_228 held-out MAE across budgets for main baselines | `core_performance_table.csv` | HIGH |
| Table 1 | Main table | PeMS7_228 Stage12 mean MAE and paired p-values | `core_performance_table.csv`, `paired_delta_table.csv` | HIGH |
| Table 2 | External table | PeMS7_1026 and Seattle main-method MAE across budgets | `external_evidence_contract.csv` | HIGH |
| Table 3 | Ablation table | Component-layer comparison on PeMS7_228 | `ablation_contract.csv` | HIGH |
| Table 4 | Theory table | Scoped statements and non-claim boundaries | `theory_statement_contract.csv` | MEDIUM |

## Citation Plan

- §1-§2 traffic counting location: `yang1998optimal`.
- §2 sensor selection/design: `joshi2009sensor`, `krause2008near`.
- §2 graph sampling/reconstruction: `chen2015sampling`, `anis2016sampling`, `manohar2018sparse`.
- §2 traffic forecasting context: `li2018dcrnn`, `yu2018stgcn`.

## Reviewer Feedback

Inline planning review: the draft should avoid claiming global optimality, certified robustness, or universal cross-network generalization. The paper should sell the TR Part B contribution as reconstruction-aware network design with transparent inverse-problem evidence, not as another black-box traffic imputation benchmark.

## Next Steps

- [x] Generate figures and tables.
- [x] Draft CAS LaTeX.
- [ ] Compile PDF.
- [ ] Run improvement loop.
- [ ] Run submission audits.
"""
    write(ROOT / "PAPER_PLAN.md", plan)


def generate_figures() -> None:
    FIG_DIR.mkdir(exist_ok=True)
    style = """import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({
    "font.size": 9,
    "font.family": "serif",
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.04,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})
COLORS = plt.cm.tab10.colors
"""
    write(FIG_DIR / "paper_plot_style.py", style)

    # Generate method workflow and main performance plots.
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    plt.rcParams.update(
        {
            "font.size": 9,
            "font.family": "serif",
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    fig, ax = plt.subplots(figsize=(7.0, 2.2))
    ax.axis("off")
    labels = [
        ("Train", "Estimate priors, graph,\nprecision and scales"),
        ("Candidates", "A/D trace, CVaR,\ncoverage, random"),
        ("Validate", "Tune score and\nswap by val MAE"),
        ("Freeze", "Fix layout rule\nbefore test"),
        ("Test", "Hidden-network\nGLS/MAP MAE"),
    ]
    for i, (title, body) in enumerate(labels):
        x = 0.02 + i * 0.195
        rect = patches.FancyBboxPatch(
            (x, 0.25),
            0.16,
            0.5,
            boxstyle="round,pad=0.02,rounding_size=0.02",
            linewidth=1.0,
            edgecolor="#2f4b7c",
            facecolor="#eef3f8",
        )
        ax.add_patch(rect)
        ax.text(x + 0.08, 0.62, title, ha="center", va="center", weight="bold")
        ax.text(x + 0.08, 0.43, body, ha="center", va="center", fontsize=8)
        if i < len(labels) - 1:
            ax.annotate(
                "",
                xy=(x + 0.185, 0.5),
                xytext=(x + 0.165, 0.5),
                arrowprops=dict(arrowstyle="->", lw=1.0, color="#444444"),
            )
    ax.text(
        0.5,
        0.08,
        "TRACE-SL separates model fitting, validation-based layout selection, and held-out deployment evaluation.",
        ha="center",
        va="center",
        fontsize=8,
    )
    fig.savefig(FIG_DIR / "fig1_workflow.pdf")
    plt.close(fig)

    pivot = pivot_main_table()
    methods = [
        "validation_swap_selected",
        "best_random_by_validation",
        "random",
        "top_variance",
        "greedy_a_trace",
    ]
    fig, ax = plt.subplots(figsize=(5.8, 3.0))
    budgets = sorted(pivot)
    for idx, method in enumerate(methods):
        ys = [float(pivot[b][method]["mean"]) for b in budgets]
        ax.plot(
            [b * 100 for b in budgets],
            ys,
            marker="o",
            label=METHOD_LABELS[method],
            color=plt.cm.tab10.colors[idx],
        )
    ax.set_xlabel("Sensor budget (% of candidate nodes)")
    ax.set_ylabel("Held-out GLS/MAP MAE")
    ax.set_xticks([10, 20, 30])
    ax.legend(frameon=False, ncol=2)
    fig.savefig(FIG_DIR / "fig2_main_mae.pdf")
    plt.close(fig)


def table_main_results() -> str:
    pivot = pivot_main_table()
    paired = {
        (float(r["budget"]), r["baseline"]): r for r in paired_vs_random_rows()
    }
    methods = [
        "validation_swap_selected",
        "best_random_by_validation",
        "random",
        "top_variance",
        "greedy_a_trace",
        "observability_proxy",
        "graph_sampling_laplacian",
        "qr_pod_modes",
        "multistart_swap_by_validation",
    ]
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\caption{PeMS7\_228 Stage12 held-out GLS/MAP MAE. Lower is better. Paired $p$ values compare TRACE-SL with the listed baseline on the same ten splits.}",
        r"\label{tab:main-results}",
        r"\small",
        r"\begin{tabular}{lccc}",
        r"\toprule",
        r"Layout & 10\% & 20\% & 30\% \\",
        r"\midrule",
    ]
    for method in methods:
        vals = []
        for b in sorted(pivot):
            row = pivot[b].get(method)
            if row:
                vals.append(fmt_num(row["mean"]))
            else:
                vals.append("--")
        label = METHOD_LABELS.get(method, method)
        if method == "validation_swap_selected":
            label = r"\textbf{TRACE-SL}"
            vals = [rf"\textbf{{{v}}}" for v in vals]
        lines.append(f"{label} & " + " & ".join(vals) + r" \\")
    lines += [
        r"\midrule",
        r"$p$ vs. best random & "
        + " & ".join(fmt_p(paired[(b, "best_random_by_validation")]["paired_t_p"]) for b in sorted(pivot))
        + r" \\",
        r"$p$ vs. random mean & "
        + " & ".join(fmt_p(paired[(b, "random")]["paired_t_p"]) for b in sorted(pivot))
        + r" \\",
        r"$p$ vs. top variance & "
        + " & ".join(fmt_p(paired[(b, "top_variance")]["paired_t_p"]) for b in sorted(pivot))
        + r" \\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table*}",
    ]
    return "\n".join(lines)


def table_external() -> str:
    rows = sorted(external_main_rows(), key=lambda r: (r["dataset"], float(r["budget"])))
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{External Stage12 evidence. TRACE-SL is evaluated on ten splits for each dataset and budget.}",
        r"\label{tab:external}",
        r"\small",
        r"\begin{tabular}{lccc}",
        r"\toprule",
        r"Dataset & Budget & MAE & Splits \\",
        r"\midrule",
    ]
    for r in rows:
        lines.append(
            f"{tex_escape(r['dataset'])} & {pct_budget(r['budget'])} & {fmt_num(r['test_mae_mean'])} & {r['actual_split_count']} " + r"\\"
        )
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(lines)


def table_ablation() -> str:
    rows = read_csv(PAPER_SOURCES / "ablation_contract.csv")
    keep = [
        r
        for r in rows
        if r["budget"] == "0.3"
        and r["layout_type"]
        in {
            "random",
            "best_random_by_validation",
            "greedy_a_trace",
            "rcss_selected",
            "validation_swap_selected",
            "multistart_swap_by_validation",
        }
    ]
    order = {
        "random": 0,
        "best_random_by_validation": 1,
        "greedy_a_trace": 2,
        "rcss_selected": 3,
        "validation_swap_selected": 4,
        "multistart_swap_by_validation": 5,
    }
    keep.sort(key=lambda r: order[r["layout_type"]])
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Component ablation at the 30\% PeMS7\_228 budget. Lower MAE is better.}",
        r"\label{tab:ablation}",
        r"\small",
        r"\begin{tabular}{llc}",
        r"\toprule",
        r"Layout & Component role & MAE \\",
        r"\midrule",
    ]
    for r in keep:
        lines.append(
            f"{METHOD_LABELS.get(r['layout_type'], r['layout_type'])} & "
            f"{tex_escape(r['component_layer'].replace('_', ' '))} & {fmt_num(r['test_mae_mean'])} "
            + r"\\"
        )
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(lines)


def table_theory() -> str:
    rows = read_csv(PAPER_SOURCES / "theory_statement_contract.csv")
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\caption{Scoped theoretical statements used in the manuscript. Each statement is intentionally bounded by its assumptions and non-claim boundary.}",
        r"\label{tab:theory}",
        r"\small",
        r"\begin{tabular}{p{0.18\textwidth}p{0.39\textwidth}p{0.34\textwidth}}",
        r"\toprule",
        r"Statement & Scoped content & Non-claim boundary \\",
        r"\midrule",
    ]
    for r in rows:
        lines.append(
            f"{tex_escape(r['statement_name'].replace('_', ' '))} & "
            f"{tex_escape(r['scoped_statement'])} & "
            f"{tex_escape(r['non_claim_boundaries'])} "
            + r"\\"
        )
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table*}"]
    return "\n".join(lines)


def generate_tables() -> None:
    tables = {
        "table_main_results.tex": table_main_results(),
        "table_external.tex": table_external(),
        "table_ablation.tex": table_ablation(),
        "table_theory.tex": table_theory(),
    }
    for name, content in tables.items():
        write(FIG_DIR / name, content)
    includes = r"""% Auto-generated snippets for TRACE-SL TR Part B draft.

\begin{figure}[t]
\centering
\includegraphics[width=\textwidth]{figures/fig1_workflow.pdf}
\caption{TRACE-SL workflow. The design protocol separates training-derived reconstruction ingredients, validation-based layout selection, and held-out deployment evaluation.}
\label{fig:workflow}
\end{figure}

\begin{figure}[t]
\centering
\includegraphics[width=0.95\linewidth]{figures/fig2_main_mae.pdf}
\caption{Held-out PeMS7\_228 GLS/MAP reconstruction MAE across sensor budgets. TRACE-SL refers to the validation-aware selected layout.}
\label{fig:main-mae}
\end{figure}

\input{tables/table_main_results}
\input{tables/table_external}
\input{tables/table_ablation}
\input{tables/table_theory}
"""
    write(FIG_DIR / "latex_includes.tex", includes)


def setup_paper_dir() -> None:
    if PAPER_DIR.exists():
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = ROOT / f"paper-backup-{stamp}"
        shutil.move(str(PAPER_DIR), str(backup))
    (PAPER_DIR / "sections").mkdir(parents=True)
    (PAPER_DIR / "figures").mkdir()
    (PAPER_DIR / "tables").mkdir()
    (PAPER_DIR / ".aris").mkdir()
    write(PAPER_DIR / ".aris" / "assurance.txt", "submission")
    for name in ["cas-sc.cls", "cas-common.sty", "cas-model2-names.bst"]:
        shutil.copy2(TEMPLATE_DIR / name, PAPER_DIR / name)
    for path in FIG_DIR.glob("*.pdf"):
        shutil.copy2(path, PAPER_DIR / "figures" / path.name)
    for path in FIG_DIR.glob("table_*.tex"):
        shutil.copy2(path, PAPER_DIR / "tables" / path.name)


def write_main_tex() -> None:
    abstract = r"""Sparse traffic sensor deployments are long-lived infrastructure decisions: once a subset of links or stations is instrumented, the remaining network state must be inferred from partial observations. Classical traffic counting formulations and many learning-based traffic estimators do not directly ask which sensors make the hidden complement most recoverable under a transparent reconstruction model. We propose TRACE-SL, a reconstruction-aware sensor layout framework that couples GLS/MAP and graph-signal reconstruction with posterior uncertainty certificates, validation-based score tuning, and validation-aware local swap refinement. The design protocol keeps model fitting, layout selection, and held-out evaluation separate. On PeMS7\_228 Stage12 evidence, TRACE-SL reduces held-out GLS/MAP MAE relative to validation-selected random layouts by 0.123, 0.095, and 0.163 at 10\%, 20\%, and 30\% sensor budgets, respectively. PeMS7\_1026 and Seattle provide additional ten-split empirical evidence. The contribution is not a claim of globally optimal or universally robust placement; it is a transparent inverse-problem design workflow whose claims are tied to scoped theory, held-out evidence, and auditable result artifacts."""
    main = rf"""\documentclass[a4paper,fleqn]{{cas-sc}}

\usepackage[authoryear,longnamesfirst]{{natbib}}
\usepackage{{amsmath,amssymb,booktabs,array,tabularx}}
\usepackage{{graphicx}}
\usepackage{{xurl}}

\input{{math_commands}}

\begin{{document}}
\let\WriteBookmarks\relax
\def\floatpagepagefraction{{1}}
\def\textpagefraction{{.001}}

\shorttitle{{TRACE-SL}}
\shortauthors{{Anonymous Authors}}

\title[mode=title]{{TRACE-SL: Reconstruction-Aware Sensor Layout Design\\for Traffic State Estimation}}

\author[1]{{Anonymous Author}}
\affiliation[1]{{organization={{Anonymous Institution}},
            city={{Anonymous City}},
            country={{Anonymous Country}}}}

\begin{{abstract}}
{abstract}
\end{{abstract}}

\begin{{highlights}}
\item We formulate sparse traffic sensing as reconstruction-aware hidden-network design.
\item TRACE-SL combines posterior certificates, validation selection, and local swap refinement.
\item Held-out Stage12 evidence spans PeMS7\_228, PeMS7\_1026, and Seattle.
\item Submission-facing claims are explicitly bounded by evidence and scoped theory.
\end{{highlights}}

\begin{{keywords}}
traffic sensor placement \sep network design \sep traffic state reconstruction \sep optimal experimental design \sep graph signal sampling
\end{{keywords}}

\maketitle

\input{{sections/1_introduction}}
\input{{sections/2_related_work}}
\input{{sections/3_problem}}
\input{{sections/4_method_theory}}
\input{{sections/5_experiments}}
\input{{sections/6_ablation_robustness}}
\input{{sections/7_discussion}}
\input{{sections/8_conclusion}}

\section*{{CRediT authorship contribution statement}}
Anonymous for review.

\section*{{Declaration of competing interest}}
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

\section*{{Data and code availability}}
The manuscript reports curated aggregate artifacts and generation scripts. Raw traffic datasets are local inputs and are not distributed with the paper source.

\bibliographystyle{{cas-model2-names}}
\bibliography{{references}}

\appendix
\input{{sections/A_appendix}}

\end{{document}}
"""
    write(PAPER_DIR / "main.tex", main)
    math = r"""% Shared TRACE-SL notation.
\newcommand{\R}{\mathbb{R}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\argmin}{\operatorname*{arg\,min}}
\newcommand{\argmax}{\operatorname*{arg\,max}}
\newcommand{\calV}{\mathcal{V}}
\newcommand{\calS}{\mathcal{S}}
\newcommand{\calH}{\mathcal{H}}
\newcommand{\calC}{\mathcal{C}}
\newcommand{\calD}{\mathcal{D}}
\newcommand{\calT}{\mathcal{T}}
\newcommand{\SigmaPost}{\Sigma_{\calH \mid \calS}}
"""
    write(PAPER_DIR / "math_commands.tex", math)


def write_sections() -> None:
    sections = {
        "0_abstract.tex": r"""Sparse traffic sensor deployments are long-lived infrastructure decisions: once a subset of links or stations is instrumented, the remaining network state must be inferred from partial observations. Classical traffic counting formulations and many learning-based traffic estimators do not directly ask which sensors make the hidden complement most recoverable under a transparent reconstruction model. We propose TRACE-SL, a reconstruction-aware sensor layout framework that couples GLS/MAP and graph-signal reconstruction with posterior uncertainty certificates, validation-based score tuning, and validation-aware local swap refinement. The design protocol keeps model fitting, layout selection, and held-out evaluation separate. On PeMS7\_228 Stage12 evidence, TRACE-SL reduces held-out GLS/MAP MAE relative to validation-selected random layouts by 0.123, 0.095, and 0.163 at 10\%, 20\%, and 30\% sensor budgets, respectively. PeMS7\_1026 and Seattle provide additional ten-split empirical evidence. The contribution is not a claim of globally optimal or universally robust placement; it is a transparent inverse-problem design workflow whose claims are tied to scoped theory, held-out evidence, and auditable result artifacts.""",
        "1_introduction.tex": r"""\section{Introduction}
\label{sec:introduction}

Traffic agencies rarely observe a road network completely. Fixed loop detectors, cameras, probe feeds, and connected-vehicle observations provide partial measurements, while the operational question often concerns the full network state. The siting decision is therefore not only a coverage problem. A sensor can be valuable because it makes unobserved links recoverable under a transparent estimation model, even when it is not the highest-flow or highest-variance location.

This paper studies sparse traffic sensor layout as reconstruction-aware network design. Given a fixed budget, we choose a set of candidate nodes or links to observe and then evaluate how well a transparent estimator reconstructs the hidden complement. This differs from classical count-location formulations that emphasize origin-destination coverage, flow interception, or link independence \citep{yang1998optimal}; it also differs from black-box traffic forecasting work that improves state estimators while taking the observation pattern as given \citep{li2018dcrnn,yu2018stgcn}. The layout and the reconstruction model must be evaluated together.

We propose TRACE-SL, a transparent reconstruction-aware sensor layout framework. TRACE-SL builds candidate layouts using posterior trace, log-determinant, scenario risk, and coverage heuristics; selects among candidate scoring rules by validation reconstruction error; and refines selected candidates with a validation-aware one-swap search. The final evaluation is held out: once the layout rule is fixed, only selected sensors are observed and non-sensor nodes are reconstructed and scored.

The contributions are fourfold. First, we formulate fixed-budget sensor layout for hidden-network reconstruction with explicit train, validation, and test separation. Second, we connect posterior trace to expected hidden-state squared error under a scoped linear-Gaussian GLS/MAP model, using it as a certificate-guided proxy rather than a universal MAE guarantee. Third, we provide Stage12 held-out evidence against random, validation-selected random, variance, observability, graph sampling, A/D-optimal, and POD-style baselines. Fourth, we release manuscript-facing claim, table, ablation, and evidence-lane artifacts that make the reported claims auditable.

\input{tables/table_main_results}

The rest of the paper is organized as follows. Section~\ref{sec:related} positions TRACE-SL relative to traffic count location, sensor selection, graph sampling, and traffic estimation. Section~\ref{sec:problem} defines the reconstruction-aware layout problem. Section~\ref{sec:method} presents TRACE-SL and its scoped theoretical statements. Sections~\ref{sec:experiments} and~\ref{sec:analysis} report main evidence, ablations, and robustness routing. Section~\ref{sec:discussion} discusses limitations, and Section~\ref{sec:conclusion} concludes.""",
        "2_related_work.tex": r"""\section{Related work}
\label{sec:related}

\paragraph{Traffic count and detector location.}
Traffic sensor location has a long history in transportation methodology. A central line of work chooses counting points to support origin-destination estimation or network monitoring, using criteria such as OD coverage, flow interception, and link independence \citep{yang1998optimal}. TRACE-SL keeps the same infrastructure-design spirit but changes the operational target: the selected sensors are judged by full-network state reconstruction on held-out days, not by deterministic coverage rules alone.

\paragraph{Sensor selection and optimal experimental design.}
The broader signal-processing and control literature studies subset selection for parameter estimation, including convex relaxations and A/D/E-optimal design criteria \citep{joshi2009sensor}. Gaussian-process sensor placement uses information gain and submodularity to choose informative locations \citep{krause2008near}. TRACE-SL borrows the idea that uncertainty certificates can guide placement, but it treats the certificate as one component of a traffic-specific validation and reconstruction workflow rather than as a stand-alone optimality guarantee.

\paragraph{Graph sampling and sparse reconstruction.}
Graph signal processing provides sampling theory and reconstruction tools for signals supported on graph vertices \citep{chen2015sampling,anis2016sampling}. Data-driven sparse sensor placement similarly exploits low-dimensional patterns to reconstruct high-dimensional states from few sensors \citep{manohar2018sparse}. TRACE-SL differs by coupling these reconstruction ideas to a deployment-style validation protocol and by comparing against graph/POD-style baselines within traffic networks.

\paragraph{Traffic state estimation and forecasting.}
Deep spatiotemporal traffic models, including diffusion convolution and graph convolutional forecasting models, have improved prediction accuracy when data are available on a fixed sensor graph \citep{li2018dcrnn,yu2018stgcn}. TRACE-SL addresses a different decision layer: before training a complex estimator, where should the fixed sparse sensors be placed if the downstream objective is hidden-network reconstruction? This separation is important because an estimator benchmark does not by itself justify the observation design.""",
        "3_problem.tex": r"""\section{Reconstruction-aware sensor layout}
\label{sec:problem}

Let $G=(\calV,E)$ denote a traffic network with candidate sensing locations $\calV$. At each time $t$, the traffic state is $x_t \in \R^{|\calV|}$. A deployment chooses a fixed sensor set $\calS \subseteq \calV$ with $|\calS| \leq k$ and observes $x_{t,\calS}$, while the hidden complement $\calH=\calV\setminus\calS$ must be reconstructed. The design objective is not to recover an OD matrix or guarantee full observability; it is to choose $\calS$ so that a transparent reconstruction rule $\hat{x}_{t,\calH}=f_{\calS}(x_{t,\calS})$ has low held-out error on hidden components.

The experiments use transparent GLS/MAP and graph-signal reconstruction models. Training data estimate reconstruction ingredients such as means, covariances or precisions, graph operators, and regularization. Validation data choose the layout rule and tune TRACE-SL scoring. Test data are used only after the layout rule is fixed. This split discipline prevents validation reconstruction error from being treated as final deployment evidence.

For a candidate layout $\calS$, the primary test metric is hidden-component MAE,
\[
    \mathrm{MAE}(\calS)=\frac{1}{|\calT_{\mathrm{test}}||\calH|}
    \sum_{t\in\calT_{\mathrm{test}}}\|x_{t,\calH}-\hat{x}_{t,\calH}\|_1.
\]
The paper-source artifacts also report RMSE, MAPE where available, posterior trace, condition number, log determinant, scenario CVaR trace, coverage, and validation diagnostics. The central claim is empirical and scoped: layouts selected by TRACE-SL improve reconstruction in the tested settings and under the stated transparent reconstruction protocol.""",
        "4_method_theory.tex": r"""\section{TRACE-SL method and scoped theory}
\label{sec:method}

\input{tables/table_theory}

TRACE-SL has three layers. The first layer constructs a candidate pool using transparent certificate and coverage criteria. Candidate generators include greedy A-trace, greedy log-determinant, scenario-average A-trace, scenario-CVaR A-trace, posterior-trace swap refinements, quality-coverage sampling, degree, top-variance, coverage, and random candidate families. The second layer selects the scoring weights on validation data rather than fixing them by hand. A selector-validation split chooses a layout for each score vector, and a tuner-validation split selects the vector with the lowest GLS/MAP reconstruction MAE. The third layer applies validation-aware one-swap refinement to strong candidates: a remove/add exchange is accepted only when it improves validation reconstruction loss.

Under a linear-Gaussian GLS/MAP model with fixed prior and observation noise, the posterior covariance on hidden components provides a principled squared-error uncertainty proxy. In this setting, the trace of $\SigmaPost$ equals the conditional expected squared hidden-state reconstruction error up to the fixed observation model. Moreover, conditioning on additional sensors cannot increase posterior covariance in positive-semidefinite order, so the posterior trace is nonincreasing for nested sensor sets. These statements motivate posterior-trace candidate generation, but they do not imply non-Gaussian MAE guarantees.

The validation-aware swap output is locally optimal only with respect to the evaluated one-swap neighborhood. If no tested remove/add exchange from the configured candidate pool strictly improves validation reconstruction loss, the returned layout is locally optimal for that finite neighborhood. This is not a global optimality result; it is a precise algorithmic statement about the search actually performed.

\input{tables/table_ablation}

The workload can be decomposed into candidate generation, candidate scoring, and swap evaluation. The relevant scaling variables are the number of candidate generators, candidate counts, budget levels, validation windows, swap starts, swap iterations, and add/remove pool sizes. TRACE-SL therefore exposes runtime and manifest artifacts rather than claiming hardware-independent optimal-placement certification.""",
        "5_experiments.tex": r"""\section{Experimental design and main results}
\label{sec:experiments}

\input{tables/table_external}

\begin{figure}[t]
\centering
\includegraphics[width=0.95\linewidth]{figures/fig2_main_mae.pdf}
\caption{Held-out PeMS7\_228 GLS/MAP reconstruction MAE across sensor budgets. TRACE-SL refers to the validation-aware selected layout.}
\label{fig:main-mae}
\end{figure}

The Stage12 experiments evaluate PeMS7\_228, PeMS7\_1026, and Seattle under 10\%, 20\%, and 30\% sensor budgets. Each reported aggregate uses ten held-out splits. Baselines include random mean, validation-selected random, top variance, greedy A-trace, greedy log-determinant, observability proxy, graph sampling, QR/POD-style sparse placement, scenario risk variants, RCSS-selected layouts, and multistart validation-swap comparators.

Table~\ref{tab:main-results} reports the main PeMS7\_228 evidence. TRACE-SL reaches mean held-out GLS/MAP MAE of 3.590, 3.355, and 3.084 at 10\%, 20\%, and 30\% budgets. Against validation-selected random layouts, the paired mean deltas are -0.123, -0.095, and -0.163 with paired $p$ values 8.8e-05, 0.0054, and 0.0005. Against random mean layouts, the paired mean deltas are -0.243, -0.220, and -0.320.

The low-budget PeMS7\_228 comparison with the multistart swap baseline is deliberately reported as a caveat. At 10\%, TRACE-SL and multistart validation swap are statistically close, and the evidence does not justify a claim that one selected layout dominates every strong internal variant at every budget. The paper-level claim is therefore about reconstruction-aware layout design and the TRACE-SL portfolio, not about a universal winner on every row.

Table~\ref{tab:external} summarizes external evidence. PeMS7\_1026 and Seattle both have ten tracked Stage12 splits and support multi-network empirical discussion. This evidence should not be read as a universal generalization theorem: it shows that the same design logic transfers across the tested networks and protocols.""",
        "6_ablation_robustness.tex": r"""\section{Ablations and robustness routing}
\label{sec:analysis}

The ablation contract separates the roles of random candidate pools, validation selection, certificate-guided candidate generation, RCSS selection, validation-aware local refinement, and multistart swap search. Table~\ref{tab:ablation} shows the 30\% PeMS7\_228 component comparison. The ordering supports the intended mechanism: reconstruction-aware candidate generation improves over random baselines, validation and certificates help select recoverable candidates, and local refinement improves the final layout.

The ablation should be interpreted at the component level rather than as a kitchen-sink heuristic. Greedy A-trace and scenario risk variants are certificate-only candidates. Validation-selected random isolates validation selection without certificate-guided candidate generation. RCSS-selected layouts isolate score-based selection before local refinement. Validation-swap selected layouts add the local neighborhood search. Multistart swap is retained as a serious comparator because it is close at low budget and strong at higher budgets.

Robustness evidence is routed as stress-test evidence. The project includes perturbation artifacts for sensor failure, observation noise, missingness, heterogeneous costs, temporal shift, and candidate-pool sensitivity. These tests support bounded robustness discussion in the tested settings. They do not support the phrase globally robust, and they do not replace held-out Stage12 evidence for main performance claims.""",
        "7_discussion.tex": r"""\section{Discussion and limitations}
\label{sec:discussion}

TRACE-SL is useful because it aligns a costly infrastructure decision with the downstream inverse problem. A high-flow or high-variance sensor can be attractive, but a reconstruction-aware layout may instead choose sensors that reduce hidden-state uncertainty and improve validation recoverability. The method is intentionally transparent: its certificate terms, validation losses, selected layouts, and held-out outcomes can be inspected.

Several limitations define the claim boundary. First, posterior trace is a squared-error uncertainty certificate under scoped GLS/MAP assumptions; it is not a theorem that MAE must improve on non-Gaussian traffic data. Second, validation-aware swap search is local to the evaluated one-swap neighborhood and candidate pool. Third, PeMS7\_1026 and Seattle support multi-network empirical evidence, not universal cross-network generalization. Fourth, robustness results are stress tests rather than formal certification against all perturbations.

These limitations are methodological guardrails rather than defects. They make the manuscript falsifiable: a reviewer can trace each claim to a table, theorem statement, or explicit caveat. Future work should study stronger stochastic or bilevel formulations, approximation properties under traffic-specific covariance structure, and deployment studies with real maintenance and sensor-failure costs.""",
        "8_conclusion.tex": r"""\section{Conclusion}
\label{sec:conclusion}

This paper presented TRACE-SL, a transparent reconstruction-aware framework for sparse traffic sensor layout design. The method treats the sensor set as a design variable for hidden-network reconstruction, combines posterior and scenario certificates with validation selection and local refinement, and evaluates layouts only after the selection rule is fixed. Across PeMS7\_228, PeMS7\_1026, and Seattle Stage12 evidence, TRACE-SL supports a bounded but practically meaningful claim: reconstruction-aware layout design can improve full-network state reconstruction relative to coverage, graph, random, and POD-style baselines in the tested settings. The final contribution is an auditable bridge between traffic network design, transparent inverse problems, and empirical sensor deployment evidence.""",
        "A_appendix.tex": r"""\section{Additional audit notes}

The source package is generated from \texttt{NARRATIVE\_REPORT.md} and CSV/JSON paper-source artifacts under \texttt{TRC-23-02333/trace\_sl\_results/paper\_sources/}. Raw datasets are not embedded in the paper source. Numeric claims in the main text should be rechecked by \texttt{paper-claim-audit} after every editing round.

\section{Proof sketches for scoped statements}

For the posterior trace identity, the proof follows the standard conditional Gaussian calculation: under a fixed linear observation model and squared-error loss, the conditional mean minimizes expected squared error and the residual covariance over hidden components is the posterior covariance. Taking the trace gives the expected squared Euclidean reconstruction error over hidden components.

For monotonicity, adding a sensor corresponds to conditioning on an additional linear observation under the same prior/noise model. The Schur complement update subtracts a positive semidefinite term from the previous posterior covariance, hence the posterior covariance is nonincreasing in Loewner order and its trace is nonincreasing.

For validation-aware swap local optimality, the algorithm terminates after evaluating the configured finite neighborhood. If no evaluated remove/add exchange strictly reduces validation reconstruction loss, the returned layout is locally optimal with respect to that evaluated neighborhood. The statement is not about swaps outside the configured add/remove pools or about global optimality.""",
    }
    for name, text in sections.items():
        write(PAPER_DIR / "sections" / name, text)


def write_bib() -> None:
    bib = r"""@article{yang1998optimal,
  author = {Yang, Hai and Zhou, Jing},
  title = {Optimal traffic counting locations for origin-destination matrix estimation},
  journal = {Transportation Research Part B: Methodological},
  volume = {32},
  number = {2},
  pages = {109--126},
  year = {1998},
  doi = {10.1016/S0191-2615(97)00016-7}
}

@article{joshi2009sensor,
  author = {Joshi, Siddharth and Boyd, Stephen},
  title = {Sensor Selection via Convex Optimization},
  journal = {IEEE Transactions on Signal Processing},
  volume = {57},
  number = {2},
  pages = {451--462},
  year = {2009},
  doi = {10.1109/TSP.2008.2007095}
}

@article{krause2008near,
  author = {Krause, Andreas and Singh, Ajit and Guestrin, Carlos},
  title = {Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies},
  journal = {Journal of Machine Learning Research},
  volume = {9},
  pages = {235--284},
  year = {2008},
  url = {https://www.jmlr.org/papers/v9/krause08a.html}
}

@article{chen2015sampling,
  author = {Chen, Siheng and Varma, Rohan and Sandryhaila, Aliaksei and Kovacevic, Jelena},
  title = {Discrete Signal Processing on Graphs: Sampling Theory},
  journal = {IEEE Transactions on Signal Processing},
  volume = {63},
  number = {24},
  pages = {6510--6523},
  year = {2015},
  doi = {10.1109/TSP.2015.2469645}
}

@article{anis2016sampling,
  author = {Anis, Aamir and Gadde, Akshay and Ortega, Antonio},
  title = {Efficient Sampling Set Selection for Bandlimited Graph Signals Using Graph Spectral Proxies},
  journal = {IEEE Transactions on Signal Processing},
  volume = {64},
  number = {14},
  pages = {3775--3789},
  year = {2016},
  doi = {10.1109/TSP.2016.2546233}
}

@article{manohar2018sparse,
  author = {Manohar, Krithika and Brunton, Bingni W. and Kutz, J. Nathan and Brunton, Steven L.},
  title = {Data-Driven Sparse Sensor Placement for Reconstruction: Demonstrating the Benefits of Exploiting Known Patterns},
  journal = {IEEE Control Systems Magazine},
  volume = {38},
  number = {3},
  pages = {63--86},
  year = {2018},
  doi = {10.1109/MCS.2018.2810460}
}

@inproceedings{li2018dcrnn,
  author = {Li, Yaguang and Yu, Rose and Shahabi, Cyrus and Liu, Yan},
  title = {Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting},
  booktitle = {International Conference on Learning Representations},
  year = {2018},
  url = {https://openreview.net/forum?id=SJiHXGWAZ}
}

@inproceedings{yu2018stgcn,
  author = {Yu, Bing and Yin, Haoteng and Zhu, Zhanxing},
  title = {Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting},
  booktitle = {Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence},
  pages = {3634--3640},
  year = {2018},
  doi = {10.24963/ijcai.2018/505}
}
"""
    write(PAPER_DIR / "references.bib", bib)


def write_report_stub() -> None:
    report = """# Paper Writing Pipeline Report

**Input**: NARRATIVE_REPORT.md
**Venue**: Transportation Research Part B: Methodological
**Assurance**: submission
**Submission-ready**: no
**Date**: 2026-05-26

## Pipeline Summary

| Phase | Status | Output |
|-------|--------|--------|
| 0. Assurance Setup | Complete | paper/.aris/assurance.txt = submission |
| 1. Paper Plan | Complete | PAPER_PLAN.md |
| 2. Figures | Complete | figures/ and paper/tables/ |
| 3. LaTeX Writing | Complete | paper/main.tex and sections |
| 4. Compilation | Pending | paper/main.pdf |
| 5. Improvement | Pending | round PDFs and log |
| 6. Submission Audits | Pending | PROOF/PAPER_CLAIM/CITATION/KILL_ARGUMENT JSON |

## Remaining Issues

- Compile and format the CAS manuscript.
- Run improvement loop and mandatory audits.
"""
    write(PAPER_DIR / "PAPER_WRITING_PIPELINE_REPORT.md", report)


def generate_all() -> None:
    write_plan()
    generate_figures()
    generate_tables()
    setup_paper_dir()
    write_main_tex()
    write_sections()
    write_bib()
    write_report_stub()


if __name__ == "__main__":
    generate_all()
    print("Generated PAPER_PLAN.md, figures/, and paper/ TR Part B draft.")
