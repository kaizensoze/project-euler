'''
Created on Apr 2, 2009

@author: anon
'''
import cProfile

from ProjectEulerLibrary import primeNumbers, sumOfPrimes

primes = primeNumbers(10)
print(primes)

# cProfile.run('print(primeNumbers(10))')
# cProfile.run('print(sumOfPrimes(10))') 
