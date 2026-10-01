# Data Cleaning

APIs for preparing datasets by identifying, removing, correcting, or standardizing data issues.

## APIs

This category includes APIs for tasks such as:

* Handling missing values
* Removing duplicate records
* Detecting and handling invalid values
* Standardizing data formats
* Cleaning column values
* Converting data types
* Detecting inconsistent data
* Handling outliers
* Normalizing values
* Preparing data for analysis

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

Use clear, action-oriented names that describe the cleaning operation.

Examples:

* Remove Missing Values
* Remove Duplicate Rows
* Replace Missing Values
* Detect Invalid Values
* Standardize Column Values
* Convert Data Types
* Remove Outliers
* Trim Text Values
* Validate Data Types

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.
