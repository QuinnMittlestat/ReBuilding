import matplotlib
import matplotlib.pyplot as plt
import sqlite3
from calls import *
from calc import *


conn = sqlite3.connect('weather_data.db')
curr = conn.cursor()


curr.execute('''
        SELECT city, state, temperature, ten_year_temp, twenty_five_year_temp
        FROM cities JOIN state_ids ON cities.state_id = state_ids.state_id
        JOIN todays_temp ON cities.city_id = todays_temp.city_id
        JOIN historic_temp ON todays_temp.city_id = historic_temp.city_id
              ''')


conn.commit()
data = curr.fetchall()
#print(data)


cities = []
states = []
states_doubled = []
current_temps = []
ten_temps = []
tf_temps = []
last = ""
for i in data:
    cities.append(i[0])
    if i[1] != last:
        states.append(i[1])
        last = i[1]
    states_doubled.append(i[1])
    current_temps.append(i[2])
    ten_temps.append(i[3])
    tf_temps.append(i[4])


ten_differences = []
tf_differeces = []
distances = []


d1 = calculate_temp_difference()
d2 = calculate_distance_between_points()


for i in d1:
    ten_differences.append(i[1])
    tf_differeces.append(i[2])
for i in d2:
    distances.append(i[1])


avg_diffs = []
for i in zip(ten_differences, tf_differeces):
    avg_diffs.append(round(i[0] + i[1]))


state_diffs = []
id = 0
for i in range(50):
    state_diffs.append((avg_diffs[id] + avg_diffs[id+1]) / 2)
    id += 2


font = {'weight': 'bold', 'size': 5}
matplotlib.rc('font', **font)


def cities_vs_ten():
    y = cities
    x = ten_differences


    fig, ax = plt.subplots()
    bar = ax.bar(y, x, color="#D92828")
    ax.bar_label(bar, ten_differences)


    ax.set_xlabel('City', fontsize=10)
    ax.set_ylabel('Difference in Temperature', fontsize=10)
    ax.grid()


    plt.title('Difference Between Current and 10 Year Temperatures for Each City', fontsize=15)
    plt.xticks(rotation=90)
    plt.show()


def cities_vs_25():
    y = cities
    x = tf_differeces


    fig, ax = plt.subplots()
    bar = ax.bar(y, x, color="#CD7036")
    ax.bar_label(bar, tf_differeces)


    ax.set_xlabel('City', fontsize=10)
    ax.set_ylabel('Difference in Temperature', fontsize=10)
    ax.grid()


    plt.title('Difference Between Current and 25 Year Temperatures for Each City', fontsize=15)
    plt.xticks(rotation=90)
    plt.show()


def city_avg():
    x = avg_diffs


    fig, ax = plt.subplots()
    ax.hist(x, 25, color="#5A96F0")
    ax.set_ylabel('Frequency of Temperature Change', fontsize=10)
    ax.set_xlabel('Difference in Temperature', fontsize=10)
    ax.grid()


    plt.title('Average Change in Temperature for Cities', fontsize=15)
    plt.show()


def state_avg():
    x = state_diffs


    fig, ax = plt.subplots()
    ax.hist(x, 25, color="#AC0764")
    ax.set_ylabel('Frequency of Temperature Change', fontsize=10)
    ax.set_xlabel('Difference in Temperature', fontsize=10)
    ax.grid()


    plt.title('Average Change in Temperature for States', fontsize=15)
    plt.show()


def distance_to_AA():
    y = cities
    x = distances


    fig, ax = plt.subplots()
    bar = ax.bar(y, x, color='lime')
    ax.bar_label(bar, distances)
    ax.set_xlabel('Cities', fontsize=10)
    ax.set_ylabel('Distance (mi)', fontsize=10)
    ax.grid()


    plt.title('Distance From Each City to Ann Arbor ', fontsize=15)
    plt.xticks(rotation=90)
    plt.show()




cities_vs_ten()
cities_vs_25()
city_avg()
state_avg()
distance_to_AA()



