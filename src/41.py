'''
Created on Apr 12, 2009

@author: anon
'''
from ProjectEulerLibrary import isPrime, isPandigital

for n in range(1,9000000):
    if isPandigital(n) and isPrime(n):
        print(n)
