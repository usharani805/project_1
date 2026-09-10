# Function to convert names to uppercase
def transform_name(name):
    return name.upper()


# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)


# Function to transform student data
def transform_student(student):
    student["name"] = transform_name(student["name"])
    student["average"] = calculate_average(student["marks"])
    return student


# Original data
students = [
    {
        "name": "John",
        "marks": [80, 90, 85]
    },
    {
        "name": "Alice",
        "marks": [90, 95, 88]
    }
]


# Transform the data
transformed_students = []

for student in students:
    transformed_students.append(transform_student(student))


# Display transformed data
print("Transformed Student Data:")

for student in transformed_students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Average:", student["average"])
    print()