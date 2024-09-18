
# not a pure function - since printing to the console is a side effect  
def _print_loop(text, count):
    if count == 0:
        return text, count

    print(text)

    return print_loop(text, count - 1)

def print_loop(*args):
    arg1, args2 = args
    return _print_loop(arg1, args2)

def ordered_list(arr_list, index=0) -> bool:
    if index == len(arr_list) - 1:
        return True

    if arr_list[index] > arr_list[index + 1]:
        return False

    return ordered_list(arr_list, index + 1)

def setup_print(text, count):
    # Optional: Add more behavior here if you want to tweak or format this for a certain use case
    return [text, count]
