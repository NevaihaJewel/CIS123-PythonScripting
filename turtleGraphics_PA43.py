import turtle

ID = str(input("What's your student ID?: "))
sizeSQ = int(input("What's the size for the square?: "))
sizeC = int(input("What's the size for the circle?: "))
side1 = int(input("What is the first side of the triangle?: "))
side2 = int(input("What is the second side of the triangle?: "))
side3 = int(input("What is the third side of the triangle?: "))


def studentId():
    turtle.write("Your student ID is " +ID)

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def circle(size):
    turtle.circle(size)

def triangle(size1, size2, size3):
    turtle.forward(size1)
    turtle.right(120)
    turtle.forward(size2)
    turtle.right(120)
    turtle.forward(size3)
    turtle.right(120)

square(sizeSQ)
turtle.penup()
turtle.forward(150)
turtle.pendown()

circle(sizeC)
turtle.penup()
turtle.forward(100)
turtle.pendown()

triangle(side1, side2, side3)

studentId()
