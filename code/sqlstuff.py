import sqlite3
from calls import *
from main import *
from calc import *


temp_data = main()
current_temps = temp_data[0]
ten_temps = temp_data[1]
twentyfive_temps = temp_data[2]
list_coords = temp_data[3]


def sql():
   conn = sqlite3.connect("weather_data.db")
   curr = conn.cursor()


   curr.execute('''
           CREATE TABLE IF NOT EXISTS cities (
               city_id INTEGER PRIMARY KEY,
               city TEXT NOT NULL,
               state_id INTEGER
           )
       ''')


   curr.execute('''
           CREATE TABLE IF NOT EXISTS state_ids (
               state_id INTEGER PRIMARY KEY,
               state TEXT NOT NULL
           )
       ''')


   curr.execute('''
           CREATE TABLE IF NOT EXISTS coordinates (
               city_id INTEGER PRIMARY KEY,
               latitude INTEGER,
               longitude INTEGER
           )
       ''')


   #Current Weather
   curr.execute('''
           CREATE TABLE IF NOT EXISTS todays_temp (
               city_id INTEGER PRIMARY KEY,
               temperature INTEGER
           )
       ''')


   #Historical Weather
   curr.execute('''
           CREATE TABLE IF NOT EXISTS historic_temp (
               city_id INTEGER PRIMARY KEY,
               ten_year_temp INTEGER,
               twenty_five_year_temp INTEGER
           )
       ''')
   conn.commit()


def city_sql():


    conn = sqlite3.connect("weather_data.db")
    curr = conn.cursor()
  
    cities = city_list()
    x = 0
    last = ""
    curr.execute("SELECT COUNT(*) FROM cities")
    result = curr.fetchall()[0][0]
    c_id = 0
    s_id = 0
    if result >= 1:
        c_id = result
        s_id = result // 2
    for c in cities[result:]:
        if x == 25:
            break
        city = c[0]
        if city == "Portland" and c_id == 36:
            city = "Portland, ME"
        if city == "Portland" and c_id == 72:
            city = "Portland, OR"
        if city == "Columbus" and c_id == 19:
            city = "Columbus, GA"
        if city == "Columbus" and c_id == 68:
            city = "Columbus, OH"
        if city == "Columbia" and c_id == 39:
            city = "Columbia, MD"
        if city == "Columbia" and c_id == 79:
            city = "Columbia, SC"
        state = c[1]
        c_id += 1
        x += 1
        if state != last:
            s_id += 1
            last = state
        curr.execute('''
            INSERT INTO cities
            (city_id, city, state_id)
            VALUES (?, ?, ?)
            ''',
            (c_id, city, s_id))
          
        curr.execute('''
            INSERT OR IGNORE INTO state_ids
            (state_id, state)
            VALUES (?, ?)
            ''',
            (s_id, state))
    conn.commit()


def coord_sql():
   conn = sqlite3.connect("weather_data.db")
   curr = conn.cursor()
   curr.execute("SELECT COUNT(*) FROM coordinates")
   result = curr.fetchall()[0][0]
   x = 0
   c_id = 0
   if result >= 1:
        c_id = result
   for coords in list_coords[result:]:
       if x == 25:
           break
       lat = coords[0]
       long = coords[1]
       c_id += 1
       x += 1
       curr.execute('''
               INSERT INTO coordinates
                   (city_id, latitude, longitude)
                   VALUES (?, ?, ?)
                   ''',
                   (c_id, lat, long))
   conn.commit()


def current_sql():
   conn = sqlite3.connect("weather_data.db")
   curr = conn.cursor()
   curr.execute("SELECT COUNT(*) FROM todays_temp")
   result = curr.fetchall()[0][0]
   x = 0
   c_id = 0
   if result >= 1:
        c_id = result
   for temp in current_temps[result:]:
       if x == 25:
           break
       c_id += 1
       x += 1
       curr.execute('''
               INSERT INTO todays_temp
                   (city_id, temperature)
                   VALUES (?, ?)
                   ''',
                   (c_id, current_temps[(c_id - 1)]))
   conn.commit()


def historic_sql():
   conn = sqlite3.connect("weather_data.db")
   curr = conn.cursor()
   curr.execute("SELECT COUNT(*) FROM historic_temp")
   result = curr.fetchall()[0][0]
   x = 0
   c_id = 0
   z = zip(ten_temps,twentyfive_temps)
   l = list(z)
   print(type(l))
   if result >= 1:
        c_id = result
   for ten_year, twenfive_year in l[result:]:
       if x == 25:
           break
       c_id += 1
       x += 1
       curr.execute('''
               INSERT INTO historic_temp
                   (city_id, ten_year_temp, twenty_five_year_temp)
                   VALUES (?, ?, ?)
                   ''',
                   (c_id, ten_year, twenfive_year))
   conn.commit()





def run():
    city_sql()
    coord_sql()
    current_sql()
    historic_sql()

sql()
run()
run()
run()
run()