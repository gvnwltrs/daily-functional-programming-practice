
# Data structures: Objects or Closures
def manage_ip_address():
    pass

def get_order_numbers():
    return ["001", "002", "003"]

## Pure functions
def set_port_number(ip_address, port_number):
    pass
 
def update_order_numbers(order_numbers, new_order_number):
    return order_numbers + [new_order_number]

def calculate_sales_price(price):
    tax = 0.149
    return price + (price * tax)

def clear_events_up_to_last(data):
    return data['events'][-1]

def build_email_message_for_recent_purchase(message_structure):
    def message_to(sender):
        def message_from(from_):
            def message_subject(subject):
                def message_body(body):
                    def message():
                        message_structure_copy = message_structure.copy()
                        message_structure_copy['to'] = sender 
                        message_structure_copy['from'] = from_
                        message_structure_copy['subject'] = subject
                        message_structure_copy['body'] = body
                        return message_structure_copy
                    return message
                return message_body
            return message_subject
        return message_from
    return message_to