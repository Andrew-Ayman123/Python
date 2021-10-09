from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self, ) -> None:
        super().__init__(visible=False)
        self.color('Black')
        self.penup()
        self.goto((-280,250))
        self.score=1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f'Level : {self.score}',align='left',font=FONT)

    def increase_level(self):
        self.score+=1
        self.write_level()

    def game_over(self):
        self.home()
        self.write('GAME OVER',align='center',font=("Courier", 25, "bold"))

    def g_score(self):
        return self.score