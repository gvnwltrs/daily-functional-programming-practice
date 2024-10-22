import unittest
from pure_functions.pure_functions import (
    add, 
    subtract, 
    multiply, 
    divide,
    see_if_username_exists,
    calculate_speed,
    strip_numbers,
    set_class_c_ip_address,
)

from pure_functions.other import (
    get_date, 
    create_date_msg, 
    modify_or_access_name, 
    get_name, 
    append_to_name 
)

class TestPureFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(subtract(2, 1), 1)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_division(self):
        self.assertEqual(divide(6, 3), 2)

    def test_using_calendar_date_from_the_impure(self):
        date = get_date()
        date_msg = create_date_msg(date) 
        expect = f'Today is {date}'
        self.assertEqual(date_msg, expect)

    def test_add_name(self):
        set_name = modify_or_access_name()
        self.assertEqual(set_name('John'), 'John')
    
    def test_add_last_name(self):
        setup_name = modify_or_access_name()
        setup_name('John')
        name = get_name(setup_name)
        new_name = append_to_name(name)
        self.assertEqual(new_name, 'John Doe')

    def test_user_name_exists(self):
        result = see_if_username_exists('John')
        self.assertTrue(result)

    def test_speed_calculation(self):
        result = calculate_speed(100, 10)
        expect = 10
        self.assertTrue(result, expect)

    def test_strip_numbers(self):
        result = strip_numbers('John123')
        expect = 'John'
        self.assertEqual(result, expect)

    def test_set_ip_address(self):
        result = set_class_c_ip_address(100)
        expect = '192.168.0.100'
        self.assertEqual(result, expect)

