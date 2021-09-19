#Yavuz 1 b and c

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

def partb():
    import itertools
    perms = itertools.permutations('ABCD')
    count = 0
    for i in perms:
        #print(list(i))
        if isPat(''.join(i)):
            count+= 1
            print(''.join(i))
    print(count)


#Part c function:

def p(n):
    if n in [0,1]:
        return 1
    if n in memoization:
        return memoization[n]

    total = 0
    for i in range (2,n+1):
        total += p(n-i) * (p(i-1)+p(i-2))
    memoization[n] = total

    
    return total


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

partb()

memoization = {} #for partc
#memoization data:{2: 2, 3: 5, 4: 14, 5: 42, 6: 132, 7: 429, 8: 1430, 9: 4862, 10: 16796, 11: 58786, 12: 208012, 13: 742900, 14: 2674440, 15: 9694845, 16: 35357670, 17: 129644790, 18: 477638700, 19: 1767263190, 20: 6564120420, 21: 24466267020, 22: 91482563640, 23: 343059613650, 24: 1289904147324, 25: 4861946401452, 26: 18367353072152}
