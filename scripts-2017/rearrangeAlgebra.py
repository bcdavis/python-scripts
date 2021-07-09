"""
Ben Davis
8-22-2017
attempt to simplify an equation with algebra in python...
"""




def IfQuantity(charList):   # charList = original equation
    print("\nEntered quantity function --------- ")
    quant = ""
    quantList = []
    for element in range(len(charList)):
        print(charList[element])
        if ord(charList[element]) == ord('('):
            print("begin quantity")
            while (ord(charList[element]) != ord('(')):   # ---- makes sure another quantity isn't inside current quantity
                quant += charList[element]
                print(quant)
                if (ord(charList[element]) == ord(')')):  #ends the quantity
                    print("end quantity")
                    quantList.append(quant)
                    break
                else: 
                    element = element+1
    print(quant)
    return quant
    
        
        

varList = ['a','b','c','x','y','z','0']
operations = ['*', '/', '+', '-', '^','=','(',')']
characterList = []

equation = input("Enter an equation (use ^ for exponentiaion, / for division, * for multiply, - for minus, + addition, = equals):\n")
for i in range(len(equation)):
    characterList.append(equation[i])

for j in range(len(characterList)):
    if ord(characterList[j]) == ord(operations[0]):
        print(characterList[j] + " : multiplication")
    elif ord(characterList[j]) == ord(operations[1]):
        print(characterList[j] + " : division")
    elif ord(characterList[j]) == ord(operations[2]):
        print(characterList[j] + " : addition")
    elif ord(characterList[j]) == ord(operations[3]):
        print(characterList[j] + " : subtraction")
    elif ord(characterList[j]) == ord(operations[4]):
        print(characterList[j] + " : exponentiation")
    elif ord(characterList[j]) == ord(operations[5]):
        print(characterList[j] + " : equals")
    else:
        print(characterList[j])

quantities = IfQuantity(equation)
print(quantities)


    
