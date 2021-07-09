# interlacing strings:




word = input(str("Enter a word: "))
bisonList = ['b','i','s','o','n']
while word != "":
    wordList = list(word)
    herdWord = ""       
    for i in range(len(wordList)):
        herdWord = herdWord + wordList[i]
        if i != len(wordList)-1: # checks is i is the last letter of input word
            herdWord = herdWord + bisonList[i % 5]      
    print(herdWord)
    word = input(str("Enter a word: "))


        
        
        

