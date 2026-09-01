from connection import get_connection


employee_id = int(input("Enter employee ID: "))

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
        FROM employees
        WHERE employee_id = %s;
    """, (employee_id,))

    employee = cursor.fetchone()

connection.close()

if employee:
    print("Employee found:")
    print(employee)
else:
    print("Employee not found.")