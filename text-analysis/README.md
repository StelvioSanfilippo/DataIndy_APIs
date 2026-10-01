# Text Analysis

APIs for analyzing, processing, transforming, and extracting information from text data within datasets.

## APIs

This category includes APIs for tasks such as:

* `calculate_text_length`
* `count_words`
* `count_characters`
* `count_sentences`
* `count_words_by_frequency`
* `extract_keywords`
* `extract_entities`
* `detect_language`
* `calculate_text_similarity`
* `calculate_text_sentiment`
* `classify_text`
* `clean_text`
* `normalize_text`
* `tokenize_text`
* `remove_stopwords`
* `calculate_text_statistics`

## API Requirements

Text Analysis APIs should:

* Accept the current Dataset provided by DataIndy when required.
* Accept additional parameters when needed.
* Define a single main function.
* Import required libraries inside the function.
* Validate input data and parameters.
* Clearly identify the text column or columns being analyzed.
* Clearly identify any assumptions about language, encoding, or text format when required.
* Handle missing or non-text values appropriately.
* Return a supported result type: Table, Figure, or JSON object.
* Avoid direct filesystem, database, network, operating-system, or external-service access.

## API Naming

Use clear, action-oriented Python function names that describe the text analysis operation.

Function names should use `snake_case`.

Examples:

* `calculate_text_length`
* `count_words`
* `count_characters`
* `count_sentences`
* `count_words_by_frequency`
* `extract_keywords`
* `extract_entities`
* `detect_language`
* `calculate_text_similarity`
* `calculate_text_sentiment`
* `classify_text`
* `clean_text`
* `normalize_text`
* `tokenize_text`
* `remove_stopwords`
* `calculate_text_statistics`

Each API should have its own directory and README documenting its metadata, parameters, return type, and usage.
