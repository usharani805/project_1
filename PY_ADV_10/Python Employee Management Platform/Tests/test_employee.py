import unittest
from services import (
    create_employee,
    update_employee,
    delete_employee,
    search_employee,
    list_employees
)
from database import create_table, get_connection


class TestEmployeeServices(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_table()

    def setUp(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE id = ?",
            (201,)
        )

        connection.commit()
        connection.close()

        create_employee(201, "Test User", "IT", 50000)

    def tearDown(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE id = ?",
            (201,)
        )

        connection.commit()
        connection.close()

    def test_create_employee(self):
        employee = search_employee(201)

        self.assertIsNotNone(employee)
        self.assertEqual(employee[1], "Test User")

    def test_search_employee(self):
        employee = search_employee(201)

        self.assertIsNotNone(employee)
        self.assertEqual(employee[0], 201)

    def test_update_employee(self):
        update_employee(201, "Updated User", "HR", 55000)

        employee = search_employee(201)

        self.assertEqual(employee[1], "Updated User")
        self.assertEqual(employee[2], "HR")
        self.assertEqual(employee[3], 55000)

    def test_list_employees(self):
        employees = list_employees()

        self.assertGreater(len(employees), 0)

    def test_delete_employee(self):
        delete_employee(201)

        employee = search_employee(201)

        self.assertIsNone(employee)


if __name__ == "__main__":
    unittest.main()