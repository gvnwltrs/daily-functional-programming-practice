import unittest
from higher_order_functions.math_calc import square, get_cubed
from higher_order_functions.other import capitalize_and_underscore_spaces, to_uppercase, underscore_spaces

class TestHigherOrderFunctions(unittest.TestCase):

    def test_square_calc(self):
        input = 2
        expect = 4
        self.assertEqual(square(input), expect)
    
    def test_cubed_after_square_calc(self):
        input = 2
        expect = 8 
        self.assertEqual(get_cubed(input), expect)
    
    def test_uppercase_string(self):
        input = "hello"
        expect = "HELLO"
        self.assertEqual(to_uppercase(input), expect)
    
    def test_underscore_string_spaces(self):
        input = "hello world"
        expect = "hello_world"
        self.assertEqual(underscore_spaces(input), expect)
    
    def test_capitalize_and_underscore_spaces(self):
        input = "hello world"
        expect = "HELLO_WORLD"
        handler = capitalize_and_underscore_spaces()
        self.assertEqual(handler(input), expect)