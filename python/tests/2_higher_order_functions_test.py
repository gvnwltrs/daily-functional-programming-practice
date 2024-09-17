import unittest
from higher_order_functions.math_calc import square, get_cubed

class TestHigherOrderFunctions(unittest.TestCase):

    def test_square_calc(self):
        input = 2
        expect = 4
        self.assertEqual(square(input), expect)
    
    def test_cubed_after_square_calc(self):
        input = 2
        expect = 8 
        self.assertEqual(get_cubed(input), expect)