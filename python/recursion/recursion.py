
def calculate_average(values: list[int], sum=0, count=0) -> int:
    if len(values) == 0:
        return sum // count 
    return calculate_average(values[1:], sum + values[0], count + 1)