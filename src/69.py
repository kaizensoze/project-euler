from ProjectEulerLibrary import primeFactorize, factorize, gcd

max = 0
maxN = -1
phis = {}

def calculatePhi(n):
    factors = primeFactorize(n)
    phi = n
    for factor in set(factors):
        phi *= (1 - 1/factor)
    print('- ', end='')
    return phi

for n in range(2, 40000):
    phi = None
    factors = factorize(n, True)
    for i in factors:
        for j in factors:
            if i == j:
                continue
            if i*j == n and gcd(i,j) == 1:
                phi = phis[i]*phis[j]
                print('+ ', end='')
                break
        if phi != None:
            break
    if phi == None:
        phi = calculatePhi(n)
                
    phis[n] = phi
    val = n/phi
    print('n=%d  phi=%d  n/phi=%f' % (n,phi,val))
    if val > max:
        max = val
        maxN = n

print('%d (%f)' % (maxN, max))

# 30000-40000 => 30030 (5.213542)
# 40000-50000 => lower
