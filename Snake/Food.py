from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, width: int, height: int) -> None:
        super().__init__('circle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')
        self.width = width
        self.height = height
        self.go_to_rand()

    def go_to_rand(self):
        pad=20
        x = randint(-self.width/2+pad, self.width/2-pad)
        y = randint(-self.height/2+pad, self.height/2-pad)
        self.goto(x, y)
