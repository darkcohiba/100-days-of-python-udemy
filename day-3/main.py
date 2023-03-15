# lab 1
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (number % 2 != 0):
    print("This is an odd number.")
else:
    print("This is an even number.")

# lab 2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (int(weight) / (float(height) * float(height)))
bmi = round(bmi, 2)
# print(bmi)

if bmi > 35:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are clinically obese.")
elif 30 < bmi < 35:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are obese.")
elif 25 < bmi < 30:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 18.5 < bmi < 25:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you have a normal weight.")
else:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are underweight.")


# lab 3
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# lab 4
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        if extra_cheese == "Y":
            bill += 1
        else:
            print(f"Your final bill is: ${bill}.")
        print(f"Your final bill is: ${bill}.")
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
        else:
            print(f"Your final bill is: ${bill}.")
    else: 
        if extra_cheese == "Y":
            bill += 1
        else:
            print(f"Your final bill is: ${bill}.")
        print(f"Your final bill is: ${bill}.")
else: 
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
        else:
            print(f"Your final bill is: ${bill}.")
    else: 
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
    print(f"Your final bill is: ${bill}.")

# lab 5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_t = name1.lower().count("t") + name2.lower().count("t")
total_r = name1.lower().count("r") + name2.lower().count("r")
total_u = name1.lower().count("u") + name2.lower().count("u")
total_e = name1.lower().count("e") + name2.lower().count("e")
total_true = total_r + total_t + total_u + total_e

total_l = name1.lower().count("l") + name2.lower().count("l")
total_o = name1.lower().count("o") + name2.lower().count("o")
total_v = name1.lower().count("v") + name2.lower().count("v")
total_love = total_l + total_v +total_o + total_e
score = str(total_true) + str(total_love)
score = int(score)
if score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
elif score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
else:
    print(f"Your score is {score}.")



