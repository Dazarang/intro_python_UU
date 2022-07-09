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

# Function to make rectangles at x,y with spec width, height and color
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
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()
    
# Function that calls rectangle and makes three with colors 
def tricolor(x, y, h):
    """Function that loops different colors and calls the rectangle function

    Args:
        x (paramter): x loc
        y (parameter): y loc
        h (parameter): height of rectangle
    """
    colors = ["blue", "white", "red"]
    w = h/2
    for i in range(3):
        rectangle(x + w*i, y, w, h, colors[i])
    
# Function that makes a star/pentagram at x, y with spec sides
def pentagram(x, y, side=200):
    """Function that calls on makeTurtle, to make a turtle, that loops and draws a pentagram

    Args:
        x (parameter): x location
        y (parameter): y location
        side (parameter, optional): Length of pentagram side. Defaults to 200.
    """
    t = makeTurtle(x, y)  
    t.setheading(270 - 36/2)
    t.fillcolor("green")
    t.begin_fill()
    for i in range(5):
        t.forward(side)
        t.left(180-36)
    t.end_fill()
    
# Function to make multiple stars in a row
def makeStars(x, y, numbStars, side):
    """Function that loops pentagram function to make given number of stars

    Args:
        x (parameter): x location
        y (parameter): y location
        numbStars (paramter): Number of stars wanted
        side (parameter): Length of pentagram star
    """
    
    for i in range(numbStars):
        pentagram(x, y, side)
        x += side

    
########## 
# Calling on functions with different inputs
xCor = -150
yCor = -150
height = 200
starSide = height/2
tricolor(xCor, yCor, height)
"""
Some math so the stars align and scale with flag: 
Since the right edge of the first star (to the left) should aline with the first vertical line in flag -> 
flags xCor - stars side/2 (since it starts in middle), will let them aline. 
The vertical line of the star from top to bottom is cos(18)[~0,95]*side. The upperstars and lower stars will be height/4 pixels from flag
The lower stars is easy, the flag starts in bottom left, while the upper part will be yCor + height (flag) + heigth from flag + stars vertical length (starts at top)
The flags width = 3height/2, the width fits 3 stars --> starside height/2
"""
makeStars(xCor-starSide/2, yCor+height + height/4 + 0.95*starSide, 5, starSide)
makeStars(xCor-starSide/2, yCor-height/4, 5, starSide)

turtle.done()