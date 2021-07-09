# physics 2 grade calculator as of 11-16-2017
"""
# = example grade numbers

E1 = float(input("Enter exam 1 grade: "))  #62
E2 = float(input("Enter exam 2 grade: "))  #40
E3 = float(input("Enter exam 3 grade: "))  #46
H = float(input("Average homework grade: "))  #93.305
L = float(input("Enter average lab grade: ")) #87.7
F = float(input("Enter final exam grade: ")) 

FG1 = 0.17*(E1 + E2 + E3) + 0.12*H + 0.14*L + 0.23*F

print("Your final grade in Physics 2 is: %0.2f"%FG1)
"""


"""
# computer organization
Q1 = float(input("Enter quiz 1 grade: "))  #64
Q2 = float(input("Enter quiz 2 grade: ")) #50
Q3 = float(input("Enter quiz 3 grade: ")) #?
Q4 = float(input("Enter quiz 4 grade: ")) #?
Q5 = float(input("Enter quiz 5 grade: ")) #?

T1 = float(input("Enter test 1 grade: ")) #36
T2 = float(input("Enter test 2 grade: ")) #?
T3 = float(input("Enter test 3 grade: ")) #?

LDP = float(input("Enter logic design projects grade: ")) #?
AP = float(input("Enter assembly progam grade: ")) #?

FE = float(input("Enter final exam grade: ")) #?

Total = 0.1*(Q1+Q2+Q3+Q4+Q5) + 0.3*(T1+T2+T3) + 0.2*(LDP) + 0.2*(AP) + 0.2*(FE)
print("Your final grade in Computer Organizaion is: %0.2f"%(Total/2))
"""

#Data Structures grader \ DAA grader
#current100 = 700
hw1 = float(input("HW1 grade: ")) #47
hw2 = float(input("HW2 grade: ")) #0
hw3 = float(input("HW3 grade: ")) #30
hw4 = float(input("HW4 grade: ")) # 24
hw5 = float(input("HW5 grade: ")) #20
hw6 = float(input("HW6 grade: ")) #35
hw7 = float(input("HW7 grade: ")) #35
hw8 = float(input("HW8 grade: ")) #36
hw9 = float(input("HW9 grade: ")) #40
hw10 = float(input("possible HW10 grade: ")) #?37
hwTot = (hw1+hw2+hw3+hw4+hw5+hw6+hw7 + hw8 + hw9 + hw10)

q1 = float(input("Quiz1 grade: ")) #3
q2 = float(input("Quiz2 grade: "))#3
q3 = float(input("Quiz3 grade: "))#6
q4 = float(input("Quiz4 grade: "))#2
#q3 = float(input("possible Quiz3 grade: ")) # ?/24
qTot = (q1+q2+q3+q4)

midterm1 = float(input("Midterm1 grade: ")) # 69
midterm2 = float(input("possible Midterm2 grade: ")) # 51

final = float(input("possible FinalExam grade: ")) # ?/100
TotCount = hwTot + qTot + midterm1 + midterm2 + final
print(TotCount)
total = 0.4*hwTot + 0.15*midterm1 + 0.15*midterm2 + 0.1*qTot + 0.2*final
print("Final grade in Data Structures is: %0.2f"%(TotCount/7.71)) #700 points
print("Also: %0.2f"%total)


"""
# DCD1 Grader
hw1 = float(input("HW1 grade: "))
hw2 = float(input("HW2 grade: "))
hw3 = float(input("HW3 grade: "))
hw4 = float(input("HW4 grade: "))
hw5 = float(input("HW5 grade: "))
hw6 = float(input("HW6 grade: "))
hw7 = float(input("HW7 grade: "))
hw8 = float(input("HW8 grade: "))
hw9 = float(input("possible HW9 grade: "))
#hw10 = float(input("possible HW10 grade: "))
hwTotal = hw1+hw2+hw3+hw4+hw5+hw6+hw7+hw8+hw9
hwAvg = (hwTotal)/9

mp1 = float(input("mp1 grade: ")) 
mp2 = float(input("mp2 grade: "))
mp3 = float(input("mp3 grade: "))
mp4 = float(input("mp4 grade: "))
mp5 = float(input("mp5 grade: "))
mp6 = float(input("mp6 grade: "))
mp7 = float(input("mp7 grade: "))
mp8 = float(input("mp8 grade: "))
#mp9 = float(input("possible mp9 grade: "))
mpTotal = mp1+mp2+mp3+mp4+mp5+mp6+mp7+mp8
mpAvg = (mpTotal)/8 

q1 = float(input("Quiz1 grade: "))
q2 = float(input("Quiz2 grade: "))
q3 = float(input("Quiz3 grade: "))
q4 = float(input("Quiz4 grade: "))
q5 = float(input("Quiz5 grade: "))
q6 = float(input("Quiz6 grade: "))
q7 = float(input("Quiz7 grade: "))
q8 = float(input("Quiz8 grade: "))
#q9 = float(input("possible Quiz9 grade: "))
qTotal = q1+q2+q3+q4+q5+q6+q7+q8
qAvg = (qTotal)/8

midterm1 = float(input("Midterm1 grade: "))
midterm2 = float(input("Midterm2 grade: "))
midterm3 = float(input("Midterm3 grade: "))
midterm4 = float(input("Midterm4 grade: "))
midtermTotal = midterm1+midterm2+midterm3+midterm4
midtermAvg = (midtermTotal)/4

finalP = float(input("Possible FinalP grade: "))

total = hwTotal + midtermTotal + qTotal + finalP + hwTotal
print(total)
FG = 0.1*hwAvg + 0.225*mpAvg + 0.35*midtermAvg + 0.125*qAvg + 0.2*finalP
print("Final grade in DCD1 is: %0.2f"%FG)
"""
