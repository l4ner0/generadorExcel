import json
import csv

with open("data.json") as file:
       data = json.load(file)

with open("dataCSV.csv", "w", newline='') as file:
       csv_file = csv.writer(file)
       csv_file.writerow(data[0])
       for item in data:
           csv_file.writerow(item.values())