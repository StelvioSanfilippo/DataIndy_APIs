# Reporting

APIs for generating summaries, tables, charts, and structured analytical outputs for DataIndy analysis pages and automatically generated analysis documents.

## APIs

This category includes APIs for tasks such as:

* `generate_summary`
* `generate_statistics_summary`
* `generate_group_summary`
* `generate_analysis_summary`
* `generate_data_quality_summary`
* `generate_table`
* `generate_summary_table`
* `generate_comparison_table`
* `generate_frequency_table`
* `generate_report_section`
* `generate_insights`
* `generate_key_findings`
* `generate_metric_summary`
* `generate_kpi_summary`
* `generate_analysis_overview`

## API Requirements

Reporting APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the data, metrics, or analysis results being summarized.
* Produce clear and structured analytical outputs suitable for DataIndy analysis pages and generated analysis documents.
* Keep generated results concise, readable, and relevant to the requested analysis.
* Avoid unsupported claims or conclusions that are not derived from the provided data.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the reporting operation.

Function names should use `snake_case`.

Examples:

* `generate_summary`
* `generate_statistics_summary`
* `generate_group_summary`
* `generate_analysis_summary`
* `generate_data_quality_summary`
* `generate_table`
* `generate_summary_table`
* `generate_comparison_table`
* `generate_frequency_table`
* `generate_report_section`
* `generate_insights`
* `generate_key_findings`
* `generate_metric_summary`
* `generate_kpi_summary`
* `generate_analysis_overview`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.
