fruits = ["Apple", "Peach", "Banana"]

for fruit in fruits:
    print(fruit)

# lab 1
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

total_heights = sum(student_heights)
total_kids = len(student_heights)
average = round(total_heights / total_kids)
print(average)

# lab 2
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
# print(max(student_scores))
for x in student_scores:
    if x > highest_score:
        highest_score = x
print(f"The highest score in the class is: {highest_score}")

# for loop with range
count = 0
for x in range(1, 101):
    count += x

print(count)


# lab 3
#Write your code below this row 👇
total = 0
for x in range(0, 101, 2):
    total += x
print(total)

# lab 4
#Write your code below this row 👇

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
    

