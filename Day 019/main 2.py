from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
all_turtles = []

for tur in range(len(colors)):
    # turtle_name = colors[tur]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tur])
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.goto(-230, y)
    y += 40
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True


import random
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")                
        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    

screen.exitonclick()