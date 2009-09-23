
from ProjectEulerLibrary import isPrime
from operator import itemgetter
from math import fabs

def identity(x):
    return ''.join([str(x) for x in sorted([int(i) for i in str(x)])])

def isPerm(x,y):
    return x != y and identity(x) == identity(y)

def constDiffCheck(x):
    count = 0
    diffDict = {}
    for y in x:
        for z in x:
            if y != z:
                diff = z - y
                if diff in diffDict.keys() \
                        and z in diffDict[diff]:
                    count += 1
                    if count >= 2:
                        print(diffDict)
                        return
                diffDict[diff] = (z,y)

def run():
    primes = set([x for x in range(1000, 9999+1) if isPrime(x)])
    primesByPerm = {}
    groups = []
    for x in primes:
        primesByPerm[x] = identity(x)

    for v in primesByPerm.values():
        blah = sorted([x for x in primesByPerm.keys() \
                                           if primesByPerm[x] == v])
        if blah not in groups:
            groups.append(blah)

    for x in groups:
        if len(x) >= 3:
            #print(x)
            constDiffCheck(x)
run()

