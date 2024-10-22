import unittest

from pure_functions.modify_data_structure import add_to_list, update_call_log 
from pure_functions.immutability_and_data_structures import (
    get_order_numbers, 
    update_order_numbers,
    calculate_sales_price, 
    clear_events_up_to_last, 
    build_email_message_for_recent_purchase,
)

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

    def test_calculate_sales_price(self):
        data_structure = {
            "item_1": {
                "product:": "Burger",
                "price": 10.00
            },
            "item_2": {
                "product:": "Fries",
                "price": 5.00
            }
        }

        result = calculate_sales_price(data_structure['item_1']['price'])
        expect = 11.49
        self.assertEqual(result, expect)
    
    def test_delete_all_data_events_except_for_last(self):
        data = {
            "events": [
                { "id": 1, "name": "Event 1" },
                { "id": 2, "name": "Event 2" },
                { "id": 3, "name": "Event 3" },
                { "id": 4, "name": "Event 4" },
                { "id": 5, "name": "Event 5" }
            ]
        }
        result = clear_events_up_to_last(data)
        expect = { "id": 5, "name": "Event 5" } 
        self.assertEqual(result, expect)
    
    def test_buld_email_message(self):
        email_message_template = {
            "to": "",
            "from": "",
            "subject": "",
            "body": ""
        }
        email_to = build_email_message_for_recent_purchase(email_message_template)("johnsmith@lol.com")
        email_from = email_to("sales@widgets.com") 
        email_subject = email_from("Thank You!")
        email_body = email_subject("Thank you for your recent purchase of a Widget! We hope you enjoy it!")
        result = email_body()
        expect = {
            "to": "johnsmith@lol.com", 
            "from": "sales@widgets.com",
            "subject": "Thank You!",
            "body": "Thank you for your recent purchase of a Widget! We hope you enjoy it!"
        }
        self.assertEqual(result, expect)
        # self.assertIsNot(email_message_template, result)