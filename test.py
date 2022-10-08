import unittest
from main import calc, checkInput


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

    def test_checkInput(self):
        """
        Testing various inputs for checkInput
        """
        self.assertEqual(checkInput("1+1"), "1+1", "Should match input string")
        self.assertEqual(checkInput("1 + 1"), "1 + 1", "Should Match Input")

    def test_NoInputCheckInput(self):
        """Testing No Input for check input"""
        with self.assertRaises(Exception) as context:
            checkInput("")
            self.assertTrue("No Input Entered" in context.exception) # type: ignore

    def test_UnexpectedChar_checkInput(self):
        """Testing unexpected input for checkInput"""
        with self.assertRaises(Exception) as context:
            checkInput("a")
            self.assertTrue("Unexpected character passed" in context.exception) # type: ignore

    def test_doubleOp_checkInput(self):
        """Testing double operator in checkInput"""
        with self.assertRaises(Exception) as context:
            checkInput("1++2")
            self.assertTrue("Double Operator Found" in context.exception) # type: ignore


if __name__ == "__main__":
    unittest.main()
    print("All tests Passed")
