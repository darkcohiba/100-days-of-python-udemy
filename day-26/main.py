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