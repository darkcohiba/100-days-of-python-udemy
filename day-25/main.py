
# weather_data = []
# with open("weather_data.csv") as f:
#     contents = f.readlines()
#     for day in contents:
#         weather_data.append(day)

import csv

with open("weather_data.csv") as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        print(row[1])
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)