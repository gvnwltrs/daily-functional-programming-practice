import unittest
from recursion.looping_and_conditionals import print_loop, ordered_list, setup_print 

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
