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
print(new_numbers)

