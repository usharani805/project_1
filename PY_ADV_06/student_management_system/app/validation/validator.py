import re


def validate_name(name: str) -> bool:
    """Validate student name."""
    return bool(name and name.strip())


def validate_age(age: int) -> bool:
    """Validate student age."""
    return isinstance(age, int) and 1 <= age <= 100


def validate_email(email: str) -> bool:
    """Validate student email."""
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return bool(re.match(pattern, email))


def validate_student(name: str, age: int, email: str) -> bool:
    """Validate all student details."""
    return (
        validate_name(name)
        and validate_age(age)
        and validate_email(email)
    )