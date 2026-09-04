from database import get_connection
from logging_config import logger


def create_employee(employee_id, name, department, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO employees (id, name, department, salary)
            VALUES (?, ?, ?, ?)
            """,
            (employee_id, name, department, salary)
        )

        connection.commit()
        connection.close()

        logger.info(f"Employee created: {employee_id}")

    except Exception as e:
        logger.error(f"Error creating employee: {e}")
        raise Exception(f"Error creating employee: {e}")


def update_employee(employee_id, name, department, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE employees
            SET name = ?, department = ?, salary = ?
            WHERE id = ?
            """,
            (name, department, salary, employee_id)
        )

        connection.commit()
        connection.close()

        logger.info(f"Employee updated: {employee_id}")

    except Exception as e:
        logger.error(f"Error updating employee: {e}")
        raise Exception(f"Error updating employee: {e}")


def delete_employee(employee_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE id = ?",
            (employee_id,)
        )

        connection.commit()
        connection.close()

        logger.info(f"Employee deleted: {employee_id}")

    except Exception as e:
        logger.error(f"Error deleting employee: {e}")
        raise Exception(f"Error deleting employee: {e}")


def search_employee(employee_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM employees WHERE id = ?",
            (employee_id,)
        )

        employee = cursor.fetchone()
        connection.close()

        logger.info(f"Employee searched: {employee_id}")

        return employee

    except Exception as e:
        logger.error(f"Error searching employee: {e}")
        raise Exception(f"Error searching employee: {e}")


def list_employees():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employees")

        employees = cursor.fetchall()
        connection.close()

        logger.info("Employee list retrieved")

        return employees

    except Exception as e:
        logger.error(f"Error listing employees: {e}")
        raise Exception(f"Error listing employees: {e}")