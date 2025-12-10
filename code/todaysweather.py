import calls
import main

def get_todays_temperature(weatherdata):
    temp_list = []
    for i in range(len(weatherdata['properties']['periods'])):
        if todays_date == weatherdata['properties']['periods'][i]['startTime'][5:10]:
            temperature = float(weatherdata['properties']['periods'][i]['temperature'])
            temp_list.append(temperature)
    temp = sum(temp_list)/2
    return temp

