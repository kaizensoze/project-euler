'''
Created on Apr 1, 2009

@author: anon
'''
from decimal import *
from functools import reduce
from math import ceil, sqrt

def sumOfMultiples(divisors, limit):
    curr = 1
    sum = 0
    while curr < limit:
        for x in divisors:
            if curr % x == 0:
                sum += curr
                break
        curr = curr + 1            
    return sum

def sumOfFibonacciEven(limit):
    prev = curr = 1
    sum = 0
    while curr < limit:
        if curr % 2 == 0:
            sum += curr
        temp = curr
        curr = curr + prev
        prev = temp
    return sum

def fibonacciTerm(numDigits):
    count = 2
    prev = curr = 1
    while len(str(curr)) < numDigits:
        temp = curr
        curr = curr + prev
        prev = temp
        count = count + 1
    return count

def maxPrimeFactor(composite):
    largestPrimeFactor = 1
    for x in range(1, int(ceil(sqrt(composite)))):
        if composite % x == 0:
            if isPrime(x):
                largestPrimeFactor = x
    return largestPrimeFactor

def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def nthPrime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    curr = 20
    prime = True
        
    while len(primes) < n:
        for x in primes:
            if curr % x == 0:
                prime = False
                break
        if prime:
            primes.append(curr)
        curr = curr + 1
        prime = True
        
    return primes.pop()

def getPrimes(n):
    sieve = [True]*n  
    for x in range(4, n, 2):  
        sieve[x] = False  
    # any multiple of num above sqrt(n) is also a multiple of a  
    # lower prime, hence has already been eliminated  
    for num in range(3, int(sqrt(n)) + 1, 2):  
        if sieve[num]:
            for y in range(num**2, n, 2*num):  
                sieve[y] = False  
    result = [x for x in range(2, n) if sieve[x]]  
    return result  

def maxPalindromeProduct():
    a = 999
    b = 999
    maxPalindrome = 1
    
    for x in range(a, 1, -1):
        for y in range(b, 1, -1):
            p = x * y
            if isPalindrome(p) and p > maxPalindrome:
                maxPalindrome = p
    return maxPalindrome

def isPalindrome(n):
    s = str(n)
    length = len(s)
    left = 0
    right = length - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

def lcm(numbers):
    lcm = 1
    factorCounts = {}
    for x in numbers:
        factors = primeFactorize(x)
        for i in factors:
            if not factorCounts.has_key(i):
                factorCounts[i] = factors.count(i)
            elif factors.count(i) > factorCounts[i]:
                factorCounts[i] = factors.count(i)
    for k in factorCounts.iterkeys():
        lcm = lcm * (k ** factorCounts[k])
    return lcm

def triangleNumberWithNDivisors(numDivisors):
    x = 2
    triangle = 1
    
    while len(factorize(triangle)) < numDivisors:
        triangle = triangle + x
        x = x + 1
    
    return triangle

# refactored this to not allow duplicates
# not sure what effects this has on all
# pre-existing functions that use this
# in already solved projecteuler problems
def factorize(n, proper=False):
    x = 2
    factors = set([1])
    if n != 1 and not proper:
        factors.add(n)
    
    while x < n:
    
    return triangle

# refactored this to not allow duplicates
# not sure what effects this has on all
# pre-existing functions that use this
# in already solved projecteuler problems
# if proper==True, do not treat n as its own factor
def factorize(n, proper=False):
    x = 2
    factors = set([1])
    if n != 1 and not proper:
        factors.add(n)
    
    while x < n:
        if x in factors:
            break
        
        result = divmod(n,x)
        q = result[0]
        r = result[1]
        
        if r == 0:
            factors.add(q)
            factors.add(x)
        x = x + 1

    return factors

def primeFactorize2(n):
    val = n
    primes = []
    while val > 1:
        for x in range(1, val+1):
            if isPrime(x) and val % x == 0:
                val = int(val / x)
                primes.append(x)
                break    
    return primes

def sumOfSquares(n):
    return sum([x*x for x in n])

def squareOfSum(n):
    return sum([x for x in n]) ** 2

def maxConsecutiveProduct(n):
    s = n.split()
    maxProd = 1
    for x in s:
        for i in range(len(x)):
            if i + 5 < len(x):
                prod = reduce(lambda a,b: a*b, 
                              [int(y) for y in x[i:(i+5)]])
                if prod > maxProd:
                    maxProd = prod
    return maxProd
    
def sumOfPrimes(limit):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    curr = 21
    prime = True
        
    while curr < limit:
        #print(curr)
        for x in primes:
            if curr % x == 0:
                prime = False
                break
        if prime:
            primes.append(curr)
        curr = curr + 2
        prime = True
    return sum(primes)

def generatePythagoreanTriple(m, n):
    if not (m > n):
        return None
    return (2*m*n, m**2 - n**2, m**2 + n**2)

def generatePythagoreanTriples(desiredSum):
    for n in range(1,30):
        for m in range(n+1,30):
            triple = generatePythagoreanTriple(m,n)
            #print(triple)
            if sum(triple) == desiredSum:
                return triple
    return None

