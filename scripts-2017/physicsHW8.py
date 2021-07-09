
import math
def Problem8(i1, i2, a, b, l):
    u = 1.25664*10**-6
    answer = u*i1*i2*l/(2*math.pi)*(1/(a+b)-1/a)
    return answer

def main():
    downAmp = float(input("Enter the current in the long wire (if arrow points down, make negative): "))
    rectAmp = float(input("Enter the current of the rectangle box: "))
    wDistToR = float(input("Enter (in meters) the distance between the wire and the rectangle: "))
    rDistToR = float(input("Enter (in meters) the width of the rectangle: "))
    lengthRect = float(input("Enter (in meters) the length of the rectangle: "))
    
    ans = Problem8(downAmp,rectAmp,wDistToR,rDistToR,lengthRect)
    print("\nAnswer: ", ans)
main()
