
def get_date():
    import datetime
    return datetime.datetime.now().date()

def create_date_msg(new_date):
    return f'Today is {new_date}'

def name_state():
    name = None

    def set_name(new_name=None):
        nonlocal name
        if new_name is None:
            return name
        else:
            name = new_name
            return name

    return set_name

def modify_or_access_name(new_name=None):
    return name_state()

def get_name(function):
    return function() 

def append_to_name(name):
    return f'{name} Doe'