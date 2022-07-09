import turtle
import random

####### Functions ##########
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
def makeTurtle(x, y, visible = True):
    """Function that creats a turtle

    Args:
        x (parameter): x axis location
        y (parameter): y axis location
        visible (True, optional): Turtle visible or not. Defaults to True.

    Returns:
        t (variable): Return variable t
    """
    t = turtle.Turtle()
    t.shape("turtle")
    if not visible:
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
    t = makeTurtle(x, y, False)
    t.color(color)
    t.fillcolor()
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()
    
def moveRandom(t):
    """Function that gets data on turtle heading, then sets random heading 
    bewtween the value +- 45 and moves forward random between 0 to 25. 
    If turtle x or y cordinate is greater than 250 its outside the rectange and
    the heading i set towards origo

    Args:
        t (parameter): Turtle input
    """
    tHeading = t.heading()
    t.seth(random.uniform(tHeading-45, tHeading+45))
    t.forward(random.randint(0, 25))
    if abs(t.xcor())>= 250 or abs(t.ycor())>=250:
        t.seth(t.towards(0, 0))


def makeRandTurtle(side=500, color=""):
    """Function that calls on makeTurtle to make a turtle at random location at given parameter side

    Args:
        side (int, optional): Value for where turtle random turtle can spawn. Defaults to 500.
        color (str, optional): Color of the turtle. Defaults to "".

    Returns:
        t (variable): returns t, turtle, at a random location
        
    Set lower point of random location to a non decimal number since //2
    Set higher point of random location to -"-
    """
    locLow = -side//2
    locHigh = side//2
    t = makeTurtle(random.randint(locLow, locHigh), random.randint(locLow, locHigh), True)
    t.speed(0)
    t.color(color)
    # t.shape("turtle")
    t.seth(random.randint(0, 359))
    
    return t


###############

"""
Uses variable side for the square and is equal to 500. 

"""
side = 500

"""
Calls on the rectangle function with location -side/2, for x and y, to get lower left point so the center of square is at (0, 0), 
with width and hight as side, with infill color sky blue
Calls mmakeRandTurtle to make a turtle at a random location within given sides
"""
rectangle(-side/2, -side/2, side, side, "SkyBlue")

t = makeRandTurtle(side, "red")
u = makeRandTurtle(side, "green")

numb = 0

for i in range(250):
    moveRandom(t)
    moveRandom(u)
    
    if t.distance(u)<=50:
        t.write("Close!", font=('Calibri', 12))
        numb += 1
        
print(f'Number of times (iterations) turtles was withing 50 pixels of each other: {numb}')  
      
turtle.done()
