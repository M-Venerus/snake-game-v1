from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 12, "normal"))
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 12, "normal"))