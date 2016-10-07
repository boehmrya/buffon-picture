# Ryan Boehm
# BuffonPicture.py
# CS:1210:0AAA
# HW 07 - Buffon's Picture
# Drawa a picture (using the python turtle module) of the Buffon's Needle monte carlo method for the estimation of the value of π.


import math
import random
import turtle
    

# Sets the turtle object and the screen
def turtlePrep(t):
    # make the screen 14 by 14, so we can use a 12 by 12 area for the picture
    turtle.setworldcoordinates(-14, -14, 14, 14) # LLx, LLy, URx, URy  
    turtle.setup()
    wn = t.getscreen()
    wn.title("Buffon's Needle")
    t.speed(0) # fastest = 0
    t.hideturtle() # don't want to see the turtle darting all over the place      
    
    
# Draws the square border around the grid
def drawBorder(t):
    t.pensize(3)
    t.up()
    t.goto(-12, 12)
    t.down()
    for i in range(4):
        t.forward(24)
        t.right(90)
    t.up()    


# Draws the orange gridlines
def drawGrid(t):
    t.color("orange")
    t.pensize(1)
    y = -12 #accumulator for y coordinate
    t.goto(-12, y)
    for i in range(12):
        t.forward(24)
        y += 2
        t.up()
        t.goto(-12, y)
        t.down()     
    

# Single function to draw the picture.  The individual lines are drawn in the buffonNeedle() function.
def drawPic(t):
    drawBorder(t)
    drawGrid(t)
     

# Draws the lines as determined by the distance and angle in the buffonNeedle() function.
def drawLine(t, distanceToLine, needleAngle, color):
    #Get coordinates for starting line
    y = random.randrange(-10, 9, 2)
    y += (2 - distanceToLine)
    x = random.randint(-10, 10)
    
    #position the turtle
    t.up()
    t.goto(x, y)
    t.down()
    
    #draw the line
    t.color(color)
    t.left(needleAngle)
    t.forward(1)
    

# Documents the number of drops and the approximation for pi on the bottom of the screen.
def writeMessage(t, numDrops, pi):
    t.color('black')
    t.goto(0, -11.5)
    
    #set up message based on inputs 
    message = 'n = ' + str(numDrops) + '.'
    message += ' Approximation for pi = '
    message += str(pi) + '.'
    
    t.write(message, False, 'center',('Arial',16,'bold'))
    

# Buffon's Needle monte carlo method.  
# Calculates the approximation and draws a line for each drop.
def buffonNeedle(t, numDrops):
    hits = 0 #accumulator to track number of hits
    
    for i in range(numDrops):
        distanceToLine = 2 * random.random() #distance to the next line from the original drop point of the needle.
        needleAngle = random.randint(0, 180) #angle of needle.
        needleDistance = math.sin(math.radians(needleAngle)) #how far the needle stretches in terms of distance to the next line (based on the angle).
        
        #check if there is a hit
        if needleDistance >= distanceToLine:
            hits += 1
            drawLine(t, distanceToLine, needleAngle, "red")
        else:
            drawLine(t, distanceToLine, needleAngle, "blue")
        t.up()
        t.home()
        
    #if there were no hits, return a message.
    if hits == 0:
        approximation = "There weren't any hits. Please use a larger number of drops."
    else:
        approximation = numDrops / hits
        
    return approximation


def main():
    #initialize turtle and draw the picture
    t = turtle.Turtle()
    turtlePrep(t)
    drawPic(t)
    
    # Get user input using a pop-up window.
    numDrops = int(turtle.textinput("Buffon's Needle", "How many drops: "))
    pi = buffonNeedle(t, numDrops)
    writeMessage(t, numDrops, pi)
   
    
main()