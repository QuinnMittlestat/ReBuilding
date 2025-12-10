import sqlite3
from calls import *



conn = sqlite3.connect("weather_data.db")
curr = conn.cursor()

curr.execute('DROP TABLE cities')

#Cities
curr.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            city_id INTEGER PRIMARY KEY,
            city TEXT NOT NULL,
            state_id INTEGER, 
            state TEXT NOT NULL
        )
    ''')

cities = city_list()
c_id = 0
s_id = 0
last = ""
for c in cities:
    city = c[0]
    print(city)
    state = c[1]
    print(state)
    c_id += 1
    print(f"c = {c_id}")
    print(f"last = {last}")
    if state != last:
        s_id += 1
        last = state
        print(f"s = {s_id}")
        print(f"last = {last}")
    curr.execute('''
            INSERT INTO cities 
                (city_id, city, state_id, state)
                VALUES (?, ?, ?, ?) 
                ''', 
                (c_id, city, s_id, state))
    


    
        
#Current Weather
curr.execute('''
        CREATE TABLE IF NOT EXISTS todays_temp (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            temperature INTEGER
        )
    ''')

#Historical Weather
curr.execute('''
        CREATE TABLE IF NOT EXISTS historic_temp (
            id INTEGER PRIMARY KEY,
            historic_date TEXT NOT NULL,
            historic_temperature INTEGER
        )
    ''')