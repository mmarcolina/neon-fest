import turtle
import random

turtle.bgcolor("black")                                             #The Background Color of the Turtle Window
color = ["red", "orange", "yellow", "light green", "cyan", "pink"]  #The Various Colors Available to Turtle

for i in range(4):                                                  #The Number of Times that Turtle Moves
    turtle.pencolor(random.choice(color))                           #Select a random color from the array of colors defined above
    turtle.forward(100)                                             #The Length that Turtle Moves
    turtle.right(50)                                                #The Angle that Turtle Turns
    for i in range(3):                                              #The Number of Times that Turtle Moves
        turtle.pencolor(random.choice(color))
        turtle.forward(100)                                         #The Length that Turtle Moves
        turtle.right(120)                                           #The Angle that Turtle Turns
        for i in range(8):                                          #The Number of Times that Turtle Moves
            turtle.pencolor(random.choice(color))
            turtle.forward(100)                                     #The Length that Turtle Moves
            turtle.right(45)                                        #The Angle that Turtle Turns

turtle.mainloop()
