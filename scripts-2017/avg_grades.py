
def semestAvg(t1, t2, t3):
    weight1 = 0.25
    weight2 = 0.5
    
    avg = ((float(t1)*weight1) + (float(t2)*weight1) + (float(t3)*weight2)) 
    return avg

def letterGrade(avg):
    if avg >= 90:
        letter = "A"
    elif avg < 90 and avg >= 80:
        letter = "B"
    elif avg < 80 and avg >= 70:
        letter = "C"
    elif avg < 70 and avg >= 60:
        letter = "D"
    elif avg < 60:
        letter = "F"      
    return letter


def main():
    file = input("Enter a filename: ")
    outfile = input("Enter an output filename: ")
    grades = open(file,"r")
    out = open(outfile,"w")

   
    stuIDs = []
    avgList = []
    letterList = []
    L = []
    line = grades.readline().strip("\n")
    while line != "":
        L = line.split(" ")

        #list of student IDs       
        stuIDs.append(L[0]) 
    
        avg = semestAvg(L[1], L[2], L[3])
        #print(str(L[1])+"," +str(L[2]) + "," + str(L[3]))

        #list of student averages
        avgList.append(avg)

        #find letter grades
        lett = letterGrade(avg)
        letterList.append(lett)
        print(str(avg) + ", " + str(lett))
        
        line = grades.readline().strip("\n")

    

    out.write("Student Average Grade\n")
    out.write("------- ------- -----\n")
    for i in range(len(stuIDs)):
        
        out.write("%7s %7.1f %5s\n"% (stuIDs[i], avgList[i], letterList[i]))


    total = 0
    for b in range(len(avgList)):
        total = total + avgList[b]
        
   #    cla
    out.close()
    grades.close()
     

main()
