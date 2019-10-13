import turtle

turtle.bgcolor("black")


for i in range(8):
    turtle.color("red", "white")
    turtle.forward(100)
    turtle.right(45)
    turtle.color("green", "yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

turtle.mainloop()
