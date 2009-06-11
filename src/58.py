'''
Created on Apr 18, 2009

@author: anon
'''
from ProjectEulerLibrary import isPrime

primeCount = 0
compositeCount = 0
n = 1

skipAmount = 1

while skipAmount <= 100000:
    for i in range(4):
        n = n + (skipAmount + 1)
        if isPrime(n):
            primeCount = primeCount + 1
        else:
            compositeCount = compositeCount + 1
    ratio = primeCount / (compositeCount + primeCount) 
    if ratio * 100 < 10:
        print(skipAmount)
        break
    skipAmount = skipAmount + 2
