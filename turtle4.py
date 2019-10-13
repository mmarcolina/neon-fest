import turtle
import random

turtle.bgcolor("black")
color = ["red", "orange", "yellow", "light green", "cyan", "pink"]

for i in range(4):
    turtle.pencolor(random.choice(color))
    turtle.forward(100)
    turtle.right(50)
    for i in range(3):
        turtle.pencolor(random.choice(color))
        turtle.forward(100)
        turtle.right(120)
        for i in range(8):
            turtle.pencolor(random.choice(color))
            turtle.forward(100)
            turtle.right(45)

turtle.mainloop()