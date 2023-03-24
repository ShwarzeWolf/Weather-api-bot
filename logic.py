from collections import namedtuple

import requests

from settings import WEATHER_API_KEY

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
cities = {'Yerevan': Coordinates(40.178836, 44.50525)}


def get_weather(city: str) -> str:
    if city not in cities:
        coordinates = get_coordinates(city)
        cities[city] = coordinates

    coordinates = cities[city]
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates.latitude}&lon={coordinates.longitude}&appid={WEATHER_API_KEY}'

    response = requests.get(url)
    weather = response.json()
    return f'The weather now in {city}: {weather["weather"][0]["description"]}'


def get_coordinates(city: str) -> Coordinates:
    geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}'
    response = requests.get(geocode_url)
    city = response.json()[0]
    return Coordinates(city['lat'], city['lon'])
