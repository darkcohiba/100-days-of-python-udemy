import turtle
from turtle import Turtle, Screen
import random

stt = Turtle()
# stt.shape("turtle")
# challenge 1, create a square
# for x in range(4):
#     stt.forward(100)
#     stt.left(90)


# challenge 2 dashed line
# for _ in range(50):
#     stt.pendown()
#     stt.forward(random.randint(15, 175))
#     stt.penup()
#     stt.forward(random.randint(15, 175))
#     stt.left(random.randint(15, 175))

# challenge 3 shape in shape
# sides = 3
# colors = ["red", "yellow", "blue", "pink", "lime green", "spring green", "indigo", "maroon", "saddle brown"]
# for _ in range(9):
#     angle = 360 / sides
#     color = random.choice(colors)
#     colors.remove(color)
#     stt.pencolor(color)
#     for _ in range(sides):
#         stt.forward(100)
#         stt.right(angle)
#     sides += 1
#     print(color)

# challenge 4 random path
# choice = ["left", "right"]
# colors = ["red", "yellow", "blue", "pink", "lime green", "spring green", "indigo", "maroon", "saddle brown"]
# direction = [0, 90, 180, 270]
# stt.width(10)
# stt.pensize(10)
# stt.speed("fastest")
#
# for _ in range(500):
#     color = random.choice(colors)
#     stt.color(color)
#     stt.forward(25)
#     stt.setheading(random.choice(direction))
#
# for _ in range(30):
#     color = random.choice(colors)
#     stt.color(color)
#     stt.forward(25)
#     if random.randint(0, 1):
#         stt.right(90)
#     else:
#         stt.left(90)

# hirst painting trial
# colors = ["red", "yellow", "blue", "pink", "lime green", "spring green", "indigo", "maroon", "saddle brown"]
# stt.width(10)

#
# def space():
#     stt.penup()
#     stt.forward(20)
#
#
# def dot():
#     stt.pendown()
#     stt.forward(10)
#
#
# def move_a_line():
#     for _ in range(10):
#         dot()
#         space()
#         dot()
#
#
# def turn_right():
#     stt.right(90)
#
#
# def turn_left():
#     stt.left(90)
#
#
# def move_up_line_right():
#     turn_right()
#     space()
#     turn_right()
#
#
# def move_up_line_left():
#     turn_left()
#     space()
#     turn_left()
#
#
# def set_color():
#     color = random.choice(colors)
#     stt.color(color)
#
#
# def set_posit(x, y):
#     stt.penup()
#     stt.setposition(x, y)
#     stt.pendown()
#
#
# set_posit(-200, -200)
#
# def cycle_left():
#     move_a_line()
#     set_color()
#     move_up_line_left()
#     set_color()
#
# def cycle_right():
#     move_a_line()
#     set_color()
#     move_up_line_right()
#     set_color()
#
# for _ in range(40):
#     cycle_left()
#     cycle_right()

# challenge spirograph
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

stt.speed("fastest")
for _ in range(100):
    stt.pencolor(random_color())
    stt.circle(80)
    stt.left(3.6)

def draw(size_gap, circle_size):
    for _ in range(round(360 / size_gap)):
        stt.pencolor(random_color())
        stt.circle(circle_size)
        stt.setheading(stt.heading() + size_gap)
#
draw(5, 100)
draw(4, 125)
draw(4, 150)
draw(2, 175)
draw(1, 200)



screen = Screen()
screen.exitonclick()
