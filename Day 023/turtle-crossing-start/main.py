import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
screen.onkeypress(player.move, "Up")
car_manager = CarManager()

i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    i += 1
    screen.update()
    
    if i % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with top wall
    if player.ycor() > 280:
        player.go_to_start()
        scoreboard.level_up()
        car_manager.level_up()    
        
    # Detect 
    for car in car_manager.all_cars:
        if car.distance(player) < 20 and car.distance(player) > 0:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()