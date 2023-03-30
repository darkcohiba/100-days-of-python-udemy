import random
from turtle import Turtle, Screen
from time import sleep

# tim = Turtle()
screen = Screen()

# etch a sketch
# def reset_turtle():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="Up", fun=lambda: tim.forward(10))
# screen.onkey(key="Left", fun=lambda: tim.left(10))
# screen.onkey(key="Right", fun=lambda: tim.right(10))
# screen.onkey(key="Down", fun=lambda: tim.back(10))
# screen.onkey(key="space", fun=reset_turtle)


# turtle race
turtle_names = ["sam", "yese", "ste", "dav", "matt", "cryp", "leslie", "esy", "grape", "leo", "bark"]
colors = ["red", "yellow", "blue", "pink", "lime green", "spring green", "indigo", "maroon", "saddle brown", "black"]

final_turtles = []

def start_race(name):
    speed = random.randint(0, 9)
    name.speed(speed)
    name.forward(500)

def set_up(turts):
    starting_x = -200
    starting_y = -200
    for _ in range(turts):
        name = random.choice(turtle_names)
        color = random.choice(colors)
        colors.remove(color)
        turtle_names.remove(name)

        name = Turtle()
        name.penup()
        name.shape("turtle")
        name.color(color)
        name.setposition(starting_x, starting_y)

        starting_y += 40
        final_turtles.append(name)

set_up(10)
for turt in final_turtles:
    start_race(turt)




screen.exitonclick()