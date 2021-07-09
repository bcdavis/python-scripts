"""
Ben Davis
CS 1213
assignment 61
4-20-2016
"""
print("This program computes area and volume of geometric solids.")
PI = 3.14159

def sphereArea(radius):
    return 4*PI*radius*radius

def trapArea(base1, base2, height):
    a = ((base1 + base2)/2)*height
    return a

def trapVolume(area, length):
    v = area*length
    return v
    

def main():
    radius = float(input("Enter the radius: "))
    print("The surface area is",round(sphereArea(radius),2))
main()
