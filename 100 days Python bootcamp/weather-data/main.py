import csv
import pandas

with open("100 days Python bootcamp/weather-data/weather_data.csv", "r") as data_file:
    data = csv.reader(data_file, delimiter=',')
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

#--------------------- Pandas ----------------------------

data = pandas.read_csv("100 days Python bootcamp/weather-data/weather_data.csv")
print(data)
print()
print(data["temp"])

temp_list = data["temp"].to_list()
print(f"{temp_list} mean: {data['temp'].mean()}, median: {data['temp'].median()}")

print(data.temp)
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("100 days Python bootcamp/weather-data/new_data.csv")
