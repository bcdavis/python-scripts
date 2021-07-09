#-----------------------------------------------------------------------------------
# File --------- letter_frequencies.py
# Programmer --- Bryan Crawley
# Course ------- CS 1213
# Project ------ Sample program
#
# This program computes and displays the frequencies of the letters of the English
# alphabet in a selected text file.
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# letterCounts
#
# This function computes and returns a list of counts for the individual letters of
# the English alphabet in a given text file. The file is assumed already open.
#-----------------------------------------------------------------------------------

def letterCounts(inputFile):
    
    counters = [0]*26
    
    for line in inputFile:
        line = line.lower()
        for letter in line:
            if letter.isalpha():
                index = ord(letter) - ord("a")
                counters[index] = counters[index] + 1
        
    return counters

#-----------------------------------------------------------------------------------
# letterFrequencies
#
# This function computes a list of frequencies for the letters of the alphabet
# based upon a list of counts for the letters.
#-----------------------------------------------------------------------------------

def letterFrequencies(counters):
    
    frequencies = [0]*len(counters)
    
    sum = 0
    for n in counters:
        sum = sum + n
        
    for index in range(len(counters)):
        frequencies[index] = counters[index] / sum
        
    return frequencies

#-----------------------------------------------------------------------------------
# Main program
#-----------------------------------------------------------------------------------

def main():
    fileName = input("Select file ---- ")
    
    inputFile = open(fileName, "r")
    counters = letterCounts(inputFile)
    inputFile.close()
    
    freq = letterFrequencies(counters)
    
    for i in range(26):
        print(chr(ord('a')+i) + ": %6.4f"%freq[i])
    
    return

#-----------------------------------------------------------------------------------
# Execution begins here.
#-----------------------------------------------------------------------------------

main()
