from turtle import Turtle, Screen
import random

def createTurtle(color, width):
    turtle = Turtle('arrow')
    turtle.speed('fastest')
    turtle.color(color)
    turtle.width(width)

    return turtle

def inScreen(screen, turtle):

    x = screen.window_width() / 2
    y = screen.window_height() / 2

    turtleX, turtleY = turtle.pos()

    return (-x < turtleX < x) and (-y < turtleY < y)

def moveTurtle():

    turtle.left(random.randrange(360))
    turtle.forward(random.randrange(200))

    if not inScreen(screen, turtle):
        turtle.undo()  # undo forward()

    screen.ontimer(moveTurtle, 50)

screen = Screen()
turtle = createTurtle("pink", 3)
moveTurtle()
screen.exitonclick()