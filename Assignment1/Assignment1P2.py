import turtle
###### Functions ######
# Function to move turtle to x and y 
def jump(t, x, y):
    """Moves turtle, t, to given location

    Args:
        t (parameter): Turtle made from module "turtle" and class "Turtle"
        x (parameter): location on the x axis
        y (parameter): location on the y axis
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

# Function to make turtle at x and y    
def makeTurtle(x, y):
    """Function that creats a turtle

    Args:
        x (parameter): x axis location
        y (parameter): y axis location

    Returns:
        t (variable): Return variable t
    """
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    jump(t, x, y)
    return t

def rectangle(x, y, width, height, color):
    """Calls on makeTurtle function to make a turtle that draws a rectangle

    Args:
        x (parameter): x axis location
        y (parameter): y axis location
        width (parameter): width of the rectanglr
        height (parameter): height of rectangle
        color (parameter): Perimeter color and fill color of rectangle 
    """
    t = makeTurtle(x, y)
    t.color(color)
    t.fillcolor()
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def pentagram(x, y, side):
    """Function that calls on makeTurtle, to make a turtle, that loops and draws a pentagram

    Args:
        x (parameter): x location
        y (parameter): y location
        side (parameter, optional): Length of pentagram side. Defaults to 200.
    """
    t = makeTurtle(x, y)  
    t.setheading(270 - 36/2)
    t.color("yellow")
    t.fillcolor()
    t.begin_fill()
    for i in range(5):
        t.forward(side)
        t.left(180-36)
    t.end_fill()
    
def vietnameseFlag(x, y, height):
    """Function that draws the vietnames flag with proportion 3:2. Calls on rectangle and pentagram function

    Args:
        x (parameter): x location
        y (parameter): y location
        height (parameter): height of the flag
    """
    width = height*3/2
    rectangle(x, y, width, height, "red")
    pentagram(x+width/2, y + height/2 + width/5, 2*0.95*width/5)
    """
    Side of star (wikpedia) 2*width*cos(18)/5. Want it centered therefore x + width / 2. 
    From top of the star to the point in middle width / 5, therefore height / 2 take us to the middle and + width / 5 for start poisiton
    """

########### 
vietnameseFlag(-200, -100, 300)

turtle.done()
    