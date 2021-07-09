# key# to note function

def key2note(key):
    new = key - 49; # 49 is the number of A440
    freq = 440 * 2**(new/12);
    return freq

def main():
    noteList = [];
    for i in range(40, 52):
        print(i)
        noteFreq = str(round(key2note(i), 2))
        noteList.append(noteFreq)

    print(noteList)

main()
    
    
