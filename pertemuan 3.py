import turtle
turtle.color('green')
turtle.forward(100)
turtle.right(45)
turtle.color('blue')
turtle.forward(50)
turtle.right(45)
turtle.color('pink')
turtle.forward(100)

import turtle
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(90)

import turtle
nbrSides = 6
for steps in range (nbrSides):
    turtle.forward(100)
    turtle.right(360/nbrSides)
    for moresteps in range(nbrSides):
        turtle.forward(50)
        turtle.right(360/nbrSides)