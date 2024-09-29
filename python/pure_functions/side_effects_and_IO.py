
## IO functions
def get_file():
    with open('resources/file.txt') as file:
        return file.read()

def get_ip_address():
    import socket
    return socket.gethostbyname(socket.gethostname())

## Pure functions
def count_words(text):
    return len(text.split())

def count_lines(text):
    return len(text.split('\n'))

def add_port_number(ip_address, port_number):
    return ip_address + ':' + str(port_number)
