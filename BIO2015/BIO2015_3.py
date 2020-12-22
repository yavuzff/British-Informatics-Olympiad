#bio 2015 q3

#3b) 10    2 2 2 2 10

from math import factorial as f

def permutations(a,b,c,d):
    totalPerm = f(a+b+c+d)
    return int(totalPerm / (f(a)*f(b)*f(c)*f(d)))

while True:

    data = [int(x) for x in input().split()]
    a,b,c,d,n = data[0],data[1],data[2],data[3],data[4]

    art = ''
    while not (a == b == c == d == 0):
        perms = permutations(a,b,c,d)

        aways = int(perms*(a/(a+b+c+d)))
        if a!=0 and n<=aways:
            art += 'A'
            a -= 1
            continue

        bways = int(perms*((a+b)/(a+b+c+d)))
        if b!=0 and n <= bways:
            art += 'B'
            b -= 1
            n -= aways
            continue

        cways = int(perms*((a+b+c)/(a+b+c+d)))
        if c!=0 and n<=cways:
            art += 'C'
            c -= 1
            n -= bways
            continue
        
        else:
            art += 'D'
            d -= 1
            n -= cways

    print (art)
                
    
    
