
import json

# Python program showing 
# a use of format() method
 
# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
     .format('Geeks', 'For', other ='Geeks'))
 
# using format() method with number 
print("Geeks :{0:2d}, Portal :{1:8.2f}".
      format(12, 00.546))
 
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))
 
print("Geeks: {a:5d},  Portal: {p:18.2f}".
     format(a = 453, p = 59.058))


print()
print()

# Python program to 
# show format () is 
# used in dictionary
 
tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}
 
# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab))



allCharacters = [
    {
        "id": 1,
        "name": "Colonel Mustard",
        "type": "character",
        "gameId": 0
    },
    {
        "id": 2,
        "name": "Mr. Green",
        "type": "character",
        "gameId": 0
    },
    {
        "id": 3,
        "name": "Professor Plum",
        "type": "character",
        "gameId": 0
    },
    {
        "id": 4,
        "name": "Mrs. White",
        "type": "character",
        "gameId": 0
    },
    {
        "id": 5,
        "name": "Miss Scarlet",
        "type": "character",
        "gameId": 0
    },
    {
        "id": 6,
        "name": "Mrs. Peacock",
        "type": "character",
        "gameId": 0
    }
]

allRooms = [
    {
        "id": 7,
        "name": "Conservatory",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 8,
        "name": "Ballroom",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 9,
        "name": "Billiards Room",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 10,
        "name": "Great Hall",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 11,
        "name": "Library",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 12,
        "name": "Lounge",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 13,
        "name": "Study",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 14,
        "name": "Kitchen",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 15,
        "name": "Dining Room",
        "type": "room",
        "gameId": 0
    },
    {
        "id": 16,
        "name": "Lead Pipe",
        "type": "weapon",
        "gameId": 0
    }
]

allWeapons = [
    {
        "id": 17,
        "name": "Knife",
        "type": "weapon",
        "gameId": 0
    },
    {
        "id": 18,
        "name": "Candlestick",
        "type": "weapon",
        "gameId": 0
    },
    {
        "id": 19,
        "name": "Gun",
        "type": "weapon",
        "gameId": 0
    },
    {
        "id": 20,
        "name": "Rope",
        "type": "weapon",
        "gameId": 0
    },
    {
        "id": 21,
        "name": "Wrench",
        "type": "weapon",
        "gameId": 0
    }
]

uId = 1

n = 6
t = 1.56
acc= 21
s = 945.00
objId = 1

data = dict(fun ="GeeksForGeeks", adj ="Portal")

gameData = str(dict(userId = uId, characters = allCharacters, weapons = allWeapons, rooms = allRooms, players = n, completionTime = t, accusables = acc, score = s, id = objId))


# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

print()
print()


print(gameData)

print()
print()



# convert them to JSON data and then print it
print('{')
print('"userId":', json.dumps(uId, indent=2), end=",\n")
print('"characters":', json.dumps(allCharacters, indent=2), end=",\n")
print('"weapons":', json.dumps(allWeapons, indent=2), end=",\n")
print('"rooms":', json.dumps(allRooms, indent=2), end=",\n")
print('"players":', json.dumps(n, indent=2), end=",\n")
print('"completionTime":', json.dumps(t, indent=2), end=",\n")
print('"accusables":', json.dumps(acc, indent=2), end=",\n")
print('"score":', json.dumps(s, indent=2), end=",\n")
print('"id":', json.dumps(objId, indent=2))  # the json data will be indented
print('}')

