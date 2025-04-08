from turtle import *

bgcolor("black")
speed(0)
hideturtle()

for i in range(160):
    color("brown")
    circle(i)
    color("green")
    circle(i*2.8)
    right(3)
    left(6)
    forward(6)

done()  