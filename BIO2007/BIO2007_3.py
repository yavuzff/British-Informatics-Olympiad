#bio 2007 q3, 17/24
#3b) 256, 34
#3d)A->ZZ B->Z

def step(word):
    new = ''

    for i in word:
        if i == 'A':
            new += 'B'
        elif i == 'B':
            new += 'AB'
        elif i == 'C':
            new += 'CD'

        elif i == 'D':
            new += 'DC'

        elif i == 'E':
            new += 'EE'

    return new

while True:
    
    word = input()
    numbers = input().split()

    numbers = [int(i) for i in numbers]

    if all([True if i == 'E' else False for i in word]):
        print('0 0 0 0 '+str(numbers[1]))

    else:
        if 'A' not in word:

            length = 2**numbers[0]
            
            if numbers[1] <= length:
                word = word[0]

            else:
                length = 2*length

                if numbers[1] <= length:
                    word = word[0] + word[1]

        
        #print('in here')
        new = step(word)
        for i in range (1,numbers[0]):
            #print('step')
            new = step(new)
            #if len(new) > numbers[1]:
              #  break


        #print(new)

        cut = new[0:numbers[1]]

        count = [0,0,0,0,0]

        for i in cut:
            if i == 'A':
                count[0] += 1
            elif i == 'B':
                count[1] += 1
            elif i == 'C':
                count[2] += 1
            elif i == 'D':
                count[3] += 1
            elif i == 'E':
                count[4] += 1
                
        for i in range (0,5):
            count[i] = str(count[i])
            
        print (' '.join(count))
