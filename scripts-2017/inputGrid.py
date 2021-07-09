import math
#import random
# Ben Davis
# attempt to program a user input grid systerm
# 8-10-2017

z = 0 #this will count how many steps we took
h = 0 #which element in the SRC we should be on

Size = []
Row = []
Col = []
for i in range(5):
    size = 5-i
    #print("global size: ", size)
    for j in range(6-size):
        row = j+1
        #print("global row: ", row)
        for k in range(6-size):
            col = k + 1
            #print("global col: ", col)
            Size.append(size)
            Row.append(row)
            Col.append(col)
SRC = []
for i in range(55):
    SRC.append([])
    SRC[i].append(Size[i])
    SRC[i].append(Row[i])
    SRC[i].append(Col[i]) #and now we have a descending list of all possible combinations
#---------------------------------------------
def Get_Symbols(grid):
    symbols = []
    print(grid[0][0][0])
    symb1 = ord(grid[0][0][0])
    breakval = 0
    print(symb1)    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(len(grid[i][j])):
                if ord(grid[i][j][k]) != symb1:
                    symb2 = ord(grid[i][j][k])
                    print("found symbol2: ", symb2)
                    breakval = 1
                if breakval == 1:
                    break
            if breakval == 1:
                break
        if breakval == 1:
            break
    symbols.append(symb1)
    symbols.append(symb2)
    return symbols
#---------------------------------------------  
#---------------------------------------------
def negate(grid, size, sRow, sCol, symbol1, symbol2):
    print("Negation------")
    newRow = ""
    row = sRow - 1
    col = sCol - 1
    oppGrid = []
    smallGrid = findSmallGrid(grid, size, sRow, sCol)
    print(grid)
    print("")
    print(smallGrid)
    for h in range(len(smallGrid)):
        newRow = ""
        for k in range(len(smallGrid[h])):
            if ord(smallGrid[h][k]) == symbol1:
                newRow = newRow + chr(symbol2)
            elif ord(smallGrid[h][k]) == symbol2:
                newRow = newRow + chr(symbol1)
        print(newRow)
        oppGrid.append(newRow)
    print(oppGrid)
    return oppGrid
#-----------------------------------------------           
#-------------------------------------------------

def flipVertical(grid, size, sRow, sCol):
    print("Flip vertical-----")
    newGrid = []
    smallGrid = findSmallGrid(grid, size, sRow, sCol)
    row = sRow - 1
    col = sCol - 1

    print(grid)
    print("")
    print(smallGrid)
    
    for i in range(len(grid)-1,-1,-1): # read rows in reverse
        print(grid[i])
        newGrid.append(grid[i])
    print(newGrid)         
    return newGrid
#-------------------------------------------------
#----------------------------------------------- 
def flipHorizontal(grid, size, sRow, sCol):
    print("Flip horizontal------")
    newRow = ""  # flip the rows around, then append each row to the new grid list
    newGrid = []
    i = 0
    j = 0
    smallGrid = findSmallGrid(grid, size, sRow, sCol)
    row = sRow - 1
    col = sCol - 1
    
    print(grid)
    print("")
    print(smallGrid)
    
    for i in range(len(smallGrid)):  # access rows
        newRow = ""
        for j in range(len(smallGrid[i])-1,-1,-1):  #access elements in rows (columns), read backwards
            newRow = newRow + smallGrid[i][j]
        print(newRow)
        newGrid.append(newRow)
    print(newGrid)
    return newGrid
#----------------------------------------------- 
#----------------------------------------------- 
def inputGrid(gridSize):
    print("\nEnter the initial and final grid input (one spaces separate initial grd form final grid):")
    initialgrid = []
    finalGrid = []
    grid = []
    i = 0
    for i in range(gridSize):
        row = ""
        row = input()
        if len(row) == ((gridSize*2)+1):
            initialgrid.append(row[0:gridSize])
            finalGrid.append(row[gridSize+1:])
    
    print(len(initialgrid), len(finalGrid))

    grid.append(initialgrid)     # so initial grid can be in grid[0]
    grid.append(finalGrid)  
    
    return grid
