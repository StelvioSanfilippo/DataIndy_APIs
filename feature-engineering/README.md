# Feature Engineering

APIs for creating, modifying, and preparing features from existing dataset columns for analysis and machine learning.

## APIs

This category includes APIs for tasks such as:

* `create_interaction_feature`
* `create_polynomial_features`
* `encode_categorical_column`
* `create_binned_feature`
* `extract_date_features`
* `calculate_ratio_feature`
* `create_group_aggregate_feature`
* `normalize_feature`
* `standardize_feature`
* `create_lag_feature`

## API Requirements

Feature Engineering APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented names that describe the feature engineering operation.

Function names should use Python `snake_case`.

Examples:

* `create_interaction_feature`
* `create_polynomial_features`
* `encode_categorical_column`
* `create_binned_feature`
* `extract_date_features`
* `calculate_ratio_feature`
* `create_group_aggregate_feature`
* `normalize_feature`
* `standardize_feature`
* `create_lag_feature`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.