def getLongestHailstoneSeqGenSeed(limit):
    seedToSeqLenMapping = {1:1}
    maxSeqLen = 0
    maxSeqLenSeed = 0
    seed = 2
    
    while seed < limit:
        n = seed
        seqLen = 1

        while n > 1:
            if n % 2 == 0: # if even, n -> n/2
                if seedToSeqLenMapping.has_key(n/2):
                    seqLen = seedToSeqLenMapping[n/2] + seqLen
                    break
                else:
                    n = n/2
            elif n % 2 == 1: # if odd, n -> 3n+1
                if seedToSeqLenMapping.has_key(3*n+1):
                    seqLen = seedToSeqLenMapping[3*n+1] + seqLen
                    break
                else:
                    n = 3*n+1
            seqLen = seqLen + 1
        
        seedToSeqLenMapping[seed] = seqLen        
        if seqLen > maxSeqLen:
            maxSeqLen = seqLen
            maxSeqLenSeed = seed
        seed = seed + 1
                        
    return maxSeqLenSeed

def amicableNumbers(limit):
    amicableNumbers = []
    n = 1
    while n < limit:
        if n not in amicableNumbers:
            a = n
            b = sum(factorize(n, True))
            if sum(factorize(a, True)) == b and sum(factorize(b, True)) == a \
                    and a != b:
                amicableNumbers = amicableNumbers + [a, b]
        n = n + 1
    return amicableNumbers

def sumOfNonAbundantSums():    
    # get abundant numbers
    abundantNumbers = []
    for n in range(12,28123+1):
        if sum(factorize(n, True)) > n:
            abundantNumbers.append(n)
    
    all = set([x for x in range(28123+1)])
    abundantSums = set([])

    for x in abundantNumbers:
        for y in abundantNumbers:
            abundantSums.add(x+y)

    return sum(all.difference(abundantSums))


#def longestRecurringCycle(limit):
##    getcontext().prec = 100
#    longestCycle = [1,0]
#    repeatThreshold = 5
#    for d in range(2,limit):
#        cycleLen = 0        
#        q = str(Decimal(1)/Decimal(d))
#        if len(q) <= 3:
#            continue
#        q = q[0:-1]
#        
#        lastDigit = str(q)[-1]
#        lastDigitIndex = len(str(q)) - 1
#        matchingDigitIndex = str(q).rfind(lastDigit, 0,-1)
#        if matchingDigitIndex == -1:
#            continue
#        
#        matchingDigit = str(q)[matchingDigitIndex]
#        distance = lastDigitIndex - matchingDigitIndex
#        
#        if distance == 1:
#            continue
##            index = matchingDigitIndex
##            match = True
##            for i in range(repeatThreshold):
##                index = index - 1
##                if index >= 0 \
##                   and str(q)[index] != str(q)[matchingDigitIndex]:
##                    match = False                
##                
##            if match:
##                cycleLen = 1
#
#        elif distance > 1:
#            match = True
#            for i in range(distance):
#                lastDigitIndex = lastDigitIndex - 1
#                matchingDigitIndex = matchingDigitIndex - 1
#                if matchingDigitIndex >= 0 \
#                   and str(q)[matchingDigitIndex] != str(q)[lastDigitIndex]:
#                    match = False
#
#            if match:
#                cycleLen = distance
#                print('d=%s q=%s cycle=%s cycleLen=%s' \
#                      % (d, q, q[matchingDigitIndex:lastDigitIndex], cycleLen))
#        
#        if cycleLen > longestCycle[1]:
#            longestCycle[0] = d
#            longestCycle[1] = cycleLen
#    
#    return longestCycle[0]

def longestRecurringCycle(limit):
    num = 0
    max = 0
    for d in range(2,limit):
        for k in range(1,d):
            if 10**k % d == 1:
                if k > max:
                    max = k
                    num = d
                break
    return num

def factorial(n):
    if n <= 1:
        return 1
    else:
        return reduce(lambda x,y: x*y, [x for x in range(1,n+1)])

def rotate(n, x):
    if len(str(n)) == 1:
        return n
    
    digits = [int(x) for x in str(n)]
    for i in range(x):        
        digits.append(digits.pop(0))
                        
    return int(''.join([str(x) for x in digits]))
        
    
def numCircularPrimes(limit):
    circularPrimes = []
    n = 2
    while n < limit:
        prime = True
        n_orig = n
        for x in range(len(str(n_orig))):
            if not isPrime(n):
                prime = False
                break
            n = rotate(n_orig, x+1)
        if prime:
            circularPrimes.append(n_orig)
        n = n_orig + 1
        
    return len(circularPrimes)

def isPandigital(n):
    if len(set([int(x) for x in str(n)])) != len(str(n)):
        return False
    
    digits = [int(x) for x in str(n)]
    digits.sort()
    
    # for 1-9 pandigital only restriction
    if digits[0] != 1:
        return False
    
    for i,x in enumerate(digits):
        if i > 0 and digits[i] - digits[i-1] != 1:
    else:
        for x in permute(s[1:]):
            for i in range(len(x)+1):
                yield x[:i] + s[0] + x[i:]

def pentagonals():
    i = 1
    while 1:
        yield(pentagonal(i))
        i += 1

def pentagonal(x):
    return int((x * (3*x - 1)) / 2)
