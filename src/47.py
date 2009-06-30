'''
Created on Jun 14, 2009

@author: anon
'''
from ProjectEulerLibrary import primeFactorize

numPrimeFactors = 4
#consec_numbers = []
#consec_factorizations = []
candidates = []


for x in range(130000,150000):
    prime_factors = set(primeFactorize(x))
    if len(prime_factors) == numPrimeFactors:
        candidates.append(x)
        print(x)


# now look for 4 consecutive numbers in the list of candidates 
# with 4 distinct prime factors
#print(candidates)
consec_count = 0

for i,x in enumerate(candidates):
    if candidates[i] == (candidates[i-1] + 1):
        consec_count += 1
        if consec_count == 4:
            print(candidates[i-3])
            break
    else:
        consec_count = 0


#x = 210
#while True:
#    prime_factors = set(primeFactorize(x))
#    if len(prime_factors) == numPrimeFactors:
#           consec_count += 1
#           consec_numbers.append(x)
#           consec_factorizations.append(prime_factors)
#           print(x)
#    else:
#        consec_numbers = []
#        consec_factorizations = []
#        consec_count = 0
#
#    if consec_count == numPrimeFactors:
#        break
#    x += 1
#    print(x)
    
#print(consec_numbers)
#print(consec_factorizations)
