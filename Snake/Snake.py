from turtle import Turtle, turtles


class Snake:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        starting_pos = [0, -20, -40, -60]
        self.turtles: list[Turtle] = []
        for pos in starting_pos:
            tur = Turtle('square')
            tur.penup()
            tur.color('White')

            tur.setpos(pos, 0)
            self.turtles.append(tur)

    def set_heading(self, angle: int):
        heading = self.turtles[0].heading()
        if heading == angle + 180 or heading == angle - 180:
            return
        self.turtles[0].setheading(angle)

    def move(self):
        for i in range(len(self.turtles)-1, 0, -1):
            x = self.turtles[i-1].xcor()
            y = self.turtles[i-1].ycor()
            self.turtles[i].setpos(x, y)
        self.turtles[0].fd(20)

    def continue_game(self) -> bool:

        for tur in self.turtles[1:]:
            if self.turtles[0].distance(tur) < 15:
                return False
        pos = self.turtles[0].pos()
        if abs(pos[0]) > self.width/2-10 or abs(pos[1]) > self.height/2-10:
            return False

        return True

    def head(self) -> Turtle:
        return self.turtles[0]

    def extend(self):
        tur = Turtle('square')
        tur.penup()
        tur.color('White')
        tur.setpos(self.turtles[-1].pos())
        self.turtles.append(tur)
