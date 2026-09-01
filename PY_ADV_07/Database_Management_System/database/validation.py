def validate_employee_id(employee_id):
    if employee_id <= 0:
        raise ValueError("Employee ID must be greater than 0.")

    return employee_id


def validate_salary(salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative.")

    return salary