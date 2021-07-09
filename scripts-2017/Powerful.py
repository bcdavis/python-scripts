def pwr(X,Y):
    if (X == 0) and (Y != 0):
        return 0.0
    elif (X == 1) and (Y!=0):
        return 1
    if Y < 0:
        return 1/(X * pwr(X, abs(Y)-1))
    elif Y == 0:
        return 1
    else:
        return X * pwr(X, abs(Y)-1)
 

def main():
    """
    inp = input()
    L = inp.split(" ")
    x = float(L[0])
    y = float(L[1])
    """
    x = float(input("Enter the base: "))
    y = int(input("Enter the power: "))
    #print(str(x)+"^"+str(y),"=",round(v,6))
    print("%.6f"% pwr(x,y))

main()
