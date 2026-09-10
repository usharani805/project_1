import unittest

from validation import validate_data
from transformation import transform_data


class TestDataProcessing(unittest.TestCase):

    def test_validation_success(self):
        data = {
            "id": 1,
            "title": "Hello",
            "body": "Test body"
        }

        result = validate_data(data)

        self.assertTrue(result)

    def test_validation_failure(self):
        data = {
            "id": 1,
            "title": "Hello"
        }

        result = validate_data(data)

        self.assertFalse(result)

    def test_transformation(self):
        data = {
            "id": 1,
            "title": "hello world",
            "body": "Test body"
        }

        result = transform_data(data)

        self.assertEqual(result["title"], "HELLO WORLD")


if __name__ == "__main__":
    unittest.main()