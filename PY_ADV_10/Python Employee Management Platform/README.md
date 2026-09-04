# Python Employee Management Platform

## Project Overview

The Python Employee Management Platform is a simple employee management system developed using Python, Flask, SQLite, and Pandas.

## Features

* Create employee
* Update employee
* Delete employee
* Search employee
* List employees
* Store employee data in SQLite database
* REST APIs using Flask
* API request validation
* Exception handling
* Application logging
* Unit testing
* Employee data analysis using Pandas
* Basic employee statistics

## Technologies Used

* Python
* Flask
* SQLite
* Pandas
* unittest
* Git

## Project Structure

```text
Python Employee Management Platform/
│
├── app.py
├── database.py
├── models.py
├── services.py
├── validation.py
├── logging_config.py
├── employee_analysis.py
├── README.md
│
├── data/
│   ├── employees.csv
│   └── clean_employees.csv
│
├── logs/
│   └── app.log
│
└── tests/
    └── test_employee.py
```

## How to Run

### 1. Activate Virtual Environment

```text
venv\Scripts\activate
```

### 2. Create Database

```text
python database.py
```

### 3. Run Flask Application

```text
python app.py
```

The application runs on:

```text
http://127.0.0.1:5000
```

## Employee APIs

### Create Employee

```text
POST /employees
```

### List Employees

```text
GET /employees
```

### Search Employee

```text
GET /employees/<employee_id>
```

### Update Employee

```text
PUT /employees/<employee_id>
```

### Delete Employee

```text
DELETE /employees/<employee_id>
```

## Pandas Data Analysis

Employee data is read from the CSV file using Pandas.

The project handles missing salary values, removes duplicate records, filters employee data, saves the cleaned dataset, and generates basic statistics.

## Unit Testing

Unit tests are implemented using Python unittest.

Run tests using:

```text
python -m unittest discover tests
```

The project contains 5 unit tests.

## Logging

Application activities and errors are recorded in:

```text
logs/app.log
```

## Project Status

The Python Employee Management Platform is implemented with employee management, REST APIs, validation, exception handling, logging, Pandas analysis, statistics, and unit testing.
