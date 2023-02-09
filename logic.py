
from collections import namedtuple

import requests
from settings import WEATHER_API_KEY

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
cities = {'Yerevan': Coordinates(40.178836, 44.50525)}


def get_weather(city):
    city_coordinates = cities.get(city)

    if city_coordinates is None:
        return 'Sorry, no such city in database'

    weather_endpoint = f'https://api.openweathermap.org/data/2.5/weather?lat={city_coordinates.latitude}&lon={city_coordinates.longitude}&appid={WEATHER_API_KEY}'
    response = requests.get(weather_endpoint)
    weather = response.json()

    return f'The weather now in {city}: {weather["weather"][0]["description"]}'
