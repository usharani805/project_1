from connection import get_connection


def create_employee(employee_id, employee_name, email, department, salary, department_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO employees
                (employee_id, employee_name, email, department, salary, department_id)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                employee_id,
                employee_name,
                email,
                department,
                salary,
                department_id
            ))

        connection.commit()
        return True

    except Exception as error:
        connection.rollback()
        print("Error creating employee:", error)
        return False

    finally:
        connection.close()


def get_employee(employee_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM employees
                WHERE employee_id = %s;
            """, (employee_id,))

            return cursor.fetchone()

    finally:
        connection.close()


def get_all_employees():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM employees
                ORDER BY employee_id;
            """)

            return cursor.fetchall()

    finally:
        connection.close()


def update_employee(employee_id, salary):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employees
                SET salary = %s
                WHERE employee_id = %s;
            """, (salary, employee_id))

        connection.commit()
        return True

    except Exception as error:
        connection.rollback()
        print("Error updating employee:", error)
        return False

    finally:
        connection.close()


def delete_employee(employee_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM employees
                WHERE employee_id = %s;
            """, (employee_id,))

        connection.commit()
        return True

    except Exception as error:
        connection.rollback()
        print("Error deleting employee:", error)
        return False

    finally:
        connection.close()


def search_employee(search_text):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM employees
                WHERE employee_name ILIKE %s
                   OR email ILIKE %s;
            """, (
                f"%{search_text}%",
                f"%{search_text}%"
            ))

            return cursor.fetchall()

    finally:
        connection.close()