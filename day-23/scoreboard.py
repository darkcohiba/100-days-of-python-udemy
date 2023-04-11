from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.write_level()

    def write_level(self):
        self.goto(-280, 260)
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="left", font=FONT )




