FONT = ("Courier", 24, "normal")
from turtle import Turtle

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase.


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        
    def level_up(self):
        self.level += 1
        self.update_scoreboard()