import gmpy
import time
from gmpy import mpz, mpq

start = time.time()
primes = [x for x in range(1,1000000) if gmpy.is_prime(x)]
prod = 1
for prime in primes:
    if prod >= 1000000:
        break
    print(prod)
    print(prime)
    prod *= prime
end = time.time()
print('done in %.2f seconds' % (end-start))
# n = 510510
