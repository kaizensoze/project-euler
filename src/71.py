'''
Created on Apr 22, 2009

@author: joeg
'''

reduced = []

def gcd(a,b):
    while a:
        a, b = b%a, a
    return b

#relativelyPrime = {}
#for d in range(1,1000000):
#    relativelyPrime[d] = [x for x in range(1,d) if gcd(x,d) == 1]
#    print(d, relativelyPrime[d])

#def reduce(s):
#    n,d = [int(x) for x in s.split('/')]
#    hcf = gcd(n,d)
#    if hcf == 1:
#        return (str(n) + '/' + str(d))
#    else:
#        while n % hcf == 0:
#            n = int(n / hcf)
#            d = int(d / hcf)
#    return (str(n) + '/' + str(d))

#print(reduce('24/256'))

for d in range(1,200):
    for n in [x for x in range(1,d) if gcd(x,d) == 1]:
        print(n,d)
        fraction = str(n) + '/' + str(d)
        if fraction not in reduced:
            reduced.append(fraction)

# sort reduced based on calculated values
def fractionCmp(s1, s2):
    n1, d1 = [int(x) for x in s1.split('/')]
    n2, d2 = [int(x) for x in s2.split('/')]
    
    return cmp( (n1/d1), (n2/d2) )


print(sorted(reduced, cmp=fractionCmp))

# find 3/7
# check numerator of fraction to left of 3/7