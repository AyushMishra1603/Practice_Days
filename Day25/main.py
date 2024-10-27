import csv
import pandas

# with open("weather_data.csv") as file:
#     read  = file.readlines()
#     print(read)

"""Working with CSV"""
# with open("weather_data.csv") as file:
#     read = list(csv.reader(file))
#     temperature = []
#     for row in read:
#         if row[1].isdigit():
#             temperature.append(int(row[1]))
#     print(temperature)

""" Working with pandas """
#data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# #print(data_dict)
# temp_list = data["temp"].to_list()
# #print(temp_list)
#
# def average(list_1):
#     return sum(list_1)/len(list_1)

#print(round(average(temp_list),2))

#print(data["temp"].max())
#print(data[data["temp"] == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp = monday.temp
#
# print((temp * 9/5) + 32)

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
