import math
from typing import List, Optional

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Color palette tuned for kids: soft, high-contrast, colorblind-friendly-ish
PALETTE = [
    "#FF6F61",  # coral
    "#4BC0C0",  # teal
    "#FFD166",  # sunflower
    "#6C5CE7",  # purple
    "#06D6A0",  # green
    "#F78C6B",  # peach
    "#118AB2",  # blue
    "#EF476F",  # pink-red
]

SAFE_DPI = 120  # keep pixel count small and predictable

# Enforce safe defaults globally for all renderers
plt.rcParams["figure.dpi"] = SAFE_DPI
plt.rcParams["savefig.dpi"] = SAFE_DPI
plt.rcParams["figure.autolayout"] = True
plt.rcParams["savefig.bbox"] = "tight"


def _apply_kid_style(ax, title: Optional[str] = None) -> None:
    ax.set_facecolor("#FFF8F0")
    if title:
        ax.set_title(title, fontsize=18, fontweight="bold", color="#2D2D2D", pad=16)
    ax.tick_params(axis="both", which="major", labelsize=12)
    for spine in ax.spines.values():
        spine.set_visible(False)


def fig_to_png_bytes(fig) -> bytes:
    """Serialize a Matplotlib figure to PNG bytes with safe DPI and tight bbox."""
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=SAFE_DPI, bbox_inches="tight")
    buf.seek(0)
    return buf.read()


