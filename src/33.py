'''
Created on Apr 16, 2009

@author: joeg
'''

for den in range(10,100):
    for num in range(10,den):
        trivial = True
        numDigits = [int(x) for x in str(num)]
        denDigits = [int(x) for x in str(den)]
        for x in numDigits:
            if x in denDigits:
                numDigits.remove(x)
                denDigits.remove(x)
                if x != 0:
                    trivial = False
        newNum = int(''.join([str(x) for x in numDigits]))
        newDen = int(''.join([str(x) for x in denDigits]))
        if den != 0 and newDen != 0 and num/den ==  newNum/newDen:
            if not trivial:
                print(num, den)

#387296                
#38729600