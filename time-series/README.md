# Time Series Analysis

APIs for analyzing time-dependent data, identifying patterns and trends, and generating time series features and forecasts.

## APIs

This category includes APIs for tasks such as:

* `calculate_moving_average`
* `calculate_exponential_moving_average`
* `calculate_rolling_statistics`
* `calculate_growth_rate`
* `calculate_percentage_change`
* `calculate_lag_values`
* `calculate_lead_values`
* `calculate_autocorrelation`
* `decompose_time_series`
* `detect_time_series_trends`
* `detect_seasonality`
* `detect_time_series_anomalies`
* `resample_time_series`
* `forecast_time_series`

## API Requirements

Time Series Analysis APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the time-related columns and assumptions when required.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the time series operation.

Function names should use `snake_case`.

Examples:

* `calculate_moving_average`
* `calculate_exponential_moving_average`
* `calculate_rolling_statistics`
* `calculate_growth_rate`
* `calculate_percentage_change`
* `calculate_lag_values`
* `calculate_lead_values`
* `calculate_autocorrelation`
* `decompose_time_series`
* `detect_time_series_trends`
* `detect_seasonality`
* `detect_time_series_anomalies`
* `resample_time_series`
* `forecast_time_series`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.
