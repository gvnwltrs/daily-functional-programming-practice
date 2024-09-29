import unittest

from higher_order_functions.composition_and_curry import square_then_add_one, add_5, format_to_jpg
from higher_order_functions.other import ask_question, now_handle_the_question 

class TestCompositionAndCurry(unittest.TestCase):

    def test_composition(self):
        test = square_then_add_one(2)
        expected_result = 5
        self.assertEqual(test == expected_result, True)
    
    def test_curry(self):
        setup = add_5(5) # Manually setting to add 5
        input = 2
        test = setup(input)
        expected_result = 7
        self.assertEqual(test == expected_result, True)
    
    def test_question_and_response(self):
        expected_result = "Q: What is my name? || R: Your name is John Doe."
        test = ask_question("What is my name", now_handle_the_question)
        self.assertEqual(test == expected_result, True)
    
    def test_add_file_format(self):
        file = "test"
        test = format_to_jpg(file) 
        expect = "File converted to JPG."
        self.assertEqual(test[1] == expect, True)