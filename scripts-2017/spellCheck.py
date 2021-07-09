#---------------------------------------------------------
# The "spellCheck" function determines whether the input
# from the inputFile is a correctly spelled word, and if not
# it will return the word and later be written to a file
# containing misspelled words
#---------------------------------------------------------
def spell_check(word, english):
    if word not in english:
        return word
    elif word in english:
        return  None

#---------------------------------------------------------
# The main function will include all of the code that will
# perform actions that are not contained within our other
# functions, and will generally call on those other fu]ctions
# to perform required tasks
#---------------------------------------------------------
def main():
    # Grabbing user input
    inputFile = input('Enter the name of the file to input from: ')
    outputFile = input('Enter the name of the file to output to: ')
    english = {}  # Will contain all available correctly spelled words.
    wrong = []  # Will contain all incorrectly spelled words.
    num = 0  # Used for line counter.

    # Opening, Closing, and adding words to spell check dictionary
    wardzfile=open('wordlist.txt', 'r')
    rfile= wardzfile.read()
    rfile= rfile.split()
    wardzfile.close()
    for line in rfile:
        (key) = line.strip()
        english[key] = ''
    # Opening, Closing, Checking words, and adding wrong ones to wrong list
    file =open(inputFile, 'r')
    rfile= file.read()
    rfile= rfile.lower().split("\n")
    file.close
    for line in rfile:
        line = line.strip()
        print(line)
        #fun = spell_check(line, english)
        #print(fun)
        #if fun is not None:
            #wrong.append(fun)
    #print(wrong)

    # Opening, Closing, and Writing to output fil
    wardzlist =[]
    out=open(outputFile, 'w')
    for line in rfile:
        wardzlist.append(line.split())
    #print(wardzlist)
    for lyne in range(len(wardzlist)):
        #print(lyne)
        for wird in range(len(wardzlist[lyne])):
            wardzlist[lyne][wird]=wardzlist[lyne][wird].strip('.,?!-;:')
            #print(wardzlist[lyne][wird])
        if wardzlist[lyne][wird] not in english:
          
            out.write('%d %s\n' % (num, wardzlist[lyne][wird]))
        num += 1
    """    
    count=0
    wardzlist=[]
    for line in rfile:
        wardzlist.append(line.split())
        #count+=1

    wardzlist=[]
    out=open(outputFile,"w")
    for i in range(len(wardzlist)):
        for j in range(len(wardzlist[i])):
            wardzlist[i][j]=wardzlist[i][j].strip('.,?!-;:')
            if wardzlist[i][j] not in english:
                #for m in wardzlist:
                    #p=wardzlist.index(m)
              
                for L in wrong:
                    #print(L)
                    out.write('%d %s\n' % (num, L))
                #out.write(wardzlist[i][j]+str(count)+'\n')
                    num += 1
                    """
    out.close()

main()
