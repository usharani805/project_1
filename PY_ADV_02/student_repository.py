# Student class
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"{self.student_id} - {self.name}"


# Repository
class StudentRepository:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return self.students

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


# Main program
repository = StudentRepository()

repository.add_student(Student(1, "John"))
repository.add_student(Student(2, "Alice"))
repository.add_student(Student(3, "David"))

print("All Students:")

for student in repository.get_all_students():
    print(student)

print("\nSearching for student with ID 2:")

student = repository.find_student(2)

if student:
    print(student)
else:
    print("Student not found")