# TODO:
#     - create the screen
#     - create and move the paddle
#     -create another paddle
#     -create and move the ball
#     -detect collision with wall and create bounce
#     -detect collision with paddle
#     -detect when paddle misses
#     -keep score


from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()





screen.listen()

screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True

l_player_score = 0
r_player_score = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with upper walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("wall bounce")
        ball.bounce_y()


    # detect collision with either paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        print("paddle bounce")
        ball.bounce_x()




screen.exitonclick()
