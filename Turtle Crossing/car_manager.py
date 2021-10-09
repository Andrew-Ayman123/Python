from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.all_cars: list[Turtle] = []

    def create_car(self) -> None:
        if randint(1, 5) == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.goto(300, randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self, level: int):
        delete_cars: list[Turtle] = []
        for car in self.all_cars:
            car.backward(
                min((STARTING_MOVE_DISTANCE+level/5*MOVE_INCREMENT), 50))
            if car.xcor() <= -300:
                delete_cars.append(car)
            
        for car in delete_cars:
            car.reset()
            car.hideturtle()
            self.all_cars.remove(car)
            del car
