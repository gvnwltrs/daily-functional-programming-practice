

def add(num_1: int, num_2: int) -> int:
    return num_1 + num_2

def subtract(num_1: int, num_2: int) -> int:
    return num_1 - num_2

def multiply(num_1: int, num_2: int) -> int:
    return num_1 * num_2

def divide(num_1: int, num_2: int) -> int:
    return num_1 / num_2

def see_if_username_exists(name: str) -> bool:
    valid_names = ['John', 'Jane', 'Doe']
    return name in valid_names

def calculate_speed(distance: int, time: int) -> int:
    return distance / time

def strip_numbers(name: str) -> str:
    return ''.join([i for i in name if not i.isdigit()]) ## add i for i in list if i is not a number

def set_class_c_ip_address(last_octet: int, subnet: int=0) -> str:
    return f'192.168.{subnet}.{last_octet}'