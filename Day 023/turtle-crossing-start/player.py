STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
# Idea dump:
# - Create a new class called Player that inherits from the Turtle class.
# - Create a move method in the Player class that moves the turtle object by a fixed amount of pixels each time the up key is pressed.

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
