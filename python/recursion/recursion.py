
def calculate_average(values: list[int], sum=0, count=0) -> int:
    if len(values) == 0:
        return sum // count 
    return calculate_average(values[1:], sum + values[0], count + 1)

def high_payment_events(data: list[int], high_payment=200, count=0) -> int:
    if len(data) == 0:
        return count
    if data[0] >= high_payment:
        count += 1
    return high_payment_events(data[1:], high_payment, count)

def calculate_sum(data: list[int], sum=0) -> int:
    if len(data) == 0:
        return sum
    return calculate_sum(data[1:], sum + data[0]) # slice the list starting at index 1, add the first element to the sum