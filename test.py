import unittest
from main import calc


class TestCalc(unittest.TestCase):
    def test_basic_sum(self):
        """
        Test if two different versions of 1+1 work
        """
        self.assertEqual(calc('1 + 1'), 2, "Should be 2")
        self.assertEqual(calc('1+1'), 2, "Should be 2")

    def test_basic_mul(self):
        """
        Testing if two different versions of 2*2 work
        """
        self.assertEqual(calc("2 * 2"), 4, "Should be 4")
        self.assertEqual(calc("2*2"), 4, "Should be 4")

    def test_basic_sub(self):
        """Testing Basic Subtraction"""
        self.assertEqual(calc("1 - 1"), 0, "Should be 0")
        self.assertEqual(calc("1-1"), 0, "Should be 0")


if __name__ == "__main__":
    unittest.main()
    print("All tests Passed")
