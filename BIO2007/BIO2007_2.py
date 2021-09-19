#bio 2007 q2
#2b XOEXXXOOO and XOOXXXOOE, XOOXXXOOE will be chosen
from copy import deepcopy

def adjacent(index):
    if index == 0:
        return list(board[1:])

    elif index == 1:
        return [2,8] 

    elif index == 8:
        return [1,7]

    else:
        return [index-1,index+1]

def canMove(index):
    player = board[index]

    if board[index] == 'E':
        return False
    if index == 0:
        return board.index('E') #can always move to E

    else: 
        adj = adjacent(index) #plus middle
        adjvalue = [board[adj[0]],board[adj[1]]]

        if 'E' in adjvalue:
            return adj[adjvalue.index('E')]

        elif board[adj[0]] == board[adj[1]] == player:
            return False

        elif board[0] == 'E':
            return 0

        else:
            return False
    

def isLoss(player):
    for i in range (0,len(board)):
        if board[i] == player:
            if str(canMove(i)) != 'False':
                return False

    return True

def canWin(moves,opp):
    global board
    
    orig = deepcopy(board)
    for i in moves: #see if winning
        index = i[0]
        to = i[1]
        board[to] = board[index]
        board[index] = 'E'
        if isLoss(opp):
            return i
        board = deepcopy(orig)
        
    return False

def generatePossible(current):
    possible = []
    for i in range (0,len(board)):
        if board[i] == current:
            move = canMove(i)
            if str(move) != 'False':
                possible.append([i,move])
    return possible



board = list(input())
info = input()

turn = 0
current = 'O'

while True:
    end = False
    if current == 'O':
        opp = 'X'
    else:
        opp = 'O'
    
    possible = generatePossible(current)

    if isLoss(current):
        if current == 'O':
            print(''.join(board))
            print('Player 2 wins')
            break
        else:
            print(''.join(board))
            print('Player 1 wins')
            break
        
    moved = False
    move = canWin(possible,opp)
    if move != False: #check if can win
        moved = True
        end = True

    if not moved:
        orig = deepcopy(board)
        for i in possible:
            index = i[0]
            to = i[1]
            board[to] = board[index]
            board[index] = 'E'
            
            oppPossible = generatePossible(opp)
            oppMove = canWin(oppPossible,current)
            
            if oppMove == False:
                moved = True
                break
            else:
                board = deepcopy(orig)
    
    
    if not moved: #just move left most
        index = possible[0][0]
        to = possible[0][1]
        board[to] = board[index]
        board[index] = 'E'
        

    if current == 'O':
        current = 'X'
        opp = 'O'
    else:
        current = 'O'
        opp = 'X'

    if info == 'n' and not end:
        print(''.join(board))
        info = input()
        
    turn += 1

    if turn == 1000:
        print('Draw')
        break
