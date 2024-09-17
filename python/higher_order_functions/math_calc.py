

def square_calc(x):
    return x * x

def square(x, func=square_calc):
    return func(x)

def get_cubed(x, func=square_calc):
    return x * func(x)