class StudentValidator:

    @staticmethod
    def validate(student_id, name, course):
        if not student_id:
            raise ValueError("Student ID is required")

        if not name or not name.strip():
            raise ValueError("Student name is required")

        if not course or not course.strip():
            raise ValueError("Course is required")

        return True