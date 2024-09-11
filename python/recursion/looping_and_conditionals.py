
def print_loop(text, count):
    if count == 0:
        return text, count
    
    print(text)

    return print_loop(text, count - 1)

def ordered_list(arr_list, index=0) -> bool:
    if index == len(arr_list) - 1:
        return True

    if arr_list[index] > arr_list[index + 1]:
        return False

    return ordered_list(arr_list, index + 1)