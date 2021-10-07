##LOUIS ADRIAN MENDOZA
import json
import yaml
import csv

with open('covid_cases.json','r') as json_file:
    ourjson = json.load(json_file)

print(type(ourjson))

csv_column = ['dateRep','countriesAndTerritories','cases','deaths']
filename = 'Covid_cases.csv'

with open (filename, 'w') as filename:
    writer = csv.DictWriter(filename, fieldname=csv_column)
    writer.writeheader()
    for i in ourjson:
        writer.writerow(i)

print("Created and import data to CSV file")
print("by Louis Adrian Mendoza")

