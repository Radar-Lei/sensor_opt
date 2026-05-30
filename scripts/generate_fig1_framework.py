#!/usr/bin/env python3
"""Generate a clean vector PDF for Figure 1: TRACE-BiOpt bilevel framework.

Outputs a true vector PDF (no raster embeddings) suitable for
Transportation Research Part B / Elsevier submission.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# ---------- font / output config ----------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "pdf.fonttype": 42,          # TrueType embed
    "ps.fonttype": 42,
    "text.usetex": False,
    "axes.linewidth": 0.6,
    "savefig.dpi": 300,
})

# ---------- colour palette (blue-academic) ----------
C_UPPER      = "#2C5F8A"   # dark blue – upper level
C_UPPER_BG   = "#D6E4F0"   # light blue fill
C_LOWER      = "#3A7D44"   # dark green – lower level
C_LOWER_BG   = "#DAE8DA"   # light green fill
C_INPUT      = "#F5F5F5"   # light grey – input/output
C_OUTPUT     = "#F5F5F5"
C_ARROW      = "#333333"
C_OBJ_TERM  = "#4A90C4"    # medium blue – objective terms
C_OBJ_BG    = "#EBF3FA"    # very light blue – objective boxes
C_FEEDBACK   = "#B03A2E"   # red – feedback arrows
C_LABEL     = "#1A1A1A"


def _box(ax, x, y, w, h, label, bg, edge, fontsize=8,
         bold=False, multiline=None, text_color=C_LABEL):
    """Draw a rounded rectangle with centred label."""
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02",
        facecolor=bg, edgecolor=edge, linewidth=1.0, zorder=2,
    )
    ax.add_patch(box)
    weight = "bold" if bold else "normal"
    if multiline:
        lines = multiline.split("\n")
        n = len(lines)
        for i, line in enumerate(lines):
            dy = (n / 2 - i - 0.5) * fontsize * 0.018
            ax.text(x + w / 2, y + h / 2 + dy, line,
                    ha="center", va="center", fontsize=fontsize,
                    fontweight=weight, color=text_color, zorder=3)
    else:
        ax.text(x + w / 2, y + h / 2, label,
                ha="center", va="center", fontsize=fontsize,
                fontweight=weight, color=text_color, zorder=3)
    return (x, y, w, h)


def _arrow(ax, x0, y0, x1, y1, color=C_ARROW, style="->", lw=1.0,
           connectionstyle="arc3,rad=0"):
    """Draw an arrow between two points."""
    arrow = FancyArrowPatch(
        (x0, y0), (x1, y1),
        arrowstyle=style, color=color,
        linewidth=lw, zorder=4,
        connectionstyle=connectionstyle,
        mutation_scale=10,
    )
    ax.add_patch(arrow)


def _arrow_label(ax, x, y, label, fontsize=6.5, color="#555555", rotation=0):
    ax.text(x, y, label, ha="center", va="center",
            fontsize=fontsize, color=color, style="italic", zorder=5,
            rotation=rotation,
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                      edgecolor="none", alpha=0.85))


def main():
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("auto")
    ax.axis("off")

    # ========== Layout coordinates ==========
    # Upper level: y in [0.58, 0.95]
    # Lower level: y in [0.10, 0.42]
    # Input:  left side
    # Output: right side

    # --- Input block (left) ---
    ix, iy, iw, ih = 0.02, 0.48, 0.13, 0.32
    _box(ax, ix, iy, iw, ih, "",
         bg=C_INPUT, edge="#999999",
         multiline="Traffic\nNetwork\nData\n$G=(\\mathcal{V},E)$\n$\\mathcal{D}_{\\mathrm{tr}}$\n$\\mathcal{D}_{\\mathrm{val}}$",
         fontsize=6.5)

    # --- Output block (right) ---
    ox, oy, ow, oh = 0.85, 0.48, 0.13, 0.32
    _box(ax, ox, oy, ow, oh, "",
         bg=C_OUTPUT, edge="#999999",
         multiline="Optimal\nSensor Layout\n$\\hat{\\mathcal{S}}$",
         fontsize=7, bold=True)

    # ============================================================
    # Upper Level (design) – one continuous rounded rectangle
    # ============================================================
    ux, uy, uw, uh = 0.20, 0.58, 0.62, 0.37
    upper_bg = FancyBboxPatch(
        (ux, uy), uw, uh,
        boxstyle="round,pad=0.015",
        facecolor=C_UPPER_BG, edgecolor=C_UPPER, linewidth=1.6, zorder=1,
    )
    ax.add_patch(upper_bg)

    # Combined title line: level name + objective on one line
    ax.text(ux + uw / 2, uy + uh - 0.04,
            "Upper Level — Sensor Layout Design:     "
            "minimize  $J(\\mathcal{S})$",
            fontsize=8, fontweight="bold", color=C_UPPER, zorder=3,
            ha="center")

    # Four objective term boxes inside upper level
    term_y = uy + 0.12
    term_h = 0.12
    term_w = 0.13
    term_gap = 0.018
    terms_start_x = ux + (uw - 4 * term_w - 3 * term_gap) / 2

    terms = [
        ("Huber\nReconstruction\nLoss", "$\\hat{R}_{\\mathrm{Huber}}$"),
        ("Posterior\nUncertainty", "$\\mathrm{tr}(\\Sigma_{\\mathcal{H}})$"),
        ("CVaR\nTail Risk", "$\\mathrm{CVaR}_{\\alpha}$"),
        ("Spatial\nRegularization", "$\\Omega_{\\mathrm{spatial}}$"),
    ]

    for i, (name, formula) in enumerate(terms):
        tx = terms_start_x + i * (term_w + term_gap)
        _box(ax, tx, term_y, term_w, term_h, "",
             bg=C_OBJ_BG, edge=C_OBJ_TERM,
             multiline=name, fontsize=6, text_color="#2C3E50")
        # Formula label below each box
        ax.text(tx + term_w / 2, term_y - 0.02, formula,
                ha="center", va="center", fontsize=5.5, color="#555555", zorder=3)

    # Plus signs between term boxes
    for i in range(len(terms) - 1):
        px = terms_start_x + (i + 1) * (term_w + term_gap) - term_gap / 2
        ax.text(px, term_y + term_h / 2, "+",
                ha="center", va="center", fontsize=10,
                fontweight="bold", color=C_UPPER, zorder=3)

    # ============================================================
    # Lower Level (reconstruction)
    # ============================================================
    lx, ly, lw, lh = 0.20, 0.10, 0.62, 0.34
    lower_bg = FancyBboxPatch(
        (lx, ly), lw, lh,
        boxstyle="round,pad=0.015",
        facecolor=C_LOWER_BG, edgecolor=C_LOWER, linewidth=1.6, zorder=1,
    )
    ax.add_patch(lower_bg)

    ax.text(lx + lw / 2, ly + lh - 0.04,
            "Lower Level — Transparent GLS/MAP Reconstruction",
            fontsize=8, fontweight="bold", color=C_LOWER, zorder=3,
            ha="center")

    # Lower-level formula (split into two lines for readability)
    formula_line1 = (
        "$\\hat{x}_t(\\mathcal{S}) = \\arg\\min_z$"
    )
    formula_line2 = (
        "$\\left\\{"
        "\\frac{1}{2}\\|M_s(z - x_t)\\|_{R^{-1}}^2"
        " + \\frac{\\lambda_Q}{2}(z-\\mu_t)^\\top Q(z-\\mu_t)"
        " + \\frac{\\lambda_L}{2}z^\\top L z"
        " + \\frac{\\epsilon}{2}\\|z\\|_2^2"
        "\\right\\}$"
    )
    ax.text(lx + lw / 2, ly + lh / 2 + 0.01, formula_line2,
            ha="center", va="center", fontsize=6.5, color="#1A1A1A", zorder=3)

    # Key ingredients
    ingredients = ("Prior $\\mu_t$  ·  Precision $Q$  ·  "
                   "Laplacian $L$  ·  Noise $R$  ·  Sensor mask $M_s$")
    ax.text(lx + lw / 2, ly + 0.04, ingredients,
            ha="center", va="center", fontsize=5.5, color="#555555", zorder=3)

    # ============================================================
    # Arrows
    # ============================================================

    # (1) Input → Upper level
    _arrow(ax, ix + iw, iy + ih * 0.6, ux + 0.005, uy + uh * 0.5,
           color=C_ARROW, lw=1.2)
    _arrow_label(ax, (ix + iw + ux) / 2, iy + ih * 0.6 + 0.025,
                 "$G, \\mathcal{D}$", fontsize=6)

    # (2) Input → Lower level (curved, down the left side)
    _arrow(ax, ix + iw * 0.6, iy, lx + 0.02, ly + lh,
           color=C_ARROW, lw=0.9, connectionstyle="arc3,rad=-0.15")

    # (3) Upper level → Output
    _arrow(ax, ux + uw - 0.005, uy + uh * 0.5, ox, oy + oh * 0.5,
           color=C_ARROW, lw=1.2)
    _arrow_label(ax, (ux + uw + ox) / 2, uy + uh * 0.5 + 0.025,
                 "optimal $\\hat{\\mathcal{S}}$", fontsize=6)

    # (4) Upper → Lower: layout S feeds into reconstruction
    #     Arrow on the left side of the gap
    mid_y = (uy + ly + lh) / 2
    _arrow(ax, ux + uw * 0.40, uy, lx + lw * 0.40, ly + lh,
           color=C_ARROW, lw=1.1)
    _arrow_label(ax, ux + uw * 0.40 - 0.07, mid_y,
                 "layout $\\mathcal{S}$", fontsize=6)

    # (5) Lower → Upper: feedback (reconstruction error, posterior)
    #     Arrow on the right side of the gap, curved to avoid overlap with (4)
    _arrow(ax, lx + lw * 0.60, ly + lh, ux + uw * 0.60, uy,
           color=C_FEEDBACK, lw=1.1, connectionstyle="arc3,rad=-0.25")
    _arrow_label(ax, ux + uw * 0.60 + 0.09, mid_y,
                 "reconstruction error\nposterior covariance",
                 fontsize=5.5, color=C_FEEDBACK)

    # (6) Lower level → output (reconstructed state estimate)
    _arrow(ax, lx + lw, ly + lh * 0.3, ox, oy + oh * 0.1,
           color="#999999", lw=0.8, connectionstyle="arc3,rad=-0.2")
    _arrow_label(ax, (lx + lw + ox) / 2, ly + lh * 0.15,
                 "$\\hat{x}_{\\mathcal{H}}$", fontsize=6, color="#999999")

    # ============================================================
    # Baselines note (bottom)
    # ============================================================
    ax.text(0.50, 0.02,
            "Baselines: external audited comparison class "
            "(held-out evaluation only, not inside solver)",
            ha="center", va="center", fontsize=6, color="#777777",
            style="italic", zorder=3,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FAFAFA",
                      edgecolor="#CCCCCC", linewidth=0.5))

    # ========== Save ==========
    out_path = Path(__file__).resolve().parent.parent / "paper" / "figures" / "fig1_trace_biopt_framework_v2.pdf"
    fig.savefig(str(out_path), format="pdf", bbox_inches="tight",
                pad_inches=0.05, metadata={"Creator": "matplotlib"})
    plt.close(fig)
    print(f"Saved vector PDF to {out_path}")
    print(f"File size: {out_path.stat().st_size / 1024:.1f} KB")

    # Quick sanity check: verify it is NOT a raster PDF
    with open(out_path, "rb") as f:
        content = f.read()
    has_jpeg = b"JPEG" in content
    has_dct = b"DCTDecode" in content
    if has_jpeg or has_dct:
        print("WARNING: output contains raster data (JPEG/DCT)!")
    else:
        print("OK: output is a clean vector PDF (no JPEG/DCT raster data).")


if __name__ == "__main__":
    main()
