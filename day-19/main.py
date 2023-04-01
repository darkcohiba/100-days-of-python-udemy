# import random
# from turtle import Turtle, Screen
# from time import sleep

# tim = Turtle()
# screen = Screen()

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
# turtle_names = ["sam", "yese", "ste", "dav", "matt", "cryp", "leslie", "esy", "grape", "leo", "bark"]
# colors = ["red", "yellow", "blue", "pink", "lime green", "spring green", "indigo", "maroon", "saddle brown", "black"]
#
# final_turtles = []
#
# def start_race(name):
#     speed = random.randint(0, 9)
#     name.speed(speed)
#     name.forward(500)
# screen.listen()
# def set_up(turts):
#     starting_x = -200
#     starting_y = -200
#     for _ in range(turts):
#         name = random.choice(turtle_names)
#         color = random.choice(colors)
#         colors.remove(color)
#         turtle_names.remove(name)
#
#         name = Turtle()
#         name.penup()
#         name.shape("turtle")
#         name.color(color)
#         name.setposition(starting_x, starting_y)
#         # screen.onkey(key="space", fun=lambda: name.forward(100))
#
#         starting_y += 40
#         final_turtles.append(name)
#
#
# set_up(10)

# angelica solution
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors_avail = ["green", "tan", "brown", "pink", "yellow", "blue"]
user_bet = screen.textinput(title="make your bet", prompt=f"Which turtle will win the race, enter a color,\n {colors_avail}")
# print(user_bet)
all_turtles = []
y_var = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors_avail[turtle_index])
    # tim.speed("fastest")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_var[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()