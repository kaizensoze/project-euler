import gmpy

from gmpy import mpz, mpq

next_primes = {}
primes = []
prime_factorizations = {}

# generate primes
for n in range(1, 1000000):
    nextPrime =  gmpy.next_prime(n)
    next_primes[n] = nextPrime
    primes.append(nextPrime)

primes = sorted(set(primes))

def primeFactorize(n):
    orign = n
    # use memoized value if possible
    for prime in primes:
        if prime >= n:
            break
        cached_n,check = divmod(mpz(n), prime)
        if check != 0:
            continue
        if cached_n in prime_factorizations:
            factors = prime_factorizations[cached_n]
            if prime in factors:
                factors[prime] += 1
            else:
                factors[prime] = 1
            prime_factorizations[n] = factors
            print('+ '),
            #print(factors)
            return factors
    
    # otherwise:
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

max = 0
maxN = 0

for n in range(2, 1000000):
    phi_val = phi(n)
    val = n/mpq(phi_val)

    print('%d  ' % n),
    print('%d  ' % phi_val),
    print('%f' % val)

    if val > max:
        max = val
        maxN = n

print(maxN),
print(max)
