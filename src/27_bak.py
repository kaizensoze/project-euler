'''
Created on Apr 16, 2009

@author: joeg
'''
import math

def isprime(n,PROB):
    '''returns if the number is prime. Failure rate: 1/4**PROB '''
    if n==2: return '1'
    if n==1 or n&1==0:return '0'
    s=0
    d=n-1
    while 1&d==0:
        s+=1
        d>>=1
    for i in range(PROB):
        a=random.randint(2,n-1)
        composit=True
        if pow(a,d,n)==1:
            composit=False
        if composit:
            for r in xrange(0,s):
                if pow(a,d*2**r,n)==n-1:
                    composit=False
                    break
        if composit: return False
    return True

# n² + an + b, where |a| < 1000 and |b| < 1000
for n in range(1000):
    for a in range(-999,999+1):        
        for b in range(-999,999+1):
            
        