import requests
from flask import current_app

from webapp.config import WEATHER_API_KEY

def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        "key": current_app.config['WEATHER_API_KEY'],
        "q": city_name,
        "days": 1
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'current' in weather:
            try:
                return weather['current']
            except (IndexError, TypeError):
                return False
    except (requests.RequestException, ValueError):
        print('Network error')
        return False
    return False

if __name__ == '__main__':
    print(weather_by_city('Moscow'))