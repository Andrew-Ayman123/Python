from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape='circle')
        self.color('White')
        self.penup()
        self.home()
        self.xinc = 5
        self.yinc = 5
        self.move_speed = .05

    def move(self) -> None:

        self.goto(self.xcor()+self.xinc, self.ycor()+self.yinc)

    def y_bounce(self):
        self.yinc *= -1

    def x_bounce(self):
        if self.move_speed > .005:
            self.move_speed *= .9

        self.xinc *= -1

    def reset_ball(self):
        self.home()
        self.x_bounce()
        self.move_speed = .05
