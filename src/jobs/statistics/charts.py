from matplotlib import pyplot
from matplotlib.patheffects import withStroke
from config import STATISTICS_CHARTS_DIRECTORY

def generate_chart(title: str, description: str, image_name: str, x_items: list[int], y_items: list[str]):
    WHITE = "white"
    BLUE = "#076fa2"
    BLACK = "black"
    GREY = "#A8BAC4"
    y = [i * 0.9 for i in range(len(y_items))]
    figure, axis = pyplot.subplots(figsize=(12, 7))
    axis.barh(y, x_items, height=0.55, align="edge", color=BLUE)
    max_x = max(x_items)
    x_jump = max_x / len(x_items)
    ticks = [round(i * x_jump, 2) for i in range(0, len(x_items))] + [max_x]
    axis.xaxis.set_ticks(ticks)
    axis.xaxis.set_ticklabels(ticks, size=16, fontweight=100)
    axis.xaxis.set_tick_params(labelbottom=False, labeltop=True, length=0)
    axis.set_xlim((-x_jump, max_x + x_jump))
    axis.set_ylim((0, len(y_items) * 0.9 - 0.2))
    axis.grid(axis="x", color=GREY, lw=1.2)
    axis.spines["right"].set_visible(False)
    axis.spines["top"].set_visible(False)
    axis.spines["bottom"].set_visible(False)
    axis.spines["bottom"].set_visible(False)
    axis.spines["left"].set_visible(False)
    axis.yaxis.set_visible(False)
    for name, count, y_pos in zip(y_items, x_items, y):
        axis.text(
            x_jump * .05, 
            y_pos + 0.5 / 2, 
            name, 
            color=BLACK, 
            fontsize=12,
            va="center",
            path_effects=[withStroke(linewidth=0, foreground=WHITE)]
        ) 
    figure.subplots_adjust(left=0.005, right=1, top=0.8, bottom=0.1)
    figure.text(0.02, 0.925, title, fontsize=18, fontweight="bold")
    figure.text(0.02, 0.875, description, fontsize=14)
    figure.set_facecolor(WHITE)
    figure.savefig(f"{STATISTICS_CHARTS_DIRECTORY}/{image_name}.png")