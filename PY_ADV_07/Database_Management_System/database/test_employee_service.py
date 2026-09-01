import pytest

from employee_service import (
    get_employee,
    get_all_employees,
    search_employee
)


def test_get_employee():
    employee = get_employee(1)

    assert employee is not None
    assert employee[0] == 1


def test_get_all_employees():
    employees = get_all_employees()

    assert isinstance(employees, list)
    assert len(employees) > 0


def test_search_employee():
    results = search_employee("Ravi")

    assert isinstance(results, list)
    assert len(results) > 0