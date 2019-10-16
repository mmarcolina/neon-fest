from turtle import Turtle, Screen
import random

colors = ["red", "blue", "yellow", "green"]         #The Various Colors Available to Turtle
pen = Turtle()
pen.speed("fastest")                                #The Speed that Turtle Moves
screen = Screen()

def draw_circles():
    for i in range(200):                            #The Number of Times that Turtle Moves, While Drawing the circles
        pen.color(colors[i % 4], colors[i % 4])
        pen.fillcolor()
        pen.begin_fill()
        pen.circle(i)                               #The of the Circle that Turtle Makes, Increases Every Run
        pen.end_fill()
        pen.left(90)                                #The Angle that Turtle Turns before drawing the next circle



def draw_star():
    pen.color("black")                              #The Color of the Trail that Turtle Leaves
    for j in range(12):                             #The Number of Times that Turtle Moves
        pen.forward(-90)                            #The Length that Turtle Moves
        for i in range(50):                         
            pen.forward(300)
            pen.right(165)

draw_circles()
draw_star()
screen.exitonclick()
