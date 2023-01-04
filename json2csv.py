'''
Python program to convert
JSON file to CSV
C:\python\python json2csv.py
'''
import json
import csv

# Open JSON file and loadthe data into the variable salary_data
with open('salary.json') as json_file:
	salary_data  = json.load(json_file)

# Open a file for writing
data_file = open('salary.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

for sal in salary_data:
    csv_writer.writerow(sal.values())    

data_file.close()
