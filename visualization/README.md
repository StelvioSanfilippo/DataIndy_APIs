# Visualization

APIs for creating charts, plots, and other visual representations of data for analysis and reporting.

## APIs

This category includes APIs for tasks such as:

* `create_histogram`
* `create_bar_chart`
* `create_line_chart`
* `create_scatter_plot`
* `create_box_plot`
* `create_violin_plot`
* `create_pie_chart`
* `create_area_chart`
* `create_heatmap`
* `create_correlation_heatmap`
* `create_pair_plot`
* `create_density_plot`
* `create_count_plot`
* `create_time_series_plot`
* `create_distribution_plot`

## API Requirements

Visualization APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the columns and data types required for the visualization.
* Use a non-interactive plotting backend when required by the DataIndy runtime.
* Return a supported result type: Figure, Table, or JSON object.
* Ensure generated figures are suitable for display in DataIndy analysis pages and generated analysis documents.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the visualization operation.

Function names should use `snake_case`.

Examples:

* `create_histogram`
* `create_bar_chart`
* `create_line_chart`
* `create_scatter_plot`
* `create_box_plot`
* `create_violin_plot`
* `create_pie_chart`
* `create_area_chart`
* `create_heatmap`
* `create_correlation_heatmap`
* `create_pair_plot`
* `create_density_plot`
* `create_count_plot`
* `create_time_series_plot`
* `create_distribution_plot`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.
