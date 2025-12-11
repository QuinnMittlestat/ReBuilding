import sqlite3
from calls import *
from main import *



conn = sqlite3.connect("weather_data.db")
curr = conn.cursor()

temp_data = main()

current_temps = temp_data[0]
ten_temps = temp_data[1]
twentyfive_temps = temp_data[2]

#Cities
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

cities = city_list()
c_id = 0
s_id = 0
last = ""
for c in cities:
    city = c[0]
    #print(city)
    state = c[1]
    #print(state)
    c_id += 1
    #print(f"c = {c_id}")
    #print(f"last = {last}")
    if state != last:
        s_id += 1
        last = state
        #print(f"s = {s_id}")
        #print(f"last = {last}")
    curr.execute('''
            INSERT OR REPLACE INTO cities 
                (city_id, city, state_id)
                VALUES (?, ?, ?) 
                ''', 
                (c_id, city, s_id))
    
    curr.execute('''
            INSERT OR REPLACE INTO state_ids 
                (state_id, state)
                VALUES (?, ?) 
                ''', 
                (s_id, state))

c_id = 1
for temp in current_temps:
    print(f"current: {temp}")
    curr.execute('''
            INSERT OR REPLACE INTO todays_temp
                 (city_id, temperature)
                 VALUES (?, ?)
                 ''',
                 (c_id, current_temps[(c_id - 1)])) 
    c_id += 1

c_id = 1
for ten_year, twenfive_year in zip(ten_temps,twentyfive_temps):
    print(f"10: {ten_year}, 25: {twenfive_year}")
    curr.execute('''
            INSERT OR REPLACE INTO historic_temp
                 (city_id, ten_year_temp, twenty_five_year_temp)
                 VALUES (?, ?, ?)
                 ''',
                 (c_id, ten_year, twenfive_year)) 
    c_id += 1
    
conn.commit()