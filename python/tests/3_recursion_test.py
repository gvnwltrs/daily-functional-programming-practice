import unittest
from recursion.looping_and_conditionals import print_loop, ordered_list, setup_print, count_number_of_items_found 
from recursion.recursion import (
    calculate_average
)

class TestRecursion(unittest.TestCase):

    def test_loop_count(self):
        text, count = print_loop("Hello World", 5)
        self.assertEqual(count, 0)


    def test_conditional_result(self):
        test_list = [1, 2, 3, 4, 5]
        result = ordered_list(test_list)
        self.assertIsNotNone(result)
    
    def test_use_pure_functions_for_impure_print_loops(self):
        # First we'll setup up what we want to print, including the number of loops
        test_text = "Hello World"
        test_count = 5
        print_loop_args = setup_print(test_text, test_count)

        # Now we'll pass the setup to the impure print loop function
        text, count = print_loop(*print_loop_args)
        # Now we'll check this impure function operation based on what it returns
        self.assertEqual([test_text, 0], [text, count])

    def test_items_filter_count(self):
        fruit_list = ["apple", "banana", "cherry", "kiwi", "mango", "mango", "apple", "banana", "banana"]
        filter = "banana"
        test = count_number_of_items_found(fruit_list, filter)
        expect = 3
        self.assertEqual(test, expect)
    
    def test_calculate_average_for_home_prices(self):
        house_prices = [100000, 200000, 300000, 400000, 500000]
        result = calculate_average(house_prices)
        expect = 300000
        self.assertEqual(result, expect)

