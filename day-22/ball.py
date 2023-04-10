from turtle import Turtle
from random import randint as rt
from time import sleep

balls = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

        self.create_ball()

    def create_ball(self):
        """This function will create a ball and the first ball created will go in the center of the screen"""
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
        """This will move the ball diagonally"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Use this to bounce the ball on the y axis, changes the y axis multiplier to negative"""
        self.y_move *= -1
        self.move_speed *= .9

    def bounce_x(self):
        """Use this to bounce the ball on the x axis, changes the x axis multiplier to negative"""
        self.x_move *= -1

    def reset_position(self):
        sleep(1)
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



