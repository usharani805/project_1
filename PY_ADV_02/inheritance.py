class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Student inherits from Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()
        print("Course:", self.course)


# Teacher inherits from Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print("Subject:", self.subject)


# Creating objects
student = Student("Rahul", 20, "Python")
teacher = Teacher("Mr. Kumar", 35, "Computer Science")

print("----- Student Details -----")
student.display_student()

print("\n----- Teacher Details -----")
teacher.display_teacher()