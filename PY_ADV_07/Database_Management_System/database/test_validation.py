import pytest

from validation import validate_employee_id, validate_salary


def test_validate_employee_id():
    assert validate_employee_id(1) == 1


def test_validate_salary():
    assert validate_salary(50000) == 50000


def test_invalid_employee_id():
    with pytest.raises(ValueError):
        validate_employee_id(-1)


def test_invalid_salary():
    with pytest.raises(ValueError):
        validate_salary(-5000)