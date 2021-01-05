#BIO 2007 q1
#1b) 10 9 8 2 1

#points: 1 for each pair of same card, 1 for each group adding up to 15

nums = [int(x) for x in input().split()]

total = 0

#counting pairs
for i in range (0,len(nums)-1):
    rest = nums[i+1:]
    total += rest.count(nums[i])
    
#2,3,4,5 adds up to 15
#case 5:
if sum(nums) == 15:
    total+= 1
    print(total)

else:
    #case 2
    sols2 = []
    for i in range (0,len(nums)):
        for j in range (0,len(nums)):
            if i != j and nums[i] + nums[j] == 15:
                sol = [i,j]
                sol.sort()
                if sol not in sols2:
                    sols2.append(sol)

    total += len(sols2)

    #case 3
    sols3 = []

    for i in range (0,len(nums)):
        for j in range (0,len(nums)):
            for k in range (0,len(nums)):
                if i!=j and i!=k and j!=k and nums[i] + nums[j] + nums[k] == 15:
                    sol = [i,j,k]
                    sol.sort()
                    if sol not in sols3:
                        sols3.append(sol)

    total += len(sols3)

    #case 4
    sols4 = []
    for i in range (0,len(nums)):
        for j in range (0,len(nums)):
            for k in range (0,len(nums)):
                for l in range (0,len(nums)):
                    if i!=j and i!= k and i!=l and j!= k and j!=l and k!=l and nums[i] + nums[j] + nums[k] + nums[l] == 15:
                       sol = [i,j,k,l]
                       sol.sort()
                       if sol not in sols4:
                           sols4.append(sol)

    total += len(sols4)
    print(total)
                        
