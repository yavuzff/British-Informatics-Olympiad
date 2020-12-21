#bio 2015 q1

#1b) [A][A][B][C][B][A][A]
#    [AA][B][C][B][AA]
#    [AA][BCB][AA]
#    [A][A][BCB][A][A]
#    [A][ABCBA][A]


def blocks(word):
    groupings = 0
    for i in range (1,len(word)//2+1): #block length can be between 1 and half of the word
        start = word[:i] #the substrings gathered from start and end of string
        end = word[-i:]
        if start == end: #if the same
            groupings += 1 + blocks(word[i:-i]) 
            
    return groupings


word = input().strip()

if len(word) in [2,3]:
    if word[0] == word[-1]:
        print('1')
    else:
        print ('0')
else:
    print (blocks(word))