#-----------------------------------------------        
#----------------------------------------------- 
def findSmallGrid(grid, size, startrow, startcolumn):
    smallGrid = []
    row = startrow-1
    col = startcolumn -1
    print(str(row), str(col))
    for i in range(size):
        smallGrid.append([])
    for p in range(size):
        print("for p in size: " + str(p))
        for j in range(size):
            print("for j in size: " + str(j))
            smallGrid[p].append(grid[p+row][j+col]) #the small grid is the specific section of the thing we are editing
    return smallGrid
#-----------------------------------------------
#---------------------------------- Where the steps are taken to match the grids
def callRandomFunctions(grid, originalGrid, initialError, endGrid):
    #size = random.randint(1,5)
    #startrow = random.randint(1,6-size)
    #startcolumn = random.randint(1,6-size)
    global h
    size = SRC[h][0]
    startrow = SRC[h][1]
    startcolumn = SRC[h][2]

#---attempt to negate selected region:
    grid = negate(grid, size, startrow, startcolumn)
    errorAfterInvert = checkIfEqual(grid, endGrid)

    global z
    h = h + 1
    
    if errorAfterNegate >= initialError:
        grid = negate(grid, size, startrow, startcolumn)  #reset b/c worse after negation
        errorAfterNegate = checkIfEqual(grid, endGrid)
    else:
        print("negation successful")
        print(size,startrow,startcolumn)
        z = z + 1

#---attempt to flip vertically selected region:
    grid = flipVertical(grid, size, startrow, startcolumn)
    errorAfterVertical = checkIfEqual(grid, endGrid)

    if errorAfterVertical >= errorAfterInvert:
        grid = flipVertical(grid, size, startrow, startcolumn) #reset b/c worse after vertical
        errorAfterVertical = checkIfEqual(grid, endGrid)
    else:
        print("vertical flip successful")
        print(size,startrow,startcolumn)
        z = z + 1

#---attempt to flip horizontally selected region:
    grid = flipHorizontal(grid, size, startrow, startcolumn)
    errorAfterHorizontal = checkIfEqual(grid, endGrid)

    if errorAfterHorizontal >= errorAfterVertical:
        grid = flipHorizontal(grid, size, startrow, startcolumn) #reset b/c worse after horizontal
        errorAfterHorizontal = checkIfEqual(grid, endGrid)
    else:
        print("horizontal flip successful")
        print(size,startrow,startcolumn)
        z = z + 1
    
    return grid
#----------------------------------------------- 
#----------------------------------------------- 
def main():
    #size = int(input("What size is the square grid?"))
        
    initGrid = inputGrid(5) #each test case will be a 5X5 grid
    print(initGrid)

    size = SRC[h][0]
    startrow = SRC[h][1]
    startcolumn = SRC[h][2]

    symbols = Get_Symbols(initGrid)
    symbol1 = symbols[0]
    symbol2 = symbols[1]
    beginGrid = initGrid[0]
    endGrid = initGrid[1]
    
    
    print("\nBeginning grid:")
    j = 0
    for j in range(len(beginGrid)):   # accessing the initial grid 
        print(str(beginGrid[j]))

    print("\nFinal grid:")
    k = 0
    for k in range(len(endGrid)):
        print(str(endGrid[k]))

    small = findSmallGrid(beginGrid, size, startrow, startcolumn)
    print(small)

    #print("\n vertical flip of grid:")
    #vertGrid = flipVertical(initGrid[0])
    #print(vertGrid)

    #print("\n horizontal flip of grid:")
    #horzGrid = flipHorizontal(vertGrid)   # let's see if we can flip the already flipped grid :)
    #print(horzGrid)

    #print("\n negate grid:")
    #nGrid = negate(initGrid[0], symbol1, symbol2)
    #print(nGrid)

main()
#----------------------------------------------- 
