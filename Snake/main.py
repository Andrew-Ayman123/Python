from Snake import Snake
from turtle import Turtle, Screen
from time import sleep
from Food import Food
from Score import Score

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title('Snake Game')
    screen.bgcolor('Black')
    screen.tracer(0)
    snake = Snake(600, 600)

    screen.listen()
    screen.onkey(key='w', fun=lambda: snake.set_heading(90))
    screen.onkey(key='a', fun=lambda: snake.set_heading(180))
    screen.onkey(key='s', fun=lambda: snake.set_heading(-90))
    screen.onkey(key='d', fun=lambda: snake.set_heading(0))

    food = Food(600, 600)
    score= Score(600,600)
    screen.update()
    
    while snake.continue_game():
        snake.move()
        if snake.head().distance(food)<15:
            food.go_to_rand()
            score.increment() 
            snake.extend()
        sleep(.1)
        screen.update()
    score.game_over()
    screen.exitonclick()
if __name__ =='__main__':
    main()

