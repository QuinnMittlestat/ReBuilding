from calls import *

def main():
    list_cities = city_list()
    list_coords = geocoding(list_cities)
    list_weather_data = weather(list_coords)
    list_todays_temps = get_todays_temperature(list_weather_data)
    return list_todays_temps

print(main())
