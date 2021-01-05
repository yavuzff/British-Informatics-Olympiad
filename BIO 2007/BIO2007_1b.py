#28
from itertools import combinations_with_replacement as c
nums = [1,2,3,4,5,6,7,8,9,10]

combs = c(nums,5)

total = 0
for i in combs:
    if sum(i) == 15:
        print(i)
        total+= 1

print(total-1) #33333 is a combination but can only have 4 of the same

