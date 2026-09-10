import csv

# Write data to CSV file
students = [
    ["ID", "Name", "Age"],
    [1, "John", 20],
    [2, "Alice", 21],
    [3, "David", 19]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Data written to students.csv")


# Read data from CSV file
print("\nReading data from students.csv:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)