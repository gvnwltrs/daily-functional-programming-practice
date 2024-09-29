

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