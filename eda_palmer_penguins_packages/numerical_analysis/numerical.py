import matplotlib.pyplot as plt
import seaborn as sns


def plot_histograms(
    df,
    numerical_stats,
    color_palette,
    figsize=(20, 5),
    bins=50,
    alpha=0.55,
    color="#0f7175ff",
    kde=True,
):
    """
    Plot histograms for each numerical column in the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the data.
    numerical_stats (DataFrame): The DataFrame containing the numerical statistics.
    color_palette (list): The color palette for the histograms.
    figsize (tuple): The size of the figure.
    bins (int): The number of bins for the histograms.
    alpha (float): The transparency of the histograms.
    color (str): The color of the histograms.
    kde (bool): Whether to plot a kernel density estimate.

    Returns:
    None
    """

    fig, ax = plt.subplots(1, len(numerical_stats.columns), figsize=figsize)
    for i, col in enumerate(numerical_stats.columns):
        sns.histplot(
            ax=ax[i],
            data=df,
            x=col,
            palette=color_palette,
            bins=bins,
            alpha=alpha,
            color=color,
            kde=kde,
        )

        ax[i].lines[0].set_color("#4c36f5")

        ax[i].axvline(
            x=numerical_stats.loc["25%", col],
            color="#f26a02",
            linestyle="dashed",
            linewidth=2.5,
            label="Q1",
        )

        ax[i].axvline(
            x=numerical_stats.loc["75%", col],
            color="#bd00b0",
            linestyle="dashed",
            linewidth=2.5,
            label="Q3",
        )

        ax[i].axvline(
            x=numerical_stats.loc["mean", col],
            color="#f75c6b",
            linestyle="dashed",
            linewidth=2.5,
            label="Mean",
        )

        ax[i].legend()


def plot_distributions(df, category_columns, numeric_columns, palette=None):
    """
    Plot histograms of numeric columns, grouped by category columns.

    Parameters:
    df (DataFrame): The DataFrame containing the data.
    category_columns (list): The list of category columns to group by.
    numeric_columns (list): The list of numeric columns to plot.
    palette (str or list, optional): The color palette for the plots.

    Returns:
    None
    """
    num_rows = len(category_columns)
    num_cols = len(numeric_columns)

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 15))

    for i, i_col in enumerate(category_columns):
        for j, j_col in enumerate(numeric_columns):
            sns.histplot(
                data=df,
                x=j_col,
                hue=i_col,
                bins=40,
                multiple="stack" if 1 == 2 else "dodge",
                palette=palette,
                kde=True,
                ax=axs[i][j],
            )

            axs[i][j].set_title((j_col) if i == 0 else None)
            axs[i, j].set_xlabel(None)
            axs[i, j].set_ylabel(None)


def plot_distribution_specie(
    df, numeric_columns, category_columns, species, penguin_color=None, bins=20
):
    """
    Plot histograms of a specified species for each numeric column, grouped by category columns.

    Parameters:
    df2 (DataFrame): The DataFrame containing the data.
    numeric_columns (list): The list of numeric columns to plot.
    category_columns (list): The list of category columns to group by.
    species (str): The species to plot ('Adelie', 'Chinstrap', etc.).
    penguin_color (str or list): The color palette for the plots.
    bins (int): The number of bins for the histograms.

    Returns:
    None
    """
    species_data = df[df["species"] == species]

    num_rows = len(numeric_columns)
    num_cols = len(category_columns)

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 13))

    for i, i_col in enumerate(numeric_columns):
        for j, j_col in enumerate(category_columns):
            sns.histplot(
                ax=axs[i][j],
                data=species_data,
                x=i_col,
                hue=j_col,
                multiple="layer",
                bins=bins,
                kde=True,
                palette=penguin_color,
            )

            (
                axs[i][j].set_ylabel(numeric_columns[i], labelpad=60, rotation=0)
                if j == 0
                else axs[i][j].set_ylabel(None)
            )
            axs[i][j].set_xlabel(None)
    fig.suptitle(f"{species} Species")
    plt.subplots_adjust(top=0.95)
