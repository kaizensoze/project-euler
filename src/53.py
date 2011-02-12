'''
Created on Apr 17, 2009

@author: joeg
'''
from functools import reduce


def factorial(n):
    if n <= 1:
        return 1
    return reduce(lambda x,y: x*y, [x for x in range(1,n+1)])

def choose(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

count = 0
for n in range(1,100+1):
    for r in range(1,n+1):
        if choose(n,r) > 1000000:
            count = count + 1

print(count)