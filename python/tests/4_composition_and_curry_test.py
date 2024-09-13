import unittest

from higher_order_functions import composition_and_curry as cc

class TestCompositionAndCurry(unittest.TestCase):

    def test_composition(self):
        test = cc.square_then_add_one(2)
        expected_result = 5
        self.assertEqual(test == expected_result, True)
    
    def test_curry(self):
        setup = cc.add_5(5) # Manually setting to add 5
        input = 2
        test = setup(input)
        expected_result = 7
        self.assertEqual(test == expected_result, True)