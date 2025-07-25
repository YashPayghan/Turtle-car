import time
import turtle
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.create_score()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    #detect collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > FINISH_LINE_Y :
        player.goto(STARTING_POSITION)
        scoreboard.increse_level()
        car_manager.increase_speed()






screen.exitonclick()
