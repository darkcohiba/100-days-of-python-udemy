from turtle import Turtle, Screen

sam_the_turt = Turtle()
sam_the_turt.shape("turtle")
# challenge 1, create a square
for x in range(4):
    sam_the_turt.forward(100)
    sam_the_turt.left(90)

screen = Screen()
screen.exitonclick()
