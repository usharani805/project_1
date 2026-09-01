from connection import get_connection


connection = get_connection()

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT
            employee_id,
            employee_name,
            email,
            department,
            salary,
            department_id
        FROM employees;
    """)

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


connection.close()