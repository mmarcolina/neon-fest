from turtle import Turtle, Screen


colors = ["red", "purple", "blue", "green", "orange", "yellow"]     #The Various Colors Available to Turtle
pen = Turtle()
pen.speed("fastest")                                                #The Speed that Turtle Moves
screen = Screen()
screen.bgcolor("black")                                             #The Background Color of the Turtle Window

for x in range(360):                                                #The Number of Times that Turtle Moves
    pen.pencolor(colors[x%6])                                       #Chooses a new color each time the loop starts
    pen.width(x/100 + 1)                                            #Determines the Width of Turtle, Increases Every Run
    pen.forward(x)                                                  #The Length that Turtle Moves, Increases Every Run
    pen.left(59)                                                    #The Angle that Turtle Turns
    for j in range(4):                                              #Creates a square after the main loop finishes
        pen.forward(5)
        pen.right(90)

screen.exitonclick()    
