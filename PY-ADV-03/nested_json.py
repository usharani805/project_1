import json

# Nested JSON data
json_data = '''
{
    "school": {
        "name": "ABC School",
        "location": {
            "city": "Hyderabad",
            "state": "Telangana"
        },
        "students": [
            {
                "id": 1,
                "name": "John",
                "marks": {
                    "math": 85,
                    "science": 90
                }
            },
            {
                "id": 2,
                "name": "Alice",
                "marks": {
                    "math": 92,
                    "science": 88
                }
            }
        ]
    }
}
'''

# Convert JSON into Python dictionary
data = json.loads(json_data)

# Access nested data
print("School Name:", data["school"]["name"])
print("City:", data["school"]["location"]["city"])
print("State:", data["school"]["location"]["state"])

print("\nStudent Details:")

for student in data["school"]["students"]:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Math:", student["marks"]["math"])
    print("Science:", student["marks"]["science"])
    print()