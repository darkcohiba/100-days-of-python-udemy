# imports
from turtle import Screen
from snake import Snake
from food import Food
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x_position = 0

snake = Snake()
food = Food()

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

screen.exitonclick()
