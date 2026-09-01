from validation import validate_employee_id, validate_salary


try:
    employee_id = int(input("Enter employee ID: "))
    validate_employee_id(employee_id)

    salary = float(input("Enter salary: "))
    validate_salary(salary)

    print("Validation successful!")

except ValueError as error:
    print("Validation error:", error)