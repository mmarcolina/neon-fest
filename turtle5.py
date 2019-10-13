import turtle
import random

turtle.bgcolor("black")
color = ["red", "orange", "yellow", "light green", "cyan", "pink"]
count = 0
turtle.penup()
turtle.setpos(-250, 0)
turtle.pendown()

while count < 5:
    for i in range(3):
        turtle.pencolor(random.choice(color))
        turtle.forward(100)
        turtle.right(120)
        for i in range(6):
            turtle.pencolor(random.choice(color))
            turtle.forward(100)
            turtle.right(60)
    turtle.forward(100)        
    count += 1            


turtle.mainloop()