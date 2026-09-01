from connection import get_connection


connection = get_connection()

with connection.cursor() as cursor:

    # Insert departments
    cursor.execute("""
        INSERT INTO departments (department_id, department_name)
        VALUES
            (1, 'Human Resources'),
            (2, 'Information Technology'),
            (3, 'Finance')
        ON CONFLICT DO NOTHING;
    """)

    # Insert employees
    cursor.execute("""
        INSERT INTO employees
        (employee_id, employee_name, email, department, salary, department_id)
        VALUES
            (1, 'Usha', 'usha@example.com', 'Human Resources', 50000, 1),
            (2, 'Ravi', 'ravi@example.com', 'Information Technology', 45000, 2),
            (3, 'Anil', 'anil@example.com', 'Finance', 55000, 3)
        ON CONFLICT DO NOTHING;
    """)


connection.commit()
connection.close()

print("Departments and employees inserted successfully!")