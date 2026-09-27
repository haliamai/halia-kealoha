"""
Regenerates Figure 1 (break-even curve) for the Hawaii geothermal research paper
from the locked sensitivity model in capabilities/economic-research/spec.md
(Section 4, "Locked sensitivity design").

Locked equation: Delta_p* = C / V_public, with C = $5,000,000 (verified, Data
Sources row 1). The four scenario points are computed directly from this
equation at the locked V_public values; nothing about the model is decided in
this script, it only renders it.

Run from anywhere; the output PNG is written next to this script.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import textwrap

# ---- Locked inputs (do not change) ----
C = 5_000_000  # verified public cost of characterization (Data Sources row 1)

# Locked V_public sensitivity scenarios (Section 4). Break-even Delta p* for
# each is computed from the equation below, never hard-coded.
V_SCENARIOS = [10_000_000, 25_000_000, 50_000_000, 100_000_000]


def breakeven_dp(v_public, cost=C):
    """Delta p* = C / V_public -- the locked break-even equation."""
    return cost / v_public


scenarios = [(v, breakeven_dp(v)) for v in V_SCENARIOS]

# ---- Curve: Delta p* = C / V_public, plotted over the locked scenario range only ----
v_min, v_max = min(V_SCENARIOS), max(V_SCENARIOS)
v_vals = np.linspace(v_min, v_max, 500)
dp_star = breakeven_dp(v_vals)

# ---- Palette (validated default palette, dataviz skill) ----
blue = "#2a78d6"       # categorical slot 1 - curve
good_green = "#0ca30c"  # status: good (positive net value region)
critical_red = "#d03b3b"  # status: critical (negative net value region)
text_primary = "#0b0b0b"
text_secondary = "#52514e"
surface = "#fcfcfb"
grid_color = "#d9d8d3"

fig, ax = plt.subplots(figsize=(8, 5.9), dpi=300)
fig.patch.set_facecolor(surface)
ax.set_facecolor(surface)

# Shade the above/below regions (subtle; labels carry the meaning, not color alone)
ax.fill_between(v_vals, dp_star, 0.55, color=good_green, alpha=0.06, zorder=0)
ax.fill_between(v_vals, 0, dp_star, color=critical_red, alpha=0.06, zorder=0)

# The break-even curve itself
ax.plot(v_vals, dp_star, color=blue, linewidth=2.5, zorder=3,
         label=r"Break-even: $\Delta p^{*} = \$5,000,000 / V_{public}$")

# Mark and label the four locked scenario points
# The $10M point sits nearest the plot's left/top boundary, so it gets a custom
# offset (up and to the right of the marker) for breathing room; the other three
# keep the default centered-above placement.
label_overrides = {10_000_000: {"xytext": (14, 10), "ha": "left"}}
for v, dp in scenarios:
    ax.scatter([v], [dp], s=70, color=blue, edgecolor="white", linewidth=1.2, zorder=4)
    style = {"xytext": (0, 8), "ha": "center"}
    style.update(label_overrides.get(v, {}))
    ax.annotate(
        f"${v/1_000_000:,.0f}M, {dp*100:.0f}%",
        xy=(v, dp),
        xytext=style["xytext"],
        textcoords="offset points",
        ha=style["ha"],
        va="bottom",
        fontsize=9.5,
        color=text_primary,
        fontweight="normal",
        zorder=5,
    )

# Region labels (explicit text, not color-only) - centered top/bottom, clear of points and curve
ax.text(0.5, 0.95, "Positive net expected public value (above curve)",
         transform=ax.transAxes, ha="center", va="top", fontsize=9.5,
         color=text_secondary, style="italic")
ax.text(0.5, 0.015, "Negative net expected public value (below curve)",
         transform=ax.transAxes, ha="center", va="bottom", fontsize=9.5,
         color=text_secondary, style="italic")

# Axes formatting - display range locked to the scenario range ($10M-$100M), no
# extension beyond it
ax.set_xlim(v_min - 3_000_000, v_max + 3_000_000)
ax.set_ylim(0, 0.55)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1_000_000:,.0f}M"))
ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=0))

ax.set_xlabel("Assumed public value if the project succeeds ($V_{public}$, illustrative sensitivity scenario)",
              fontsize=10.5, color=text_primary, labelpad=10)
ax.set_ylabel("Break-even probability improvement needed ($\\Delta p^{*}$)",
              fontsize=10.5, color=text_primary, labelpad=10)

fig_title = ("Figure 1. Break-Even Probability Improvement Needed for a $5 Million\n"
             "Characterization Investment, by Assumed Public Value")
fig.suptitle(fig_title, fontsize=13.5, color=text_primary, fontweight="bold", y=0.985)

# Grid (recessive)
ax.grid(True, color=grid_color, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
for spine in ["left", "bottom"]:
    ax.spines[spine].set_color(grid_color)

note_text = (
    "Note. The curve shows the minimum improvement in the probability of successful commercial "
    "development ($\\Delta p^{*}$) needed for a \\$5 million characterization investment to break even "
    "at different assumed levels of public value ($V_{public}$). Both variables are sensitivity "
    "assumptions, not empirical estimates. Points above the curve produce positive net expected "
    "public value under the stated assumptions; points below produce negative net expected public "
    "value. A positive result does not, by itself, establish that additional public funding is justified."
)
note_wrapped = "\n".join(textwrap.wrap(note_text, width=98))
n_lines = note_wrapped.count("\n") + 1
bottom_margin = 0.022 * n_lines + 0.015

plt.tight_layout(rect=[0, bottom_margin, 1, 0.90])

# Caption note, below the axes (figure-level, clear of the plot area)
fig.text(0.5, 0.01, note_wrapped, ha="center", va="bottom", fontsize=8.5, color=text_secondary)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "breakeven-curve.png")
plt.savefig(out_path, facecolor=surface, bbox_inches="tight")
print("Saved:", out_path)

# Print the exact plotted point data for verification
print("\nLocked scenario points (V_public, break-even Delta p*), computed from Delta p* = C / V_public:")
for v, dp in scenarios:
    print(f"  V_public=${v:,} -> Delta p*={dp:.0%}  ({C}/{v} = {dp:.4f})")
