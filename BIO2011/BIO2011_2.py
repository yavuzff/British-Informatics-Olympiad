#1h left 21:30
#BIO 2011 Q2
#2b)'2C', 'KC', '3H', 'KH', '4S', 'KS', '2D', 'KD', '4C', '2H', '7H', '5S'
#2d)
'''
When a move is made, a pile of cards with a matching top card is moved onto a
pile of cards with a matching top card(i.e. valid move). If the pile on the right
consists of at least 2 cards, this means when the finished pile is dealt at the end,
the matching cards will not be adjacent. However, in a game, the first move is always
moving a single card on top of another single matching card, meaning that they will
be adjacent to each other somewhere in the finished pile and when dealt out, they will
be next to each other. Although the card moving may be different, they will still match
and it will be a valid move.
'''

import copy
def shuffle(deck,n):
    deck = copy.deepcopy(deck)
    
    for i in range (n):
        card = deck[0]
        deck.pop(0)
        deck.append(card)
    
    deck.pop(-1)
    return (card,deck)
    

def initalShuffle():              
    ##vals = 'A23456789TJQK'
    ##deck = []
    ##
    ##for i in ['C','H','S','D']:
    ##    for j in vals:
    ##        deck.append(j+i)

    orig = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']

    deck = copy.deepcopy(orig)
    board = []

    nums = [int(x) for x in input().split()]
    c = 0
    while len(deck) > 0:
        info = shuffle(deck,nums[c])
        board.append(info[0])
        deck = info[1]

        c= (c+1)%6

    #print('answer:',board[:12]) #for 2b
    
    print(board[0] + ' ' + board[-1])
    return board

def rightmost1(board):
    l = len(board)
    if l == 1:
        return None

    for i in range (0,l-3):
        index = l-i-1
        card = board[index]
        if isvalid(card,board[index-1]):
            return(index,index-1)

        if isvalid(card,board[index-3]):
            return(index,index-3)


    if l>3 and isvalid(board[3],board[2]):
        return (3,2)

    if l>3 and isvalid(board[3],board[0]):
        return (3,0)
        
    if l>2 and isvalid(board[2],board[1]):
        return (2,1)
    
    if isvalid(board[1],board[0]):
        return (1,0)

    return None

    
def strategy1(board):
    board = copy.deepcopy(board)
    piles = [1 for i in range (len(board))]
    
    move = True
    while len(board) > 1 or move == None:
        move = rightmost1(board)

        if move == None:
            break
        
        board[move[1]] = board[move[0]]
        piles[move[1]] += piles[move[0]]
            
        board.pop(move[0])
        piles.pop(move[0])

    print(str(len(piles)) + ' ' + board[0])

def strategy2(board):
    board = copy.deepcopy(board)
    piles = [1 for i in range (len(board))]

    move = True
    while len(board)>1 or move == None:
        move = maxmove(board,piles)
        if move == None:
            break
        
        board[move[1]] = board[move[0]]
        piles[move[1]] += piles[move[0]]
            
        board.pop(move[0])
        piles.pop(move[0])

    print(str(len(piles)) + ' ' + board[0])
    
def maxmove(board,piles,three = False):
    board = copy.deepcopy(board)
    
    moves = []
    madepile = []
    
    l = len(board)
    if l == 1:
        return None

    for i in range (0,l-3):
        index = l-i-1
        
        card = board[index]
        if isvalid(card,board[index-1]):
            moves.append((index,index-1))
            temp = piles[index] + piles[index-1]
            madepile.append(temp)

        if isvalid(card,board[index-3]):
            moves.append((index,index-3))
            temp = piles[index] + piles[index-3]
            madepile.append(temp)

        
    if l>2 and isvalid(board[2],board[1]):
        moves.append((2,1))
        madepile.append(piles[2] + piles[1])
    
    if isvalid(board[1],board[0]):
        moves.append((1,0))
        madepile.append(piles[1] + piles[0])

    if moves == []:
        return None
    
    if three == False:
        return moves[madepile.index(max(madepile))]
    else:
        return moves
    

def isvalid(card1,card2):
    if card1[0] == card2[0]:
        return True
    elif card1[1] == card2[1]:
        return True
    return False

def strategy3(board):
    board = copy.deepcopy(board)
    piles = [1 for i in range (len(board))]
    
    move = True
    while len(board) > 1 or move == None:
        move = moves3(board,piles)

        if move == None:
            break
        
        board[move[1]] = board[move[0]]
        piles[move[1]] += piles[move[0]]
            
        board.pop(move[0])
        piles.pop(move[0])

    print(str(len(piles)) + ' ' + board[0]) 
    

def moves3(board,piles):
    possibleMoves = maxmove(board,piles,True)
    
    if possibleMoves == None:
        return None
    
    futureMoves = []
    for move in possibleMoves:
        tempB = copy.deepcopy(board)
        tempP = copy.deepcopy(piles)

        tempB[move[1]] = tempB[move[0]]
        tempP[move[1]] += tempP[move[0]]
            
        tempB.pop(move[0])
        tempP.pop(move[0])

        nextMov = maxmove(tempB,tempP,True)
        if nextMov == None:
            futureMoves.append(0)
        else:
            futureMoves.append(len(nextMov))
            
    return possibleMoves[futureMoves.index(max(futureMoves))]


board = initalShuffle()
strategy1(board)
strategy2(board)
strategy3(board)






















