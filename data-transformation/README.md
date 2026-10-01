# Data Transformation

APIs for transforming, reshaping, aggregating, and restructuring datasets for analysis.

## APIs

This category includes APIs for tasks such as:

* `transform_column`
* `rename_columns`
* `reorder_columns`
* `filter_rows`
* `sort_rows`
* `group_and_aggregate`
* `pivot_data`
* `melt_data`
* `merge_datasets`
* `join_datasets`
* `concatenate_datasets`
* `reshape_data`
* `aggregate_data`
* `normalize_data`

## API Requirements

Data Transformation APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the transformation operation.

Function names should use `snake_case`.

Examples:

* `transform_column`
* `rename_columns`
* `reorder_columns`
* `filter_rows`
* `sort_rows`
* `group_and_aggregate`
* `pivot_data`
* `melt_data`
* `merge_datasets`
* `join_datasets`
* `concatenate_datasets`
* `reshape_data`
* `aggregate_data`
* `normalize_data`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.
