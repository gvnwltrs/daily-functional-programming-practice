import unittest
import warnings
from _pytest.config import Config

from pure_functions.side_effects_and_IO import (
    get_file, 
    count_words, 
    count_lines, 
    get_ip_address,
    add_port_number,
    fetch_weather,
    todays_location_and_temperature_forecast,
    get_system_current_date_and_time,
    current_formatted_date_and_time,
    get_emails_from_file,
    generate_email_list,
)

class TestSideEffectsAndIO(unittest.TestCase):

    # How to isolate a side effect from a pure function
    def test_side_effect_handling(self):
        file_word_count = 13
        side_effect_output = get_file()
        test = count_words(side_effect_output)
        self.assertEqual(test, file_word_count)

    def test_count_lines(self):
        file_line_count = 11
        side_effect_output = get_file()
        test = count_lines(side_effect_output) 
        self.assertEqual(test, file_line_count)
    
    def test_add_port_number(self):
        ip_address = get_ip_address()
        test = add_port_number(ip_address, 80)
        expect = ip_address + ':80'
        self.assertEqual(test, expect)

    @unittest.skip("Skipping this test because it requires an internet connection")
    def test_get_weather_temp_for_location(self):
        michigan_weather_data = fetch_weather('Michigan')
        result = todays_location_and_temperature_forecast(michigan_weather_data)
        expect = f"The temperature for today in Michigan is {michigan_weather_data.temperature} degrees"
        self.assertEqual(result, expect)

    def test_get_date_and_time(self):
        import datetime
        io_data = get_system_current_date_and_time()
        result = current_formatted_date_and_time(io_data)
        expect = f"Today's date is {datetime.datetime.now().date()} and the time is {datetime.datetime.now().strftime('%H:%M')}"
        self.assertEqual(result, expect)
    
    def test_extracting_email_addresses(self):
        emails = get_emails_from_file()
        result = generate_email_list(emails) 
        expect = {
            'John1': 'john1@email.com',
            'John2': 'john2@email.com'
        }
        self.assertEqual(result, expect)