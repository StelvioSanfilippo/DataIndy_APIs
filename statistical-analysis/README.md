# Statistical Analysis

APIs for performing statistical calculations, hypothesis tests, comparisons, and analysis of relationships within datasets.

## APIs

This category includes APIs for tasks such as:

* `calculate_descriptive_statistics`
* `calculate_correlation`
* `calculate_covariance`
* `calculate_percentiles`
* `calculate_frequency_distribution`
* `calculate_confidence_interval`
* `perform_hypothesis_test`
* `perform_t_test`
* `perform_anova`
* `perform_chi_square_test`
* `calculate_effect_size`
* `calculate_p_value`
* `test_normality`
* `test_variance`
* `compare_groups`

## API Requirements

Statistical Analysis APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the statistical method used.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the statistical operation.

Function names should use `snake_case`.

Examples:

* `calculate_descriptive_statistics`
* `calculate_correlation`
* `calculate_covariance`
* `calculate_percentiles`
* `calculate_frequency_distribution`
* `calculate_confidence_interval`
* `perform_hypothesis_test`
* `perform_t_test`
* `perform_anova`
* `perform_chi_square_test`
* `calculate_effect_size`
* `calculate_p_value`
* `test_normality`
* `test_variance`
* `compare_groups`

Each API should have its own directory and README documenting its metadata, parameters, statistical method, return type, and usage.
