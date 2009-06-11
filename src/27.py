'''
Created on Apr 12, 2009

@author: anon
'''
from ProjectEulerLibrary import isPrime

maxPrimeCount = 0
coeffProd = 1
lastWasPrime = True

for b in [x for x in range(1,1000) if isPrime(x)]:
    for a in range(-999, 999):
        primeCount = 0
        n = 0
        while isPrime(n**2 + a*n + b):
            primeCount = primeCount + 1
            n = n + 1
            
        if primeCount > maxPrimeCount:
            maxPrimeCount= primeCount
            coeffProd = a * b
            
        print('a=%s b=%s' % (a,b))

print(coeffProd)
