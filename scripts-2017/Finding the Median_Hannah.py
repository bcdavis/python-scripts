x = 0
while x == 0:
    numbers = input("Please provide list of numbers separated by comma, e.g. 1,2,3: ")

    numbersList =  list(map(int,numbers.split(','))) #turns the input into a list
    sortList = sorted(numbersList, key=int) #puts the list in ascending order

    half = int(len(numbersList)/2) #find the median point in an odd string
    oddMed = sortList[half] #find the number at that point
    evenMedNum = int(half-1) #to find the median of a string with an even number of elements, you avereage the two middle values.
    evenMed = (sortList[half]+sortList[evenMedNum])/2 #so that's what this does
    if evenMed%1 == 0: #if the value is not a decimal, this gets rid of the .0 at the end
        evenMed = int(evenMed)

    if len(sortList)%2 == 0: #if the string is even
        print("The median is " + str(evenMed))
    else: #if the string is odd
        print("The median is " + str(oddMed))
    userInput = input("Do you want to enter a new string? y/n: ")
    if userInput == 'n':
        x = 12345678910
