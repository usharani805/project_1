from app.services.student_service import StudentService
from app.exceptions.student_exceptions import (
    InvalidStudentException,
    StudentNotFoundException,
)


def main():
    """Run the Student Management System."""

    student_service = StudentService()

    try:
        # Create student
        student_service.create_student(
            1,
            "Usha",
            25,
            "usha@gmail.com"
        )

        # Search student
        student = student_service.search_student(1)
        print("Student:", student)

        # Update student
        student_service.update_student(
            1,
            "Usha Rani",
            26,
            "usharani@gmail.com"
        )

        # Search updated student
        student = student_service.search_student(1)
        print("Updated Student:", student)

        # Delete student
        student_service.delete_student(1)

    except InvalidStudentException as error:
        print("Validation Error:", error)

    except StudentNotFoundException as error:
        print("Student Error:", error)

    except Exception as error:
        print("Unexpected Error:", error)


if __name__ == "__main__":
    main()