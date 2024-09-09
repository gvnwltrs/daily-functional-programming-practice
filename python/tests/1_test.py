import unittest
from pure_functions import math_calc

class TestPureFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(math_calc.add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(math_calc.subtract(2, 1), 1)

    def test_multiplication(self):
        self.assertEqual(math_calc.multiply(2, 3), 6)

    def test_division(self):
        self.assertEqual(math_calc.divide(6, 3), 2)

