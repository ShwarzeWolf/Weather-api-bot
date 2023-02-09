
from collections import namedtuple

import requests
from settings import WEATHER_API_KEY

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
cities = {'Yerevan': Coordinates(40.178836, 44.50525)}


def get_weather(city):
    city_coordinates = cities.get(city)

    if city_coordinates is None:
        city_coordinates = get_city_coordinates(city)
        cities[city] = city_coordinates

    weather_endpoint = f'https://api.openweathermap.org/data/2.5/weather?lat={city_coordinates.latitude}&lon={city_coordinates.longitude}&appid={WEATHER_API_KEY}'
    response = requests.get(weather_endpoint)
    weather = response.json()

    return f'The weather now in {city}: {weather["weather"][0]["description"]}'


def get_city_coordinates(city):
    city_endpoint = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}'

    response = requests.get(city_endpoint)
    # taking just the first city
    city = response.json()[0]

    return Coordinates(city['lat'], city['lon'])

