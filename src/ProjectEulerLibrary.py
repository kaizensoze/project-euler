
import math

def primeNumbers(n):
    numbers = [x for x in range(2, n+1)]
    marked = [False for x in numbers]
    x = p = 2
    while p:
        while x <= numbers[-1]:
            if x != p:
                marked[x-2] = True
            x += p
        try:
            p_index = next(i for i,x in enumerate(marked) if not x and numbers[i] > p)
            p = numbers[p_index]
            x = p ** 2
        except StopIteration:
            p = None
    primes = [x for i,x in enumerate(numbers) if not marked[i]]
    return primes

def sumOfPrimes(n):
    primes = primeNumbers(n)
    return sum(primes)