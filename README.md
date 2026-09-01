# Student Management System

## Project Description

The Student Management System is a Python application developed using a structured and maintainable project architecture.

The application supports student creation, update, deletion, and search operations with input validation, custom exception handling, logging, and unit testing.

## Features

- Create a student
- Update student details
- Delete a student
- Search for a student
- Input validation
- Custom exception handling
- Python logging
- Unit testing
- Type hints
- Docstrings
- Object-Oriented Programming

## Project Structure

```text
student_management_system/
│
├── app/
│   ├── services/
│   │   └── student_service.py
│   │
│   ├── validation/
│   │   └── validator.py
│   │
│   ├── exceptions/
│   │   └── student_exceptions.py
│   │
│   └── utils/
│       └── logger.py
│
├── tests/
│   ├── test_student_service.py
│   └── test_validation.py
│
├── application.log
├── requirements.txt
├── README.md
└── main.py