def popList(L):
    Lpopped = []
    for i in range(len(L)):
        p = L[i]
        Lpopped.append(p)
        print(p)
        
    return Lpopped
    

def main():
    
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    newList = popList(l)
    print(newList)
    print(l)
main()

