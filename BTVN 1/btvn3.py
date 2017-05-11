from turtle import *
color("red")
speed(-1)

side = 50 
x = 60 
n = 4

right(x/2)

for i in range(n):

    forward(side)
    left(x)
    forward(side)
    left(180-x)
    forward(side)
    left(x)
    forward(side)
    if i < n-1:
        right(x + 180 - 360/n)
