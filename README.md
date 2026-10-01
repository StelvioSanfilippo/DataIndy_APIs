# DataIndy APIs

Public Python APIs for DataIndy - Indydataquest.com. Build custom analysis components for DataIndy analysis pages and automatically generated analysis documents.

## About

This repository contains Python APIs designed to extend the analytical capabilities of the DataIndy platform.

Each API performs a specific data analysis, transformation, visualization, or supporting operation. API results can be incorporated into DataIndy analysis pages and automatically included in generated analysis documents.

The DataIndy platform itself is proprietary software. This repository contains only the API components made available under the license included with this repository.

## API Categories

APIs are organized into the following categories:

1. **Utilities / Helpers**
2. **Data Cleaning**
3. **Feature Engineering**
4. **Data Transformation**
5. **Statistical Analysis**
6. **Time Series Analysis**
7. **Machine Learning**
8. **Visualization**
9. **Data Quality & Validation**
10. **Text Analysis**
11. **Advanced Statistics**
12. **Reporting**
13. **Export**

## How DataIndy APIs Work

DataIndy APIs are Python functions that operate on data supplied by the DataIndy platform.

An API can:

* Use the current Dataset provided by DataIndy.
* Accept additional parameters.
* Perform a specific analytical operation.
* Return a table, figure, or JSON object.
* Be incorporated into a DataIndy analysis page.
* Contribute results to automatically generated analysis documents.

APIs should be self-contained and should not require direct access to external resources.

## API Structure

Each API should define a single main function.

A typical API has the following structure:

```text
category/
└── api-name/
    ├── README.md
    ├── src/
    ├── tests/
    └── examples/
```

The API documentation should describe:

* Category
* API name
* Description
* Parameters
* Return type
* Usage or examples where appropriate

## API Development Rules

### 1. Define a Single Function

Each API must define a single function that implements the API operation.

The function may:

* Accept parameters.
* Use the current Dataset supplied by DataIndy.
* Perform the required computation.
* Return the API result.

### 2. Import Libraries Inside the Function

Python libraries required by an API should be imported inside the API function.

For example:

```python
def calculate_statistics(df):
    import pandas as pd
    import numpy as np

    # API logic
```

This keeps each API self-contained and makes its dependencies explicit.

### 3. Return a Supported Result

An API must return one of the supported result types:

* **Table** — typically a `pandas.DataFrame`
* **Figure** — typically a `matplotlib.figure.Figure`
* **JSON object** — a JSON-serializable object such as a dictionary or list

The returned result should contain the information required by DataIndy to incorporate the API output into an analysis page or generated analysis document.

### 4. No Direct External I/O

For security reasons, APIs must operate on the Dataset and parameters provided to them and should not directly access external resources.

APIs must not:

* Read from or write to the local filesystem.
* Access databases directly.
* Make HTTP or network requests.
* Download or upload files.
* Execute shell commands or external processes.
* Access operating-system resources.
* Access environment variables or secrets.
* Connect to external services.

APIs should perform their analysis using the data and parameters available to the function.

## API Template

The following template can be used when creating a new API:

```python
def my_new_api(df, parameter1=None, parameter2=None):
    """
    Example API template.

    Parameters
    ----------
    df : pandas.DataFrame
        The input dataset provided automatically by the platform.
    parameter1 : any, optional
        Example parameter description.
    parameter2 : any, optional
        Example parameter description.

    Returns
    -------
    pandas.DataFrame, matplotlib.figure.Figure, dict, or JSON-serializable object
        The result of the API computation.
    """
    import matplotlib
    matplotlib.use("Agg")  # Ensure non-interactive backend
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    # --- Example logic ---
    # Detect numerical columns
    num_cols = df.select_dtypes(include="number").columns

    # If no numerical columns, return a message
    if len(num_cols) == 0:
        return {"message": "No numerical columns found in the dataset."}

    # Create a simple plot
    fig, ax = plt.subplots(figsize=(6.5, 4.0), dpi=150)
    ax.plot(
        df.index[:10],
        df[num_cols[0]].iloc[:10],
        marker="o"
    )

    ax.set_title(f"{num_cols[0]} values (example output)")
    ax.set_xlabel("Index")
    ax.set_ylabel(num_cols[0])

    plt.tight_layout()
    plt.draw()

    return fig
```

