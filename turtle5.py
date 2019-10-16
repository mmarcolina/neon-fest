import turtle
import random

turtle.bgcolor("black")                                             #The Background Color of the Turtle Window
color = ["red", "orange", "yellow", "light green", "cyan", "pink"]  #The Various Colors Available to Turtle
count = 0
turtle.penup()
turtle.setpos(-250, 0)
turtle.pendown()

while count < 5:                                                    #Counter, Determines How Many Times Turtle Runs
    for i in range(3):                                              #The Number of Times that Turtle Moves
        turtle.pencolor(random.choice(color))
        turtle.forward(100)                                         #The Length that Turtle Moves
        turtle.right(120)                                           #The Angle that Turtle Turns
        for i in range(6):                                          #The Number of Times that Turtle Moves
            turtle.pencolor(random.choice(color))
            turtle.forward(100)                                     #The Length that Turtle Moves
            turtle.right(60)                                        #The Angle that Turtle Turns
    turtle.forward(100)                                             #The Length that Turtle Moves
    count += 1            


turtle.mainloop()
