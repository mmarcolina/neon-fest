import turtle

turtle.color("blue") 
  
def sqrfunc(size): 
    for i in range(4): 
        turtle.fd(size) 
        turtle.left(90) 
        size = size-5
  
sqrfunc(146) 
sqrfunc(126) 
sqrfunc(106) 
sqrfunc(86) 
sqrfunc(66) 
sqrfunc(46) 
sqrfunc(26) 