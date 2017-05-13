from turtle import *
speed(-1)
for i in range(7,2,-1):
   begin_fill()
   for j in range(i):
       if i%6==1:
            color("grey")     
            forward(100)
            left(360/i)
       if i%5==1:
            color("yellow")
            forward(100)
            left(360/i)
       if i%3==2:
            color("brown")
            forward(100)
            left(360/i)
       if i%3==1:
            color("blue")
            forward(100)
            left(360/i)
     
       end_fill()
