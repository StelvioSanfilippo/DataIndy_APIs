# Advanced Statistics

APIs for advanced statistical modeling, probability analysis, multivariate methods, regression analysis, and specialized statistical techniques.

## APIs

This category includes APIs for tasks such as:

* `fit_linear_regression`
* `fit_multiple_regression`
* `fit_logistic_regression`
* `fit_polynomial_regression`
* `fit_ridge_regression`
* `fit_lasso_regression`
* `calculate_regression_diagnostics`
* `calculate_odds_ratio`
* `calculate_probability_distribution`
* `fit_probability_distribution`
* `perform_bootstrap_analysis`
* `perform_monte_carlo_simulation`
* `perform_principal_component_analysis`
* `perform_factor_analysis`
* `perform_cluster_analysis`
* `perform_multivariate_analysis`
* `calculate_partial_correlation`
* `calculate_multiple_correlation`
* `perform_survival_analysis`
* `perform_power_analysis`

## API Requirements

Advanced Statistics APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the statistical method, model, or technique being used.
* Clearly identify required assumptions and relevant limitations.
* Validate data against the assumptions of the selected statistical method when appropriate.
* Report important model or statistical results clearly.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the advanced statistical operation.

Function names should use `snake_case`.

Examples:

* `fit_linear_regression`
* `fit_multiple_regression`
* `fit_logistic_regression`
* `fit_polynomial_regression`
* `fit_ridge_regression`
* `fit_lasso_regression`
* `calculate_regression_diagnostics`
* `calculate_odds_ratio`
* `calculate_probability_distribution`
* `fit_probability_distribution`
* `perform_bootstrap_analysis`
* `perform_monte_carlo_simulation`
* `perform_principal_component_analysis`
* `perform_factor_analysis`
* `perform_cluster_analysis`
* `perform_multivariate_analysis`
* `calculate_partial_correlation`
* `calculate_multiple_correlation`
* `perform_survival_analysis`
* `perform_power_analysis`

Each API should have its own directory and README documenting its metadata, parameters, statistical method or model, assumptions, return type, and usage.
