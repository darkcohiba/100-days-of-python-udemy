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

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# creating paddle
# paddle = Turtle("square")
# paddle.goto(350, 0)
# paddle.color("white")
# paddle.turtlesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

screen.listen()

# screen.onkey(key="Up", fun=go_up)
# screen.onkey(key="Down", fun=go_down)

game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()
