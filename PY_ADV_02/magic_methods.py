class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}"

    def __add__(self, other):
        return self.marks + other.marks


student1 = Student("Rahul", 80)
student2 = Student("Priya", 90)

print(student1)
print(student2)

total = student1 + student2

print("Total Marks:", total)