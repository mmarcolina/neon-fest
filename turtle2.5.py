import turtle

turtle.color("blue")      #The Color Trail that Turtle Leaves Behind
  
def sqrfunc(size):
    for i in range(4):    #The Number of Sides on the Shape Turtle Makes
        turtle.fd(size) 
        turtle.left(90)   #The Angle that Turtle Turns
        size = size-5
  
sqrfunc(146)              #The Size of Each Side of the Shape Turtle Makes
sqrfunc(126) 
sqrfunc(106) 
sqrfunc(86) 
sqrfunc(66) 
sqrfunc(46) 
sqrfunc(26) 
