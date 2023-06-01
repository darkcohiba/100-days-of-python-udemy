# list comprehension
# new_list = [new_item for item in list]

old_list = [1, 2, 3]
times_2 = [n * 2 for n in old_list]
# print(times_2)
names = ["sam", "nInfa", "adam"]
correct_names = [n.title() for n in names]
# print(correct_names)

# list comprehension with strings
name = "Sam"
new_name = [letter for letter in name]
# print(new_name)

# working with ranges
new_numbers = [num * 2 for num in range(1,5)]
# print(new_numbers)

# conditional comprehension
# [new_item for item in list if test]
conditional_names = ["Allison", "beth", "Caroline", "FRed", "Peter", "David", "Seb", "Tom"]
short_names = [name.title() for name in conditional_names if len(name) <= 4]
# print(short_names)

# square numbers
numbers= [1, 2, 3, 4, 5]
exponent_num = [num **2 for num in numbers]
# print(exponent_num)

# even numbers
even_num = [num for num in numbers if num%2 == 0]
# print(even_num)

# dict comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
students = ["Sam", "Max", "Alex", "Smith"]

from random import randint as ri
student_grades = {item:ri(50, 99) for item in students}
# print(student_grades)
students_passed = {student:score for (student, score) in student_grades.items() if score > 70}
# print(students_passed)

sentence = "What is the airspeed velocity of an unloaden swallow?"
sentence_words = sentence.split(" ")
sentence_dict = {word:len(word) for word in sentence_words}
sentence_dict_two = {word:len(word) for word in sentence.split(" ")}
# print(sentence_dict_two)
# print(sentence_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

def convert_to_f(c):
    return (c * 9 / 5) + 32

weather_f ={key:convert_to_f(value) for (key, value) in weather_c.items()}
weather_f_sol ={key:(value * 9/5) +32 for (key, value) in weather_c.items()}
# print(weather_f_sol)
# print(weather_f)


student_grades = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas
import time

student_data_frame = pandas.DataFrame(student_grades)
# print(student_data_frame)

# loop through rows of data with pandas
# for (index, row) in student_data_frame.iterrows():
#     if (row.score > 80):
        # print(type(row))
        # print("the only passing student is...")
        # time.sleep(3)
        # print(row.student, row.score)
# dictionary comprehension using dataframes:
# {new_key:new_value for (index, row) in df.iterrows()}

nato_alpha_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alpha_csv)
nato_alpha_dict = {row.letter:row.code for (index, row) in nato_alpha_csv.iterrows()}
name = input("Enter your name: ").upper()
nato_name = [nato_alpha_dict[letter] for letter in name]
print(nato_name)