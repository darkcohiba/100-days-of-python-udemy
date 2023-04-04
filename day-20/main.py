from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x_position = 0


# for _ in range(3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.setposition(x_position, 0)
#     x_position -= 20
#     snakes.append(new_turtle)

game_is_on = True

# while game_is_on:
#     screen.update()
#     sleep(0.1)
#     for seg_num in range(len(snakes) -1, 0, -1):
#         new_x = snakes[seg_num - 1].xcor()
#         new_y = snakes[seg_num - 1].ycor()
#         snakes[seg_num].goto(new_x, new_y)
#     snakes[0].forward(30)
#     snakes[0].left(90)



screen.exitonclick()