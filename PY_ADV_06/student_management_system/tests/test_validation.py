from app.validation.validator import (
    validate_name,
    validate_age,
    validate_email,
    validate_student,
)


def test_valid_name():
    assert validate_name("Usha") is True


def test_empty_name():
    assert validate_name("") is False


def test_valid_age():
    assert validate_age(25) is True


def test_invalid_age():
    assert validate_age(150) is False


def test_valid_email():
    assert validate_email("usha@gmail.com") is True


def test_invalid_email():
    assert validate_email("usha@") is False


def test_valid_student():
    assert validate_student(
        "Usha",
        25,
        "usha@gmail.com"
    ) is True