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
        print(weather)
        await client.close()
        return weather

def fetch_weather(location: str, operation=get_todays_weather_temp_for_location):
    return asyncio.run(operation(location))

## Pure functions
def count_words(text):
    return len(text.split())

def count_lines(text):
    return len(text.split('\n'))

def add_port_number(ip_address, port_number):
    return ip_address + ':' + str(port_number)

def todays_location_and_temperature_forecast(weather_data):
    return f"The temperature for today in {weather_data.region} is {weather_data.temperature} degrees"