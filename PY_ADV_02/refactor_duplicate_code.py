class Student:
    def __init__(self, name):
        self.name = name

    def print_student(self):
        print("Student:", self.name)


student1 = Student("John")
student2 = Student("Alice")

print("Student:", student1.name)
print("Student:", student2.name)