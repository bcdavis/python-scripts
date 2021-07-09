import random

def checkRep(nums1, unums2):
    for i in range(len(nums1)):
        #print("is " +str(nums1[i])+" the same as " +str(nums1[i+1]) + "?")
        if nums1[i] not in unums2:
            unums2.append(nums1[i])
        #else:
            #print("%d already used"% nums1[i])

  
            
          
def main():       
    uniques = []
    sortedList = []
    for u in range(50):
        r = random.randint(0,25)
        sortedList.append(r)

    sortedList.sort()
    print(sortedList)
    #for k in range(len(sortedList)):
    checkRep(sortedList, uniques)
        
    print("uniques is " + str(len(uniques)) + " number(s) long.")
    avg = len(sortedList)/len(uniques)
    print(round(avg,2))
main()
