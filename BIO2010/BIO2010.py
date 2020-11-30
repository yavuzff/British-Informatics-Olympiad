#q2:28415970,17049582,14207985
#q3:138

def returnCount(number):
    numbers = [0,0,0,0,0,0,0,0,0,0]

    for i in number:
        numbers[int(i)] +=1

    return numbers

while True:
    numberInput = input().strip()
    numberCount = returnCount(numberInput)

    #print(numbers)

    anagrams = []
    for i in range(2,10):
        newNumber = str(int(numberInput)*i)
        newCount = returnCount(newNumber)
        valid = True
        
        for j in range(0,9):
            if newCount[j] != numberCount[j]:
                valid = False
                break

        if valid == True:
            anagrams.append(i)
            
    answer = ''

    if len(anagrams)==0:
        print('NO')
    else:
        for i in anagrams:
            answer += str(i)+' '

        print(answer.strip())

'''
#Q3 working
def has_doubles(n):
    return len(set(str(n))) < len(str(n))

total = 0
for num in range (100000,999999):
    numlist = list(map(int, str(num)))
    if len(numlist) == len(set(numlist)):
        for a in range (2,10):
            numCount = returnCount(str(num))
            new = num * a
            newCount = returnCount(str(new))

            if newCount == numCount:
                total+= 1
                break

        
print(total)
'''

