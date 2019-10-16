import turtle

turtle.bgcolor("black")                 #The Background Color of the Turtle Window


for i in range(8):                      #The Number of Times that Turtle Moves
    turtle.color("red", "white")        #The Color of the Trail that Turtle Leaves Behind
    turtle.forward(100)                 #The Length that Turtle Moves
    turtle.right(45)                    #The Angle that Turtle Turns
    turtle.color("green", "yellow")     #The Color of the Trail that Turtle Leaves Behind, The Fill Color
    turtle.begin_fill()
    turtle.circle(50)                   #The Size of the Circle that Turtle makes
    turtle.end_fill()

turtle.mainloop()
