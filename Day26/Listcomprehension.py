new_list = [number*2 for number in range(1, 5)]

print(new_list)

names = ["Ayush", "Anjali", "Deepa", "Shivi", "Aman", "love"]
short_names = [name.upper() for name in names if len(name) < 6]
print(short_names)

"""New problem: Squaring Numbers"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

"""New Problem: Filtering Even Numbers"""
list_of_strings = ['9','0','32','8', '2', '8', '64', '29', '42', '99']
numbers = [int(item) for item in list_of_strings]
results = [even_num for even_num in numbers if even_num % 2 == 0]
print(results)
