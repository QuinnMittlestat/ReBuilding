import requests
import json
from bs4 import BeautifulSoup
import re

#List of Top Cities
cities = []
city_pattern = r"([A-Z]{1}.+)"

wiki_url = "https://kids.kiddle.co/List_of_largest_cities_of_U.S._states_and_territories_by_population"
wiki_r = requests.get(wiki_url)
soup = BeautifulSoup(wiki_r.content, 'html.parser')
table = soup.find_all('table', class_="wikitable sortable sort-under")[0]
#print(type(table))
#print(table.encode('utf-8'))
rows = table.find_all('tr')
#for i in rows:
#    print(i.encode('utf-8'))
for row in rows[2:]:
    boxes = row.find_all('td')
    names = []
    for box in boxes:
        matches = re.findall(city_pattern, box.get_text())
        for match in matches:
            try:
                #print(match)
                names.append(match)
            except:
                #print(match.encode('utf-8'))
                names.append(match.encode('utf-8'))
    #print(names)
    territories = ['American Samoa', 'Guam', 'Northern Mariana Islands', 'Puerto Rico', 'Virgin Islands (U.S.)']
    if names[0] not in territories:
        state = names[0]
        city1 = names[1]
        if len(names) > 2:
            city2 = names[2]
        cities.append((city1, state))
        if len(names) > 2:
            cities.append((city2, state))
print(cities)

def geocoding(city,state):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid=d49508eda5382fe81a5b8e5b4ce7e539"
    responseGeocoding = requests.get(url)
    geocoding = responseGeocoding.json()
    #print(geocoding)
    lat = geocoding[0]['lat']
    long = geocoding[0]['lon']
    return (lat,long)

def main(cities_list):
    list_coords = []
    for item in cities_list[0:6]:
        city = item[0]
        state = item[1]
        coords = geocoding(city,state)
        list_coords.append(coords)
        #todays_date = weather(lat,long)['properties']['generatedAt'][5:10]
    #print(list_coords)
#main(cities)


'''
#Historical Weather Data
oikolab_key = 'ce8810d4a9da4e90917232c8cd33e99f'
hw_url = 'https://api.oikolab.com/weather'
hw_params = {'param': 'temperature', 'location': 'Toronto, Ontario', 'start': '1990-01-01', 'end': '1990-01-02', 'freq': 'D'}
hw_headers = {'api-key': oikolab_key}

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