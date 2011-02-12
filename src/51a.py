import gmpy
import re

primes = [x for x in range(1000000) if gmpy.is_prime(x)]
solns = []
p = '1***03'

def swap(s):
    if '*' not in s:
        if gmpy.is_prime(int(s)) > 0:
            solns.append(s)
        return
    for i in range(10):
        swap(s.replace('*', str(i)))

#swap(p) 
#print(solns, len(solns))

select_primes = [x for x in primes if len(str(x)) == 6 and str(x).count('1') >= 2]
for x in select_primes:
    #print(x)
    p = str(x).replace('1', '*')
    solns = []
    swap(p)
    if len(solns) >= 8:
        print(sorted(solns))
