#bio 2010 question 3, solves 1 and 2 jug problems

def fill(jug): #fills a jug
    jugs[jug] = jugSize[jug]

def empty(jug): #empties a jug
    jugs[jug] = 0

def transfer(jug,jug2): #transfers from jug1 to jug2
    remaining = jugSize[jug2] - jugs[jug2]

    if jugs[jug] <= remaining: #the first jug will be empty in this case
        jugs[jug2] += jugs[jug]
        empty(jug)

    else: #the second jug will be full in this case
        jugs[jug] -= remaining
        jugs[jug2] += remaining




#while True: #usedfor testing
#inputting data
first = input().split()
first = [int(x) for x in first]

jugsNum = first[0]
required = first[1]

jugSize = [int(x) for x in input().split()]


jugs = [0]*jugsNum


#if there is 1 jug, or the required sum is the total capacity of a jug
if jugsNum == 1 or (required in jugSize):
    print('1') #then 1 move will be enough

else: #if there are 2 jugs
    #2 processes will be done, the lowest will be returned
    step = 0
    while required not in jugs:
    #until the required amount of water is found:
        
        if jugs[0] == 0: #fill jug1 if empty
            fill(0)

        elif jugs[1] == jugSize[1]: #empty jug2 if full
            empty(1)
            
        else:
            transfer(0,1) #else transfer from 1 to 2

       
        #print(jugs)
        step+=1

    #print(step)
    #reset the variables
    step2 = 0
    jugs = [0]*jugsNum

    while required not in jugs:
        if jugs[1] == 0:#fill jug2 if empty
            fill(1)

        elif jugs[0] == jugSize[0]:#empty jug1 if full
            empty(0)
            
        else: #transfer from jug2 to jug1
            transfer(1,0)
    
        step2 += 1
    #print(step2)

    print(min(step,step2)) #return the lowest step one for answer

    
    
