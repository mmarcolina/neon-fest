from turtle import Turtle, Screen


colors = ["red", "purple", "blue", "green", "orange", "yellow"] 
pen = Turtle()
pen.speed("fastest")
screen = Screen()
screen.bgcolor("black") 

for x in range(360): 
    pen.pencolor(colors[x%6]) 
    pen.width(x/100 + 1) 
    pen.forward(x) 
    pen.left(59)
    for j in range(4):
        pen.forward(5)
        pen.right(90) 

screen.exitonclick()    