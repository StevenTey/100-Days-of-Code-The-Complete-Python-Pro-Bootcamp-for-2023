COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

# Create a Car Manager that will randomly generate the cars that the turtle has to avoid.


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.create_car()
        self.move_distance = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        # generate a list of random y coordinates between -250 and 250 with a step of 20
        # random_y = random.choice(range(-250, 250, 20))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)
    
    def level_up(self):
        self.move_distance += MOVE_INCREMENT
        
