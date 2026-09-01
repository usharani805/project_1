from connection import get_connection


connection = get_connection()

with connection.cursor() as cursor:
    cursor.execute("""
        DELETE FROM employees
        WHERE employee_id = 3;
    """)

connection.commit()
connection.close()

print("Employee deleted successfully!")