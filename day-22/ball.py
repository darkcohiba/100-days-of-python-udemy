from turtle import Turtle
from random import randint as rt

balls = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()

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
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)


