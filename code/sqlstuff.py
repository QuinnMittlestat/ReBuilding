import sqlite3



conn = sqlite3.connect("weather_data.db")
curr = conn.cursor()

curr.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            city TEXT NOT NULL,
            state TEXT NOT NULL
        )
    ''')

curr.execute('''
        CREATE TABLE IF NOT EXISTS todays_temp (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            temperature INTEGER
        )
    ''')

curr.execute('''
        CREATE TABLE IF NOT EXISTS historic_temp (
            id INTEGER PRIMARY KEY,
            historic_date TEXT NOT NULL,
            historic_temperature INTEGER
        )
    ''')