from turtle import Turtle
from random import randint as rt

balls = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10

        self.create_ball()

    def create_ball(self):
        print("new ball")
        self.penup()
        self.shape("circle")
        self.color("white")
        global balls
        if balls != 0:
            new_x = rt(-225, 225)
            new_y = rt(-225, 225)
            print(new_x, new_y)
            self.goto(new_x, new_y)
        balls += 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1



