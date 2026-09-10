class Student:
    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating objects
student1 = Student("Rahul", 20, "Python")
student2 = Student("Priya", 21, "Java")

# Calling the method using objects
print("Student 1 Details")
student1.display_details()

print("\nStudent 2 Details")
student2.display_details()