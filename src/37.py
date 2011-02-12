'''
Created on Apr 17, 2009

@author: anon
'''
from ProjectEulerLibrary import isPrime

truncatablePrimes = []

for n in range(10,740000+1):
    if isPrime(n):
        prime = True
        for x in range(len(str(n))):
            left = [int(y) for y in str(n)]
            right = [int(y) for y in str(n)]
            
            for y in range(x+1):
                left.pop(0)
                right.pop(-1)
            
            if len(left) == 0 or len(right) == 0:
                break
            
            if len(left) == 1:
                left = left[0]
            else:
                left = int(''.join([str(y) for y in left]))
                
            if len(right) == 1:
                right = right[0]
            else:
                right = int(''.join([str(y) for y in right]))                
            
            if not isPrime(left) or not isPrime(right):
                prime = False
        if prime:
            truncatablePrimes.append(n)

print(truncatablePrimes)
print(sum(truncatablePrimes))