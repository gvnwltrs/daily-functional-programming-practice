
def get_date():
    import datetime
    return datetime.datetime.now().date()

def create_date_msg(new_date):
    return f'Today is {new_date}'