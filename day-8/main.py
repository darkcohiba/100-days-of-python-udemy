# lab 1
#Write your code below this line 👇
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {round(number_of_cans)} cans of paint.")
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# her solution
# import math
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(f"You'll need {round(num_of_cans)} cans of paint.")


# lab 2
#Write your code below this line 👇
def prime_checker(number):
    count = 0
    # while prime == True:
    if number <= 2:
        print("It's a prime number.")
    else:
        for x in range(2, number):
            if number % x == 0:
                count += 1
    if count == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
