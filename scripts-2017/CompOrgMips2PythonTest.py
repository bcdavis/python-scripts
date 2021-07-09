
userInput = input("Enter some sentences: ")
sentences = userInput.split(".")
words = userInput.split(" ")
#print(words)
#print(sentences)
ups = 0
lows = 0
puncts = 0
spaces = 0
charCount = 0
for i in range(len(userInput)):
    #ascii caps: 65-90
    #ascii lowers: 97-122
    if((ord(userInput[i]) >= 65) and (ord(userInput[i]) <= 90)):
        ups += 1
    elif((ord(userInput[i]) >= 97) and (ord(userInput[i]) <= 122)):
        lows += 1
    elif((ord(userInput[i]) >= 33) and (ord(userInput[i]) <= 46)):
        puncts += 1
    elif((ord(userInput[i]) == 63) or (ord(userInput[i]) == 58) or (ord(userInput[i]) == 59)):
        puncts += 1
    elif(ord(userInput[i]) == ord(' ')):
        spaces += 1
    charCount += 1
        

array = [userInput, charCount, len(words), len(sentences), ups, lows, puncts, spaces]
wrdArray = ["User Input: ", "Characters: ", "Words: ", "Sentences: ", "Uppercase letters: ", "Lowercase letters: ", "Punctuation marks: ", "Spaces: "]
for n in range(len(array)):
    print(wrdArray[n] + str(array[n]))
