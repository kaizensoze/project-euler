import gmpy

from gmpy import mpz, mpq
from ProjectEulerLibrary import primeFactorize, phi, factorize, gcd


max = 0
maxN = 0

phi_cache = {}

for n in range(2, 1000000):
    #phi_val = mpz(-1)
    #factors = factorize(n, True)
    #for i in factors:
    #    for j in factors:
    #        if i == j:
    #            continue
    #        if i*j == n and gcd(i,j) == 1:
    #            phi_val = phi_cache[i]*phi_cache[j]
    #            print('+ '),
    #            break
    #    if int(phi_val) != -1:
    #        break
    #if int(phi_val) == -1:
    #    print('- '),
    phi_val = phi(n)

    #phi_cache[n] = phi_val
    val = n/mpq(phi_val)

    print('%d  ' % n),
    print('%d  ' % phi_val),
    print('%f' % val)

    if val > max:
        max = val
        maxN = n

print(maxN),
print(max)
