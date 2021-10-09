import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    score = Scoreboard()
    player = Player()
    carM = CarManager()
    screen.listen()
    screen.onkeypress(player.move, 'w')
    is_game_on = True
    while is_game_on:
        time.sleep(0.05)
        screen.update()
        if player.is_finished():
            score.increase_level()
            player.reset_player()
        carM.create_car()
        carM.move_car(score.g_score()-1)
        for car in carM.all_cars:
            if player.distance(car) <= 21:
                is_game_on = False
    score.game_over()
    screen.update()
    screen.exitonclick()


if __name__ == '__main__':
    main()
