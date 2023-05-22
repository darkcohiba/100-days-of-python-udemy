# weather_data = []
# with open("weather_data.csv") as f:
#     contents = f.readlines()
#     for day in contents:
#         weather_data.append(day)

# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# print(len(data.temp))
# print(data.temp)
# print(data["temp"])

# getting a row
# print(data[data.day == "Monday"])

# print(data.temp.max())
# get the rows with the highest temp
# print(data[data.temp == data.temp.max()])


# convert temp to farenheit
# def convert(temp):
#     return (temp * 9 / 5) + 32


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp)
# print(convert(monday_temp))


# create a new csv
# student_dict = {
#     "students": ["Amy", "Sam", "Gabe"],
#     "scores": [50, 60, 80]
# }

# new_data = pandas.DataFrame(student_dict)
# print(new_data)
# new_data.to_csv("student_data.csv")

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur = squirrel_data["Primary Fur Color"]
print(fur)


