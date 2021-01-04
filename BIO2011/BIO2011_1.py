#BIO 2011 Q1
#1b)r,q
#1c)k
def fibo(n,first,second):
    if n == 1:
        return first

    count = 2
    while count < n:
        temp = first
        first = second
        second = (second + temp)%26
        count += 1
        
    return second


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

data = input().split()

num1 = data[0]
num2 = data[1]
n = int(data[2])

index1 = alphabet.index(num1)+1
index2 = alphabet.index(num2)+1

answer = fibo(n,index1,index2)

answer = (answer-1)%26

print(alphabet[answer])
