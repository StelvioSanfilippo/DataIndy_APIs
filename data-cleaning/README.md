# Data Cleaning

APIs for preparing datasets by identifying, removing, correcting, or standardizing data issues.

## APIs

This category includes APIs for tasks such as:

* `remove_missing_values`
* `remove_duplicate_rows`
* `replace_missing_values`
* `detect_invalid_values`
* `standardize_column_values`
* `convert_data_types`
* `remove_outliers`
* `trim_text_values`
* `validate_data_types`

## API Requirements

Data Cleaning APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the cleaning operation.

Function names should use `snake_case`.

Examples:

* `remove_missing_values`
* `remove_duplicate_rows`
* `replace_missing_values`
* `detect_invalid_values`
* `standardize_column_values`
* `convert_data_types`
* `remove_outliers`
* `trim_text_values`
* `validate_data_types`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.

