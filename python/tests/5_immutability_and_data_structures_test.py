import unittest

from pure_functions.modify_data_structure import add_to_list, access_copy_of_call_log, update_request_for_call_log, handle_call_log_update 

class TestImmutabilityAndDataStructures(unittest.TestCase):

    def test_add_to_a_list(self):
        test = add_to_list([1, 2, 3], 4)
        expected_result = [1, 2, 3, 4]

        # This should pass, because we are not modifying the original list, 
        # we are returning a new list which has a new memory address. 
        self.assertIsNot(test, expected_result) 
    
    def test_update_the_call_log(self):
        call_log = access_copy_of_call_log()
        request = update_request_for_call_log(call_log, '2021-08-10', '12:00', 'Call with John')
        handle_call_log_update(request)
        recent_call_log_update = access_copy_of_call_log("2021-08-10", "12:00")
        expected_result = {
            '2021-08-10': {
                '12:00': 'Call with John'
            }
        }
        self.assertEqual(recent_call_log_update, expected_result)
        
