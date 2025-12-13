import requests
import json
from bs4 import BeautifulSoup
import re


#List of Top Cities
def city_list():
   cities = []
   city_pattern = r"([A-Z]{1}.+)"


   wiki_url = "https://kids.kiddle.co/List_of_largest_cities_of_U.S._states_and_territories_by_population"
   wiki_r = requests.get(wiki_url)
   soup = BeautifulSoup(wiki_r.content, 'html.parser')
   table = soup.find_all('table', class_="wikitable sortable sort-under")[0]
   rows = table.find_all('tr')
   for row in rows[2:]:
       boxes = row.find_all('td')
       names = []
       for box in boxes:
           matches = re.findall(city_pattern, box.get_text())
           for match in matches:
               try:
                   names.append(match)
               except:
                   names.append(match.encode('utf-8'))
       territories = ['American Samoa', 'Guam', 'Northern Mariana Islands', 'Puerto Rico', 'Virgin Islands (U.S.)', 'District of Columbia']
       if names[0] not in territories:
           state = names[0]
           city1 = names[1]
           if len(names) > 2:
               city2 = names[2]
           cities.append((city1, state))
           if len(names) > 2:
               cities.append((city2, state))
   return cities


def geocoding(cities):
   coords_list = []
   for city in cities:
       url = f"http://api.openweathermap.org/geo/1.0/direct?q={city[0]},{city[1]},US&appid=d49508eda5382fe81a5b8e5b4ce7e539"
       responseGeocoding = requests.get(url)
       geocoding = responseGeocoding.json()
       lat = geocoding[0]['lat']
       long = geocoding[0]['lon']
       coords = (lat,long)
       coords_list.append(coords)
   return coords_list




def weather(coords_list):
   weather_data_list = []
   for coords in coords_list:
       lat = coords[0]
       long = coords[1]
       urlWeather = (f"https://api.weather.gov/points/{lat},{long}")
       responseWeather = requests.get(urlWeather)
       get_urlWeather = responseWeather.json()
       forecast_url = get_urlWeather["properties"]["forecast"]
       response_urlWeather = requests.get(forecast_url)
       weather_data = response_urlWeather.json()
       weather_data_list.append(weather_data)
   return weather_data_list


def get_todays_temperature(weather_data_list):
   temp_list = []
   for weatherdata in weather_data_list:
       todays_date = weatherdata['properties']['generatedAt'][:10]
       for i in range(len(weatherdata['properties']['periods'])):
           l = []
           if todays_date == weatherdata['properties']['periods'][i]['startTime'][:10] or todays_date == weatherdata['properties']['periods'][i]['endTime'][:10]:
               temperature = float(weatherdata['properties']['periods'][i]['temperature'])
           l.append(temperature)
       temp_list.append((sum(l)/len(l)))
   return temp_list


def get_historical_temp(cities,date):
   historical_temp_list = []
   for item in cities:
       city = item[0]
       state = item[1]
       string = f"{city}, {state}"
       oikolab_key = '577d335dbf214ed697a3a306b0d634a1'
       hw_url = 'https://api.oikolab.com/weather'
       hw_params = {'param': 'temperature', 'location': string, 'start': date, 'end': date, 'freq': 'D'}
       hw_r = requests.get(hw_url, hw_params, headers={'api-key': oikolab_key})
       old_weather_data = hw_r.json()['data']
       old_weather_data = json.loads(old_weather_data)
       temp = old_weather_data['data'][0][4]
       temp = round((((9/5) * temp) + 32), 2)
       historical_temp_list.append(temp)
   return historical_temp_list



