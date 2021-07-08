from turtle import *
bgcolor("black")
color("cyan")
speed(0)

def draw_square():
    for side in range(4):
        forward(100)
        right(90)
        for side in range(4):
            forward(50)
            right(90)

penup()
back(20)
pendown()

for square in range(80):
    draw_square()
    forward(5)
    left(5)

hideturtle()
