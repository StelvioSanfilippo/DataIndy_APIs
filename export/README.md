# Export

APIs for preparing analytical results and datasets for export into supported output formats and downstream workflows.

## APIs

This category includes APIs for tasks such as:

* `export_to_csv`
* `export_to_json`
* `export_to_excel`
* `export_to_html`
* `export_to_markdown`
* `export_to_parquet`
* `export_table`
* `export_analysis_results`
* `export_summary`
* `prepare_export_data`
* `format_export_data`
* `convert_output_format`

## API Requirements

Export APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the output format and required data structure.
* Return a supported result type: Table, Figure, or JSON object.
* Not write files directly to the filesystem.
* Not access external storage, databases, networks, or external services.
* Prepare export-ready data or output representations for handling by the DataIndy platform.
* Ensure exported data preserves relevant values, column names, and data types when applicable.

## API Naming

Use clear, action-oriented Python function names that describe the export operation.

Function names should use `snake_case`.

Examples:

* `export_to_csv`
* `export_to_json`
* `export_to_excel`
* `export_to_html`
* `export_to_markdown`
* `export_to_parquet`
* `export_table`
* `export_analysis_results`
* `export_summary`
* `prepare_export_data`
* `format_export_data`
* `convert_output_format`

Each API should have its own directory and README documenting its metadata, parameters, return type, output format, and usage.
