from turtle import Turtle, Screen

class Gradient:
    def __init__(self, start_color, end_color, steps):
        self.current_step = 0
        self.start_color = start_color
        self.current_color = start_color
        self.color_iteration = []
        self.amount_of_steps = steps
        for i in range(0, 3):
            self.color_iteration.append((end_color[i] - start_color[i])/float(steps))
    def get_next_color(self):
        self.current_step += 1
        if (self.current_step > self.amount_of_steps):
            return None
        for i in range(0, 3):
            self.current_color[i] += self.color_iteration[i]
        return [int(round(self.current_color[0])), int(round(self.current_color[1])), int(round(self.current_color[2]))]
my_gradient = Gradient([255,0,0], [0,255,0], 255)
my_second_gradient = Gradient([0,0,0], [255,255,255], 245)
class Gradients:
    def __init__(self, gradients):
        self.amount_of_gradients = len(gradients)
        self.gradients = gradients
        self.current_gradient_number = -1
        self.get_next_gradient()
    def get_next_gradient(self):
        self.current_gradient_number += 1
        if (self.current_gradient_number >= self.amount_of_gradients):
            raise Exception('The amount of gradients was smaller than the current gradient')
        self.current_gradient = Gradient(self.gradients[self.current_gradient_number]['start'], self.gradients[self.current_gradient_number]['end'], self.gradients[self.current_gradient_number]['steps'])
    def get_next_color(self):
        color = self.current_gradient.get_next_color()
        if (color == None):
            self.get_next_gradient()
            color = self.current_gradient.get_next_color()
        return color
my_colors = Gradients([{'steps':10, 'start':[0,0,0], 'end':[255,255,255]},
                       {'steps':20, 'start':[255,255,255], 'end':[0,0,255]},
                       {'steps':30, 'start':[0,0,255], 'end':[255,0,10]},
                       {'steps':40, 'start':[255,0,10], 'end':[0,255,0]},
                       {'steps':50, 'start':[0,255,0], 'end':[255,255,0]},
                       {'steps':60, 'start':[255,255,0], 'end':[255,0,255]}])
COUNT = 200                 #Number of Times Turtle Runs
ANGLE = 15                  #The Angle that Turtle Turns (per shape)
STARTING_LENGTH = 20        #The Starting Length That Turtle Moves
LENGTH_INCREMENT = 0        #Adjusts the Size of the Shape by this Amount Every Run
DISTANCE_INCREMENT = 1      #Adjusts the Distance between Shapes by this Amount Every Run
dist = 0                    #The Starting Distance between the Shapes
N = 8                       #The Number of Sides the Shape has


def draw_polygon(turtle, size):
    global dist
    angle = 360 / N
    for _ in range(N):
        turtle.forward(size)
        turtle.left(angle)
    dist += DISTANCE_INCREMENT
    turtle.forward(dist)
screen = Screen()
screen.colormode(255)
pen = Turtle()
pen.speed('fastest')        #The Speed that Turtle Moves
length = STARTING_LENGTH
for r in range(COUNT):
    color = my_colors.get_next_color()
    
    pen.fillcolor(color)
    screen.bgcolor("black")
    pen.begin_fill()
    draw_polygon(pen, length)
    pen.end_fill()
    length += LENGTH_INCREMENT
    pen.left(ANGLE)
pen.hideturtle()
screen.exitonclick()
