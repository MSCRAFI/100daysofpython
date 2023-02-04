# making weather program using weatherapi and requests module
import requests as rq


class weather:
    def __init__(self):
        # Base URL
        self.BASE_URL = "http://api.weatherapi.com/v1/current.json?key="
        self.API_KEY = open("API.txt", "r").read()  # getting the API

    def get_weather(self, LOCATION):  # getting data as DICT
        URL = self.BASE_URL + self.API_KEY + "&q=" + LOCATION + "&aqi=yes"
        self.response = rq.get(URL).json()

    def print_info(self):
        # getting the info from DICT and printing it using fstring
        print(f"The location you selected is \
{self.response['location']['name']}, {self.response['location']['country']} \
and current temperature of your location is \
{self.response['current']['temp_c']}°C or {self.response['current']['temp_f']}\
°F.\nBut people in this location feeling like \
{self.response['current']['feelslike_c']}°C or \
{self.response['current']['feelslike_f']}°F.")


wtr = weather()  # calling the class
# getting the actual location
location = input("Enter your location to check current temperature:\n>> ")
wtr.get_weather(location)
wtr.print_info()
