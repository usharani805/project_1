import json

# JSON data
json_data = '''
{
    "students": [
        {
            "id": 1,
            "name": "John",
            "age": 20
        },
        {
            "id": 2,
            "name": "Alice",
            "age": 21
        },
        {
            "id": 3,
            "name": "David",
            "age": 19
        }
    ]
}
'''

# Convert JSON data into Python object
data = json.loads(json_data)

# Process and display student information
print("Student Details:")

for student in data["students"]:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print()