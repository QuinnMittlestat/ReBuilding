import sqlite3
from sqlstuff import *
from main import *
import math


def calculate_temp_difference():
   conn = sqlite3.connect('weather_data.db')
   curr = conn.cursor()


   curr.execute('''SELECT
                   cities.city, todays_temp.temperature, historic_temp.ten_year_temp, historic_temp.twenty_five_year_temp
                   FROM cities JOIN todays_temp ON cities.city_id = todays_temp.city_id
                   JOIN historic_temp ON todays_temp.city_id = historic_temp.city_id
               ''')
  


   conn.commit()
   result = curr.fetchall()


   difference_list = []
   for row in result:
       city = row[0]
       tenyeardifference = round((float(row[1] - row[2])), 2)
       twentyfiveyeardifference = round((float(row[1] - row[3])), 2)
       historic_difference = round((float(row[2] - row[3])))
       t = (city, tenyeardifference, twentyfiveyeardifference, historic_difference)
       difference_list.append(t)


   conn.close()
   return difference_list


def calculate_distance_between_points():
   conn = sqlite3.connect('weather_data.db')
   curr = conn.cursor()


   ann_arbor = geocoding([('Ann Arbor', 'Michigan')])
   ann_arbor_lat = ann_arbor[0][0] / 57.29577951
   ann_arbor_long = ann_arbor[0][1] / 57.29577951


   curr.execute('''SELECT
                   cities.city_id, cities.city, coordinates.city_id, coordinates.latitude, coordinates.longitude
                   FROM cities JOIN coordinates ON cities.city_id = coordinates.city_id
               ''')
  
   conn.commit()
   result = curr.fetchall()


   distance_list = []
   for row in result:
       print(row)
       city = row[1]
       latitude = row[3] / 57.29577951
       longitude = row[4] / 57.29577951
       distance = round((3963.0 * math.acos((math.sin((ann_arbor_lat)) * math.sin((latitude))) + math.cos((ann_arbor_lat)) * math.cos((latitude)) * math.cos((longitude - ann_arbor_long)))), 2)
       distance_list.append((city, distance))
  
   conn.close()
   return distance_list


print(calculate_distance_between_points())



