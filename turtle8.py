from turtle import Turtle, Screen
import random

def createTurtle(color, width):
    turtle = Turtle('arrow')                            #The Shape that the Turtle Icon is
    turtle.speed('fastest')                             #The Speed that Turtle Moves
    turtle.color(color)
    turtle.width(width)

    return turtle

def inScreen(screen, turtle):

    x = screen.window_width() / 2                       #The Width of the Window that Turtle Creates
    y = screen.window_height() / 2                      #The Height of the Window that Turtle Creates

    turtleX, turtleY = turtle.pos()

    return (-x < turtleX < x) and (-y < turtleY < y)

def moveTurtle():

    turtle.left(random.randrange(360))                  #The Angle that Turtle Turns, Random Between 0 and 360 Degrees
    turtle.forward(random.randrange(200))               #The Length that Turtle Moves, Random Between 0 and 200 Units

    if not inScreen(screen, turtle):
        turtle.undo()  # undo forward()

    screen.ontimer(moveTurtle, 50)                      #Move Turtle Every 50 Milliseconds

screen = Screen()
turtle = createTurtle("pink", 3)                        #Set the Color and Width of Turtle
moveTurtle()
screen.exitonclick()
