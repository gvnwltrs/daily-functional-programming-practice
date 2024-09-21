
def add_to_list(lst, item):
    return lst + [item]

def update_call_log(call_log, date, time, call):
    call_log[date] = {time: call}
    return {date : call_log[date]}