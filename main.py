from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mike's Snake Game")

all_turtles = []

for i in range(0, 41, 20):
    new_turt = Turtle(shape="square")
    new_turt.color("white")
    new_turt.penup()
    new_turt.goto(x=-i, y=0)



















screen.exitonclick()
