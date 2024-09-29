import unittest

from pure_functions.modify_data_structure import add_to_list, update_call_log 
from pure_functions.immutability_and_data_structures import get_order_numbers, update_order_numbers 

class TestImmutabilityAndDataStructures(unittest.TestCase):

    def test_add_to_a_list(self):
        test = add_to_list([1, 2, 3], 4)
        expected_result = [1, 2, 3, 4]

        # This should pass, because we are not modifying the original list, 
        # we are returning a new list which has a new memory address. 
        self.assertIsNot(test, expected_result) 
    
    def test_update_the_call_log(self):
        call_log = { '2021-08-10': { '10:00': 'Call with Jane' } } 
        updated_call_log = update_call_log(call_log, '2021-08-11', '12:00', 'Call with John')
        expected_result = { '2021-08-11': { '12:00': 'Call with John' } }
        self.assertEqual(updated_call_log, expected_result)
    
    def test_update_the_call_log_is_not_modifying_the_orginal(self):
        call_log = { '2021-08-10': { '10:00': 'Call with Jane' } } 
        updated_call_log = update_call_log(call_log, '2021-08-11', '12:00', 'Call with John')
        self.assertIsNot(updated_call_log, call_log)
    
    def test_add_new_order_number(self):
        order_numbers = get_order_numbers()
        test = update_order_numbers(order_numbers, "007")
        expect = ["001", "002", "003", "007"]
        self.assertEqual(test, expect)
        self.assertIsNot(test, order_numbers)

        
