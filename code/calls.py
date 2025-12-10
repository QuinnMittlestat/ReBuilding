import requests
import json
from bs4 import BeautifulSoup

#List of Top Cities
wiki_url = "https://kids.kiddle.co/List_of_largest_cities_of_U.S._states_and_territories_by_population"
wiki_r = requests.get(wiki_url)
soup = BeautifulSoup(wiki_r.content, 'html.parser')
rows = soup.find('table', class_="wikitable sortable sort-under")
#print(rows)
cities = []




'''
#Historical Weather Data
oikolab_key = 'ce8810d4a9da4e90917232c8cd33e99f'
hw_url = 'https://api.oikolab.com/weather'
hw_params = {'param': 'temperature', 'location': 'Toronto, Ontario', 'start': '1990-01-01', 'end': '1990-01-02', 'freq': 'D'}
hw_headers = {'api-key': oikolab_key}
'''

'''
hw_r = requests.get(hw_url, hw_params, headers={'api-key': oikolab_key})
old_weather_data = json.loads(hw_r.json()['data'])
temp = old_weather_data['data'][0][4]
'''






'''zipCode = "to be done"
countryCode = "US"
urlGeocoding = (f"http://api.openweathermap.org/geo/1.0/zip?zip={zipCode},{countryCode}&appid=d49508eda5382fe81a5b8e5b4ce7e539")

responseGeocoding = requests.get(urlGeocoding)
urlGeocoding = responseGeocoding.json()
lat = urlGeocoding['lat'] #Getting latitude from geocoding
long = urlGeocoding['lon'] #Getting longitude from geocoding'''