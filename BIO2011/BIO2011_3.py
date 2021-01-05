#1b)8x6x4x2 = 384

def returnDigits(n):
    total = 0
    digit = 1
    while 1:
        total += 9**(digit//2)
        if total >= n:
            total -= 9**(digit//2)
            return (total,digit)
        digit += 1
    
def formNum(order,digits):
    num = ['']*digits

    if digits%2 != 0:
        num[digits//2] = '5'

    #now need to fill first digits//2 places
    a = form(order,digits//2)
    for i in range (0,len(a)):
        num[i] = a[i]
        
        num[digits-1-i] = str(10-int(a[i]))
        

    return num

choices = [1,2,3,4,5,6,7,8,9]
def form(order,digits):
    if digits == 1:
        return str(order)
    
    total = 9**digits
    per = int(total/9)

    for i in range (1,10):
        if order <= per*i:
            return str(i) + form(order-(per*(i-1)),digits-1)

n = int(input())
if n == 1:
    print(5)
else:
    data = returnDigits(n)
    needed = n-data[0]
    digits = data[1]
    print(''.join(formNum(needed,digits)))
