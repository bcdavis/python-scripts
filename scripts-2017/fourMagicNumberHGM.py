numberNames = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"onehundred",200:"twohundred",300:"threehundred",400:"fourhundred",500:"fivehundred",600:"sixhundred",700:"sevenhundred",800:"eighthundred",900:"ninehundred",1000:"onethousand", 2000:"twothousand", 3000:"threethousand", 4000:"fourthousand", 5000:"fivethousand", 6000:"sixthousand", 7000:"seventhousand", 8000:"eightthousand",9000:"ninethousand", 10000: "tenthousand"}
teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"} #a list of the special two digit numbers
brokenNumber={}
def main():
    origNumber = int(input("Gimme an integer number: "))
    number = abs(origNumber)
    x = checkIfTeen(number)
    if x == 1:
        x = findNextTeenNumber(number)
        if origNumber < 0:
            x = x + 8 #8 letters in "negative"
    else:
        x = findNextNumber(number)
        if origNumber < 0:
            x = x + 8 #8 letters in "negative"
    if number == 4:
        print("4 is the magic number.")
    elif origNumber <0:
        print(str(origNumber)+" is "+str(x)+".")
        number = x
        x = findNextNumber(number)
        while x !=4:
            print(str(number)+" is "+str(x)+".")
            number = x
            x = findNextNumber(number)
        if x == 4:
            print(str(number)+" is "+str(x)+".")
            print("4 is the magic number.")
    else:
        while x !=4:
            print(str(number)+" is "+str(x)+".")
            number = x
            x = findNextNumber(number)
        if x == 4:
            print(str(number)+" is "+str(x)+".")
            print("4 is the magic number.")

def findNameCount(number, power): #handles the different places
    number = number*10**power
    return len(numberNames[number])
def findNextNumber(number): #takes a number and gives you the length of its word
    if number in numberNames:
        return(len(numberNames[number]))
    else:
        length = len(str(number))
        x=0 #this is how long the name of our number will be
        for i in range(length):
            brokenNumber[int("{0}".format(i))]=(int(str(number)[length-1-i])) #breaks down number into indiviual intergers. dictionary will look like 0:1, 1:4. etc
        for i in range(length):
            if brokenNumber[i]!=0:
                x = x + findNameCount(brokenNumber[i],i)
        return(x)
def findNextTeenNumber(number): #specifically for the hundreds and thousands that end in teen
        length = len(str(number))
        x=0 #this is how long the name of our number will be
        for i in range(length):
            brokenNumber[int("{0}".format(i))]=(int(str(number)[length-1-i])) #breaks down number into indiviual intergers. dictionary will look like 0:1, 1:4. etc
        for i in range(length-2):
            if brokenNumber[length-1-i]!=0:
                x = x + findNameCount(brokenNumber[length-1-i],length-1-i)
        strnum = str(number)
        ltd =(strnum[length-2]+strnum[length-1])
        ltd = int(ltd)
        ltd = teens[ltd]
        ltd = str(ltd)
        ltd = len(ltd)
        x = x + ltd
        return(x)
def checkIfTeen(number):
    number = str(number)
    length = len(number)-1
    ltd = (number[length-1]+number[length]) #ltd = last two digits
    if (int(ltd) in teens) and (length>1):
        return 1

main()
answer = "yes"
while answer!="no":
    answer = input("Do you want to try again? yes/no: ")
    answer = str.lower(answer)
    if (answer!="no") and (answer!="yes"):
        print("Well you didn't say no so here we go again!")
    if answer!="no":
        main()