def _limit_ticks(ax, tick_min: int, tick_max: int) -> None:
    span = max(1, tick_max - tick_min)
    # Aim for <= 40 ticks for readability and performance
    step = max(1, span // 40)
    ticks = np.arange(tick_min, tick_max + 1, step)
    ax.set_xticks(ticks)


def create_number_line_with_jumps(
    origin: int,
    jumps: List[int],
    tick_min: Optional[int] = None,
    tick_max: Optional[int] = None,
    title: Optional[str] = None,
) -> plt.Figure:
    """Create a number line with curved arrow jumps.

    - origin: starting value on the number line
    - jumps: list of integers (positive forward, negative backward)
    - tick_min/tick_max: range to display; computed if not provided
    """
    # Determine range
    positions = [origin]
    current = origin
    for j in jumps:
        current += j
        positions.append(current)

    min_pos = min(positions)
    max_pos = max(positions)
    span = max(5, max_pos - min_pos)

    if tick_min is None:
        tick_min = min_pos - max(2, span // 5)
    if tick_max is None:
        tick_max = max_pos + max(2, span // 5)

    fig, ax = plt.subplots(figsize=(10, 3), dpi=SAFE_DPI)

    # Draw baseline
    ax.hlines(0, tick_min - 0.5, tick_max + 0.5, color="#2D2D2D", linewidth=2)

    # Ticks
    _limit_ticks(ax, tick_min, tick_max)
    ax.set_yticks([])

    # Jumps as curved arrows
    current = origin
    for idx, j in enumerate(jumps):
        direction = 1 if j >= 0 else -1
        end = current + j
        color = PALETTE[idx % len(PALETTE)]
        style = mpatches.FancyArrowPatch(
            (current, 0),
            (end, 0),
            connectionstyle=f"arc3,rad={0.25 * direction}",
            arrowstyle="Simple,head_length=10,head_width=6,tail_width=2",
            color=color,
            linewidth=2,
        )
        ax.add_patch(style)
        # Label the size of the jump
        mid = (current + end) / 2
        ax.text(
            mid,
            0.9 + 0.15 * (idx % 3),
            f"{j:+}",
            ha="center",
            va="bottom",
            fontsize=14,
            color=color,
            fontweight="bold",
        )
        current = end

    # Mark origin and final
    ax.scatter([origin], [0], s=60, color="#2D2D2D", zorder=3)
    ax.scatter([current], [0], s=80, color="#2D2D2D", zorder=3)
    ax.text(origin, -0.4, f"start {origin}", ha="center", va="top", fontsize=12)
    ax.text(current, -0.4, f"end {current}", ha="center", va="top", fontsize=12)

    _apply_kid_style(ax, title)
    ax.set_xlim(tick_min - 0.5, tick_max + 0.5)
    fig.tight_layout()
    return fig


def create_array_model(
    rows: int,
    cols: int,
    fill_until: Optional[int] = None,
    title: Optional[str] = None,
) -> plt.Figure:
    """Draw a rows x cols array (multiplication model). Optionally animate fill order.

    - fill_until: how many cells to fill (left-to-right, top-to-bottom). If None, fill all.
    """
    if rows <= 0 or cols <= 0:
        rows, cols = 1, 1

    total = rows * cols
    if fill_until is None:
        fill_until = total
    fill_until = max(0, min(fill_until, total))

    cell_in = 0.7
    width_in = min(14, max(4, cols * cell_in))
    height_in = min(10, max(3, rows * cell_in))
    fig, ax = plt.subplots(figsize=(width_in, height_in), dpi=SAFE_DPI)

    # Draw grid
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            filled = idx < fill_until
            color = PALETTE[(r % len(PALETTE))] if filled else "#E7E2DC"
            rect = mpatches.Rectangle((c, rows - 1 - r), 1, 1, facecolor=color, edgecolor="#FFFFFF", linewidth=2)
            ax.add_patch(rect)

    # Ticks and styling
    ax.set_xticks(np.arange(0, cols + 1, 1))
    ax.set_yticks(np.arange(0, rows + 1, 1))
    ax.grid(False)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    _apply_kid_style(ax, title)
    fig.tight_layout()
    return fig


def create_grouping_model(
    total: int,
    group_size: int,
    step_groups: Optional[int] = None,
    items_per_row: int = 12,
    title: Optional[str] = None,
) -> plt.Figure:
    """Visualize division as grouping: color items by groups of size group_size.

    - step_groups: show only the first N complete groups (for step-by-step). If None, show all groups.
    - items_per_row: layout width for the dot grid.
    """
    total = max(0, int(total))
    group_size = max(1, int(group_size))

    quotient = total // group_size
    remainder = total % group_size

    if step_groups is None:
        step_groups = quotient
    step_groups = max(0, min(step_groups, quotient))

    # Layout
    cols = max(6, min(items_per_row, 20))
    rows = int(math.ceil(total / cols)) if total > 0 else 1

    fig_height = min(10, 1 + rows * 0.7)
    fig_width = min(14, 1 + cols * 0.6)
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=SAFE_DPI)

    # Draw items as circles
    for idx in range(total):
        r = idx // cols
        c = idx % cols
        group_index = idx // group_size
        is_complete_group = group_index < step_groups
        in_remainder = idx >= quotient * group_size

        if in_remainder:
            color = "#BBBBBB"  # remainder shown in gray
        elif is_complete_group:
            color = PALETTE[group_index % len(PALETTE)]
        else:
            color = "#E7E2DC"  # not yet grouped

        circle = mpatches.Circle(
            (c + 0.5, rows - 1 - r + 0.5),
            radius=0.25,
            facecolor=color,
            edgecolor="#FFFFFF",
            linewidth=2,
        )
        ax.add_patch(circle)

    # Legend-like labels
    ax.text(
        0,
        rows + 0.4,
        f"Group size: {group_size}  |  Groups made: {step_groups}/{quotient}  |  Remainder: {remainder}",
        ha="left",
        va="bottom",
        fontsize=14,
        color="#2D2D2D",
        fontweight="bold",
    )

    # Styling
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows + 1)
    ax.set_xticks([])
    ax.set_yticks([])

    _apply_kid_style(ax, title)
    fig.tight_layout()
    return fig


def create_combine_takeaway_dots(
    count_a: int,
    count_b: int,
    mode: str = "add",
    items_per_row: int = 12,
    title: Optional[str] = None,
) -> plt.Figure:
    """Show two sets of dots combined (add) or with some crossed out (subtract).

    - mode: "add" or "subtract" (subtract means b is taken away from a)
    - For add: first A in one color, then B in another color, total underneath
    - For subtract: show A dots, and mark B of them as faded/outlined
    """
    count_a = max(0, int(count_a))
    count_b = max(0, int(count_b))

    if mode not in {"add", "subtract"}:
        mode = "add"

    if mode == "subtract":
        total = max(0, count_a)
        to_remove = min(count_a, count_b)
    else:
        total = count_a + count_b
        to_remove = 0

    cols = max(6, min(items_per_row, 20))
    rows = int(math.ceil(total / cols)) if total > 0 else 1

    fig, ax = plt.subplots(figsize=(min(14, 1 + cols * 0.6), min(8, 1 + rows * 0.7)), dpi=SAFE_DPI)

    # Draw dots
    for idx in range(total):
        r = idx // cols
        c = idx % cols
        # Determine color
        if mode == "add":
            color = PALETTE[0] if idx < count_a else PALETTE[2]
            alpha = 1.0
            cross = False
        else:
            # subtract mode
            color = PALETTE[0]
            alpha = 0.3 if idx < to_remove else 1.0
            cross = idx < to_remove

        circle = mpatches.Circle((c + 0.5, rows - 1 - r + 0.5), 0.28, facecolor=color, edgecolor="#FFFFFF", linewidth=2, alpha=alpha)
        ax.add_patch(circle)
        if cross:
            ax.text(c + 0.5, rows - 1 - r + 0.5, "✖", ha="center", va="center", fontsize=18, color="#2D2D2D", fontweight="bold")

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows + 1)
    ax.set_xticks([])
    ax.set_yticks([])

    _apply_kid_style(ax, title)
    fig.tight_layout()
    return fig
