import turtle
turtle.color("green")
for step in range (5) :
    turtle.forward (100)
    turtle.right (360/5)
    for moresteps in range (5) :
        turtle.forward (50)
        turtle.right (360/5)