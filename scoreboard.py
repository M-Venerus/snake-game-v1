from turtle import Turtle
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"Score = {self.score}", False, align="center", font=FONT)
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=FONT)
        
    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER. Final score: {self.score}", False, align="center", font=FONT)