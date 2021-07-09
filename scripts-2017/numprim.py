
total = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                total.append(str(i)+str(j)+str(k)+str(l))

#N = int(input("Positive integer --- "))
count = 0
primesList = []
for N in range(len(total)):
    if N > 1:
        prime = True
        for h in range(2,N):
            if (N % h) == 0:
                prime = False
                break           
        if prime == False:
            print(N,"is composite")
        else:
            count += 1
            primesList.append(N)
            print(N,"is prime")
    else:
        print("Of course",N,"is not prime you fool!")

print("There is/are %d prime number(s) out of %d."% (count, len(total)))

