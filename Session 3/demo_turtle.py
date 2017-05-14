from turtle import *
speed(-1)
colors = ["blue","grey", "red","orange","cyon"]
number_of_shapes = 17
color_index = 0
for i in range(6,2,-1):
     color(colors[color_index % len(colors)])
     color_index +=1
     for j in range(i):
        forward(100)
        left(360/i)     
