
def swap(a,x,y):
    t1 = a[x]
    t2 = a[y]
    a[x] = t2
    a[y] = t1
    return a
    
def main():
    Lst = str(input("Enter a string of binary numbers: "))
    L = []
    for n in range(len(Lst)):
        L.append(int(Lst[n]))
    print("Number of digits: ",len(L))

    print(L)
    
    mid = int(round(len(L)/2,0))

    MidLeft = []
    MidRight = []
    for l in range(0, mid):
        MidLeft.append(L[l])
    for g in range(mid, len(L)):
        MidRight.append(L[g])

    #print(MidLeft, MidRight)
    counter = 0
    while 1 in MidLeft:
        for i in range(len(L)):
            #print("i =", i)
            a1 = L[i]
            #print("a1 =", a1)
            if i < len(L)-1 :
                a2 = L[i+1]
                #print("a2 =", a2)
                if a1 > a2:
                    L = swap(L,i,i+1)
                    counter += 1
                    print(L)
                    
            else:
                a1 = L[i-i]
                a2 = L[i+1-i]
                
            #print(L)
            i += 1
        #print("-------------")
        MidLeft = []
        MidRight = []
        for l in range(0, mid):
            MidLeft.append(L[l])
        for g in range(mid, len(L)):
            MidRight.append(L[g])

        #print(MidLeft, MidRight)
    print("Sorted binary string in "+str(counter)+" moves for no reason is: \n",L)
        
main()

       
    
