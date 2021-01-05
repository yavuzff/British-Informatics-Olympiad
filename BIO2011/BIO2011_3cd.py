#1c)38

num = '1' + ('0'*18)
num = int(num)-1
digits = 1

while num > 0:
    num -= 9**(digits//2)
    digits += 1
    
print(digits-1)

#1d)
'''
There are the same number of 1000 and 1001 digit upside down numbers,
9^500 of them. 

All of the upside down numbers with 1001 contains at least one 5.
As it has an odd number of digits, the middle digit or the 501st digit
will be counted twice when adding up as it is both the 501st digit from
left and right, thus it has to be a 5. This means that the other 1000
digits can be non 5.

Not all of the 1000 digit numbers will have a 5 in it (unlike the 1001 digit)
which gives it a lower total. The ones that do have a 5 in it will need it to
occur twice, giving 998 other digits.

Therefore there are more 1001 digit upside down numbers with at least one 5 in it.
