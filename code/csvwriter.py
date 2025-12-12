import csv

calculate_temp_difference = __import__('calc').calculate_temp_difference
with open('temperature_differences.csv', mode='w', newline='') as file:
    writer = csv.writer(file)