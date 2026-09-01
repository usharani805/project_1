from connection import get_connection


connection = get_connection()

with connection.cursor() as cursor:
    cursor.execute("""
        UPDATE employees
        SET salary = 52000
        WHERE employee_id = 1;
    """)

connection.commit()
connection.close()

print("Employee salary updated successfully!")