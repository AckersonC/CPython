import turtle
nbrsides = int(input ("How many sides does your shape have? "))
for steps in range(nbrsides) :
    turtle.forward (100)
    turtle.right(360/nbrsides)


