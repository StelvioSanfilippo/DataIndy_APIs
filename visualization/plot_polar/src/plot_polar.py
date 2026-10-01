def plot_polar(
    df,
    category_column=None,
    value_column=None,
    color_map="viridis",
    title=None
):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    if not category_column or category_column not in df.columns:
        return {
            "message": "Please provide a valid 'category_column'."
        }

    if not value_column or value_column not in df.columns:
        return {
            "message": "Please provide a valid 'value_column'."
        }

    if not df[value_column].dtype.kind in "biufc":
        return {
            "message": f"Column '{value_column}' must be numerical."
        }

    if category_column == value_column:
        return {
            "message": (
                "'category_column' and 'value_column' "
                "must be different."
            )
        }

    available_colors = [
        "viridis",
        "plasma",
        "inferno",
        "magma",
        "cividis",
        "coolwarm",
        "RdBu_r",
        "Blues",
        "Greens",
        "Oranges",
        "Reds",
        "Purples"
    ]

    try:
        cmap = plt.get_cmap(color_map)
    except (ValueError, TypeError):
        return {
            "message": (
                f"Color map '{color_map}' was not found. "
                f"Available recommended color maps: {available_colors}"
            )
        }

    data = df[
        [
            category_column,
            value_column
        ]
    ].copy()

    data[value_column] = data[value_column].replace(
        [np.inf, -np.inf],
        np.nan
    )

    data = data.dropna(
        subset=[
            category_column,
            value_column
        ]
    )

    if data.empty:
        return {
            "message": "No usable rows were found."
        }

    if len(data) < 2:
        return {
            "message": "At least two usable rows are required."
        }

    # Use category order from the DataFrame.
    categories = [
        str(value)
        for value in data[category_column]
    ]

    values = data[
        value_column
    ].to_numpy(dtype=float)

    angles = np.linspace(
        0,
        2 * np.pi,
        len(values),
        endpoint=False
    )

    # Close the circular line
    closed_angles = np.append(
        angles,
        angles[0]
    )

    closed_values = np.append(
        values,
        values[0]
    )

    figure_size = max(
        7,
        min(12, 6 + len(values) * 0.15)
    )

    fig, ax = plt.subplots(
        figsize=(figure_size, figure_size),
        subplot_kw={
            "projection": "polar"
        }
    )

    color = cmap(0.6)

    ax.plot(
        closed_angles,
        closed_values,
        color=color,
        linewidth=2,
        label=value_column
    )

    ax.fill(
        closed_angles,
        closed_values,
        color=color,
        alpha=0.2
    )

    ax.scatter(
        angles,
        values,
        color=color,
        s=60,
        zorder=3
    )

    ax.set_xticks(
        angles
    )

    ax.set_xticklabels(
        categories
    )

    ax.set_title(
        title or f"Polar Chart of {value_column}",
        pad=25
    )

    ax.set_ylabel(
        value_column,
        labelpad=20
    )

    ax.legend(
        title="Series",
        loc="upper right",
        bbox_to_anchor=(1.15, 1.1)
    )

    ax.grid(
        True,
        alpha=0.3
    )

    fig.tight_layout()

    return fig
