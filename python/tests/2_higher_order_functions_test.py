import unittest
from higher_order_functions.higher_order_functions import (
    square, 
    get_cubed,
    turn_off_air_conditioner,
    select_investment_temperament,
    get_email_subscriber,
    plan_email_with_coupon_code,
)

from higher_order_functions.other import (
    capitalize_and_underscore_spaces, 
    to_uppercase, 
    underscore_spaces,
)

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
    
    def test_turn_off_air_conditioner(self):
        temperature_update = "72F"
        result = turn_off_air_conditioner(temperature_update)
        expect = True
        self.assertEqual(result, expect)

    def test_investment_balancer(self):
        result = select_investment_temperament()
        expect = "Conservative: 20% stocks, 80% bonds"
        self.assertEqual(result, expect)

    def test_plan_to_email_coupons(self):
        subscribers = {
            "subscriber_id_1": {"firstname": "John",  "lastname": "Smith", "email": "johnsmith@lol.com", "referral_count": 10}, 
            "subscriber_id_2": {"firstname": "Jane",  "lastname": "Smith", "email": "janesmith@lol.com", "referral_count": 5}, 
        }
        result = plan_email_with_coupon_code(get_email_subscriber(subscribers))
        expect = {
            "from": "newsletter@coupondepot.co", 
            "to": "johnsmith@lol.com",
            "subject": "Your coupons are here!",
            "body": "Here are your coupons John: use code [ 10PERCENTOFF ] on your next purchase!"
        }
        self.assertEqual(result, expect)