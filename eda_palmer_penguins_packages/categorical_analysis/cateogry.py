import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_category_count(
    df, category_columns, color_palette, figsize=(20, 5), alpha=0.6
):
    """
    Plot histograms for each category column in the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the data.
    category_columns (list): The list of category columns to plot.
    color_palette (list): The color palette for the histograms.
    figsize (tuple): The size of the figure.
    alpha (float): The transparency of the histograms.

    Returns:
    None
    """
    fig, axs = plt.subplots(1, len(category_columns), figsize=figsize)
    for i, category in enumerate(category_columns):
        sns.countplot(
            x=category,
            data=df,
            ax=axs[i],
            palette=color_palette,
            alpha=alpha,
        )
        axs[i].set_title(f"{category} Count")
        axs[i].set_xlabel(category)
        axs[i].set_ylabel("Count")


def plot_category_proportions(
    df, category_columns, color_palette=None, figsize=(10, 5)
):
    """
    Plot stacked bar charts for each category column in the DataFrame to show proportions.

    Parameters:
    df (DataFrame): The DataFrame containing the data.
    category_columns (list): The list of category columns to plot.
    figsize (tuple): The size of the figure.

    Returns:
    None
    """
    num_subplots = len(category_columns)

    fig, axs = plt.subplots(1, num_subplots, figsize=figsize)

    if num_subplots == 1:
        axs = [axs]

    for i, category in enumerate(category_columns):

        # Get the proportion of each category
        proportions = df[category].value_counts(normalize=True) * 100

        proportions = proportions.sort_index()

        proportions_df = pd.DataFrame(
            {"proportion": proportions, "category": proportions.index}
        )

        sns.barplot(
            ax=axs[i],
            data=proportions_df,
            x="category",
            y="proportion",
            palette=color_palette,
        )

        for p in axs[i].patches:
            height = p.get_height()
            axs[i].text(
                p.get_x() + p.get_width() / 2.0,
                height + 1,
                f"{height:.2f}%",
                ha="center",
            )

        axs[i].set_title(f"Proportion of {category}")
        axs[i].set_xlabel(category)
        axs[i].set_ylabel("Proportion (%)")
        axs[i].set_ylim(0.0, 100)

        axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation=45, ha="right")


def plot_categorical_vs_numeric(
    df, category_columns, numeric_columns, plot_type="violin", palette=None
):
    """
    Plot categorical vs numeric columns using either violinplot or boxplot.

    Parameters:
    df (DataFrame): The DataFrame containing the data.
    category_columns (list): The list of category columns to plot.
    numeric_columns (list): The list of numeric columns to plot.
    plot_type (str): The type of plot to generate, either 'violin' or 'box'.
    palette (str or list, optional): The color palette for the plots.

    Returns:
    None
    """
    num_rows = len(category_columns)
    num_cols = len(numeric_columns)

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 15))

    for i, i_col in enumerate(category_columns):
        for j, j_col in enumerate(numeric_columns):
            if plot_type == "violin":
                sns.violinplot(
                    split=True if i == 2 else False,
                    ax=axs[i, j],
                    data=df,
                    x="species",
                    y=j_col,
                    hue=i_col,
                    palette=palette,
                )
            elif plot_type == "box":
                sns.boxplot(
                    ax=axs[i][j],
                    data=df,
                    x="species",
                    y=j_col,
                    hue=i_col,
                    palette=palette,
                )
            else:
                raise ValueError("plot_type must be either 'violin' or 'box'")

            axs[i][j].set_title(j_col if i == 0 else None)
            axs[i][j].set_xlabel(None)
            axs[i][j].set_ylabel(None)
