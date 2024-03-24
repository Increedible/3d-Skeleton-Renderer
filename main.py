# Import the Turtle module for graphic drawings and math module for mathematical calculations.
from turtle import *
from math import *

# Right now set to truncated Icosahedron.

# Define the coordinates of the vertices of the object to be drawn.
xvertices = [0,1,4.854101966249685,0,1,-4.854101966249685,0,-1,4.854101966249685,0,-1,-4.854101966249685,1,3.618033988749895,3.23606797749979,1,3.618033988749895,-3.23606797749979,-1,3.618033988749895,3.23606797749979,-1,3.618033988749895,-3.23606797749979,1,-3.618033988749895,3.23606797749979,1,-3.618033988749895,-3.23606797749979,-1,-3.618033988749895,3.23606797749979,-1,-3.618033988749895,-3.23606797749979,1.618033988749895,2,4.23606797749979,1.618033988749895,2,-4.23606797749979,-1.618033988749895,2,4.23606797749979,-1.618033988749895,2,-4.23606797749979,1.618033988749895,-2,4.23606797749979,1.618033988749895,-2,-4.23606797749979,-1.618033988749895,-2,4.23606797749979,-1.618033988749895,-2,-4.23606797749979]
yvertices = [1,4.854101966249685,0,1,-4.854101966249685,0,-1,4.854101966249685,0,-1,-4.854101966249685,0,3.618033988749895,3.23606797749979,1,3.618033988749895,-3.23606797749979,1,3.618033988749895,3.23606797749979,-1,3.618033988749895,-3.23606797749979,-1,-3.618033988749895,3.23606797749979,1,-3.618033988749895,-3.23606797749979,1,-3.618033988749895,3.23606797749979,-1,-3.618033988749895,-3.23606797749979,-1,2,4.23606797749979,1.618033988749895,2,-4.23606797749979,1.618033988749895,2,4.23606797749979,-1.618033988749895,2,-4.23606797749979,-1.618033988749895,-2,4.23606797749979,1.618033988749895,-2,-4.23606797749979,1.618033988749895,-2,4.23606797749979,-1.618033988749895,-2,-4.23606797749979,-1.618033988749895]
zvertices = [4.854101966249685,0,1,-4.854101966249685,0,1,4.854101966249685,0,-1,-4.854101966249685,0,-1,3.23606797749979,1,3.618033988749895,-3.23606797749979,1,3.618033988749895,3.23606797749979,-1,3.618033988749895,-3.23606797749979,-1,3.618033988749895,3.23606797749979,1,-3.618033988749895,-3.23606797749979,1,-3.618033988749895,3.23606797749979,-1,-3.618033988749895,-3.23606797749979,-1,-3.618033988749895,4.23606797749979,1.618033988749895,2,-4.23606797749979,1.618033988749895,2,4.23606797749979,-1.618033988749895,2,-4.23606797749979,-1.618033988749895,2,4.23606797749979,1.618033988749895,-2,-4.23606797749979,1.618033988749895,-2,4.23606797749979,-1.618033988749895,-2,-4.23606797749979,-1.618033988749895,-2]

# Define which vertices need to be connected to form the edges of the object.
edges = [(1,7),(1,37),(1,43),(2,8),(2,38),(2,44),(3,9),(3,39),(3,45),(4,10),(4,40),(4,46),(5,11),(5,41),(5,47),(6,12),(6,42),(6,48),(7,49),(7,55),(8,50),(8,56),(9,51),(9,57),(10,52),(10,58),(11,53),(11,59),(12,54),(12,60),(13,19),(13,37),(13,38),(14,20),(14,38),(14,39),(15,21),(15,37),(15,39),(16,22),(16,40),(16,44),(17,23),(17,41),(17,45),(18,24),(18,42),(18,43),(19,43),(19,50),(20,44),(20,51),(21,45),(21,49),(22,46),(22,56),(23,47),(23,57),(24,48),(24,55),(25,31),(25,41),(25,49),(26,32),(26,42),(26,50),(27,33),(27,40),(27,51),(28,34),(28,47),(28,52),(29,35),(29,48),(29,53),(30,36),(30,46),(30,54),(31,53),(31,55),(32,54),(32,56),(33,52),(33,57),(34,58),(34,59),(35,59),(35,60),(36,58),(36,60)]

# Set the focal length for the perspective view.
sizeincrease = 30

# Stel de focale lengte in voor de perspectiefweergave.
focallength = 340

# Starting value for the rotation angle.
angle = -2 * pi

# An infinite loop to keep the animation running continuously.
while True:
    # Increase the rotation angle slightly with each iteration.
    angle += 0.01
    # Reset the angle if it exceeds 2 pi.
    if angle >= 0:
        angle = -2 * pi

    # Reset the Turtle environment for each new drawing.
    reset()
    # Set the animation speed to maximum.
    tracer(0)
    # Hide the turtle cursor.
    hideturtle()

    # Draw each edge of the object.
    for i in range(len(edges)):
        # Pen up to move without drawing.
        penup()

        # Calculate the transformed x and y coordinates of the first vertex of the current edge.
        tx1 = ((cos(angle) * xvertices[edges[i][0] - 1] + sin(angle) * zvertices[edges[i][0] - 1]) * sizeincrease * focallength) / ((-sin(angle) * xvertices[edges[i][0] - 1] + cos(angle) * zvertices[edges[i][0] - 1]) * sizeincrease + focallength)
        ty1 = ((yvertices[edges[i][0] - 1]) * sizeincrease * focallength) / ((-sin(angle) * xvertices[edges[i][0] - 1] + cos(angle) * zvertices[edges[i][0] - 1]) * sizeincrease + focallength)

        # Calculate the transformed x and y coordinates of the second vertex of the current edge.
        tx2 = ((cos(angle) * xvertices[edges[i][1] - 1] + sin(angle) * zvertices[edges[i][1] - 1]) * sizeincrease * focallength) / ((-sin(angle) * xvertices[edges[i][1] - 1] + cos(angle) * zvertices[edges[i][1] - 1]) * sizeincrease + focallength)
        ty2 = ((yvertices[edges[i][1] - 1]) * sizeincrease * focallength) / ((-sin(angle) * xvertices[edges[i][1] - 1] + cos(angle) * zvertices[edges[i][1] - 1]) * sizeincrease + focallength)

        # Go to the first vertex.
        goto(tx1, ty1)
        # Pen down to start drawing.
        pendown()
        # Draw a line to the second vertex.
        goto(tx2, ty2)
        # Update the screen with the new drawing.
        update()
