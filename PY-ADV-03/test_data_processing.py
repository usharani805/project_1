import unittest
from data_processing import calculate_average, convert_to_uppercase


class TestDataProcessing(unittest.TestCase):

    def test_calculate_average(self):
        result = calculate_average([10, 20, 30])
        self.assertEqual(result, 20)

    def test_convert_to_uppercase(self):
        result = convert_to_uppercase("hello")
        self.assertEqual(result, "HELLO")


if __name__ == "__main__":
    unittest.main()