import sqlite3
from calls import *
from main import *



conn = sqlite3.connect("weather_data.db")
curr = conn.cursor()


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
                (city_id, city, state_id, state)
                VALUES (?, ?, ?, ?) 
                ''', 
                (c_id, city, s_id, state))
    conn.commit()


        
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

temp_data = main()

current_temps = temp_data[0]
ten_temps = temp_data[1]
twentyfive_temps = temp_data[2]


#Current Weather
c_id = 1
for temp in current_temps:
    print(f"current: {temp}")
    #print(current_temps[(c_id - 1)])
    curr.execute('''
            INSERT OR REPLACE INTO todays_temp
                 (city_id, temperature)
                 VALUES (?, ?)
                 ''',
                 (c_id, current_temps[(c_id - 1)])) 
    c_id += 1
    conn.commit()

c_id = 1
for ten_year, twenfive_year in zip(ten_temps,twentyfive_temps):
    print(f"10: {ten_year}, 25: {twenfive_year}")
    curr.execute('''
            INSERT INTO historic_temp
                 (city_id, ten_year_temp, twenty_five_year_temp)
                 VALUES (?, ?, ?)
                 ''',
                 (c_id, ten_year, twenfive_year)) 
    c_id += 1
    conn.commit()


#Historical Weather
# c_id = 1
# for temp in ten_temps:
#     print(f"10: {temp}")
#     #print(ten_temps[(c_id - 1)])
#     curr.execute('''
#             INSERT OR REPLACE INTO historic_temp
#                  (city_id, ten_year_temp)
#                  VALUES (?, ?)
#                  ''',
#                  (c_id, ten_temps[(c_id - 1)])) 
#     c_id += 1

# c_id = 1
# for temp in twentyfive_temps:
#     t = []
#     t.append(temp)
#     print(f"25: {temp}")
#     #print(twentyfive_temps[(c_id - 1)])
#     curr.execute('''
#             INSERT OR REPLACE INTO historic_temp
#                  (twenty_five_year_temp)
#                  VALUES (?)
#                  ''',
#                  (t))
#     c_id += 1