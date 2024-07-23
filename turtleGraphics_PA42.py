import turtle

print("nevada3921")

def square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

def circle():
    turtle.circle(90)

def triangle():
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)


square()
turtle.penup()
turtle.forward(150)
turtle.pendown()

circle()
turtle.penup()
turtle.forward(100)
turtle.pendown()

triangle()
