from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0),  (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            self.new_segment = Turtle(shape="square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(position)
            self.segments.append(self.new_segment)

    def move(self):
        for seg_num in range(2, 0, -1):
            self.new_x = self.segments[seg_num -1].xcor()
            self.new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(self.new_x, self.new_y)
        self.segments[0].forward(20)
