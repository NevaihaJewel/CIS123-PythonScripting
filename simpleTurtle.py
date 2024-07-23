import turtle

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def circle(size):
    turtle.circle(size)

def rectangle(sideA, sideB):
    for i in range(2):
        turtle.forward(sideA)
        turtle.right(90)
        turtle.forward(sideB)
        turtle.right(90)

def anyShape(sides, direction):
    angle = int(360/sides)
    size = int(900/sides)
    for i in range(sides):
        turtle.forward(size)
        if direction == "r":
            turtle.right(angle)
        else:
            turtle.left(angle)

square(100)
turtle.penup()
turtle.forward(150)
turtle.pendown()

circle(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()

rectangle(100, 50)
turtle.penup()
turtle.forward(150)
turtle.pendown()

anyShape(7,'r')
