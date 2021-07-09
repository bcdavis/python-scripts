import math
def sin(angle):
    return math.sin(angle)
def cos(angle):
    return math.cos(angle)
'''q1 = 2*10**-9
q2 = 1*10**-9
q3 = 6*10**-9
q4 = 7*10**-9
r2 = 1.414
r3 = 4.123
r4 = 3.16
o1 = math.radians(45)
o2 = math.radians(75.96)
o3 = math.radians(18.43)
k = 8.98755*10**9'''

q1 = float(input("absolute value of q, in nC: "))*10**-9
q2 = float(input("absolute value of q1, in nC: "))*10**-9
q3 = float(input("absolute value of q2, in nC: "))*10**-9
q4 = float(input("absolute value of q3, in nC: "))*10**-9
r2 = float(input("distance from q to q1, in m: "))
r3 = float(input("distance from q to q2, in m: "))
r4 = float(input("distance from q to q3, in m: "))
o1 = math.radians(float(input("theta1, in degrees: ")))
o2 = math.radians(float(input("theta2, in degrees: ")))
o3 = math.radians(float(input("theta3, in degrees: ")))
k = 8.98755*10**9
def findSign(thing):
    while (thing != "+") and (thing !="-"):
        thing = input("I'm sorry, you must choose + or - : ")
    if thing == "+":
        return 1
    elif thing == "-":
        return -1
x1 = input("Is the x component of q1 + or - : ")
x1 = findSign(x1)
y1 = input("Is the y component of q1 + or - : ")
y1 = findSign(y1)
x2 = input("Is the x component of q2 + or - : ")
x2 = findSign(x2)
y2 = input("Is the y component of q2 + or - : ")
y2 = findSign(y2)
x3 = input("Is the x component of q3 + or - : ")
x3 = findSign(x3)
y3 = input("Is the y component of q3 + or - : ")
y3 = findSign(y3)

xcomp = x1*k*q1*q2*cos(o1)/r2/r2 + x2*k*q1*q3*cos(o2)/r3/r3 + x3*k*q1*q4*cos(o3)/r4/r4
ycomp = y1*k*q1*q2*sin(o1)/r2/r2 + y2*k*q1*q3*sin(o2)/r3/r3 + y3*k*q1*q4*sin(o3)/r4/r4
print(str(xcomp)+"i, "+str(ycomp)+"j")
xcomp2 = xcomp*xcomp
ycomp2 = ycomp*ycomp
final = math.sqrt(xcomp2+ycomp2)
print("This is your final vector:", final)
print("This is your reference angle: "+str(math.degrees(math.atan(ycomp/xcomp))))
