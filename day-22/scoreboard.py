from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_player_score = 0
        self.right_player_score = 0
        self.ht()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_player_score} : {self.right_player_score}", align="center", font=("Arial", 24, "normal"))

    def left_score(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def right_score(self):
        self.right_player_score += 1
        self.update_scoreboard()
