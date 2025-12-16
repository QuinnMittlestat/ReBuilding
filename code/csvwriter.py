import csv
from calc import *

data1 = calculate_temp_difference()
data2 = calculate_distance_between_points()

def create_output_file():
    with open('calculations.txt','w') as output_file:
        output_file.write('City Name, 10 year difference, 25 year difference, Difference between 10 and 25 years\n')
        for line in data1:
            output_file.write(f'{line}\n')
        output_file.write('City Name, Distance from Ann Arbor (miles)\n')
        for x in data2:
            output_file.write(f'{x}\n')
    return output_file

def read_output_file():
    with open('calculations.txt','r') as results:
        results = results.read()
    return results

create_output_file()
read_output_file()