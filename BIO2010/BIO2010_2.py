"""
q1:32

q2d:The die will always be stuck in a loop as there are finite possibilities of heading
and orientation a die can be in. The die will end up in the same state as before, i.e.
it will have the same heading and orientation on the same part of the board. If it is in the
exact same state, it will perform the exact same moves as there is no randomness and the die
will ne stuck in an infinite loop.

"""

def inputLines(): #inputting data needed for game
    line1 = input().strip().split()
    line2 = input().split()
    line3 = input().split()

    for i in range (0,3):
        line1[i] = int(line1[i])
        line2[i] = int(line2[i])
        line3[i] = int(line3[i])

    return line1+line2+line3

def formGrid():
    #11 by 11 formed with all 1's
    grid = [1]*11

    for i in range(0,11):
        grid[i] = [1]*11


    middle = inputLines() #the middle of the grid is input 

    current = 0
    #print(middle)
    for i in range (4,7): #the middle of the grid 4 to 7 is updated with the middle entered by user
        for j in range (4,7):
            grid[i][j] = middle[current]
            current += 1


    
    #print (grid)

    return grid

def outputGrid(location,grid): #outputting grid
    x = location[0] #the location of the dice is split to x and y values
    y = location[1]
    
    for i in range(-1,2): #the left(-1), current (0)and right(+1) part of the x value will be shown
        row = ''
        for j in range(-1,2): #aboce, current and below of y values will be shown
        #loops 9 times in total for each box in the 3by3 grid
            
            if x+i <0 or y+j <0 or x+i>10 or y+j>10: #checks if the end of the grid is reached
                row += 'X' #adds an x if reached
                
            else:
                row += str(grid[x+i][y+j]) #if not end, the value at the grid is output
                
        print(row.strip()) #printed row by row
    
    
def makeMove():
    global headings,heading,grid,location,faceup
    
    total = faceup + grid[location[0]][location[1]]
    #print (total)
    
    if total > 6: #bring it to lower than 6
        total -= 6
        
    
    grid[location[0]][location[1]] = total #total and heading is received
    index = headings.index(heading)
    
    if total == 2: #need to manually change the possibilities of headings, e.g. 90 degree clockwise, anticlockwise
        if index == 0:
            heading = headings[2]
        elif index == 1:
            heading = headings[3]
        elif index == 2:
            heading = headings[1]
        else:
            heading = headings[0]

    elif total == 3 or total==4:
        if index == 0:
            heading = headings[1]
        elif index == 1:
            heading = headings[0]
        elif index == 2:
            heading = headings[3]
        else:
            heading = headings[2]
    elif total == 5:
        if index == 0:
            heading = headings[3]
        elif index == 1:
            heading = headings[2]
        elif index == 2:
            heading = headings[0]
        else:
            heading = headings[1]
        
    diceCombination(heading) #then the current layout of the dice is updated 

    
    location[0] += heading[0]
    location[1] += heading[1]
    location[0] = location[0]%11
    location[1] = location[1]%11
    
    
def diceCombination(heading):
    global dice
    #dice = [up,down,front,back,left,right]
    #dice = [1,6,5,2,3,4]
    orig = dice[:]

    #manually changing dice combination
    
    if heading ==[-1,0]: #up
        dice[0] = orig[2]
        dice[1] = orig[3]
        dice[2] = orig[1]
        dice[3] = orig[0]
        #dice[4] = orig[4]
        #dice[5] = orig[5]

    elif heading == [1,0]: #down
        dice[0] = orig[3]
        dice[1] = orig[2]
        dice[2] = orig[0]
        dice[3] = orig[1]

    elif heading == [0,1]: #right
        dice[0] = orig[4]
        dice[1] = orig[5]
        #dice[2] = orig[2]
        #dice[3] = orig[3]
        dice[4] = orig[1]
        dice[5] = orig[0]

    elif heading == [0,-1]:#left
        dice[0] = orig[5]
        dice[1] = orig[4]
        dice[4] = orig[0]
        dice[5] = orig[1]
        
    #print( dice)
    #return dice

while True: #used for testing
    #dice = [up,down,front,back,left,right]
    dice = [1,6,5,2,3,4]


    headings = [[-1,0],[1,0],[0,1],[0,-1]] #up down right left
        
    grid = formGrid()

    location = [5,5] #6,6 is the starting position
    heading = [-1,0]#up is the first heading
    faceup = dice[0]


    moves = 1
    while moves != 0: #loops until 0 is input
        moves = int(input())
        if moves != 0:
            for i in range(0,moves): #performs the moces
                faceup = dice[0]
                makeMove()
                #print (faceup)
                 
            outputGrid(location,grid)#outputs the grid



