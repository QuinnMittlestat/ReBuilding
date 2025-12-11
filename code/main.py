from calls import *

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

def get_todays_temperature(weatherdata,lat,long):
    temp_list = []
    todays_date = weatherdata['properties']['generatedAt'][:10]
    for i in range(len(weatherdata['properties']['periods'])):
        if todays_date == weatherdata['properties']['periods'][i]['startTime'][5:10]:
            temperature = float(weatherdata['properties']['periods'][i]['temperature'])
            temp_list.append(temperature)
    return temp_list




def main(cities_list):
    list_coords = []
    for item in cities_list:
        city = item[0]
        state = item[1]
        coords = geocoding(city,state)
        lat = coords[0]
        long = coords[1]
        list_coords.append(coords)
    print(list_coords)
    for coords in list_coords:
        get_todays_temperature
    

main(city_list())

