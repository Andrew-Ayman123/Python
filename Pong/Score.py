from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.penup()
        self.color('White')
        self.goto((0,220))
        self.rscore=0
        self.lscore=0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'{self.lscore}  {self.rscore}', align='center',
                   font=('Courier', 60, 'normal'))
