import turtle

turtle.setup(800, 800)


def triangle(side, n):
    if n == 0:
        for i in range(3):
            turtle.forward(side)
            turtle.left(120)
    else:
        triangle(side/2, n-1)
        turtle.forward(side/2)
        triangle(side/2, n-1)
        turtle.backward(side/2)
        turtle.left(60)
        turtle.forward(side/2)
        turtle.right(60)
        triangle(side/2, n-1)
        turtle.left(60)
        turtle.backward(side/2)
        turtle.right(60)


turtle.width(2)
triangle(500, 4)
