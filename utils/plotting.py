import matplotlib.pyplot as plt
import seaborn as sns


def setup_plotting():
    """
    Configure default plotting style for the project.
    Call once at the beginning of every notebook.
    """

    sns.set_theme(
        style="whitegrid",
        context="notebook",
        palette="deep"
    )

    plt.rcParams.update({
        "figure.figsize": (10, 5),
        "figure.dpi": 120,
        "savefig.dpi": 300,

        "axes.titlesize": 16,
        "axes.labelsize": 13,

        "xtick.labelsize": 11,
        "ytick.labelsize": 11,

        "legend.fontsize": 11,

        "axes.spines.top": False,
        "axes.spines.right": False,

        "axes.grid": True,
        "grid.alpha": 0.3,

        "figure.autolayout": True
    })