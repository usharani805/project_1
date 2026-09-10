import unittest

from models.student import Student
from services.student_service import StudentService


class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.service = StudentService()

    def test_add_student(self):
        student = Student(1, "Usha", "Python")

        self.service.add_student(student)

        self.assertEqual(
            len(self.service.get_all_students()),
            1
        )

    def test_get_student(self):
        student = Student(1, "Usha", "Python")

        self.service.add_student(student)

        result = self.service.get_student(1)

        self.assertEqual(result.name, "Usha")


if __name__ == "__main__":
    unittest.main()