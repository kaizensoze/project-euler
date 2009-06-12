'''
Created on Apr 17, 2009

@author: joeg
'''

oneOnlyCount = 0

for p in range(3,2000000+1):
    count = 0
    moreThanOne = False
    for a in range(1,p):
#        if moreThanOne == True:
#            break
        for b in range(1,(p-a)):
#            if moreThanOne == True:
#                break
            c = p - b - a
            
            if (a + b + c == p) \
                and (a**2 + b**2 == c**2) \
                and (a < b < c):
                count = count + 1
#                if count > 1:
#                    moreThanOne = True
                print(p, " ", a, b, c)
            if count > 1:
                break
        if count > 1:
            break
    if count == 1:
        oneOnlyCount = oneOnlyCount + 1

print(oneOnlyCount)