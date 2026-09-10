# Python Data Processing & API Integration System

## Project Description

This project is a Python-based Data Processing and API Integration System.

It gets data from an external REST API, validates the data, transforms it, stores the processed data in JSON and CSV files, and maintains logs for monitoring and error handling.

## Project Flow

External API
↓
Python API Client
↓
Data Validation
↓
Data Transformation
↓
Processing
↓
JSON/CSV Storage
↓
Logging and Error Handling

## Project Files

### api_client.py
Connects to the external REST API and gets JSON data.

### validation.py
Validates the incoming API data.

### transformation.py
Transforms the API data into the required format.

### storage.py
Stores processed data in JSON and CSV files.

### main.py
Connects all modules and runs the complete data-processing workflow.

### test_data_processing.py
Contains unit tests for validation and transformation functions.

### result.json
Stores processed data in JSON format.

### result.csv
Stores processed data in CSV format.

### application.log
Stores application logs and error information.

## Technologies Used

- Python
- Requests library
- JSON
- CSV
- Logging
- unittest
- REST API

## How to Run

1. Install Python.
2. Install the requests library.
3. Open the project in Visual Studio.
4. Run `main.py`.
5. Check `result.json` and `result.csv` for processed data.
6. Check `application.log` for logs.
7. Run `test_data_processing.py` to execute unit tests.

## API Used

JSONPlaceholder REST API.

## Unit Testing

The project contains 3 unit tests.

All tests pass successfully.

Example output:

Ran 3 tests in 0.000s

OK

## Output

The application successfully:

- Retrieves data from the API.
- Validates the incoming data.
- Transforms the data.
- Saves data to JSON and CSV.
- Records application logs.
- Handles API errors and timeout errors.

## Conclusion

This project demonstrates Python API integration, data validation, data transformation, file storage, logging, error handling, and unit testing.