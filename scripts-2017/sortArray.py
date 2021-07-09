
def swap(a,b):
    if a < b:
        print("a", a)
        return a
    else:
        print("b", b)
        return b

def Sort(L):
    print(len(L))
    K = []
    for i in range(len(L)):
        print(L[i])
        
        #if i == len(L)-1:
 #           K.append(L[i])
        #else:
 #           K.append(swap(L[i], L[i+1]))
    return K


def main():
    L = [1,5,3,8,0,9]
    M = Sort(L)
    print(M)
main()
