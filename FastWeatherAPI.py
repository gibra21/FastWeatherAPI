import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = "London"


def kelvin_to_celsius_far(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&qp" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius , temp_fahrenheit = kelvin_to_celsius_far(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_far(feels_like_kelvin)
wind_speed = response['main']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f} C or {temp_fahrenheit}F")
print(f"Temperature in {CITY}: Feels like {feels_like_celsius:.2f} C or {feels_like_fahrenheit}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"Sun Rise Time in {CITY}: {sunset_time}am")
print(f"Sunset in {CITY}: {sunset_time}pm")





