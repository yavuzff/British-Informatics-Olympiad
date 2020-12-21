#bio 2015 q2

def checkBlock(x,y): #checks if a block can be placed 
    valid = True    #i.e all adjacent and current block is free

    if board[x][y] != 0:
        return False
    elif x<9 and board[x+1][y] != 0:
        valid = False
    elif x<9 and y<9 and board[x+1][y+1] != 0:
        valid = False
    elif x<9 and y>0 and board[x+1][y-1] != 0:
        valid = False
        
    elif x>0 and board[x-1][y] != 0:
        valid = False
    elif x>0 and y>0 and board[x-1][y-1] != 0:
        valid = False
    elif x>0 and y<9 and board[x-1][y+1] != 0:
        valid = False

    elif y>0 and board[x][y-1] != 0:
        valid = False
    elif y<9 and board[x][y+1] != 0:
        valid = False

    return valid


data = [int(x) for x in input().split()] #data is input
board = []
for i in range (10):
    board.append([0]*10)

a = data[0]
c = data[1]
m = data[2]
r = 0

#4 ship, two 3 ship, three 2 ship, four 1 ship
ships = [4,3,3,2,2,2,1,1,1,1]
ship = 0
answer = ''
while ship < 10:
    l = ships[ship] #the length of the ship is received from the list of ships
    
    r = (a*r+c)%m #the algorithm is carried out on the value

    x = int(str(r)[-1])
    y = int(('0'+str(r))[-2])

    r = (a*r+c)%m

    if r % 2 == 0:
        place = 'H'

    else:
        place = 'V'

    valid = True

    #made sure if the ship can fit onto the board
    if place == 'V' and y+l >10:
        valid = False
    if place == 'H' and x+l > 10:
        valid = False
        
    origx = x
    origy = y #x and y are given in format so 0,0 is bottom left
    temp = x  #these values are converted so x and y correctly work with the 2d array
    x = y 
    y = temp
    x = 9-x
    
    if valid:
        for i in range (0,l): #l is the length of the ship
            if place == 'H': #all the blocks are checked if free
                if not checkBlock(x,y+i):
                    valid = False

            else:
                if not checkBlock(x-i,y):
                    valid = False
            
    if valid:
        for i in range (0,l): #the blocks are filled
            if place == 'H':
                board[x][y+i] = 1
            else:
                board[x-i][y] = 1
        answer += str(origx)+' '+str(origy)+' '+place+'\n'
        ship += 1 #next ship
    
print(answer[:-1]) #removes the last \n when printing
        
