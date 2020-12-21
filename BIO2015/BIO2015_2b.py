#bio 2015 q2b
#3 0, 4 0, 8 0, 7 0
#2c 62

a = 2
c = 3
m = 17
r = 0

for i in range (8):
    
    r = (a*r+c)%m #the algorithm is carried out on the value

    x = int(str(r)[-1])
    y = int(('0'+str(r))[-2])

    r = (a*r+c)%m

    if r % 2 == 0:
        place = 'H'

    else:
        place = 'V'

    valid = True


    print(x,y)
        
