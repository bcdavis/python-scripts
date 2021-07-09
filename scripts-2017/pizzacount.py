
pizacount = int(input("Enter number of pizzas: "))

while pizacount < 1:
    pizacount = int(input("Invalid pizza number: "))
    
num = int(input("Enter number of people: "))
while num < 1:
    num = int(input("Someone's got to pay for it...: "))

print("%d want %d pizza(s)."%(num, pizacount))
