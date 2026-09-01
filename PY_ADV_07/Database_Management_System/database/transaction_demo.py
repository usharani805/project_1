from connection import get_connection


connection = get_connection()

try:
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE employees
            SET salary = salary + 1000
            WHERE employee_id = 1;
        """)

    connection.commit()
    print("Transaction committed successfully!")

except Exception as error:
    connection.rollback()
    print("Transaction rolled back:", error)

finally:
    connection.close()