from sqlstuff import *
import sqlite3

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
        print(row)
        city = row[0]
        tenyeardifference = round((float(row[1] - row[2])), 2)
        twentyfiveyeardifference = round((float(row[1] - row[3])), 2)
        t = (city, tenyeardifference, twentyfiveyeardifference)
        difference_list.append(t)

    conn.close()
    return difference_list
    #curr.execute('''SELECT previous, Present, previous-Present as Difference from tablename
                #''')
print(calculate_temp_difference())