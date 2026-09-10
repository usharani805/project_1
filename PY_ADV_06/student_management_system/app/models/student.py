class Student:
    """Represent a student in the Student Management System."""

    def __init__(self, student_id: int, name: str, age: int, course: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def update(self, name: str, age: int, course: str) -> None:
        """Update student details."""
        self.name = name
        self.age = age
        self.course = course

    def __str__(self) -> str:
        """Return a readable student representation."""
        return (
            f"ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Course: {self.course}"
        )