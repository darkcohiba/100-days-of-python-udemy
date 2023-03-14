# lab 1 data types
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# lab 2 converting
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (int(weight) / (float(height) * float(height)))
print(int(bmi))