## API Metadata

Each API should provide metadata describing its purpose and interface.

### Category

The category in which the API belongs.

Example:

```text
Category:
Time Series Analysis
```

### Name

The API name should be short, descriptive, and action-oriented.

A recommended naming pattern is:

```text
[Action] [Object]
```

or:

```text
[Action] [Object] by [Method/Dimension]
```

Examples:

```text
Calculate_descriptive_statistics
Detect_outliers
Create_histogram
Calculate_moving_average
Remove_missing_values
```

Use clear action words such as:

* Calculate
* Create
* Detect
* Remove
* Transform
* Compare
* Generate
* Encode
* Normalize
* Aggregate
* Validate

Avoid vague names such as:

```text
Data_tool
Analysis_helper
Process_data
My_API
```

The corresponding Python function should use `snake_case` and clearly correspond to the API name.

Example:

```text
Calculate Moving Average
```

```python
def calculate_moving_average(...):
```

### Description

The description should clearly explain:

1. What the API does.
2. What data or columns it operates on.
3. What it returns.

A useful structure is:

```text
[Action] [object/data] using [method or condition].
Returns [result].
```

Descriptions should be concise, written in plain language, and include important assumptions or limitations when necessary.

### Parameters

Document every parameter used by the API.

Each parameter should specify:

* Name
* Data type
* Required or optional
* Default value
* Description
* Allowed values or range, when applicable

Use descriptive parameter names such as:

```text
column
group_column
value_column
window_size
threshold
method
include_missing
confidence_level
```

Avoid vague names such as:

```text
x
y
value
option
input
param1
param2
```

Parameters should use sensible defaults when appropriate, and invalid values should produce clear error messages.

### Example Metadata

```text
Category:
Time Series Analysis

Name:
Calculate Moving Average

Description:
Calculates a moving average for a selected numeric column and returns
the resulting values as a table.

Parameters:

column
Type: str
Required: Yes
Description: Name of the numeric column to analyze.

window_size
Type: int
Required: No
Default: 7
Description: Number of observations included in the moving window.
Allowed values: Integer greater than 0.

Returns:
Table
```

## Creating a New API

When creating a new API:

1. Select the appropriate category.
2. Create a directory for the API.
3. Define the API metadata.
4. Define a single Python function.
5. Import required libraries inside the function.
6. Validate parameters and input data.
7. Implement the analytical operation.
8. Return a supported result type.
9. Add tests where appropriate.
10. Document the API and provide examples when useful.

## Repository Structure

```text
dataindy-apis/
├── utilities/
├── data-cleaning/
├── feature-engineering/
├── data-transformation/
├── statistical-analysis/
├── time-series/
├── machine-learning/
├── visualization/
├── data-quality/
├── text-analysis/
├── advanced-statistics/
├── reporting/
└── export/
```

Example:

```text
statistical-analysis/
└── correlation/
    ├── README.md
    ├── src/
    ├── tests/
    └── examples/
```

## Security

DataIndy APIs are intended to execute analytical operations within the DataIndy environment.

To reduce security risks, API implementations should remain isolated from external resources and operate only on the supplied Dataset and function parameters.

Do not include credentials, secrets, tokens, private keys, or other sensitive information in API code.

## Contributing

Contributions to the API collection are welcome where they follow the API development rules and repository guidelines.

New APIs should:

* Have a clear and specific purpose.
* Belong to an appropriate category.
* Follow the API naming conventions.
* Define a single main function.
* Import dependencies inside the function.
* Avoid direct external I/O.
* Return a supported result type.
* Include appropriate documentation.
* Include tests where practical.

## License

The API source code in this repository is provided under the **DataIndy API License**.

The license permits specified forms of use, modification, and distribution while restricting use of the API collection for products or services that compete with the DataIndy platform.

The license applies **only to the source code contained in this repository**.

The DataIndy platform, application, services, branding, proprietary code, and other materials not contained in this repository are not licensed under the DataIndy API License.

See the `LICENSE` file for the complete terms.

```

---

This version deliberately leaves the exact **competitive-use language** to the custom `LICENSE` file, where we can define it precisely rather than making the README itself legally ambiguous.
```
