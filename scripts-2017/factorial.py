#------------------------------------------------------
# Developer -- Bryan Crawley
# Project ---- Class demonstration
#
# This program computes the factorial of a positive
# integer.
#------------------------------------------------------

C = []
def factorial2(n,i):#--------------------------------recursive function
    #create base case to make it not infinite loop
    #q = n-i
    if q == 1:
        return 1
    else:  # optional else
        return q * factorial2(n,i+1)  # currently an infinite loop (w/o base case)
     # recursive step ^


def main():
    print("This program computes the factorial of non-negative integer N.")
    print()
    n = int(input("Enter N: "))

 #   factorial = 1

    #for count in range(1,n+1):
 #       factorial = factorial * count

    #print("Factorial of %d is %d."%(n,factorial))
    L = ['a','b','c','d','e','f','g']
    
    for i in range(len(L)):
        C.append(L[i]*factorial2(n,i))

    print(C)
main()





