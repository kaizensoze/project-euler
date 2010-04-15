import gmpy
import itertools

from gmpy import mpz, mpq

limit = 10
maxN = 0

"""
once n_count reaches million, we can assume
we've generated all unique n <= million using primes
"""
n_count = 0
primes = (gmpy.next_prime(n) for n in range(1, limit))
print(type(primes))
exit()

"""
we want to generate all unique n as quickly as possible.
to avoid duplicate factorizations, keep records of all
distinct prime combinations tried
"""
tried_combos = {}

""" n -> phi(n) """
pairs = {}

# generate primes
for n in range(1, limit):
    nextPrime =  gmpy.next_prime(n)
    primes.append(nextPrime)
primes = sorted(set(primes))

def generateCombos(prime_list):
    #print('prime list: ', prime_list),
    combos = []
    for i in range(1, len(prime_list)+1):
        combos.extend(list(itertools.combinations(prime_list, i)))
    #print('combos: ', combos)
    return combos

def iterateToLimit(combo, choice):
    global n_count, limit
    k = 0
    gen = 1
    n_count += 1
    if n_count == limit - 1:
        print(maxN)
    # TODO: 
    #       for each choice, generate n's until >= limit
    #       for each n, create factors dict and use it to generate phi
    #       calculate n/phi and compare with max
    #       set max if appropriate
    #       increment n_count
    #       if n_count = limit-1, return max

def generateNUpToLimit(combo):
    #print(combo)
    choices = []
    increment_choices = [x for x in range(len(combo))]
    for i in range(1, len(increment_choices)+1):
        choices.extend(list(itertools.combinations(increment_choices, i)))
    #print(increment_choices)
    for choice in choices:
        iterateToLimit(combo, choice)

for prime in primes:
    upToPrime = [x for x in primes if x <= prime]
    combos = generateCombos(upToPrime)
    for combo in combos:
        if combo not in tried_combos:
            generateNUpToLimit(combo)
            tried_combos[combo] = True

"""
def primeFactorize(n):
    print('- '),
    prime = mpz(2)
    n = mpz(n)
    factors = {}
    while n >= prime:
        newn, mult = n.remove(prime)
        if mult:
            factors[prime] = mult
            n = newn
        prime = next_primes[prime]
    prime_factorizations[orign] = factors
    #print(factors)
    return factors

def phi(n):
    fac = primeFactorize(n)
    result = 1
    for factor in fac:
        result *= (factor-1) * (factor**(fac[factor]-1))
    return result
"""

