from turtle import Turtle, Screen
import random

# input1 = int(input("How far forward should the turtle move? "))
treasure_x = random.randint(-150, 150)
treasure_y = random.randint(-150, 150)
treasure = (treasure_y, treasure_x)
print(treasure)

def move(direction, paces):
    if direction == "forward":
        sam.forward(paces)
    elif direction == "left":
        sam.left(paces)
    elif direction == "right":
        sam.right(paces)
    elif direction == "back":
        sam.back(paces)
    elif direction == "position":
        print(sam.position())

def compare(location, treasure):
    # print(treasure[0])
    # print(round(location[0]))
    if treasure[0] == round(location[0]) and treasure[1] == round(location[1]):
        return True
    else:
        return False

sam = Turtle()
sam.shape("turtle")
continue_tell = compare(sam.position(), treasure)
# sam.penup()
sam.hideturtle()
sam.setposition(treasure)
sam.setposition(0, 0)
sam.showturtle()
# sam.pendown()
# print(continue_tell)
while not continue_tell:
    direction = input("What direction should we go,back, forward, right, left?: ")
    paces = int(input("How far in that direction or to that angle should the turtle move? "))
    move(direction, paces)
    # sam.position()
    # print(compare(sam.position(), treasure))
    continue_tell = compare(sam.position(), treasure)
print("You made it out of the loop you win!")
screen = Screen()
screen.exitonclick()



# the real thing
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
