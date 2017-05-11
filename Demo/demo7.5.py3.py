from turtle import *
speed(-1)
for i in range(11,2,-1):
   begin_fill()
   for j in range(i):
       if i%2==1:
            color("blue", "red")     
            forward(100)
            left(360/i)
       if i%2==0:
            color("red", "green")
            forward(100)
            left(360/i)
       end_fill()
