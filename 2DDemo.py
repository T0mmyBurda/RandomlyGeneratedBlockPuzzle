import random

#matrix that will repesent a 2d puzzle
mat = [ [ "1" , "" , "" , "" ] ,
        [ "" , "1" , "" , "" ] ,
        [ "" , "" , "1" , "" ] ,
        [ "" , "" , "" , "1" ] ]

def main():

    makePiece("y")

def printMat():
    line = ""
    
    for i in range(len(mat)):
        line = ""
        for j in range (len(mat[0])):
            if(mat[i][j] == ""):
                line += "-" # "-" is equal to an empty space
            else:
                line += mat[i][j] # prints symbol at spot in matrix

            line += " "
        print(line)

def makePiece(sym):
    #gets cordinates to start piece
    curX = random.randint(0, 3)
    curY = random.randint(0, 3)

    #gets new cordinates if the spot is taken already
    while(mat[curX][curY] != ""):
        curX = random.randint(0, 3)
        curY = random.randint(0, 3)

    print(curX)
    print(curY)

    mat[curY][curX] = sym
    printMat()

    pieceCords = [] #holds a record of all the cords of the piece so that when there is a locked cord a new one can continue the peice
    lockedCords = [] # array of indexes of locked cords so they are not reused
    
    for i in range (3):
        pieceCords.append([curX , curY]) #stores cords in pieceCords
        cords = nextDir(curX , curY , sym)
        printMat()
        curX = cords[0]
        curY = cords[1]

        if (locked(curX , curY)):
            print("CORDS " + str(curX) + " , " + str(curY) + " LOCKED")
            lockedCords.append([curX , curY]) #adds current cord to list of locked cords
            cord = random.choice(pieceCords) #chooses new cord
            while(cord not in lockedCords): #makes sure new cords are not in locked list
                cord = random.choice(pieceCords)
            curX = cords[0]#sets new cords
            curY = cords[1]
            print("NEW CORDS: " + str(curX) + " , " + str(curY))
            

def nextDir(x , y , sym):
    direction = random.randint(0, 3)

    if(direction == 0): #up
        if(y > 0):
            print("up , " + mat[y - 1][x])
        if(y == 0):
            print("edge")
            return nextDir(x , y , sym)
        elif(mat[y - 1][x] != ""):
            print("blocked")
            return nextDir(x , y , sym)
        else:
            mat[y - 1][x] = sym
            print("cords = " + str(x) + " , " + str((y - 1)))
            return [x , y - 1]
        
    if(direction == 1): #left
        if(x < 3):
            print("left , " + mat[y][x + 1])
        if(x == 3):
            print("edge")
            return nextDir(x , y , sym)
        elif(mat[y][x + 1] != ""):
            print("blocked")
            return nextDir(x , y , sym)
        else:
            mat[y][x + 1] = sym
            print("cords = " + str((x + 1)) + " , " + str(y))
            return [x + 1 , y]

    if(direction == 2): #down
        if(y < 3):
            print("down , " + mat[y + 1][x])
        if(y == 3):
            print("edge")
            return nextDir(x , y , sym)
        elif(mat[y + 1][x] != ""):
            print("blocked")
            return nextDir(x , y , sym)
        else:
            mat[y + 1][x] = sym
            print("cords = " + str(x) + " , " + str((y + 1)))
            return [x , y + 1]

    if(direction == 3): #right
        if(x > 0):
            print("right , " + mat[y][x - 1])
        if(x == 0):
            print("edge")
            return nextDir(x , y , sym)
        elif(mat[y][x - 1] != ""):
            print("blocked")
            return nextDir(x , y , sym)
        else:
            mat[y][x - 1] = sym
            print("cords = " + str((x - 1)) + " , " + str(y))
            return [x - 1 , y]

    

def locked (x , y):
    if((y == 0) or (mat[y - 1][x] != "")): #checks if up is blocked
        print("up locked")
        if((x == 3) or (mat[y][x + 1] != "")): #checks if left is blocked
            print("left locked")
            if((y == 3) or (mat[y][x - 1] != "")): #checks right is blocked
                print("right locked")
                if((x == 0) or (mat[y + 1][x] != "")): #checks down up is blocked
                    print("down locked")
                    return True
    return False

    
main()
