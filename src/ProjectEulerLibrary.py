
import math

def primeNumbers(n):
    A = [True for x in range(2,n+1)]
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if A[i-2]:
            j = i ** 2
            while j <= n:
                A[j-2] = False
                j += i
    return [(i+2) for i,x in enumerate(A) if x]

def sumOfPrimes(n):
    primes = primeNumbers(n)
    return sum(primes)