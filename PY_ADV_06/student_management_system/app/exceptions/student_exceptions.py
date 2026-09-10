class StudentManagementException(Exception):
    """Base exception for Student Management System."""


class StudentNotFoundException(StudentManagementException):
    """Raised when a student is not found."""


class InvalidStudentException(StudentManagementException):
    """Raised when student details are invalid."""