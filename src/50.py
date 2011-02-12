'''
Created on Jun 12, 2009

@author: anon
'''

import math
from ProjectEulerLibrary import getPrimes, isPrime

n = 1000000
primes = getPrimes(math.ceil(n/2))

maxLength = 0
maxLengthSum = 0

for i in range(len(primes)):
    sum = 0
    length = 0
    for y in primes[i:]:
        sum += y
        if sum >= n:
            break
        if isPrime(sum) and length > maxLength:
            maxLengthSum = sum
            maxLength = length
        length += 1
               
print(maxLengthSum)