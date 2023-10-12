import math
pi = math.pi
def circle(radius):
     return pi * radius**2
 
def cube(side):
     return side**3
 
def cylinder(radius, height):
     return 2*pi*radius + 2*pi*height
 
def sphere(radius):
     return 4*pi*(radius**2)
 
value=int(input())
print("Area of circle:",circle(value))
print("Area of cube:",cube(value))
print("Surface area of cylinder:",cylinder(value))
print("Surface area of sphere:",sphere(value))
