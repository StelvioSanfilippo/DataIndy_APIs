# Machine Learning

APIs for preparing data for machine learning, training models, generating predictions, and evaluating model performance.

## APIs

This category includes APIs for tasks such as:

* `split_dataset`
* `train_linear_regression`
* `train_logistic_regression`
* `train_decision_tree`
* `train_random_forest`
* `train_gradient_boosting`
* `train_knn_model`
* `train_naive_bayes`
* `train_svm_model`
* `generate_predictions`
* `evaluate_model`
* `calculate_classification_metrics`
* `calculate_regression_metrics`
* `calculate_feature_importance`
* `cross_validate_model`
* `tune_model_parameters`

## API Requirements

Machine Learning APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the target column, feature columns, and modeling assumptions when required.
* Use appropriate methods for handling missing values, categorical data, and feature types when required.
* Clearly identify the model or algorithm being used.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the machine learning operation.

Function names should use `snake_case`.

Examples:

* `split_dataset`
* `train_linear_regression`
* `train_logistic_regression`
* `train_decision_tree`
* `train_random_forest`
* `train_gradient_boosting`
* `train_knn_model`
* `train_naive_bayes`
* `train_svm_model`
* `generate_predictions`
* `evaluate_model`
* `calculate_classification_metrics`
* `calculate_regression_metrics`
* `calculate_feature_importance`
* `cross_validate_model`
* `tune_model_parameters`

Each API should have its own directory and README documenting its metadata, parameters, model or algorithm, return type, and usage.
