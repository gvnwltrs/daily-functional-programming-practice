from typing import Callable

# Data

# Calculations 
def square_calc(x):
    return x * x

def square(x, func=square_calc):
    return func(x)

def get_cubed(x, func=square_calc):
    return x * func(x)

def trigger_turn_air_conditioner_off():
    # code to turn off air conditioner (use try/except block)
    return True

def turn_off_air_conditioner(temperature_update, func=trigger_turn_air_conditioner_off):
    set_point = "72F" 
    if temperature_update == set_point:
        return func()
    return False

def select_investment_temperament(option=None):
    return investment_balancer(option)

def investment_balancer(option):
    if option == "Aggressive":
        return "Aggressive: 50% stocks, 50% bonds"
    return "Conservative: 20% stocks, 80% bonds"

def get_email_subscriber(subscribers_group: dict, name: str = None) -> dict:
   return next(iter(subscribers_group.values())) if name is None else subscribers_group[name] 

def selectCoupon(ref_count):
    if ref_count < 10:
        return "NOCOUPON"
    return "10PERCENTOFF"

def plan_email_with_coupon_code(func: Callable[[dict], str], coupon=selectCoupon) -> dict:
    email = {
        "from": "newsletter@coupondepot.co",
        "to": func['email'], 
        "subject": "Your coupons are here!",
        "body": "Here are your coupons " + func['firstname'] + ": use code [ " +  coupon(func['referral_count']) + " ] on your next purchase!"
    }
    return email 

# Actions

