from database.connection import get_connection


def view_employees():
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
            ORDER BY employee_id;
        """)

        employees = cursor.fetchall()

    connection.close()

    if employees:
        print("\nEmployee Details:")
        for employee in employees:
            print(employee)
    else:
        print("\nNo employees found.")


def search_employee():
    try:
        employee_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Invalid employee ID. Please enter a number.")
        return

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
        print("\nEmployee found:")
        print(employee)
    else:
        print("\nEmployee not found.")


def main():
    while True:
        print("\n===== Employee Management System =====")
        print("1. View Employees")
        print("2. Search Employee")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_employees()

        elif choice == "2":
            search_employee()

        elif choice == "3":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()