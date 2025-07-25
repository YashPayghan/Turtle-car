from random import random
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []


    def create_car(self):
        random_choice = random.randint(0,6)
        if random_choice == 1 :
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_car.penup()
            random_y=random.randint(-250,250)
            new_car.goto(280,random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        new_speed=STARTING_MOVE_DISTANCE+MOVE_INCREMENT
        for car in self.all_cars:
            car.forward(new_speed)







