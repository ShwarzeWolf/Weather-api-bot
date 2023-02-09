
from collections import namedtuple

import requests
from settings import WEATHER_API_KEY

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
city_coordinates = {'Yerevan': Coordinates(40.178836, 44.50525)}


def get_weather(city):
    coordinates = city_coordinates.get(city)

    if coordinates is None:
        coordinates = get_coordinates(city)
        city_coordinates[city] = coordinates

    weather_endpoint = f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates.latitude}&lon={coordinates.longitude}&appid={WEATHER_API_KEY}'
    response = requests.get(weather_endpoint)
    weather = response.json()

    return f'The weather now in {city}: {weather["weather"][0]["description"]}'


def get_coordinates(city):
    geocode_endpoint = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}'
    response = requests.get(geocode_endpoint)
    city = response.json()[0] # from all cities now we want only the first match

    return Coordinates(city['lat'], city['lon'])

