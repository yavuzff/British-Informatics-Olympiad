#Yavuz Ferhatosmanoglu King Edward VI school

def lastletter(word):
    last = -1
    for i in range (len(word)):
        index = alpha.index(word[i])
        if index > last:
            last = index
    return last

def isValid(word1,word2):
    last = lastletter(word2)

    for i in word1:
        index = alpha.index(i)
        if index <= last:
            return False

    return True

def allSplits(word):
    if len(word) == 2:
        return [[word[0],word[1]]]

    splits = []
    for mid in range (1,len(word)):
        part1 = word[:mid]
        part2 = word[mid:]
        splits.append([part1,part2])

    return splits

def isPat(word):
    if len(word) == 1:
        return True
    
    splits = allSplits(word)
    for comb in splits:
        w1 = comb[0]
        w2 = comb[1]
        if not isValid(w1,w2):
            continue

        r1 = ''.join(reversed(w1))
        r2 = ''.join(reversed(w2))
        
        if isPat(r1) and isPat(r2):
            return True
        
    return False

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

words = input().split()
word1 = words[0]
word2 = words[1]

if isPat(word1):
    print('YES')
else:
    print('NO')

if isPat(word2):
    print('YES')
else:
    print('NO')

if isPat(word1+word2):
    print('YES')
else:
    print('NO')
