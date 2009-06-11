'''
Created on Apr 24, 2009

@author: anon
'''

def lastNDigits(a,b,n):
    while b > 0:
        x = a * 2
        if len(str(x)) > n:
            a = int(str(x)[1:])
        else:
            a = x
        b = b - 1
    return a

print(lastNDigits(28433, 7830457, 10)+1)
#print(lastNDigits(34, 12, 3))
#print(lastNDigits(568, 8, 4))
