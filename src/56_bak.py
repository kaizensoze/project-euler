'''
Created on Apr 17, 2009

@author: joeg
'''

maxSum = 0
for a in range(1,100):
    for b in range(1,100):
        mySum = sum([int(x) for x in str(a**b)])
        if mySum > maxSum:
            maxSum = mySum

print(maxSum)        