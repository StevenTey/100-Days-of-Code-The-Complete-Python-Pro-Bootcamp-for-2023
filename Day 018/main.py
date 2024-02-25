from turtle import Turtle, Screen
import random
import turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("lime green")
turtle.colormode(255)
# Draw A Square with 100 X 100
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Draw a Dashed Line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# Draw different shapes
# for i in range(3, 11):
#     angle = 360 / i
#     for _ in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# colors = ["red", "blue", "green", "yellow", "purple", "orange"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(5)
timmy_the_turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0 ,255)
    return (r,g,b)

# # Draw a random walk
for i in range(30):
    # color = random.choice(colors)
    timmy_the_turtle.pencolor(random_color())
    # direction = random.randint(0, 360)
    direction = 360/30
    timmy_the_turtle.left(direction)
    # timmy_the_turtle.forward(30)
    timmy_the_turtle.circle(100)



screen = Screen()
screen.exitonclick()
