def validate_employee(data):
    if not data:
        return "Request data is required"

    if "id" not in data:
        return "Employee ID is required"

    if "name" not in data or not data["name"]:
        return "Employee name is required"

    if "department" not in data or not data["department"]:
        return "Department is required"

    if "salary" not in data:
        return "Salary is required"

    if not isinstance(data["salary"], (int, float)):
        return "Salary must be a number"

    return None