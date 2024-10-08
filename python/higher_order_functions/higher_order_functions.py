
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