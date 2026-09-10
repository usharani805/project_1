class Student:
    school_name = "ABC College"
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_count += 1

    # Instance method
    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)

    # Class method
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18


# Creating objects
student1 = Student("Rahul", 20)
student2 = Student("Priya", 17)

# Instance method
print("Student Details:")
student1.display()

print("\nSchool:", Student.school_name)

# Class method
Student.change_school("XYZ University")
print("Updated School:", Student.school_name)

# Static method
print("\nIs Rahul an adult?", Student.is_adult(student1.age))
print("Is Priya an adult?", Student.is_adult(student2.age))

# Number of students
print("\nTotal Students:", Student.student_count)