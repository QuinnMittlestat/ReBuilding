import json
import requests

def geocoding(city,state):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid=d49508eda5382fe81a5b8e5b4ce7e539"
    responseGeocoding = requests.get(url)
    urlGeocoding = responseGeocoding.json()
    return urlGeocoding

def weather(lat,long):
    urlWeather = (f"https://api.weather.gov/points/{lat},{long}")
    responseWeather = requests.get(urlWeather)
    get_urlWeather = responseWeather.json()
    forecast_url = get_urlWeather["properties"]["forecast"]
    response_urlWeather = requests.get(forecast_url)
    weather_data = response_urlWeather.json()
    return weather_data

def main(cities_list):
    for city in cities_list:
        lat = geocoding(city[0],city[1])['lat']
        long = geocoding(city[0],city[1])['long']
        todays_date = weather(lat,long)['properties']['generatedAt'][5:10]

main(cities)

