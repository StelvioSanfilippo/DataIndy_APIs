# Data Quality & Validation

APIs for assessing dataset quality, validating data consistency, identifying potential issues, and measuring data completeness and reliability.

## APIs

This category includes APIs for tasks such as:

* `validate_dataset`
* `validate_column`
* `check_missing_values`
* `check_duplicate_rows`
* `check_duplicate_values`
* `check_data_types`
* `check_value_ranges`
* `check_unique_values`
* `check_column_consistency`
* `check_data_completeness`
* `check_data_consistency`
* `check_data_integrity`
* `detect_anomalies`
* `detect_invalid_values`
* `calculate_data_quality_score`
* `generate_data_quality_report`

## API Requirements

Data Quality & Validation APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the quality checks or validation rules being applied.
* Report validation results clearly, including detected issues when applicable.
* Distinguish between validation failures, warnings, and informational results when appropriate.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the data quality or validation operation.

Function names should use `snake_case`.

Examples:

* `validate_dataset`
* `validate_column`
* `check_missing_values`
* `check_duplicate_rows`
* `check_duplicate_values`
* `check_data_types`
* `check_value_ranges`
* `check_unique_values`
* `check_column_consistency`
* `check_data_completeness`
* `check_data_consistency`
* `check_data_integrity`
* `detect_anomalies`
* `detect_invalid_values`
* `calculate_data_quality_score`
* `generate_data_quality_report`

Each API should have its own directory and README documenting its metadata, parameters, validation rules, return type, and usage.
