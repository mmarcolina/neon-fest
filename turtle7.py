from turtle import Turtle, Screen
import random

colors = ["red", "blue", "yellow", "green"]
pen = Turtle()
pen.speed("fastest")
screen = Screen()

def draw_circles():
    for i in range(200):
        pen.color(colors[i % 4], colors[i % 4])
        pen.fillcolor()
        pen.begin_fill()
        pen.circle(i)
        pen.end_fill()
        pen.left(90)



def draw_star():
    pen.color("black")
    for j in range(12):
        pen.forward(-90)         
        for i in range(50):
            pen.forward(300)
            pen.right(165)       

draw_circles()
draw_star()
screen.exitonclick()