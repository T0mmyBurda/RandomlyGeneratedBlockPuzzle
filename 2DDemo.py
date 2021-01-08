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
    
    for i in range (3):
        cords = nextDir(curX , curY , sym)
        printMat()
        curX = cords[0]
        curY = cords[1]

def nextDir(x , y , sym):
    #nextDir = random.randint(0, 3)
    direction = random.randint(0, 3)

    if(direction == 0): #up
        print("up , " + mat[y - 1][x])
        if(y == 0):
            print("edge")
            nextDir(x , y , sym)
        elif(mat[y - 1][x] != ""):
            print("blocked")
            nextDir(x , y , sym)
        else:
            mat[y - 1][x] = sym
            return [x , y - 1]
        
    if(direction == 1): #left
        print("left , " + mat[y][x + 1])
        if(x == 3):
            print("edge")
            nextDir(x , y , sym)
        elif(mat[y][x + 1] != ""):
            print("blocked")
            nextDir(x , y , sym)
        else:
            mat[y][x + 1] = sym
            return [x + 1 , y]

    if(direction == 2): #down
        print("down , " + mat[y - 1][x])
        if(y == 3):
            print("edge")
            nextDir(x , y , sym)
        elif(mat[y - 1][x] != ""):
            print("blocked")
            nextDir(x , y , sym)
        else:
            mat[y - 1][x] = sym
            return [x , y - 1]

    if(direction == 3): #right
        print("right , " + mat[y][x - 1])
        if(x == 0):
            print("edge")
            nextDir(x , y , sym)
        elif(mat[y][x - 1] != ""):
            print("blocked")
            nextDir(x , y , sym)
        else:
            mat[y][x - 1] = sym
            return [x - 1 , y]

    

def locked (x , y):
    if((y == 0) or (mat[y - 1][x] != "")): #checks if up is blocked
        print("up locked")
        if((x == 3) or (mat[y][x + 1] != "")): #checks if left is blocked
            print("left locked")
            if((y == 3) or (mat[y][x - 1] != "")): #checks right up is blocked
                print("down locked")
                if((x == 0) or (mat[y][x - 1] != "")): #checks down up is blocked
                    print("right locked")
                    return True
    return False

    
main()
