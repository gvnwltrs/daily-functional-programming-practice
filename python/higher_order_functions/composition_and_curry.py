from typing import Callable
from functools import reduce

# Pure Functions
def square(x):
    return x*x

def add_one(x):
    return x+1

# Function Composition 
def square_then_add_one(x):
    return add_one(square(x)) 

# Uncurried Function
def _add_5(a, b):
    return a + b

# Curried Function
def add_5(a):
    return lambda b: a + b # Since this returns a function, whatever we set the lambda to will be the second argument always; b is each new call to the function

def to_jpg(file):
    return file + ".jpg", "File converted to JPG."

def format_to_jpg(file):
    return to_jpg(file)

def generate_size_output(size_inches):
    return { "size": str(size_inches // 12) + "ft" }

def generate_weight_output(weight_lbs):
    return { "weight": str(weight_lbs) + "lbs" }

def generate_size_and_weight_profile(size_inches, weight_lbs):
    size = str(size_inches // 12) + "ft"
    weight = str(weight_lbs) + "lbs"
    return {"size": size, "weight": weight}

def generate_size_and_weight_profile_enhanced(size_output: Callable[[int], int], weight_output: Callable[[int], int]):
    return lambda size, weight: size_output(size) | weight_output(weight)

def curry_add(a):
    return lambda b: lambda c: a + b + c

def build_sentence(input):
    def sentence_1(input_1):
        def sentence_2(input_2):
            def sentence_3(input_3):
                return input_1 + input_2 + input_3
            return sentence_3
        return sentence_2
    return sentence_1(input)

def generate_sales_total_for_state_partial(state_tax):
    def state_sales_tax(tax_for_state):
        def sales_total(items):
            sub_total =  reduce(lambda total, item_price: total + item_price, items.values(), 0)
            return sub_total + (sub_total * tax_for_state)
        return sales_total
    return state_sales_tax(state_tax) # filling in the input for the inner function, which makes this a partial function

def generate_sales_total_for_state_curried(state_tax):
    def sales_total(items):
        sub_total =  reduce(lambda total, item_price: total + item_price, items.values(), 0)
        return sub_total + (sub_total * state_tax)
    return sales_total