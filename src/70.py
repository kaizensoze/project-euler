#!/usr/bin/python

import gmpy
import sys
from itertools import product
from itertools import permutations
from operator import itemgetter
from collections import defaultdict
from operator import mul
from time import time

phi_results = {}

def prime_factors(x):
    prime = gmpy.mpz(2)
    x = gmpy.mpz(x)
    factors = {}
    while x >= prime:
        newx, mult = x.remove(prime)
        if mult:
            factors[prime] = mult
            x = newx
        prime = prime.next_prime()
    return factors

def phi(x):
    print(x)
    global phi_results

    if gmpy.is_prime(x):
        return x-1

    fac = prime_factors(x)
    result = int( x * reduce(mul, [(1-1.0/p) for p in fac]) )
    return result

"""
t1 = time()
#print(phi(2310))
for n in range(3,10000000):
    print(n)
    phi_results[n] = phi(n)
t2 = time()
print(t2-t1)

n = 87109
phi = 79180
a = tuple([x for x in str(n)])
b = [p for p in permutations([y for y in str(phi)])]
print(a in b)
sys.exit(0)

soln = []
p = [x for x in range(6000) if gmpy.is_prime(x)]
for pair in product(p,p):
    p1 = pair[0]
    p2 = pair[1]
    if p1 != p2:
        n = p1 * p2
        phi = (p1-1)*(p2-1)
        div = 1.0*n/phi
        soln.append( (n, phi, div) )

soln = sorted(soln, key=itemgetter(2))
for s in soln:
    n = s[0]
    phi = s[1]
    a = tuple([x for x in str(n)])
    b = [p for p in permutations([y for y in str(phi)])]
    if a in b:
        print(n)
"""
