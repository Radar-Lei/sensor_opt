#!/usr/bin/env python3
"""Generate a pure-vector Figure 1 (TRACE-BiOpt framework flowchart).

Reproduces the four-step pipeline diagram as matplotlib patches and text,
with no embedded raster images.

Output:
    paper/figures/fig1_trace_biopt_framework_v2.pdf

Run from repository root:
    python scripts/generate_trace_biopt_figure1_vector.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ── colour palette (project-consistent) ──────────────────────────────
BLUE_MAIN   = "#0072B2"
BLUE_LIGHT  = "#D6EAF8"
GREEN_MAIN  = "#009E73"
GREEN_LIGHT = "#D5F5E3"
GREY_MAIN   = "#6B7280"
GREY_LIGHT  = "#F3F4F6"
WHITE       = "#FFFFFF"
BLACK       = "#1F2937"
DASH_BORDER = "#9CA3AF"

# ── figure geometry ──────────────────────────────────────────────────
FIG_W, FIG_H = 12.5, 4.0
DPI = 300

# Section widths and gaps (designed for 12-inch total width)
GAP = 0.38          # horizontal gap between sections
ARROW_LEN = 0.30    # arrow length in gap
PAD_LEFT = 0.15     # left margin
PAD_BOT = 0.50      # bottom margin (for output box)

S1_W = 2.05
S2_W = 3.60
S3_W = 2.45
S4_W = 2.35
SEC_H = 3.05        # section height (all equal)


def _add_section_box(ax, x, y, w, h, color, label, label_num,
                     header_fs=8.0):
    """Draw a rounded-corner section box with a numbered header stripe."""
    body = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02",
        facecolor=WHITE, edgecolor=color, linewidth=1.4, zorder=1,
    )
    ax.add_patch(body)
    header_h = 0.28
    header = FancyBboxPatch(
        (x, y + h - header_h), w, header_h,
        boxstyle="round,pad=0.02",
        facecolor=color, edgecolor=color, linewidth=0, zorder=2,
    )
    ax.add_patch(header)
    ax.text(x + w / 2, y + h - header_h / 2,
            f"{label_num}  {label}",
            ha="center", va="center", fontsize=header_fs, fontweight="bold",
            color=WHITE, zorder=3)


def _add_sub_box(ax, x, y, w, h, border_color, header_text, body_text,
                 header_fs=5.8, body_fs=5.5):
    """Draw a sub-module box with a coloured header bar and body text."""
    body = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012",
        facecolor=WHITE, edgecolor=border_color, linewidth=1.0, zorder=2,
    )
    ax.add_patch(body)
    hh = 0.20
    header = FancyBboxPatch(
        (x + 0.01, y + h - hh - 0.01), w - 0.02, hh,
        boxstyle="round,pad=0.006",
        facecolor=border_color, edgecolor=border_color, linewidth=0,
        zorder=3,
    )
    ax.add_patch(header)
    ax.text(x + w / 2, y + h - hh / 2 - 0.01,
            header_text,
            ha="center", va="center", fontsize=header_fs, fontweight="bold",
            color=WHITE, zorder=4)
    ax.text(x + w / 2, y + (h - hh) / 2,
            body_text,
            ha="center", va="center", fontsize=body_fs, color=BLACK,
            linespacing=1.35, zorder=4)


def _arrow(ax, x0, y0, x1, y1, color=BLUE_MAIN, lw=1.3,
           mutation_scale=10):
    """Draw a FancyArrowPatch."""
    arrow = FancyArrowPatch(
        (x0, y0), (x1, y1),
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        color=color, linewidth=lw,
        connectionstyle="arc3,rad=0",
        zorder=5,
    )
    ax.add_patch(arrow)


def _draw_network_icon(ax, cx, cy, r=0.10, n=5, color=BLUE_MAIN):
    """Draw a tiny network graph icon (nodes + edges)."""
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False) - np.pi / 2
    xs = cx + r * np.cos(angles)
    ys = cy + r * np.sin(angles)
    for i in range(n):
        for j in range(i + 1, n):
            ax.plot([xs[i], xs[j]], [ys[i], ys[j]],
                    color=color, lw=0.5, alpha=0.35, zorder=3)
    ax.scatter(xs, ys, s=10, c=color, zorder=4,
               edgecolors='white', linewidths=0.3)


def _draw_line_chart_icon(ax, cx, cy, w=0.28, h=0.10, color=BLUE_MAIN):
    """Draw a tiny line chart icon."""
    xs = np.linspace(cx - w / 2, cx + w / 2, 20)
    ys = cy + h / 2 * np.sin(np.linspace(0, 2 * np.pi, 20))
    ax.plot(xs, ys, color=color, lw=0.8, zorder=3)
    ax.plot([cx - w / 2, cx + w / 2], [cy - h / 2, cy - h / 2],
            color=GREY_MAIN, lw=0.4, zorder=2)
    ax.plot([cx - w / 2, cx - w / 2], [cy - h / 2, cy + h / 2],
            color=GREY_MAIN, lw=0.4, zorder=2)


def _draw_candidate_grid_icon(ax, cx, cy, color=BLUE_MAIN):
    """Draw a 3x3 grid of candidate node circles."""
    for i in range(3):
        for j in range(3):
            ax.add_patch(plt.Circle(
                (cx - 0.10 + i * 0.10, cy - 0.10 + j * 0.10), 0.028,
                fill=False, edgecolor=color, lw=0.6, zorder=3))


def _draw_bar_chart_icon(ax, cx, cy, w=0.50, h=0.18, color=GREY_MAIN):
    """Draw a tiny bar chart icon."""
    n_bars = 5
    bw = w / (n_bars * 1.5)
    heights = np.array([0.9, 0.65, 0.75, 0.55, 0.80]) * h
    for i in range(n_bars):
        bar_x = cx - w / 2 + i * (bw * 1.5) + bw * 0.25
        ax.add_patch(FancyBboxPatch(
            (bar_x, cy - h / 2), bw, heights[i],
            boxstyle="round,pad=0.003",
            facecolor=color, edgecolor=color, alpha=0.6,
            linewidth=0, zorder=3))


def main():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(-0.2, FIG_W + 0.2)
    ax.set_ylim(-0.15, FIG_H + 0.05)
    ax.set_aspect("equal")
    ax.axis("off")

    # Compute section x positions
    s1_x = PAD_LEFT
    s2_x = s1_x + S1_W + GAP
    s3_x = s2_x + S2_W + GAP
    s4_x = s3_x + S3_W + GAP
    sec_y = PAD_BOT

    # ══════════════════════════════════════════════════════════════════
    # Section 1 – Inputs
    # ══════════════════════════════════════════════════════════════════
    _add_section_box(ax, s1_x, sec_y, S1_W, SEC_H, BLUE_MAIN, "Inputs", 1)

    bx0 = s1_x + 0.10
    bw = S1_W - 0.20

    _add_sub_box(ax, bx0, 2.35, bw, 0.75, BLUE_MAIN,
                 "Traffic network",
                 "Graph $G(V,E)$\nwith distances")
    _draw_network_icon(ax, bx0 + bw / 2, 2.60, r=0.09, n=5, color=BLUE_MAIN)

    _add_sub_box(ax, bx0, 1.35, bw, 0.75, BLUE_MAIN,
                 "Historical traffic states",
                 "Speed / flow time series")
    _draw_line_chart_icon(ax, bx0 + bw / 2, 1.60, w=0.22, h=0.09,
                          color=BLUE_MAIN)

    _add_sub_box(ax, bx0, 0.35, bw, 0.75, BLUE_MAIN,
                 "Budget & candidates",
                 "Sensor budget $k$\nCandidate node set")
    _draw_candidate_grid_icon(ax, bx0 + bw / 2, 0.65, color=BLUE_MAIN)

    # ══════════════════════════════════════════════════════════════════
    # Arrow 1 -> 2
    # ══════════════════════════════════════════════════════════════════
    mid_y = sec_y + SEC_H / 2
    _arrow(ax, s1_x + S1_W + 0.04, mid_y,
           s1_x + S1_W + GAP - 0.04, mid_y)

    # ══════════════════════════════════════════════════════════════════
    # Section 2 – Recoverability-Driven Bilevel Optimization
    # ══════════════════════════════════════════════════════════════════
    _add_section_box(ax, s2_x, sec_y, S2_W, SEC_H, GREEN_MAIN,
                     "Recoverability-Driven Bilevel Optimization", 2)

    ul_x = s2_x + 0.12
    ul_w = S2_W - 0.24

    # -- Upper-level sub-box --
    ul_y = 2.25
    ul_h = 0.55
    _add_sub_box(ax, ul_x, ul_y, ul_w, ul_h, GREEN_MAIN,
                 "Upper level",
                 "Choose sensor layout $z$  ($|z| = k$)")

    # -- Lower-level sub-box --
    ll_y = 1.40
    ll_h = 0.55
    _add_sub_box(ax, ul_x, ll_y, ul_w, ll_h, GREEN_MAIN,
                 "Lower level",
                 "Reconstruct hidden states $x$ via transparent GLS/MAP")

    # -- Bidirectional feedback arrows --
    mid_x = ul_x + ul_w / 2
    _arrow(ax, mid_x - 0.45, ul_y,
           mid_x - 0.45, ll_y + ll_h + 0.04,
           color=GREEN_MAIN, lw=1.1, mutation_scale=9)
    _arrow(ax, mid_x + 0.45, ll_y + ll_h,
           mid_x + 0.45, ul_y - 0.04,
           color=GREEN_MAIN, lw=1.1, mutation_scale=9)

    # -- Objective components (dashed box) --
    obj_x = ul_x
    obj_y = 0.45
    obj_w = ul_w
    obj_h = 0.75
    dashed_box = FancyBboxPatch(
        (obj_x, obj_y), obj_w, obj_h,
        boxstyle="round,pad=0.015",
        facecolor=GREEN_LIGHT, edgecolor=DASH_BORDER, linewidth=0.9,
        linestyle="--", zorder=2,
    )
    ax.add_patch(dashed_box)
    ax.text(obj_x + 0.06, obj_y + obj_h - 0.10,
            "Objective components",
            fontsize=5.5, fontstyle="italic", color=GREY_MAIN, zorder=3)

    # Four component pills
    pill_w = (obj_w - 0.30) / 2
    pill_h = 0.20
    pill_data = [
        ("Reconstruction\nerror", obj_x + 0.08, obj_y + 0.40),
        ("Posterior\nuncertainty", obj_x + 0.08 + pill_w + 0.06, obj_y + 0.40),
        ("Tail risk\n(CVaR)", obj_x + 0.08, obj_y + 0.08),
        ("Spatial\nredundancy", obj_x + 0.08 + pill_w + 0.06, obj_y + 0.08),
    ]
    for label, px, py in pill_data:
        pill = FancyBboxPatch(
            (px, py), pill_w, pill_h,
            boxstyle="round,pad=0.008",
            facecolor=WHITE, edgecolor=GREEN_MAIN, linewidth=0.7, zorder=3,
        )
        ax.add_patch(pill)
        ax.text(px + pill_w / 2, py + pill_h / 2,
                label, ha="center", va="center",
                fontsize=5.0, color=BLACK, zorder=4, linespacing=1.25)

    # -- Solver bar --
    sol_x = ul_x + ul_w * 0.10
    sol_y = sec_y + 0.05
    sol_w = ul_w * 0.80
    sol_h = 0.25
    solver = FancyBboxPatch(
        (sol_x, sol_y), sol_w, sol_h,
        boxstyle="round,pad=0.008",
        facecolor=GREEN_MAIN, edgecolor=GREEN_MAIN, linewidth=0, zorder=3,
    )
    ax.add_patch(solver)
    ax.text(sol_x + sol_w / 2, sol_y + sol_h / 2,
            "Deterministic exchange refinement",
            ha="center", va="center", fontsize=5.8, fontweight="bold",
            color=WHITE, zorder=4)

    # ══════════════════════════════════════════════════════════════════
    # Arrow 2 -> 3
    # ══════════════════════════════════════════════════════════════════
    _arrow(ax, s2_x + S2_W + 0.04, mid_y,
           s2_x + S2_W + GAP - 0.04, mid_y)

    # ══════════════════════════════════════════════════════════════════
    # Section 3 – Selected layout & evaluation
    # ══════════════════════════════════════════════════════════════════
    _add_section_box(ax, s3_x, sec_y, S3_W, SEC_H, BLUE_MAIN,
                     "Selected Layout & Evaluation", 3)

    bx3 = s3_x + 0.10
    bw3 = S3_W - 0.20

    _add_sub_box(ax, bx3, 2.35, bw3, 0.75, BLUE_MAIN,
                 "Selected sensor layout",
                 "Optimal sensors $S^*$\non network $G$")
    # network icon with filled sensor nodes
    n_nodes = 5
    angles = np.linspace(0, 2 * np.pi, n_nodes, endpoint=False) - np.pi / 2
    ncx, ncy = bx3 + bw3 / 2, 2.62
    nr = 0.09
    nxs = ncx + nr * np.cos(angles)
    nys = ncy + nr * np.sin(angles)
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            ax.plot([nxs[i], nxs[j]], [nys[i], nys[j]],
                    color=GREY_MAIN, lw=0.4, alpha=0.4, zorder=3)
    for idx in [0, 3]:
        ax.add_patch(plt.Circle((nxs[idx], nys[idx]), 0.025,
                                facecolor=BLUE_MAIN, edgecolor=WHITE,
                                lw=0.4, zorder=4))
    for idx in [1, 2, 4]:
        ax.add_patch(plt.Circle((nxs[idx], nys[idx]), 0.020,
                                fill=False, edgecolor=GREY_MAIN,
                                lw=0.5, zorder=4))

    _add_sub_box(ax, bx3, 1.35, bw3, 0.75, BLUE_MAIN,
                 "Held-out reconstruction",
                 "Observed vs. reconstructed\nstates on test split")
    # mini dual-line chart icon
    xs_line = np.linspace(bx3 + 0.15, bx3 + bw3 - 0.15, 25)
    ys_rec = 1.68 + 0.07 * np.sin(np.linspace(0, 2.5 * np.pi, 25))
    ys_obs = ys_rec + 0.03 * np.sin(np.linspace(1, 4 * np.pi, 25))
    ax.plot(xs_line, ys_obs, color=GREY_MAIN, lw=0.5, ls="--", zorder=3)
    ax.plot(xs_line, ys_rec, color=BLUE_MAIN, lw=0.7, zorder=3)

    # metric label
    ax.text(bx3 + bw3 / 2, 1.38,
            "Metric: GLS/MAP MAE",
            ha="center", va="center", fontsize=5.0,
            color=GREY_MAIN, zorder=4)

    # ══════════════════════════════════════════════════════════════════
    # Arrow 3 -> 4
    # ══════════════════════════════════════════════════════════════════
    _arrow(ax, s3_x + S3_W + 0.04, mid_y,
           s3_x + S3_W + GAP - 0.04, mid_y)

    # ══════════════════════════════════════════════════════════════════
    # Section 4 – Comparison & Claim Boundary
    # ══════════════════════════════════════════════════════════════════
    _add_section_box(ax, s4_x, sec_y, S4_W, SEC_H, BLUE_MAIN,
                     "Comparison & Claim Boundary", 4,
                     header_fs=7.2)

    bx4 = s4_x + 0.10
    bw4 = S4_W - 0.20

    _add_sub_box(ax, bx4, 2.35, bw4, 0.75, BLUE_MAIN,
                 "Non-BiOpt baselines",
                 "Pre-registered baselines\n(random, degree, greedy ...)")
    _draw_bar_chart_icon(ax, bx4 + bw4 / 2, 2.62, w=0.55, h=0.16,
                         color=GREY_MAIN)

    _add_sub_box(ax, bx4, 1.35, bw4, 0.75, BLUE_MAIN,
                 "Current-best comparison",
                 "TRACE-BiOpt vs. best\nbaselines on test split")
    # mini comparison bars
    bar_ours_h = 0.16
    bar_base_h = 0.13
    ax.add_patch(FancyBboxPatch(
        (bx4 + bw4 / 2 - 0.30, 1.62), 0.22, bar_ours_h,
        boxstyle="round,pad=0.004",
        facecolor=BLUE_MAIN, edgecolor=BLUE_MAIN, alpha=0.7,
        linewidth=0, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (bx4 + bw4 / 2 + 0.08, 1.62), 0.22, bar_base_h,
        boxstyle="round,pad=0.004",
        facecolor=GREY_MAIN, edgecolor=GREY_MAIN, alpha=0.5,
        linewidth=0, zorder=3))
    ax.text(bx4 + bw4 / 2 - 0.19, 1.56, "Ours",
            ha="center", va="center", fontsize=4.5, color=BLUE_MAIN, zorder=4)
    ax.text(bx4 + bw4 / 2 + 0.19, 1.53, "Best\nbase",
            ha="center", va="center", fontsize=4.0, color=GREY_MAIN, zorder=4,
            linespacing=1.1)

    # annotation note at bottom of section 4
    ax.text(s4_x + S4_W / 2, sec_y + 0.25,
            "Baselines: held-out comparison\nonly, never inside solver",
            ha="center", va="center", fontsize=4.5,
            fontstyle="italic", color=GREY_MAIN, zorder=4)

    # ══════════════════════════════════════════════════════════════════
    # Output box (below Section 2)
    # ══════════════════════════════════════════════════════════════════
    out_x = s2_x
    out_y = sec_y - 0.35
    out_w = S2_W
    out_h = 0.22
    # down arrow from solver to output
    _arrow(ax, s2_x + S2_W / 2, sec_y,
           s2_x + S2_W / 2, out_y + out_h + 0.03,
           color=BLUE_MAIN, lw=1.2, mutation_scale=9)
    out_box = FancyBboxPatch(
        (out_x, out_y), out_w, out_h,
        boxstyle="round,pad=0.010",
        facecolor=BLUE_LIGHT, edgecolor=BLUE_MAIN, linewidth=1.0, zorder=2,
    )
    ax.add_patch(out_box)
    ax.text(out_x + out_w / 2, out_y + out_h / 2,
            "Output: recoverability-aware sensor deployment "
            "with lower held-out reconstruction error",
            ha="center", va="center", fontsize=5.8,
            color=BLACK, zorder=3)

    # ── save ─────────────────────────────────────────────────────────
    fig.tight_layout(pad=0.1)
    out_path = Path("paper/figures/fig1_trace_biopt_framework_v2.pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_path), format="pdf", dpi=DPI, bbox_inches="tight")
    fig.savefig(str(out_path.with_suffix(".png")), format="png", dpi=DPI,
                bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path.resolve()}")
    print(f"Saved: {out_path.with_suffix('.png').resolve()}")


if __name__ == "__main__":
    main()
