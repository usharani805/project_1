from app.validation.validator import validate_student
from app.exceptions.student_exceptions import (
    InvalidStudentException,
    StudentNotFoundException,
)
from app.utils.logger import get_logger


class StudentService:
    """Manage student operations."""

    def __init__(self):
        self.students = {}
        self.logger = get_logger("StudentService")

    def create_student(
        self, student_id: int, name: str, age: int, email: str
    ) -> None:
        """Create a new student after validation."""

        if not validate_student(name, age, email):
            self.logger.error("Invalid student details")
            raise InvalidStudentException("Invalid student details")

        self.students[student_id] = {
            "name": name,
            "age": age,
            "email": email,
        }

        self.logger.info(
            "Student %s created successfully", student_id
        )
        print("Student added successfully!")

    def update_student(
        self, student_id: int, name: str, age: int, email: str
    ) -> None:
        """Update an existing student after validation."""

        if student_id not in self.students:
            self.logger.error(
                "Student %s not found", student_id
            )
            raise StudentNotFoundException(
                f"Student with ID {student_id} not found"
            )

        if not validate_student(name, age, email):
            self.logger.error("Invalid student details")
            raise InvalidStudentException("Invalid student details")

        self.students[student_id] = {
            "name": name,
            "age": age,
            "email": email,
        }

        self.logger.info(
            "Student %s updated successfully", student_id
        )
        print("Student updated successfully!")

    def search_student(self, student_id: int):
        """Search for a student by ID."""

        if student_id not in self.students:
            self.logger.error(
                "Student %s not found", student_id
            )
            raise StudentNotFoundException(
                f"Student with ID {student_id} not found"
            )

        self.logger.info(
            "Student %s searched successfully", student_id
        )
        return self.students[student_id]

    def delete_student(self, student_id: int) -> None:
        """Delete a student by ID."""

        if student_id not in self.students:
            self.logger.error(
                "Student %s not found", student_id
            )
            raise StudentNotFoundException(
                f"Student with ID {student_id} not found"
            )

        del self.students[student_id]

        self.logger.info(
            "Student %s deleted successfully", student_id
        )
        print("Student deleted successfully!")