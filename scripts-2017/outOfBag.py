

emptyList = []
lineList= ["Therefore,", "cat", "is", "out", "of", "the", "suitcase."]



for i in range(len(lineList)):
    word = lineList[i]
    #print(word)
    if word.endswith(".") or word.endswith(","):
        neWord = word
        emptyList.append(neWord)
        
    else:
        for j in word:
        #print(j)                
            neWord = word[1:] + j + "ay"
            emptyList.append(neWord)
            #print(neWord)
            break

for k in range(len(emptyList)):
    print(emptyList[k] + " ")
    #print(emptyList[k], end = " ")


