import matplotlib
import matplotlib.pyplot as plt
import sqlite3
from calls import *

conn = sqlite3.connect('weather_data.db')
curr = conn.cursor()

curr.execute('''
        SELECT city, state FROM cities JOIN state_ids ON cities.city_id = state_ids.state_id
              ''')

conn.commit()
cities_data = curr.fetchall()
print(cities_data)

temps = [36.0, 35.0, 1.0, 9.0, 52.0, 47.0, 41.0, 42.0, 54.0, 55.0, 34.0, 36.0, 22.0, 22.0, 25.0, 25.0, 40.0, 64.0, 35.0, 33.0, 71.0, 69.0, 39.0, 36.0, 25.0, 23.0, 26.0, 21.0, 20.0, 17.0, 38.0, 30.0, 31.0, 29.0, 48.0, 45.0, 18.0, 11.0, 28.0, 24.0, 21.0, 18.0, 16.0, 14.0, 12.0, 12.0, 41.0, 45.0, 30.0, 30.0, 14.0, 40.0, 25.0, 26.0, 52.0, 52.0, 13.0, 16.0, 24.0, 27.0, 35.0, 36.0, 29.0, 14.0, 32.0, 29.0, -2.0, -3.0, 26.0, 24.0, 44.0, 42.0, 50.0, 48.0, 26.0, 21.0, 21.0, 22.0, 38.0, 32.0, 12.0, 21.0, 37.0, 42.0, 55.0, 51.0, 37.0, 36.0, 13.0, 12.0, 31.0, 28.0, 47.0, 41.0, 27.0, 28.0, 16.0, 10.0, 31.0, 33.0]

cities = []
states = []
last = ''
for i in cities_data:
    cities.append(i[0])


print(cities)
print(states)

def city_temps_current():

    y = cities
    x = temps

    fig, ax = plt.subplots()
    ax.scatter(y, x)
    ax.set_xlabel('city')
    ax.set_ylabel('temp')
    ax.set_title('temp/city')
    ax.grid()
    plt.show()

def state_temps_current():
    y = states
    x = state_temps

    fig, ax = plt.subplots()
    ax.bar(y, x)
    ax.set_xlabel('state')
    ax.set_ylabel('temp')
    ax.set_title('state/city')
    ax.grid()
    plt.show()

def state_temps_comparison():
    y = states
    x1 = state_temps
    x2 = ten_state_temps
    x3 = tf_state_temps

    fig, ax = plt.subplots()
    ax.bar(y, x1)
    ax.bar(y, x2)
    ax.bar(y, x3)
    ax.set_xlabel('state')
    ax.set_ylabel('temp')
    ax.set_title('state/city')
    ax.grid()
    plt.show()

#state_temps_comparison()
#city_temps_current()
#state_temps_current()
