#Create two functions that calculate and print out the area of a circle 
# and the volume of a sphere given the radius. Your main should prompt 
# the user for the radius and call both functions.

#Be sure to print the information out in a nicely formatted way. For example/
#The radius is: 54.7 cm
#The area of the circle is: 9399.9 cm squared
#The volume of the sphere is: 685568.1 cm cubed

import math
def areaCircle(radius):
    area = math.pi * pow(radius,2)
    print(f"Area of circle is {math.floor(area)} m square")

def volumeCircle(radius):
    volume = 4/3 * math.pi * pow(radius,3)
    print(f"Volume of the circle is {math.floor(volume)} m cubed")

r = float(input("Please enter the radius of circle " ))

areaCircle(r)
volumeCircle(r)