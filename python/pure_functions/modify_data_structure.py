
def add_to_list(lst, item):
    return lst + [item]

def access_copy_of_call_log(date=None, time=None, update=False, updated_log=None):
    log = {}
    if update:
        def modify_call_log():
            nonlocal log
            log = updated_log
        return modify_call_log()
    
    if date is not None:
        return log[date]
    elif date is not None and time is not None:
        return log[date][time]
    else:
        return log


def update_request_for_call_log(call_log, date, time, description):
    call_log[date] = {time: description}
    return call_log

def handle_call_log_update(request):
    try:
        print(request)
        updated_log_return = access_copy_of_call_log(update=True, updated_log=request)
    except KeyError:
        raise KeyError("Invalid request")
    return updated_log_return, True