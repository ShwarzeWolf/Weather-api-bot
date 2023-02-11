
from collections import namedtuple

import requests
from settings import WEATHER_API_KEY

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
cities = {'Yerevan': Coordinates(40.178836, 44.50525)}


def get_weather(city):
    if city not in cities:
        return 'Your city is not supported yet'

    coordinates = cities[city]
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates.latitude}&lon={coordinates.longitude}&appid={WEATHER_API_KEY}'

    response = requests.get(url)
    weather = response.json()
    return f'The weather now in Yerevan: {weather["weather"][0]["description"]}'
