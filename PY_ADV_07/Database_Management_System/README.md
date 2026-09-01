# Employee Management System

## Project Description

This is a Python and PostgreSQL based Employee Management System.

The project connects Python with PostgreSQL using the Psycopg 3 library and performs employee database operations.

The project includes CRUD operations, employee search, validation, transactions, service-layer functions, and automated testing using pytest.

## Technologies Used

* Python
* PostgreSQL
* Psycopg 3
* SQL
* Pytest
* Git and GitHub

## Features

* PostgreSQL database connection
* Create database tables
* Insert employee records
* Fetch employee records
* Search employees
* Update employee records
* Delete employee records
* Employee ID and salary validation
* Transaction handling
* Employee service layer
* Automated database tests
* Automated validation tests

## Project Structure

```text
Database_Management_System/
│
├── database/
│   ├── connection.py
│   ├── schema.sql
│   ├── create_tables.py
│   ├── insert_data.py
│   ├── fetch_data.py
│   ├── update_employee.py
│   ├── delete_employee.py
│   ├── search_employee.py
│   ├── validation.py
│   ├── employee_service.py
│   ├── transaction_demo.py
│   ├── test_validation.py
│   └── test_employee_service.py
│
├── main.py
├── test_connection.py
└── README.md
```

## Testing

The project uses pytest for automated testing.

Run all tests using:

```bash
python -m pytest -v
```

Current test result:

```text
7 passed
```

## Database

PostgreSQL is used as the backend database.

Python connects to PostgreSQL using the Psycopg 3 library.

## GitHub

The project is maintained using Git and GitHub.
## GitHub

The project is maintained using Git and GitHub.

## How to Run

### 1. Install Dependencies

```bash
pip install psycopg pytest
