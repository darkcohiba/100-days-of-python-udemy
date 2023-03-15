import random

# random number
random_interger = random.randint(0,100)
print (round(random.random(), 2) * 100)

# lab 1
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲



#Write the rest of your code below this line 👇
import random
random_num = random.randint(0,1)
if random_num == 1:
    print ("Heads")
else:
    print("Tails")

# lab 2
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
name_length = len(names) - 1
random_number = random.randint(0, name_length)
payer = names[random_number]
print(f"{payer} is going to buy the meal today!")