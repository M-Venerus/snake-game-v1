from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mike's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_speed = 0.2
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        scoreboard.update_score()
        snake.extend()
        game_speed *= 0.9

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
        
scoreboard.final_score()
        
    
        

screen.exitonclick()
