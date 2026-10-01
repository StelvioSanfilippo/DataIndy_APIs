# Plot Polar

Creates a polar chart for visualizing a numerical value around a circular axis using categorical labels.

## Metadata

### Category

Visualization

### Name

Plot Polar

### Description

Creates a polar chart for visualizing a numerical value around a circular axis. Each row represents a category and its corresponding numerical value. The categories are displayed around the circular axis in the order they appear in the dataset.

### Function

`plot_polar`

### Parameters

#### `df`

* **Type:** pandas.DataFrame
* **Required:** Yes
* **Description:** The input dataset provided automatically by DataIndy.

#### `category_column`

* **Type:** str
* **Required:** Yes
* **Description:** Name of the column containing categories or labels to display around the circular axis.
* **Example:** `"month"`

#### `value_column`

* **Type:** str
* **Required:** Yes
* **Description:** Name of the numerical column containing the values to visualize.
* **Example:** `"sales"`

#### `color_map`

* **Type:** str
* **Required:** No
* **Default:** `"viridis"`
* **Description:** Name of the Matplotlib color map used to determine the chart color.
* **Example:** `"plasma"`

#### `title`

* **Type:** str or None
* **Required:** No
* **Default:** `None`
* **Description:** Optional title for the chart. If omitted, a title is generated automatically.

### Returns

**Figure**

Returns a Matplotlib `Figure` containing the polar chart.

## Example Parameters

```json
{
  "title": "Optional chart title.",
  "color_map": "viridis",
  "value_column": "score",
  "category_column": "country"
}
```

## Example

```python
plot_polar(
    df,
    category_column="country",
    value_column="score",
    color_map="viridis",
    title="Scores by Country"
)
```

## Requirements

* `category_column` must exist in the dataset.
* `value_column` must exist in the dataset.
* `value_column` must contain numerical data.
* `category_column` and `value_column` must be different columns.
* At least two usable rows are required.
* Rows with missing category or value data are excluded.
* Infinite numerical values are treated as missing values.
* Categories are displayed in the order they appear in the dataset.
* The specified color map must be supported by Matplotlib.
* The API uses a non-interactive Matplotlib backend suitable for the DataIndy runtime.
* The API does not perform filesystem, database, network, operating-system, or external-service access.
