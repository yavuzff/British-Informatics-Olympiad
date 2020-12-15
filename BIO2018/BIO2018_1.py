#BIO 2018
#1b 5
#1c 96,49
import math
while True: #part c done through testing using this
    inputData = input().split()
    interest = int(inputData[0])
    repayment = int(inputData[1])


    debt = 100
    repaid = 0
    paid = 0

    while debt > 0:
        
        i = interest
        #i = math.ceil(i*100)/100
        d = debt*(i/100)
        d = math.ceil(d*100)/100
        debt += d
        
        r = repayment
        #r = math.ceil(r*100)/100 
        p = debt*(r/100)
        p = math.ceil(p*100)/100
        
        if p<50:
            p = 50
        if p>debt:
            p = debt
        
        repaid += p
        paid += 1
        debt -= p
        
        repaid = math.ceil(repaid*100)/100
    #print('Number of payments:',paid)  
    print(repaid)


