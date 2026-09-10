# Function to clean and handle incorrect or missing values
def clean_student_data(student):
    # Handle missing name
    if not student.get("name"):
        student["name"] = "Unknown"

    # Handle missing or incorrect age
    if not isinstance(student.get("age"), int):
        student["age"] = 0

    # Handle incorrect age range
    if student["age"] < 0 or student["age"] > 100:
        student["age"] = 0

    # Handle missing email
    if not student.get("email"):
        student["email"] = "Not Provided"

    return student


# Incoming data
students = [
    {
        "name": "John",
        "age": 20,
        "email": "john@example.com"
    },
    {
        "name": "",
        "age": "twenty",
        "email": ""
    },
    {
        "name": "Alice",
        "age": 150,
        "email": "alice@example.com"
    }
]


# Clean the data
for student in students:
    clean_student_data(student)


# Display cleaned data
print("Cleaned Student Data:")

for student in students:
    print(student)