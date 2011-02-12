'''
Created on Apr 8, 2009

@author: joeg
'''
from decimal import *

sum = 0
for x in range(1,1000+1):
    n = x**x
    sum = sum + n

print(sum)
print(str(sum)[-10:])