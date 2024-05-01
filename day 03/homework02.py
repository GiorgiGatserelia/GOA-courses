from turtle import*

speed(1000000)
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

#house2
#square2
penup()
goto(-250,0)
pendown()

left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of the square2

#draw door2

forward(70)
color("green")
begin_fill()
left(90)
forward(120)
right(90)
forward(61)
right(90)
forward(120)
end_fill()
#end of the door2
color("orange")

left(90)
forward(70)
left(90)
forward(200)

#draw a roof2

color("red")
begin_fill()
left(30)
forward(200)
left(120)
forward(200)
end_fill()

#end of the roof2

penup()
goto(-98,75)
pendown()

#window01

left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
#window02

penup()
goto(-238,75)
pendown()

forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
#end of the house 2

penup()
goto(-500,0)
pendown()

#house 3
color("green")
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square3


#draw door3

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

#end of the door 3

color("green")
left(90)
forward(70)
left(90)
forward(200)

#draw roof3

color("orange")
begin_fill()
left(30)
forward(200)
left(120)
forward(200)
end_fill()

#end of the roof3

penup()
goto(-485,75)
pendown()

#drow window 03

left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)

#sun

penup()
goto(400,300)
pendown()
begin_fill()
color("yellow")
circle(30)
end_fill()














exitonclick()