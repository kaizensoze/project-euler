'''
Created on Apr 9, 2009

@author: anon
'''
from functools import reduce
from ProjectEulerLibrary import factorial

sum = 0
for i in range(10,1000000):
    digits = [int(y) for y in str(i)]
    if i == reduce(lambda x,y: x+y, [factorial(x) for x in digits]):
        sum = sum + i
        
print(sum)