import unittest

from higher_order_functions.composition_and_curry import (
    square_then_add_one, add_5, 
    format_to_jpg,
    generate_size_and_weight_profile,
    generate_size_and_weight_profile_enhanced,
    generate_size_output,
    generate_weight_output,
    curry_add,
    build_sentence, 
    generate_sales_total_for_state_partial,
    generate_sales_total_for_state_curried,
)

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
    
    def test_size_and_weight_composition_regular(self):
        result = generate_size_and_weight_profile(72, 200)
        expect = {'size': '6ft', 'weight': '200lbs'}
        self.assertTrue(result == expect)

    def test_size_and_weight_curried(self): # not actually curried, but the function is composed
        composed_setup = generate_size_and_weight_profile_enhanced(generate_size_output, generate_weight_output)
        result = composed_setup(72, 200)
        expect = {'size': '6ft', 'weight': '200lbs'}
        self.assertTrue(result == expect)

    def test_curried_adding_1_to_sum(self):
        add_1 = curry_add(1)
        result = add_1(2)(3)
        expect = 6
        self.assertTrue(result == expect)
    
    def test_curried_adding_1_and_2_to_sum(self):
        add_1_and_2 = curry_add(1)(2)
        final = add_1_and_2(3)
        expect = 6
        self.assertEqual(final, expect)

    def test_curried_adding_all_3_then_another_input(self):
        add_one = curry_add(1)
        add_two = add_one(2)
        result = add_two(4)
        expect = 7 
        self.assertTrue(result == expect)

    def test_sentence_builder(self):
        sentence_1 = build_sentence("Hello, my name is ")
        sentence_2 = sentence_1("John Smith, ")
        result = sentence_2("and I am 30 years old.") 
        expect = "Hello, my name is John Smith, and I am 30 years old."
        self.assertEqual(result, expect)
    
    def test_total_sale_price_with_sales_tax_for_state_partial(self):
        state_sales_tax = {
            "CA": 0.075,
            "NY": 0.045,
            "TX": 0.0625
        }
        items = {
            "item_1": 10,
            "item_2": 20,
            "item_3": 30
        }
        texas_sales_total_plus_tax = generate_sales_total_for_state_partial(state_sales_tax["TX"])
        result = texas_sales_total_plus_tax(items)
        expect = 63.75
        self.assertEqual(result, expect)
    
    def test_total_sale_price_with_sales_tax_for_state(self):
        state_sales_tax = {
            "CA": 0.075,
            "NY": 0.045,
            "TX": 0.0625
        }
        items = {
            "item_1": 10,
            "item_2": 20,
            "item_3": 30
        }
        texas_sales_total_plus_tax = generate_sales_total_for_state_curried(state_sales_tax["TX"])
        result = texas_sales_total_plus_tax(items)
        expect = 63.75
        self.assertEqual(result, expect)
