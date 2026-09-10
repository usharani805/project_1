from models.student import Student
from exceptions.custom_exception import (
    StudentNotFoundException,
    InvalidStudentException
)


class StudentService:

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if not isinstance(student, Student):
            raise InvalidStudentException("Invalid student object")

        self.students[student.student_id] = student

    def get_student(self, student_id):
        student = self.students.get(student_id)

        if student is None:
            raise StudentNotFoundException(
                f"Student with ID {student_id} not found"
            )

        return student

    def get_all_students(self):
        return list(self.students.values())