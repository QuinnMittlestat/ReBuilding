from calls import *


def main():
   list_cities = city_list()
   list_coords = geocoding(list_cities)
   list_weather_data = weather(list_coords)
   todays_date = list_weather_data[0]['properties']['generatedAt'][:10]
   year = int(todays_date[:4])
   rest_of_date = todays_date[4:]
   yr10 = year - 10
   yr25 = year - 25
   date1 = f"{yr10}{rest_of_date}"
   date2 = f"{yr25}{rest_of_date}"
   list_todays_temps = get_todays_temperature(list_weather_data)
   list_historic_temps_10yr = get_historical_temp(list_cities,date1)
   print(list_historic_temps_10yr)
   print(list_todays_temps)
   list_historic_temps_25yr = get_historical_temp(list_cities,date2)
   temp_data = (list_todays_temps,list_historic_temps_10yr,list_historic_temps_25yr,list_coords)
   return temp_data





