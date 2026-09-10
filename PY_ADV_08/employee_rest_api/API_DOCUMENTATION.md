# Employee REST API Documentation

## Base URL

`http://127.0.0.1:5000`

## 1. Get All Employees

**Method:** GET

**URL:** `/employees`

Returns all employees from the database.

## 2. Get Employee by ID

**Method:** GET

**URL:** `/employees/<employee_id>`

Example:

`/employees/1`

Returns one employee by employee ID.

## 3. Create Employee

**Method:** POST

**URL:** `/employees`

**Request JSON:**

```json
{
  "employee_name": "Sita",
  "email": "sita@gmail.com",
  "department": "Finance",
  "salary": 50000,
  "department_id": 3
}
```

**Success Status:** `201 Created`

## 4. Update Employee

**Method:** PUT

**URL:** `/employees/<employee_id>`

Example:

`/employees/1`

**Request JSON:**

```json
{
  "employee_name": "Ravi Kumar",
  "email": "ravikumar@gmail.com",
  "department": "IT",
  "salary": 55000,
  "department_id": 1
}
```

**Success Status:** `200 OK`

## 5. Delete Employee

**Method:** DELETE

**URL:** `/employees/<employee_id>`

Example:

`/employees/4`

**Success Status:** `200 OK`

## HTTP Status Codes

* `200` – Successful request
* `201` – Employee created successfully
* `400` – Invalid request or missing data
* `404` – Employee or endpoint not found
* `500` – Internal server error

## Technologies Used

* Python
* Flask
* PostgreSQL
* psycopg2
* JSON
* Postman
* Pytest

## Features

* REST API
* CRUD operations
* JSON requests and responses
* Request validation
* Exception handling
* Logging
* PostgreSQL database integration
* API testing using Postman
