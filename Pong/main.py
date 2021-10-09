from Dashed import Dashed
from Score import Score
from Ball import Ball
from Paddle import Paddle
from turtle import Screen
from time import sleep

WIDTH = 800
HEIGHT = 600


def main():

    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor('Black')
    screen.title('Ping Pong')
    screen.tracer(0)
    # screen.update()
    dashed=Dashed()
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))

    screen.listen()
    screen.onkeypress(key='Up', fun=r_paddle.move_upward)
    screen.onkeypress(key='Down', fun=r_paddle.move_downword)
    screen.onkeypress(key='w', fun=l_paddle.move_upward)
    screen.onkeypress(key='s', fun=l_paddle.move_downword)
    
    ball = Ball()
    score = Score()
    while True:
        ball.move()
        screen.update()
        sleep(ball.move_speed)

        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.y_bounce()
        # Detect Collis ion with r_paddle
        if ball.xcor() >= 340 and ball.distance(r_paddle) <= 55:
            ball.x_bounce()
        # Detect Collision with l_paddle
        elif ball.xcor() <= -340 and ball.distance(l_paddle) <= 55:
            ball.x_bounce()

        if ball.xcor() >= 380:
            score.lscore += 1
            score.write_score()
            ball.reset_ball()

        elif ball.xcor() <= -380:
            score.rscore += 1
            score.write_score()
            ball.reset_ball()


if __name__ == '__main__':
    main()
