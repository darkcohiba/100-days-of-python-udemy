# imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x_position = 0

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

#     detecting food
    if snake.head.distance(food) < 15:
        print('nom nom nom')
        food.refresh()
        score.increase_score()
        snake.extend()


#     detect collison with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        print("you dead")
        score.game_over()
        # screen.bye()
        game_is_on = False

#     detach collision of tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False



screen.exitonclick()
