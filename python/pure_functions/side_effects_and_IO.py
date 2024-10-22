import python_weather   
import asyncio

## IO functions
def get_file():
    with open('resources/file.txt') as file:
        return file.read()

def get_ip_address():
    import socket
    return socket.gethostbyname(socket.gethostname())

async def get_todays_weather_temp_for_location(location: str):

    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(location)
        await client.close()
        return weather

def fetch_weather(location: str, operation=get_todays_weather_temp_for_location):
    return asyncio.run(operation(location))

def get_system_current_date_and_time():
    import datetime
    return datetime.datetime.now()

def get_emails_from_file():
    emails = []
    with open('resources/file.txt') as file:
        for line in file:
            if 'email' in line or 'username' in line:
                emails.append(line.strip())  
        return emails 

## Pure functions
def count_words(text):
    return len(text.split())

def count_lines(text):
    return len(text.split('\n'))

def add_port_number(ip_address, port_number):
    return ip_address + ':' + str(port_number)

def todays_location_and_temperature_forecast(weather_data):
    return f"The temperature for today in {weather_data.region} is {weather_data.temperature} degrees"

def current_formatted_date_and_time(io_data):
    return f"Today's date is {io_data.strftime('%Y-%m-%d')} and the time is {io_data.strftime('%H:%M')}"

def generate_email_list(emails):
    email_list = {}
    current_username = ''
    for email in emails:
        if 'username' in email:
            current_username = email.split(':')[1].strip()
        elif 'email' in email:
            email_list[current_username] = email.split(':')[1].strip()
    return email_list