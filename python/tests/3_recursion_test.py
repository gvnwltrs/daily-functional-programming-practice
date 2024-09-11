import unittest
from recursion import looping_and_conditionals as lc

class TestRecursion(unittest.TestCase):

    def test_loop_count(self):
        text, count = lc.print_loop("Hello World", 5)
        self.assertEqual(count, 0)


    def test_conditional_result(self):
        test_list = [1, 2, 3, 4, 5]
        result = lc.ordered_list(test_list)
        self.assertIsNotNone(result)