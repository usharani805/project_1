from connection import get_connection


def create_employee(name, email, department_id, salary):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO employees
                (employee_name, email, department_id, salary)
                VALUES (%s, %s, %s, %s)
                RETURNING employee_id;
            """, (name, email, department_id, salary))

            employee_id = cursor.fetchone()[0]
            connection.commit()
            return employee_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_employee(employee_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    employee_id,
                    employee_name,
                    email,
                    department,
                    salary,
                    department_id
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
                SELECT
                    employee_id,
                    employee_name,
                    email,
                    department,
                    salary,
                    department_id
                FROM employees
                ORDER BY salary DESC;
            """)

            return cursor.fetchall()

    finally:
        connection.close()


def update_employee(employee_id, name, email, department_id, salary):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employees
                SET
                    employee_name = %s,
                    email = %s,
                    department_id = %s,
                    salary = %s
                WHERE employee_id = %s
                RETURNING employee_id;
            """, (name, email, department_id, salary, employee_id))

            result = cursor.fetchone()
            connection.commit()

            return result[0] if result else None

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def delete_employee(employee_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM employees
                WHERE employee_id = %s
                RETURNING employee_id;
            """, (employee_id,))

            result = cursor.fetchone()
            connection.commit()

            return result[0] if result else None

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def search_employee(search_term):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    employee_id,
                    employee_name,
                    email,
                    department,
                    salary,
                    department_id
                FROM employees
                WHERE employee_name ILIKE %s
                   OR email ILIKE %s
                ORDER BY employee_name;
            """, (f"%{search_term}%", f"%{search_term}%"))

            return cursor.fetchall()

    finally:
        connection.close()


def get_employees_with_departments():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    e.employee_id,
                    e.employee_name,
                    e.email,
                    e.department,
                    e.salary,
                    e.department_id
                FROM employees e
                JOIN departments d
                    ON e.department_id = d.department_id
                ORDER BY e.salary DESC;
            """)

            return cursor.fetchall()

    finally:
        connection.close()