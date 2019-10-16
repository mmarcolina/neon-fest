from turtle import Turtle, Screen


colors = ["red", "purple", "blue", "green", "orange", "yellow"]     #The Various Colors Available to Turtle
pen = Turtle()
pen.speed("fastest")                                                #The Speed that Turtle Moves
screen = Screen()
screen.bgcolor("black")                                             #The Background Color of the Turtle Window

for x in range(360):                                                #The Number of Times that Turtle Moves
    pen.pencolor(colors[x%6])  
    pen.width(x/100 + 1)                                            #Determines the Width of Turtle, Increases Every Run
    pen.forward(x)                                                  #The Length that Turtle Moves, Increases Every Run
    pen.left(59)                                                    #The Angle that Turtle Turns
    for j in range(4):                                              #The Number of Times that Turtle Moves
        pen.forward(5)                                              #The Length that Turtle Moves
        pen.right(90)                                               #The Angle that Turtle Turns

screen.exitonclick()    
