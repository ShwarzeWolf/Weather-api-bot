
from collections import namedtuple
from settings import WEATHER_API_KEY
import requests

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
Yerevan = Coordinates(40.178836, 44.50525)
url = f'https://api.openweathermap.org/data/2.5/weather?lat={Yerevan.latitude}&lon={Yerevan.longitude}&appid={WEATHER_API_KEY}'


def get_weather():
    response = requests.get(url)
    weather = response.json()
    return f'The weather now in Yerevan: {weather["weather"][0]["description"]}'
