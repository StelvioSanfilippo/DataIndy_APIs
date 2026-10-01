# Utilities / Helpers

General-purpose utility APIs and helper functions for DataIndy.

## APIs

This category includes APIs for tasks such as:

* `get_column_information`
* `get_dataset_summary`
* `get_unique_values`
* `calculate_column_statistics`
* `detect_column_types`
* `check_column_exists`
* `get_dataset_shape`
* `get_numeric_columns`
* `get_categorical_columns`

## API Requirements

Utilities / Helpers APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the utility operation.

Function names should use `snake_case`.

Examples:

* `get_column_information`
* `get_dataset_summary`
* `get_unique_values`
* `calculate_column_statistics`
* `detect_column_types`
* `check_column_exists`
* `get_dataset_shape`
* `get_numeric_columns`
* `get_categorical_columns`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.

