

#1 use for loop to print odd numbers form 1 to 99
"""
for i in range(1,100,2):
    print(i)
"""
#2 use for loop to print the multiples of 3 from 300 down to 3
"""
for i in range(300,2 ,-3):
    print(i)
"""

#3 use for loop to print the first power of 2 starting at 2
"""
prod = 2
print(prod)
for i in range(9):
    prod *= 2
    print(prod)
"""

#4 write program that asks for two numbers, a and b.
#The program should print out the sum of the integers in range a to b (inclusive)
#assume b is always bigger than a
"""
a = int(input("enter the value for a:  "))
b = int(input("enter the value for b:  "))
total = 0
for i in range(a,b+1):
    total += i

print("the sum is", total)
"""

#5 write a program that reads an integer value and prints the
#sum of all even integers
#between 2 and the input value, inclusive.
#assume the input is always higher than 2.
"""  
limit = int(input("enter the limit:  "))
total = 0


for i in range(2,limit + 1,2):
    total +=i
print("total is",total)
"""  
    


