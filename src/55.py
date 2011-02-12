'''
Created on Apr 10, 2009

@author: joeg
'''

lychrelCount = 0 
for n in range(1,10000):
    isPalindrome=False
    nCurr = n
    for i in range(50):
        nCurr = nCurr + int(str(nCurr)[::-1])
        if nCurr == int(str(nCurr)[::-1]):
            isPalindrome=True
            break
                        
    if not isPalindrome:
        lychrelCount = lychrelCount + 1

print(lychrelCount)