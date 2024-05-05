from turtle import*




#we want to paint a hause
#square


speed(20)
width(7)
 
color("purple")
forward(200)  
left(90)

forward(200)  
left(90)

forward(200)  
left(90)

forward(200)  
left(90)
#end of square
#door

forward(70)
color("green")
begin_fill()
left(90)
forward(120)#height of thr door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)

pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("yellow")

left(30)
forward(80)
left(90)
forward(50)
left(90)
forward(80)
left(90)
forward(50)
color("purple")

penup
goto(200,200)
pendown
left(90)
color("yellow")
forward(80)
right(90)
forward(50)
right(90)
forward(80)
right(90)
forward(50)
exitonclick()
