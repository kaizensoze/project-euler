'''
Created on Apr 17, 2009

@author: joeg
''' 

maxCount = 0
maxP = 0

for p in range(3,1000+1):
    count = 0
    for a in range(1,p):
        for b in range(1,(p-a)):
            c = p - b - a
            
            if (a + b + c == p) \
                and (a**2 + b**2 == c**2) \
                and (a < b < c):
                count = count + 1
                if count > maxCount:
                    maxP = p
                print(p, " ", a, b, c)

print(maxP)