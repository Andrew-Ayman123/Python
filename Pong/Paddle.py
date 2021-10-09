from turtle import Turtle, pos
from typing import Tuple


class Paddle(Turtle):
    def __init__(self, position: Tuple[int, int]):

        super().__init__(shape='square')
        self.color('White')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_upward(self):
        self.goto(self.xcor(), self.ycor()+20)

    def move_downword(self):
        self.goto(self.xcor(), self.ycor()-20)
