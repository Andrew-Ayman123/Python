from turtle import Turtle


class Dashed(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.penup()
        self.color('White')
        self.pensize(3)
        self.setpos(0, -300)
        self.seth(90)

        while self.ycor() <= 300:
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)
