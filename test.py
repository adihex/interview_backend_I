import unittest
from main import calculate 
class TestCalculate(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(calculate("1 + 1"), 2)
        self.assertEqual(calculate("2 - 1"), 1)
        with self.assertRaises(ValueError):
            calculate("2 * 3")
        with self.assertRaises(ValueError):
            calculate("6 / 2")

    def test_complex_expressions(self):
        self.assertEqual(calculate("2 - 1 + 2"), 3)
        self.assertEqual(calculate("(1 + (4 + 5 + 2) - 3) + (6 + 8)"), 23)
        self.assertEqual(calculate("10 - (4 + 5 - 2)"), 3)

    def test_unary_minus(self):
        self.assertEqual(calculate("-5"), -5)
        self.assertEqual(calculate("1 + (-5)"), -4)

    def test_parentheses(self):
        self.assertEqual(calculate("(1 + 2)"), 3)
        # self.assertEqual(calculate("(1 + 2) * 3"), 9)
        self.assertEqual(calculate("1 + (5 - 2)"), 4)

    def test_whitespace(self):
        self.assertEqual(calculate("  3  +  ( 2  -  1 )  "), 4)

    def test_invalid_expressions(self):
        with self.assertRaises(ValueError):
            calculate("1 + 2 +")
        with self.assertRaises(ValueError):
            calculate("1 + 2 -")
        with self.assertRaises(ValueError):
            calculate("+1 + 2")
        with self.assertRaises(ValueError):
            calculate("1 + 2 + (3")
        with self.assertRaises(ValueError):
            calculate("1 + 2 + 3)")
        with self.assertRaises(ValueError):
            calculate("1 + a")

if __name__ == '__main__':
    unittest.main()
