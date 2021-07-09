f1 = open("wordlist.txt","r")
content = f1.read()
lines = content.split("\n")
# lines is a list of all lines in the file

print(len(lines))
