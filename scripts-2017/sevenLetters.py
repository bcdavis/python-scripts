
tiles = []
for i in range(7):
    letter = input("Enter one letter: ").lower()
    tiles.append(letter)

f1 = open("wordlist","r")
content = f1.read()
lines = content.split("\n")
for k in range(len(lines)):
    if len(lines[k]) == 7:
        print(lines[k])
