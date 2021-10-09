from turtle import Turtle


class Score(Turtle):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(visible=False)
        self.color('White')
        self.speed('fastest')
        self.penup()

        self.setpos(0, height/2-40)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f'Score : {self.score}', align='center',
                   font=('Courier', 25, 'normal'))
    def game_over(self):
        self.home()
        self.write(f'GAME OVER', align='center',
                   font=('Courier', 25, 'bold'))
    
    def increment(self):
        self.clear()
        self.score+=1
        self.write_score()
