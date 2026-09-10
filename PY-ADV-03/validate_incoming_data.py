# Function to validate student data
def validate_student(student):
    errors = []

    # Check name
    if not student.get("name"):
        errors.append("Name is required.")

    # Check age
    if not isinstance(student.get("age"), int):
        errors.append("Age must be a number.")
    elif student["age"] < 5 or student["age"] > 100:
        errors.append("Age must be between 5 and 100.")

    # Check email
    if "@" not in student.get("email", ""):
        errors.append("Invalid email address.")

    # Return validation result
    if errors:
        return False, errors

    return True, ["Data is valid."]


# Incoming data
students = [
    {
        "name": "John",
        "age": 20,
        "email": "john@example.com"
    },
    {
        "name": "",
        "age": 150,
        "email": "aliceexample.com"
    }
]


# Validate each student
for student in students:
    valid, messages = validate_student(student)

    print("Student:", student)

    if valid:
        print("Result: Valid")
    else:
        print("Result: Invalid")

    for message in messages:
        print("-", message)

    print()