import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import GameOver

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake.io")
screen.tracer(0)
screen.update()
game_is_on = True
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = Scoreboard()
gameover = GameOver()

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.06)

    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.updateScore()
        snake.extend()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            break

    if snake.head.xcor() >300 or snake.head.xcor() < -300:
        game_is_on = False

    if snake.head.ycor() >300 or snake.head.ycor() < -300:
        game_is_on = False

if not game_is_on:
    gameover.show_over()

screen.exitonclick()