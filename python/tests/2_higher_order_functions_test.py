import unittest
from higher_order_functions import math_calc

class TestHigherOrderFunctions(unittest.TestCase):

   def test_square_calc(self):
       self.assertEqual(math_calc.square(2), 4)