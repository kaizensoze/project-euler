"""
Find smallest prime, by replacing part of the number with same digit, is part of 8 prime family.
"""

import itertools

def generateCombos(nlist):
    combos = []
    for i in range(1, len(nlist)+1):
        combos.extend(list(itertools.combinations(nlist, i)))
    return combos

n = 100

while 1:
    for combo in generateCombos(range(len(str(n)))):
        prime_family = []
        for i in range(0,9+1):
            temp = [int(x) for x in str(n)]
            for c in combo:
                temp[c] = i
            reconstructed = int(''.join([str(x) for x in temp]))
            if putback in primes
                prime_family.append(number)
        if len(prime_family) == 8:
            print(sorted(prime_family)[0])
            exit()
