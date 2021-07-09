


def main():
    length - int(input("Enter th elength of the array: "))
    k = []
    count = 0
    while count < length:
        userInput = int(input("Enter a number: "))
        k.append(userInput)
        count = count + 1

    k.pop()

    print(k)

main()

def Sort(List):
    sortedList = []
    for i in range(len(List)):
        if i == len(List):
            break
        elif List[i] < List[i+1]:
            Swap(List[i], List[i+1], sortdList)
            


def Swap(a,b, slist):
    print(a, b)
    c = a
    a = b
    b = c
    print(a, b)
    slist.append(a)
    slist.append(b)
    return
    
