from turtle import *

speed(30)
#we want to paint a house

#step 1:  draw a square
width(6)
color("green")
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(61)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(50, 70)
pendown()
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)


penup()
goto(150, 70)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)


exitonclick()
