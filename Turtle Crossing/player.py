from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape='turtle')
        self.color('Black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self)->None:
        self.forward(MOVE_DISTANCE)

    def is_finished(self)->bool:
        return self.ycor()>=280 

    def reset_player(self)->None:
        self.goto(STARTING_POSITION)
