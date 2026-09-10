from models.student import Student
from services.student_service import StudentService
from utils.logger import logger
from validation.student_validator import StudentValidator
from api.api_service import get_api_data
from exceptions.custom_exception import (
    StudentNotFoundException,
    InvalidStudentException
)


def main():

    service = StudentService()
    StudentValidator.validate(1, "Usha", "Python")

    try:
        student1 = Student(1, "Usha", "Python")

        service.add_student(student1)
        logger.info("Student added successfully")

        print("Student added successfully!")

        student = service.get_student(1)
        logger.info("Student retrieved successfully")

        print(student.display_info())
        api_data = get_api_data()
        print(f"API Users Count: {len(api_data)}")
        logger.info("API data retrieved successfully")

    except InvalidStudentException as error:
        print(f"Invalid Student: {error}")

    except StudentNotFoundException as error:
        print(f"Student Not Found: {error}")


if __name__ == "__main__":
    main()