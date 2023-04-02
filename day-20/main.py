from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_position = 0

snakes = []
for _ in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.setposition(x_position, 0)
    x_position -= 20
    snakes.append(new_turtle)






screen.exitonclick()